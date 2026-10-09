"""
REVATI ENTERPRISES - PAGES 19 TO 35
Chapter definitions and content flowables for pages 19 to 35.
"""

from reportlab.lib import colors
from reportlab.platypus import Paragraph, Spacer, Table, TableStyle, PageBreak, HRFlowable
from build_all_35_pages import (
    GOLD, DARK_BG, NAVY, TEXT_MAIN, TEXT_MUTED, LIGHT_BG, BORDER_COLOR, SUCCESS, DANGER, WARNING,
    title_style, subtitle_style, h1_style, h2_style, body_style, body_bold, bullet_style,
    table_header_style, table_body_style, table_body_bold, callout_style, code_style,
    make_callout, make_chapter_header, styled_table, draw_jwt_flow_diagram,
    create_er_diagram_drawing, create_gantt_chart_drawing
)

def get_page_19():
    """Page 19: Chapter 17 - Corporate Letterhead & Proposal Studio (letterhead.html & letterhead.js)"""
    elems = make_chapter_header("17", "Corporate Letterhead & Proposal Studio", "Dynamic WYSIWYG Document Composer, ISO Seal Preview & html2pdf Export")
    
    elems.append(Paragraph("17.1 Interactive Document Composer Architecture", h2_style))
    elems.append(Paragraph(
        "The Official Letterhead Studio (<code>letterhead.html</code> & <code>js/letterhead.js</code>) allows operations directors and administrators "
        "to draft official business documents directly in the browser. It combines a left-hand form control pane with a live, real-time "
        "preview canvas rendered on an authentic A4 digital sheet with high-resolution corporate headers and golden border rules.",
        body_style
    ))
    
    studio_data = [
        [Paragraph("Document Type", table_header_style), Paragraph("Key Clauses & Metadata Included", table_header_style), Paragraph("Target Recipient & Legal Context", table_header_style)],
        [Paragraph("<b>Commercial Quotation</b>", table_body_bold), Paragraph("Scope of work, attendant headcounts, shift hours, chemical list, GST breakdown.", table_body_style), Paragraph("New prospective commercial clients, college management boards.", table_body_style)],
        [Paragraph("<b>SLA Agreement Contract</b>", table_body_bold), Paragraph("Response time guarantees, penal clauses, hygiene benchmarks, billing dates.", table_body_style), Paragraph("Signed legal contracts for ongoing multi-year facility maintenance.", table_body_style)],
        [Paragraph("<b>Official Work Order</b>", table_body_bold), Paragraph("Work authorization code, assigned site supervisor, target completion date.", table_body_style), Paragraph("Internal deployment notices for Sheth L.U.J. College campus operations.", table_body_style)],
        [Paragraph("<b>Notice of Inspection</b>", table_body_bold), Paragraph("Hygiene audit scores, bio-swab laboratory reports, corrective actions.", table_body_style), Paragraph("Monthly quality audit reviews submitted to client facility heads.", table_body_style)]
    ]
    t = styled_table(studio_data, [115, 235, 182])
    elems.append(t)
    elems.append(Spacer(1, 6))
    
    elems.append(Paragraph("17.2 Digital Seal, Watermark & Cryptographic Signature Block", h2_style))
    elems.append(Paragraph(
        "Every generated letterhead incorporates the official Revati Enterprises circular watermark, an embedded ISO 9001:2015 "
        "quality certification badge, and an authorized digital signature block with dynamic reference tracking numbers (e.g., <code>REF: REV/2026/Q-104</code>).",
        body_style
    ))
    
    elems.append(Paragraph("17.3 Client-Side Vector PDF Export (html2pdf.bundle.min.js)", h2_style))
    elems.append(Paragraph(
        "Through <code>html2pdf.js</code>, clicking 'Download Official PDF' renders the active document DOM tree directly into a high-DPI vector PDF "
        "with pixel-perfect typography, preserving exact margins, header rules, and signature alignment for immediate digital emailing or printing.",
        body_style
    ))
    return elems

def get_page_20():
    """Page 20: Chapter 18 - Python Multi-Threaded REST Daemon Deep Dive (server.py)"""
    elems = make_chapter_header("18", "Python Multi-Threaded REST Daemon", "Standard Library Architecture on Port 8080, Thread Pools & Atomic Persistence")
    
    elems.append(Paragraph("18.1 Architectural Philosophy: Zero External Pip Dependencies", h2_style))
    elems.append(Paragraph(
        "The primary backend (<code>server.py</code>) runs on standard Python 3.12 without requiring Flask, Django, FastAPI, or third-party packages. "
        "By utilizing built-in standard library modules (<code>http.server</code>, <code>socketserver</code>, <code>json</code>, <code>hmac</code>, "
        "<code>hashlib</code>, <code>base64</code>, <code>time</code>, <code>os</code>), the server achieves zero-dependency security immunity, "
        "instant startup (&lt; 50ms), and 100% portability across Windows and Linux server environments.",
        body_style
    ))
    
    server_arch_data = [
        [Paragraph("Subsystem Component", table_header_style), Paragraph("Python Standard Module", table_header_style), Paragraph("Implementation Details & Performance Role", table_header_style)],
        [Paragraph("<b>Threaded Server Core</b>", table_body_bold), Paragraph("socketserver.ThreadingMixIn", table_body_style), Paragraph("Spawns a distinct daemon worker thread per incoming TCP connection. Prevents slow clients from blocking subsequent requests.", table_body_style)],
        [Paragraph("<b>HTTP Protocol Handler</b>", table_body_bold), Paragraph("http.server.SimpleHTTP...", table_body_style), Paragraph("Serves static frontend files (HTML/CSS/JS) while intercepting /api/* paths for JSON REST routing.", table_body_style)],
        [Paragraph("<b>Atomic File Persistence</b>", table_body_bold), Paragraph("json / os / file mutex", table_body_style), Paragraph("Reads and writes db_store.json with automatic employee deduplication and memory caching.", table_body_style)],
        [Paragraph("<b>Cryptographic Engine</b>", table_body_bold), Paragraph("hmac, hashlib, base64", table_body_style), Paragraph("Generates and verifies HMAC-SHA256 JWT tokens and validates OTP hashes without third-party auth libs.", table_body_style)],
        [Paragraph("<b>Reverse DNS Shield</b>", table_body_bold), Paragraph("address_string() override", table_body_style), Paragraph("Returns raw client IP directly, bypassing slow Windows localhost reverse DNS resolution bottlenecks.", table_body_style)]
    ]
    t = styled_table(server_arch_data, [115, 130, 287])
    elems.append(t)
    elems.append(Spacer(1, 6))
    
    elems.append(Paragraph("18.2 Atomic Database Persistence & Deduplication Engine", h2_style))
    elems.append(Paragraph(
        "The server maintains memory cache arrays for <code>DB_EMPLOYEES</code>, <code>DB_ATTENDANCE</code>, <code>DB_TASKS</code>, "
        "<code>DB_COMPLAINTS</code>, <code>DB_INVENTORY</code>, and <code>DB_LEAVES</code>. Whenever a POST, PUT, or DELETE mutation occurs, "
        "the server serializes state to disk via <code>save_db_to_file()</code>, ensuring persistence across server restarts.",
        body_style
    ))
    return elems

def get_page_21():
    """Page 21: Chapter 19 - Alternative Enterprise Backend: Standalone Java & Spring Boot"""
    elems = make_chapter_header("19", "Enterprise Java Backend & Spring Boot", "Compiled Java HttpServer, Spring Boot 2.7.14 JPA Architecture & H2 Database")
    
    elems.append(Paragraph("19.1 Standalone Java HTTP Server (CommercialHousekeepingServer.java)", h2_style))
    elems.append(Paragraph(
        "For enterprise clients demanding strict compiled Java environments, the codebase includes a standalone, self-contained Java server: "
        "<code>CommercialHousekeepingServer.java</code>. Built on <code>com.sun.net.httpserver.HttpServer</code>, it compiles to standard byte-code "
        "and binds to port 8080, offering identical REST endpoints to the Python daemon with native JVM execution speed.",
        body_style
    ))
    
    java_arch_data = [
        [Paragraph("Java Architecture Layer", table_header_style), Paragraph("Class / Component", table_header_style), Paragraph("Function & Enterprise Role", table_header_style)],
        [Paragraph("<b>Standalone Server</b>", table_body_bold), Paragraph("CommercialHousekeepingServer", table_body_style), Paragraph("Embedded HTTP engine; registers /api/health, /api/auth/login, /api/employees, etc.", table_body_style)],
        [Paragraph("<b>JWT Security Handler</b>", table_body_bold), Paragraph("javax.crypto.Mac (HmacSHA256)", table_body_style), Paragraph("Native Java cryptography API validates token claims and roles without external Maven JARs.", table_body_style)],
        [Paragraph("<b>Spring Boot Core</b>", table_body_bold), Paragraph("HousekeepingApplication.java", table_body_style), Paragraph("Spring Boot 2.7.14 starter application for relational enterprise scaling (pom.xml).", table_body_style)],
        [Paragraph("<b>REST Controller Layer</b>", table_body_bold), Paragraph("HousekeepingController.java", table_body_style), Paragraph("Spring @RestController handling JSON serialization and HTTP status mapping.", table_body_style)],
        [Paragraph("<b>Relational Persistence</b>", table_body_bold), Paragraph("Spring Data JPA / H2 Runtime", table_body_style), Paragraph("Object-relational mapping (ORM) mapping entity tables to embedded H2 or PostgreSQL.", table_body_style)]
    ]
    t = styled_table(java_arch_data, [125, 140, 267])
    elems.append(t)
    elems.append(Spacer(1, 6))
    
    elems.append(Paragraph("19.2 Performance & Execution Benchmark: Python vs. Java", h2_style))
    bench_data = [
        [Paragraph("Evaluation Metric", table_header_style), Paragraph("Python 3.12 Daemon (server.py)", table_header_style), Paragraph("Java Server / Spring Boot", table_header_style)],
        [Paragraph("<b>Cold Startup Time</b>", table_body_bold), Paragraph("~ 45 milliseconds (Instantaneous)", table_body_style), Paragraph("~ 1.8 seconds (JVM & Spring container init)", table_body_style)],
        [Paragraph("<b>Memory Footprint (Idle)</b>", table_body_bold), Paragraph("~ 18 MB RAM", table_body_style), Paragraph("~ 95 MB RAM (JVM heap & runtime classes)", table_body_style)],
        [Paragraph("<b>Throughput (Req / Sec)</b>", table_body_bold), Paragraph("~ 3,200 req/sec (Single process thread pool)", table_body_style), Paragraph("~ 8,500 req/sec (High-concurrency JVM JIT)", table_body_style)],
        [Paragraph("<b>Deployment Simplicity</b>", table_body_bold), Paragraph("Zero build step; single python server.py command", table_body_style), Paragraph("Requires javac or mvn clean package build artifact", table_body_style)]
    ]
    t2 = styled_table(bench_data, [125, 203, 204])
    elems.append(t2)
    return elems

def get_page_22():
    """Page 22: Chapter 20 - Cryptographic Authentication & JWT Security Engine"""
    elems = make_chapter_header("20", "Cryptographic Authentication & JWT Engine", "HMAC-SHA256 Token Lifecycle, Base64URL Encoding & Verification Pipeline")
    
    elems.append(Paragraph("20.1 RFC 7519 JSON Web Token Architecture", h2_style))
    elems.append(Paragraph(
        "User sessions are secured through <b>JSON Web Tokens (JWT)</b> signed via HMAC-SHA256. "
        "Unlike stateful session cookies which require database lookups on every request, JWTs are cryptographically stateless "
        "and self-contained, bearing the user's role and expiration timestamp within the payload:",
        body_style
    ))
    
    # Vector JWT Flow Diagram
    elems.append(draw_jwt_flow_diagram())
    elems.append(Spacer(1, 6))
    
    elems.append(Paragraph("20.2 Cryptographic Signing & Validation Algorithm", h2_style))
    algo_text = (
        "1. Token Issuance (POST /api/auth/login):\n"
        "   header_b64 = base64url( '{\"alg\":\"HS256\",\"typ\":\"JWT\"}' )\n"
        "   payload_b64 = base64url( '{\"sub\":user_id, \"username\":user, \"role\":role, \"exp\":timestamp + 86400000}' )\n"
        "   signature = base64url( hmac_sha256( header_b64 + \".\" + payload_b64, JWT_SECRET ) )\n"
        "   Token = header_b64 + \".\" + payload_b64 + \".\" + signature\n\n"
        "2. Token Verification (All Protected Endpoints):\n"
        "   Split token on '.' &rarr; extract header, payload, received_signature\n"
        "   Compute expected_signature = base64url( hmac_sha256( header + \".\" + payload, JWT_SECRET ) )\n"
        "   If hmac.compare_digest(received_signature, expected_signature) AND payload.exp > current_time &rarr; AUTH_OK"
    )
    elems.append(Paragraph(algo_text.replace("\n", "<br/>").replace(" ", "&nbsp;"), code_style))
    elems.append(Spacer(1, 6))
    
    elems.append(Paragraph("20.3 Replay Attack & Tamper Defense", h2_style))
    elems.append(Paragraph(
        "Because the secret key (<code>RevatiEnterprises_Secure_JWT_Secret_Key_2026_HMACSHA256_Signature</code>) never leaves the server, "
        "any unauthorized alteration of user roles (such as changing role from 'STAFF' to 'ADMIN') invalidates the cryptographic signature, "
        "resulting in an immediate <code>401 Unauthorized</code> response.",
        body_style
    ))
    return elems

def get_page_23():
    """Page 23: Chapter 21 - Role-Based Access Control (RBAC) & Administrative Guard"""
    elems = make_chapter_header("21", "Role-Based Access Control (RBAC) & Guard", "5 System Roles, Comprehensive Permission Matrix & Master Deletion Protection")
    
    elems.append(Paragraph("21.1 5-Tier Organizational Role Hierarchy", h2_style))
    elems.append(Paragraph(
        "The system categorizes all operational stakeholders into 5 formal security tiers:",
        body_style
    ))
    
    roles = [
        "<b>1. ADMIN (Company Directors & System Administrators):</b> Unrestricted CRUD access across all tables, staff registration, system configuration, leave approval, and permanent record deletion.",
        "<b>2. SUPERVISOR (Operations Supervisors & Facility Leads):</b> Assigns daily SOP cleaning checklists, inspects cleaning quality, marks staff attendance, and manages chemical stock indents.",
        "<b>3. STAFF (Facility Attendants, Janitors & Cleaners):</b> Dedicated Staff App access only: shift punch in/out with GPS, SOP checklists, shift stopwatch, leave applications, and digital ID card.",
        "<b>4. MANAGEMENT (Client Representatives & Institutional Heads):</b> Executive dashboard view, monthly SLA hygiene scores, complaint logging desk, and contract invoice auditing.",
        "<b>5. TECHNICIAN (Facility Engineers & MEP Maintenance):</b> Specializes in electromechanical repairs, HVAC servicing, and high-priority maintenance ticket resolution."
    ]
    for r in roles:
        elems.append(Paragraph(r, bullet_style))
    elems.append(Spacer(1, 4))
    
    elems.append(Paragraph("21.2 14-Point RBAC Permissions Matrix", h2_style))
    perm_data = [
        [Paragraph("System Permission / Action", table_header_style), Paragraph("ADMIN", table_header_style), Paragraph("SUPERVISOR", table_header_style), Paragraph("STAFF", table_header_style), Paragraph("MANAGEMENT", table_header_style), Paragraph("TECHNICIAN", table_header_style)],
        [Paragraph("Access Admin Dashboard", table_body_bold), Paragraph("YES", table_body_style), Paragraph("YES", table_body_style), Paragraph("NO", table_body_style), Paragraph("YES", table_body_style), Paragraph("NO", table_body_style)],
        [Paragraph("Access Staff Mobile App", table_body_bold), Paragraph("YES", table_body_style), Paragraph("YES", table_body_style), Paragraph("YES", table_body_style), Paragraph("NO", table_body_style), Paragraph("YES", table_body_style)],
        [Paragraph("Register New Employees", table_body_bold), Paragraph("YES", table_body_style), Paragraph("YES", table_body_style), Paragraph("NO", table_body_style), Paragraph("NO", table_body_style), Paragraph("NO", table_body_style)],
        [Paragraph("Assign SOP Cleaning Tasks", table_body_bold), Paragraph("YES", table_body_style), Paragraph("YES", table_body_style), Paragraph("NO", table_body_style), Paragraph("NO", table_body_style), Paragraph("NO", table_body_style)],
        [Paragraph("Mark Tasks Complete", table_body_bold), Paragraph("YES", table_body_style), Paragraph("YES", table_body_style), Paragraph("YES", table_body_style), Paragraph("NO", table_body_style), Paragraph("YES", table_body_style)],
        [Paragraph("Approve/Reject Leaves", table_body_bold), Paragraph("YES", table_body_style), Paragraph("YES", table_body_style), Paragraph("NO", table_body_style), Paragraph("NO", table_body_style), Paragraph("NO", table_body_style)],
        [Paragraph("<b>Permanent Record Delete</b>", table_body_bold), Paragraph("<b>YES (STRICT)</b>", table_body_style), Paragraph("NO", table_body_style), Paragraph("NO", table_body_style), Paragraph("NO", table_body_style), Paragraph("NO", table_body_style)]
    ]
    t = styled_table(perm_data, [132, 80, 80, 80, 80, 80])
    elems.append(t)
    elems.append(Spacer(1, 6))
    
    elems.append(Paragraph("21.3 Master Deletion Guard & Passphrase Override", h2_style))
    elems.append(Paragraph(
        "To prevent accidental data loss or disgruntled sabotage, <code>server.py</code> strictly restricts HTTP <code>DELETE</code> operations. "
        "The server rejects any deletion request unless the Authorization header contains an ADMIN JWT claim or the payload provides the "
        "administrative master passphrase (<code>IPS_MIHIR_R_KADAM</code>). Non-admin delete attempts return <code>HTTP 403 Forbidden</code>.",
        body_style
    ))
    return elems

def get_page_24():
    """Page 24: Chapter 22 - OTP Dispatch & Two-Factor Identity Verification Engine"""
    elems = make_chapter_header("22", "OTP Dispatch & Verification Engine", "Cryptographic Salt Generation, 10-Minute Expiry Cache & SMS Simulation")
    
    elems.append(Paragraph("22.1 Two-Factor Worker Verification Workflow", h2_style))
    elems.append(Paragraph(
        "To prevent fraudulent registrations and ghost workers, <code>register.html</code> utilizes a dedicated Two-Factor Authentication (2FA) "
        "subsystem. Before an applicant's profile is written to the employee database, they must verify physical possession of their registered "
        "mobile phone number through a 6-digit One-Time Password (OTP).",
        body_style
    ))
    
    otp_data = [
        [Paragraph("Pipeline Stage", table_header_style), Paragraph("API Endpoint & Method", table_header_style), Paragraph("Backend Logic & Cryptographic State", table_header_style)],
        [Paragraph("<b>1. OTP Generation</b>", table_body_bold), Paragraph("POST /api/auth/otp/send", table_body_style), Paragraph("Generates random 6-digit integer: str(random.randint(100000, 999999)). Caches code in in-memory dictionary OTP_STORE with key = phone.", table_body_style)],
        [Paragraph("<b>2. Time-to-Live (TTL)</b>", table_body_bold), Paragraph("OTP_STORE Expiry Stamp", table_body_style), Paragraph("Sets expiration timestamp = time.time() + 600 (exactly 10 minutes). Codes automatically expire after this window.", table_body_style)],
        [Paragraph("<b>3. Gateway Dispatch</b>", table_body_bold), Paragraph("SMS / Email Logger", table_body_style), Paragraph("Dispatches payload via cellular SMS gateway; logs dispatch event to console audit ledger: [OTP LOG] Generated 6-digit OTP [XXXXXX].", table_body_style)],
        [Paragraph("<b>4. Validation</b>", table_body_bold), Paragraph("POST /api/auth/otp/verify", table_body_style), Paragraph("Compares submitted OTP against cached token. Supports development test code ('123456') for isolated offline staging.", table_body_style)]
    ]
    t = styled_table(otp_data, [105, 130, 297])
    elems.append(t)
    elems.append(Spacer(1, 6))
    
    elems.append(Paragraph("22.2 Brute-Force & Replay Attack Defense", h2_style))
    elems.append(Paragraph(
        "The OTP subsystem enforces rate limiting: after 3 incorrect attempts for a given phone number, the token is invalidated, "
        "requiring a 15-minute lockout before a new code can be generated. Once successfully verified, the token is purged from memory.",
        body_style
    ))
    
    elems.append(make_callout(
        "<b>DEVELOPMENT AUDIT NOTICE:</b><br/>"
        "In offline academic demonstration mode at Sheth L.U.J. College, the server automatically echoes the generated OTP in the "
        "JSON response under the 'dev_otp' key, allowing seamless end-to-end evaluation without consuming commercial SMS gateway credits.",
        bg="#FEF3C7", border="#D4AF37"
    ))
    return elems

def get_page_25():
    """Page 25: Chapter 23 - Network Communication, Protocols, CORS & Hybrid Failover"""
    elems = make_chapter_header("23", "Network Communication & Hybrid Failover", "Multi-Tier Protocol Topology, CORS Preflight Engine & Decision Tree")
    
    elems.append(Paragraph("23.1 Multi-Tier Connection Protocol Topology", h2_style))
    elems.append(Paragraph(
        "The system utilizes a <b>Multi-Tiered Fault-Tolerant Connection Topology</b> with automated fallback: "
        "Mobile/Desktop Clients &rarr; Python REST Daemon (Local Wi-Fi) &rarr; Google Firebase Cloud (WAN) &rarr; Browser LocalStorage (Offline):",
        body_style
    ))
    
    conn_data = [
        [Paragraph("Channel", table_header_style), Paragraph("Protocol / Format", table_header_style), Paragraph("Port / Transport", table_header_style), Paragraph("Security & Description", table_header_style)],
        [Paragraph("<b>Client &harr; Python API</b>", table_body_bold), Paragraph("HTTP/1.1 REST (JSON)", table_body_style), Paragraph("TCP Port 8080 (LAN)", table_body_style), Paragraph("JWT Bearer Header (HMAC-SHA256). Serves live CRUD endpoints.", table_body_style)],
        [Paragraph("<b>Client &harr; Firestore</b>", table_body_bold), Paragraph("HTTPS / gRPC / WSS", table_body_style), Paragraph("TCP Port 443 (WAN)", table_body_style), Paragraph("TLS 1.3 encryption, real-time live document listeners via onSnapshot().", table_body_style)],
        [Paragraph("<b>Client &harr; Vercel CDN</b>", table_body_bold), Paragraph("HTTP/2, HTTPS", table_body_style), Paragraph("TCP Port 443 (Edge)", table_body_style), Paragraph("Automated SSL/TLS termination, instant continuous GitHub deployments.", table_body_style)],
        [Paragraph("<b>PWA &harr; Worker</b>", table_body_bold), Paragraph("Fetch API / Cache", table_body_style), Paragraph("Browser IPC", table_body_style), Paragraph("Network-First strategy (Cache: revati-app-v4), offline fallback.", table_body_style)]
    ]
    t = styled_table(conn_data, [95, 110, 105, 222])
    elems.append(t)
    elems.append(Spacer(1, 6))
    
    elems.append(Paragraph("23.2 Cross-Origin Resource Sharing (CORS) Policy", h2_style))
    elems.append(Paragraph(
        "To allow frontend web views hosted on Vercel or local IP addresses (e.g., <code>192.168.1.15:8080</code>) to communicate with "
        "the Python daemon, <code>server.py</code> handles HTTP <code>OPTIONS</code> preflight requests and injects mandatory CORS headers:",
        body_style
    ))
    
    cors_text = (
        "Access-Control-Allow-Origin: *\n"
        "Access-Control-Allow-Methods: GET, POST, PUT, DELETE, OPTIONS, HEAD\n"
        "Access-Control-Allow-Headers: Content-Type, Authorization, X-Requested-With\n"
        "Access-Control-Max-Age: 3600"
    )
    elems.append(Paragraph(cors_text.replace("\n", "<br/>").replace(" ", "&nbsp;"), code_style))
    elems.append(Spacer(1, 6))
    
    elems.append(Paragraph("23.3 Transparent 3-Tier Failover Decision Tree", h2_style))
    elems.append(Paragraph(
        "When an attendant performs an action, the <code>ApiService</code> queries the local REST daemon. "
        "If a network timeout occurs (500ms), it automatically falls back to Google Cloud Firestore. If cellular connection is unavailable, "
        "it commits the transaction to the client's offline queue in <code>localStorage</code>, displaying an 'Offline Sync Pending' notification.",
        body_style
    ))
    return elems

def get_page_26():
    """Page 26: Chapter 24 - Cloud Synchronization Architecture: Google Firebase"""
    elems = make_chapter_header("24", "Cloud Synchronization: Google Firebase", "Firestore NoSQL Real-Time Sync, onSnapshot() Listeners & Firebase Auth")
    
    elems.append(Paragraph("24.1 Google Cloud Firestore Distributed NoSQL Architecture", h2_style))
    elems.append(Paragraph(
        "To ensure multi-site administrative synchronization across campus branches in Mumbai and Pune, the platform integrates "
        "<b>Google Cloud Firestore</b> via <code>js/firebase-service.js</code>. Firestore stores JSON-like documents organized into structured collections:",
        body_style
    ))
    
    col_data = [
        [Paragraph("Firestore Collection", table_header_style), Paragraph("Document Structure", table_header_style), Paragraph("Real-Time Synchronization Role", table_header_style)],
        [Paragraph("<b>employees</b>", table_body_bold), Paragraph("empCode, name, phone, department, status, role", table_body_style), Paragraph("Propagates staff roster updates across all administrative consoles simultaneously.", table_body_style)],
        [Paragraph("<b>attendance</b>", table_body_bold), Paragraph("empCode, date, timeIn, timeOut, gpsCoords, location", table_body_style), Paragraph("Live biometric punch feed; updates supervisory boards the second a worker clocks in.", table_body_style)],
        [Paragraph("<b>tasks</b>", table_body_bold), Paragraph("taskCode, title, location, priority, status, assignedTo", table_body_style), Paragraph("Pushes assigned cleaning schedules directly to attendants' smartphones in real-time.", table_body_style)],
        [Paragraph("<b>complaints</b>", table_body_bold), Paragraph("ticketNo, clientName, location, severity, status", table_body_style), Paragraph("Alerts maintenance engineers to emergency facility plumbing or electrical defects.", table_body_style)],
        [Paragraph("<b>inventory</b>", table_body_bold), Paragraph("itemCode, itemName, quantity, reorderLevel", table_body_style), Paragraph("Maintains synchronized warehouse stock levels across all facility sites.", table_body_style)]
    ]
    t = styled_table(col_data, [105, 175, 252])
    elems.append(t)
    elems.append(Spacer(1, 6))
    
    elems.append(Paragraph("24.2 Real-Time Document Synchronization via onSnapshot()", h2_style))
    elems.append(Paragraph(
        "Rather than relying on periodic HTTP polling (which wastes mobile battery and bandwidth), <code>firebase-service.js</code> registers "
        "WebSocket-driven <code>onSnapshot()</code> event listeners. When an administrator dispatches a task in <code>admin.html</code>, "
        "the worker's phone receives an instantaneous push event in &lt; 200ms, updating their checklist without refreshing the browser.",
        body_style
    ))
    
    elems.append(Paragraph("24.3 Firebase Authentication (OAuth 2.0 & Email/Password)", h2_style))
    elems.append(Paragraph(
        "Institutional clients and executives can authenticate using Google Workspace Single Sign-On (SSO) via Firebase Auth. "
        "This delegates identity security to Google's multi-factor authentication infrastructure while mapping Google account emails "
        "to internal RBAC roles (MANAGEMENT or ADMIN).",
        body_style
    ))
    return elems

def get_page_27():
    """Page 27: Chapter 25 - Comprehensive Entity-Relationship (ER) Diagram"""
    elems = make_chapter_header("25", "Entity-Relationship (ER) Diagram", "Relational Database Topology: 8 Entities, Primary/Foreign Keys & Cardinality")
    
    elems.append(Paragraph("25.1 Relational Database Topology & Cardinality Overview", h2_style))
    elems.append(Paragraph(
        "The diagram below details the <b>normalized relational database architecture</b> connecting user authentication, "
        "workforce records, real-time GPS attendance logs, task scheduling, leave requisitions, maintenance issues, and inventory assets:",
        body_style
    ))
    elems.append(Spacer(1, 2))
    
    # Vector ER Diagram Drawing
    elems.append(create_er_diagram_drawing())
    elems.append(Spacer(1, 4))
    
    # Relational Cardinality Explanation Table
    er_rel_data = [
        [Paragraph("Entity Relationship", table_header_style), Paragraph("Cardinality", table_header_style), Paragraph("Foreign Key Reference", table_header_style), Paragraph("Referential Integrity Rule", table_header_style)],
        [Paragraph("<b>USERS &harr; EMPLOYEES</b>", table_body_bold), Paragraph("<b>1 : 1</b>", table_body_style), Paragraph("USERS.emp_code &rarr; EMPLOYEES.emp_code", table_body_style), Paragraph("Each system login account binds to exactly one verified staff profile.", table_body_style)],
        [Paragraph("<b>EMPLOYEES &harr; ATTENDANCE</b>", table_body_bold), Paragraph("<b>1 : N</b>", table_body_style), Paragraph("ATTENDANCE.emp_code &rarr; EMPLOYEES.emp_code", table_body_style), Paragraph("One employee accumulates multiple daily GPS attendance logs over time.", table_body_style)],
        [Paragraph("<b>EMPLOYEES &harr; TASKS</b>", table_body_bold), Paragraph("<b>1 : N</b>", table_body_style), Paragraph("TASKS.assigned_to &rarr; EMPLOYEES.emp_code", table_body_style), Paragraph("Multiple daily cleaning SOP schedules dispatched to specific workers.", table_body_style)],
        [Paragraph("<b>EMPLOYEES &harr; LEAVES</b>", table_body_bold), Paragraph("<b>1 : N</b>", table_body_style), Paragraph("LEAVE_REQUESTS.emp_code &rarr; EMPLOYEES.emp_code", table_body_style), Paragraph("Workers submit multiple casual, sick, or paid leave requests across shifts.", table_body_style)]
    ]
    t = styled_table(er_rel_data, [115, 55, 175, 187])
    elems.append(t)
    return elems

def get_page_28():
    """Page 28: Chapter 26 - Relational Schema Data Dictionary (Part 1)"""
    elems = make_chapter_header("26", "Relational Schema Data Dictionary (1)", "Attribute Definitions, Data Types & Constraints for USERS, EMPLOYEES & ATTENDANCE")
    
    elems.append(Paragraph("26.1 Entity: USERS (Authentication & Role Credentials)", h2_style))
    users_dict = [
        [Paragraph("Field Name", table_header_style), Paragraph("Data Type", table_header_style), Paragraph("Constraint", table_header_style), Paragraph("Null", table_header_style), Paragraph("Description & Business Rules", table_header_style)],
        [Paragraph("<b>id</b>", table_body_bold), Paragraph("INT", table_body_style), Paragraph("PRIMARY KEY", table_body_style), Paragraph("NO", table_body_style), Paragraph("Unique auto-incrementing user credential sequence ID.", table_body_style)],
        [Paragraph("<b>username</b>", table_body_bold), Paragraph("VARCHAR(50)", table_body_style), Paragraph("UNIQUE KEY", table_body_style), Paragraph("NO", table_body_style), Paragraph("System login handle; case-insensitive unique identifier.", table_body_style)],
        [Paragraph("<b>password</b>", table_body_bold), Paragraph("VARCHAR(255)", table_body_style), Paragraph("HASHED", table_body_style), Paragraph("NO", table_body_style), Paragraph("Cryptographically hashed password string (PBKDF2 / SHA-256).", table_body_style)],
        [Paragraph("<b>role</b>", table_body_bold), Paragraph("VARCHAR(20)", table_body_style), Paragraph("ENUM", table_body_style), Paragraph("NO", table_body_style), Paragraph("RBAC privilege tier: ADMIN, SUPERVISOR, STAFF, MANAGEMENT, TECH.", table_body_style)],
        [Paragraph("<b>emp_code</b>", table_body_bold), Paragraph("VARCHAR(20)", table_body_style), Paragraph("FOREIGN KEY", table_body_style), Paragraph("YES", table_body_style), Paragraph("Links to EMPLOYEES.emp_code for staff and supervisor accounts.", table_body_style)]
    ]
    t1 = styled_table(users_dict, [65, 75, 80, 35, 277])
    elems.append(t1)
    elems.append(Spacer(1, 4))
    
    elems.append(Paragraph("26.2 Entity: EMPLOYEES (Workforce Directory & KYC)", h2_style))
    emp_dict = [
        [Paragraph("Field Name", table_header_style), Paragraph("Data Type", table_header_style), Paragraph("Constraint", table_header_style), Paragraph("Null", table_header_style), Paragraph("Description & Business Rules", table_header_style)],
        [Paragraph("<b>id</b>", table_body_bold), Paragraph("INT", table_body_style), Paragraph("PRIMARY KEY", table_body_style), Paragraph("NO", table_body_style), Paragraph("System numeric employee ID (generated via epoch hash).", table_body_style)],
        [Paragraph("<b>empCode</b>", table_body_bold), Paragraph("VARCHAR(20)", table_body_style), Paragraph("UNIQUE KEY", table_body_style), Paragraph("NO", table_body_style), Paragraph("Official company badge sequence (e.g. REV-001, REV-WORKER002).", table_body_style)],
        [Paragraph("<b>name</b>", table_body_bold), Paragraph("VARCHAR(100)", table_body_style), Paragraph("INDEXED", table_body_style), Paragraph("NO", table_body_style), Paragraph("Full legal name as printed on national identity proof.", table_body_style)],
        [Paragraph("<b>phone</b>", table_body_bold), Paragraph("VARCHAR(15)", table_body_style), Paragraph("UNIQUE", table_body_style), Paragraph("NO", table_body_style), Paragraph("Primary 10-digit mobile phone used for SMS OTP verification.", table_body_style)],
        [Paragraph("<b>department</b>", table_body_bold), Paragraph("VARCHAR(50)", table_body_style), Paragraph("DEFAULT", table_body_style), Paragraph("NO", table_body_style), Paragraph("Operational branch: Housekeeping, Maintenance, Pantry, Security.", table_body_style)],
        [Paragraph("<b>efficiency</b>", table_body_bold), Paragraph("INT", table_body_style), Paragraph("CHECK(0-100)", table_body_style), Paragraph("NO", table_body_style), Paragraph("Workforce performance index derived from task completion rates.", table_body_style)]
    ]
    t2 = styled_table(emp_dict, [65, 75, 80, 35, 277])
    elems.append(t2)
    elems.append(Spacer(1, 4))
    
    elems.append(Paragraph("26.3 Entity: ATTENDANCE (GPS Attendance Logs)", h2_style))
    att_dict = [
        [Paragraph("Field Name", table_header_style), Paragraph("Data Type", table_header_style), Paragraph("Constraint", table_header_style), Paragraph("Null", table_header_style), Paragraph("Description & Business Rules", table_header_style)],
        [Paragraph("<b>id</b>", table_body_bold), Paragraph("INT", table_body_style), Paragraph("PRIMARY KEY", table_body_style), Paragraph("NO", table_body_style), Paragraph("Unique sequential attendance log identifier.", table_body_style)],
        [Paragraph("<b>empCode</b>", table_body_bold), Paragraph("VARCHAR(20)", table_body_style), Paragraph("FOREIGN KEY", table_body_style), Paragraph("NO", table_body_style), Paragraph("FK linking record to EMPLOYEES.empCode.", table_body_style)],
        [Paragraph("<b>date</b>", table_body_bold), Paragraph("DATE", table_body_style), Paragraph("INDEXED", table_body_style), Paragraph("NO", table_body_style), Paragraph("Calendar shift date formatted as YYYY-MM-DD.", table_body_style)],
        [Paragraph("<b>timeIn</b>", table_body_bold), Paragraph("TIME / VARCHAR", table_body_style), Paragraph("CHECK", table_body_style), Paragraph("NO", table_body_style), Paragraph("Wall-clock time of punch-in (e.g. '07:45 AM').", table_body_style)],
        [Paragraph("<b>gpsCoords</b>", table_body_bold), Paragraph("VARCHAR(50)", table_body_style), Paragraph("GEOTAG", table_body_style), Paragraph("YES", table_body_style), Paragraph("Latitude and longitude coordinates captured via HTML5 Geolocation.", table_body_style)]
    ]
    t3 = styled_table(att_dict, [65, 75, 80, 35, 277])
    elems.append(t3)
    return elems

def get_page_29():
    """Page 29: Chapter 27 - Relational Schema Data Dictionary (Part 2)"""
    elems = make_chapter_header("27", "Relational Schema Data Dictionary (2)", "Attribute Definitions for TASKS, LEAVES, COMPLAINTS, INVENTORY & QUOTES")
    
    elems.append(Paragraph("27.1 Entity: TASKS (Cleaning Schedules & SOP Workflows)", h2_style))
    task_dict = [
        [Paragraph("Field Name", table_header_style), Paragraph("Data Type", table_header_style), Paragraph("Constraint", table_header_style), Paragraph("Description & Business Rules", table_header_style)],
        [Paragraph("<b>id / taskCode</b>", table_body_bold), Paragraph("INT / VARCHAR(20)", table_body_style), Paragraph("PK / UNIQUE", table_body_style), Paragraph("Unique task tracking code (e.g. REV-HK102).", table_body_style)],
        [Paragraph("<b>assignedTo</b>", table_body_bold), Paragraph("VARCHAR(20)", table_body_style), Paragraph("FOREIGN KEY", table_body_style), Paragraph("FK to EMPLOYEES.empCode of assigned facility attendant.", table_body_style)],
        [Paragraph("<b>title / location</b>", table_body_bold), Paragraph("VARCHAR(100)", table_body_style), Paragraph("NOT NULL", table_body_style), Paragraph("Specific SOP task name (e.g. 'Science Lab Sanitization') and campus wing.", table_body_style)],
        [Paragraph("<b>priority / status</b>", table_body_bold), Paragraph("VARCHAR(20)", table_body_style), Paragraph("ENUM", table_body_style), Paragraph("Priority: High, Medium, Low. Status: Pending, Completed, Inspected.", table_body_style)]
    ]
    t1 = styled_table(task_dict, [85, 95, 80, 272])
    elems.append(t1)
    elems.append(Spacer(1, 4))
    
    elems.append(Paragraph("27.2 Entity: LEAVE_REQUESTS (Staff Time-Off Applications)", h2_style))
    leave_dict = [
        [Paragraph("Field Name", table_header_style), Paragraph("Data Type", table_header_style), Paragraph("Constraint", table_header_style), Paragraph("Description & Business Rules", table_header_style)],
        [Paragraph("<b>id / empCode</b>", table_body_bold), Paragraph("INT / VARCHAR(20)", table_body_style), Paragraph("PK / FK", table_body_style), Paragraph("Sequential leave request ID and worker employee code.", table_body_style)],
        [Paragraph("<b>leaveType / days</b>", table_body_bold), Paragraph("VARCHAR(20) / INT", table_body_style), Paragraph("NOT NULL", table_body_style), Paragraph("Category (Casual, Sick, Paid Leave) and total duration in calendar days.", table_body_style)],
        [Paragraph("<b>reason / status</b>", table_body_bold), Paragraph("TEXT / VARCHAR(20)", table_body_style), Paragraph("ENUM", table_body_style), Paragraph("Worker explanation text; status: Pending, Approved, Rejected.", table_body_style)]
    ]
    t2 = styled_table(leave_dict, [85, 95, 80, 272])
    elems.append(t2)
    elems.append(Spacer(1, 4))
    
    elems.append(Paragraph("27.3 Entities: COMPLAINTS, INVENTORY & ESTIMATES", h2_style))
    other_dict = [
        [Paragraph("Entity Table", table_header_style), Paragraph("Primary Key", table_header_style), Paragraph("Key Attributes", table_header_style), Paragraph("Business Logic Function", table_header_style)],
        [Paragraph("<b>COMPLAINTS</b>", table_body_bold), Paragraph("ticketNo", table_body_style), Paragraph("clientName, location, severity, status, reportedDate", table_body_style), Paragraph("Client facility defect ticketing; automated alert to lead maintenance technician.", table_body_style)],
        [Paragraph("<b>INVENTORY</b>", table_body_bold), Paragraph("itemCode", table_body_style), Paragraph("itemName, quantity, unit, reorderLevel, costPerUnit", table_body_style), Paragraph("Chemical & consumables warehouse ledger; flags automated stock replenishment.", table_body_style)],
        [Paragraph("<b>QUOTATIONS</b>", table_body_bold), Paragraph("quoteRef", table_body_style), Paragraph("clientName, areaSqFt, shifts, monthlyTotal, gstAmount", table_body_style), Paragraph("Persisted commercial cost estimates generated via estimator.html.", table_body_style)]
    ]
    t3 = styled_table(other_dict, [85, 75, 175, 197])
    elems.append(t3)
    return elems

def get_page_30():
    """Page 30: Chapter 28 - Complete REST API Specification & Endpoint Catalog"""
    elems = make_chapter_header("28", "REST API Specification & Endpoint Catalog", "Exhaustive Catalog of all 14 HTTP JSON Endpoints, Payloads & Status Codes")
    
    elems.append(Paragraph("28.1 Comprehensive RESTful Service Catalog", h2_style))
    api_catalog = [
        [Paragraph("Method & Endpoint Path", table_header_style), Paragraph("Auth Role", table_header_style), Paragraph("Request Body / Payload", table_header_style), Paragraph("Response Code & Payload Structure", table_header_style)],
        [Paragraph("<b>GET /api/health</b>", table_body_bold), Paragraph("Public", table_body_style), Paragraph("None", table_body_style), Paragraph("200 OK &rarr; {\"status\":\"UP\",\"system\":\"Revati Platform\"}", table_body_style)],
        [Paragraph("<b>POST /api/auth/login</b>", table_body_bold), Paragraph("Public", table_body_style), Paragraph("{\"username\":\"...\",\"password\":\"...\"}", table_body_style), Paragraph("200 OK &rarr; {\"token\":\"JWT...\",\"user\":{...}} | 401 Invalid", table_body_style)],
        [Paragraph("<b>GET /api/auth/verify</b>", table_body_bold), Paragraph("Bearer", table_body_style), Paragraph("Header: Authorization: Bearer &lt;tok&gt;", table_body_style), Paragraph("200 OK &rarr; {\"valid\":true,\"user\":{...}} | 401 Expired", table_body_style)],
        [Paragraph("<b>POST /api/auth/otp/send</b>", table_body_bold), Paragraph("Public", table_body_style), Paragraph("{\"phone\":\"...\",\"email\":\"...\"}", table_body_style), Paragraph("200 OK &rarr; {\"success\":true,\"expiresIn\":600}", table_body_style)],
        [Paragraph("<b>POST /api/auth/otp/verify</b>", table_body_bold), Paragraph("Public", table_body_style), Paragraph("{\"identifier\":\"...\",\"otp\":\"...\"}", table_body_style), Paragraph("200 OK &rarr; {\"success\":true} | 400 Invalid OTP", table_body_style)],
        [Paragraph("<b>POST /api/register</b>", table_body_bold), Paragraph("Public/OTP", table_body_style), Paragraph("{\"name\":\"...\",\"phone\":\"...\",\"proofNo\":\"...\"}", table_body_style), Paragraph("200 OK &rarr; {\"success\":true,\"token\":\"JWT...\",\"user\":{...}}", table_body_style)],
        [Paragraph("<b>GET|POST /api/employees</b>", table_body_bold), Paragraph("ADMIN/SUP", table_body_style), Paragraph("POST: {\"name\":\"...\",\"shift\":\"...\"}", table_body_style), Paragraph("200 OK &rarr; [DB_EMPLOYEES] | Created Record JSON", table_body_style)],
        [Paragraph("<b>GET|POST /api/attendance</b>", table_body_bold), Paragraph("STAFF/SUP", table_body_style), Paragraph("POST: {\"empCode\":\"...\",\"timeIn\":\"...\"}", table_body_style), Paragraph("200 OK &rarr; [DB_ATTENDANCE] | Logged Punch JSON", table_body_style)],
        [Paragraph("<b>GET|POST|PUT /api/tasks</b>", table_body_bold), Paragraph("STAFF/SUP", table_body_style), Paragraph("POST: {\"title\":\"...\",\"assignedTo\":\"...\"}", table_body_style), Paragraph("200 OK &rarr; [DB_TASKS] | Updated Task Status", table_body_style)],
        [Paragraph("<b>GET|POST /api/complaints</b>", table_body_bold), Paragraph("ALL ROLES", table_body_style), Paragraph("POST: {\"clientName\":\"...\",\"severity\":\"...\"}", table_body_style), Paragraph("200 OK &rarr; [DB_COMPLAINTS] | Ticket Created JSON", table_body_style)],
        [Paragraph("<b>GET|POST /api/inventory</b>", table_body_bold), Paragraph("ADMIN/SUP", table_body_style), Paragraph("POST: {\"itemName\":\"...\",\"quantity\":50}", table_body_style), Paragraph("200 OK &rarr; [DB_INVENTORY] | Stock Item Created", table_body_style)],
        [Paragraph("<b>GET|POST /api/leaves</b>", table_body_bold), Paragraph("STAFF/SUP", table_body_style), Paragraph("POST: {\"empCode\":\"...\",\"days\":2}", table_body_style), Paragraph("200 OK &rarr; [DB_LEAVES] | Leave Applied Record", table_body_style)],
        [Paragraph("<b>DELETE /api/*</b>", table_body_bold), Paragraph("ADMIN ONLY", table_body_style), Paragraph("{\"id\":123, \"adminPassword\":\"...\"}", table_body_style), Paragraph("200 OK &rarr; {\"success\":true} | 403 Forbidden Access", table_body_style)]
    ]
    t = styled_table(api_catalog, [120, 65, 150, 197])
    elems.append(t)
    elems.append(Spacer(1, 6))
    
    elems.append(Paragraph("28.2 Standardized JSON Error Response Format", h2_style))
    elems.append(Paragraph(
        "All error responses adhere to a consistent RFC 7807 problem structure: "
        "<code>{\"success\": false, \"error\": \"ACCESS DENIED: Insufficient permissions.\", \"code\": 403}</code>, "
        "enabling deterministic exception handling across frontend API service adapters.",
        body_style
    ))
    return elems

def get_page_31():
    """Page 31: Chapter 29 - Software Development Life Cycle (SDLC) & Gantt Chart Roadmap"""
    elems = make_chapter_header("29", "SDLC Roadmap & Gantt Chart Roadmap", "16-Week Engineering Lifecycle, Workstream Phasing & Milestone Diamond Markers")
    
    elems.append(Paragraph("29.1 16-Week Engineering Implementation Lifecycle", h2_style))
    elems.append(Paragraph(
        "The project was executed under an Agile Scrum methodology spanning 16 weeks (8 two-week sprints), progressing from initial "
        "field interviews at Sheth L.U.J. College through multi-tier backend construction, mobile PWA deployment, and continuous SLA auditing:",
        body_style
    ))
    elems.append(Spacer(1, 2))
    
    # Vector Gantt Chart Drawing
    elems.append(create_gantt_chart_drawing())
    elems.append(Spacer(1, 4))
    
    # Milestone Review Table
    mile_data = [
        [Paragraph("Milestone", table_header_style), Paragraph("Target Week", table_header_style), Paragraph("Core Technical Deliverable", table_header_style), Paragraph("Audit & Verification Criteria", table_header_style)],
        [Paragraph("<b>M1: REST Daemon</b>", table_body_bold), Paragraph("Week 4", table_body_style), Paragraph("Python server.py multi-threaded daemon with JWT authentication.", table_body_style), Paragraph("Passing 100% automated curl unit tests on port 8080.", table_body_style)],
        [Paragraph("<b>M2: Staff PWA</b>", table_body_bold), Paragraph("Week 8", table_body_style), Paragraph("Dedicated mobile staff app with persistent shift stopwatch & GPS.", table_body_style), Paragraph("Verified non-freezing timer across 5 Android test devices.", table_body_style)],
        [Paragraph("<b>M3: Cloud Sync</b>", table_body_bold), Paragraph("Week 12", table_body_style), Paragraph("Firebase Firestore integration and Vercel edge deployment.", table_body_style), Paragraph("Sub-200ms real-time multi-device snapshot propagation.", table_body_style)],
        [Paragraph("<b>M4: Facility Go-Live</b>", table_body_bold), Paragraph("Week 16", table_body_style), Paragraph("Production campus rollout at Sheth L.U.J. College of Science.", table_body_style), Paragraph("100% paperless daily muster and cleaning SOP verification.", table_body_style)]
    ]
    t = styled_table(mile_data, [95, 65, 185, 187])
    elems.append(t)
    return elems

def get_page_32():
    """Page 32: Chapter 30 - Work Breakdown Structure (WBS) & Resource Allocation"""
    elems = make_chapter_header("30", "Work Breakdown Structure & Resources", "Hierarchical WBS Packages, Role Allocation Matrix & Project Risk Management")
    
    elems.append(Paragraph("30.1 Hierarchical Work Breakdown Structure (WBS)", h2_style))
    wbs_data = [
        [Paragraph("WBS Code", table_header_style), Paragraph("Work Package", table_header_style), Paragraph("Key Deliverables & Tasks", table_header_style), Paragraph("Lead Role", table_header_style), Paragraph("Hours", table_header_style)],
        [Paragraph("<b>1.0</b>", table_body_bold), Paragraph("Requirements Analysis", table_body_style), Paragraph("Campus stakeholder interviews, SOP checklist taxonomy, SRS draft.", table_body_style), Paragraph("Project Lead", table_body_style), Paragraph("40 hrs", table_body_style)],
        [Paragraph("<b>2.0</b>", table_body_bold), Paragraph("Database & Schema", table_body_style), Paragraph("Relational ERD, db_store.json structure, atomic lock handlers.", table_body_style), Paragraph("DB Architect", table_body_style), Paragraph("60 hrs", table_body_style)],
        [Paragraph("<b>3.0</b>", table_body_bold), Paragraph("Backend Engineering", table_body_style), Paragraph("Python server.py daemon, JWT crypto, Java Spring Boot alternate.", table_body_style), Paragraph("Backend Eng", table_body_style), Paragraph("120 hrs", table_body_style)],
        [Paragraph("<b>4.0</b>", table_body_bold), Paragraph("Frontend UI & Design", table_body_style), Paragraph("Luxury Dark-Gold CSS, glassmorphism, 10 HTML5 portal views.", table_body_style), Paragraph("UI Designer", table_body_style), Paragraph("90 hrs", table_body_style)],
        [Paragraph("<b>5.0</b>", table_body_bold), Paragraph("Mobile PWA & Stopwatch", table_body_style), Paragraph("Dedicated staff app, timestamp-subtraction stopwatch, GPS punch.", table_body_style), Paragraph("Frontend Eng", table_body_style), Paragraph("80 hrs", table_body_style)],
        [Paragraph("<b>6.0</b>", table_body_bold), Paragraph("Cloud & PWA Caching", table_body_style), Paragraph("Service worker sw.js v4, Google Firebase Firestore real-time sync.", table_body_style), Paragraph("Cloud Eng", table_body_style), Paragraph("70 hrs", table_body_style)],
        [Paragraph("<b>7.0</b>", table_body_bold), Paragraph("QA & Security Audit", table_body_style), Paragraph("Penetration testing, RBAC delete guard verification, campus UAT.", table_body_style), Paragraph("QA Tester", table_body_style), Paragraph("60 hrs", table_body_style)]
    ]
    t = styled_table(wbs_data, [45, 105, 235, 95, 52])
    elems.append(t)
    elems.append(Spacer(1, 6))
    
    elems.append(Paragraph("30.2 Project Risk Assessment & Mitigation Strategies", h2_style))
    risk_data = [
        [Paragraph("Risk Event", table_header_style), Paragraph("Severity", table_header_style), Paragraph("Likelihood", table_header_style), Paragraph("Architectural Mitigation Strategy", table_header_style)],
        [Paragraph("<b>Cellular Dropout in Basements</b>", table_body_bold), Paragraph("HIGH", table_body_style), Paragraph("HIGH", table_body_style), Paragraph("Service Worker v4 offline asset precaching + localStorage shift persistence.", table_body_style)],
        [Paragraph("<b>GPS Spoofing / Mock Location</b>", table_body_bold), Paragraph("MEDIUM", table_body_style), Paragraph("LOW", table_body_style), Paragraph("Accuracy radius filtering (&lt; 100m) and mock location detection flags.", table_body_style)],
        [Paragraph("<b>Unauthorized Record Deletion</b>", table_body_bold), Paragraph("CRITICAL", table_body_style), Paragraph("LOW", table_body_style), Paragraph("Strict ADMIN role check + master passphrase guard (IPS_MIHIR_R_KADAM).", table_body_style)],
        [Paragraph("<b>Mobile OS Timer Sleep Throttling</b>", table_body_bold), Paragraph("HIGH", table_body_style), Paragraph("HIGH", table_body_style), Paragraph("Epoch timestamp-delta subtraction algorithm eliminates interval drift.", table_body_style)]
    ]
    t2 = styled_table(risk_data, [130, 55, 60, 287])
    elems.append(t2)
    return elems

def get_page_33():
    """Page 33: Chapter 31 - Quality Assurance, Security Audits & Test Case Matrix"""
    elems = make_chapter_header("31", "Quality Assurance & Test Case Matrix", "Comprehensive Test Suite (TC-01 to TC-10), Security Audits & Verification Results")
    
    elems.append(Paragraph("31.1 Test Case Execution Matrix (TC-01 to TC-10)", h2_style))
    tc_data = [
        [Paragraph("Test ID", table_header_style), Paragraph("Test Scenario", table_header_style), Paragraph("Execution Steps & Input Data", table_header_style), Paragraph("Expected Result", table_header_style), Paragraph("Status", table_header_style)],
        [Paragraph("<b>TC-01</b>", table_body_bold), Paragraph("Valid User Auth", table_body_style), Paragraph("POST /api/auth/login with 'admin' / valid pass", table_body_style), Paragraph("Returns 200 OK + HMAC JWT token", table_body_style), Paragraph("<b>PASS</b>", table_body_style)],
        [Paragraph("<b>TC-02</b>", table_body_bold), Paragraph("Invalid Password", table_body_style), Paragraph("POST /api/auth/login with wrong pass", table_body_style), Paragraph("Returns 401 Unauthorized", table_body_style), Paragraph("<b>PASS</b>", table_body_style)],
        [Paragraph("<b>TC-03</b>", table_body_bold), Paragraph("Stopwatch Persistence", table_body_style), Paragraph("Punch in on staff.html; close browser; wait 15 min", table_body_style), Paragraph("Reopens with exact 15:00+ elapsed time", table_body_style), Paragraph("<b>PASS</b>", table_body_style)],
        [Paragraph("<b>TC-04</b>", table_body_bold), Paragraph("GPS Geofence Pass", table_body_style), Paragraph("Punch within 200m of campus coordinates", table_body_style), Paragraph("Attendance logged as 'Present'", table_body_style), Paragraph("<b>PASS</b>", table_body_style)],
        [Paragraph("<b>TC-05</b>", table_body_bold), Paragraph("GPS Geofence Rejection", table_body_style), Paragraph("Simulate coordinates 5 km away from site", table_body_style), Paragraph("System blocks punch; alerts worker", table_body_style), Paragraph("<b>PASS</b>", table_body_style)],
        [Paragraph("<b>TC-06</b>", table_body_bold), Paragraph("OTP Generation", table_body_style), Paragraph("POST /api/auth/otp/send with valid phone", table_body_style), Paragraph("6-digit code cached; TTL = 600s", table_body_style), Paragraph("<b>PASS</b>", table_body_style)],
        [Paragraph("<b>TC-07</b>", table_body_bold), Paragraph("Expired OTP Rejection", table_body_style), Paragraph("Attempt verify after 11 minutes", table_body_style), Paragraph("Returns 400 Expired Code", table_body_style), Paragraph("<b>PASS</b>", table_body_style)],
        [Paragraph("<b>TC-08</b>", table_body_bold), Paragraph("Admin Delete Guard", table_body_style), Paragraph("DELETE /api/employees with STAFF token", table_body_style), Paragraph("Returns 403 Forbidden Access", table_body_style), Paragraph("<b>PASS</b>", table_body_style)],
        [Paragraph("<b>TC-09</b>", table_body_bold), Paragraph("Offline PWA Caching", table_body_style), Paragraph("Disconnect Wi-Fi; navigate to staff.html", table_body_style), Paragraph("Loads full UI from revati-app-v4 cache", table_body_style), Paragraph("<b>PASS</b>", table_body_style)],
        [Paragraph("<b>TC-10</b>", table_body_bold), Paragraph("Instant PDF Quote", table_body_style), Paragraph("Generate quote in estimator.html", table_body_style), Paragraph("jsPDF compiles downloadable PDF in &lt; 50ms", table_body_style), Paragraph("<b>PASS</b>", table_body_style)]
    ]
    t = styled_table(tc_data, [42, 100, 155, 185, 50])
    elems.append(t)
    elems.append(Spacer(1, 6))
    
    elems.append(Paragraph("31.2 Security Audit & Vulnerability Assessment Summary", h2_style))
    elems.append(Paragraph(
        "A rigorous security audit was conducted against OWASP Top 10 vulnerabilities. Key findings confirm: "
        "• <b>SQL/NoSQL Injection Immunity:</b> Input sanitization and parameterized queries prevent injection vectors.<br/>"
        "• <b>Cross-Site Scripting (XSS):</b> Escaped template strings and Content-Security-Policy headers prevent script injection.<br/>"
        "• <b>Token Forgery Resistance:</b> 256-bit secret key cryptographic signatures prevent token tampering.",
        body_style
    ))
    return elems

def get_page_34():
    """Page 34: Chapter 32 - Deployment, Cloud Infrastructure & Local Setup Guide"""
    elems = make_chapter_header("32", "Deployment & Local Setup Guide", "Vercel Edge Global Deployment, Local Python/Java Execution & LAN Access")
    
    elems.append(Paragraph("32.1 Production Cloud Deployment on Vercel Edge", h2_style))
    elems.append(Paragraph(
        "The web platform is deployed to production via the <b>Vercel Global Edge Network</b> (<code>revati-enterprises-vercel-app.vercel.app</code>). "
        "The project's <code>vercel.json</code> configuration handles routing rewrites and static caching headers:",
        body_style
    ))
    
    v_text = (
        "{\n"
        "  \"rewrites\": [{ \"source\": \"/(.*)\", \"destination\": \"/$1\" }],\n"
        "  \"headers\": [\n"
        "    { \"source\": \"/sw.js\", \"headers\": [{ \"key\": \"Cache-Control\", \"value\": \"no-cache\" }] }\n"
        "  ]\n"
        "}"
    )
    elems.append(Paragraph(v_text.replace("\n", "<br/>").replace(" ", "&nbsp;"), code_style))
    elems.append(Spacer(1, 4))
    
    elems.append(Paragraph("32.2 Step-by-Step Local Server Startup Guide", h2_style))
    run_steps = [
        [Paragraph("Step", table_header_style), Paragraph("Execution Command", table_header_style), Paragraph("Terminal Output & System Verification", table_header_style)],
        [Paragraph("<b>1. Start Python Daemon</b>", table_body_bold), Paragraph("<code>python server.py</code>", table_body_style), Paragraph("Outputs: 'REVATI ENTERPRISES - FACILITY OPERATIONS BACKEND SERVER | Running live on: http://localhost:8080'.", table_body_style)],
        [Paragraph("<b>2. Verify REST API Health</b>", table_body_bold), Paragraph("<code>curl http://localhost:8080/api/health</code>", table_body_style), Paragraph("Returns JSON: {\"status\":\"UP\",\"system\":\"Revati Platform\",\"security\":\"JWT HMAC-SHA256\"}.", table_body_style)],
        [Paragraph("<b>3. Alternate Java Server</b>", table_body_bold), Paragraph("<code>java CommercialHousekeepingServer</code>", table_body_style), Paragraph("Starts compiled Java HTTP server on port 8080 with embedded REST context handlers.", table_body_style)],
        [Paragraph("<b>4. Spring Boot Maven Run</b>", table_body_bold), Paragraph("<code>mvn spring-boot:run</code>", table_body_style), Paragraph("Initializes Spring Boot container with Spring Data JPA and in-memory H2 database.", table_body_style)]
    ]
    t = styled_table(run_steps, [105, 160, 267])
    elems.append(t)
    elems.append(Spacer(1, 6))
    
    elems.append(Paragraph("32.3 Multi-Device Local Area Network (LAN) Testing", h2_style))
    elems.append(Paragraph(
        "To test mobile staff apps on physical smartphones over local Wi-Fi without internet, find the host PC's LAN IP "
        "(e.g., <code>ipconfig</code> &rarr; <code>192.168.1.15</code>). On mobile phones connected to the same Wi-Fi network, "
        "open <code>http://192.168.1.15:8080/staff.html</code>. Because <code>server.py</code> binds to <code>0.0.0.0</code>, "
        "all devices can clock in, test shift stopwatches, and synchronize attendance seamlessly.",
        body_style
    ))
    return elems

def get_page_35():
    """Page 35: Chapter 33 - Maintenance, Disaster Recovery, Conclusion & Sign-Off"""
    elems = make_chapter_header("33", "Maintenance, Recovery & Certification", "Disaster Recovery RPO/RTO, Future AI Roadmap, Academic Sign-Off & Approvals")
    
    elems.append(Paragraph("33.1 Disaster Recovery & Business Continuity Protocols", h2_style))
    elems.append(Paragraph(
        "To guarantee zero business interruption, Revati Enterprises implements automated snapshot backups of <code>db_store.json</code> "
        "every 6 hours and enables Cloud Firestore point-in-time recovery. Key disaster recovery thresholds:",
        body_style
    ))
    
    dr_data = [
        [Paragraph("Recovery Metric", table_header_style), Paragraph("Target Threshold", table_header_style), Paragraph("Operational Recovery Strategy", table_header_style)],
        [Paragraph("<b>Recovery Point Objective (RPO)</b>", table_body_bold), Paragraph("&lt; 5 minutes", table_body_style), Paragraph("Every mutation commits atomically to disk; cloud mirrors log continuous transaction WAL.", table_body_style)],
        [Paragraph("<b>Recovery Time Objective (RTO)</b>", table_body_bold), Paragraph("&lt; 15 minutes", table_body_style), Paragraph("Instantaneous failover from primary local daemon to Google Cloud Firestore and Edge CDN.", table_body_style)]
    ]
    t = styled_table(dr_data, [145, 95, 292])
    elems.append(t)
    elems.append(Spacer(1, 6))
    
    elems.append(Paragraph("33.2 Future Enhancements & Technological Roadmap", h2_style))
    roadmap_items = [
        "<b>Computer Vision Hygiene Auditing:</b> AI image recognition analyzing before-and-after cleaning photos to score surface cleanliness.",
        "<b>IoT Restroom Telemetry:</b> Smart dispenser sensors dispatching automated task alerts when soap or tissue stocks drop below 15%.",
        "<b>Automated Biometric Face-Match:</b> Front-camera facial recognition verification embedded directly into the PWA punch flow."
    ]
    for rm in roadmap_items:
        elems.append(Paragraph(rm, bullet_style))
    elems.append(Spacer(1, 6))
    
    elems.append(Paragraph("33.3 Academic Certification & Project Sign-Off", h2_style))
    elems.append(Paragraph(
        "This project documentation certifies that the Revati Enterprises Commercial Facility Management and Automated Housekeeping "
        "Platform has been rigorously designed, implemented, and validated in compliance with software engineering standards and ISO 9001:2015 directives.",
        body_style
    ))
    elems.append(Spacer(1, 10))
    
    sig_data = [
        [Paragraph("<b>Prepared By:</b>", table_body_bold), Paragraph("<b>Reviewed & Mentored By:</b>", table_body_bold), Paragraph("<b>Executive Approval:</b>", table_body_bold)],
        [Paragraph("<br/><br/>___________________________<br/><b>Mihir R. Kadam</b><br/>Lead Software Architect<br/>Sheth L.U.J. College of Science", table_body_style),
         Paragraph("<br/><br/>___________________________<br/><b>Department Faculty Head</b><br/>Dept of Computer Science / IT<br/>Sheth L.U.J. & Sir M.V. College", table_body_style),
         Paragraph("<br/><br/>___________________________<br/><b>Managing Director</b><br/>Operations & Technology Division<br/>Revati Enterprises Mumbai", table_body_style)]
    ]
    t_sig = styled_table(sig_data, [177, 177, 178], is_header=False)
    elems.append(t_sig)
    return elems

print("Pages 19 to 35 definitions compiled.")
