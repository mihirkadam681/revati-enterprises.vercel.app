// REVATI ENTERPRISES - JWT Security & API Client Service Layer

const API_BASE_URL = 'http://localhost:8080/api';

// Role Permissions Matrix
const ROLE_PERMISSIONS = {
    ADMIN: {
        title: 'Company Administrator',
        allowedViews: ['dashboard', 'employees', 'staff-directory', 'leaves', 'org-hierarchy', 'housekeeping', 'maintenance', 'inventory', 'reports', 'users', 'admin-panel', 'letterhead'],
        canRegisterEmployee: true,
        canAssignTask: true,
        canLodgeComplaint: true,
        canAddInventory: true,
        canManageUsers: true,
        canMarkAttendance: true,
        canInspectTask: true,
        canResolveComplaint: true,
        canManageLeaves: true,
        badgeClass: 'badge-gold'
    },
    MANAGEMENT: {
        title: 'Client & Facility Customer',
        allowedViews: ['dashboard', 'org-hierarchy', 'housekeeping', 'maintenance', 'reports', 'letterhead'],
        canRegisterEmployee: false,
        canAssignTask: false,
        canLodgeComplaint: true,
        canAddInventory: false,
        canManageUsers: false,
        canMarkAttendance: false,
        canInspectTask: false,
        canResolveComplaint: false,
        canManageLeaves: false,
        badgeClass: 'badge-info'
    },
    SUPERVISOR: {
        title: 'Operations Supervisor',
        allowedViews: ['dashboard', 'employees', 'staff-directory', 'leaves', 'org-hierarchy', 'housekeeping', 'maintenance', 'inventory', 'reports', 'letterhead'],
        canRegisterEmployee: true,
        canAssignTask: true,
        canLodgeComplaint: true,
        canAddInventory: true,
        canManageUsers: false,
        canMarkAttendance: true,
        canInspectTask: true,
        canResolveComplaint: true,
        canManageLeaves: true,
        badgeClass: 'badge-gold'
    },
    CLIENT: {
        title: 'Client & Facility Customer',
        allowedViews: ['dashboard', 'org-hierarchy', 'housekeeping', 'maintenance', 'reports', 'letterhead'],
        canRegisterEmployee: false,
        canAssignTask: false,
        canLodgeComplaint: true,
        canAddInventory: false,
        canManageUsers: false,
        canMarkAttendance: false,
        canInspectTask: false,
        canResolveComplaint: false,
        badgeClass: 'badge-info'
    }
};

class ApiService {
    constructor() {
        this.useLocalStorageFallback = true;
        this.initStorage();
    }

    initStorage() {
        if (!localStorage.getItem('hk_data_v1')) {
            localStorage.setItem('hk_data_v1', JSON.stringify(INITIAL_DATA));
        }
        if (!localStorage.getItem('hk_current_user')) {
            localStorage.setItem('hk_current_user', JSON.stringify(INITIAL_DATA.users[0])); // Admin by default
        }
    }

    getToken() {
        return localStorage.getItem('hk_jwt_token') || '';
    }

    setToken(token) {
        if (token) localStorage.setItem('hk_jwt_token', token);
        else localStorage.removeItem('hk_jwt_token');
    }

    getLocalData() {
        return JSON.parse(localStorage.getItem('hk_data_v5')) || INITIAL_DATA;
    }

    saveLocalData(data) {
        localStorage.setItem('hk_data_v5', JSON.stringify(data));
    }

    getCurrentUser() {
        return JSON.parse(localStorage.getItem('hk_current_user')) || INITIAL_DATA.users[0];
    }

    setCurrentUser(user) {
        localStorage.setItem('hk_current_user', JSON.stringify(user));
    }

    getPermissions() {
        const user = this.getCurrentUser();
        return ROLE_PERMISSIONS[user.role] || ROLE_PERMISSIONS.STAFF;
    }

    async login(username, password) {
        try {
            const response = await fetch(`${API_BASE_URL}/auth/login`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ username, password })
            });
            const data = await response.json();
            if (response.ok && data.success) {
                this.setToken(data.token);
                this.setCurrentUser(data.user);
                return { success: true, user: data.user, token: data.token };
            }
        } catch (e) {
            console.warn('Java server login failed, matching fallback database');
        }

        // Firebase Cloud Firestore User Check
        if (window.firebaseService && window.firebaseService.isInitialized()) {
            try {
                const fbUsers = await window.firebaseService.getCollection('users');
                if (fbUsers && fbUsers.length > 0) {
                    const matchedFb = fbUsers.find(u => (u.username || '').toLowerCase() === username.toLowerCase());
                    if (matchedFb) {
                        const token = "fb_jwt_token_" + Date.now();
                        this.setToken(token);
                        this.setCurrentUser(matchedFb);
                        return { success: true, user: matchedFb, token: token };
                    }
                }
            } catch (err) {
                console.warn('Firebase login lookup error:', err);
            }
        }

        // Local Fallback Login Check
        const localUsers = this.getLocalData().users;
        const matched = localUsers.find(u => u.username.toLowerCase() === username.toLowerCase());
        if (matched) {
            const mockToken = "mock_jwt_token_" + Date.now();
            this.setToken(mockToken);
            this.setCurrentUser(matched);
            return { success: true, user: matched, token: mockToken };
        }

        return { success: false, message: 'Invalid username or password credentials.' };
    }

    logout() {
        this.setToken('');
        localStorage.removeItem('hk_current_user');
    }

    async checkBackendHealth() {
        try {
            const response = await fetch(`${API_BASE_URL}/health`, { method: 'GET' });
            if (response.ok) {
                this.useLocalStorageFallback = false;
                return true;
            }
        } catch (e) {
            this.useLocalStorageFallback = true;
        }
        return false;
    }

    async request(endpoint, method = 'GET', body = null) {
        // 1. Check Firebase Cloud Firestore Integration
        if (window.firebaseService && window.firebaseService.isInitialized()) {
            try {
                const fbResult = await this.handleFirebaseRequest(endpoint, method, body);
                if (fbResult !== null && fbResult !== undefined) {
                    return fbResult;
                }
            } catch (err) {
                console.warn('[ApiService] Firestore request failed, using local fallback.', err);
            }
        }

        // 2. Check Java Server Backend
        try {
            const isServerUp = await this.checkBackendHealth();
            if (isServerUp) {
                const token = this.getToken();
                const headers = { 'Content-Type': 'application/json' };
                if (token) headers['Authorization'] = `Bearer ${token}`;

                const options = { method, headers };
                if (body) options.body = JSON.stringify(body);

                const res = await fetch(`${API_BASE_URL}${endpoint}`, options);
                if (res.ok) {
                    const serverResult = await res.json();
                    if (method === 'POST' || method === 'PUT') {
                        this.handleLocalRequest(endpoint, method, serverResult);
                    }
                    return serverResult;
                }
            }
        } catch (err) {
            console.warn('Backend server request error, using local storage fallback.', err);
        }

        // 3. Local Storage Fallback
        return this.handleLocalRequest(endpoint, method, body);
    }

    async handleFirebaseRequest(endpoint, method, body) {
        const fb = window.firebaseService;
        const localData = this.getLocalData();

        if (endpoint === '/employees') {
            if (method === 'GET') {
                const items = await fb.getCollection('employees');
                if (items && items.length > 0) {
                    localData.employees = items;
                    this.saveLocalData(localData);
                    return items;
                }
                return localData.employees || [];
            }
            if (method === 'POST') {
                const newEmp = { id: Date.now(), ...body, status: 'Active', efficiency: 90 };
                await fb.setDocument('employees', newEmp);
                localData.employees = (localData.employees || []).filter(e => e.id !== newEmp.id && (e.name || '').trim().toLowerCase() !== (newEmp.name || '').trim().toLowerCase());
                localData.employees.unshift(newEmp);
                this.saveLocalData(localData);
                return newEmp;
            }
            if (method === 'PUT') {
                await fb.setDocument('employees', body);
                const index = (localData.employees || []).findIndex(e => e.id === body.id);
                if (index !== -1) {
                    localData.employees[index] = { ...localData.employees[index], ...body };
                } else {
                    localData.employees.unshift(body);
                }
                this.saveLocalData(localData);
                return body;
            }
            if (method === 'DELETE') {
                await fb.deleteDocument('employees', body.id);
                localData.employees = (localData.employees || []).filter(e => e.id !== body.id);
                this.saveLocalData(localData);
                return { success: true };
            }
        }

        if (endpoint === '/tasks') {
            if (method === 'GET') {
                const items = await fb.getCollection('tasks');
                if (items && items.length > 0) {
                    localData.tasks = items;
                    this.saveLocalData(localData);
                    return items;
                }
                return localData.tasks || [];
            }
            if (method === 'POST') {
                const newTask = {
                    id: Date.now(),
                    taskCode: 'REV-HK' + Math.floor(100 + Math.random() * 900),
                    date: new Date().toISOString().split('T')[0],
                    status: 'Pending',
                    inspectedBy: 'Pending',
                    ...body
                };
                await fb.setDocument('tasks', newTask);
                localData.tasks.unshift(newTask);
                this.saveLocalData(localData);
                return newTask;
            }
            if (method === 'PUT') {
                await fb.setDocument('tasks', body);
                const index = localData.tasks.findIndex(t => t.id === body.id);
                if (index !== -1) {
                    localData.tasks[index] = { ...localData.tasks[index], ...body };
                    this.saveLocalData(localData);
                    return localData.tasks[index];
                }
            }
        }

        if (endpoint === '/complaints') {
            if (method === 'GET') {
                const items = await fb.getCollection('complaints');
                if (items && items.length > 0) {
                    localData.complaints = items;
                    this.saveLocalData(localData);
                    return items;
                }
                return localData.complaints || [];
            }
            if (method === 'POST') {
                const newTicket = {
                    id: Date.now(),
                    ticketNo: 'REV-MNT' + Math.floor(900 + Math.random() * 99),
                    reportedDate: new Date().toLocaleString(),
                    status: 'Pending',
                    resolution: 'Under inspection',
                    ...body
                };
                await fb.setDocument('complaints', newTicket);
                localData.complaints.unshift(newTicket);
                this.saveLocalData(localData);
                return newTicket;
            }
            if (method === 'PUT') {
                await fb.setDocument('complaints', body);
                const index = localData.complaints.findIndex(c => c.id === body.id);
                if (index !== -1) {
                    localData.complaints[index] = { ...localData.complaints[index], ...body };
                    this.saveLocalData(localData);
                    return localData.complaints[index];
                }
            }
        }

        if (endpoint === '/inventory') {
            if (method === 'GET') {
                const items = await fb.getCollection('inventory');
                if (items && items.length > 0) {
                    localData.inventory = items;
                    this.saveLocalData(localData);
                    return items;
                }
                return localData.inventory || [];
            }
            if (method === 'POST') {
                const newItem = {
                    id: Date.now(),
                    itemCode: 'REV-INV' + String((localData.inventory || []).length + 1).padStart(2, '0'),
                    status: body.quantity <= body.reorderLevel ? 'Low Stock' : 'In Stock',
                    ...body
                };
                await fb.setDocument('inventory', newItem);
                localData.inventory.unshift(newItem);
                this.saveLocalData(localData);
                return newItem;
            }
            if (method === 'PUT') {
                await fb.setDocument('inventory', body);
                const index = localData.inventory.findIndex(i => i.id === body.id);
                if (index !== -1) {
                    localData.inventory[index] = { ...localData.inventory[index], ...body };
                    localData.inventory[index].status = localData.inventory[index].quantity <= localData.inventory[index].reorderLevel ? 'Low Stock' : 'In Stock';
                    this.saveLocalData(localData);
                    return localData.inventory[index];
                }
            }
        }

        if (endpoint === '/attendance') {
            if (method === 'GET') {
                const items = await fb.getCollection('attendance');
                if (items && items.length > 0) {
                    localData.attendance = items;
                    this.saveLocalData(localData);
                    return items;
                }
                return localData.attendance || [];
            }
            if (method === 'POST') {
                const newAtt = { id: Date.now(), date: new Date().toISOString().split('T')[0], ...body };
                await fb.setDocument('attendance', newAtt);
                if (!localData.attendance) localData.attendance = [];
                localData.attendance.unshift(newAtt);
                this.saveLocalData(localData);
                return newAtt;
            }
        }

        if (endpoint === '/leaves') {
            if (method === 'GET') {
                const items = await fb.getCollection('leaves');
                if (items && items.length > 0) {
                    localData.leaves = items;
                    this.saveLocalData(localData);
                    return items;
                }
                return localData.leaves || [];
            }
            if (method === 'POST') {
                const newLeave = {
                    id: Date.now(),
                    status: 'Pending',
                    appliedDate: new Date().toLocaleDateString() + ' ' + new Date().toLocaleTimeString(),
                    ...body
                };
                await fb.setDocument('leaves', newLeave);
                if (!localData.leaves) localData.leaves = [];
                localData.leaves.unshift(newLeave);
                this.saveLocalData(localData);
                return newLeave;
            }
            if (method === 'PUT') {
                await fb.setDocument('leaves', body);
                const idx = localData.leaves.findIndex(l => l.id === body.id);
                if (idx !== -1) {
                    localData.leaves[idx] = { ...localData.leaves[idx], ...body };
                    this.saveLocalData(localData);
                    return localData.leaves[idx];
                }
            }
            if (method === 'DELETE') {
                await fb.deleteDocument('leaves', body.id);
                localData.leaves = (localData.leaves || []).filter(l => l.id !== body.id);
                this.saveLocalData(localData);
                return { success: true };
            }
        }

        if (endpoint === '/register') {
            if (!localData.employees) localData.employees = [];
            const empId = Date.now();
            const empCode = 'REV-WORKER' + String(localData.employees.length + 1).padStart(3, '0');
            const username = (body.email || body.phone || 'worker_' + empId).split('@')[0];
            const newWorker = {
                id: empId,
                empCode: empCode,
                role: 'STAFF',
                designation: 'Facility Operations Attendant',
                department: 'Housekeeping & Maintenance',
                status: 'Active',
                efficiency: 95,
                registeredDate: new Date().toISOString().split('T')[0],
                ...body
            };
            const newUser = {
                id: empId,
                name: body.name,
                username: username,
                password: 'staff123',
                role: 'STAFF',
                email: body.email,
                phone: body.phone
            };

            await fb.setDocument('employees', newWorker);
            await fb.setDocument('users', newUser);

            localData.employees.unshift(newWorker);
            if (!localData.users) localData.users = [];
            localData.users.push(newUser);
            this.saveLocalData(localData);

            const token = "fb_jwt_worker_" + empId;
            this.setToken(token);
            this.setCurrentUser(newWorker);
            return { success: true, user: newWorker, token };
        }

        if (endpoint === '/users') {
            if (method === 'GET') {
                const items = await fb.getCollection('users');
                if (items && items.length > 0) {
                    localData.users = items;
                    this.saveLocalData(localData);
                    return items;
                }
                return localData.users || [];
            }
        }

        return null;
    }

    handleLocalRequest(endpoint, method, body) {
        const data = this.getLocalData();

        if (endpoint === '/employees') {
            if (method === 'GET') return data.employees || [];
            if (method === 'POST') {
                const newEmp = { id: Date.now(), ...body, status: 'Active', efficiency: 90 };
                data.employees = (data.employees || []).filter(e => e.id !== newEmp.id && (e.name || '').trim().toLowerCase() !== (newEmp.name || '').trim().toLowerCase());
                data.employees.unshift(newEmp);
                this.saveLocalData(data);
                return newEmp;
            }
            if (method === 'PUT') {
                const index = (data.employees || []).findIndex(e => e.id === body.id);
                if (index !== -1) {
                    data.employees[index] = { ...data.employees[index], ...body };
                } else {
                    data.employees.unshift(body);
                }
                this.saveLocalData(data);
                return body;
            }
            if (method === 'DELETE') {
                data.employees = (data.employees || []).filter(e => e.id !== body.id);
                this.saveLocalData(data);
                return { success: true };
            }
        }

        if (endpoint === '/tasks') {
            if (method === 'GET') return data.tasks;
            if (method === 'POST') {
                const newTask = {
                    id: Date.now(),
                    taskCode: 'REV-HK' + Math.floor(100 + Math.random() * 900),
                    date: new Date().toISOString().split('T')[0],
                    status: 'Pending',
                    inspectedBy: 'Pending',
                    ...body
                };
                data.tasks.unshift(newTask);
                this.saveLocalData(data);
                return newTask;
            }
            if (method === 'PUT') {
                const index = data.tasks.findIndex(t => t.id === body.id);
                if (index !== -1) {
                    data.tasks[index] = { ...data.tasks[index], ...body };
                    this.saveLocalData(data);
                    return data.tasks[index];
                }
            }
        }

        if (endpoint === '/complaints') {
            if (method === 'GET') return data.complaints;
            if (method === 'POST') {
                const newTicket = {
                    id: Date.now(),
                    ticketNo: 'REV-MNT' + Math.floor(900 + Math.random() * 99),
                    reportedDate: new Date().toLocaleString(),
                    status: 'Pending',
                    resolution: 'Under inspection',
                    ...body
                };
                data.complaints.unshift(newTicket);
                this.saveLocalData(data);
                return newTicket;
            }
            if (method === 'PUT') {
                const index = data.complaints.findIndex(c => c.id === body.id);
                if (index !== -1) {
                    data.complaints[index] = { ...data.complaints[index], ...body };
                    this.saveLocalData(data);
                    return data.complaints[index];
                }
            }
        }

        if (endpoint === '/inventory') {
            if (method === 'GET') return data.inventory;
            if (method === 'POST') {
                const newItem = {
                    id: Date.now(),
                    itemCode: 'REV-INV' + String(data.inventory.length + 1).padStart(2, '0'),
                    status: body.quantity <= body.reorderLevel ? 'Low Stock' : 'In Stock',
                    ...body
                };
                data.inventory.unshift(newItem);
                this.saveLocalData(data);
                return newItem;
            }
            if (method === 'PUT') {
                const index = data.inventory.findIndex(i => i.id === body.id);
                if (index !== -1) {
                    data.inventory[index] = { ...data.inventory[index], ...body };
                    data.inventory[index].status = data.inventory[index].quantity <= data.inventory[index].reorderLevel ? 'Low Stock' : 'In Stock';
                    this.saveLocalData(data);
                    return data.inventory[index];
                }
            }
        }

        if (endpoint === '/attendance') {
            if (method === 'GET') return data.attendance || [];
            if (method === 'POST') {
                const newAtt = { id: Date.now(), date: new Date().toISOString().split('T')[0], ...body };
                if (!data.attendance) data.attendance = [];
                data.attendance.unshift(newAtt);
                this.saveLocalData(data);
                return newAtt;
            }
        }

        if (endpoint === '/leaves') {
            if (!data.leaves) data.leaves = [];
            if (method === 'GET') return data.leaves;
            if (method === 'POST') {
                const newLeave = {
                    id: Date.now(),
                    status: 'Pending',
                    appliedDate: new Date().toLocaleDateString() + ' ' + new Date().toLocaleTimeString(),
                    ...body
                };
                data.leaves.unshift(newLeave);
                this.saveLocalData(data);
                return newLeave;
            }
            if (method === 'PUT') {
                const idx = data.leaves.findIndex(l => l.id === body.id);
                if (idx !== -1) {
                    data.leaves[idx] = { ...data.leaves[idx], ...body };
                    this.saveLocalData(data);
                    return data.leaves[idx];
                }
            }
            if (method === 'DELETE') {
                const currentUser = this.getCurrentUser();
                if (currentUser.role !== 'ADMIN') {
                    throw new Error("ACCESS DENIED: Only Administrator has the authority to delete data.");
                }
                data.leaves = data.leaves.filter(l => l.id !== body.id);
                this.saveLocalData(data);
                return { success: true };
            }
        }

        if (endpoint === '/auth/otp/send') {
            const otpCode = Math.floor(100000 + Math.random() * 900000).toString();
            sessionStorage.setItem('last_otp_' + (body.phone || body.email), otpCode);
            return {
                success: true,
                message: `OTP dispatched to Phone: ${body.phone} & Email: ${body.email}`,
                dev_otp: otpCode
            };
        }

        if (endpoint === '/auth/otp/verify') {
            const storedOtp = sessionStorage.getItem('last_otp_' + body.identifier);
            if (body.otp === '123456' || body.otp === storedOtp) {
                return { success: true, message: "OTP Verified" };
            } else {
                return { success: false, message: "Invalid verification code" };
            }
        }

        if (endpoint === '/register') {
            if (!data.employees) data.employees = [];
            const empId = Date.now();
            const empCode = 'REV-WORKER' + String(data.employees.length + 1).padStart(3, '0');
            const username = (body.email || body.phone || 'worker_' + empId).split('@')[0];
            const newWorker = {
                id: empId,
                empCode: empCode,
                role: 'STAFF',
                designation: 'Facility Operations Attendant',
                department: 'Housekeeping & Maintenance',
                status: 'Active',
                efficiency: 95,
                registeredDate: new Date().toISOString().split('T')[0],
                ...body
            };
            data.employees.unshift(newWorker);

            // Add user for login
            if (!data.users) data.users = [];
            data.users.push({
                id: empId,
                name: body.name,
                username: username,
                password: 'staff123',
                role: 'STAFF',
                email: body.email,
                phone: body.phone
            });
            this.saveLocalData(data);
            const mockToken = "mock_jwt_token_worker_" + empId;
            this.setToken(mockToken);
            this.setCurrentUser(newWorker);
            return { success: true, user: newWorker, token: mockToken };
        }

        if (endpoint === '/reports') {
            if (method === 'GET') return data.reports;
        }

        if (endpoint === '/users') {
            if (method === 'GET') return data.users;
        }

        return data;
    }

    async sendOtp(phone, email) {
        return await this.request('/auth/otp/send', 'POST', { phone, email });
    }

    async verifyOtp(identifier, otp) {
        return await this.request('/auth/otp/verify', 'POST', { identifier, otp });
    }

    async registerWorker(workerData) {
        return await this.request('/register', 'POST', workerData);
    }

    async getLeaves() {
        return await this.request('/leaves', 'GET');
    }

    async applyLeave(leaveData) {
        return await this.request('/leaves', 'POST', leaveData);
    }

    async updateLeaveStatus(id, status, comment = '') {
        return await this.request('/leaves', 'PUT', { id, status, adminComment: comment });
    }

    async deleteRecord(endpoint, id) {
        const user = this.getCurrentUser();
        if (user.role !== 'ADMIN') {
            alert("⚠️ ACCESS DENIED: Only Company Administrator has the authority to permanently delete records.");
            return { success: false, error: "Only Admin can delete records" };
        }
        return await this.request(endpoint, 'DELETE', { id, role: user.role, adminPassword: 'IPS_MIHIR_R_KADAM' });
    }
}

const api = new ApiService();
