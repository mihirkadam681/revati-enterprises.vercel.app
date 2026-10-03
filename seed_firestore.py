import urllib.request
import json
import os

API_KEY = "AIzaSyAOZJf89jiisnUX5kTNVbZaZZ2YSPHVZCE"
PROJECT_ID = "revati-enterprises-178f1"
BASE_URL = f"https://firestore.googleapis.com/v1/projects/{PROJECT_ID}/databases/(default)/documents"

def to_firestore_value(val):
    if isinstance(val, bool):
        return {"booleanValue": val}
    elif isinstance(val, int):
        return {"integerValue": str(val)}
    elif isinstance(val, float):
        return {"doubleValue": val}
    elif isinstance(val, str):
        return {"stringValue": val}
    elif isinstance(val, list):
        return {"arrayValue": {"values": [to_firestore_value(x) for x in val]}}
    elif isinstance(val, dict):
        return {"mapValue": {"fields": {k: to_firestore_value(v) for k, v in val.items()}}}
    else:
        return {"stringValue": str(val)}

def save_doc(collection, doc_id, data):
    fields = {k: to_firestore_value(v) for k, v in data.items()}
    payload = json.dumps({"fields": fields}).encode("utf-8")
    
    # Try PATCH first (creates or replaces document cleanly)
    patch_url = f"{BASE_URL}/{collection}/{doc_id}?key={API_KEY}"
    req = urllib.request.Request(patch_url, data=payload, headers={"Content-Type": "application/json"}, method="PATCH")
    try:
        with urllib.request.urlopen(req) as resp:
            print(f"[OK] Seeded {collection}/{doc_id}")
    except Exception as e:
        print(f"[ERROR] Failed {collection}/{doc_id}: {e}")

print("Seeding Revati Enterprises Cloud Firestore Collections...")

# 1. USERS
users = [
    {"id": 1, "name": "Revati Administrator", "username": "admin", "role": "ADMIN", "email": "admin@revatienterprises.com", "phone": "+91 9769930626"},
    {"id": 2, "name": "Operations Lead", "username": "manager", "role": "MANAGEMENT", "email": "manager@revatienterprises.com", "phone": "+91 9930023185"},
    {"id": 3, "name": "Site Supervisor", "username": "supervisor", "role": "SUPERVISOR", "email": "supervisor@revati.com", "phone": "+91 9820011223"}
]
for u in users:
    save_doc("users", u["username"], u)

# 2. EMPLOYEES
employees = [
    {
        "id": 101,
        "empCode": "REV-EMP001",
        "name": "Rahul S. Sharma",
        "role": "STAFF",
        "designation": "Senior Housekeeping Lead",
        "department": "Housekeeping Operations",
        "phone": "+91 9820123456",
        "email": "rahul.sharma@revati.com",
        "gender": "Male",
        "address": "Andheri East, Mumbai, Maharashtra 400069",
        "nationalityProofType": "Aadhaar Card",
        "nationalityProofNo": "7890-1234-5678",
        "qualification": "HSC Certified in Hospitality & Hygiene",
        "experience": "5 Years",
        "skills": "Floor Scrubbing, Facade Rope Access, Chemical Handling",
        "status": "Active",
        "efficiency": 98,
        "registeredDate": "2026-01-15"
    },
    {
        "id": 102,
        "empCode": "REV-EMP002",
        "name": "Pooja V. Kamble",
        "role": "STAFF",
        "designation": "Hygiene & Sanitization Specialist",
        "department": "Hospital & Washroom Hygiene",
        "phone": "+91 9833445566",
        "email": "pooja.kamble@revati.com",
        "gender": "Female",
        "address": "Kalyan West, Thane District, Maharashtra 421301",
        "nationalityProofType": "Aadhaar Card",
        "nationalityProofNo": "5432-8765-4321",
        "qualification": "Graduate (Hygiene Safety Certification)",
        "experience": "3 Years",
        "skills": "Hospital Disinfection, Bio-hazard Protocol, Inventory Control",
        "status": "Active",
        "efficiency": 96,
        "registeredDate": "2026-02-01"
    },
    {
        "id": 103,
        "empCode": "REV-EMP003",
        "name": "Amit Kumar Yadav",
        "role": "STAFF",
        "designation": "High-Rise Glass Facade Technician",
        "department": "Facade & Glass Maintenance",
        "phone": "+91 9769112233",
        "email": "amit.yadav@revati.com",
        "gender": "Male",
        "address": "Navi Mumbai, Maharashtra 400705",
        "nationalityProofType": "PAN Card",
        "nationalityProofNo": "ABCDE1234F",
        "qualification": "IRATA Rope Access Certified Level 1",
        "experience": "4 Years",
        "skills": "Cradle Operation, High-Rise BMU, Safety Anchor Systems",
        "status": "Active",
        "efficiency": 94,
        "registeredDate": "2026-03-10"
    }
]
for emp in employees:
    save_doc("employees", emp["empCode"], emp)

# 3. TASKS
tasks = [
    {
        "id": 201,
        "taskCode": "REV-HK101",
        "title": "High-Rise Glass Facade Cleaning & BMU Cradle Inspection",
        "area": "Tower A - Floors 10 to 25 (External Glass)",
        "assignedTo": "Amit Kumar Yadav (REV-EMP003)",
        "shift": "Morning (07:00 AM - 03:00 PM)",
        "priority": "High",
        "date": "2026-10-03",
        "status": "In Progress",
        "inspectedBy": "Operations Lead",
        "notes": "Check safety harness & weather wind speed before descent."
    },
    {
        "id": 202,
        "taskCode": "REV-HK102",
        "title": "Executive Lobby Deep Scrubbing & Marble Crystallization",
        "area": "Ground Floor Main Lobby & Reception",
        "assignedTo": "Rahul S. Sharma (REV-EMP001)",
        "shift": "Night (10:00 PM - 06:00 AM)",
        "priority": "Medium",
        "date": "2026-10-03",
        "status": "Completed",
        "inspectedBy": "Site Supervisor",
        "notes": "Completed using Taski R2 & single disc buffer machine."
    },
    {
        "id": 203,
        "taskCode": "REV-HK103",
        "title": "Restroom Sanitization & Bio-Enzymatic Dosing",
        "area": "Floors 1 through 8 Restrooms",
        "assignedTo": "Pooja V. Kamble (REV-EMP002)",
        "shift": "Morning (08:00 AM - 04:00 PM)",
        "priority": "High",
        "date": "2026-10-03",
        "status": "Completed",
        "inspectedBy": "Site Supervisor",
        "notes": "All dispensers refilled, odor neutralizer applied."
    }
]
for t in tasks:
    save_doc("tasks", t["taskCode"], t)

# 4. INVENTORY
inventory = [
    {"id": 301, "itemCode": "INV-CH01", "itemName": "Diversey Taski R2 All-Purpose Floor Cleaner", "category": "Chemicals", "quantity": 45, "unit": "Liters", "reorderLevel": 15, "status": "In Stock"},
    {"id": 302, "itemCode": "INV-CH02", "itemName": "Diversey Taski R3 Glass & Mirror Cleaner", "category": "Chemicals", "quantity": 28, "unit": "Liters", "reorderLevel": 10, "status": "In Stock"},
    {"id": 303, "itemCode": "INV-EQ01", "itemName": "Taski Ergodisc 165 Heavy Duty Single Disc Scrubber", "category": "Machinery", "quantity": 4, "unit": "Units", "reorderLevel": 2, "status": "In Stock"},
    {"id": 304, "itemCode": "INV-EQ02", "itemName": "Industrial Wet & Dry Vacuum Cleaner 80L", "category": "Machinery", "quantity": 6, "unit": "Units", "reorderLevel": 3, "status": "In Stock"},
    {"id": 305, "itemCode": "INV-CN01", "itemName": "Microfiber Color-Coded Wiping Cloths (Pack of 50)", "category": "Consumables", "quantity": 8, "unit": "Packs", "reorderLevel": 10, "status": "Low Stock"},
    {"id": 306, "itemCode": "INV-PP01", "itemName": "Nitrile Chemical Resistant Safety Gloves", "category": "Safety PPE", "quantity": 120, "unit": "Pairs", "reorderLevel": 40, "status": "In Stock"}
]
for inv in inventory:
    save_doc("inventory", inv["itemCode"], inv)

# 5. COMPLAINTS
complaints = [
    {
        "id": 401,
        "ticketCode": "TKT-2026-001",
        "clientName": "Nesco IT Park Tower 4 Management",
        "siteName": "Goregaon East, Mumbai",
        "issueType": "Glass Water Stain Cleaning Request",
        "severity": "Moderate",
        "status": "In Progress",
        "reportedDate": "2026-10-02",
        "description": "Monsoon mineral streaks visible on 14th floor south facing glass panels.",
        "resolutionNotes": "Assigned to facade team for scheduled Saturday morning BMU wash."
    },
    {
        "id": 402,
        "ticketCode": "TKT-2026-002",
        "clientName": "Hiranandani Business Park Corp",
        "siteName": "Powai, Mumbai",
        "issueType": "Cafeteria Deep Scrubbing Request",
        "severity": "Low",
        "status": "Resolved",
        "reportedDate": "2026-09-28",
        "description": "Quarterly grease strip and high-pressure steam cleaning in food court zone.",
        "resolutionNotes": "Completed overnight Sunday. Client signed SLA clearance sheet."
    }
]
for c in complaints:
    save_doc("complaints", c["ticketCode"], c)

# 6. ATTENDANCE
attendance = [
    {"id": 501, "empCode": "REV-EMP001", "name": "Rahul S. Sharma", "date": "2026-10-03", "punchInTime": "06:55 AM", "punchOutTime": "--", "status": "Present", "site": "Nesco IT Park"},
    {"id": 502, "empCode": "REV-EMP002", "name": "Pooja V. Kamble", "date": "2026-10-03", "punchInTime": "07:45 AM", "punchOutTime": "--", "status": "Present", "site": "Hiranandani Powai"},
    {"id": 503, "empCode": "REV-EMP003", "name": "Amit Kumar Yadav", "date": "2026-10-03", "punchInTime": "06:50 AM", "punchOutTime": "--", "status": "Present", "site": "One BKC Tower"}
]
for a in attendance:
    save_doc("attendance", str(a["id"]), a)

# 7. LEAVES
leaves = [
    {
        "id": 601,
        "empCode": "REV-EMP002",
        "name": "Pooja V. Kamble",
        "leaveType": "Casual Leave",
        "startDate": "2026-10-10",
        "endDate": "2026-10-12",
        "days": 3,
        "reason": "Family festival function in hometown",
        "status": "Approved",
        "appliedDate": "2026-10-01 11:30 AM"
    }
]
for l in leaves:
    save_doc("leaves", str(l["id"]), l)

print("ALL COLLECTIONS SEEDED SUCCESSFULLY!")
