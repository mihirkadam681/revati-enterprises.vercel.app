"""
========================================================================================
REVATI ENTERPRISES - 35-PAGE COMPREHENSIVE TECHNICAL DOCUMENTATION & SYSTEM MANUAL
Author: Antigravity AI Engineering Suite & Revati Enterprises Systems Division
Date: October 2026
Standard: Academic Capstone & Enterprise Production Specification
Target: Exactly 35 High-Density, Professionally Formatted PDF Pages
========================================================================================
"""

import os
import sys
import time
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.graphics.shapes import (
    Drawing, Rect, String, Line, Group, Polygon, Circle
)
from reportlab.pdfgen import canvas

PDF_FILENAME = "Revati_Enterprises_Complete_35_Page_Documentation.pdf"
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
        if self._pageNumber > 1:
            # Running Header
            self.setFont("Helvetica-Bold", 8)
            self.setFillColor(colors.HexColor("#D4AF37"))
            self.drawString(40, 762, "REVATI ENTERPRISES")
            self.setFont("Helvetica", 7.5)
            self.setFillColor(colors.HexColor("#64748B"))
            self.drawString(135, 762, "|   FACILITY OPERATIONS & AUTOMATED HOUSEKEEPING PLATFORM")
            self.drawRightString(572, 762, "ISO 9001:2015 CERTIFIED")
            
            self.setStrokeColor(colors.HexColor("#D4AF37"))
            self.setLineWidth(0.75)
            self.line(40, 755, 572, 755)
            
            # Running Footer
            self.setStrokeColor(colors.HexColor("#E2E8F0"))
            self.setLineWidth(0.5)
            self.line(40, 36, 572, 36)
            
            self.setFont("Helvetica", 7.2)
            self.setFillColor(colors.HexColor("#64748B"))
            self.drawString(40, 24, "Academic & Enterprise Engineering Specification | Confidential & Proprietary")
            page_text = f"Page {self._pageNumber} of {page_count}"
            self.setFont("Helvetica-Bold", 7.2)
            self.setFillColor(colors.HexColor("#0F172A"))
            self.drawRightString(572, 24, page_text)
        self.restoreState()

# Palette Constants
GOLD = colors.HexColor("#D4AF37")
DARK_BG = colors.HexColor("#07090E")
NAVY = colors.HexColor("#1E3A8A")
TEXT_MAIN = colors.HexColor("#1F2937")
TEXT_MUTED = colors.HexColor("#4B5563")
LIGHT_BG = colors.HexColor("#F8FAFC")
BORDER_COLOR = colors.HexColor("#CBD5E1")
SUCCESS = colors.HexColor("#059669")
DANGER = colors.HexColor("#DC2626")
WARNING = colors.HexColor("#D97706")

styles = getSampleStyleSheet()

# Typography Styles
title_style = ParagraphStyle(
    'DocTitle', parent=styles['Normal'],
    fontName='Helvetica-Bold', fontSize=18, leading=22, textColor=DARK_BG, spaceAfter=2
)
subtitle_style = ParagraphStyle(
    'DocSubtitle', parent=styles['Normal'],
    fontName='Helvetica-Bold', fontSize=9, leading=12, textColor=GOLD, spaceAfter=4
)
h1_style = ParagraphStyle(
    'Heading1_Custom', parent=styles['Normal'],
    fontName='Helvetica-Bold', fontSize=10.5, leading=13, textColor=DARK_BG, spaceBefore=2, spaceAfter=2
)
h2_style = ParagraphStyle(
    'Heading2_Custom', parent=styles['Normal'],
    fontName='Helvetica-Bold', fontSize=8.5, leading=11, textColor=NAVY, spaceBefore=2, spaceAfter=1.5
)
body_style = ParagraphStyle(
    'Body_Custom', parent=styles['Normal'],
    fontName='Helvetica', fontSize=7.6, leading=10.2, textColor=TEXT_MAIN, spaceAfter=3
)
body_bold = ParagraphStyle(
    'Body_Bold_Custom', parent=body_style,
    fontName='Helvetica-Bold'
)
bullet_style = ParagraphStyle(
    'Bullet_Custom', parent=body_style,
    leftIndent=8, firstLineIndent=-5, spaceAfter=1.5
)
table_header_style = ParagraphStyle(
    'TableHeader', parent=styles['Normal'],
    fontName='Helvetica-Bold', fontSize=7, leading=8.8, textColor=colors.white
)
table_body_style = ParagraphStyle(
    'TableBody', parent=styles['Normal'],
    fontName='Helvetica', fontSize=6.7, leading=8.5, textColor=TEXT_MAIN
)
table_body_bold = ParagraphStyle(
    'TableBodyBold', parent=table_body_style,
    fontName='Helvetica-Bold'
)
callout_style = ParagraphStyle(
    'CalloutText', parent=styles['Normal'],
    fontName='Helvetica-Oblique', fontSize=7, leading=9.2, textColor=DARK_BG
)
code_style = ParagraphStyle(
    'CodeText', parent=styles['Normal'],
    fontName='Courier', fontSize=6.5, leading=8.2, textColor=colors.HexColor("#0F172A")
)

def make_callout(text, bg="#FEF3C7", border="#D4AF37", width=532):
    t = Table([[Paragraph(text, callout_style)]], colWidths=[width])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor(bg)),
        ('BOX', (0,0), (-1,-1), 0.75, colors.HexColor(border)),
        ('PADDING', (0,0), (-1,-1), 3.5),
    ]))
    return t

def make_chapter_header(chap_num, title, subtitle_text):
    elems = []
    t = f"CHAPTER {chap_num}: {title.upper()}"
    elems.append(Paragraph(t, h1_style))
    elems.append(Paragraph(subtitle_text, subtitle_style))
    elems.append(HRFlowable(width="100%", thickness=1, color=GOLD, spaceBefore=0, spaceAfter=4))
    return elems

def styled_table(data, col_widths, is_header=True):
    t = Table(data, colWidths=col_widths)
    t_style = [
        ('GRID', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('PADDING', (0,0), (-1,-1), 3),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ]
    if is_header:
        t_style.append(('BACKGROUND', (0,0), (-1,0), DARK_BG))
        t_style.append(('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, LIGHT_BG]))
    else:
        t_style.append(('ROWBACKGROUNDS', (0,0), (-1,-1), [colors.white, LIGHT_BG]))
    t.setStyle(TableStyle(t_style))
    return t

# =========================================================================
# DRAWING HELPERS
# =========================================================================

def draw_cover_banner():
    w, h = 532, 160
    d = Drawing(w, h)
    d.add(Rect(0, 0, w, h, rx=8, ry=8, fillColor=DARK_BG, strokeColor=GOLD, strokeWidth=1.5))
    d.add(Circle(w/2, h/2 + 10, 42, fillColor=colors.HexColor("#111827"), strokeColor=GOLD, strokeWidth=2))
    d.add(String(w/2, h/2 + 18, "REVATI", textAnchor="middle", fontName="Helvetica-Bold", fontSize=13, fillColor=GOLD))
    d.add(String(w/2, h/2 + 4, "ENTERPRISES", textAnchor="middle", fontName="Helvetica-Bold", fontSize=8, fillColor=colors.white))
    d.add(String(w/2, h/2 - 9, "EST. 2026", textAnchor="middle", fontName="Helvetica", fontSize=6, fillColor=colors.HexColor("#94A3B8")))
    d.add(Line(30, 28, w-30, 28, strokeColor=GOLD, strokeWidth=0.8))
    d.add(String(w/2, 14, "COMMERCIAL FACILITY MANAGEMENT & AUTOMATED HOUSEKEEPING PLATFORM", textAnchor="middle", fontName="Helvetica-Bold", fontSize=7.5, fillColor=colors.HexColor("#F3E5AB")))
    return d

def draw_architecture_diagram():
    w, h = 532, 180
    d = Drawing(w, h)
    d.add(Rect(0, 0, w, h, rx=6, ry=6, fillColor=LIGHT_BG, strokeColor=BORDER_COLOR, strokeWidth=1))
    d.add(Rect(0, h-20, w, 20, rx=6, ry=6, fillColor=DARK_BG, strokeColor=DARK_BG))
    d.add(Rect(0, h-20, w, 6, fillColor=DARK_BG, strokeColor=DARK_BG))
    d.add(String(12, h-14, "HYBRID MULTI-TIER SYSTEM ARCHITECTURE & FAILOVER TOPOLOGY", fontName="Helvetica-Bold", fontSize=8, fillColor=GOLD))
    
    # 4 Tier Boxes
    box_w, box_h = 115, 125
    tiers = [
        (12, 18, "1. CLIENT PWA LAYER", colors.HexColor("#1E293B"), [
            "Dedicated Staff App (staff.html)",
            "Admin Console (admin.html)",
            "Worker KYC Portal (register.html)",
            "Cost Estimator & Letterhead",
            "Service Worker v4 Caching"
        ]),
        (142, 18, "2. LOCAL REST DAEMON", colors.HexColor("#1E3A8A"), [
            "Python 3.12 (server.py:8080)",
            "Multi-Threaded HTTP/1.1",
            "HMAC-SHA256 JWT Security",
            "OTP Dispatch & Verification",
            "Strict Admin Delete Guard"
        ]),
        (272, 18, "3. CLOUD SERVERLESS", colors.HexColor("#065F46"), [
            "Google Cloud Firestore NoSQL",
            "Real-time onSnapshot() Sync",
            "Firebase Auth (OAuth & Pass)",
            "Vercel Edge Global Anycast",
            "Automated SSL/TLS (HTTPS)"
        ]),
        (402, 18, "4. PERSISTENCE TIER", colors.HexColor("#7C2D12"), [
            "Local db_store.json (Atomic)",
            "Browser localStorage Shift State",
            "IndexedDB Offline Store",
            "Spring Boot JPA / H2 SQL",
            "Audit Log Ledger"
        ])
    ]
    for bx, by, btitle, bgcol, lines in tiers:
        d.add(Rect(bx, by, box_w, box_h, rx=4, ry=4, fillColor=colors.white, strokeColor=BORDER_COLOR, strokeWidth=0.8))
        d.add(Rect(bx, by + box_h - 18, box_w, 18, rx=4, ry=4, fillColor=bgcol, strokeColor=bgcol))
        d.add(Rect(bx, by + box_h - 18, box_w, 4, fillColor=bgcol, strokeColor=bgcol))
        d.add(String(bx + 6, by + box_h - 12, btitle, fontName="Helvetica-Bold", fontSize=6.5, fillColor=colors.white))
        curr_y = by + box_h - 30
        for l in lines:
            d.add(String(bx + 5, curr_y, "- " + l, fontName="Helvetica", fontSize=5.8, fillColor=TEXT_MAIN))
            curr_y -= 18
            
    # Connector arrows
    d.add(Line(127, 85, 142, 85, strokeColor=GOLD, strokeWidth=1.5))
    d.add(Line(257, 85, 272, 85, strokeColor=GOLD, strokeWidth=1.5))
    d.add(Line(387, 85, 402, 85, strokeColor=GOLD, strokeWidth=1.5))
    return d

def draw_pwa_lifecycle_diagram():
    w, h = 532, 150
    d = Drawing(w, h)
    d.add(Rect(0, 0, w, h, rx=6, ry=6, fillColor=LIGHT_BG, strokeColor=BORDER_COLOR, strokeWidth=1))
    d.add(Rect(0, h-20, w, 20, rx=6, ry=6, fillColor=DARK_BG, strokeColor=DARK_BG))
    d.add(String(12, h-14, "PROGRESSIVE WEB APP (PWA) SERVICE WORKER LIFECYCLE & CACHING", fontName="Helvetica-Bold", fontSize=8, fillColor=GOLD))
    
    stages = [
        (15, 20, 105, 95, "Registration", "#1E293B", ["navigator.serviceWorker", "register('/sw.js')", "Scope: '/'"]),
        (145, 20, 105, 95, "Install Event", "#1E3A8A", ["Precache core shell", "Cache: revati-app-v4", "skipWaiting() active"]),
        (275, 20, 105, 95, "Activate Event", "#065F46", ["Purge stale caches", "clients.claim()", "Control active clients"]),
        (405, 20, 115, 95, "Fetch Intercept", "#831843", ["Network-First strategy", "Clone & store response", "Offline fallback cache"])
    ]
    for sx, sy, sw, sh, stitle, scol, slines in stages:
        d.add(Rect(sx, sy, sw, sh, rx=4, ry=4, fillColor=colors.white, strokeColor=BORDER_COLOR, strokeWidth=0.8))
        d.add(Rect(sx, sy+sh-16, sw, 16, rx=4, ry=4, fillColor=colors.HexColor(scol), strokeColor=colors.HexColor(scol)))
        d.add(String(sx+6, sy+sh-11, stitle, fontName="Helvetica-Bold", fontSize=6.8, fillColor=colors.white))
        cy = sy + sh - 28
        for line in slines:
            d.add(String(sx+5, cy, "• " + line, fontName="Helvetica", fontSize=6.2, fillColor=TEXT_MAIN))
            cy -= 18
    # Connecting Arrows
    d.add(Line(120, 68, 145, 68, strokeColor=GOLD, strokeWidth=1.5))
    d.add(Line(250, 68, 275, 68, strokeColor=GOLD, strokeWidth=1.5))
    d.add(Line(380, 68, 405, 68, strokeColor=GOLD, strokeWidth=1.5))
    return d

def draw_jwt_flow_diagram():
    w, h = 532, 140
    d = Drawing(w, h)
    d.add(Rect(0, 0, w, h, rx=6, ry=6, fillColor=LIGHT_BG, strokeColor=BORDER_COLOR, strokeWidth=1))
    d.add(Rect(0, h-20, w, 20, rx=6, ry=6, fillColor=DARK_BG, strokeColor=DARK_BG))
    d.add(String(12, h-14, "HMAC-SHA256 JSON WEB TOKEN (JWT) LIFECYCLE & SIGNATURE VERIFICATION", fontName="Helvetica-Bold", fontSize=8, fillColor=GOLD))
    
    parts = [
        (15, 25, 155, 85, "1. HEADER (Base64URL)", "#1E293B", ["{\n  \"alg\": \"HS256\",\n  \"typ\": \"JWT\"\n}"]),
        (185, 25, 155, 85, "2. PAYLOAD (Claims)", "#1E3A8A", ["{\n  \"sub\": 1,\n  \"username\": \"admin\",\n  \"role\": \"ADMIN\",\n  \"exp\": 1775892000\n}"]),
        (355, 25, 162, 85, "3. SIGNATURE (Cryptographic)", "#065F46", ["HMACSHA256(\n  base64Url(Header) + \".\" +\n  base64Url(Payload),\n  JWT_SECRET\n)"])
    ]
    for px, py, pw, ph, ptitle, pcol, plines in parts:
        d.add(Rect(px, py, pw, ph, rx=4, ry=4, fillColor=colors.white, strokeColor=BORDER_COLOR, strokeWidth=0.8))
        d.add(Rect(px, py+ph-16, pw, 16, rx=4, ry=4, fillColor=colors.HexColor(pcol), strokeColor=colors.HexColor(pcol)))
        d.add(String(px+6, py+ph-11, ptitle, fontName="Helvetica-Bold", fontSize=6.5, fillColor=colors.white))
        cy = py + ph - 28
        for block in plines:
            for line in block.split("\n"):
                d.add(String(px+6, cy, line, fontName="Courier", fontSize=5.8, fillColor=TEXT_MAIN))
                cy -= 10
    return d

def create_er_diagram_drawing():
    """Generates vector Entity-Relationship diagram for Chapter 25."""
    w, h = 532, 330
    d = Drawing(w, h)
    d.add(Rect(0, 0, w, h, rx=6, ry=6, fillColor=LIGHT_BG, strokeColor=BORDER_COLOR, strokeWidth=1))
    d.add(Rect(0, h-22, w, 22, rx=6, ry=6, fillColor=DARK_BG, strokeColor=DARK_BG))
    d.add(Rect(0, h-22, w, 6, fillColor=DARK_BG, strokeColor=DARK_BG))
    d.add(String(10, h-15, "RELATIONAL DATA SCHEMA (ER DIAGRAM) - 8 CORE ENTITIES & CARDINALITY", fontName="Helvetica-Bold", fontSize=8, fillColor=GOLD))
    
    # Legend
    d.add(Rect(320, h-17, 8, 8, fillColor=colors.HexColor("#DC2626"), strokeColor=colors.HexColor("#DC2626")))
    d.add(String(332, h-14, "PK: Primary Key", fontName="Helvetica", fontSize=6.5, fillColor=colors.white))
    d.add(Rect(390, h-17, 8, 8, fillColor=colors.HexColor("#2563EB"), strokeColor=colors.HexColor("#2563EB")))
    d.add(String(402, h-14, "FK: Foreign Key", fontName="Helvetica", fontSize=6.5, fillColor=colors.white))
    d.add(String(460, h-14, "1 : N Relational", fontName="Helvetica-Bold", fontSize=6.5, fillColor=colors.HexColor("#38BDF8")))

    def draw_entity(x, y, ew, eh, title, header_bg, fields):
        d.add(Rect(x, y, ew, eh, rx=4, ry=4, fillColor=colors.white, strokeColor=colors.HexColor("#94A3B8"), strokeWidth=0.8))
        header_h = 16
        d.add(Rect(x, y + eh - header_h, ew, header_h, rx=4, ry=4, fillColor=header_bg, strokeColor=header_bg))
        d.add(Rect(x, y + eh - header_h, ew, 4, fillColor=header_bg, strokeColor=header_bg))
        d.add(String(x + 5, y + eh - 12, title, fontName="Helvetica-Bold", fontSize=6.8, fillColor=colors.white))
        curr_y = y + eh - header_h - 9
        for fld in fields:
            is_pk = fld.startswith("[PK]")
            is_fk = fld.startswith("[FK]")
            is_uk = fld.startswith("[UK]")
            col = colors.HexColor("#DC2626") if is_pk else (colors.HexColor("#2563EB") if is_fk else (colors.HexColor("#D97706") if is_uk else colors.HexColor("#334155")))
            f_font = "Helvetica-Bold" if (is_pk or is_fk or is_uk) else "Helvetica"
            d.add(String(x + 5, curr_y, fld, fontName=f_font, fontSize=5.8, fillColor=col))
            curr_y -= 9.5

    # 1. USERS
    draw_entity(8, 185, 120, 110, "USERS (Auth & RBAC)", colors.HexColor("#1E293B"), [
        "[PK] id : INT (AUTO)", "[UK] username : VARCHAR", "password_hash : VARCHAR",
        "role : ENUM(ADMIN..)", "[FK] emp_code : VARCHAR", "is_active : BOOLEAN",
        "last_login : TIMESTAMP", "created_at : TIMESTAMP"
    ])

    # 2. EMPLOYEES
    draw_entity(180, 165, 150, 130, "EMPLOYEES (Workforce Core)", colors.HexColor("#1E3A8A"), [
        "[PK] id : INT (AUTO)", "[UK] emp_code : VARCHAR(20)", "name : VARCHAR(100)",
        "department : VARCHAR(50)", "designation : VARCHAR(50)", "phone : VARCHAR(15)",
        "email : VARCHAR(100)", "shift : VARCHAR(20)", "efficiency : INT",
        "status : VARCHAR(20)", "joining_date : DATE"
    ])

    # 3. ATTENDANCE
    draw_entity(385, 185, 135, 110, "ATTENDANCE (GPS/Shift)", colors.HexColor("#047857"), [
        "[PK] id : INT (AUTO)", "[FK] emp_code : VARCHAR(20)", "date : DATE",
        "time_in : TIME", "time_out : TIME", "duration_hrs : FLOAT",
        "gps_coords : VARCHAR(50)", "status : VARCHAR(20)"
    ])

    # 4. LEAVE_REQUESTS
    draw_entity(8, 20, 120, 120, "LEAVE_REQUESTS (Portal)", colors.HexColor("#7C3AED"), [
        "[PK] id : INT (AUTO)", "[FK] emp_code : VARCHAR(20)", "leave_type : ENUM(CL,SL,PL)",
        "start_date : DATE", "end_date : DATE", "days_count : INT",
        "reason : TEXT", "status : ENUM(Apprv..)", "[FK] approved_by : INT", "applied_at : TIMESTAMP"
    ])

    # 5. TASKS
    draw_entity(180, 20, 150, 120, "TASKS (Schedules & SOPs)", colors.HexColor("#0284C7"), [
        "[PK] id : INT (AUTO)", "[UK] task_code : VARCHAR(20)", "[FK] assigned_to : VARCHAR(20)",
        "title : VARCHAR(100)", "location : VARCHAR(100)", "priority : ENUM(Hi,Med,Lo)",
        "scheduled_date : DATE", "status : ENUM(Pending..)", "[FK] inspected_by : INT", "completed_at : TIMESTAMP"
    ])

    # 6. MAINTENANCE_TICKETS
    draw_entity(385, 82, 135, 75, "MAINTENANCE_TICKETS", colors.HexColor("#D97706"), [
        "[PK] id : INT (AUTO)", "[UK] ticket_no : VARCHAR(20)", "client_name : VARCHAR(100)",
        "location : VARCHAR(100)", "severity : VARCHAR(20)", "status : VARCHAR(20)"
    ])

    # 7. INVENTORY_ITEMS
    draw_entity(385, 20, 135, 55, "INVENTORY_ITEMS", colors.HexColor("#475569"), [
        "[PK] id : INT (AUTO)", "[UK] item_code : VARCHAR(20)", "item_name : VARCHAR(80)",
        "quantity : INT", "reorder_level : INT"
    ])

    # Connectors
    d.add(Line(128, 240, 180, 240, strokeColor=colors.HexColor("#2563EB"), strokeWidth=1.2))
    d.add(String(132, 243, "1", fontName="Helvetica-Bold", fontSize=7, fillColor=colors.HexColor("#DC2626")))
    d.add(String(172, 243, "1", fontName="Helvetica-Bold", fontSize=7, fillColor=colors.HexColor("#1D4ED8")))

    d.add(Line(330, 240, 385, 240, strokeColor=colors.HexColor("#2563EB"), strokeWidth=1.2))
    d.add(String(334, 243, "1", fontName="Helvetica-Bold", fontSize=7, fillColor=colors.HexColor("#DC2626")))
    d.add(String(375, 243, "N", fontName="Helvetica-Bold", fontSize=7, fillColor=colors.HexColor("#1D4ED8")))

    d.add(Line(255, 165, 255, 140, strokeColor=colors.HexColor("#2563EB"), strokeWidth=1.2))
    d.add(String(258, 155, "1", fontName="Helvetica-Bold", fontSize=7, fillColor=colors.HexColor("#DC2626")))
    d.add(String(258, 142, "N", fontName="Helvetica-Bold", fontSize=7, fillColor=colors.HexColor("#1D4ED8")))

    return d

def create_gantt_chart_drawing():
    """Generates vector Gantt Chart for Chapter 29."""
    w, h = 532, 280
    d = Drawing(w, h)
    d.add(Rect(0, 0, w, h, rx=6, ry=6, fillColor=colors.white, strokeColor=BORDER_COLOR, strokeWidth=1))
    
    header_h = 24
    d.add(Rect(0, h - header_h, w, header_h, rx=6, ry=6, fillColor=DARK_BG, strokeColor=DARK_BG))
    d.add(Rect(0, h - header_h, w, 6, fillColor=DARK_BG, strokeColor=DARK_BG))
    d.add(String(10, h - 16, "PROJECT WORKSTREAM & ENGINEERING TIMELINE (16 WEEKS)", fontName="Helvetica-Bold", fontSize=7.5, fillColor=GOLD))
    
    col_w = 42
    start_x = 185
    weeks = ["W1-2", "W3-4", "W5-6", "W7-8", "W9-10", "W11-12", "W13-14", "W15-16"]
    for i, wk in enumerate(weeks):
        cx = start_x + i * col_w
        d.add(String(cx + 8, h - 16, wk, fontName="Helvetica-Bold", fontSize=6.8, fillColor=colors.white))
        
    for i in range(len(weeks) + 1):
        gx = start_x + i * col_w
        d.add(Line(gx, 25, gx, h - header_h, strokeColor=colors.HexColor("#F1F5F9"), strokeWidth=0.8))

    tasks = [
        ("1. Architecture & Security Model", 0.0, 1.0, "100%", colors.HexColor("#059669"), None),
        ("2. DB Schema & Python REST Daemon", 0.6, 1.2, "100%", colors.HexColor("#059669"), 1.8),
        ("3. Luxury UI & HTML5 Portals", 1.4, 1.4, "100%", colors.HexColor("#059669"), None),
        ("4. Staff App PWA & Stopwatch State", 2.2, 1.6, "100%", colors.HexColor("#059669"), 3.8),
        ("5. Biometric GPS Punch & KYC Flow", 3.2, 1.5, "100%", colors.HexColor("#059669"), None),
        ("6. Firebase Real-Time Synchronization", 4.2, 1.4, "100%", colors.HexColor("#059669"), 5.6),
        ("7. QA Audit, Penetration Test & Launch", 5.2, 1.2, "100%", colors.HexColor("#059669"), 6.4),
        ("8. Continuous SLA Operations & Support", 6.0, 2.0, "96%", colors.HexColor("#D97706"), None)
    ]

    row_h = 24
    start_y = h - header_h - 22
    for idx, (tname, s_idx, span, pct_label, bar_color, milestone_idx) in enumerate(tasks):
        y = start_y - (idx * row_h)
        if idx % 2 == 0:
            d.add(Rect(0, y - 5, w, row_h, fillColor=LIGHT_BG, strokeColor=colors.transparent))
        d.add(String(10, y + 2, tname, fontName="Helvetica-Bold", fontSize=6.8, fillColor=TEXT_MAIN))
        bx = start_x + (s_idx * col_w)
        bw = span * col_w
        d.add(Rect(bx, y - 2, bw, 13, rx=3, ry=3, fillColor=bar_color, strokeColor=bar_color))
        d.add(String(bx + 4, y + 2, pct_label, fontName="Helvetica-Bold", fontSize=6, fillColor=colors.white))
        if milestone_idx is not None:
            mx = start_x + (milestone_idx * col_w)
            my = y + 4.5
            d.add(Polygon([mx, my + 5, mx + 5, my, mx, my - 5, mx - 5, my], fillColor=GOLD, strokeColor=DARK_BG, strokeWidth=0.8))

    # Bottom Legend
    leg_y = 6
    d.add(Rect(0, 0, w, 22, rx=6, ry=6, fillColor=DARK_BG, strokeColor=DARK_BG))
    d.add(Rect(0, 16, w, 6, fillColor=DARK_BG, strokeColor=DARK_BG))
    d.add(Rect(15, leg_y + 2, 12, 8, rx=2, ry=2, fillColor=colors.HexColor("#059669"), strokeColor=colors.HexColor("#059669")))
    d.add(String(32, leg_y + 3, "Completed Phases (100%)", fontName="Helvetica", fontSize=6.5, fillColor=colors.white))
    d.add(Rect(175, leg_y + 2, 12, 8, rx=2, ry=2, fillColor=colors.HexColor("#D97706"), strokeColor=colors.HexColor("#D97706")))
    d.add(String(192, leg_y + 3, "Active SLA Tracking (96%)", fontName="Helvetica", fontSize=6.5, fillColor=colors.white))
    d.add(Polygon([325, leg_y + 6, 329, leg_y + 2, 325, leg_y - 2, 321, leg_y + 2], fillColor=GOLD, strokeColor=colors.white, strokeWidth=0.5))
    d.add(String(335, leg_y + 3, "Milestone Deliverable (M1: REST, M2: Staff PWA, M3: Cloud Go-Live)", fontName="Helvetica", fontSize=6.5, fillColor=colors.white))
    return d

print("Drawings and visual engines ready.")
