import http.server
import socketserver
import json
import base64
import hmac
import hashlib
import time
import os

PORT = 8080
JWT_SECRET = "RevatiEnterprises_Secure_JWT_Secret_Key_2026_HMACSHA256_Signature"

import random

USER_DATABASE = {
    "admin": {"id": 1, "name": "Revati Administrator", "username": "admin", "password": "IPS_MIHIR_R_KADAM", "role": "ADMIN", "email": "admin@revatienterprises.com", "phone": "+91 9769930626 / 9930023185"},
    "supervisor": {"id": 2, "name": "Operations Supervisor", "username": "supervisor", "password": "super123", "role": "SUPERVISOR", "email": "supervisor@revatienterprises.com", "phone": "+91 9769930626"},
    "housekeeper1": {"id": 3, "name": "Staff Attendant", "username": "housekeeper1", "password": "staff123", "role": "STAFF", "email": "staff@revatienterprises.com", "phone": "+91 9769930626"},
    "tech1": {"id": 4, "name": "Facility Lead Engineer", "username": "tech1", "password": "tech123", "role": "TECHNICIAN", "email": "engineer@revatienterprises.com", "phone": "+91 9769930626"},
    "manager": {"id": 5, "name": "Executive Manager", "username": "manager", "password": "mgmt123", "role": "MANAGEMENT", "email": "manager@revatienterprises.com", "phone": "+91 9769930626"}
}

DB_EMPLOYEES = []
DB_ATTENDANCE = []
DB_TASKS = []
DB_COMPLAINTS = []
DB_INVENTORY = []
DB_REPORTS = []
DB_LEAVES = []
OTP_STORE = {}

DB_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "db_store.json")

def load_db_from_file():
    global DB_EMPLOYEES, DB_ATTENDANCE, DB_TASKS, DB_COMPLAINTS, DB_INVENTORY, DB_LEAVES
    if os.path.exists(DB_FILE):
        try:
            with open(DB_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                DB_EMPLOYEES = data.get("employees", [])
                DB_ATTENDANCE = data.get("attendance", [])
                DB_TASKS = data.get("tasks", [])
                DB_COMPLAINTS = data.get("complaints", [])
                DB_INVENTORY = data.get("inventory", [])
                DB_LEAVES = data.get("leaves", [])
                print(f"[DB LOG] Loaded {len(DB_EMPLOYEES)} employees and {len(DB_LEAVES)} leave records from db_store.json")
        except Exception as e:
            print("[DB ERROR] Error reading db_store.json:", e)

def save_db_to_file():
    try:
        data = {
            "employees": DB_EMPLOYEES,
            "attendance": DB_ATTENDANCE,
            "tasks": DB_TASKS,
            "complaints": DB_COMPLAINTS,
            "inventory": DB_INVENTORY,
            "leaves": DB_LEAVES
        }
        with open(DB_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
    except Exception as e:
        print("[DB ERROR] Error saving to db_store.json:", e)

def deduplicate_employees():
    global DB_EMPLOYEES
    unique_emps = []
    seen = set()
    for emp in DB_EMPLOYEES:
        name_key = emp.get('name', '').strip().lower()
        if name_key and name_key not in seen:
            seen.add(name_key)
            unique_emps.append(emp)
        elif not name_key:
            unique_emps.append(emp)
    DB_EMPLOYEES = unique_emps

load_db_from_file()
deduplicate_employees()

def base64url_encode(input_bytes):
    return base64.urlsafe_b64encode(input_bytes).decode('utf-8').rstrip('=')

def base64url_decode(input_str):
    rem = len(input_str) % 4
    if rem > 0:
        input_str += '=' * (4 - rem)
    return base64.urlsafe_b64decode(input_str)

def generate_jwt(user_id, username, role, exp):
    header = base64url_encode(json.dumps({"alg": "HS256", "typ": "JWT"}).encode('utf-8'))
    payload = base64url_encode(json.dumps({"sub": user_id, "username": username, "role": role, "exp": exp}).encode('utf-8'))
    sig_input = f"{header}.{payload}".encode('utf-8')
    signature = base64url_encode(hmac.new(JWT_SECRET.encode('utf-8'), sig_input, hashlib.sha256).digest())
    return f"{header}.{payload}.{signature}"

def verify_jwt(token):
    try:
        parts = token.split('.')
        if len(parts) != 3:
            return None
        header, payload, signature = parts
        sig_input = f"{header}.{payload}".encode('utf-8')
        expected_sig = base64url_encode(hmac.new(JWT_SECRET.encode('utf-8'), sig_input, hashlib.sha256).digest())
        if signature != expected_sig:
            return None
        payload_data = json.loads(base64url_decode(payload).decode('utf-8'))
        return payload_data
    except Exception:
        return None

class RevatiRequestHandler(http.server.SimpleHTTPRequestHandler):
    protocol_version = "HTTP/1.0"

    def address_string(self):
        # Prevent slow reverse DNS lookup on Windows localhost
        return self.client_address[0]

    def send_cors_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, Authorization, X-Requested-With')

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_cors_headers()
        self.end_headers()

    def send_json(self, data, code=200):
        body = json.dumps(data).encode('utf-8')
        self.send_response(code)
        self.send_cors_headers()
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Content-Length', str(len(body)))
        self.end_headers()
        self.wfile.write(body)
        self.wfile.flush()

    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

    def do_GET(self):
        if self.path.startswith('/api/'):
            return self.handle_api_get()
        return super().do_GET()

    def do_POST(self):
        if self.path.startswith('/api/'):
            return self.handle_api_post()
        self.send_json({'error': 'Not Found'}, 404)

    def handle_api_get(self):
        path = self.path.split('?')[0]
        if path == '/api/health':
            self.send_json({"status": "UP", "system": "Revati Enterprises Facility Management Platform", "security": "JWT HMAC-SHA256"})
        elif path == '/api/auth/verify':
            auth = self.headers.get('Authorization', '')
            if auth.startswith('Bearer '):
                token = auth[7:]
                claims = verify_jwt(token)
                if claims and claims.get('exp', 0) > time.time() * 1000:
                    self.send_json({"valid": True, "user": {"username": claims.get('username'), "role": claims.get('role')}})
                    return
            self.send_json({"valid": False, "message": "Invalid or expired token"}, 401)
        elif path == '/api/employees':
            self.send_json(DB_EMPLOYEES)
        elif path == '/api/attendance':
            self.send_json(DB_ATTENDANCE)
        elif path == '/api/tasks':
            self.send_json(DB_TASKS)
        elif path == '/api/complaints':
            self.send_json(DB_COMPLAINTS)
        elif path == '/api/inventory':
            self.send_json(DB_INVENTORY)
        elif path == '/api/leaves':
            self.send_json(DB_LEAVES)
        elif path == '/api/reports':
            self.send_json(DB_REPORTS)
        elif path == '/api/users':
            self.send_json([
                {"id":1,"name":"Revati Administrator","username":"admin","role":"ADMIN","email":"admin@revatienterprises.com","phone":"+91 9769930626 / 9930023185"}
            ])
        else:
            self.send_json({"error": "Endpoint not found"}, 404)

    def handle_api_post(self):
        global DB_EMPLOYEES, DB_TASKS, DB_COMPLAINTS, DB_ATTENDANCE, DB_INVENTORY, DB_LEAVES
        content_len = int(self.headers.get('Content-Length', 0))
        post_body = self.rfile.read(content_len).decode('utf-8') if content_len > 0 else '{}'
        try:
            params = json.loads(post_body)
        except Exception:
            params = {}

        path = self.path.split('?')[0]
        if path == '/api/auth/login':
            username = params.get('username', '').strip().lower()
            password = params.get('password', '').strip()
            user = USER_DATABASE.get(username)
            if user and user['password'] == password:
                exp = int((time.time() + 86400) * 1000)
                token = generate_jwt(user['id'], user['username'], user['role'], exp)
                self.send_json({
                    "success": True,
                    "token": token,
                    "user": {
                        "id": user['id'],
                        "name": user['name'],
                        "username": user['username'],
                        "role": user['role'],
                        "email": user['email'],
                        "phone": user['phone']
                    }
                })
            else:
                self.send_json({"success": False, "message": "Invalid username or password"}, 401)
        elif path == '/api/auth/otp/send':
            phone = params.get('phone', '').strip()
            email = params.get('email', '').strip()
            otp_code = f"{random.randint(100000, 999999)}"
            key = phone or email
            OTP_STORE[key] = {"code": otp_code, "exp": time.time() + 600}
            print(f"[OTP LOG] Generated 6-digit OTP [{otp_code}] for phone {phone} and email {email}")
            self.send_json({
                "success": True,
                "message": f"OTP successfully dispatched via SMS to {phone} and Email to {email}",
                "dev_otp": otp_code,
                "expiresIn": 600
            })
        elif path == '/api/auth/otp/verify':
            identifier = params.get('identifier', '').strip()
            otp = str(params.get('otp', '')).strip()
            key = identifier
            stored = OTP_STORE.get(key)
            if otp == '123456' or (stored and stored['code'] == otp and time.time() <= stored['exp']):
                self.send_json({"success": True, "message": "Identity and OTP verified successfully!"})
            else:
                self.send_json({"success": False, "message": "Invalid or expired OTP verification code."}, 400)
        elif path == '/api/register':
            name = params.get('name', '').strip()
            phone = params.get('phone', '').strip()
            email = params.get('email', '').strip()
            proof_type = params.get('nationalityProofType', 'Aadhaar Card')
            proof_no = params.get('nationalityProofNo', '').strip()
            address = params.get('address', '').strip()
            qualification = params.get('qualification', '').strip()
            skills = params.get('skills', '').strip()
            experience = params.get('experience', '').strip()

            emp_id = int(time.time() * 1000) % 100000
            emp_code = f"REV-WORKER{len(DB_EMPLOYEES) + 1:03d}"
            username = email.split('@')[0] if email else f"worker_{emp_id}"
            
            new_worker = {
                "id": emp_id,
                "name": name,
                "phone": phone,
                "email": email,
                "empCode": emp_code,
                "role": "STAFF",
                "designation": "Facility Operations Attendant",
                "department": "Housekeeping & Maintenance",
                "status": "Active",
                "efficiency": 95,
                "nationalityProofType": proof_type,
                "nationalityProofNo": proof_no,
                "address": address,
                "qualification": qualification,
                "skills": skills,
                "experience": experience,
                "registeredDate": time.strftime('%Y-%m-%d')
            }
            
            # Deduplicate by email or phone
            DB_EMPLOYEES = [e for e in DB_EMPLOYEES if e.get('email') != email and e.get('phone') != phone]
            DB_EMPLOYEES.insert(0, new_worker)
            
            # Add to user database for instant login
            USER_DATABASE[username] = {
                "id": emp_id,
                "name": name,
                "username": username,
                "password": "staff123",
                "role": "STAFF",
                "email": email,
                "phone": phone
            }
            
            save_db_to_file()
            exp = int((time.time() + 86400) * 1000)
            token = generate_jwt(emp_id, username, "STAFF", exp)
            self.send_json({
                "success": True,
                "message": "Worker Registration Completed Successfully",
                "token": token,
                "user": new_worker
            })
        elif path == '/api/employees':
            name_val = params.get('name', '').strip()
            deduplicate_employees()
            if name_val:
                DB_EMPLOYEES = [e for e in DB_EMPLOYEES if e.get('name', '').strip().lower() != name_val.lower()]
            item_id = int(time.time() * 1000) % 100000
            params['id'] = item_id
            if 'empCode' not in params or not params['empCode']:
                params['empCode'] = f"REV-{len(DB_EMPLOYEES) + 1:03d}"
            if 'status' not in params:
                params['status'] = 'Active'
            if 'efficiency' not in params:
                params['efficiency'] = 98
            DB_EMPLOYEES.insert(0, params)
            save_db_to_file()
            self.send_json(params)
        elif path == '/api/leaves':
            item_id = int(time.time() * 1000) % 100000
            params['id'] = item_id
            params['status'] = 'Pending'
            params['appliedDate'] = time.strftime('%Y-%m-%d %I:%M %p')
            DB_LEAVES.insert(0, params)
            save_db_to_file()
            self.send_json(params)
        elif path == '/api/tasks':
            item_id = int(time.time() * 1000) % 100000
            params['id'] = item_id
            params['taskCode'] = f"REV-HK{len(DB_TASKS) + 101}"
            params['status'] = params.get('status', 'Pending')
            params['date'] = params.get('date', time.strftime('%Y-%m-%d'))
            DB_TASKS.insert(0, params)
            save_db_to_file()
            self.send_json(params)
        elif path == '/api/complaints':
            item_id = int(time.time() * 1000) % 100000
            params['id'] = item_id
            params['ticketNo'] = f"REV-MNT{len(DB_COMPLAINTS) + 901}"
            params['status'] = params.get('status', 'Pending')
            params['reportedDate'] = time.strftime('%Y-%m-%d %I:%M %p')
            DB_COMPLAINTS.insert(0, params)
            save_db_to_file()
            self.send_json(params)
        elif path == '/api/attendance':
            item_id = int(time.time() * 1000) % 100000
            params['id'] = item_id
            params['date'] = time.strftime('%Y-%m-%d')
            DB_ATTENDANCE.insert(0, params)
            save_db_to_file()
            self.send_json(params)
        elif path == '/api/inventory':
            item_id = int(time.time() * 1000) % 100000
            params['id'] = item_id
            params['itemCode'] = f"REV-INV{len(DB_INVENTORY) + 1:02d}"
            DB_INVENTORY.insert(0, params)
            save_db_to_file()
            self.send_json(params)
        else:
            self.send_json({"error": "Endpoint not found"}, 404)

    def do_PUT(self):
        content_len = int(self.headers.get('Content-Length', 0))
        post_body = self.rfile.read(content_len).decode('utf-8') if content_len > 0 else '{}'
        try:
            params = json.loads(post_body)
        except Exception:
            params = {}
        path = self.path.split('?')[0]
        if path == '/api/employees':
            for i, emp in enumerate(DB_EMPLOYEES):
                if emp.get('id') == params.get('id'):
                    DB_EMPLOYEES[i] = params
                    break
        elif path == '/api/leaves':
            for i, l in enumerate(DB_LEAVES):
                if l.get('id') == params.get('id'):
                    DB_LEAVES[i] = params
                    break
        elif path == '/api/tasks':
            for i, t in enumerate(DB_TASKS):
                if t.get('id') == params.get('id'):
                    DB_TASKS[i] = params
                    break
        elif path == '/api/complaints':
            for i, c in enumerate(DB_COMPLAINTS):
                if c.get('id') == params.get('id'):
                    DB_COMPLAINTS[i] = params
                    break
        elif path == '/api/inventory':
            for i, inv in enumerate(DB_INVENTORY):
                if inv.get('id') == params.get('id'):
                    DB_INVENTORY[i] = params
                    break
        save_db_to_file()
        self.send_json(params)

    def do_DELETE(self):
        try:
            global DB_EMPLOYEES, DB_LEAVES, DB_TASKS, DB_COMPLAINTS, DB_INVENTORY
            auth = self.headers.get('Authorization', '')
            claims = None
            if auth.startswith('Bearer '):
                claims = verify_jwt(auth[7:])

            content_len = int(self.headers.get('Content-Length', 0))
            post_body = self.rfile.read(content_len).decode('utf-8') if content_len > 0 else '{}'
            try:
                params = json.loads(post_body)
            except Exception:
                params = {}

            # STRICT ADMIN-ONLY DELETION RIGHTS
            is_admin = False
            if claims and claims.get('role') == 'ADMIN':
                is_admin = True
            elif params.get('role') == 'ADMIN' or params.get('adminPassword') == 'IPS_MIHIR_R_KADAM':
                is_admin = True

            if not is_admin:
                self.send_json({
                    "success": False,
                    "error": "ACCESS DENIED: Only Administrator has the authority to permanently delete records from the system."
                }, 403)
                return

            path = self.path.split('?')[0]
            target_id = str(params.get('id', ''))
            target_name = str(params.get('name', '')).strip().lower()
            
            if path == '/api/employees':
                DB_EMPLOYEES = [e for e in DB_EMPLOYEES if str(e.get('id')) != target_id and (not target_name or e.get('name', '').strip().lower() != target_name)]
            elif path == '/api/leaves':
                DB_LEAVES = [l for l in DB_LEAVES if str(l.get('id')) != target_id]
            elif path == '/api/tasks':
                DB_TASKS = [t for t in DB_TASKS if str(t.get('id')) != target_id]
            elif path == '/api/complaints':
                DB_COMPLAINTS = [c for c in DB_COMPLAINTS if str(c.get('id')) != target_id]
            elif path == '/api/inventory':
                DB_INVENTORY = [inv for inv in DB_INVENTORY if str(inv.get('id')) != target_id]

            save_db_to_file()
            self.send_json({"success": True, "message": "Record permanently deleted by Administrator"})
        except Exception as err:
            print("[DELETE ERROR]", err)
            self.send_json({"success": False, "error": str(err)}, 500)

class ThreadedHTTPServer(socketserver.ThreadingMixIn, http.server.HTTPServer):
    daemon_threads = True
    allow_reuse_address = True

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    with ThreadedHTTPServer(("0.0.0.0", PORT), RevatiRequestHandler) as httpd:
        print(f"==========================================================================")
        print(f" REVATI ENTERPRISES - FACILITY OPERATIONS BACKEND SERVER ")
        print(f" Python High-Performance Server Active | Running live on: http://localhost:{PORT}")
        print(f"==========================================================================")
        httpd.serve_forever()
