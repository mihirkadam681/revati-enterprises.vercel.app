"""
Revati Enterprises - Master Source Code Word Document (.docx) Generator
Generates an enterprise-grade Microsoft Word document containing all source code
used to build the Revati Enterprises Commercial Housekeeping & Facility Management website.
"""

import os
import sys
import time
import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn

# --- Color Constants ---
COLOR_NAVY = "0F294A"      # #0F294A (Deep Navy Blue)
COLOR_BLUE = "1E3A8A"      # #1E3A8A (Corporate Blue)
COLOR_TEAL = "0284C7"      # #0284C7 (Sky Accent)
COLOR_DARK = "0F172A"      # #0F172A (Slate 900 Text)
COLOR_MUTED = "64748B"     # #64748B (Muted Gray Text)
COLOR_BORDER = "CBD5E1"    # #CBD5E1 (Border Gray)
COLOR_BG_LIGHT = "F8FAFC"  # #F8FAFC (Subtle Slate Background)
COLOR_BG_ALT = "F1F5F9"    # #F1F5F9 (Alternate Row Background)
COLOR_CODE = "1E293B"      # #1E293B (Code Monospace Text)

def set_cell_background(cell, fill_hex):
    """Sets background fill of a table cell."""
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)

def set_cell_padding(cell, top=100, bottom=100, left=150, right=150):
    """Sets cell padding in dxa (1 pt = 20 dxa)."""
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(
        f'<w:tcMar {nsdecls("w")}>'
        f'<w:top w:w="{top}" w:type="dxa"/>'
        f'<w:bottom w:w="{bottom}" w:type="dxa"/>'
        f'<w:left w:w="{left}" w:type="dxa"/>'
        f'<w:right w:w="{right}" w:type="dxa"/>'
        f'</w:tcMar>'
    )
    tcPr.append(tcMar)

def set_cell_borders(cell, top=None, bottom=None, left=None, right=None):
    """Applies clean borders to a cell."""
    tcPr = cell._tc.get_or_add_tcPr()
    borders = ['<w:tcBorders %s>' % nsdecls("w")]
    for side, border in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        if border:
            val = border.get('val', 'single')
            sz = border.get('sz', '4')
            color = border.get('color', COLOR_BORDER)
            borders.append(f'<w:{side} w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>')
        else:
            borders.append(f'<w:{side} w:val="none"/>')
    borders.append('</w:tcBorders>')
    tcBorders = parse_xml(''.join(borders))
    tcPr.append(tcBorders)

def add_header_footer(doc):
    """Adds running headers and footers to the document."""
    for section in doc.sections:
        # Header
        header = section.header
        hp = header.paragraphs[0]
        hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        hrun = hp.add_run("REVATI ENTERPRISES  |  Complete Source Code Repository")
        hrun.font.name = "Calibri"
        hrun.font.size = Pt(8.5)
        hrun.font.color.rgb = RGBColor(100, 116, 139)

        # Footer
        footer = section.footer
        fp = footer.paragraphs[0]
        fp.alignment = WD_ALIGN_PARAGRAPH.LEFT
        frun1 = fp.add_run("Commercial Facility Management & Housekeeping Web Application  •  Confidential")
        frun1.font.name = "Calibri"
        frun1.font.size = Pt(8.5)
        frun1.font.color.rgb = RGBColor(100, 116, 139)

        # Page numbering run on the right
        fp_right = footer.add_paragraph()
        fp_right.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        fp_right.paragraph_format.space_before = Pt(0)
        fp_right.paragraph_format.space_after = Pt(0)
        
        prun = fp_right.add_run("Page ")
        prun.font.name = "Calibri"
        prun.font.size = Pt(8.5)
        prun.font.color.rgb = RGBColor(100, 116, 139)
        
        fld1 = parse_xml(r'<w:fldChar %s w:fldCharType="begin"/>' % nsdecls('w'))
        instr1 = parse_xml(r'<w:instrText %s xml:space="preserve"> PAGE </w:instrText>' % nsdecls('w'))
        fld2 = parse_xml(r'<w:fldChar %s w:fldCharType="separate"/>' % nsdecls('w'))
        fld3 = parse_xml(r'<w:fldChar %s w:fldCharType="end"/>' % nsdecls('w'))
        prun._r.append(fld1); prun._r.append(instr1); prun._r.append(fld2); prun._r.append(fld3)

        prun2 = fp_right.add_run(" of ")
        prun2.font.name = "Calibri"
        prun2.font.size = Pt(8.5)
        prun2.font.color.rgb = RGBColor(100, 116, 139)

        fld4 = parse_xml(r'<w:fldChar %s w:fldCharType="begin"/>' % nsdecls('w'))
        instr2 = parse_xml(r'<w:instrText %s xml:space="preserve"> NUMPAGES </w:instrText>' % nsdecls('w'))
        fld5 = parse_xml(r'<w:fldChar %s w:fldCharType="separate"/>' % nsdecls('w'))
        fld6 = parse_xml(r'<w:fldChar %s w:fldCharType="end"/>' % nsdecls('w'))
        prun2._r.append(fld4); prun2._r.append(instr2); prun2._r.append(fld5); prun2._r.append(fld6)

# Master Registry of all 33 files organized into clean categories
FILES_REGISTRY = [
    # -------------------------------------------------------------
    # CATEGORY 1: FRONTEND USER INTERFACE PAGES (HTML5)
    # -------------------------------------------------------------
    {
        "category": "Frontend User Interface Pages (HTML5)",
        "section_id": "2",
        "files": [
            {
                "path": "about.html",
                "name": "about.html",
                "lang": "HTML5 / Web Standard",
                "title": "Corporate Profile, Vision & Standards Page",
                "desc": "Presents corporate credentials, company background, mission, vision, ISO 9001:2015 quality assurance standards, environmental health and safety certifications, leadership team bios, and corporate facility management compliance protocols."
            },
            {
                "path": "admin.html",
                "name": "admin.html",
                "lang": "HTML5 / Web Standard",
                "title": "Enterprise Operations & Administrative Dashboard",
                "desc": "Master operations management dashboard for facility managers and system administrators. Provides real-time metrics, active client contract monitoring, staff attendance tracking, task scheduling, customer complaint escalation management, chemical and machinery inventory auditing, revenue analytics, and access control."
            },
            {
                "path": "contact.html",
                "name": "contact.html",
                "lang": "HTML5 / Web Standard",
                "title": "Client Inquiry, Support & Geolocation Portal",
                "desc": "Customer contact and inquiry interface featuring multi-field service quote request form, interactive corporate address mapping, direct WhatsApp dispatch integration, emergency facility incident response helpline, and operational business hours."
            },
            {
                "path": "estimator.html",
                "name": "estimator.html",
                "lang": "HTML5 / Web Standard",
                "title": "Commercial Cost, Area & Frequency Pricing Estimator",
                "desc": "Interactive dynamic cost estimation engine. Allows clients to configure facility square footage, premises category (IT parks, hospitals, commercial towers, warehouses), service frequency, staff count, specialized chemical/machinery options, and generate real-time itemized price estimates with PDF export capabilities."
            },
            {
                "path": "index.html",
                "name": "index.html",
                "lang": "HTML5 / Web Standard",
                "title": "Primary Corporate Landing Page & Value Showcase",
                "desc": "Core entry page of the platform featuring dynamic 3D hero particle animations, cinematic video teaser modal, value propositions, commercial housekeeping service grid, enterprise client testimonials, animated live statistics, quote request call-to-actions, and comprehensive footer navigation."
            },
            {
                "path": "letterhead.html",
                "name": "letterhead.html",
                "lang": "HTML5 / Web Standard",
                "title": "Official Proposal, Quotation & Document Generator",
                "desc": "Standardized corporate proposal and quotation generator. Features ISO-compliant enterprise letterhead layouts, dynamic line-item billing calculations, GST and discount computations, digital signature authorization pads, and high-fidelity print/PDF export layouts."
            },
            {
                "path": "register.html",
                "name": "register.html",
                "lang": "HTML5 / Web Standard",
                "title": "Multi-Role Account Creation & Access Portal",
                "desc": "Enterprise onboarding and registration interface supporting multi-role signup (Client Organization, Staff Technician, Facility Supervisor, Administrator). Includes input validation, terms of service acceptance, password strength verification, and Firebase Auth registration hooks."
            },
            {
                "path": "services.html",
                "name": "services.html",
                "lang": "HTML5 / Web Standard",
                "title": "Comprehensive Commercial Services Directory",
                "desc": "Detailed commercial service catalog showcasing Corporate Housekeeping, Mechanized Floor Scrubbing, High-Rise Facade Cleaning, MEP (Mechanical, Electrical, Plumbing) Engineering Maintenance, Industrial Pest Management, Waste Management, and Hospitality Support."
            },
            {
                "path": "staff.html",
                "name": "staff.html",
                "lang": "HTML5 / Web Standard",
                "title": "Field Workforce Mobile Operations Portal",
                "desc": "Mobile-first responsive operations portal for field technicians and cleaning crews. Enables GPS geolocation clock-in/clock-out attendance logging, daily cleaning task checklists, supply usage recording, safety hazard incident reporting, and supervisor communication."
            },
            {
                "path": "welcome.html",
                "name": "welcome.html",
                "lang": "HTML5 / Web Standard",
                "title": "Client Onboarding & Contract Initiation Portal",
                "desc": "Dedicated onboarding hub for new commercial contracts. Outlines Service Level Agreements (SLAs), operational onboarding schedules, assigned facility managers, safety orientation protocols, and direct dashboard quick-links."
            }
        ]
    },
    # -------------------------------------------------------------
    # CATEGORY 2: STYLING & VISUAL DESIGN SYSTEM (CSS3)
    # -------------------------------------------------------------
    {
        "category": "Styling & Visual Design System (CSS3)",
        "section_id": "3",
        "files": [
            {
                "path": "css/styles.css",
                "name": "css/styles.css",
                "lang": "CSS3 / Modern Design Tokens",
                "title": "Master Enterprise Design System & Component Stylesheet",
                "desc": "Core design tokens and layout styling system. Defines CSS custom properties (variables) for primary/accent palettes, typography scale, responsive grid and flexbox systems, glassmorphism card surfaces, dashboard widgets, modal dialogs, toast notifications, buttons, badges, tables, theme switches, and print media rules."
            },
            {
                "path": "css/video-intro.css",
                "name": "css/video-intro.css",
                "lang": "CSS3 / Animation Stylesheet",
                "title": "Cinematic Video Intro & Animated Canvas Stylesheet",
                "desc": "Specialized visual styling for the brand video introduction modal. Features full-screen backdrop blurs, audio/video playback control layouts, canvas overlay positioning, pulse rings, and keyframe entrance/exit transitions."
            }
        ]
    },
    # -------------------------------------------------------------
    # CATEGORY 3: FRONTEND LOGIC & APPLICATION SCRIPTS (JAVASCRIPT)
    # -------------------------------------------------------------
    {
        "category": "Frontend Logic & Application Scripts (JavaScript ES6+)",
        "section_id": "4",
        "files": [
            {
                "path": "js/api.js",
                "name": "js/api.js",
                "lang": "JavaScript (ES6+) / REST Client",
                "title": "Centralized REST API Client & Network Service Layer",
                "desc": "Unified API gateway wrapper around fetch(). Manages JWT Bearer token lifecycle, request/response headers, error handling, and dedicated REST endpoints for user authentication, staff attendance, task assignments, inventory items, and administrative reports."
            },
            {
                "path": "js/app.js",
                "name": "js/app.js",
                "lang": "JavaScript (ES6+) / Core Controller",
                "title": "Core Application Controller, State Engine & UI Logic",
                "desc": "Central web application orchestrator. Handles client-side application state, DOM event listeners, mobile navigation drawers, counter animations, interactive modals, toast notification dispatchers, search and filter controls, and dynamic page state."
            },
            {
                "path": "js/excelExporter.js",
                "name": "js/excelExporter.js",
                "lang": "JavaScript (ES6+) / Utility",
                "title": "Enterprise Data Export Utility (CSV / Excel)",
                "desc": "Client-side spreadsheet generation utility. Converts HTML data tables and JSON object arrays into structured CSV format, sets MIME headers, and triggers browser file downloads with automatic timestamped filenames."
            },
            {
                "path": "js/firebase-service.js",
                "name": "js/firebase-service.js",
                "lang": "JavaScript (ES6+) / Cloud Database Service",
                "title": "Google Cloud Firestore & Firebase Auth Adapter",
                "desc": "Firebase integration module managing Cloud Firestore database collections and Firebase Authentication. Implements real-time collection listeners, document creation, updates, and sync for employees, tasks, and attendance."
            },
            {
                "path": "js/letterhead.js",
                "name": "js/letterhead.js",
                "lang": "JavaScript (ES6+) / Document Engine",
                "title": "Quotation Calculation Engine & Proposal Document Builder",
                "desc": "Dynamic quotation and letterhead builder logic. Calculates subtotal, GST/tax percentages, discounts, and net payable totals, auto-generates invoice numbers, binds form inputs to the live document view, and coordinates jsPDF export."
            },
            {
                "path": "js/mockData.js",
                "name": "js/mockData.js",
                "lang": "JavaScript (ES6+) / Fallback Data",
                "title": "Offline Simulation Records & Fallback Dataset",
                "desc": "Preconfigured offline mock database storing baseline client accounts, employees, maintenance tasks, and inventory for local previews and offline demonstration without an active backend."
            },
            {
                "path": "js/scroll3d.js",
                "name": "js/scroll3d.js",
                "lang": "JavaScript (ES6+) / Animation Controller",
                "title": "3D Interactive Parallax & Mouse Dynamics Engine",
                "desc": "Calculates mousemove perspective tilt and scroll-linked 3D matrix transforms for hero cards. Uses requestAnimationFrame optimization for smooth 60fps rendering without layout jank."
            },
            {
                "path": "js/theme-switcher.js",
                "name": "js/theme-switcher.js",
                "lang": "JavaScript (ES6+) / State Utility",
                "title": "Theme Switcher Bootstrap & State Persister",
                "desc": "Bootstrap script initializing dark and light mode preferences, synchronizing HTML root data attributes with localStorage."
            },
            {
                "path": "js/video-intro.js",
                "name": "js/video-intro.js",
                "lang": "JavaScript (ES6+) / Multimedia Engine",
                "title": "Interactive Video Intro & Canvas Particle Controller",
                "desc": "Interactive cinematic player and HTML5 canvas particle physics engine. Manages video playback, audio fading, particle rendering, user skip preferences, and session persistence."
            },
            {
                "path": "sw.js",
                "name": "sw.js",
                "lang": "JavaScript (PWA Service Worker)",
                "title": "Progressive Web App Service Worker (Offline Cache)",
                "desc": "Service worker implementing cache-first offline asset strategies, network fallbacks, cache invalidation, and background synchronization for field personnel operating in low-connectivity commercial environments."
            }
        ]
    },
    # -------------------------------------------------------------
    # CATEGORY 4: BACKEND IMPLEMENTATIONS & DATA STORES (PYTHON & JAVA)
    # -------------------------------------------------------------
    {
        "category": "Backend Microservices & Server Logic (Python & Java)",
        "section_id": "5",
        "files": [
            {
                "path": "server.py",
                "name": "server.py",
                "lang": "Python 3 / HTTP REST Server",
                "title": "Python REST Backend Server with JWT Authentication",
                "desc": "Lightweight Python HTTP server implementing custom REST routing, JWT Bearer token generation and verification, SHA-256 password hashing, CORS headers, and CRUD API endpoints for authentication, attendance, staff, tasks, inventory, and reports."
            },
            {
                "path": "CommercialHousekeepingServer.java",
                "name": "CommercialHousekeepingServer.java",
                "lang": "Java / Standalone HTTP Server",
                "title": "Standalone Java Microservice Server with JWT & BCrypt",
                "desc": "Pure Java HTTP server built using com.sun.net.httpserver. Implements concurrent executor thread pooling, HMAC-SHA256 JWT token generation, password hashing, thread-safe in-memory state stores, static file serving, and REST endpoints for all platform operations."
            },
            {
                "path": "src/main/java/com/housekeeping/HousekeepingApplication.java",
                "name": "src/main/java/com/housekeeping/HousekeepingApplication.java",
                "lang": "Java / Spring Boot",
                "title": "Spring Boot Application Entry Point",
                "desc": "Spring Boot application entry point annotated with @SpringBootApplication, initializing the embedded Tomcat container, auto-configuration, and dependency injection context."
            },
            {
                "path": "src/main/java/com/housekeeping/controller/HousekeepingController.java",
                "name": "src/main/java/com/housekeeping/controller/HousekeepingController.java",
                "lang": "Java / Spring Boot REST Controller",
                "title": "Spring MVC REST Operations Controller",
                "desc": "Spring @RestController exposing enterprise REST endpoints for service catalog, client inquiries, operations health check, and system status with @CrossOrigin support."
            },
            {
                "path": "seed_firestore.py",
                "name": "seed_firestore.py",
                "lang": "Python 3 / Cloud Database Seeder",
                "title": "Cloud Firestore Database Seeder & Mock Data Injector",
                "desc": "Database initialization script for Google Cloud Firestore. Populates collections for users, employees, client contracts, daily tasks, machinery inventory, and cleaning supplies."
            },
            {
                "path": "db_store.json",
                "name": "db_store.json",
                "lang": "JSON / Database Store",
                "title": "Local JSON Document Database Schema & Baseline State",
                "desc": "Baseline JSON document database store providing persistent local records for users, employees, facilities, tasks, and inventory items for zero-configuration execution."
            }
        ]
    },
    # -------------------------------------------------------------
    # CATEGORY 5: CONFIGURATION & DEPLOYMENT SPECIFICATIONS
    # -------------------------------------------------------------
    {
        "category": "Configuration, Build & Deployment Specifications",
        "section_id": "6",
        "files": [
            {
                "path": "manifest.json",
                "name": "manifest.json",
                "lang": "JSON / PWA Manifest",
                "title": "Progressive Web App Manifest Specification",
                "desc": "PWA web application manifest defining application name, icons, standalone display mode, orientation, theme colors, and background colors for home-screen installation."
            },
            {
                "path": "pom.xml",
                "name": "pom.xml",
                "lang": "XML / Maven Build Descriptor",
                "title": "Maven Project Object Model & Java Dependency Management",
                "desc": "Apache Maven build descriptor for the Java Spring Boot application, specifying dependencies (Spring Boot Starter Web, Jackson, JJWT, Lombok) and Maven compiler plugins."
            },
            {
                "path": "src/main/resources/application.properties",
                "name": "src/main/resources/application.properties",
                "lang": "Properties / Configuration",
                "title": "Spring Boot Application Configuration Properties",
                "desc": "Spring Boot application configuration properties defining server port (8080), application metadata, JSON serialization formatting, and logging levels."
            },
            {
                "path": "vercel.json",
                "name": "vercel.json",
                "lang": "JSON / Cloud Hosting",
                "title": "Vercel Cloud Serverless Deployment & Routing Descriptor",
                "desc": "Vercel cloud deployment descriptor specifying routing rules, SPA rewrites, and static asset CDN caching headers."
            },
            {
                "path": ".gitignore",
                "name": ".gitignore",
                "lang": "Git Configuration",
                "title": "Git Version Control Exclusion Specification",
                "desc": "Git version control exclusion file ignoring compiled Java bytecode (*.class, target/), Python caches (__pycache__/, *.pyc), virtual environments, and temporary stores."
            }
        ]
    }
]

def build_word_document():
    print("=" * 80)
    print("REVATI ENTERPRISES - WORD DOCUMENT GENERATION PROCESS")
    print("=" * 80)
    t_start = time.time()

    doc = Document()

    # Configure Margins: 0.75 in (54 pt) all around for professional engineering density
    for sec in doc.sections:
        sec.top_margin = Inches(0.75)
        sec.bottom_margin = Inches(0.75)
        sec.left_margin = Inches(0.75)
        sec.right_margin = Inches(0.75)

    add_header_footer(doc)

    # -------------------------------------------------------------
    # 1. COVER PAGE / TITLE PAGE
    # -------------------------------------------------------------
    print("Generating Cover Page...")
    
    # Top Decorative Spacing
    p_top_space = doc.add_paragraph()
    p_top_space.paragraph_format.space_before = Pt(36)
    p_top_space.paragraph_format.space_after = Pt(12)

    # Enterprise Name
    p_brand = doc.add_paragraph()
    p_brand.paragraph_format.space_before = Pt(0)
    p_brand.paragraph_format.space_after = Pt(6)
    r_brand = p_brand.add_run("REVATI ENTERPRISES")
    r_brand.font.name = "Calibri"
    r_brand.font.size = Pt(28)
    r_brand.font.bold = True
    r_brand.font.color.rgb = RGBColor(15, 41, 74) # Navy

    # Subtitle
    p_sub = doc.add_paragraph()
    p_sub.paragraph_format.space_before = Pt(0)
    p_sub.paragraph_format.space_after = Pt(18)
    r_sub = p_sub.add_run("COMMERCIAL FACILITY MANAGEMENT & HOUSEKEEPING PLATFORM")
    r_sub.font.name = "Calibri"
    r_sub.font.size = Pt(14)
    r_sub.font.bold = True
    r_sub.font.color.rgb = RGBColor(2, 132, 199) # Sky Accent

    # Accent Divider Bar
    p_div = doc.add_paragraph()
    p_div.paragraph_format.space_before = Pt(0)
    p_div.paragraph_format.space_after = Pt(24)
    r_div = p_div.add_run("━" * 52)
    r_div.font.name = "Calibri"
    r_div.font.size = Pt(12)
    r_div.font.color.rgb = RGBColor(203, 213, 225)

    # Main Document Title
    p_title = doc.add_paragraph()
    p_title.paragraph_format.space_before = Pt(0)
    p_title.paragraph_format.space_after = Pt(8)
    r_title = p_title.add_run("Complete Source Code Repository\n& Technical Architecture Specification")
    r_title.font.name = "Calibri"
    r_title.font.size = Pt(22)
    r_title.font.bold = True
    r_title.font.color.rgb = RGBColor(15, 23, 42)

    p_doc_desc = doc.add_paragraph()
    p_doc_desc.paragraph_format.space_before = Pt(0)
    p_doc_desc.paragraph_format.space_after = Pt(28)
    r_doc_desc = p_doc_desc.add_run(
        "A comprehensive, classified documentation volume containing 100% of the custom source code, "
        "stylesheets, interactive scripts, backend REST microservices, cloud database bindings, "
        "and deployment configurations engineered for the Revati Enterprises web application."
    )
    r_doc_desc.font.name = "Calibri"
    r_doc_desc.font.size = Pt(11)
    r_doc_desc.font.color.rgb = RGBColor(71, 85, 105)

    # Metadata Summary Box Table
    meta_table = doc.add_table(rows=6, cols=2)
    meta_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    meta_table.autofit = False

    meta_data = [
        ("Platform Version", "v2.4.0 (Enterprise Commercial Production Release)"),
        ("System Architecture", "HTML5 Single Page App + Progressive Web App + Dual REST Backend (Python & Java)"),
        ("Custom Source Files", "33 Core Platform Files (Sorted & Categorized)"),
        ("Total Source Lines", "15,469 Lines of Custom Source Code"),
        ("Technology Stack", "HTML5, CSS3, JavaScript (ES6+), Python 3, Java (Spring Boot & Sun HTTP), Firestore, PWA"),
        ("Document Classification", "Confidential & Proprietary Technical Architecture Documentation")
    ]

    for row_idx, (lbl, val) in enumerate(meta_data):
        row = meta_table.rows[row_idx]
        
        # Left label cell
        c0 = row.cells[0]
        c0.width = Inches(2.2)
        set_cell_background(c0, COLOR_NAVY if row_idx % 2 == 0 else "16365C")
        set_cell_padding(c0, top=100, bottom=100, left=150, right=150)
        set_cell_borders(c0, 
                         top=dict(val='single', sz=4, color=COLOR_BORDER),
                         bottom=dict(val='single', sz=4, color=COLOR_BORDER),
                         left=dict(val='single', sz=4, color=COLOR_BORDER),
                         right=dict(val='single', sz=4, color=COLOR_BORDER))
        p0 = c0.paragraphs[0]
        p0.paragraph_format.space_before = Pt(0)
        p0.paragraph_format.space_after = Pt(0)
        r0 = p0.add_run(lbl)
        r0.font.name = "Calibri"
        r0.font.size = Pt(10)
        r0.font.bold = True
        r0.font.color.rgb = RGBColor(255, 255, 255)

        # Right value cell
        c1 = row.cells[1]
        c1.width = Inches(4.8)
        set_cell_background(c1, COLOR_BG_LIGHT if row_idx % 2 == 0 else "FFFFFF")
        set_cell_padding(c1, top=100, bottom=100, left=150, right=150)
        set_cell_borders(c1, 
                         top=dict(val='single', sz=4, color=COLOR_BORDER),
                         bottom=dict(val='single', sz=4, color=COLOR_BORDER),
                         left=dict(val='single', sz=4, color=COLOR_BORDER),
                         right=dict(val='single', sz=4, color=COLOR_BORDER))
        p1 = c1.paragraphs[0]
        p1.paragraph_format.space_before = Pt(0)
        p1.paragraph_format.space_after = Pt(0)
        r1 = p1.add_run(val)
        r1.font.name = "Calibri"
        r1.font.size = Pt(10)
        r1.font.color.rgb = RGBColor(15, 23, 42)

    doc.add_page_break()

    # -------------------------------------------------------------
    # 2. SECTION 1: ARCHITECTURAL BLUEPRINT & MASTER INDEX
    # -------------------------------------------------------------
    print("Generating Section 1: Executive Architectural Blueprint & Master File Index...")
    
    h1 = doc.add_paragraph()
    h1.paragraph_format.space_before = Pt(12)
    h1.paragraph_format.space_after = Pt(6)
    r_h1 = h1.add_run("1. Executive System Architecture & Master Codebase Directory")
    r_h1.font.name = "Calibri"
    r_h1.font.size = Pt(18)
    r_h1.font.bold = True
    r_h1.font.color.rgb = RGBColor(15, 41, 74)

    p_arch = doc.add_paragraph()
    p_arch.paragraph_format.space_before = Pt(4)
    p_arch.paragraph_format.space_after = Pt(10)
    p_arch.paragraph_format.line_spacing = 1.15
    r_arch = p_arch.add_run(
        "The Revati Enterprises Commercial Facility Management Platform is designed as a modern, high-resilience, "
        "multi-tier web application tailored for enterprise facility administration, commercial housekeeping quotation, "
        "and field workforce operations. The system incorporates an integrated Progressive Web App (PWA) frontend with "
        "rich glassmorphic aesthetics, a centralized REST API service client with JWT security tokens, and support for dual "
        "backend microservice tiers (Python HTTP server and Java Spring Boot / Standalone HTTP server)."
    )
    r_arch.font.name = "Calibri"
    r_arch.font.size = Pt(10)
    r_arch.font.color.rgb = RGBColor(15, 23, 42)

    # Master File Index Table
    p_idx_title = doc.add_paragraph()
    p_idx_title.paragraph_format.space_before = Pt(12)
    p_idx_title.paragraph_format.space_after = Pt(6)
    r_idx_title = p_idx_title.add_run("Master Codebase Inventory (All 33 Custom Files Sorted & Categorized)")
    r_idx_title.font.name = "Calibri"
    r_idx_title.font.size = Pt(13)
    r_idx_title.font.bold = True
    r_idx_title.font.color.rgb = RGBColor(30, 58, 138)

    # Compute statistics and build table
    all_files_flat = []
    for cat in FILES_REGISTRY:
        for f in cat["files"]:
            f["category_name"] = cat["category"]
            f["section_id"] = cat["section_id"]
            # Read file stats
            if os.path.exists(f["path"]):
                sz = os.path.getsize(f["path"])
                with open(f["path"], 'r', encoding='utf-8', errors='ignore') as fp:
                    lines = fp.readlines()
                    line_count = len(lines)
            else:
                sz = 0
                line_count = 0
            f["size_bytes"] = sz
            f["size_kb"] = round(sz / 1024, 1)
            f["line_count"] = line_count
            all_files_flat.append(f)

    # Table Header
    index_table = doc.add_table(rows=len(all_files_flat) + 2, cols=6)
    index_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    index_table.autofit = False

    headers = ["#", "Category", "File Path", "Language", "Lines", "Size (KB)"]
    widths = [Inches(0.4), Inches(1.8), Inches(2.2), Inches(1.2), Inches(0.7), Inches(0.7)]

    # Style header row
    hdr_row = index_table.rows[0]
    for c_idx, title in enumerate(headers):
        cell = hdr_row.cells[c_idx]
        cell.width = widths[c_idx]
        set_cell_background(cell, COLOR_NAVY)
        set_cell_padding(cell, top=80, bottom=80, left=100, right=100)
        set_cell_borders(cell, 
                         top=dict(val='single', sz=6, color=COLOR_NAVY),
                         bottom=dict(val='single', sz=6, color=COLOR_NAVY),
                         left=dict(val='single', sz=4, color="FFFFFF"),
                         right=dict(val='single', sz=4, color="FFFFFF"))
        cp = cell.paragraphs[0]
        cp.paragraph_format.space_before = Pt(0)
        cp.paragraph_format.space_after = Pt(0)
        if c_idx in [0, 4, 5]:
            cp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        else:
            cp.alignment = WD_ALIGN_PARAGRAPH.LEFT
        crun = cp.add_run(title)
        crun.font.name = "Calibri"
        crun.font.size = Pt(9)
        crun.font.bold = True
        crun.font.color.rgb = RGBColor(255, 255, 255)

    total_lines = sum(f["line_count"] for f in all_files_flat)
    total_kb = sum(f["size_kb"] for f in all_files_flat)

    # Populate rows
    for r_idx, f in enumerate(all_files_flat):
        row = index_table.rows[r_idx + 1]
        bg_col = COLOR_BG_LIGHT if r_idx % 2 == 0 else "FFFFFF"

        vals = [
            str(r_idx + 1),
            f["category_name"].split(" (")[0], # Short category
            f["name"],
            f["lang"].split(" /")[0], # Short lang
            f"{f['line_count']:,}",
            f"{f['size_kb']} KB"
        ]

        for c_idx, val in enumerate(vals):
            cell = row.cells[c_idx]
            cell.width = widths[c_idx]
            set_cell_background(cell, bg_col)
            set_cell_padding(cell, top=60, bottom=60, left=80, right=80)
            set_cell_borders(cell, 
                             top=dict(val='single', sz=2, color=COLOR_BORDER),
                             bottom=dict(val='single', sz=2, color=COLOR_BORDER),
                             left=dict(val='none'),
                             right=dict(val='none'))
            cp = cell.paragraphs[0]
            cp.paragraph_format.space_before = Pt(0)
            cp.paragraph_format.space_after = Pt(0)
            if c_idx in [0, 4, 5]:
                cp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
            else:
                cp.alignment = WD_ALIGN_PARAGRAPH.LEFT
            crun = cp.add_run(val)
            crun.font.name = "Calibri"
            crun.font.size = Pt(8.5)
            if c_idx == 2:
                crun.font.bold = True
                crun.font.color.rgb = RGBColor(30, 58, 138)
            else:
                crun.font.color.rgb = RGBColor(15, 23, 42)

    # Summary Totals Row
    tot_row = index_table.rows[-1]
    tot_vals = ["", "TOTALS", f"33 Project Files", "Full Suite", f"{total_lines:,}", f"{total_kb:.1f} KB"]
    for c_idx, val in enumerate(tot_vals):
        cell = tot_row.cells[c_idx]
        cell.width = widths[c_idx]
        set_cell_background(cell, COLOR_BG_ALT)
        set_cell_padding(cell, top=80, bottom=80, left=80, right=80)
        set_cell_borders(cell, 
                         top=dict(val='single', sz=6, color=COLOR_NAVY),
                         bottom=dict(val='single', sz=6, color=COLOR_NAVY),
                         left=dict(val='none'),
                         right=dict(val='none'))
        cp = cell.paragraphs[0]
        cp.paragraph_format.space_before = Pt(0)
        cp.paragraph_format.space_after = Pt(0)
        if c_idx in [0, 4, 5]:
            cp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        else:
            cp.alignment = WD_ALIGN_PARAGRAPH.LEFT
        crun = cp.add_run(val)
        crun.font.name = "Calibri"
        crun.font.size = Pt(9)
        crun.font.bold = True
        crun.font.color.rgb = RGBColor(15, 41, 74)

    doc.add_page_break()

    # -------------------------------------------------------------
    # 3. CODE SECTIONS: CATEGORIES 1 THROUGH 5
    # -------------------------------------------------------------
    file_counter = 0

    for cat_idx, cat in enumerate(FILES_REGISTRY):
        cat_title = cat["category"]
        sec_num = cat["section_id"]
        files_in_cat = cat["files"]

        print(f"\nProcessing Section {sec_num}: {cat_title} ({len(files_in_cat)} files)...")

        # Category Header (Heading 1)
        h_cat = doc.add_paragraph()
        h_cat.paragraph_format.space_before = Pt(14)
        h_cat.paragraph_format.space_after = Pt(6)
        r_cat = h_cat.add_run(f"{sec_num}. {cat_title}")
        r_cat.font.name = "Calibri"
        r_cat.font.size = Pt(17)
        r_cat.font.bold = True
        r_cat.font.color.rgb = RGBColor(15, 41, 74)

        # Category Introduction Paragraph
        p_cat_intro = doc.add_paragraph()
        p_cat_intro.paragraph_format.space_before = Pt(0)
        p_cat_intro.paragraph_format.space_after = Pt(14)
        p_cat_intro.paragraph_format.line_spacing = 1.15

        if sec_num == "2":
            intro_text = (
                "This section contains the complete source code for all ten (10) user-facing HTML5 pages "
                "that constitute the presentation layer of Revati Enterprises. Each page adheres to semantic W3C standards, "
                "features responsive viewports, includes full accessibility metadata, and links seamlessly with the master "
                "design system and JavaScript client controllers."
            )
        elif sec_num == "3":
            intro_text = (
                "This section encapsulates the comprehensive styling architecture and visual design system. "
                "Styles are engineered using pure Vanilla CSS with complete custom property design tokens, supporting "
                "dark and light modes, responsive layout grids, glassmorphism surface components, dashboard widgets, "
                "and hardware-accelerated 3D intro animations."
            )
        elif sec_num == "4":
            intro_text = (
                "This section contains the complete client-side JavaScript controllers, reactive state engines, "
                "unified REST API client, Firestore database connector, proposal calculation engine, Excel exporter, "
                "3D parallax physics engine, and Progressive Web App (PWA) offline Service Worker."
            )
        elif sec_num == "5":
            intro_text = (
                "This section documents the backend server microservices and data persistence schemas. It includes "
                "the lightweight Python HTTP REST server, the standalone multi-threaded Java HTTP microservice, the "
                "Spring Boot enterprise web application controller, database seeding scripts, and local JSON document stores."
            )
        elif sec_num == "6":
            intro_text = (
                "This section provides all foundational project configuration files, including the PWA manifest, "
                "Maven POM build descriptor, Spring application properties, Vercel global CDN deployment configurations, "
                "and Git version control exclusion rules."
            )
        else:
            intro_text = "Technical specification and complete source code repository."

        r_cat_intro = p_cat_intro.add_run(intro_text)
        r_cat_intro.font.name = "Calibri"
        r_cat_intro.font.size = Pt(10)
        r_cat_intro.font.color.rgb = RGBColor(71, 85, 105)

        # Iterate through files in category
        for f_idx, f_info in enumerate(files_in_cat):
            file_counter += 1
            f_path = f_info["path"]
            f_name = f_info["name"]
            f_title = f_info["title"]
            f_lang = f_info["lang"]
            f_desc = f_info["desc"]

            print(f"  [{file_counter}/33] Processing: {f_name} ...")

            # Read source code
            if os.path.exists(f_path):
                with open(f_path, 'r', encoding='utf-8', errors='ignore') as fp:
                    code_content = fp.read()
                code_lines = code_content.splitlines()
                f_size = os.path.getsize(f_path)
            else:
                code_lines = ["// File not found on disk"]
                f_size = 0

            line_count = len(code_lines)
            size_kb = round(f_size / 1024, 1)

            # Subheading for file (Heading 2)
            p_fhead = doc.add_paragraph()
            p_fhead.paragraph_format.space_before = Pt(16)
            p_fhead.paragraph_format.space_after = Pt(4)
            r_fhead = p_fhead.add_run(f"{sec_num}.{f_idx + 1}  {f_name}")
            r_fhead.font.name = "Calibri"
            r_fhead.font.size = Pt(13)
            r_fhead.font.bold = True
            r_fhead.font.color.rgb = RGBColor(30, 58, 138)

            # Title / Sub-caption
            p_fsub = doc.add_paragraph()
            p_fsub.paragraph_format.space_before = Pt(0)
            p_fsub.paragraph_format.space_after = Pt(6)
            r_fsub = p_fsub.add_run(f"Module: {f_title}")
            r_fsub.font.name = "Calibri"
            r_fsub.font.size = Pt(10)
            r_fsub.font.bold = True
            r_fsub.font.color.rgb = RGBColor(2, 132, 199)

            # File Metadata Table
            f_table = doc.add_table(rows=4, cols=2)
            f_table.alignment = WD_TABLE_ALIGNMENT.CENTER
            f_table.autofit = False

            f_meta_rows = [
                ("Relative File Path", f_path),
                ("Language & Classification", f_lang),
                ("Metrics", f"{line_count:,} Lines of Code  |  {size_kb} KB ({f_size:,} bytes)"),
                ("Architectural Scope", f_desc)
            ]

            for r_i, (k, v) in enumerate(f_meta_rows):
                row = f_table.rows[r_i]
                c0 = row.cells[0]
                c0.width = Inches(1.8)
                set_cell_background(c0, COLOR_BG_ALT)
                set_cell_padding(c0, top=60, bottom=60, left=80, right=80)
                set_cell_borders(c0,
                                 top=dict(val='single', sz=2, color=COLOR_BORDER),
                                 bottom=dict(val='single', sz=2, color=COLOR_BORDER),
                                 left=dict(val='single', sz=2, color=COLOR_BORDER),
                                 right=dict(val='single', sz=2, color=COLOR_BORDER))
                p0 = c0.paragraphs[0]
                p0.paragraph_format.space_before = Pt(0)
                p0.paragraph_format.space_after = Pt(0)
                r0 = p0.add_run(k)
                r0.font.name = "Calibri"
                r0.font.size = Pt(8.5)
                r0.font.bold = True
                r0.font.color.rgb = RGBColor(15, 41, 74)

                c1 = row.cells[1]
                c1.width = Inches(5.2)
                set_cell_background(c1, "FFFFFF")
                set_cell_padding(c1, top=60, bottom=60, left=80, right=80)
                set_cell_borders(c1,
                                 top=dict(val='single', sz=2, color=COLOR_BORDER),
                                 bottom=dict(val='single', sz=2, color=COLOR_BORDER),
                                 left=dict(val='single', sz=2, color=COLOR_BORDER),
                                 right=dict(val='single', sz=2, color=COLOR_BORDER))
                p1 = c1.paragraphs[0]
                p1.paragraph_format.space_before = Pt(0)
                p1.paragraph_format.space_after = Pt(0)
                r1 = p1.add_run(v)
                r1.font.name = "Calibri"
                r1.font.size = Pt(8.5)
                r1.font.color.rgb = RGBColor(15, 23, 42)

            # Code Header Banner
            p_code_hdr = doc.add_paragraph()
            p_code_hdr.paragraph_format.space_before = Pt(8)
            p_code_hdr.paragraph_format.space_after = Pt(3)
            r_code_hdr = p_code_hdr.add_run(f"FULL VERBATIM SOURCE CODE — {f_name.upper()} ({line_count:,} LINES):")
            r_code_hdr.font.name = "Calibri"
            r_code_hdr.font.size = Pt(9)
            r_code_hdr.font.bold = True
            r_code_hdr.font.color.rgb = RGBColor(71, 85, 105)

            # Add source code lines
            # To ensure optimal performance and pristine pagination in Word,
            # we format each line as an indented monospace paragraph.
            for line in code_lines:
                clean_line = line.replace('\t', '    ').rstrip('\r\n')
                p_code = doc.add_paragraph()
                p_code.paragraph_format.space_before = Pt(0)
                p_code.paragraph_format.space_after = Pt(0)
                p_code.paragraph_format.line_spacing = 1.05
                p_code.paragraph_format.left_indent = Inches(0.12)

                r_code = p_code.add_run(clean_line if clean_line else " ")
                r_code.font.name = "Consolas"
                r_code.font.size = Pt(7.5)
                r_code.font.color.rgb = RGBColor(30, 41, 59)

            # Add clean spacing after each file
            p_spacer = doc.add_paragraph()
            p_spacer.paragraph_format.space_before = Pt(6)
            p_spacer.paragraph_format.space_after = Pt(6)
            r_spacer = p_spacer.add_run("━" * 60)
            r_spacer.font.name = "Calibri"
            r_spacer.font.size = Pt(9)
            r_spacer.font.color.rgb = RGBColor(226, 232, 240)

        # End of category: page break
        doc.add_page_break()

    # -------------------------------------------------------------
    # 4. SECTION 6: ARCHITECTURAL NOTE ON THIRD-PARTY VENDOR LIBRARIES
    # -------------------------------------------------------------
    print("Adding Section 7: Third-Party Libraries & Documentation Scripts...")
    h_vend = doc.add_paragraph()
    h_vend.paragraph_format.space_before = Pt(12)
    h_vend.paragraph_format.space_after = Pt(6)
    r_vend = h_vend.add_run("7. Architectural Reference: Third-Party Client Libraries & Tooling")
    r_vend.font.name = "Calibri"
    r_vend.font.size = Pt(17)
    r_vend.font.bold = True
    r_vend.font.color.rgb = RGBColor(15, 41, 74)

    p_vend_desc = doc.add_paragraph()
    p_vend_desc.paragraph_format.space_before = Pt(4)
    p_vend_desc.paragraph_format.space_after = Pt(10)
    p_vend_desc.paragraph_format.line_spacing = 1.15
    r_vend_desc = p_vend_desc.add_run(
        "To ensure complete technical disclosure, this section catalogues external client-side libraries "
        "and internal documentation build utilities utilized during project development.\n\n"
        "• js/jspdf.umd.min.js (364.5 KB, UMD Minified Distribution):\n"
        "  Client-side PDF generation engine utilized by 'js/letterhead.js' and 'estimator.html' for converting dynamic HTML "
        "  quotations and commercial proposals into downloadable vector PDF documents. Because it is a minified third-party "
        "  distribution bundle, it is linked externally and integrated through official standard APIs rather than hand-authored code.\n\n"
        "• Documentation & Academic Report Generation Scripts:\n"
        "  The repository includes auxiliary Python automation utilities ('build_academic_report.py', 'academic_framework.py', "
        "  'academic_pages_part1.py', 'academic_pages_part2.py', 'generate_pdf_report.py') used to compile multi-chapter "
        "  academic documentation and PDF reports for project reviews and university submissions."
    )
    r_vend_desc.font.name = "Calibri"
    r_vend_desc.font.size = Pt(10)
    r_vend_desc.font.color.rgb = RGBColor(15, 23, 42)

    # -------------------------------------------------------------
    # SAVE DOCUMENT
    # -------------------------------------------------------------
    output_filename = "Revati_Enterprises_Complete_Code_Documentation.docx"
    print(f"\nSaving complete Word document to '{output_filename}'...")
    doc.save(output_filename)

    elapsed = time.time() - t_start
    out_size = os.path.getsize(output_filename)
    print("=" * 80)
    print(f"SUCCESS: Document successfully created in {elapsed:.2f} seconds!")
    print(f"File Path: {os.path.abspath(output_filename)}")
    print(f"File Size: {out_size / 1024:.1f} KB ({out_size:,} bytes)")
    print(f"Total Custom Files Documented: {len(all_files_flat)}")
    print(f"Total Code Lines Documented: {total_lines:,}")
    print("=" * 80)

if __name__ == "__main__":
    build_word_document()
