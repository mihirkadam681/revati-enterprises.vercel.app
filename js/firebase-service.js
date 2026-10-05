// REVATI ENTERPRISES - Firebase Cloud Firestore & Authentication Service
// Seamless Real-Time Cloud Synchronization & Offline Fallback Layer

// Default Firebase Project Configuration for Revati Enterprises
const DEFAULT_FIREBASE_CONFIG = {
    apiKey: "AIzaSyAOZJf89jiisnUX5kTNVbZaZZ2YSPHVZCE",
    authDomain: "revati-enterprises-178f1.firebaseapp.com",
    projectId: "revati-enterprises-178f1",
    storageBucket: "revati-enterprises-178f1.firebasestorage.app",
    messagingSenderId: "71519014879",
    appId: "1:71519014879:web:c6273a981300784f7ffe6a",
    measurementId: "G-M2W9L56X7T"
};

class FirebaseService {
    constructor() {
        this.app = null;
        this.db = null;
        this.auth = null;
        this.analytics = null;
        this.isReady = false;
        this.listeners = {};
        this.statusListeners = [];
        this.status = 'unconfigured'; // 'unconfigured', 'connected', 'error', 'connecting'

        // Check for stored Firebase Config in localStorage or default fallback
        this.config = this.loadConfig();

        // Auto-initialize if config exists
        if (this.config && this.config.projectId && this.config.apiKey) {
            if (typeof firebase !== 'undefined') {
                this.initFirebase(this.config);
            } else {
                // If scripts load asynchronously or before DOM ready
                window.addEventListener('DOMContentLoaded', () => {
                    if (typeof firebase !== 'undefined' && !this.isReady) {
                        this.initFirebase(this.config);
                    }
                });
            }
        }
    }

    loadConfig() {
        try {
            const saved = localStorage.getItem('revati_firebase_config');
            if (saved) {
                const parsed = JSON.parse(saved);
                if (parsed && parsed.apiKey && parsed.projectId === DEFAULT_FIREBASE_CONFIG.projectId) {
                    return parsed;
                }
            }
        } catch (e) {
            console.warn('Failed to parse saved Firebase config', e);
        }

        // Save and return project default credentials
        try {
            localStorage.setItem('revati_firebase_config', JSON.stringify(DEFAULT_FIREBASE_CONFIG));
        } catch (e) { }
        return { ...DEFAULT_FIREBASE_CONFIG };
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

    getAuth() {
        if (this.auth) return this.auth;
        if (typeof firebase !== 'undefined' && typeof firebase.auth === 'function') {
            try {
                this.auth = firebase.auth();
                return this.auth;
            } catch (e) {
                console.warn('[FirebaseService] getAuth fallback notice:', e);
            }
        }
        return null;
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
            this.isReady = true;
            this.updateStatus('connected');
            console.log('[FirebaseService] Successfully initialized Firebase Cloud Firestore & Auth');

            // Initialize Analytics if supported
            if (typeof firebase.analytics === 'function' && config.measurementId) {
                try {
                    this.analytics = firebase.analytics();
                } catch (e) {
                    console.warn('[FirebaseService] Analytics notice:', e);
                }
            }

            // Enable offline persistence in background (non-blocking)
            if (this.db && typeof this.db.enablePersistence === 'function') {
                this.db.enablePersistence({ synchronizeTabs: true }).catch(err => {
                    console.warn('[FirebaseService] Firestore persistence notice:', err.message || err.code);
                });
            }

            return true;
        } catch (err) {
            console.error('[FirebaseService] Initialization Error:', err);
            if (typeof firebase !== 'undefined' && typeof firebase.auth === 'function') {
                try { this.auth = firebase.auth(); } catch (e) { }
            }
            this.isReady = false;
            this.updateStatus('error', err.message);
            return false;
        }
    }

    isInitialized() {
        return (this.isReady && this.db !== null) || (this.auth !== null);
    }

    // --- CUSTOMER & CLIENT AUTHENTICATION (EMAIL/PASSWORD + GOOGLE) ---

    async signInWithEmail(email, password) {
        const auth = this.getAuth();
        if (!auth) throw new Error("Firebase Auth is connecting, please click again in a moment.");
        const cred = await auth.signInWithEmailAndPassword(email, password);
        return cred.user;
    }

    async signUpWithEmail(email, password, displayName = '', phone = '') {
        const auth = this.getAuth();
        if (!auth) throw new Error("Firebase Auth is connecting, please click again in a moment.");
        const cred = await auth.createUserWithEmailAndPassword(email, password);
        const user = cred.user;
        if (displayName && user && typeof user.updateProfile === 'function') {
            try {
                await user.updateProfile({ displayName: displayName });
            } catch (e) {
                console.warn('[FirebaseService] updateProfile notice:', e);
            }
        }
        try {
            await this.setDocument('customers', {
                id: user.uid,
                uid: user.uid,
                name: displayName || email.split('@')[0],
                email: email,
                phone: phone,
                role: 'CUSTOMER',
                provider: 'password',
                createdAt: new Date().toISOString()
            });
        } catch (e) {
            console.warn('[FirebaseService] Customer Firestore record notice:', e);
        }
        return user;
    }

    async signInWithGoogle() {
        const auth = this.getAuth();
        if (!auth) throw new Error("Firebase Auth is connecting, please click again in a moment.");
        const provider = new firebase.auth.GoogleAuthProvider();
        provider.setCustomParameters({ prompt: 'select_account' });
        const result = await auth.signInWithPopup(provider);
        const user = result.user;
        if (user) {
            try {
                await this.setDocument('customers', {
                    id: user.uid,
                    uid: user.uid,
                    name: user.displayName || user.email.split('@')[0],
                    email: user.email,
                    photoURL: user.photoURL || '',
                    role: 'CUSTOMER',
                    provider: 'google',
                    lastLogin: new Date().toISOString()
                });
            } catch (e) {
                console.warn('[FirebaseService] Customer Google record notice:', e);
            }
        }
        return user;
    }

    async sendPasswordReset(email) {
        const auth = this.getAuth();
        if (!auth) throw new Error("Firebase Auth is connecting, please try again in a moment.");
        await auth.sendPasswordResetEmail(email);
        return true;
    }

    async signOut() {
        const auth = this.getAuth();
        if (auth) {
            await auth.signOut();
            localStorage.removeItem('revati_customer_session');
        }
    }

    onAuthStateChanged(callback) {
        const auth = this.getAuth();
        if (auth) {
            return auth.onAuthStateChanged(callback);
        } else {
            const checkInterval = setInterval(() => {
                const a = this.getAuth();
                if (a) {
                    clearInterval(checkInterval);
                    return a.onAuthStateChanged(callback);
                }
            }, 100);
        }
    }

    getCurrentUser() {
        const auth = this.getAuth();
        return auth ? auth.currentUser : null;
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
