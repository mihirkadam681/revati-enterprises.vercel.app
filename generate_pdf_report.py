import os
import sys
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.pdfgen import canvas

PDF_FILENAME = "Revati_Enterprises_Technical_Architecture.pdf"
PDF_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), PDF_FILENAME)

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_header_footer(num_pages)
            super().showPage()
        super().save()

    def draw_header_footer(self, page_count):
        self.saveState()
        self.setFont("Helvetica-Bold", 8)
        self.setFillColor(colors.HexColor("#D4AF37"))
        
        # Header (Top Line & Title)
        self.drawString(54, 755, "REVATI ENTERPRISES  |  TECHNICAL ARCHITECTURE & SPECIFICATION REPORT")
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#6B7280"))
        self.drawRightString(558, 755, "ISO 9001:2015 CERTIFIED")
        
        self.setStrokeColor(colors.HexColor("#D4AF37"))
        self.setLineWidth(0.75)
        self.line(54, 748, 558, 748)
        
        # Footer
        self.setStrokeColor(colors.HexColor("#E5E7EB"))
        self.setLineWidth(0.5)
        self.line(54, 45, 558, 45)
        
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#6B7280"))
        self.drawString(54, 32, "Confidential - For Internal Operations, Development & Audit Teams Only")
        page_text = f"Page {self._pageNumber} of {page_count}"
        self.drawRightString(558, 32, page_text)
        self.restoreState()

def build_pdf():
    doc = SimpleDocTemplate(
        PDF_PATH,
        pagesize=letter,
        leftMargin=54,
        rightMargin=54,
        topMargin=54,
        bottomMargin=54
    )

    styles = getSampleStyleSheet()

    # Custom Palette
    GOLD = colors.HexColor("#D4AF37")
    DARK_BG = colors.HexColor("#0B0E17")
    NAVY = colors.HexColor("#1E3A8A")
    TEXT_MAIN = colors.HexColor("#1F2937")
    TEXT_MUTED = colors.HexColor("#4B5563")
    ACCENT_GREEN = colors.HexColor("#059669")
    LIGHT_GRAY = colors.HexColor("#F9FAFB")
    BORDER_COLOR = colors.HexColor("#E5E7EB")

    # Typography Styles
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=22,
        leading=26,
        textColor=DARK_BG,
        spaceAfter=4
    )

    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=15,
        textColor=GOLD,
        spaceAfter=14
    )

    h1_style = ParagraphStyle(
        'Heading1_Custom',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=13,
        leading=17,
        textColor=DARK_BG,
        spaceBefore=12,
        spaceAfter=6
    )

    h2_style = ParagraphStyle(
        'Heading2_Custom',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10.5,
        leading=14,
        textColor=NAVY,
        spaceBefore=8,
        spaceAfter=4
    )

    body_style = ParagraphStyle(
        'Body_Custom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=12,
        textColor=TEXT_MAIN,
        spaceAfter=6
    )

    bullet_style = ParagraphStyle(
        'Bullet_Custom',
        parent=body_style,
        leftIndent=12,
        firstLineIndent=-8,
        spaceAfter=4
    )

    table_header_style = ParagraphStyle(
        'TableHeader',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=10,
        textColor=colors.white
    )

    table_body_style = ParagraphStyle(
        'TableBody',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7.8,
        leading=10.5,
        textColor=TEXT_MAIN
    )

    table_body_bold = ParagraphStyle(
        'TableBodyBold',
        parent=table_body_style,
        fontName='Helvetica-Bold'
    )

    callout_style = ParagraphStyle(
        'CalloutText',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=8.2,
        leading=11.5,
        textColor=DARK_BG
    )

    story = []

    # Title Banner Block
    story.append(Paragraph("REVATI ENTERPRISES", title_style))
    story.append(Paragraph("FULL-STACK ARCHITECTURE, LANGUAGES, CONNECTIONS & DATA MODELS", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=2, color=GOLD, spaceBefore=0, spaceAfter=10))

    # Executive Overview
    meta_data = [
        [Paragraph("<b>Document Version:</b> 2.4.0 (Enterprise Gold)", table_body_style), Paragraph("<b>Production URL:</b> revati-enterprises-vercel-app.vercel.app", table_body_style)],
        [Paragraph("<b>Generated:</b> October 2026", table_body_style), Paragraph("<b>Local Server:</b> http://localhost:8080 (REST + PWA)", table_body_style)],
        [Paragraph("<b>Target Domain:</b> Commercial Facility & Staff Operations", table_body_style), Paragraph("<b>Security Protocol:</b> JWT HMAC-SHA256 & Firebase Auth", table_body_style)]
    ]
    meta_table = Table(meta_data, colWidths=[240, 264])
    meta_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#F3F4F6")),
        ('PADDING', (0,0), (-1,-1), 5),
        ('BOX', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    story.append(meta_table)
    story.append(Spacer(1, 10))

    # SECTION 1: SYSTEM OVERVIEW
    story.append(Paragraph("1. Executive Summary & Core Tech Stack", h1_style))
    story.append(Paragraph(
        "The <b>REVATI ENTERPRISES</b> platform is a hybrid, high-resilience facility management and enterprise workforce system. "
        "It features a responsive luxury client presentation portal, an administrative governance center, and a dedicated <b>STAFF APP ONLY</b> "
        "mobile PWA with biometric attendance, active GPS verification, and persistent duty shift timers. The system operates on a dual-tier "
        "architecture providing full offline local capability as well as scalable cloud synchronization.",
        body_style
    ))

    overview_data = [
        [Paragraph("Layer", table_header_style), Paragraph("Primary Language / Technology", table_header_style), Paragraph("Core Responsibilities & Components", table_header_style)],
        [
            Paragraph("<b>Frontend UI</b>", table_body_bold),
            Paragraph("<b>HTML5, Vanilla CSS3, JavaScript (ES6+)</b>", table_body_style),
            Paragraph("Interactive client portal, Admin Dashboard, Staff Mobile App, Cost Estimator, Quotation Generator.", table_body_style)
        ],
        [
            Paragraph("<b>Backend (Local)</b>", table_body_bold),
            Paragraph("<b>Python 3.12 (Multi-Threaded HTTP/1.1)</b><br/><i>Alternative: Java 8+ / Spring Boot</i>", table_body_style),
            Paragraph("High-speed REST API server on port 8080, HMAC-SHA256 JWT auth, file & JSON document store persistence.", table_body_style)
        ],
        [
            Paragraph("<b>Cloud Backend</b>", table_body_bold),
            Paragraph("<b>Google Firebase (Firestore & Auth)</b><br/><b>Vercel Edge Network</b>", table_body_style),
            Paragraph("Serverless cloud document database, real-time sync listeners, Google & Email authentication, global CDN.", table_body_style)
        ],
        [
            Paragraph("<b>Networking</b>", table_body_bold),
            Paragraph("<b>RESTful JSON over HTTP, CORS, WebSockets/gRPC</b>", table_body_style),
            Paragraph("Cross-device communication between mobile clients, local servers, and Google Cloud endpoints.", table_body_style)
        ],
        [
            Paragraph("<b>Client Storage</b>", table_body_bold),
            Paragraph("<b>LocalStorage, Cache API, Service Worker</b>", table_body_style),
            Paragraph("Offline resilience, punch-state stopwatch persistence, PWA caching, zero-data-loss fallback.", table_body_style)
        ]
    ]
    overview_table = Table(overview_data, colWidths=[90, 160, 254])
    overview_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), DARK_BG),
        ('GRID', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('PADDING', (0,0), (-1,-1), 5),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, LIGHT_GRAY])
    ]))
    story.append(overview_table)
    story.append(Spacer(1, 12))

    # SECTION 2: FRONTEND SPECIFICATION
    story.append(Paragraph("2. Frontend Architecture & Languages", h1_style))
    story.append(Paragraph("<b>Languages & Standards:</b> HTML5, CSS3, JavaScript (ECMAScript 2022+)", h2_style))
    
    frontend_points = [
        "<b>HTML5 Architecture:</b> Fully semantic pages (<code>welcome.html</code>, <code>index.html</code>, <code>services.html</code>, <code>estimator.html</code>, <code>staff.html</code>, <code>admin.html</code>, <code>register.html</code>, <code>letterhead.html</code>) with complete OpenGraph metadata, PWA Manifest linking, and accessibility compliance.",
        "<b>Vanilla CSS3 Luxury Design System:</b> Tailored Dark-Gold palette (<code>--bg-main: #07090E</code>, <code>--gold-primary: #D4AF37</code>), glassmorphism (<code>backdrop-filter: blur(16px)</code>), CSS Grid / Flexbox layouts, hardware-accelerated 3D parallax transforms, and 5 responsive breakpoints (1200px, 1024px, 768px, 480px, 375px).",
        "<b>Client-Side Script Modules:</b>",
        "&nbsp;&nbsp;&bull; <code>js/app.js</code>: Main application router, modular dashboard tabs, reactive KPI counters, and data tables.",
        "&nbsp;&nbsp;&bull; <code>js/api.js</code>: JWT security client, automated multi-tier request routing (Firebase -> Java/Python API -> LocalStorage fallback).",
        "&nbsp;&nbsp;&bull; <code>js/firebase-service.js</code>: Cloud Firestore CRUD, Firebase Auth (Google OAuth & Email/Password), live snapshot subscriptions.",
        "&nbsp;&nbsp;&bull; <code>js/video-intro.js</code>: Canvas 2D cinematic particle generator, light dust rendering, and Web Audio API tone synthesis.",
        "&nbsp;&nbsp;&bull; <code>js/scroll3d.js</code>: Smooth scroll parallax effects, touch swipe gesture detection, and interactive slides.",
        "&nbsp;&nbsp;&bull; <code>js/jspdf.umd.min.js</code> & <code>js/excelExporter.js</code>: Client-side vector PDF generation and CSV/Excel data export engines.",
        "&nbsp;&nbsp;&bull; <code>sw.js</code>: Service Worker v4 with Network-First strategy and runtime asset caching for mobile offline access.",
        "<b>Icons & Visual Assets:</b> Hybrid vector system using Multi-CDN FontAwesome 6.5.1 + embedded inline SVG symbol sprites guaranteeing 100% offline rendering without broken glyph boxes."
    ]
    for pt in frontend_points:
        story.append(Paragraph(pt, bullet_style))

    story.append(Spacer(1, 10))

    # SECTION 3: BACKEND SPECIFICATION
    story.append(Paragraph("3. Backend Architecture & Languages", h1_style))
    story.append(Paragraph("<b>Primary Backend:</b> Python 3.12 Multi-Threaded Daemon (<code>server.py</code>)", h2_style))
    story.append(Paragraph(
        "The primary backend server is written in <b>Python 3.12</b> using standard libraries (<code>http.server</code>, <code>socketserver</code>, <code>hmac</code>, <code>hashlib</code>, <code>json</code>, <code>base64</code>) "
        "to ensure zero third-party dependency vulnerabilities. It implements a multi-threaded HTTP/1.1 daemon binding to <code>0.0.0.0:8080</code>.",
        body_style
    ))

    py_points = [
        "<b>Multi-Threading:</b> <code>socketserver.ThreadingMixIn</code> with daemonized worker threads for simultaneous mobile and desktop client connections.",
        "<b>HMAC-SHA256 JWT Authentication Engine:</b> Cryptographically signs and verifies JWT tokens with a 256-bit secret key, enforcing role permissions and token expiration.",
        "<b>Persistent Document Storage:</b> Backed by <code>db_store.json</code> with atomic write locks, automated schema initialization, and data deduplication.",
        "<b>Full RESTful Endpoint Matrix:</b> Provides <code>/api/health</code>, <code>/api/auth/login</code>, <code>/api/auth/verify</code>, <code>/api/auth/otp/send</code>, <code>/api/auth/otp/verify</code>, <code>/api/register</code>, <code>/api/employees</code>, <code>/api/tasks</code>, <code>/api/attendance</code>, <code>/api/leaves</code>, <code>/api/complaints</code>, <code>/api/inventory</code>, and <code>/api/reports</code>.",
        "<b>CORS & Connection Headers:</b> Emits <code>Access-Control-Allow-Origin: *</code>, allows mobile devices across the local Wi-Fi subnet (e.g. <code>192.168.0.105:8080</code>), and closes idle sockets cleanly with HTTP/1.1 standards."
    ]
    for pt in py_points:
        story.append(Paragraph(pt, bullet_style))

    story.append(Spacer(1, 6))
    story.append(Paragraph("<b>Secondary Alternative Backend:</b> Java 8+ / Spring Boot (<code>CommercialHousekeepingServer.java</code>)", h2_style))
    story.append(Paragraph(
        "A complete compiled Java backend is also provided in the repository, utilizing <code>com.sun.net.httpserver.HttpServer</code> with modular HTTP handlers and "
        "javax.crypto HMAC-SHA256 hashing. A Maven Spring Boot configuration (<code>pom.xml</code>, <code>HousekeepingApplication.java</code>) is structured with H2 in-memory SQL database and Hibernate JPA.",
        body_style
    ))

    story.append(PageBreak())

    # SECTION 4: CONNECTIONS & NETWORKING
    story.append(Paragraph("4. Connections, Protocols & Communication Channels", h1_style))
    story.append(Paragraph(
        "The system utilizes a <b>Multi-Tiered Fault-Tolerant Connection Topology</b>. Clients automatically probe cloud and local channels, falling back gracefully without crashing:",
        body_style
    ))

    conn_data = [
        [Paragraph("Connection Channel", table_header_style), Paragraph("Protocol / Format", table_header_style), Paragraph("Port / Transport", table_header_style), Paragraph("Security & Description", table_header_style)],
        [
            Paragraph("<b>Client <-> Python API</b>", table_body_bold),
            Paragraph("HTTP/1.1 REST (JSON)", table_body_style),
            Paragraph("TCP Port 8080<br/>(Localhost & Wi-Fi LAN)", table_body_style),
            Paragraph("JWT Bearer Header (HMAC-SHA256). Serves data and static HTML/CSS/JS.", table_body_style)
        ],
        [
            Paragraph("<b>Client <-> Firebase Firestore</b>", table_body_bold),
            Paragraph("HTTPS / gRPC / WebSockets", table_body_style),
            Paragraph("TCP Port 443<br/>(Google Cloud Edge)", table_body_style),
            Paragraph("TLS 1.3, Firebase Security Rules, live document synchronization via <code>onSnapshot</code>.", table_body_style)
        ],
        [
            Paragraph("<b>Client <-> Firebase Auth</b>", table_body_bold),
            Paragraph("OAuth 2.0 / HTTPS", table_body_style),
            Paragraph("TCP Port 443", table_body_style),
            Paragraph("Google Identity Services popup and secure password token exchange.", table_body_style)
        ],
        [
            Paragraph("<b>Client <-> Vercel Edge</b>", table_body_bold),
            Paragraph("HTTP/2, HTTPS", table_body_style),
            Paragraph("TCP Port 443<br/>(Global Anycast CDN)", table_body_style),
            Paragraph("Automated SSL/TLS, static asset delivery, and instant GitHub deployment triggers.", table_body_style)
        ],
        [
            Paragraph("<b>PWA <-> Service Worker</b>", table_body_bold),
            Paragraph("Service Worker Fetch API", table_body_style),
            Paragraph("Internal Browser IPC", table_body_style),
            Paragraph("Network-First caching strategy (Cache Name: <code>revati-app-v4</code>), offline fallback.", table_body_style)
        ]
    ]
    conn_table = Table(conn_data, colWidths=[100, 110, 110, 184])
    conn_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), DARK_BG),
        ('GRID', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('PADDING', (0,0), (-1,-1), 5),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, LIGHT_GRAY])
    ]))
    story.append(conn_table)
    story.append(Spacer(1, 14))

    # SECTION 5: DATA MODELS & ENTITY SCHEMAS
    story.append(Paragraph("5. Data Models, Entities & State Architecture", h1_style))
    story.append(Paragraph(
        "All data models are designed with schema consistency across Firebase Cloud Firestore, Python JSON store, and browser LocalStorage:",
        body_style
    ))

    models_data = [
        [Paragraph("Model Entity", table_header_style), Paragraph("Key Fields & Schema Attributes", table_header_style), Paragraph("Business Logic & Usage", table_header_style)],
        [
            Paragraph("<b>User Entity</b>", table_body_bold),
            Paragraph("<code>id, name, username, password, role, email, phone</code>", table_body_style),
            Paragraph("Authentication, session tokens, and Role-Based Access Control (ADMIN, SUPERVISOR, STAFF, MANAGEMENT).", table_body_style)
        ],
        [
            Paragraph("<b>Employee / Staff</b>", table_body_bold),
            Paragraph("<code>id, empCode, name, role, designation, department, status, efficiency, phone, email, proofType, proofNo, qualification, address</code>", table_body_style),
            Paragraph("Complete workforce directory, biometric registration records, statutory ID tracking (Aadhaar / Passport).", table_body_style)
        ],
        [
            Paragraph("<b>Attendance Entity</b>", table_body_bold),
            Paragraph("<code>id, employeeName, empCode, date, timeIn, timeOut, location, status</code>", table_body_style),
            Paragraph("Biometric punch-in and punch-out records with verified GPS coordinates and shift duration tracking.", table_body_style)
        ],
        [
            Paragraph("<b>Shift Stopwatch State</b>", table_body_bold),
            Paragraph("<code>isPunchedIn, inTime, startTimestamp, date</code>", table_body_style),
            Paragraph("Persistent active duty timer in <code>localStorage</code>; prevents timer reset on mobile refresh or browser sleep.", table_body_style)
        ],
        [
            Paragraph("<b>Task Assignment</b>", table_body_bold),
            Paragraph("<code>id, taskCode, title, description, location, priority, date, status ('Pending', 'Completed'), inspectedBy</code>", table_body_style),
            Paragraph("Commercial cleaning schedules, facility checklists, and mobile staff verification workflows.", table_body_style)
        ],
        [
            Paragraph("<b>Leave Requisition</b>", table_body_bold),
            Paragraph("<code>id, empName, empCode, leaveType, startDate, endDate, phoneOnLeave, reason, appliedDate, status, adminComment</code>", table_body_style),
            Paragraph("Casual (CL), Sick (SL), and Privilege (PL) leave workflows with admin approval and emergency contacts.", table_body_style)
        ],
        [
            Paragraph("<b>Maintenance Ticket</b>", table_body_bold),
            Paragraph("<code>id, ticketNo, clientName, location, priority, description, reportedDate, status, resolution</code>", table_body_style),
            Paragraph("Facility issue reporting, plumbing/electrical dispatch, and resolution tracking.", table_body_style)
        ],
        [
            Paragraph("<b>Inventory Item</b>", table_body_bold),
            Paragraph("<code>id, itemCode, itemName, category, quantity, reorderLevel, unit, status ('In Stock', 'Low Stock')</code>", table_body_style),
            Paragraph("Industrial chemicals (Taski, EcoLab), floor scrubbers, PPE gear, and automated reorder alerts.", table_body_style)
        ]
    ]
    models_table = Table(models_data, colWidths=[95, 205, 204])
    models_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), DARK_BG),
        ('GRID', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('PADDING', (0,0), (-1,-1), 4.5),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, LIGHT_GRAY])
    ]))
    story.append(models_table)
    story.append(Spacer(1, 14))

    # SECTION 6: RBAC SECURITY PERMISSIONS MATRIX
    story.append(Paragraph("6. Role-Based Access Control (RBAC) Matrix", h1_style))
    rbac_data = [
        [Paragraph("Role Name", table_header_style), Paragraph("Target User Group", table_header_style), Paragraph("Allowed Views", table_header_style), Paragraph("Key Authorizations", table_header_style)],
        [
            Paragraph("<b>ADMIN</b>", table_body_bold),
            Paragraph("Company Directors & Operations Heads", table_body_style),
            Paragraph("All Views: Dashboard, Staff Directory, Leaves, Housekeeping, Inventory, Reports, Users, Letterhead", table_body_style),
            Paragraph("Full CRUD, register staff, delete records, approve/reject leaves, configure system settings.", table_body_style)
        ],
        [
            Paragraph("<b>SUPERVISOR</b>", table_body_bold),
            Paragraph("Field Area Supervisors & Leads", table_body_style),
            Paragraph("Dashboard, Employees, Tasks, Inventory, Reports, Attendance", table_body_style),
            Paragraph("Assign tasks, verify completed jobs, mark staff attendance, manage inventory levels.", table_body_style)
        ],
        [
            Paragraph("<b>STAFF</b>", table_body_bold),
            Paragraph("Facility Attendants, Cleaners & Techs", table_body_style),
            Paragraph("<b>Dedicated Staff App Only:</b> My Tasks, Shift Punch Clock, Leave Portal, Staff ID", table_body_style),
            Paragraph("Punch in/out with GPS, mark assigned duties completed, apply for leaves, view profile.", table_body_style)
        ],
        [
            Paragraph("<b>MANAGEMENT</b>", table_body_bold),
            Paragraph("Client Facility Representatives", table_body_style),
            Paragraph("Dashboard, Service Scope, Facility Reports, Complaints Desk", table_body_style),
            Paragraph("Log maintenance tickets, inspect site service quality, view monthly compliance reports.", table_body_style)
        ]
    ]
    rbac_table = Table(rbac_data, colWidths=[75, 120, 160, 149])
    rbac_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), DARK_BG),
        ('GRID', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('PADDING', (0,0), (-1,-1), 4.5),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, LIGHT_GRAY])
    ]))
    story.append(rbac_table)
    story.append(Spacer(1, 14))

    # SECTION 7: SUMMARY CALLOUT BOX
    summary_box_data = [
        [Paragraph(
            "<b>TECHNICAL CERTIFICATION SUMMARY:</b><br/>"
            "This architecture report confirms that Revati Enterprises utilizes an enterprise-grade, high-availability architecture "
            "comprising standards-compliant HTML5/CSS3/JavaScript frontend clients, a Python 3.12 multi-threaded REST daemon on port 8080, "
            "Google Firebase Cloud Firestore/Auth synchronization, and robust PWA service worker caching. "
            "The mobile experience features non-freezing time engines, persistent shift stopwatches, and resilient offline vector SVG iconography.",
            callout_style
        )]
    ]
    summary_table = Table(summary_box_data, colWidths=[504])
    summary_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#FEF3C7")),
        ('BOX', (0,0), (-1,-1), 1, GOLD),
        ('PADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(summary_table)

    # Build the document with running header and footer numbers
    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"[SUCCESS] PDF generated successfully at: {PDF_PATH}")

if __name__ == '__main__':
    build_pdf()
