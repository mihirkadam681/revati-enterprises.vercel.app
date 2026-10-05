import os
import sys
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.graphics.shapes import (
    Drawing, Rect, String, Line, Group, Polygon
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

def create_er_diagram_drawing():
    """Generates a professional vector-based Entity-Relationship (ER) diagram."""
    w, h = 504, 325
    d = Drawing(w, h)
    
    # Outer diagram canvas border with subtle background
    d.add(Rect(0, 0, w, h, rx=6, ry=6, fillColor=colors.HexColor("#F8FAFC"), strokeColor=colors.HexColor("#CBD5E1"), strokeWidth=1))
    
    # Title & Legend Strip at Top
    d.add(Rect(0, h - 24, w, 24, rx=6, ry=6, fillColor=colors.HexColor("#0F172A"), strokeColor=colors.HexColor("#0F172A")))
    d.add(Rect(0, h - 24, w, 6, fillColor=colors.HexColor("#0F172A"), strokeColor=colors.HexColor("#0F172A"))) # Square bottom corners
    d.add(String(10, h - 16, "RELATIONAL DATA SCHEMA (ER DIAGRAM) - ENTITIES & CARDINALITY", fontName="Helvetica-Bold", fontSize=8, fillColor=colors.HexColor("#D4AF37")))
    
    # Legend items in header
    d.add(Rect(320, h - 18, 8, 8, fillColor=colors.HexColor("#DC2626"), strokeColor=colors.HexColor("#DC2626"), rx=1, ry=1))
    d.add(String(332, h - 15, "PK: Primary Key", fontName="Helvetica", fontSize=6.5, fillColor=colors.white))
    d.add(Rect(390, h - 18, 8, 8, fillColor=colors.HexColor("#2563EB"), strokeColor=colors.HexColor("#2563EB"), rx=1, ry=1))
    d.add(String(402, h - 15, "FK: Foreign Key", fontName="Helvetica", fontSize=6.5, fillColor=colors.white))
    d.add(String(455, h - 15, "1 : N  Cardinality", fontName="Helvetica-Bold", fontSize=6.5, fillColor=colors.HexColor("#38BDF8")))
    
    # Helper to render a stylized entity table
    def draw_entity(x, y, ew, eh, title, header_bg, fields):
        # Card container
        d.add(Rect(x, y, ew, eh, rx=4, ry=4, fillColor=colors.white, strokeColor=colors.HexColor("#94A3B8"), strokeWidth=0.8))
        # Header banner
        header_h = 16
        d.add(Rect(x, y + eh - header_h, ew, header_h, rx=4, ry=4, fillColor=header_bg, strokeColor=header_bg))
        d.add(Rect(x, y + eh - header_h, ew, 4, fillColor=header_bg, strokeColor=header_bg))
        d.add(String(x + 5, y + eh - 12, title, fontName="Helvetica-Bold", fontSize=7, fillColor=colors.white))
        # Attributes
        curr_y = y + eh - header_h - 10
        for fld in fields:
            is_pk = fld.startswith("[PK]")
            is_fk = fld.startswith("[FK]")
            is_uk = fld.startswith("[UK]")
            
            if is_pk:
                col = colors.HexColor("#DC2626")
                f_font = "Helvetica-Bold"
            elif is_fk:
                col = colors.HexColor("#2563EB")
                f_font = "Helvetica-Bold"
            elif is_uk:
                col = colors.HexColor("#D97706")
                f_font = "Helvetica-Bold"
            else:
                col = colors.HexColor("#334155")
                f_font = "Helvetica"
                
            d.add(String(x + 5, curr_y, fld, fontName=f_font, fontSize=6, fillColor=col))
            curr_y -= 10.5

    # 1. USERS Entity (Top Left)
    draw_entity(
        x=8, y=175, ew=120, eh=112,
        title="USERS (Auth & RBAC)",
        header_bg=colors.HexColor("#1E293B"),
        fields=[
            "[PK] id : INT (AUTO)",
            "[UK] username : VARCHAR",
            "password_hash : VARCHAR",
            "role : ENUM(ADMIN..)",
            "[FK] emp_code : VARCHAR",
            "is_active : BOOLEAN",
            "last_login : TIMESTAMP",
            "created_at : TIMESTAMP"
        ]
    )

    # 2. EMPLOYEES Entity (Top Center - Central Hub)
    draw_entity(
        x=175, y=155, ew=150, eh=132,
        title="EMPLOYEES (Workforce Core)",
        header_bg=colors.HexColor("#1E3A8A"),
        fields=[
            "[PK] id : INT (AUTO)",
            "[UK] emp_code : VARCHAR(20)",
            "name : VARCHAR(100)",
            "department : VARCHAR(50)",
            "designation : VARCHAR(50)",
            "phone : VARCHAR(15)",
            "email : VARCHAR(100)",
            "shift : VARCHAR(20)",
            "efficiency : INT",
            "status : VARCHAR(20)",
            "joining_date : DATE"
        ]
    )

    # 3. ATTENDANCE Entity (Top Right)
    draw_entity(
        x=368, y=175, ew=128, eh=112,
        title="ATTENDANCE (GPS/Shift)",
        header_bg=colors.HexColor("#047857"),
        fields=[
            "[PK] id : INT (AUTO)",
            "[FK] emp_code : VARCHAR(20)",
            "date : DATE",
            "time_in : TIME",
            "time_out : TIME",
            "duration_hrs : FLOAT",
            "gps_coords : VARCHAR(50)",
            "status : VARCHAR(20)"
        ]
    )

    # 4. LEAVE_REQUESTS Entity (Bottom Left)
    draw_entity(
        x=8, y=12, ew=120, eh=122,
        title="LEAVE_REQUESTS (Portal)",
        header_bg=colors.HexColor("#7C3AED"),
        fields=[
            "[PK] id : INT (AUTO)",
            "[FK] emp_code : VARCHAR(20)",
            "leave_type : ENUM(CL,SL,PL)",
            "start_date : DATE",
            "end_date : DATE",
            "days_count : INT",
            "reason : TEXT",
            "status : ENUM(Apprv..)",
            "[FK] approved_by : INT",
            "applied_at : TIMESTAMP"
        ]
    )

    # 5. TASKS Entity (Bottom Center)
    draw_entity(
        x=175, y=12, ew=150, eh=122,
        title="TASKS (Schedules & SOPs)",
        header_bg=colors.HexColor("#0284C7"),
        fields=[
            "[PK] id : INT (AUTO)",
            "[UK] task_code : VARCHAR(20)",
            "[FK] assigned_to : VARCHAR(20)",
            "title : VARCHAR(100)",
            "location : VARCHAR(100)",
            "priority : ENUM(Hi,Med,Lo)",
            "scheduled_date : DATE",
            "status : ENUM(Pending..)",
            "[FK] inspected_by : INT",
            "completed_at : TIMESTAMP"
        ]
    )

    # 6. MAINTENANCE_TICKETS Entity (Bottom Right Upper)
    draw_entity(
        x=368, y=78, ew=128, eh=76,
        title="MAINTENANCE_TICKETS",
        header_bg=colors.HexColor("#D97706"),
        fields=[
            "[PK] id : INT (AUTO)",
            "[UK] ticket_no : VARCHAR(20)",
            "client_name : VARCHAR(100)",
            "location : VARCHAR(100)",
            "severity : VARCHAR(20)",
            "status : VARCHAR(20)"
        ]
    )

    # 7. INVENTORY_ITEMS Entity (Bottom Right Lower)
    draw_entity(
        x=368, y=12, ew=128, eh=58,
        title="INVENTORY_ITEMS",
        header_bg=colors.HexColor("#475569"),
        fields=[
            "[PK] id : INT (AUTO)",
            "[UK] item_code : VARCHAR(20)",
            "item_name : VARCHAR(80)",
            "quantity : INT",
            "reorder_level : INT"
        ]
    )

    # Relationship Connectors & Cardinality Labels
    def draw_arrow_h(x1, y1, x2, y2, label_start, label_end, text_mid=None):
        d.add(Line(x1, y1, x2, y2, strokeColor=colors.HexColor("#2563EB"), strokeWidth=1.2))
        d.add(String(x1 + 3, y1 + 3, label_start, fontName="Helvetica-Bold", fontSize=7, fillColor=colors.HexColor("#DC2626")))
        d.add(String(x2 - 12, y2 + 3, label_end, fontName="Helvetica-Bold", fontSize=7, fillColor=colors.HexColor("#1D4ED8")))
        if text_mid:
            mid_x = (x1 + x2) / 2 - 18
            d.add(String(mid_x, y1 + 4, text_mid, fontName="Helvetica-Bold", fontSize=6, fillColor=colors.HexColor("#475569")))

    # Connector 1: USERS (1) <----> (1) EMPLOYEES
    draw_arrow_h(128, 230, 175, 230, "1", "1", "1 : 1 Auth")

    # Connector 2: EMPLOYEES (1) <----> (N) ATTENDANCE
    draw_arrow_h(325, 230, 368, 230, "1", "N", "1 : N Logs")

    # Connector 3: EMPLOYEES (1) <----> (N) TASKS (Vertical)
    d.add(Line(250, 155, 250, 134, strokeColor=colors.HexColor("#2563EB"), strokeWidth=1.2))
    d.add(String(253, 146, "1", fontName="Helvetica-Bold", fontSize=7, fillColor=colors.HexColor("#DC2626")))
    d.add(String(253, 135, "N", fontName="Helvetica-Bold", fontSize=7, fillColor=colors.HexColor("#1D4ED8")))
    d.add(String(215, 142, "1 : N Assigned", fontName="Helvetica-Bold", fontSize=6, fillColor=colors.HexColor("#475569")))

    # Connector 4: EMPLOYEES (1) <----> (N) LEAVE_REQUESTS (Stepped)
    d.add(Line(195, 155, 195, 143, strokeColor=colors.HexColor("#7C3AED"), strokeWidth=1))
    d.add(Line(195, 143, 68, 143, strokeColor=colors.HexColor("#7C3AED"), strokeWidth=1))
    d.add(Line(68, 143, 68, 134, strokeColor=colors.HexColor("#7C3AED"), strokeWidth=1))
    d.add(String(198, 148, "1", fontName="Helvetica-Bold", fontSize=7, fillColor=colors.HexColor("#DC2626")))
    d.add(String(72, 136, "N", fontName="Helvetica-Bold", fontSize=7, fillColor=colors.HexColor("#7C3AED")))
    d.add(String(110, 145, "1 : N Leave History", fontName="Helvetica-Bold", fontSize=6, fillColor=colors.HexColor("#7C3AED")))

    # Connector 5: TASKS (1) <----> (N) MAINTENANCE
    d.add(Line(325, 105, 368, 105, strokeColor=colors.HexColor("#D97706"), strokeWidth=1))
    d.add(String(330, 108, "1", fontName="Helvetica-Bold", fontSize=6.5, fillColor=colors.HexColor("#0284C7")))
    d.add(String(356, 108, "N", fontName="Helvetica-Bold", fontSize=6.5, fillColor=colors.HexColor("#D97706")))

    return d

def create_gantt_chart_drawing():
    """Generates an executive vector Gantt Chart showing project roadmap and milestones."""
    w, h = 504, 255
    d = Drawing(w, h)
    
    # Outer boundary
    d.add(Rect(0, 0, w, h, rx=6, ry=6, fillColor=colors.white, strokeColor=colors.HexColor("#CBD5E1"), strokeWidth=1))
    
    # Header Bar
    header_h = 26
    d.add(Rect(0, h - header_h, w, header_h, rx=6, ry=6, fillColor=colors.HexColor("#0F172A"), strokeColor=colors.HexColor("#0F172A")))
    d.add(Rect(0, h - header_h, w, 6, fillColor=colors.HexColor("#0F172A"), strokeColor=colors.HexColor("#0F172A")))
    
    d.add(String(10, h - 17, "WORKSTREAM / MILESTONE PHASE", fontName="Helvetica-Bold", fontSize=7.5, fillColor=colors.HexColor("#D4AF37")))
    
    col_w = 54
    start_x = 180
    weeks = ["W1 - W2", "W3 - W4", "W5 - W6", "W7 - W8", "W9 - W10", "W11 - W12"]
    for i, wk in enumerate(weeks):
        cx = start_x + i * col_w
        d.add(String(cx + 8, h - 17, wk, fontName="Helvetica-Bold", fontSize=7, fillColor=colors.white))
        
    # Vertical grid lines across all timeline columns
    for i in range(len(weeks) + 1):
        gx = start_x + i * col_w
        d.add(Line(gx, 25, gx, h - header_h, strokeColor=colors.HexColor("#F1F5F9"), strokeWidth=0.8))

    # Tasks / Workstreams list: (name, start_idx, span, pct, status_color, milestone_x)
    tasks = [
        ("1. Architecture & RBAC Security Model", 0.0, 1.0, "100%", colors.HexColor("#059669"), None),
        ("2. DB Schema & Python REST Daemon", 0.7, 1.3, "100%", colors.HexColor("#059669"), 2.0),
        ("3. Luxury UI System & Web Portals", 1.5, 1.3, "100%", colors.HexColor("#059669"), None),
        ("4. Dedicated Staff App PWA & Stopwatch", 2.2, 1.8, "100%", colors.HexColor("#059669"), 4.0),
        ("5. Biometric GPS Punch & Offline SW", 3.2, 1.4, "100%", colors.HexColor("#059669"), None),
        ("6. Firebase Real-Time Sync & Failover", 3.8, 1.2, "100%", colors.HexColor("#059669"), 5.0),
        ("7. Vercel Cloud Launch & QA Audit", 4.4, 1.0, "100%", colors.HexColor("#059669"), None),
        ("8. Post-Launch SLA & Continuous Ops", 4.9, 1.1, "92%", colors.HexColor("#D97706"), None)
    ]

    row_h = 22
    start_y = h - header_h - 20
    
    for idx, (tname, s_idx, span, pct_label, bar_color, milestone_idx) in enumerate(tasks):
        y = start_y - (idx * row_h)
        
        # Zebra striping background for row
        if idx % 2 == 0:
            d.add(Rect(0, y - 5, w, row_h, fillColor=colors.HexColor("#F8FAFC"), strokeColor=colors.transparent))
            
        # Task label
        d.add(String(10, y + 1, tname, fontName="Helvetica-Bold", fontSize=6.8, fillColor=colors.HexColor("#1E293B")))
        
        # Gantt Bar
        bx = start_x + (s_idx * col_w)
        bw = span * col_w
        d.add(Rect(bx, y - 2, bw, 13, rx=3, ry=3, fillColor=bar_color, strokeColor=bar_color))
        
        # Percentage indicator inside or next to bar
        d.add(String(bx + 4, y + 1.5, pct_label, fontName="Helvetica-Bold", fontSize=6, fillColor=colors.white))
        
        # Milestone Diamond Marker
        if milestone_idx is not None:
            mx = start_x + (milestone_idx * col_w)
            my = y + 4.5
            d.add(Polygon(
                [mx, my + 5, mx + 5, my, mx, my - 5, mx - 5, my],
                fillColor=colors.HexColor("#D4AF37"),
                strokeColor=colors.HexColor("#0F172A"),
                strokeWidth=0.8
            ))

    # Bottom Legend
    leg_y = 7
    d.add(Rect(0, 0, w, 24, rx=6, ry=6, fillColor=colors.HexColor("#0F172A"), strokeColor=colors.HexColor("#0F172A")))
    d.add(Rect(0, 18, w, 6, fillColor=colors.HexColor("#0F172A"), strokeColor=colors.HexColor("#0F172A"))) # Square top
    
    # Legend 1: Completed
    d.add(Rect(15, leg_y + 2, 12, 8, rx=2, ry=2, fillColor=colors.HexColor("#059669"), strokeColor=colors.HexColor("#059669")))
    d.add(String(32, leg_y + 3, "Completed Milestones (100%)", fontName="Helvetica", fontSize=6.5, fillColor=colors.white))
    
    # Legend 2: Active SLA
    d.add(Rect(185, leg_y + 2, 12, 8, rx=2, ry=2, fillColor=colors.HexColor("#D97706"), strokeColor=colors.HexColor("#D97706")))
    d.add(String(202, leg_y + 3, "Active SLA Tracking (92%)", fontName="Helvetica", fontSize=6.5, fillColor=colors.white))
    
    # Legend 3: Diamond Milestone
    d.add(Polygon([335, leg_y + 6, 339, leg_y + 2, 335, leg_y - 2, 331, leg_y + 2], fillColor=colors.HexColor("#D4AF37"), strokeColor=colors.white, strokeWidth=0.5))
    d.add(String(345, leg_y + 3, "Release Milestone (M1: REST, M2: Staff PWA, M3: Cloud Go-Live)", fontName="Helvetica", fontSize=6.5, fillColor=colors.white))

    return d

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
    LIGHT_GRAY = colors.HexColor("#F9FAFB")
    BORDER_COLOR = colors.HexColor("#E5E7EB")

    # Typography Styles
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=20,
        leading=24,
        textColor=DARK_BG,
        spaceAfter=3
    )

    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=14,
        textColor=GOLD,
        spaceAfter=10
    )

    h1_style = ParagraphStyle(
        'Heading1_Custom',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=15,
        textColor=DARK_BG,
        spaceBefore=10,
        spaceAfter=5
    )

    h2_style = ParagraphStyle(
        'Heading2_Custom',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9.5,
        leading=13,
        textColor=NAVY,
        spaceBefore=6,
        spaceAfter=3
    )

    body_style = ParagraphStyle(
        'Body_Custom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=11.5,
        textColor=TEXT_MAIN,
        spaceAfter=5
    )

    bullet_style = ParagraphStyle(
        'Bullet_Custom',
        parent=body_style,
        leftIndent=10,
        firstLineIndent=-6,
        spaceAfter=3
    )

    table_header_style = ParagraphStyle(
        'TableHeader',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=7.5,
        leading=9.5,
        textColor=colors.white
    )

    table_body_style = ParagraphStyle(
        'TableBody',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7.2,
        leading=9.5,
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
        fontSize=7.8,
        leading=11,
        textColor=DARK_BG
    )

    story = []

    # =========================================================================
    # PAGE 1: TITLE, EXECUTIVE OVERVIEW, FRONTEND & BACKEND ARCHITECTURE
    # =========================================================================
    story.append(Paragraph("REVATI ENTERPRISES", title_style))
    story.append(Paragraph("FULL-STACK ARCHITECTURE, LANGUAGES, CONNECTIONS, ER DIAGRAM & ROADMAP", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=GOLD, spaceBefore=0, spaceAfter=8))

    # Executive Overview Metadata
    meta_data = [
        [Paragraph("<b>Document Version:</b> 3.0.0 (Enterprise Architectural Edition)", table_body_style), Paragraph("<b>Production URL:</b> revati-enterprises-vercel-app.vercel.app", table_body_style)],
        [Paragraph("<b>Generated:</b> October 2026", table_body_style), Paragraph("<b>Local Server:</b> http://localhost:8080 (REST API Daemon)", table_body_style)],
        [Paragraph("<b>Target Domain:</b> Commercial Hospitality & Facility Operations", table_body_style), Paragraph("<b>Security Protocol:</b> HMAC-SHA256 JWT & Firebase Auth", table_body_style)]
    ]
    meta_table = Table(meta_data, colWidths=[244, 260])
    meta_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#F3F4F6")),
        ('PADDING', (0,0), (-1,-1), 4),
        ('BOX', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    story.append(meta_table)
    story.append(Spacer(1, 8))

    # SECTION 1: SYSTEM OVERVIEW
    story.append(Paragraph("1. Executive Summary & Core Tech Stack", h1_style))
    story.append(Paragraph(
        "<b>Revati Enterprises</b> provides commercial facility management and hospitality services. The technology infrastructure "
        "is built as a resilient, offline-capable hybrid system encompassing customer booking portals, administrative business intelligence, "
        "and a dedicated <b>STAFF APP ONLY</b> mobile PWA featuring non-freezing live clocks, shift stopwatch persistence, and offline vector SVG icons.",
        body_style
    ))

    overview_data = [
        [Paragraph("Layer", table_header_style), Paragraph("Languages & Technologies", table_header_style), Paragraph("Responsibilities & Architecture Role", table_header_style)],
        [
            Paragraph("<b>Frontend UI</b>", table_body_bold),
            Paragraph("<b>HTML5, Vanilla CSS3, JavaScript (ES6+)</b>", table_body_style),
            Paragraph("Client presentation portal, Admin Governance Center, Dedicated Staff PWA, Cost Estimator, Quotation Generator.", table_body_style)
        ],
        [
            Paragraph("<b>Backend (Local)</b>", table_body_bold),
            Paragraph("<b>Python 3.12 (Multi-Threaded HTTP/1.1)</b><br/><i>Alternate: Java 8+ / Spring Boot</i>", table_body_style),
            Paragraph("REST API on port 8080 (<code>server.py</code>), HMAC-SHA256 JWT auth, persistent JSON document store (<code>db_store.json</code>).", table_body_style)
        ],
        [
            Paragraph("<b>Cloud Backend</b>", table_body_bold),
            Paragraph("<b>Google Firebase (Firestore & Auth)</b><br/><b>Vercel Edge Network</b>", table_body_style),
            Paragraph("Serverless distributed NoSQL database, real-time snapshot listeners, Google & Email authentication, global CDN.", table_body_style)
        ],
        [
            Paragraph("<b>Networking</b>", table_body_bold),
            Paragraph("<b>RESTful JSON over HTTP, CORS, WebSockets/gRPC</b>", table_body_style),
            Paragraph("Bidirectional client-to-server synchronization, token bearer authentication, and real-time operational updates.", table_body_style)
        ]
    ]
    overview_table = Table(overview_data, colWidths=[85, 170, 249])
    overview_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), DARK_BG),
        ('GRID', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('PADDING', (0,0), (-1,-1), 4),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, LIGHT_GRAY])
    ]))
    story.append(overview_table)
    story.append(Spacer(1, 8))

    # SECTION 2: FRONTEND SPECIFICATION
    story.append(Paragraph("2. Frontend Architecture & Languages", h1_style))
    frontend_points = [
        "<b>HTML5 Semantic Architecture:</b> Responsive views (<code>staff.html</code>, <code>admin.html</code>, <code>welcome.html</code>, <code>index.html</code>, <code>services.html</code>, <code>estimator.html</code>) with embedded inline SVG symbol sprites guaranteeing zero broken icons even when offline.",
        "<b>Vanilla CSS3 Design System:</b> Luxury Dark-Gold theme (<code>#07090E</code>, <code>#D4AF37</code>), glassmorphism (<code>backdrop-filter: blur(16px)</code>), CSS Grid / Flexbox layouts, and 5 responsive breakpoints ensuring fluid rendering from mobile devices up to 4K displays.",
        "<b>JavaScript (ES6+) Engines:</b> Modular application router (<code>js/app.js</code>), multi-tier API abstraction (<code>js/api.js</code>), cloud sync (<code>js/firebase-service.js</code>), particle synthesis (<code>js/video-intro.js</code>), and Service Worker cache busting (<code>sw.js</code> v4).",
        "<b>Mobile Non-Freezing Shift Stopwatch:</b> High-precision ticker synchronizing with <code>localStorage</code> (<code>revati_staff_active_shift_v1</code>) so timers never reset or freeze on browser sleep or page refresh."
    ]
    for pt in frontend_points:
        story.append(Paragraph(pt, bullet_style))

    story.append(Spacer(1, 6))

    # SECTION 3: BACKEND SPECIFICATION
    story.append(Paragraph("3. Backend Architecture & Languages", h1_style))
    py_points = [
        "<b>Python 3.12 Multi-Threaded Daemon (<code>server.py</code>):</b> Standard library implementation (<code>http.server</code>, <code>socketserver.ThreadingMixIn</code>) binding to <code>0.0.0.0:8080</code> for zero-dependency vulnerability immunity.",
        "<b>HMAC-SHA256 JWT Engine:</b> Cryptographically verifies bearer tokens, role privileges, and expiration timestamps for all API endpoints (<code>/api/login</code>, <code>/api/verify</code>, <code>/api/attendance</code>, <code>/api/tasks</code>, <code>/api/complaints</code>).",
        "<b>Java 8+ / Spring Boot Enterprise Alternate:</b> Complete compiled alternate backend (<code>CommercialHousekeepingServer.java</code>) supporting relational SQL via Hibernate JPA and embedded H2 database engines."
    ]
    for pt in py_points:
        story.append(Paragraph(pt, bullet_style))

    story.append(PageBreak())

    # =========================================================================
    # PAGE 2: CONNECTIONS, NETWORKING & RBAC SECURITY MATRIX
    # =========================================================================
    story.append(Paragraph("4. Connections, Protocols & Network Communication", h1_style))
    story.append(Paragraph(
        "The system utilizes a <b>Multi-Tiered Fault-Tolerant Connection Topology</b> with automated fallback: "
        "Mobile/Desktop Clients &rarr; Python REST Daemon (Local Wi-Fi) &rarr; Google Firebase Cloud (WAN) &rarr; Browser LocalStorage (Offline).",
        body_style
    ))

    conn_data = [
        [Paragraph("Connection Channel", table_header_style), Paragraph("Protocol / Format", table_header_style), Paragraph("Port / Transport", table_header_style), Paragraph("Security & Description", table_header_style)],
        [
            Paragraph("<b>Client &harr; Python API</b>", table_body_bold),
            Paragraph("HTTP/1.1 REST (JSON)", table_body_style),
            Paragraph("TCP Port 8080<br/>(Localhost & Wi-Fi LAN)", table_body_style),
            Paragraph("JWT Bearer Header (HMAC-SHA256). Serves live CRUD endpoints and static web assets.", table_body_style)
        ],
        [
            Paragraph("<b>Client &harr; Cloud Firestore</b>", table_body_bold),
            Paragraph("HTTPS / gRPC / WebSockets", table_body_style),
            Paragraph("TCP Port 443<br/>(Google Cloud Edge)", table_body_style),
            Paragraph("TLS 1.3 encryption, real-time live document listeners via <code>onSnapshot()</code>.", table_body_style)
        ],
        [
            Paragraph("<b>Client &harr; Firebase Auth</b>", table_body_bold),
            Paragraph("OAuth 2.0 / HTTPS", table_body_style),
            Paragraph("TCP Port 443", table_body_style),
            Paragraph("Google Identity Services popup and cryptographic password exchange.", table_body_style)
        ],
        [
            Paragraph("<b>Client &harr; Vercel Edge</b>", table_body_bold),
            Paragraph("HTTP/2, HTTPS", table_body_style),
            Paragraph("TCP Port 443<br/>(Global Anycast CDN)", table_body_style),
            Paragraph("Automated SSL/TLS termination, instant continuous GitHub deployments.", table_body_style)
        ],
        [
            Paragraph("<b>PWA &harr; Service Worker</b>", table_body_bold),
            Paragraph("Service Worker Fetch API", table_body_style),
            Paragraph("Internal Browser IPC", table_body_style),
            Paragraph("Network-First strategy (Cache: <code>revati-app-v4</code>), offline asset fallback.", table_body_style)
        ]
    ]
    conn_table = Table(conn_data, colWidths=[95, 110, 110, 189])
    conn_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), DARK_BG),
        ('GRID', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('PADDING', (0,0), (-1,-1), 4.5),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, LIGHT_GRAY])
    ]))
    story.append(conn_table)
    story.append(Spacer(1, 12))

    # SECTION 5: RBAC SECURITY PERMISSIONS MATRIX
    story.append(Paragraph("5. Role-Based Access Control (RBAC) Security Matrix", h1_style))
    rbac_data = [
        [Paragraph("Role Name", table_header_style), Paragraph("Target User Group", table_header_style), Paragraph("Allowed Portals & Views", table_header_style), Paragraph("Key Authorizations & Constraints", table_header_style)],
        [
            Paragraph("<b>ADMIN</b>", table_body_bold),
            Paragraph("Company Directors & Operations Heads", table_body_style),
            Paragraph("All Portals: Dashboard, Staff Directory, Leaves, Housekeeping, Inventory, Reports, Users, Letterhead", table_body_style),
            Paragraph("Full system CRUD, register/terminate staff, delete records, approve/reject leaves, configure system parameters.", table_body_style)
        ],
        [
            Paragraph("<b>SUPERVISOR</b>", table_body_bold),
            Paragraph("Field Facility Leads & Floor Heads", table_body_style),
            Paragraph("Dashboard, Employees, Tasks, Inventory, Reports, Attendance Oversight", table_body_style),
            Paragraph("Delegate tasks, inspect and verify cleaning quality, punch attendance for team, log stock consumption.", table_body_style)
        ],
        [
            Paragraph("<b>STAFF</b>", table_body_bold),
            Paragraph("Facility Attendants, Cleaners & Techs", table_body_style),
            Paragraph("<b>Dedicated Staff App Only:</b> My Tasks, Shift Punch Clock, Leave Portal, Staff ID", table_body_style),
            Paragraph("Biometric GPS punch-in/out, active shift stopwatch, mark assigned SOP tasks completed, submit leave requests.", table_body_style)
        ],
        [
            Paragraph("<b>MANAGEMENT</b>", table_body_bold),
            Paragraph("Client Facility Representatives", table_body_style),
            Paragraph("Executive Dashboard, Service Scope, Facility Reports, Complaints Desk", table_body_style),
            Paragraph("Report maintenance tickets, audit site SLA compliance, view monthly facility quality ratings.", table_body_style)
        ]
    ]
    rbac_table = Table(rbac_data, colWidths=[70, 115, 165, 154])
    rbac_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), DARK_BG),
        ('GRID', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('PADDING', (0,0), (-1,-1), 4.5),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, LIGHT_GRAY])
    ]))
    story.append(rbac_table)

    story.append(PageBreak())

    # =========================================================================
    # PAGE 3: ENTITY-RELATIONSHIP (ER) DIAGRAM & ARCHITECTURAL SCHEMA
    # =========================================================================
    story.append(Paragraph("6. Relational Data Architecture (Entity-Relationship Diagram)", h1_style))
    story.append(Paragraph(
        "The diagram below details the <b>normalized relational database architecture</b> connecting user authentication, "
        "workforce records, real-time GPS attendance logs, task scheduling, leave requisitions, maintenance issues, and inventory assets:",
        body_style
    ))
    story.append(Spacer(1, 4))

    # Add Vector ER Diagram Drawing
    er_drawing = create_er_diagram_drawing()
    story.append(er_drawing)
    story.append(Spacer(1, 8))

    # ER Relationship Explanation Table
    er_summary_data = [
        [Paragraph("Relationship", table_header_style), Paragraph("Cardinality", table_header_style), Paragraph("Foreign Key Linkage", table_header_style), Paragraph("Business Integrity Rule", table_header_style)],
        [
            Paragraph("<b>User &harr; Employee</b>", table_body_bold),
            Paragraph("<b>1 : 1</b>", table_body_style),
            Paragraph("<code>USERS.emp_code &rarr; EMPLOYEES.emp_code</code>", table_body_style),
            Paragraph("Each login credential is bound to an active registered employee profile.", table_body_style)
        ],
        [
            Paragraph("<b>Employee &harr; Attendance</b>", table_body_bold),
            Paragraph("<b>1 : N</b>", table_body_style),
            Paragraph("<code>ATTENDANCE.emp_code &rarr; EMPLOYEES.emp_code</code>", table_body_style),
            Paragraph("One staff member creates multiple daily biometric punch-in and GPS geo-verified records.", table_body_style)
        ],
        [
            Paragraph("<b>Employee &harr; Tasks</b>", table_body_bold),
            Paragraph("<b>1 : N</b>", table_body_style),
            Paragraph("<code>TASKS.assigned_to &rarr; EMPLOYEES.emp_code</code>", table_body_style),
            Paragraph("Multiple daily commercial housekeeping schedules assigned to specific staff members.", table_body_style)
        ],
        [
            Paragraph("<b>Employee &harr; Leaves</b>", table_body_bold),
            Paragraph("<b>1 : N</b>", table_body_style),
            Paragraph("<code>LEAVE_REQUESTS.emp_code &rarr; EMPLOYEES.emp_code</code>", table_body_style),
            Paragraph("Staff submit multiple leave applications with emergency contacts and admin sign-off.", table_body_style)
        ]
    ]
    er_summary_table = Table(er_summary_data, colWidths=[105, 55, 170, 174])
    er_summary_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), DARK_BG),
        ('GRID', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('PADDING', (0,0), (-1,-1), 3.5),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, LIGHT_GRAY])
    ]))
    story.append(er_summary_table)

    story.append(PageBreak())

    # =========================================================================
    # PAGE 4: GANTT CHART ROADMAP, DATA MODELS & CERTIFICATION
    # =========================================================================
    story.append(Paragraph("7. Project Implementation & Roadmap (Gantt Chart)", h1_style))
    story.append(Paragraph(
        "The following vector <b>Gantt Chart</b> illustrates the engineering sprint timeline, key release milestones (M1: REST Daemon, "
        "M2: Dedicated Staff App PWA, M3: Cloud Go-Live), and continuous facility SLA operations:",
        body_style
    ))
    story.append(Spacer(1, 4))

    # Add Vector Gantt Chart Drawing
    gantt_drawing = create_gantt_chart_drawing()
    story.append(gantt_drawing)
    story.append(Spacer(1, 10))

    # SECTION 8: CORE DATA DOMAIN ENTITY SPECIFICATIONS
    story.append(Paragraph("8. Data Domain Models & Entity Schema Specifications", h1_style))
    models_data = [
        [Paragraph("Entity Model", table_header_style), Paragraph("Key Fields & Schema Attributes", table_header_style), Paragraph("Business Logic & Persistence Target", table_header_style)],
        [
            Paragraph("<b>User Entity</b>", table_body_bold),
            Paragraph("<code>id, name, username, password, role, email, phone</code>", table_body_style),
            Paragraph("JWT authentication, session security tokens, and RBAC authorization tiering.", table_body_style)
        ],
        [
            Paragraph("<b>Employee Record</b>", table_body_bold),
            Paragraph("<code>id, empCode, name, role, department, shift, phone, email, proofNo</code>", table_body_style),
            Paragraph("Workforce roster, KYC verification, shift assignment, and efficiency rating.", table_body_style)
        ],
        [
            Paragraph("<b>Attendance Log</b>", table_body_bold),
            Paragraph("<code>id, empCode, date, timeIn, timeOut, location, status, durationHrs</code>", table_body_style),
            Paragraph("Biometric punch-in/out, GPS coordinates, and payroll time calculation.", table_body_style)
        ],
        [
            Paragraph("<b>Shift Stopwatch</b>", table_body_bold),
            Paragraph("<code>isPunchedIn, inTime, startTimestamp, shiftDurationHours, date</code>", table_body_style),
            Paragraph("Persistent state in <code>localStorage</code>; survives browser sleep, reboots, and refreshes.", table_body_style)
        ],
        [
            Paragraph("<b>Task Assignment</b>", table_body_bold),
            Paragraph("<code>id, taskCode, title, location, priority, date, status, inspectedBy</code>", table_body_style),
            Paragraph("Facility checklist workflows, SOP compliance, and mobile staff verification.", table_body_style)
        ]
    ]
    models_table = Table(models_data, colWidths=[90, 205, 209])
    models_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), DARK_BG),
        ('GRID', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('PADDING', (0,0), (-1,-1), 3.5),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, LIGHT_GRAY])
    ]))
    story.append(models_table)
    story.append(Spacer(1, 10))

    # SECTION 9: SUMMARY CALLOUT BOX
    summary_box_data = [
        [Paragraph(
            "<b>ARCHITECTURAL AUDIT & CERTIFICATION:</b><br/>"
            "This report certifies that Revati Enterprises operates on an enterprise-grade, high-availability architecture "
            "comprising HTML5/CSS3/JavaScript frontend clients, a Python 3.12 multi-threaded REST daemon on port 8080, "
            "Google Firebase Cloud Firestore/Auth synchronization, and robust PWA service worker caching. "
            "The dedicated Staff App incorporates persistent shift timers, offline SVG iconography, and full relational integrity.",
            callout_style
        )]
    ]
    summary_table = Table(summary_box_data, colWidths=[504])
    summary_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#FEF3C7")),
        ('BOX', (0,0), (-1,-1), 1, GOLD),
        ('PADDING', (0,0), (-1,-1), 7),
    ]))
    story.append(summary_table)

    # Build the document with running header and footer numbers
    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"[SUCCESS] PDF generated successfully at: {PDF_PATH}")

if __name__ == '__main__':
    build_pdf()
