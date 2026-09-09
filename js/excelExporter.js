// REVATI ENTERPRISES - Official Excel Export Service Engine
// Converts data tables into Microsoft Excel (.xlsx / .csv) formats with UTF-8 BOM for full character support

class ExcelExporter {
    static exportToCSV(filename, headers, rows) {
        let csvContent = "\uFEFF"; // UTF-8 BOM for Microsoft Excel auto-encoding
        
        // Add Header Row
        csvContent += headers.map(h => `"${String(h).replace(/"/g, '""')}"`).join(",") + "\r\n";
        
        // Add Data Rows
        rows.forEach(row => {
            const rowData = row.map(val => {
                if (val === null || val === undefined) return '""';
                return `"${String(val).replace(/"/g, '""')}"`;
            });
            csvContent += rowData.join(",") + "\r\n";
        });

        // Trigger Download
        const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' });
        const url = URL.createObjectURL(blob);
        const link = document.createElement('a');
        link.setAttribute('href', url);
        link.setAttribute('download', `${filename}_${new Date().toISOString().split('T')[0]}.csv`);
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
    }

    static exportWorkers(employees) {
        const headers = [
            "Employee Code",
            "Full Name",
            "Phone Number",
            "Email Address",
            "Nationality Proof Type",
            "Proof ID Number",
            "Residential Address",
            "Qualifications & Degrees",
            "Skills & Expertise",
            "Experience",
            "Role",
            "Department",
            "Status",
            "Registration Date"
        ];

        const rows = employees.map(emp => [
            emp.empCode || 'N/A',
            emp.name || 'N/A',
            emp.phone || 'N/A',
            emp.email || 'N/A',
            emp.nationalityProofType || 'Aadhaar Card',
            emp.nationalityProofNo || 'N/A',
            emp.address || 'N/A',
            emp.qualification || 'N/A',
            emp.skills || 'N/A',
            emp.experience || 'N/A',
            emp.role || 'STAFF',
            emp.department || 'Operations',
            emp.status || 'Active',
            emp.registeredDate || 'N/A'
        ]);

        this.exportToCSV("Revati_Worker_Registration_Directory", headers, rows);
    }

    static exportAttendance(attendance) {
        const headers = [
            "Record ID",
            "Date",
            "Employee Code / Name",
            "Punch In Time",
            "Punch Out Time",
            "GPS Location / Site Address",
            "Shift / Status"
        ];

        const rows = attendance.map(att => [
            att.id || 'N/A',
            att.date || new Date().toISOString().split('T')[0],
            att.employeeName || att.empCode || 'Staff Member',
            att.timeIn || att.time || '09:00 AM',
            att.timeOut || '06:00 PM',
            att.location || 'Client On-Site Location',
            att.status || 'Present'
        ]);

        this.exportToCSV("Revati_Attendance_Log_Sheet", headers, rows);
    }

    static exportLeaves(leaves) {
        const headers = [
            "Application ID",
            "Employee Name",
            "Employee Code",
            "Leave Type",
            "Start Date",
            "End Date",
            "Total Days",
            "Reason / Justification",
            "Contact Phone During Leave",
            "Application Date",
            "Approval Status",
            "Admin Remarks"
        ];

        const rows = leaves.map(l => [
            l.id || 'N/A',
            l.empName || 'Staff Attendant',
            l.empCode || 'REV-WORKER',
            l.leaveType || 'Casual Leave',
            l.startDate || 'N/A',
            l.endDate || 'N/A',
            l.totalDays || 1,
            l.reason || 'Personal Work',
            l.phoneOnLeave || 'N/A',
            l.appliedDate || 'N/A',
            l.status || 'Pending',
            l.adminComment || 'N/A'
        ]);

        this.exportToCSV("Revati_Staff_Leave_Applications", headers, rows);
    }

    static exportTasks(tasks) {
        const headers = [
            "Task Code",
            "Task Title / Description",
            "Duty Location / Site Address",
            "Assigned Worker",
            "Priority",
            "Scheduled Date",
            "Status",
            "Inspection Notes"
        ];

        const rows = tasks.map(t => [
            t.taskCode || 'REV-HK',
            t.title || t.description || 'Facility Housekeeping Task',
            t.location || 'Client Facility',
            t.assignedTo || 'Unassigned',
            t.priority || 'Normal',
            t.date || new Date().toISOString().split('T')[0],
            t.status || 'Pending',
            t.inspectedBy || 'Pending'
        ]);

        this.exportToCSV("Revati_Duty_Task_Assignments", headers, rows);
    }
}
