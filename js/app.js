// REVATI ENTERPRISES - Application Controller & JWT Authentication Logic
// Academic Project: Sheth L.U.J. & Sir M.V. College of Science | Mihir R. Kadam (T082)

document.addEventListener('DOMContentLoaded', async () => {
    localStorage.removeItem('revati_admin_auth');
    sessionStorage.removeItem('revati_admin_auth');
    setupAdminSecurityForm();
    checkAdminSecurityAuth();
    setupNavigation();
    setupForms();
    setupLoginForm();
    setupFirebaseUI();
    await applyRolePermissions();
    await loadAppState();
});

window.addEventListener('beforeunload', () => {
    localStorage.removeItem('revati_admin_auth');
    sessionStorage.removeItem('revati_admin_auth');
});

// Setup JWT Login Form Submission
function setupLoginForm() {
    const loginForm = document.getElementById('loginForm');
    if (!loginForm) return;

    loginForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const u = document.getElementById('loginUsername').value;
        const p = document.getElementById('loginPassword').value;

        const res = await api.login(u, p);
        if (res.success) {
            closeModal('loginModal');
            await applyRolePermissions();
            await loadAppState();
            alert(`Authentication Successful!\nRole: ${res.user.role}\nIssued JWT Token: ${res.token.substring(0, 24)}...`);
            scrollToPortal();
        } else {
            alert('Login Failed: ' + (res.message || 'Invalid credentials'));
        }
    });
}

function handleLogout() {
    lockAdminPortal();
    api.logout();
    alert('Logged out from Revati Enterprises session.');
    window.location.reload();
}

// Role & Permission Application Engine
async function applyRolePermissions() {
    const currentUser = api.getCurrentUser();
    const perms = api.getPermissions();

    document.getElementById('userNameDisplay').textContent = currentUser.name;
    document.getElementById('userRoleDisplay').textContent = perms.title.toUpperCase();
    
    const initials = currentUser.name.split(' ').map(n => n[0]).join('').slice(0, 2);
    document.getElementById('userAvatar').textContent = initials;

    const adminBadge = document.getElementById('adminBadgeIndicator');
    adminBadge.className = `badge ${perms.badgeClass}`;
    adminBadge.innerHTML = `<i class="fa-solid fa-user-shield"></i> ${perms.title.toUpperCase()} PORTAL`;

    document.getElementById('roleBannerText').textContent = perms.title;

    // Sidebar Navigation Filtering
    const navItems = document.querySelectorAll('.nav-item');
    let firstAllowedView = null;

    navItems.forEach(item => {
        const allowedRoles = (item.getAttribute('data-role-allow') || '').split(',');
        if (currentUser.role === 'ADMIN' || allowedRoles.includes(currentUser.role)) {
            item.style.display = 'flex';
            if (!firstAllowedView) firstAllowedView = item.getAttribute('data-view');
        } else {
            item.style.display = 'none';
        }
    });

    const adminElements = document.querySelectorAll('.rbac-admin-only');
    adminElements.forEach(el => {
        el.style.display = (currentUser.role === 'ADMIN') ? '' : 'none';
    });

    // Action Buttons Guarding
    const taskBtns = document.querySelectorAll('.rbac-task-create');
    taskBtns.forEach(btn => btn.style.display = perms.canAssignTask ? 'inline-flex' : 'none');

    const cmpBtns = document.querySelectorAll('.rbac-complaint-create');
    cmpBtns.forEach(btn => btn.style.display = perms.canLodgeComplaint ? 'inline-flex' : 'none');

    const invBtns = document.querySelectorAll('.rbac-inventory-create');
    invBtns.forEach(btn => btn.style.display = perms.canAddInventory ? 'inline-flex' : 'none');

    updatePortalHeaderTitles(currentUser, perms);

    const activeNav = document.querySelector('.nav-item.active');
    const currentViewId = activeNav ? activeNav.getAttribute('data-view') : 'dashboard';
    if (!perms.allowedViews.includes(currentViewId)) {
        switchView(firstAllowedView || 'dashboard');
    }
}

function updatePortalHeaderTitles(user, perms) {
    const titleEl = document.getElementById('portalHeaderTitle');
    const descEl = document.getElementById('portalHeaderDesc');

    if (user.role === 'ADMIN' || user.role === 'SUPERVISOR') {
        titleEl.textContent = 'Company Administrator Control & Operations Master';
        descEl.textContent = 'Full enterprise oversight: manage facility client contracts, inspect site SLA compliance, review service tickets, and issue billing quotes.';
    } else {
        titleEl.textContent = 'Client & Customer Facility Management Portal';
        descEl.textContent = 'Customer self-service portal: monitor real-time housekeeping SLA scores, lodge facility maintenance tickets, and download monthly billing invoices.';
    }
}

async function selectRole(role) {
    const users = api.getLocalData().users;
    const targetUser = users.find(u => u.role === role) || users[0];

    api.setCurrentUser(targetUser);
    closeModal('switchRoleModal');
    await applyRolePermissions();
    await loadAppState();
    alert(`Entered ${ROLE_PERMISSIONS[role].title} Portal`);
}

function setupNavigation() {
    const navItems = document.querySelectorAll('.nav-item[data-view]');
    navItems.forEach(item => {
        item.addEventListener('click', () => {
            const targetView = item.getAttribute('data-view');
            if (targetView && targetView !== 'letterhead') {
                switchView(targetView);
            }
        });
    });
}

function switchView(viewId) {
    if (!viewId || viewId === 'null' || viewId === 'undefined') return;
    const currentUser = api.getCurrentUser();
    const perms = api.getPermissions();
    
    // Administrator has full, unrestricted access to all portal views
    if (currentUser.role !== 'ADMIN' && (!perms || !perms.allowedViews || !perms.allowedViews.includes(viewId))) {
        alert(`Access Denied: Your role (${perms ? perms.title : 'User'}) does not have permission to view ${viewId}.`);
        return;
    }

    document.querySelectorAll('.nav-item').forEach(el => el.classList.remove('active'));
    document.querySelectorAll('.page-view').forEach(el => el.classList.remove('active'));

    const navTarget = document.querySelector(`.nav-item[data-view="${viewId}"]`);
    const viewTarget = document.getElementById(`view-${viewId}`);

    if (navTarget) navTarget.classList.add('active');
    if (viewTarget) viewTarget.classList.add('active');

    renderViewData(viewId);
}

async function loadAppState() {
    await renderDashboard();
    await renderEmployees();
    await renderStaffDirectory();
    await renderOrgHierarchy();
    await renderAttendance();
    await renderTasks();
    await renderComplaints();
    await renderInventory();
    await renderReports();
    await renderUsers();
    await renderLeaveApplications();
    await renderRegisteredWorkers();
    populateSelectDropdowns();
}

function renderViewData(viewId) {
    switch (viewId) {
        case 'dashboard': renderDashboard(); break;
        case 'employees': renderEmployees(); renderAttendance(); break;
        case 'staff-directory': renderStaffDirectory(); break;
        case 'leaves': renderLeaveApplications(); renderRegisteredWorkers(); break;
        case 'org-hierarchy': renderOrgHierarchy(); break;
        case 'housekeeping': renderTasks(); break;
        case 'maintenance': renderComplaints(); break;
        case 'inventory': renderInventory(); break;
        case 'reports': renderReports(); break;
        case 'users': renderUsers(); break;
    }
}

async function renderDashboard() {
    const emps = await api.request('/employees') || [];
    const tasks = await api.request('/tasks') || [];
    const complaints = await api.request('/complaints') || [];
    const inventory = await api.request('/inventory') || [];
    const localData = api.getLocalData();
    const sites = localData.sites || [];
    const contracts = localData.contracts || [];

    const totalRev = contracts.reduce((sum, c) => sum + (c.monthlyRate || 0), 0);
    const revenueEl = document.getElementById('statRevenue');
    if (revenueEl) revenueEl.textContent = `₹ ${totalRev.toLocaleString()}`;

    const slaEl = document.getElementById('statSlaScore');
    if (slaEl) slaEl.textContent = tasks.length > 0 ? "98.8% Gold" : "0.0% (No Data)";

    const activeEmpsEl = document.getElementById('statActiveEmps');
    if (activeEmpsEl) activeEmpsEl.textContent = `${emps.length} Personnel`;

    const cleanTasksEl = document.getElementById('statCleaningTasks');
    if (cleanTasksEl) cleanTasksEl.textContent = `${tasks.length} Tasks`;

    const openComplaintsEl = document.getElementById('statOpenComplaints');
    if (openComplaintsEl) openComplaintsEl.textContent = `${complaints.filter(c => c.status !== 'Resolved').length} Pending`;

    // Render Commercial Site SLA Cards
    const siteCardsGrid = document.getElementById('siteCardsGrid');
    if (siteCardsGrid) {
        if (sites.length === 0) {
            siteCardsGrid.innerHTML = `
                <div style="grid-column: 1 / -1; text-align: center; color: var(--text-muted); padding: 2rem; background: rgba(255,255,255,0.02); border-radius: 12px; border: 1px dashed var(--border-color);">
                    <i class="fa-solid fa-building-circle-check" style="font-size: 2rem; color: var(--gold-primary); margin-bottom: 0.5rem;"></i><br>
                    No commercial site locations registered yet. Click <strong style="color: var(--gold-primary);">"+ Add Client/Staff"</strong> or add client contracts to track site SLA performance.
                </div>
            `;
        } else {
            siteCardsGrid.innerHTML = sites.map(s => `
                <div style="background: rgba(18, 24, 38, 0.85); border: 1px solid var(--border-color); border-radius: 12px; padding: 1.1rem; display: flex; flex-direction: column; justify-content: space-between; position: relative; overflow: hidden;">
                    <div style="position: absolute; top: 0; right: 0; background: rgba(212,175,55,0.15); color: var(--gold-primary); font-size: 0.7rem; font-weight: 700; padding: 0.25rem 0.6rem; border-bottom-left-radius: 8px;">
                        <i class="fa-solid fa-shield-halved"></i> ISO VERIFIED
                    </div>
                    <div>
                        <div style="font-size: 1rem; font-weight: 700; color: #FFF; margin-bottom: 0.2rem;">${s.siteName}</div>
                        <div style="font-size: 0.8rem; color: var(--text-muted); margin-bottom: 0.75rem;"><i class="fa-solid fa-location-dot" style="color: var(--gold-primary);"></i> ${s.location} &bull; <strong>${s.areaSqFt}</strong></div>
                        <div style="display: flex; justify-content: space-between; font-size: 0.82rem; margin-bottom: 0.4rem;">
                            <span style="color: var(--text-muted);">Supervisor:</span>
                            <span style="font-weight: 600; color: var(--text-main);">${s.supervisor}</span>
                        </div>
                        <div style="display: flex; justify-content: space-between; font-size: 0.82rem; margin-bottom: 0.75rem;">
                            <span style="color: var(--text-muted);">Active Staff:</span>
                            <span style="font-weight: 600; color: #60A5FA;">${s.staffCount} On Duty</span>
                        </div>
                    </div>
                    <div style="display: flex; justify-content: space-between; align-items: center; border-top: 1px solid rgba(255,255,255,0.06); padding-top: 0.6rem; margin-top: 0.5rem;">
                        <span class="badge badge-gold" style="font-size: 0.78rem;"><i class="fa-solid fa-award"></i> SLA: ${s.slaScore}</span>
                        <span style="font-size: 0.78rem; font-weight: 700; color: #10B981;"><i class="fa-solid fa-circle-check"></i> ${s.status}</span>
                    </div>
                </div>
            `).join('');
        }
    }

    const dashTaskBody = document.getElementById('dashTaskTableBody');
    if (dashTaskBody) {
        if (tasks.length === 0) {
            dashTaskBody.innerHTML = `<tr><td colspan="4" style="text-align: center; color: var(--text-muted); padding: 1rem;">No cleaning tasks assigned yet. Click "+ Dispatch Task" to add tasks.</td></tr>`;
        } else {
            dashTaskBody.innerHTML = tasks.slice(0, 4).map(t => `
                <tr>
                    <td><strong>${t.taskCode}</strong></td>
                    <td>${t.area}</td>
                    <td><strong>${t.assignedTo}</strong></td>
                    <td><span class="badge badge-${t.status.toLowerCase().replace(' ', '-')}">${t.status}</span></td>
                </tr>
            `).join('');
        }
    }

    const dashComplaintBody = document.getElementById('dashComplaintTableBody');
    if (dashComplaintBody) {
        if (complaints.length === 0) {
            dashComplaintBody.innerHTML = `<tr><td colspan="4" style="text-align: center; color: var(--text-muted); padding: 1rem;">No maintenance tickets logged yet. Click "+ Lodge Ticket" to report issues.</td></tr>`;
        } else {
            dashComplaintBody.innerHTML = complaints.slice(0, 4).map(c => `
                <tr>
                    <td><strong>${c.ticketNo}</strong></td>
                    <td>${c.title} (${c.category})</td>
                    <td><strong>${c.assignedTo}</strong></td>
                    <td><span class="badge badge-${c.status.toLowerCase().replace(' ', '-')}">${c.status}</span></td>
                </tr>
            `).join('');
        }
    }
}

async function renderEmployees() {
    const localData = api.getLocalData();
    const contracts = localData.contracts || [];
    const rawEmps = await api.request('/employees') || [];
    const emps = [];
    const seenNames = new Set();
    for (const e of rawEmps) {
        const key = (e.name || '').trim().toLowerCase();
        if (key && !seenNames.has(key)) {
            seenNames.add(key);
            emps.push(e);
        }
    }

    const contractsTbody = document.getElementById('contractsTableBody');
    if (contractsTbody) {
        if (contracts.length === 0) {
            contractsTbody.innerHTML = `<tr><td colspan="9" style="text-align: center; color: var(--text-muted); padding: 1.5rem;"><i class="fa-solid fa-file-contract" style="color: var(--gold-primary); margin-right: 0.4rem;"></i> No active commercial client contracts registered yet. Click <strong style="color: var(--gold-primary);">"+ New Contract Quote"</strong> to register contracts.</td></tr>`;
        } else {
            contractsTbody.innerHTML = contracts.map(c => `
                <tr>
                    <td><strong>REV-CNT${c.id}</strong></td>
                    <td><strong>${c.clientName}</strong><br><span style="font-size: 0.75rem; color: var(--text-muted);">${c.contactPerson}</span></td>
                    <td>${c.location}</td>
                    <td>${c.areaSqFt.toLocaleString()} sq ft</td>
                    <td>${c.wings} Blocks</td>
                    <td><span class="badge badge-gold">${c.tier}</span></td>
                    <td><strong style="color: var(--gold-primary);">₹ ${c.monthlyRate.toLocaleString()} / mo</strong></td>
                    <td><span class="badge badge-completed">${c.status}</span></td>
                    <td>
                        <a href="estimator.html" class="btn btn-secondary btn-sm" style="text-decoration: none;"><i class="fa-solid fa-file-pdf" style="color: var(--gold-primary);"></i> Quote PDF</a>
                    </td>
                </tr>
            `).join('');
        }
    }

    const tbody = document.getElementById('empTableBody');
    if (tbody) {
        if (emps.length === 0) {
            tbody.innerHTML = `<tr><td colspan="8" style="text-align: center; color: var(--text-muted); padding: 1.5rem;"><i class="fa-solid fa-user-plus" style="color: var(--gold-primary); margin-right: 0.4rem;"></i> No staff members registered yet. Click <strong style="color: var(--gold-primary);">"+ Register Staff (Admin)"</strong> above to enter your staff names and designations.</td></tr>`;
        } else {
            tbody.innerHTML = emps.map(e => `
                <tr>
                    <td><strong>${e.empCode}</strong></td>
                    <td><strong>${e.name}</strong></td>
                    <td>${e.department}</td>
                    <td>${e.designation}</td>
                    <td><span style="font-size: 0.8rem; color: var(--text-muted);">${e.shift}</span></td>
                    <td>${e.contact}</td>
                    <td><strong style="color: var(--success);">${e.efficiency || 95}%</strong> SLA Rating</td>
                    <td><span class="badge badge-present">${e.status || 'Active'}</span></td>
                </tr>
            `).join('');
        }
    }
}

async function renderStaffDirectory() {
    const rawEmps = await api.request('/employees') || [];
    const localData = api.getLocalData();
    const localEmps = localData.employees || [];

    // Merge server employees and local storage employees safely
    const mergedMap = new Map();
    localEmps.forEach(e => {
        const key = (e.name || '').trim().toLowerCase();
        if (key) mergedMap.set(key, e);
    });
    rawEmps.forEach(e => {
        const key = (e.name || '').trim().toLowerCase();
        if (key) mergedMap.set(key, e);
    });

    const emps = Array.from(mergedMap.values());
    localData.employees = emps;
    api.saveLocalData(localData);

    const tbody = document.getElementById('staffDirectoryTableBody');
    if (!tbody) return;

    if (emps.length === 0) {
        tbody.innerHTML = `<tr><td colspan="9" style="text-align: center; color: var(--text-muted); padding: 2rem;"><i class="fa-solid fa-user-plus" style="font-size: 1.5rem; color: var(--gold-primary); margin-bottom: 0.5rem;"></i><br>No employees registered in roster directory. Click <strong style="color: var(--gold-primary);">"+ Add New Employee"</strong> above to register staff names and info.</td></tr>`;
        return;
    }

    tbody.innerHTML = emps.map(e => {
        const shiftDisplay = e.shift || 'General (09:00 - 17:30)';
        const contactDisplay = e.contact || e.phone || 'N/A';
        return `
            <tr>
                <td><strong>${e.empCode || 'REV-WORKER'}</strong></td>
                <td><strong style="color: #fff; font-size: 0.95rem;">${e.name}</strong></td>
                <td><span class="badge badge-info">${e.department || 'Operations'}</span></td>
                <td><strong>${e.designation || 'Attendant'}</strong></td>
                <td><span style="font-size: 0.8rem; color: var(--text-muted);">${shiftDisplay}</span></td>
                <td>${contactDisplay}</td>
                <td>
                    ${e.workAssigned ? `<strong style="color: var(--gold-primary);"><i class="fa-solid fa-broom"></i> ${e.workAssigned}</strong>` : `<span style="color: var(--text-muted); font-size: 0.8rem;">Unassigned</span>`}
                </td>
                <td><span class="badge badge-present">${e.status || 'Active'}</span></td>
                <td style="text-align: center;">
                    <div style="display: flex; gap: 0.35rem; justify-content: center; flex-wrap: wrap;">
                        <button class="btn btn-gold btn-sm" onclick="assignWorkToEmployee(${e.id})" title="Assign Work / Task"><i class="fa-solid fa-briefcase"></i> Work</button>
                        <button class="btn btn-secondary btn-sm" onclick="editEmployeeData(${e.id})" title="Edit Employee Info"><i class="fa-solid fa-pen-to-square"></i> Edit</button>
                        <button class="btn btn-danger btn-sm" onclick="deleteEmployeeRecord(${e.id})" title="Remove Employee"><i class="fa-solid fa-trash"></i> Remove</button>
                    </div>
                </td>
            </tr>
        `;
    }).join('');
}

async function assignWorkToEmployee(empId) {
    const emps = await api.request('/employees') || [];
    const emp = emps.find(e => e.id === empId);
    if (!emp) return;

    const workDesc = prompt(`Assign Cleaning/Maintenance Work for Employee: "${emp.name}"`, emp.workAssigned || 'Executive Atrium Deep Cleaning');
    if (workDesc !== null && workDesc.trim() !== '') {
        emp.workAssigned = workDesc.trim();
        await api.request('/employees', 'PUT', emp);
        
        const newTask = {
            title: workDesc.trim(),
            area: 'Assigned Site Area',
            assignedTo: emp.name,
            frequency: 'Daily',
            priority: 'High',
            notes: `Assigned directly to employee ${emp.name} (${emp.designation})`
        };
        await api.request('/tasks', 'POST', newTask);

        await loadAppState();
        alert(`Work "${workDesc.trim()}" successfully assigned to ${emp.name}!`);
    }
}

async function editEmployeeData(empId) {
    const emps = await api.request('/employees') || [];
    const emp = emps.find(e => e.id === empId);
    if (!emp) return;

    const newName = prompt(`Edit Full Name for Employee (${emp.empCode}):`, emp.name);
    if (!newName) return;

    const newDesignation = prompt(`Edit Designation for ${newName}:`, emp.designation);
    if (!newDesignation) return;

    const newContact = prompt(`Edit Contact Phone Number for ${newName}:`, emp.contact || emp.phone);
    if (!newContact) return;

    emp.name = newName.trim();
    emp.designation = newDesignation.trim();
    emp.contact = newContact.trim();
    emp.phone = newContact.trim();

    await api.request('/employees', 'PUT', emp);
    await loadAppState();
    alert(`Employee ${emp.name} info updated successfully!`);
}

async function deleteEmployeeRecord(empId) {
    const localData = api.getLocalData();
    const emps = localData.employees || [];
    const emp = emps.find(e => e.id === empId) || (await api.request('/employees') || []).find(e => e.id === empId);
    if (!emp) return;

    if (confirm(`ARE YOU SURE YOU WANT TO REMOVE EMPLOYEE?\n\nName: ${emp.name}\nDesignation: ${emp.designation}\nCode: ${emp.empCode}\n\nThis will permanently delete this employee from the roster.`)) {
        // Delete from LocalStorage
        localData.employees = (localData.employees || []).filter(e => e.id !== emp.id && (e.name || '').trim().toLowerCase() !== (emp.name || '').trim().toLowerCase());
        api.saveLocalData(localData);

        // Delete from Server Database
        await api.deleteRecord('/employees', emp.id);
        
        await loadAppState();
        alert(`Employee "${emp.name}" removed from system successfully.`);
    }
}

const DEFAULT_ORG_HIERARCHY = [
    { id: 1, name: "Mihir R. Kadam", role: "Owner / Managing Director", department: "Executive Board", email: "mihir.kadam@revatienterprises.com", phone: "+91 9769930626 / 9930023185" },
    { id: 2, name: "Executive General Manager", role: "General Manager", department: "Corporate Management", email: "gm@revatienterprises.com", phone: "+91 9876543210" },
    { id: 3, name: "Operations Lead", role: "Operations / Facility Manager", department: "Facility Operations", email: "ops@revatienterprises.com", phone: "+91 9876543211" },
    { id: 4, name: "Housekeeping Lead", role: "Housekeeping Manager", department: "Housekeeping SLA", email: "hk.manager@revatienterprises.com", phone: "+91 9876543212" },
    { id: 5, name: "Maintenance Lead", role: "Maintenance Manager", department: "Technical & MEP", email: "mnt.manager@revatienterprises.com", phone: "+91 9876543213" },
    { id: 6, name: "Shift Supervisor", role: "Supervisors", department: "Field Operations", email: "supervisor@revatienterprises.com", phone: "+91 9876543214" }
];

async function getOrgHierarchyData() {
    const localData = api.getLocalData();
    if (!localData.orgHierarchy || localData.orgHierarchy.length === 0) {
        localData.orgHierarchy = DEFAULT_ORG_HIERARCHY;
        api.saveLocalData(localData);
    }
    return localData.orgHierarchy;
}

async function renderOrgHierarchy() {
    const list = await getOrgHierarchyData();

    const visualContainer = document.getElementById('visualOrgChartContainer');
    if (visualContainer) {
        visualContainer.innerHTML = `
            <div style="display: flex; flex-direction: column; align-items: center; width: 100%; gap: 0.85rem;">
                <div style="font-size: 0.72rem; color: var(--gold-primary); font-weight: 800; letter-spacing: 1px; text-transform: uppercase;">MANAGEMENT REPORTING STRUCTURE</div>
                
                <div style="display: flex; flex-direction: column; align-items: center; gap: 0.85rem; width: 100%;">
                    ${list.map((item, idx) => `
                        <div style="display: flex; flex-direction: column; align-items: center; width: 100%; max-width: 440px;">
                            <div style="background: rgba(18, 26, 40, 0.95); border: 1px solid ${idx === 0 ? 'var(--gold-primary)' : 'rgba(255,255,255,0.15)'}; border-radius: 12px; padding: 0.9rem 1.25rem; width: 100%; text-align: center; box-shadow: 0 4px 15px rgba(0,0,0,0.25);">
                                <div style="font-size: 0.82rem; font-weight: 700; color: ${idx === 0 ? 'var(--gold-primary)' : '#60A5FA'}; text-transform: uppercase; margin-bottom: 0.2rem;">
                                    ${item.role}
                                </div>
                                <div style="font-size: 1.15rem; font-weight: 800; color: #fff;">${item.name}</div>
                                <div style="font-size: 0.78rem; color: var(--text-muted); margin-top: 0.25rem;">${item.department} | ${item.phone || ''}</div>
                            </div>
                            ${idx < list.length - 1 ? `<div style="width: 2px; height: 16px; background: var(--gold-primary); margin: 0.15rem 0; opacity: 0.7;"></div><i class="fa-solid fa-chevron-down" style="color: var(--gold-primary); font-size: 0.75rem;"></i>` : ''}
                        </div>
                    `).join('')}
                </div>
            </div>
        `;
    }

    const tbody = document.getElementById('orgHierarchyTableBody');
    if (tbody) {
        if (list.length === 0) {
            tbody.innerHTML = `<tr><td colspan="6" style="text-align: center; color: var(--text-muted); padding: 1.5rem;">No management staff added yet. Click "+ Add Executive / Manager" to add roles.</td></tr>`;
        } else {
            tbody.innerHTML = list.map(item => `
                <tr>
                    <td><strong style="color: #fff; font-size: 0.95rem;">${item.name}</strong></td>
                    <td><strong style="color: var(--gold-primary);">${item.role}</strong></td>
                    <td>${item.department || 'Executive'}</td>
                    <td>${item.email || 'N/A'}</td>
                    <td>${item.phone || 'N/A'}</td>
                    <td style="text-align: center;" class="rbac-admin-only">
                        <div style="display: flex; gap: 0.35rem; justify-content: center;">
                            <button class="btn btn-secondary btn-sm" onclick="editOrgMember(${item.id})"><i class="fa-solid fa-pen-to-square"></i> Edit</button>
                            <button class="btn btn-danger btn-sm" onclick="deleteOrgMember(${item.id})"><i class="fa-solid fa-trash"></i> Delete</button>
                        </div>
                    </td>
                </tr>
            `).join('');
        }
    }
}

function openOrgModal(id = null) {
    const form = document.getElementById('orgMemberForm');
    if (form) form.reset();
    document.getElementById('orgMemberId').value = id || '';
    document.getElementById('orgModalTitle').textContent = id ? 'Edit Leadership Member' : 'Add Leadership / Management Member';
    openModal('orgMemberModal');
}

async function editOrgMember(id) {
    const list = await getOrgHierarchyData();
    const item = list.find(m => m.id === id);
    if (!item) return;

    document.getElementById('orgMemberId').value = item.id;
    document.getElementById('orgMemberName').value = item.name;
    document.getElementById('orgMemberRole').value = item.role;
    document.getElementById('orgMemberDept').value = item.department || '';
    document.getElementById('orgMemberEmail').value = item.email || '';
    document.getElementById('orgMemberPhone').value = item.phone || '';
    document.getElementById('orgModalTitle').textContent = `Edit Executive Member (${item.name})`;
    openModal('orgMemberModal');
}

async function saveOrgMemberForm(e) {
    if (e && typeof e.preventDefault === 'function') e.preventDefault();

    const idVal = document.getElementById('orgMemberId').value;
    const nameVal = document.getElementById('orgMemberName').value.trim();
    const roleVal = document.getElementById('orgMemberRole').value.trim();
    const deptVal = document.getElementById('orgMemberDept').value.trim();
    const emailVal = document.getElementById('orgMemberEmail').value.trim();
    const phoneVal = document.getElementById('orgMemberPhone').value.trim();

    if (!nameVal || !roleVal) {
        alert('Please enter Full Name and Designation/Role Title');
        return;
    }

    const localData = api.getLocalData();
    if (!localData.orgHierarchy) localData.orgHierarchy = DEFAULT_ORG_HIERARCHY;

    if (idVal) {
        const idx = localData.orgHierarchy.findIndex(m => m.id == idVal);
        if (idx !== -1) {
            localData.orgHierarchy[idx] = {
                id: Number(idVal),
                name: nameVal,
                role: roleVal,
                department: deptVal || 'Executive Board',
                email: emailVal || 'contact@revatienterprises.com',
                phone: phoneVal || '+91 9769930626'
            };
        }
    } else {
        const newMember = {
            id: Date.now(),
            name: nameVal,
            role: roleVal,
            department: deptVal || 'Executive Board',
            email: emailVal || 'contact@revatienterprises.com',
            phone: phoneVal || '+91 9769930626'
        };
        localData.orgHierarchy.push(newMember);
    }

    api.saveLocalData(localData);
    closeModal('orgMemberModal');
    await renderOrgHierarchy();
    alert(`Leadership Member "${nameVal}" Saved Successfully!`);
}

async function deleteOrgMember(id) {
    const list = await getOrgHierarchyData();
    const item = list.find(m => m.id === id);
    if (!item) return;

    if (confirm(`Remove executive member "${item.name}" (${item.role}) from organizational chart?`)) {
        const localData = api.getLocalData();
        localData.orgHierarchy = (localData.orgHierarchy || []).filter(m => m.id !== id);
        api.saveLocalData(localData);
        await renderOrgHierarchy();
        alert(`Member "${item.name}" removed.`);
    }
}

async function renderAttendance() {
    const atts = await api.request('/attendance') || [];
    const tbody = document.getElementById('attTableBody');
    if (tbody) {
        if (atts.length === 0) {
            tbody.innerHTML = `<tr><td colspan="7" style="text-align: center; color: var(--text-muted); padding: 1.5rem;"><i class="fa-solid fa-calendar-xmark" style="color: var(--gold-primary); margin-right: 0.4rem;"></i> No attendance records logged today. Click <strong style="color: #10B981;">"Mark Attendance"</strong> to log clock-ins.</td></tr>`;
        } else {
            tbody.innerHTML = atts.map(a => `
                <tr>
                    <td><strong>${a.empCode}</strong></td>
                    <td><strong>${a.empName}</strong></td>
                    <td>${a.date}</td>
                    <td><i class="fa-regular fa-clock" style="color: var(--success);"></i> ${a.clockIn}</td>
                    <td>${a.clockOut}</td>
                    <td><span class="badge badge-present">${a.status}</span></td>
                    <td><strong>${a.hoursWorked} hrs</strong></td>
                </tr>
            `).join('');
        }
    }
}

async function renderTasks() {
    const currentUser = api.getCurrentUser();
    let tasks = await api.request('/tasks');

    if (currentUser.role === 'STAFF') {
        tasks = tasks.filter(t => t.assignedTo.toLowerCase().includes(currentUser.name.toLowerCase()) || currentUser.name.toLowerCase().includes(t.assignedTo.toLowerCase()));
    }

    const tbody = document.getElementById('taskTableBody');
    if (tasks.length === 0) {
        tbody.innerHTML = `<tr><td colspan="9" style="text-align: center; color: var(--text-muted);">No housekeeping cleaning tasks assigned to your queue currently.</td></tr>`;
        return;
    }

    tbody.innerHTML = tasks.map(t => `
        <tr>
            <td><strong>${t.taskCode}</strong></td>
            <td><strong>${t.title}</strong><br><span style="font-size: 0.78rem; color: var(--text-muted);">${t.notes || ''}</span></td>
            <td>${t.area}</td>
            <td>${t.assignedTo}</td>
            <td>${t.frequency}</td>
            <td><span class="badge badge-info">${t.priority}</span></td>
            <td><span class="badge badge-${t.status.toLowerCase().replace(' ', '-')}">${t.status}</span></td>
            <td>${t.inspectedBy}</td>
            <td>
                ${t.status !== 'Completed' ? `
                    <button class="btn btn-success btn-sm" onclick="completeTask(${t.id})"><i class="fa-solid fa-check"></i> Mark Complete</button>
                ` : `<span style="color: var(--success); font-size: 0.8rem;"><i class="fa-solid fa-circle-check"></i> Verified</span>`}
            </td>
        </tr>
    `).join('');
}

async function completeTask(taskId) {
    const tasks = await api.request('/tasks');
    const task = tasks.find(t => t.id === taskId);
    if (task) {
        const currentUser = api.getCurrentUser();
        task.status = 'Completed';
        task.inspectedBy = currentUser.name;
        await api.request('/tasks', 'PUT', task);
        await renderTasks();
        await renderDashboard();
    }
}

async function renderComplaints() {
    const currentUser = api.getCurrentUser();
    const perms = api.getPermissions();
    let complaints = await api.request('/complaints');

    if (currentUser.role === 'TECHNICIAN') {
        complaints = complaints.filter(c => c.assignedTo.toLowerCase().includes(currentUser.name.toLowerCase()) || currentUser.name.toLowerCase().includes(c.assignedTo.toLowerCase()));
    }

    const tbody = document.getElementById('complaintTableBody');
    if (complaints.length === 0) {
        tbody.innerHTML = `<tr><td colspan="10" style="text-align: center; color: var(--text-muted);">No maintenance tickets assigned to your queue currently.</td></tr>`;
        return;
    }

    tbody.innerHTML = complaints.map(c => `
        <tr>
            <td><strong>${c.ticketNo}</strong></td>
            <td><strong>${c.title}</strong><br><span style="font-size: 0.78rem; color: var(--text-muted);">${c.description}</span></td>
            <td><span class="badge badge-info">${c.category}</span></td>
            <td>${c.location}</td>
            <td>${c.reportedBy}</td>
            <td>${c.assignedTo}</td>
            <td><span class="badge badge-${c.priority === 'Urgent' ? 'urgent' : 'ongoing'}">${c.priority}</span></td>
            <td><span class="badge badge-${c.status.toLowerCase().replace(' ', '-')}">${c.status}</span></td>
            <td style="font-size: 0.82rem; color: var(--text-muted);">${c.resolution}</td>
            <td>
                ${perms.canResolveComplaint && c.status !== 'Resolved' ? `
                    <button class="btn btn-primary btn-sm" onclick="resolveTicket(${c.id})"><i class="fa-solid fa-wrench"></i> Resolve Ticket</button>
                ` : c.status === 'Resolved' ? `<span style="color: var(--success); font-size: 0.8rem;"><i class="fa-solid fa-circle-check"></i> Resolved</span>` : `<span style="color: var(--text-muted); font-size: 0.78rem;">Technician Assigned</span>`}
            </td>
        </tr>
    `).join('');
}

async function resolveTicket(ticketId) {
    const complaints = await api.request('/complaints');
    const ticket = complaints.find(c => c.id === ticketId);
    if (ticket) {
        const note = prompt('Enter Maintenance Fix Resolution Note:', 'Replaced faulty component and tested operational status.');
        if (note) {
            ticket.status = 'Resolved';
            ticket.resolution = note;
            await api.request('/complaints', 'PUT', ticket);
            await renderComplaints();
            await renderDashboard();
        }
    }
}

async function renderInventory() {
    const inv = await api.request('/inventory') || [];
    const perms = api.getPermissions();
    const tbody = document.getElementById('invTableBody') || document.getElementById('inventoryTableBody');
    if (!tbody) return;

    tbody.innerHTML = inv.map(i => {
        const isLow = i.quantity <= i.reorderLevel;
        const stockPct = Math.min(100, Math.round((i.quantity / (i.reorderLevel * 4)) * 100));
        return `
            <tr>
                <td><strong>${i.itemCode}</strong></td>
                <td><strong>${i.name}</strong></td>
                <td>${i.category}</td>
                <td>
                    <div style="display: flex; flex-direction: column; gap: 0.2rem;">
                        <strong style="font-size: 0.95rem; color: ${isLow ? 'var(--danger)' : 'var(--success)'};">${i.quantity} ${i.unit}</strong>
                        <div style="width: 100px; height: 6px; background: rgba(255,255,255,0.1); border-radius: 3px; overflow: hidden;">
                            <div style="width: ${stockPct}%; height: 100%; background: ${isLow ? '#EF4444' : '#10B981'}; border-radius: 3px;"></div>
                        </div>
                    </div>
                </td>
                <td>₹ ${i.unitCost} / ${i.unit}</td>
                <td><span class="badge badge-${isLow ? 'urgent' : 'completed'}">${isLow ? 'REORDER LOW' : 'IN STOCK'}</span></td>
                <td>${i.supplier || 'N/A'}</td>
                <td>
                    ${perms.canAddInventory ? `
                        <button class="btn btn-secondary btn-sm" onclick="restockItem(${i.id})"><i class="fa-solid fa-boxes-packing" style="color: var(--gold-primary);"></i> Restock +10</button>
                    ` : `<span style="color: var(--text-muted); font-size: 0.78rem;">Stock Monitored</span>`}
                </td>
            </tr>
        `;
    }).join('');
}

async function restockItem(itemId) {
    const inv = await api.request('/inventory');
    const item = inv.find(i => i.id === itemId);
    if (item) {
        item.quantity += 10;
        await api.request('/inventory', 'PUT', item);
        await renderInventory();
        await renderDashboard();
    }
}

async function renderReports() {
    const reports = await api.request('/reports');
    const tbody = document.getElementById('reportTableBody');
    tbody.innerHTML = reports.map(r => `
        <tr>
            <td><strong>REP-${r.id}</strong></td>
            <td><strong>${r.title}</strong></td>
            <td><span class="badge badge-info">${r.type}</span></td>
            <td>${r.generatedDate}</td>
            <td>${r.period}</td>
            <td><strong style="color: var(--success);">${r.completedTasks} tasks</strong></td>
            <td><strong style="color: var(--primary);">${r.resolvedComplaints} resolved</strong></td>
            <td><strong>${r.attendanceRate}</strong></td>
            <td>
                <button class="btn btn-secondary btn-sm" onclick="window.print()"><i class="fa-solid fa-print"></i> Print</button>
            </td>
        </tr>
    `).join('');
}

async function renderUsers() {
    const users = await api.request('/users');
    const tbody = document.getElementById('usersTableBody');
    tbody.innerHTML = users.map(u => `
        <tr>
            <td><strong>USR-00${u.id}</strong></td>
            <td><strong>${u.name}</strong></td>
            <td><code>${u.username}</code></td>
            <td><span class="badge ${ROLE_PERMISSIONS[u.role] ? ROLE_PERMISSIONS[u.role].badgeClass : 'badge-info'}">${u.role}</span></td>
            <td>${u.email}</td>
            <td>${u.phone}</td>
            <td><strong style="color: ${u.role === 'ADMIN' ? 'var(--gold-primary)' : 'var(--primary)'};">${u.role === 'ADMIN' ? 'FULL CONTROL' : 'MODULE ACCESS'}</strong></td>
        </tr>
    `).join('');
}

async function populateSelectDropdowns() {
    const emps = await api.request('/employees') || [];
    
    const attEmpSelect = document.getElementById('attEmpSelect');
    if (attEmpSelect) {
        attEmpSelect.innerHTML = emps.map(e => `<option value="${e.empCode}|${e.name}">${e.empCode} - ${e.name}</option>`).join('');
    }
}

let isSavingEmployee = false;

async function saveEmployeeForm(e) {
    if (e && typeof e.preventDefault === 'function') e.preventDefault();
    if (isSavingEmployee) return;
    isSavingEmployee = true;

    const btn = document.querySelector('#empForm button[onclick*="saveEmployeeForm"]') || document.querySelector('#empForm button[type="submit"]');
    if (btn) {
        btn.disabled = true;
        btn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Saving...';
    }

    try {
        const nameInput = document.getElementById('empName');
        const deptInput = document.getElementById('empDept');
        const desigInput = document.getElementById('empDesignation');
        const contactInput = document.getElementById('empContact');
        const joiningInput = document.getElementById('empJoining');
        const shiftInput = document.getElementById('empShift');

        const nameVal = nameInput ? nameInput.value.trim() : '';
        if (!nameVal) {
            alert('Please type Employee Name before saving.');
            if (nameInput) nameInput.focus();
            return;
        }

        const deptVal = (deptInput && deptInput.value) ? deptInput.value : 'Housekeeping';
        const desigVal = (desigInput && desigInput.value.trim()) ? desigInput.value.trim() : 'Housekeeper / Attendant';
        const contactVal = (contactInput && contactInput.value.trim()) ? contactInput.value.trim() : '+91 9769930626';
        const joiningVal = (joiningInput && joiningInput.value) ? joiningInput.value : new Date().toISOString().split('T')[0];
        const shiftVal = (shiftInput && shiftInput.value) ? shiftInput.value : 'Morning (07:00 - 15:30)';

        const data = api.getLocalData();
        if (!data.employees) data.employees = [];

        // Clean duplicates in local storage
        data.employees = data.employees.filter(emp => (emp.name || '').trim().toLowerCase() !== nameVal.toLowerCase());

        const empCode = 'REV-' + String(data.employees.length + 1).padStart(3, '0');
        const newEmp = {
            id: Date.now(),
            empCode,
            name: nameVal,
            department: deptVal,
            designation: desigVal,
            contact: contactVal,
            joiningDate: joiningVal,
            shift: shiftVal,
            status: 'Active',
            efficiency: 98
        };

        data.employees.unshift(newEmp);
        api.saveLocalData(data);

        await api.request('/employees', 'POST', newEmp);

        if (nameInput) nameInput.value = '';
        if (desigInput) desigInput.value = '';
        if (contactInput) contactInput.value = '';
        closeModal('empModal');

        await loadAppState();
        alert(`Employee "${nameVal}" Saved Successfully!`);
    } catch (err) {
        console.error('Error saving employee:', err);
    } finally {
        if (btn) {
            btn.disabled = false;
            btn.innerHTML = '<i class="fa-solid fa-floppy-disk"></i> Save Employee';
        }
        isSavingEmployee = false;
    }
}

function setupForms() {
    const empForm = document.getElementById('empForm');
    if (empForm) {
        empForm.addEventListener('submit', (e) => saveEmployeeForm(e));
    }

    document.getElementById('taskForm').addEventListener('submit', async (e) => {
        e.preventDefault();
        const newTask = {
            title: document.getElementById('taskTitle').value,
            area: document.getElementById('taskArea').value,
            assignedTo: document.getElementById('taskAssignee').value,
            frequency: document.getElementById('taskFreq').value,
            priority: document.getElementById('taskPriority').value,
            notes: document.getElementById('taskNotes').value
        };
        await api.request('/tasks', 'POST', newTask);
        closeModal('taskModal');
        await loadAppState();
        alert('Housekeeping Cleaning Task Created & Assigned!');
    });

    document.getElementById('complaintForm').addEventListener('submit', async (e) => {
        e.preventDefault();
        const currentUser = api.getCurrentUser();
        const newComplaint = {
            title: document.getElementById('cmpTitle').value,
            category: document.getElementById('cmpCategory').value,
            location: document.getElementById('cmpLocation').value,
            reportedBy: currentUser.name,
            assignedTo: document.getElementById('cmpTech').value,
            priority: document.getElementById('cmpPriority').value,
            description: document.getElementById('cmpDesc').value
        };
        await api.request('/complaints', 'POST', newComplaint);
        closeModal('complaintModal');
        await loadAppState();
        alert('Maintenance Complaint Ticket Lodged Successfully!');
    });

    document.getElementById('inventoryForm').addEventListener('submit', async (e) => {
        e.preventDefault();
        const newItem = {
            name: document.getElementById('invName').value,
            category: document.getElementById('invCat').value,
            quantity: parseInt(document.getElementById('invQty').value),
            unit: document.getElementById('invUnit').value,
            unitCost: parseFloat(document.getElementById('invCost').value),
            reorderLevel: parseInt(document.getElementById('invReorder').value),
            supplier: document.getElementById('invSupplier').value
        };
        await api.request('/inventory', 'POST', newItem);
        closeModal('inventoryModal');
        await loadAppState();
        alert('Inventory Stock Item Registered!');
    });

    document.getElementById('attForm').addEventListener('submit', async (e) => {
        e.preventDefault();
        const [empCode, empName] = document.getElementById('attEmpSelect').value.split('|');
        const newAtt = {
            empCode,
            empName,
            clockIn: document.getElementById('attClockIn').value,
            clockOut: document.getElementById('attClockOut').value,
            status: document.getElementById('attStatus').value,
            hoursWorked: 8.5
        };
        await api.request('/attendance', 'POST', newAtt);
        closeModal('attendanceModal');
        await loadAppState();
        alert('Attendance Clocking Recorded!');
    });
}

function openModal(modalId) {
    const modal = document.getElementById(modalId);
    if (modal) {
        modal.classList.add('active');
        if (modalId === 'empModal') {
            const form = document.getElementById('empForm');
            if (form) form.reset();
            const empName = document.getElementById('empName');
            if (empName) empName.value = '';
        } else if (modalId === 'taskModal') {
            const form = document.getElementById('taskForm');
            if (form) form.reset();
            const taskAssignee = document.getElementById('taskAssignee');
            if (taskAssignee) taskAssignee.value = '';
        } else if (modalId === 'complaintModal') {
            const form = document.getElementById('complaintForm');
            if (form) form.reset();
            const cmpTech = document.getElementById('cmpTech');
            if (cmpTech) cmpTech.value = '';
        }
    }
}

function closeModal(modalId) {
    const modal = document.getElementById(modalId);
    if (modal) modal.classList.remove('active');
}

function checkAdminSecurityAuth() {
    localStorage.removeItem('revati_admin_auth');
    sessionStorage.removeItem('revati_admin_auth');
    const overlay = document.getElementById('securityAuthOverlay');
    if (overlay) {
        overlay.style.display = 'flex';
        const passInput = document.getElementById('adminSecretKeyInput');
        if (passInput) {
            passInput.value = '';
            passInput.focus();
        }
    }
}

function setupAdminSecurityForm() {
    const form = document.getElementById('securityAuthForm');
    if (form) {
        form.addEventListener('submit', (e) => {
            e.preventDefault();
            const passInput = document.getElementById('adminSecretKeyInput');
            const errDiv = document.getElementById('secAuthError');
            const enteredPass = passInput ? passInput.value.trim() : '';

            if (enteredPass === 'IPS_MIHIR_R_KADAM') {
                api.setCurrentUser({ id: 1, name: 'Revati Administrator', username: 'admin', role: 'ADMIN', email: 'admin@revatienterprises.com' });
                if (errDiv) errDiv.style.display = 'none';
                const overlay = document.getElementById('securityAuthOverlay');
                if (overlay) overlay.style.display = 'none';
                if (passInput) passInput.value = '';
                if (typeof loadAppState === 'function') loadAppState();
            } else {
                if (errDiv) {
                    errDiv.style.display = 'block';
                    errDiv.innerHTML = '<i class="fa-solid fa-triangle-exclamation"></i> Incorrect Security Password! Access Denied.';
                }
                if (passInput) {
                    passInput.value = '';
                    passInput.focus();
                }
            }
        });
    }
}

function lockAdminPortal() {
    localStorage.removeItem('revati_admin_auth');
    sessionStorage.removeItem('revati_admin_auth');
    const overlay = document.getElementById('securityAuthOverlay');
    if (overlay) overlay.style.display = 'flex';
    const passInput = document.getElementById('adminSecretKeyInput');
    if (passInput) {
        passInput.value = '';
        passInput.focus();
    }
}

function togglePassVisibility() {
    const passInput = document.getElementById('adminSecretKeyInput');
    const eyeIcon = document.getElementById('eyeIcon');
    if (passInput && eyeIcon) {
        if (passInput.type === 'password') {
            passInput.type = 'text';
            eyeIcon.className = 'fa-solid fa-eye-slash';
        } else {
            passInput.type = 'password';
            eyeIcon.className = 'fa-solid fa-eye';
        }
    }
}

/* LEAVE MANAGEMENT & REGISTERED WORKER EXPORT FUNCTIONS */
async function renderLeaveApplications() {
    const leaves = await api.getLeaves() || [];
    const tbody = document.getElementById('leavesAdminTableBody');
    if (!tbody) return;

    if (leaves.length === 0) {
        tbody.innerHTML = `<tr><td colspan="8" style="text-align: center; color: var(--text-muted); padding: 1.5rem;"><i class="fa-solid fa-umbrella-beach" style="color: var(--gold-primary); margin-right: 0.5rem;"></i> No leave applications submitted yet.</td></tr>`;
        return;
    }

    tbody.innerHTML = leaves.map(l => {
        let badgeClass = "badge-amber";
        if (l.status === 'Approved') badgeClass = "badge-completed";
        if (l.status === 'Rejected') badgeClass = "badge-danger";

        return `
            <tr>
                <td><strong>${l.empCode || 'REV-WORKER'}</strong></td>
                <td><strong style="color: #fff;">${l.empName || 'Staff Member'}</strong></td>
                <td><span class="badge badge-info">${l.leaveType}</span></td>
                <td><strong>${l.startDate}</strong> to <strong>${l.endDate}</strong></td>
                <td><div style="max-width: 250px; white-space: normal; font-size: 0.82rem;">${l.reason}</div></td>
                <td>${l.phoneOnLeave || 'N/A'}</td>
                <td><span class="badge ${badgeClass}">${l.status}</span></td>
                <td style="text-align: center;">
                    <div style="display: flex; gap: 0.35rem; justify-content: center;">
                        ${l.status === 'Pending' ? `
                            <button class="btn btn-primary btn-sm" onclick="handleApproveLeave(${l.id})"><i class="fa-solid fa-check"></i> Approve</button>
                            <button class="btn btn-secondary btn-sm" onclick="handleRejectLeave(${l.id})"><i class="fa-solid fa-xmark"></i> Reject</button>
                        ` : `
                            <span style="font-size: 0.78rem; color: var(--text-muted);"><i class="fa-solid fa-lock"></i> Decided</span>
                        `}
                        <button class="btn btn-danger btn-sm" onclick="handleDeleteLeave(${l.id})" title="Delete Record (Admin Only)"><i class="fa-solid fa-trash"></i> Delete</button>
                    </div>
                </td>
            </tr>
        `;
    }).join('');
}

async function handleApproveLeave(leaveId) {
    await api.updateLeaveStatus(leaveId, 'Approved', 'Approved by Operations Admin');
    await loadAppState();
    alert("Leave application approved!");
}

async function handleRejectLeave(leaveId) {
    const reason = prompt("Enter reason for leave rejection:", "Shift requirement on selected dates");
    if (reason !== null) {
        await api.updateLeaveStatus(leaveId, 'Rejected', reason);
        await loadAppState();
        alert("Leave application rejected.");
    }
}

async function handleDeleteLeave(leaveId) {
    const currentUser = api.getCurrentUser();
    if (currentUser.role !== 'ADMIN') {
        alert("⚠️ ACCESS DENIED: Only Company Administrator has authority to delete leave records.");
        return;
    }
    if (confirm("Are you sure you want to permanently delete this leave record?")) {
        await api.deleteRecord('/leaves', leaveId);
        await loadAppState();
        alert("Leave record deleted successfully.");
    }
}

async function renderRegisteredWorkers() {
    const emps = await api.request('/employees') || [];
    const tbody = document.getElementById('registeredWorkersTableBody');
    if (!tbody) return;

    if (emps.length === 0) {
        tbody.innerHTML = `<tr><td colspan="9" style="text-align: center; color: var(--text-muted); padding: 1.5rem;">No registered worker profiles.</td></tr>`;
        return;
    }

    tbody.innerHTML = emps.map(e => `
        <tr>
            <td><strong>${e.empCode || 'REV-WORKER'}</strong></td>
            <td><strong style="color: #fff;">${e.name}</strong><br><span style="font-size: 0.75rem; color: var(--text-muted);">${e.email || e.phone || ''}</span></td>
            <td><span class="badge badge-gold">${e.nationalityProofType || 'Aadhaar Card'}</span></td>
            <td><strong>${e.nationalityProofNo || 'Verified ID'}</strong></td>
            <td>${e.qualification || '10th / 12th Pass'}</td>
            <td>${e.skills || 'Facility Maintenance'}</td>
            <td><div style="max-width: 220px; font-size: 0.78rem; white-space: normal;">${e.address || 'Quarters Location'}</div></td>
            <td><span class="badge badge-present">${e.status || 'Active'}</span></td>
            <td style="text-align: center;">
                <button class="btn btn-danger btn-sm" onclick="deleteEmployeeRecord(${e.id})" title="Admin Delete Only"><i class="fa-solid fa-trash"></i> Delete</button>
            </td>
        </tr>
    `).join('');
}

function exportWorkersToExcel() {
    const emps = api.getLocalData().employees || [];
    ExcelExporter.exportWorkers(emps);
}

function exportAttendanceToExcel() {
    const att = api.getLocalData().attendance || [];
    ExcelExporter.exportAttendance(att);
}

function exportLeavesToExcel() {
    const leaves = api.getLocalData().leaves || [];
    ExcelExporter.exportLeaves(leaves);
}

function exportTasksToExcel() {
    const tasks = api.getLocalData().tasks || [];
    ExcelExporter.exportTasks(tasks);
}

// --- FIREBASE UI & REAL-TIME CLOUD SYNCHRONIZATION CONTROLLER ---
function setupFirebaseUI() {
    if (typeof firebaseService === 'undefined') return;

    firebaseService.onStatusChange((status, detail) => {
        const badgeBtn = document.getElementById('firebaseConfigBtn');
        const textSpan = document.getElementById('firebaseStatusText');
        if (!badgeBtn || !textSpan) return;

        if (status === 'connected') {
            badgeBtn.style.background = 'rgba(16, 185, 129, 0.15)';
            badgeBtn.style.borderColor = '#10B981';
            badgeBtn.style.color = '#10B981';
            textSpan.textContent = 'Firebase: 🟢 Connected (Cloud Sync)';
            setupRealtimeFirebaseSync();
        } else if (status === 'connecting') {
            badgeBtn.style.background = 'rgba(59, 130, 246, 0.15)';
            badgeBtn.style.borderColor = '#3B82F6';
            badgeBtn.style.color = '#3B82F6';
            textSpan.textContent = 'Firebase: 🔵 Syncing...';
        } else if (status === 'error') {
            badgeBtn.style.background = 'rgba(239, 68, 68, 0.15)';
            badgeBtn.style.borderColor = '#EF4444';
            badgeBtn.style.color = '#EF4444';
            textSpan.textContent = `Firebase: 🔴 Error (${detail || 'Auth/Network'})`;
        } else {
            badgeBtn.style.background = 'rgba(245, 158, 11, 0.15)';
            badgeBtn.style.borderColor = '#F59E0B';
            badgeBtn.style.color = '#F59E0B';
            textSpan.textContent = 'Firebase: 🟡 Local Fallback Mode';
        }
    });
}

function openFirebaseConfigModal() {
    const config = (typeof firebaseService !== 'undefined' && firebaseService.loadConfig()) || {};
    document.getElementById('fbApiKey').value = config.apiKey || '';
    document.getElementById('fbProjectId').value = config.projectId || '';
    document.getElementById('fbAuthDomain').value = config.authDomain || '';
    document.getElementById('fbStorageBucket').value = config.storageBucket || '';
    document.getElementById('fbAppId').value = config.appId || '';

    const statusEl = document.getElementById('fbConfigStatus');
    if (statusEl) statusEl.style.display = 'none';

    openModal('firebaseConfigModal');
}

async function saveFirebaseConfig(event) {
    event.preventDefault();
    const statusEl = document.getElementById('fbConfigStatus');
    statusEl.style.display = 'block';
    statusEl.style.background = 'rgba(59, 130, 246, 0.15)';
    statusEl.style.color = '#3B82F6';
    statusEl.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Connecting to Firebase Cloud Firestore...';

    const config = {
        apiKey: document.getElementById('fbApiKey').value.trim(),
        projectId: document.getElementById('fbProjectId').value.trim(),
        authDomain: document.getElementById('fbAuthDomain').value.trim(),
        storageBucket: document.getElementById('fbStorageBucket').value.trim(),
        appId: document.getElementById('fbAppId').value.trim()
    };

    const success = await firebaseService.saveConfig(config);
    if (success) {
        statusEl.style.background = 'rgba(16, 185, 129, 0.15)';
        statusEl.style.color = '#10B981';
        statusEl.innerHTML = '<i class="fa-solid fa-check-circle"></i> Connected to Firebase Cloud Firestore successfully!';
        
        // Seed initial data if Firestore is empty
        if (typeof INITIAL_DATA !== 'undefined') {
            await firebaseService.seedInitialDataIfEmpty(INITIAL_DATA);
        }
        
        setTimeout(() => {
            closeModal('firebaseConfigModal');
            loadAppState();
        }, 1200);
    } else {
        statusEl.style.background = 'rgba(239, 68, 68, 0.15)';
        statusEl.style.color = '#EF4444';
        statusEl.innerHTML = `<i class="fa-solid fa-triangle-exclamation"></i> Connection Failed. Please check API Key and Project ID.`;
    }
}

function clearFirebaseConfig() {
    if (confirm('Reset Firebase configuration and revert to local storage fallback mode?')) {
        firebaseService.clearConfig();
        closeModal('firebaseConfigModal');
        alert('Firebase configuration cleared. Switched to Local Fallback mode.');
    }
}

let isSyncingRealtime = false;
async function setupRealtimeFirebaseSync() {
    if (isSyncingRealtime || typeof firebaseService === 'undefined' || !firebaseService.isInitialized()) return;
    isSyncingRealtime = true;

    // Seed initial admin accounts & blank schema to Cloud Firestore if empty
    if (typeof INITIAL_DATA !== 'undefined' && firebaseService && firebaseService.isInitialized()) {
        try {
            await firebaseService.seedInitialDataIfEmpty(INITIAL_DATA);
        } catch (e) {
            console.warn('[FirebaseSync] Auto seed notice:', e);
        }
    }

    const collections = ['tasks', 'complaints', 'employees', 'attendance', 'leaves', 'inventory', 'users'];
    collections.forEach(coll => {
        firebaseService.subscribeCollection(coll, (items) => {
            if (items && items.length > 0) {
                const data = api.getLocalData();
                data[coll] = items;
                api.saveLocalData(data);
                
                // Re-render active view to show live cloud updates
                const activeNav = document.querySelector('.nav-item.active');
                if (activeNav) {
                    const currentView = activeNav.getAttribute('data-view');
                    renderViewData(currentView);
                }
            }
        });
    });
}
