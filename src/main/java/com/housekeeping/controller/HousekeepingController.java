package com.housekeeping.controller;

import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.*;

/**
 * Spring Boot REST Controller
 * Commercial Housekeeping and Maintenance System
 * Exposes API endpoints for Users, Employees, Attendance, Tasks, Complaints, Inventory, and Reports.
 */
@RestController
@RequestMapping("/api")
@CrossOrigin(origins = "*")
public class HousekeepingController {

    @GetMapping("/health")
    public ResponseEntity<Map<String, String>> healthCheck() {
        Map<String, String> status = new HashMap<>();
        status.put("status", "UP");
        status.put("framework", "Spring Boot 2.7");
        status.put("project", "Commercial Housekeeping and Maintenance System");
        status.put("author", "Mihir R. Kadam (T082)");
        return ResponseEntity.ok(status);
    }

    @PostMapping("/auth/login")
    public ResponseEntity<Map<String, Object>> login(@RequestBody Map<String, String> credentials) {
        Map<String, Object> response = new HashMap<>();
        response.put("success", true);
        response.put("message", "User authenticated successfully");
        response.put("role", credentials.getOrDefault("role", "ADMIN"));
        return ResponseEntity.ok(response);
    }

    @GetMapping("/employees")
    public ResponseEntity<List<Map<String, Object>>> getEmployees() {
        List<Map<String, Object>> employees = new ArrayList<>();
        
        Map<String, Object> e1 = new HashMap<>();
        e1.put("id", 101);
        e1.put("empCode", "EMP-001");
        e1.put("name", "Suresh Kumar");
        e1.put("department", "Housekeeping");
        e1.put("designation", "Senior Housekeeper");
        e1.put("status", "Active");
        e1.put("shift", "Morning (07:00 - 15:30)");
        e1.put("efficiency", 96);
        employees.add(e1);

        Map<String, Object> e2 = new HashMap<>();
        e2.put("id", 102);
        e2.put("empCode", "EMP-002");
        e2.put("name", "Pooja Patil");
        e2.put("department", "Housekeeping");
        e2.put("designation", "Housekeeping Attendant");
        e2.put("status", "Active");
        e2.put("shift", "Morning (07:00 - 15:30)");
        e2.put("efficiency", 92);
        employees.add(e2);

        return ResponseEntity.ok(employees);
    }

    @GetMapping("/tasks")
    public ResponseEntity<List<Map<String, Object>>> getTasks() {
        List<Map<String, Object>> tasks = new ArrayList<>();
        Map<String, Object> t1 = new HashMap<>();
        t1.put("id", 301);
        t1.put("taskCode", "HK-101");
        t1.put("title", "Executive Suite 401 Deep Cleaning");
        t1.put("area", "4th Floor - Suite 401");
        t1.put("assignedTo", "Suresh Kumar");
        t1.put("status", "Completed");
        tasks.add(t1);
        return ResponseEntity.ok(tasks);
    }

    @GetMapping("/complaints")
    public ResponseEntity<List<Map<String, Object>>> getComplaints() {
        List<Map<String, Object>> complaints = new ArrayList<>();
        Map<String, Object> c1 = new HashMap<>();
        c1.put("id", 401);
        c1.put("ticketNo", "MNT-901");
        c1.put("title", "AHU-2 Air Conditioning Cooling Defect");
        c1.put("category", "HVAC");
        c1.put("status", "In Progress");
        complaints.add(c1);
        return ResponseEntity.ok(complaints);
    }
}
