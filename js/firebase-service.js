// REVATI ENTERPRISES - Firebase Cloud Firestore & Authentication Service
// Seamless Real-Time Cloud Synchronization & Offline Fallback Layer

class FirebaseService {
    constructor() {
        this.app = null;
        this.db = null;
        this.auth = null;
        this.isReady = false;
        this.listeners = {};
        this.statusListeners = [];
        this.status = 'unconfigured'; // 'unconfigured', 'connected', 'error', 'connecting'

        // Check for stored Firebase Config in localStorage or default fallback
        this.config = this.loadConfig();
        
        // Auto-initialize if config exists
        if (this.config && this.config.projectId && this.config.apiKey) {
            this.initFirebase(this.config);
        }
    }

    loadConfig() {
        try {
            const saved = localStorage.getItem('revati_firebase_config');
            if (saved) return JSON.parse(saved);
        } catch (e) {
            console.warn('Failed to parse saved Firebase config', e);
        }
        return null;
    }

    saveConfig(config) {
        localStorage.setItem('revati_firebase_config', JSON.stringify(config));
        this.config = config;
        return this.initFirebase(config);
    }

    clearConfig() {
        localStorage.removeItem('revati_firebase_config');
        this.config = null;
        this.isReady = false;
        this.db = null;
        this.auth = null;
        this.updateStatus('unconfigured');
    }

    updateStatus(newStatus, detail = '') {
        this.status = newStatus;
        console.log(`[FirebaseService] Status: ${newStatus} ${detail ? '(' + detail + ')' : ''}`);
        this.statusListeners.forEach(fn => fn(newStatus, detail));
    }

    onStatusChange(callback) {
        if (typeof callback === 'function') {
            this.statusListeners.push(callback);
            callback(this.status);
        }
    }

    async initFirebase(config) {
        this.updateStatus('connecting');
        try {
            if (typeof firebase === 'undefined') {
                console.warn('[FirebaseService] Firebase SDK scripts not loaded yet.');
                this.updateStatus('unconfigured', 'Firebase SDK scripts missing');
                return false;
            }

            if (!firebase.apps.length) {
                this.app = firebase.initializeApp(config);
            } else {
                this.app = firebase.app();
            }

            this.db = firebase.firestore();
            this.auth = firebase.auth();

            // Enable offline persistence if available
            try {
                await this.db.enablePersistence({ synchronizeTabs: true });
            } catch (err) {
                if (err.code === 'failed-precondition') {
                    console.warn('[FirebaseService] Firestore persistence failed: Multiple tabs open');
                } else if (err.code === 'unimplemented') {
                    console.warn('[FirebaseService] Firestore persistence not supported by browser');
                }
            }

            this.isReady = true;
            this.updateStatus('connected');
            console.log('[FirebaseService] Successfully initialized Firebase Cloud Firestore & Auth');
            return true;
        } catch (err) {
            console.error('[FirebaseService] Initialization Error:', err);
            this.isReady = false;
            this.updateStatus('error', err.message);
            return false;
        }
    }

    isInitialized() {
        return this.isReady && this.db !== null;
    }

    // --- FIRESTORE CRUD OPERATIONS ---

    // Fetch entire collection
    async getCollection(collectionName) {
        if (!this.isInitialized()) return null;
        try {
            const snapshot = await this.db.collection(collectionName).get();
            const items = [];
            snapshot.forEach(doc => {
                items.push({ _docId: doc.id, ...doc.data() });
            });
            return items;
        } catch (err) {
            console.error(`[FirebaseService] Error fetching collection ${collectionName}:`, err);
            throw err;
        }
    }

    // Set/Add Document (Uses custom item.id or auto-generated doc ID)
    async setDocument(collectionName, item) {
        if (!this.isInitialized()) return null;
        try {
            const docId = item.id ? String(item.id) : this.db.collection(collectionName).doc().id;
            const docRef = this.db.collection(collectionName).doc(docId);
            const payload = { ...item, updatedAt: firebase.firestore.FieldValue.serverTimestamp() };
            await docRef.set(payload, { merge: true });
            return { _docId: docId, ...payload };
        } catch (err) {
            console.error(`[FirebaseService] Error saving document to ${collectionName}:`, err);
            throw err;
        }
    }

    // Update Document
    async updateDocument(collectionName, id, updateData) {
        if (!this.isInitialized()) return null;
        try {
            const docRef = this.db.collection(collectionName).doc(String(id));
            const payload = { ...updateData, updatedAt: firebase.firestore.FieldValue.serverTimestamp() };
            await docRef.update(payload);
            return true;
        } catch (err) {
            console.error(`[FirebaseService] Error updating document ${id} in ${collectionName}:`, err);
            throw err;
        }
    }

    // Delete Document
    async deleteDocument(collectionName, id) {
        if (!this.isInitialized()) return null;
        try {
            await this.db.collection(collectionName).doc(String(id)).delete();
            return true;
        } catch (err) {
            console.error(`[FirebaseService] Error deleting document ${id} from ${collectionName}:`, err);
            throw err;
        }
    }

    // Real-Time Live Snapshot Listener
    subscribeCollection(collectionName, onUpdate) {
        if (!this.isInitialized()) return null;
        
        // Unsubscribe existing listener if present
        if (this.listeners[collectionName]) {
            this.listeners[collectionName]();
        }

        try {
            const unsubscribe = this.db.collection(collectionName).onSnapshot(snapshot => {
                const items = [];
                snapshot.forEach(doc => {
                    items.push({ _docId: doc.id, ...doc.data() });
                });
                onUpdate(items);
            }, err => {
                console.error(`[FirebaseService] Realtime listener error for ${collectionName}:`, err);
            });

            this.listeners[collectionName] = unsubscribe;
            return unsubscribe;
        } catch (err) {
            console.error(`[FirebaseService] Failed to subscribe to ${collectionName}:`, err);
            return null;
        }
    }

    // Seed Initial Data to Firestore if empty
    async seedInitialDataIfEmpty(initialData) {
        if (!this.isInitialized()) return;
        try {
            for (const [collName, items] of Object.entries(initialData)) {
                if (Array.isArray(items) && items.length > 0) {
                    const snap = await this.db.collection(collName).limit(1).get();
                    if (snap.empty) {
                        console.log(`[FirebaseService] Seeding initial data for ${collName}...`);
                        const batch = this.db.batch();
                        items.forEach(item => {
                            const docId = item.id ? String(item.id) : this.db.collection(collName).doc().id;
                            const docRef = this.db.collection(collName).doc(docId);
                            batch.set(docRef, item);
                        });
                        await batch.commit();
                        console.log(`[FirebaseService] Seeding completed for ${collName}`);
                    }
                }
            }
        } catch (err) {
            console.warn('[FirebaseService] Error seeding initial data:', err);
        }
    }
}

// Global Singleton Instance
const firebaseService = new FirebaseService();
window.firebaseService = firebaseService;
