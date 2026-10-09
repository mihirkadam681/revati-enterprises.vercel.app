"""
REVATI ENTERPRISES - PAGES 1 TO 18
Chapter definitions and content flowables for pages 1 to 18.
"""

from reportlab.lib import colors
from reportlab.platypus import Paragraph, Spacer, Table, TableStyle, PageBreak, HRFlowable
from build_all_35_pages import (
    GOLD, DARK_BG, NAVY, TEXT_MAIN, TEXT_MUTED, LIGHT_BG, BORDER_COLOR, SUCCESS, DANGER, WARNING,
    title_style, subtitle_style, h1_style, h2_style, body_style, body_bold, bullet_style,
    table_header_style, table_body_style, table_body_bold, callout_style, code_style,
    make_callout, make_chapter_header, styled_table, draw_cover_banner, draw_architecture_diagram,
    draw_pwa_lifecycle_diagram
)

def get_page_1():
    """Page 1: Title & Cover Page"""
    elems = []
    elems.append(draw_cover_banner())
    elems.append(Spacer(1, 10))
    elems.append(Paragraph("TECHNICAL SPECIFICATION & ENGINEERING SYSTEM MANUAL", title_style))
    elems.append(Paragraph("COMPREHENSIVE 35-PAGE ARCHITECTURAL AUDIT, REST DAEMON, STAFF PWA & SLA PLATFORM", subtitle_style))
    elems.append(HRFlowable(width="100%", thickness=1.5, color=GOLD, spaceBefore=2, spaceAfter=8))
    
    meta_data = [
        [Paragraph("<b>Document Version:</b>", table_body_bold), Paragraph("4.2.0 (Enterprise Academic Edition)", table_body_style),
         Paragraph("<b>Date of Release:</b>", table_body_bold), Paragraph("October 2026", table_body_style)],
        [Paragraph("<b>Target System:</b>", table_body_bold), Paragraph("Revati Commercial Facility Operations", table_body_style),
         Paragraph("<b>Local Server:</b>", table_body_bold), Paragraph("http://localhost:8080 (REST Daemon)", table_body_style)],
        [Paragraph("<b>Production CDN:</b>", table_body_bold), Paragraph("revati-enterprises-vercel-app.vercel.app", table_body_style),
         Paragraph("<b>Security Standard:</b>", table_body_bold), Paragraph("HMAC-SHA256 JWT & PBKDF2 / SHA-256", table_body_style)],
        [Paragraph("<b>Academic Context:</b>", table_body_bold), Paragraph("Sheth L.U.J. & Sir M.V. College of Science", table_body_style),
         Paragraph("<b>Lead Architect:</b>", table_body_bold), Paragraph("Mihir R. Kadam (Lead System Engineer)", table_body_style)],
        [Paragraph("<b>Corporate Sponsor:</b>", table_body_bold), Paragraph("Revati Enterprises Facilities Division", table_body_style),
         Paragraph("<b>Quality Audit:</b>", table_body_bold), Paragraph("ISO 9001:2015 Compliant SOP Workflows", table_body_style)]
    ]
    t = styled_table(meta_data, [95, 171, 95, 171], is_header=False)
    elems.append(t)
    elems.append(Spacer(1, 10))
    
    elems.append(make_callout(
        "<b>EXECUTIVE ABSTRACT & SYSTEM MANDATE:</b><br/>"
        "This engineering document provides an exhaustive, 35-page architectural specification for the Revati Enterprises "
        "commercial facility management and automated housekeeping ecosystem. The platform integrates a high-performance, "
        "zero-dependency Python 3.12 multi-threaded REST daemon on port 8080, an enterprise Spring Boot / Java HTTP alternate, "
        "and a dedicated Progressive Web App (PWA) client featuring tamper-proof GPS attendance geofencing, shift stopwatch "
        "state persistence, automated worker onboarding with OTP identity validation, and cloud synchronization with Google Firebase.",
        bg="#FEF3C7", border="#D4AF37"
    ))
    return elems

def get_page_2():
    """Page 2: Table of Contents & Nomenclature"""
    elems = make_chapter_header("TOC", "Directory of Technical Chapters & Nomenclature", "Exhaustive 35-Page Structural Organization & Nomenclature Reference")
    
    toc_data = [
        [Paragraph("<b>Page / Chapter</b>", table_header_style), Paragraph("<b>Title & Core Subject Domain</b>", table_header_style), Paragraph("<b>Key Sub-Sections & Architectural Deliverables</b>", table_header_style)],
        [Paragraph("<b>Page 1</b>", table_body_bold), Paragraph("Cover & System Metadata", table_body_style), Paragraph("Document Control, Executive Abstract, Institutional Affiliation", table_body_style)],
        [Paragraph("<b>Page 2</b>", table_body_bold), Paragraph("Table of Contents & Glossary", table_body_style), Paragraph("Directory Structure, Technical Acronyms, System Nomenclature", table_body_style)],
        [Paragraph("<b>Page 3</b>", table_body_bold), Paragraph("Chap 1: Executive Summary", table_body_style), Paragraph("Corporate Overview, Sheth L.U.J. College Scope, Operational Footprint", table_body_style)],
        [Paragraph("<b>Page 4</b>", table_body_bold), Paragraph("Chap 2: Problem Statement", table_body_style), Paragraph("Legacy Facility Flaws, Ghost Attendance, Manual Checklists vs Digital", table_body_style)],
        [Paragraph("<b>Page 5</b>", table_body_bold), Paragraph("Chap 3: Proposed Architecture", table_body_style), Paragraph("Hybrid Multi-Tier Topology, Offline-First Principles, Vector Diagram", table_body_style)],
        [Paragraph("<b>Page 6</b>", table_body_bold), Paragraph("Chap 4: Tech Stack Breakdown", table_body_style), Paragraph("Frontend, Python REST Daemon, Java Spring Boot, Cloud Services", table_body_style)],
        [Paragraph("<b>Page 7</b>", table_body_bold), Paragraph("Chap 5: SRS Specifications", table_body_style), Paragraph("Functional Requirements FR-01 to 10, Non-Functional Metrics NFR-01 to 06", table_body_style)],
        [Paragraph("<b>Page 8</b>", table_body_bold), Paragraph("Chap 6: Hardware & Software", table_body_style), Paragraph("Client/Server Minimum Specs, OS Compatibility, Network Constraints", table_body_style)],
        [Paragraph("<b>Page 9</b>", table_body_bold), Paragraph("Chap 7: HTML5 & DOM Hierarchy", table_body_style), Paragraph("10-Page Portal Inventory, Semantic Hierarchy, Offline Vector Icons", table_body_style)],
        [Paragraph("<b>Page 10</b>", table_body_bold), Paragraph("Chap 8: CSS3 Design System", table_body_style), Paragraph("Dark-Gold Luxury Palette, Glassmorphism, Responsive Breakpoints", table_body_style)],
        [Paragraph("<b>Page 11</b>", table_body_bold), Paragraph("Chap 9: JavaScript Architecture", table_body_style), Paragraph("Modular Controllers, Event Handling, Toast Engine, Error Recovery", table_body_style)],
        [Paragraph("<b>Page 12</b>", table_body_bold), Paragraph("Chap 10: PWA & Service Worker", table_body_style), Paragraph("sw.js v4 Caching, Network-First Strategy, Manifest, Lifecycle Diagram", table_body_style)],
        [Paragraph("<b>Page 13</b>", table_body_bold), Paragraph("Chap 11: Dedicated Staff PWA", table_body_style), Paragraph("Thumb Ergonomics, SOP Checklists, Mobile Views, ID Badges", table_body_style)],
        [Paragraph("<b>Page 14</b>", table_body_bold), Paragraph("Chap 12: Shift Stopwatch Engine", table_body_style), Paragraph("Timestamp-Delta Algorithm, localStorage Persistence, Reboot Resilience", table_body_style)],
        [Paragraph("<b>Page 15</b>", table_body_bold), Paragraph("Chap 13: GPS Biometric Attendance", table_body_style), Paragraph("Haversine Geofencing, Geo-coordinates, Shift Logging, Fraud Shield", table_body_style)],
        [Paragraph("<b>Page 16</b>", table_body_bold), Paragraph("Chap 14: Admin Governance Portal", table_body_style), Paragraph("Multi-Pane Console, Staff Rosters, SLA Inspections, Excel Export", table_body_style)],
        [Paragraph("<b>Page 17</b>", table_body_bold), Paragraph("Chap 15: Worker KYC & Onboarding", table_body_style), Paragraph("3-Step Registration Wizard, Identity Proofs, OTP Dispatch & Verify", table_body_style)],
        [Paragraph("<b>Page 18</b>", table_body_bold), Paragraph("Chap 16: Cost Estimator Engine", table_body_style), Paragraph("Commercial Pricing Formula, Shift Staffing, jsPDF Client Export", table_body_style)],
        [Paragraph("<b>Pages 19-35</b>", table_body_bold), Paragraph("Backend, ERD, APIs, Gantt & Ops", table_body_style), Paragraph("Letterhead, Python/Java Daemons, JWT, RBAC, ERD, APIs, Gantt, QA, Deploy", table_body_style)]
    ]
    t = styled_table(toc_data, [65, 175, 292])
    elems.append(t)
    elems.append(Spacer(1, 6))
    
    glossary_data = [
        [Paragraph("<b>Acronym</b>", table_header_style), Paragraph("<b>Definition</b>", table_header_style), Paragraph("<b>Acronym</b>", table_header_style), Paragraph("<b>Definition</b>", table_header_style)],
        [Paragraph("<b>REST</b>", table_body_bold), Paragraph("Representational State Transfer", table_body_style), Paragraph("<b>JWT</b>", table_body_bold), Paragraph("JSON Web Token (RFC 7519)", table_body_style)],
        [Paragraph("<b>PWA</b>", table_body_bold), Paragraph("Progressive Web Application", table_body_style), Paragraph("<b>RBAC</b>", table_body_bold), Paragraph("Role-Based Access Control", table_body_style)],
        [Paragraph("<b>SOP</b>", table_body_bold), Paragraph("Standard Operating Procedure", table_body_style), Paragraph("<b>SLA</b>", table_body_bold), Paragraph("Service Level Agreement", table_body_style)],
        [Paragraph("<b>KYC</b>", table_body_bold), Paragraph("Know Your Customer / Worker Validation", table_body_style), Paragraph("<b>OTP</b>", table_body_bold), Paragraph("One-Time Password (6-Digit Token)", table_body_style)]
    ]
    t2 = styled_table(glossary_data, [55, 211, 55, 211])
    elems.append(t2)
    return elems

def get_page_3():
    """Page 3: Chapter 1 - Executive Summary & Enterprise Background"""
    elems = make_chapter_header("1", "Executive Summary & Enterprise Background", "Corporate Profile, Institutional Deployment & Strategic System Mandate")
    
    elems.append(Paragraph("1.1 Organizational Profile & Industry Standing", h2_style))
    elems.append(Paragraph(
        "<b>Revati Enterprises</b> is an ISO 9001:2015 certified integrated facility management and commercial housekeeping "
        "organization operating across Mumbai, Pune, and Maharashtra. The company specializes in enterprise corporate facility maintenance, "
        "educational campus housekeeping, industrial warehouse hygiene, hospital environmental services, and high-rise facade engineering.",
        body_style
    ))
    
    elems.append(Paragraph("1.2 Academic Affiliation & Sheth L.U.J. College Case Study", h2_style))
    elems.append(Paragraph(
        "This automated management software was developed in collaboration with and for deployment at <b>Sheth L.U.J. & Sir M.V. College "
        "of Science</b> (Andheri East, Mumbai). The college's sprawling multi-wing academic infrastructure serves over 6,000 students and faculty, "
        "requiring stringent hygiene management across 45 classrooms, 14 advanced science laboratories, 3 libraries, and administrative complexes. "
        "The software serves as both an academic capstone demonstration and a live operational facility governance platform.",
        body_style
    ))
    
    scope_data = [
        [Paragraph("Operational Dimension", table_header_style), Paragraph("Manual Operations (Legacy)", table_header_style), Paragraph("Revati Automated Digital Platform", table_header_style)],
        [Paragraph("<b>Workforce Footprint</b>", table_body_bold), Paragraph("250+ Ground Attendants across 12 sites", table_body_style), Paragraph("Digitally monitored via live GPS mobile PWA", table_body_style)],
        [Paragraph("<b>Daily Cleaning SOPs</b>", table_body_bold), Paragraph("Paper physical clipboards signed daily", table_body_style), Paragraph("Real-time digital checklists with timestamp locks", table_body_style)],
        [Paragraph("<b>Attendance Auditing</b>", table_body_bold), Paragraph("Manual muster books prone to proxy marking", table_body_style), Paragraph("GPS geofenced punch with live shift stopwatch", table_body_style)],
        [Paragraph("<b>Material Requisition</b>", table_body_bold), Paragraph("Weekly paper indent notes, delayed dispatch", table_body_style), Paragraph("Real-time stock ledger with auto reorder flags", table_body_style)],
        [Paragraph("<b>SLA & Client Invoicing</b>", table_body_bold), Paragraph("5-day lag for monthly billing reconciliation", table_body_style), Paragraph("Instant invoice generation via official studio", table_body_style)]
    ]
    t = styled_table(scope_data, [110, 211, 211])
    elems.append(t)
    elems.append(Spacer(1, 6))
    
    elems.append(Paragraph("1.3 Strategic Mission & Core Objectives", h2_style))
    elems.append(Paragraph(
        "The overarching goal of the Revati Enterprises software platform is to achieve <b>100% paperless facility governance</b>. "
        "By enforcing cryptographic authentication, GPS-anchored punch verification, and automated shift stopwatch tracking, the system "
        "guarantees client transparency, maximizes workforce efficiency, and eliminates administrative billing disputes.",
        body_style
    ))
    return elems

def get_page_4():
    """Page 4: Chapter 2 - Problem Statement & Existing System Limitations"""
    elems = make_chapter_header("2", "Problem Statement & Existing System Limitations", "Critical Bottlenecks in Manual Housekeeping Governance & Quantitative Impact")
    
    elems.append(Paragraph("2.1 Critical Bottlenecks of Traditional Facility Management", h2_style))
    elems.append(Paragraph(
        "Commercial housekeeping operations historically rely on paper registers, verbal supervisory briefings, and physical punch cards. "
        "In fast-paced commercial spaces and large educational campuses like Sheth L.U.J. College, this manual model produces severe systemic failures:",
        body_style
    ))
    
    flaws = [
        "<b>Ghost Attendance & Shift Proxies:</b> Physical muster books allow workers to sign for colleagues or claim full 8-hour shifts while arriving late or departing early, inflating labor overhead by an estimated 14% to 18%.",
        "<b>Unverified Checklist Compliance:</b> Physical paper checklists clipped behind restroom doors are frequently batch-signed by workers at the end of the day without performing actual periodic sanitization passes.",
        "<b>Lost Maintenance & Escalation Tickets:</b> Facility defects (such as plumbing leaks or electrical tripping) communicated orally or via WhatsApp get misplaced, leading to delayed repairs and broken client SLAs.",
        "<b>Stock Pilferage & Chemical Wastage:</b> Lack of real-time inventory ledgering prevents management from auditing chemical consumption against square-footage cleaned, causing unmonitored material leakage."
    ]
    for fl in flaws:
        elems.append(Paragraph(fl, bullet_style))
    elems.append(Spacer(1, 4))
    
    elems.append(Paragraph("2.2 Quantitative Impact Analysis: Manual vs. Automated", h2_style))
    comparison_data = [
        [Paragraph("Performance Metric", table_header_style), Paragraph("Manual Legacy Operations", table_header_style), Paragraph("Revati Digital Ecosystem", table_header_style), Paragraph("Efficiency Variance", table_header_style)],
        [Paragraph("<b>Daily Attendance Logging</b>", table_body_bold), Paragraph("15 - 20 mins per worker queue", table_body_style), Paragraph("&lt; 3 seconds (1-tap GPS punch)", table_body_style), Paragraph("<b>+98% Time Saved</b>", table_body_style)],
        [Paragraph("<b>SOP Inspection Audit Lag</b>", table_body_bold), Paragraph("24 to 48 hours for paper collection", table_body_style), Paragraph("Instantaneous real-time feed", table_body_style), Paragraph("<b>100% Zero Latency</b>", table_body_style)],
        [Paragraph("<b>Complaint Resolution Cycle</b>", table_body_bold), Paragraph("Average 36 hours from report to fix", table_body_style), Paragraph("&lt; 4 hours prioritized SLA routing", table_body_style), Paragraph("<b>89% Faster Fix</b>", table_body_style)],
        [Paragraph("<b>Monthly Payroll Discrepancies</b>", table_body_bold), Paragraph("8.5% disputed hours per cycle", table_body_style), Paragraph("&lt; 0.2% verified timestamp ledger", table_body_style), Paragraph("<b>97% Dispute Drop</b>", table_body_style)],
        [Paragraph("<b>Chemical Consumption Drift</b>", table_body_bold), Paragraph("12% unexplained shrinkage", table_body_style), Paragraph("Strict per-shift unit deducts", table_body_style), Paragraph("<b>11.8% Stock Saved</b>", table_body_style)]
    ]
    t = styled_table(comparison_data, [115, 145, 145, 127])
    elems.append(t)
    elems.append(Spacer(1, 6))
    
    elems.append(make_callout(
        "<b>ARCHITECTURAL CONCLUSION:</b><br/>"
        "Transitioning from manual paper muster books to an automated, cryptographically secured web platform is not merely "
        "an aesthetic upgrade—it is a critical operational imperative that directly reduces operating expenses, enforces accountability, "
        "and satisfies ISO 9001:2015 quality audit mandates.",
        bg="#FEE2E2", border="#DC2626"
    ))
    return elems

def get_page_5():
    """Page 5: Chapter 3 - Proposed Architecture & Key Objectives"""
    elems = make_chapter_header("3", "Proposed System Architecture & Objectives", "Hybrid Multi-Tier Topology, Offline Fault-Tolerance & Core Principles")
    
    elems.append(Paragraph("3.1 Architectural Principles: Offline-First & Zero Framework Bloat", h2_style))
    elems.append(Paragraph(
        "The Revati Enterprises platform employs a <b>Hybrid Multi-Tier Architecture</b> designed specifically for resilient field operations. "
        "Recognizing that facility basements, mechanical rooms, and remote campuses experience intermittent cellular coverage, the system avoids "
        "fragile single-page framework dependencies and adopts an offline-capable Progressive Web App model.",
        body_style
    ))
    
    # Vector Drawing Architecture Diagram
    elems.append(draw_architecture_diagram())
    elems.append(Spacer(1, 6))
    
    elems.append(Paragraph("3.2 Core Architectural Objectives", h2_style))
    objs = [
        "<b>High Availability (99.9% Uptime):</b> Tri-level failover: Local Python REST daemon on port 8080 &rarr; Google Cloud Firestore WAN &rarr; Client-side localStorage / IndexedDB.",
        "<b>Tamper-Proof Shift Accountability:</b> Hardware-anchored GPS geofencing and persistent timestamp subtraction stopwatches prevent fraudulent time logging.",
        "<b>Zero Dependency Footprint:</b> The backend daemon runs exclusively on Python's built-in standard library without requiring third-party pip dependencies.",
        "<b>Sub-150ms Interaction Latency:</b> Zero framework virtualization overhead yields instant rendering on low-cost entry-level Android devices."
    ]
    for ob in objs:
        elems.append(Paragraph(ob, bullet_style))
    return elems

def get_page_6():
    """Page 6: Chapter 4 - Complete Technology Stack Breakdown"""
    elems = make_chapter_header("4", "Complete Technology Stack Specification", "Multi-Tier Languages, Runtime Frameworks, Database Engines & Tools")
    
    elems.append(Paragraph("4.1 Comprehensive Technology Matrix", h2_style))
    elems.append(Paragraph(
        "Every tier of the Revati Enterprises ecosystem has been selected to optimize performance, cross-platform portability, "
        "and security. Below is the complete specification breakdown across all architectural layers:",
        body_style
    ))
    
    stack_data = [
        [Paragraph("Layer", table_header_style), Paragraph("Technology / Engine", table_header_style), Paragraph("Version", table_header_style), Paragraph("Architectural Role & Justification", table_header_style)],
        [Paragraph("<b>Frontend UI</b>", table_body_bold), Paragraph("Semantic HTML5", table_body_style), Paragraph("W3C Living", table_body_style), Paragraph("Accessible semantic DOM structure with inline SVG symbols.", table_body_style)],
        [Paragraph("<b>Styling</b>", table_body_bold), Paragraph("Vanilla CSS3", table_body_style), Paragraph("CSS3 Spec", table_body_style), Paragraph("Luxury Dark-Gold theme, glassmorphism, responsive grid.", table_body_style)],
        [Paragraph("<b>Client Scripting</b>", table_body_bold), Paragraph("Modern JavaScript", table_body_style), Paragraph("ES6+ (ES2022)", table_body_style), Paragraph("Modular service layers, event bus, dynamic DOM rendering.", table_body_style)],
        [Paragraph("<b>PWA Engine</b>", table_body_bold), Paragraph("Service Worker API", table_body_style), Paragraph("sw.js v4", table_body_style), Paragraph("Network-First caching, offline asset serving, background sync.", table_body_style)],
        [Paragraph("<b>Primary Backend</b>", table_body_bold), Paragraph("Python 3 Multi-Threaded", table_body_style), Paragraph("Python 3.12", table_body_style), Paragraph("Standard library REST API on port 8080 (server.py), zero-pip dependencies.", table_body_style)],
        [Paragraph("<b>Alternate Backend</b>", table_body_bold), Paragraph("Java Spring Boot / HTTP", table_body_style), Paragraph("Java 8 / 2.7.14", table_body_style), Paragraph("Enterprise compiled REST backend with Spring Data JPA and H2 database.", table_body_style)],
        [Paragraph("<b>Local Persistence</b>", table_body_bold), Paragraph("JSON Document Store", table_body_style), Paragraph("Atomic JSON", table_body_style), Paragraph("db_store.json file with mutex lock safety and deduplication.", table_body_style)],
        [Paragraph("<b>Cloud NoSQL</b>", table_body_bold), Paragraph("Google Cloud Firestore", table_body_style), Paragraph("SDK v9.x", table_body_style), Paragraph("Distributed real-time document listeners via onSnapshot().", table_body_style)],
        [Paragraph("<b>Cloud Identity</b>", table_body_bold), Paragraph("Firebase Authentication", table_body_style), Paragraph("v9.x Web", table_body_style), Paragraph("OAuth 2.0 Google Sign-In and secure email/password credential exchange.", table_body_style)],
        [Paragraph("<b>Edge Hosting</b>", table_body_bold), Paragraph("Vercel Edge Network", table_body_style), Paragraph("Global Anycast", table_body_style), Paragraph("Automated Git CI/CD, SSL/TLS termination, HTTP/2 distribution.", table_body_style)],
        [Paragraph("<b>Client PDF / Export</b>", table_body_bold), Paragraph("jsPDF & html2pdf.js", table_body_style), Paragraph("2.5.1 / 0.10.1", table_body_style), Paragraph("Instant 0ms client-side PDF quote and letterhead generation.", table_body_style)]
    ]
    t = styled_table(stack_data, [85, 120, 65, 262])
    elems.append(t)
    elems.append(Spacer(1, 6))
    
    elems.append(Paragraph("4.2 Design Decision: Why Vanilla Web Technologies Over Heavy Frameworks?", h2_style))
    elems.append(Paragraph(
        "Modern enterprise frameworks like React or Angular introduce heavy virtual DOM runtime overhead (often &gt; 300KB bundled JS). "
        "For housekeeping staff utilizing budget smartphones over spotty 3G/4G connections, Vanilla HTML5/CSS3/ES6+ delivers "
        "near-instant initial paint (&lt; 150ms), eliminates build-chain dependency vulnerabilities, and guarantees 100% offline stability.",
        body_style
    ))
    return elems

def get_page_7():
    """Page 7: Chapter 5 - System Requirements Specification (SRS)"""
    elems = make_chapter_header("5", "System Requirements Specification (SRS)", "Functional Capabilities (FR-01 to FR-10) & Non-Functional Quality Metrics")
    
    elems.append(Paragraph("5.1 Functional Requirements Matrix (FR-01 to FR-10)", h2_style))
    fr_data = [
        [Paragraph("Req ID", table_header_style), Paragraph("Functional Capability", table_header_style), Paragraph("Inputs / Triggers", table_header_style), Paragraph("System Processing & Output State", table_header_style)],
        [Paragraph("<b>FR-01</b>", table_body_bold), Paragraph("Cryptographic Login", table_body_style), Paragraph("Username & Password", table_body_style), Paragraph("Validates credentials; issues HMAC-SHA256 JWT token.", table_body_style)],
        [Paragraph("<b>FR-02</b>", table_body_bold), Paragraph("Worker KYC Registration", table_body_style), Paragraph("Name, Phone, Aadhaar, OTP", table_body_style), Paragraph("Validates identity proof; assigns REV-WORKER code.", table_body_style)],
        [Paragraph("<b>FR-03</b>", table_body_bold), Paragraph("Live Shift Stopwatch", table_body_style), Paragraph("Punch-In Tap", table_body_style), Paragraph("Starts epoch timer in localStorage; continuous tick.", table_body_style)],
        [Paragraph("<b>FR-04</b>", table_body_bold), Paragraph("GPS Biometric Attendance", table_body_style), Paragraph("Geolocation Coords", table_body_style), Paragraph("Validates geofence; logs timestamp in db_store.json.", table_body_style)],
        [Paragraph("<b>FR-05</b>", table_body_bold), Paragraph("SOP Task Management", table_body_style), Paragraph("Task Assignment Form", table_body_style), Paragraph("Dispatches cleaning checklists to mobile staff app.", table_body_style)],
        [Paragraph("<b>FR-06</b>", table_body_bold), Paragraph("Service Defect Tickets", table_body_style), Paragraph("Complaint Lodged", table_body_style), Paragraph("Categorizes severity; alerts supervisor and admin.", table_body_style)],
        [Paragraph("<b>FR-07</b>", table_body_bold), Paragraph("Chemical Stock Tracking", table_body_style), Paragraph("Stock Deduct / Inward", table_body_style), Paragraph("Updates inventory levels; triggers reorder warnings.", table_body_style)],
        [Paragraph("<b>FR-08</b>", table_body_bold), Paragraph("Cost Estimator & Quote", table_body_style), Paragraph("Sq Ft, Shifts, Services", table_body_style), Paragraph("Executes pricing formulas; compiles downloadable PDF.", table_body_style)],
        [Paragraph("<b>FR-09</b>", table_body_bold), Paragraph("Official Letterhead Studio", table_body_style), Paragraph("Proposal WYSIWYG Form", table_body_style), Paragraph("Renders ISO letterhead; exports vector print PDF.", table_body_style)],
        [Paragraph("<b>FR-10</b>", table_body_bold), Paragraph("Admin-Only Record Guard", table_body_style), Paragraph("DELETE API Request", table_body_style), Paragraph("Enforces ADMIN JWT claim or IPS master passphrase.", table_body_style)]
    ]
    t = styled_table(fr_data, [45, 120, 110, 257])
    elems.append(t)
    elems.append(Spacer(1, 6))
    
    elems.append(Paragraph("5.2 Non-Functional Requirements & Performance SLAs (NFR-01 to NFR-06)", h2_style))
    nfr_data = [
        [Paragraph("Metric ID", table_header_style), Paragraph("Quality Attribute", table_header_style), Paragraph("Target Threshold", table_header_style), Paragraph("Verification & Enforcement Method", table_header_style)],
        [Paragraph("<b>NFR-01</b>", table_body_bold), Paragraph("API Response Latency", table_body_style), Paragraph("&lt; 150 milliseconds", table_body_style), Paragraph("Multi-threaded socketserver daemon with keep-alive.", table_body_style)],
        [Paragraph("<b>NFR-02</b>", table_body_bold), Paragraph("System Availability", table_body_style), Paragraph("99.9% Uptime", table_body_style), Paragraph("Dual-path architecture: local Python daemon + cloud CDN.", table_body_style)],
        [Paragraph("<b>NFR-03</b>", table_body_bold), Paragraph("Offline Fault Tolerance", table_body_style), Paragraph("100% Offline Core Ops", table_body_style), Paragraph("sw.js v4 caching + localStorage shift timer persistence.", table_body_style)],
        [Paragraph("<b>NFR-04</b>", table_body_bold), Paragraph("Cryptographic Security", table_body_style), Paragraph("HMAC-SHA256 & TLS 1.3", table_body_style), Paragraph("Strict 24-hr token expiry and timing-attack resistance.", table_body_style)],
        [Paragraph("<b>NFR-05</b>", table_body_bold), Paragraph("Mobile Touch Ergonomics", table_body_style), Paragraph("&gt; 48px touch targets", table_body_style), Paragraph("Thumb-zone bottom navigation bar on staff mobile PWA.", table_body_style)],
        [Paragraph("<b>NFR-06</b>", table_body_bold), Paragraph("Browser Compatibility", table_body_style), Paragraph("100% Evergreen Support", table_body_style), Paragraph("Tested on Chrome, Safari iOS, Firefox, Edge, Android.", table_body_style)]
    ]
    t2 = styled_table(nfr_data, [45, 120, 110, 257])
    elems.append(t2)
    return elems

def get_page_8():
    """Page 8: Chapter 6 - Hardware & Software Configuration Specification"""
    elems = make_chapter_header("6", "Hardware & Software Configuration Specs", "Client & Server Runtime Environments, Operating Systems & Network Limits")
    
    elems.append(Paragraph("6.1 Hardware Configuration Specifications", h2_style))
    hw_data = [
        [Paragraph("Environment", table_header_style), Paragraph("Component", table_header_style), Paragraph("Minimum Specifications", table_header_style), Paragraph("Recommended Specifications", table_header_style)],
        [Paragraph("<b>Mobile Client</b><br/>(Staff PWA)", table_body_bold), Paragraph("Processor<br/>RAM<br/>Storage<br/>Display", table_body_style), Paragraph("Quad-Core 1.5 GHz<br/>2 GB RAM<br/>100 MB free space<br/>720 x 1280 (HD)", table_body_style), Paragraph("Octa-Core 2.0 GHz+<br/>4 GB+ RAM<br/>500 MB free space<br/>1080 x 2400 (FHD+ AMOLED)", table_body_style)],
        [Paragraph("<b>Desktop Client</b><br/>(Admin Console)", table_body_bold), Paragraph("Processor<br/>RAM<br/>Display", table_body_style), Paragraph("Dual-Core 2.0 GHz Intel/AMD<br/>4 GB RAM<br/>1366 x 768 resolution", table_body_style), Paragraph("Quad-Core Intel i5 / Apple M1+<br/>8 GB+ RAM<br/>1920 x 1080 Full HD IPS", table_body_style)],
        [Paragraph("<b>Local Server</b><br/>(Python Daemon)", table_body_bold), Paragraph("Host Machine<br/>RAM<br/>Disk", table_body_style), Paragraph("Intel Celeron / Core i3<br/>2 GB RAM<br/>Solid State Drive (SSD)", table_body_style), Paragraph("Intel Core i5 / Xeon / Cloud VM<br/>8 GB RAM<br/>NVMe SSD RAID Storage", table_body_style)],
        [Paragraph("<b>Production CDN</b><br/>(Vercel Edge)", table_body_bold), Paragraph("Serverless Tier", table_body_style), Paragraph("Global Anycast Edge Nodes<br/>Automatic horizontal scale", table_body_style), Paragraph("Tier-1 CDN with automatic failover<br/>Sub-50ms regional Edge PoPs", table_body_style)]
    ]
    t = styled_table(hw_data, [95, 80, 175, 182])
    elems.append(t)
    elems.append(Spacer(1, 6))
    
    elems.append(Paragraph("6.2 Software Operating Environment & Dependencies", h2_style))
    sw_data = [
        [Paragraph("Software Component", table_header_style), Paragraph("Supported Platforms / Operating Systems", table_header_style), Paragraph("Required Runtime / Engine Version", table_header_style)],
        [Paragraph("<b>Primary Backend Daemon</b>", table_body_bold), Paragraph("Microsoft Windows 10/11, Linux (Ubuntu/Debian), macOS", table_body_style), Paragraph("Python 3.10, 3.11, or 3.12 (Standard Library)", table_body_style)],
        [Paragraph("<b>Enterprise Java Server</b>", table_body_bold), Paragraph("Cross-platform JVM runtime (Windows/Linux/Unix)", table_body_style), Paragraph("Java JDK 8 or OpenJDK 17 LTS (Maven 3.8+)", table_body_style)],
        [Paragraph("<b>Mobile Web Browsers</b>", table_body_bold), Paragraph("Android 8.0+ (Chrome, Samsung Internet), iOS 14+ (Safari)", table_body_style), Paragraph("WebKit / Chromium with ServiceWorker & Geolocation", table_body_style)],
        [Paragraph("<b>Desktop Browsers</b>", table_body_bold), Paragraph("Windows, macOS, Linux, ChromeOS", table_body_style), Paragraph("Google Chrome 90+, Mozilla Firefox 88+, MS Edge 90+", table_body_style)]
    ]
    t2 = styled_table(sw_data, [125, 205, 202])
    elems.append(t2)
    elems.append(Spacer(1, 6))
    
    elems.append(Paragraph("6.3 Network Bandwidth & Latency Constraints", h2_style))
    elems.append(Paragraph(
        "• <b>Minimum Bandwidth:</b> 64 kbps (2G Edge) for offline-queued batch data synchronization.<br/>"
        "• <b>Optimal Bandwidth:</b> 1 Mbps+ (4G LTE / Wi-Fi) for instantaneous Firestore real-time snapshot sync.<br/>"
        "• <b>Maximum Tolerable Round-Trip Time (RTT):</b> 800ms before triggering local client-side failover.",
        body_style
    ))
    return elems

def get_page_9():
    """Page 9: Chapter 7 - Frontend Architecture: Semantic HTML5 & Page Inventory"""
    elems = make_chapter_header("7", "Frontend Architecture: Semantic HTML5", "Structural Page Inventory, Semantic DOM Landmarks & Offline Vector Sprites")
    
    elems.append(Paragraph("7.1 Comprehensive Web Portal Inventory", h2_style))
    elems.append(Paragraph(
        "The Revati Enterprises frontend comprises 10 specialized HTML5 web views designed to address distinct organizational touchpoints:",
        body_style
    ))
    
    portal_data = [
        [Paragraph("HTML File", table_header_style), Paragraph("Target Audience", table_header_style), Paragraph("Core Functional Modules & Features", table_header_style), Paragraph("Lines / Size", table_header_style)],
        [Paragraph("<b>index.html</b>", table_body_bold), Paragraph("Public / Clients", table_body_style), Paragraph("Luxury brand homepage, hero showcase, service catalog, ISO credentials.", table_body_style), Paragraph("720 L / 44 KB", table_body_style)],
        [Paragraph("<b>welcome.html</b>", table_body_bold), Paragraph("New Visitors", table_body_style), Paragraph("3D particle portal, interactive luxury entrance, executive walkthrough.", table_body_style), Paragraph("540 L / 54 KB", table_body_style)],
        [Paragraph("<b>staff.html</b>", table_body_bold), Paragraph("Facility Attendants", table_body_style), Paragraph("Dedicated Staff App: non-freezing shift stopwatch, GPS punch, leave desk.", table_body_style), Paragraph("1,397 L / 64 KB", table_body_style)],
        [Paragraph("<b>admin.html</b>", table_body_bold), Paragraph("Admin / Supervisors", table_body_style), Paragraph("Master governance console, staff rosters, SLA checklists, stock ledger.", table_body_style), Paragraph("1,169 L / 73 KB", table_body_style)],
        [Paragraph("<b>register.html</b>", table_body_bold), Paragraph("Worker Candidates", table_body_style), Paragraph("3-step worker onboarding wizard, KYC document upload, OTP phone verify.", table_body_style), Paragraph("613 L / 27 KB", table_body_style)],
        [Paragraph("<b>estimator.html</b>", table_body_bold), Paragraph("Commercial Clients", table_body_style), Paragraph("Facility cost calculator, square-footage sliders, instant jsPDF export.", table_body_style), Paragraph("931 L / 60 KB", table_body_style)],
        [Paragraph("<b>letterhead.html</b>", table_body_bold), Paragraph("Corporate Executive", table_body_style), Paragraph("Official letterhead designer, proposal generator, digital seal preview.", table_body_style), Paragraph("1,136 L / 47 KB", table_body_style)],
        [Paragraph("<b>services.html</b>", table_body_bold), Paragraph("Corporate Clients", table_body_style), Paragraph("Deep-dive facility services: mechanization, HVAC, marble care, sanitization.", table_body_style), Paragraph("380 L / 14 KB", table_body_style)],
        [Paragraph("<b>about.html</b>", table_body_bold), Paragraph("Public Stakeholders", table_body_style), Paragraph("Corporate mission, Sheth L.U.J. College case study, ISO quality policy.", table_body_style), Paragraph("320 L / 12 KB", table_body_style)],
        [Paragraph("<b>contact.html</b>", table_body_bold), Paragraph("Facility Inquiries", table_body_style), Paragraph("Client booking form, emergency helpline, pan-India regional offices.", table_body_style), Paragraph("310 L / 15 KB", table_body_style)]
    ]
    t = styled_table(portal_data, [75, 95, 290, 72])
    elems.append(t)
    elems.append(Spacer(1, 6))
    
    elems.append(Paragraph("7.2 Semantic DOM Architecture & Accessibility Standards", h2_style))
    elems.append(Paragraph(
        "All views strictly adhere to modern HTML5 semantic specifications. Key structural regions utilize "
        "<code>&lt;header&gt;</code>, <code>&lt;nav&gt;</code>, <code>&lt;main&gt;</code>, <code>&lt;section&gt;</code>, "
        "<code>&lt;aside&gt;</code>, and <code>&lt;footer&gt;</code>. ARIA accessibility attributes (<code>aria-live=\"polite\"</code>, "
        "<code>role=\"alert\"</code>) guarantee complete compatibility with assistive screen readers for inclusive workforce deployment.",
        body_style
    ))
    
    elems.append(Paragraph("7.3 Offline Vector SVG Iconography: Eliminating Font-Awesome CDN Drops", h2_style))
    elems.append(Paragraph(
        "A critical engineering enhancement in <code>staff.html</code> was replacing third-party font icon webfonts (which fail and display "
        "empty boxes when the worker enters an offline basement) with <b>inline vector SVG symbol sprites</b>. These SVG paths reside directly "
        "inside the HTML markup, guaranteeing that icons for shifts, checkmarks, tasks, and clocks render with 100% fidelity even with zero internet.",
        body_style
    ))
    return elems

def get_page_10():
    """Page 10: Chapter 8 - Design System & CSS3 Architecture"""
    elems = make_chapter_header("8", "Design System & CSS3 Architecture", "Luxury Dark-Gold Palette, Glassmorphism & Responsive Breakpoints")
    
    elems.append(Paragraph("8.1 The Luxury Dark-Gold Visual Identity", h2_style))
    elems.append(Paragraph(
        "The visual identity of Revati Enterprises departs from standard utilitarian gray dashboards by adopting a <b>Luxury Dark-Gold</b> "
        "design aesthetic. This choice establishes executive trust with commercial corporate clients while maintaining high-contrast clarity "
        "for field housekeeping personnel in varying indoor and outdoor light conditions.",
        body_style
    ))
    
    palette_data = [
        [Paragraph("Token Name", table_header_style), Paragraph("Hex Value", table_header_style), Paragraph("RGB / HSL", table_header_style), Paragraph("Usage & Psychological Domain", table_header_style)],
        [Paragraph("<b>--bg-main</b>", table_body_bold), Paragraph("#07090E", table_body_style), Paragraph("rgb(7, 9, 14)", table_body_style), Paragraph("Deep obsidian canvas; reduces battery drain on OLED screens.", table_body_style)],
        [Paragraph("<b>--gold-primary</b>", table_body_bold), Paragraph("#D4AF37", table_body_style), Paragraph("rgb(212, 175, 55)", table_body_style), Paragraph("Imperial metallic gold; brand headers, buttons, active focus states.", table_body_style)],
        [Paragraph("<b>--gold-light</b>", table_body_bold), Paragraph("#F3E5AB", table_body_style), Paragraph("rgb(243, 229, 171)", table_body_style), Paragraph("Soft champagne accent; secondary highlights and pill badges.", table_body_style)],
        [Paragraph("<b>--navy-accent</b>", table_body_bold), Paragraph("#1E3A8A", table_body_style), Paragraph("rgb(30, 58, 138)", table_body_style), Paragraph("Corporate navy; information alerts, table headers, portal badges.", table_body_style)],
        [Paragraph("<b>--success</b>", table_body_bold), Paragraph("#10B981", table_body_style), Paragraph("rgb(16, 185, 129)", table_body_style), Paragraph("Emerald green; active punch-in state, verified tasks, approved leaves.", table_body_style)],
        [Paragraph("<b>--danger</b>", table_body_bold), Paragraph("#EF4444", table_body_style), Paragraph("rgb(239, 68, 68)", table_body_style), Paragraph("Vibrant crimson; punch-out action, critical tickets, record deletion.", table_body_style)]
    ]
    t = styled_table(palette_data, [95, 75, 95, 267])
    elems.append(t)
    elems.append(Spacer(1, 6))
    
    elems.append(Paragraph("8.2 Glassmorphism & Translucent Layering Architecture", h2_style))
    elems.append(Paragraph(
        "To achieve visual depth, UI cards utilize CSS glassmorphism: <code>background: rgba(17, 24, 39, 0.95)</code> paired with "
        "<code>backdrop-filter: blur(16px)</code> and a subtle border stroke: <code>border: 1px solid rgba(212, 175, 55, 0.25)</code>. "
        "Ambient blurred 3D background orbs create dynamic light play as users scroll without impacting GPU frame rendering.",
        body_style
    ))
    
    elems.append(Paragraph("8.3 Responsive Grid & 5-Breakpoint Layout System", h2_style))
    bp_data = [
        [Paragraph("Breakpoint Token", table_header_style), Paragraph("Media Query Rule", table_header_style), Paragraph("Target Device Category & Layout Adaptation", table_header_style)],
        [Paragraph("<b>Mobile XS</b>", table_body_bold), Paragraph("max-width: 420px", table_body_style), Paragraph("Ultra-compact Android phones; single column, bottom sticky bar.", table_body_style)],
        [Paragraph("<b>Mobile Standard</b>", table_body_bold), Paragraph("max-width: 768px", table_body_style), Paragraph("Standard smartphones; touch-friendly 54px buttons, hidden sidebars.", table_body_style)],
        [Paragraph("<b>Tablet Portrait</b>", table_body_bold), Paragraph("max-width: 1024px", table_body_style), Paragraph("iPads & supervisory tablets; 2-column KPI grid, collapsible drawer.", table_body_style)],
        [Paragraph("<b>Desktop / Laptop</b>", table_body_bold), Paragraph("min-width: 1025px", table_body_style), Paragraph("Administrative consoles; persistent left sidebar, multi-pane tables.", table_body_style)],
        [Paragraph("<b>4K High-Res</b>", table_body_bold), Paragraph("min-width: 1920px", table_body_style), Paragraph("Command centers; centered max-width 1600px canvas with high-DPI scaling.", table_body_style)]
    ]
    t2 = styled_table(bp_data, [105, 115, 312])
    elems.append(t2)
    return elems

def get_page_11():
    """Page 11: Chapter 9 - Client-Side JavaScript Architecture & Controller Patterns"""
    elems = make_chapter_header("9", "Client-Side JavaScript Architecture", "Modular Service Abstraction, Event Engine & DOM Virtualization")
    
    elems.append(Paragraph("9.1 Modular Service Architecture (app.js & api.js)", h2_style))
    elems.append(Paragraph(
        "The client-side logic is structured into clean, decoupled ES6 classes that isolate UI interaction from network synchronization:",
        body_style
    ))
    
    js_modules = [
        "<b>ApiService Class (<code>js/api.js</code>):</b> Central networking gateway. Encapsulates all REST calls to <code>http://localhost:8080/api</code>, injects JWT Bearer headers, intercepts 401 Unauthorized responses to trigger re-authentication, and coordinates transparent failover to Firebase Cloud or local mock stores.",
        "<b>AppController (<code>js/app.js</code>):</b> Master DOM coordinator. Listens for user interactions, updates UI stat counters, renders modal dialogs, coordinates Excel table exports, and broadcasts system notifications.",
        "<b>Toast Notification Engine:</b> Dynamic overlay system rendering high-contrast feedback pills with animated progress bars and distinct success/error sound frequencies."
    ]
    for jm in js_modules:
        elems.append(Paragraph(jm, bullet_style))
    elems.append(Spacer(1, 4))
    
    elems.append(Paragraph("9.2 Client-Side Event Lifecycle & State Management", h2_style))
    lifecycle_data = [
        [Paragraph("Stage / Event", table_header_style), Paragraph("Responsible Component", table_header_style), Paragraph("Action Performed & State Transition", table_header_style)],
        [Paragraph("<b>1. DOMContentLoaded</b>", table_body_bold), Paragraph("app.js / staff.html", table_body_style), Paragraph("Reads session tokens; checks localStorage for active shift; initializes live clocks.", table_body_style)],
        [Paragraph("<b>2. Token Verification</b>", table_body_bold), Paragraph("ApiService.verifyToken()", table_body_style), Paragraph("Sends Bearer token to /api/auth/verify; populates user role permissions.", table_body_style)],
        [Paragraph("<b>3. Data Hydration</b>", table_body_bold), Paragraph("ApiService.fetchEmployees()", table_body_style), Paragraph("Executes parallel GET requests; populates administrative table rows.", table_body_style)],
        [Paragraph("<b>4. User Action Event</b>", table_body_bold), Paragraph("UI Event Listeners", table_body_style), Paragraph("Dispatches optimistic DOM updates; fires async POST/PUT to backend.", table_body_style)],
        [Paragraph("<b>5. Network Recovery</b>", table_body_bold), Paragraph("window.ononline", table_body_style), Paragraph("Detects internet restoration; flushes pending offline queue to server.", table_body_style)]
    ]
    t = styled_table(lifecycle_data, [105, 125, 302])
    elems.append(t)
    elems.append(Spacer(1, 6))
    
    elems.append(Paragraph("9.3 Client-Side Form Validation & Error Handling", h2_style))
    elems.append(Paragraph(
        "All forms (employee creation, task assignment, leave applications) execute rigorous client-side regex validation "
        "(e.g., Indian phone numbers: <code>/^[6-9]\\d{9}$/</code>, Aadhaar numbers: <code>/^\\d{12}$/</code>) before hitting the network. "
        "Sanitized inputs prevent malicious script injections and reduce unnecessary server compute cycles.",
        body_style
    ))
    return elems

def get_page_12():
    """Page 12: Chapter 10 - Progressive Web App (PWA) & Service Worker Architecture"""
    elems = make_chapter_header("10", "Progressive Web App (PWA) Architecture", "Service Worker Lifecycle (sw.js v4), Caching Strategies & Web Manifest")
    
    elems.append(Paragraph("10.1 PWA Foundation & Web App Manifest Configuration", h2_style))
    elems.append(Paragraph(
        "The Revati Enterprises platform functions as a full-featured <b>Progressive Web App (PWA)</b>. "
        "Through <code>manifest.json</code>, the web app can be installed natively onto Android and iOS home screens, "
        "running in standalone fullscreen mode without URL address bars, providing a native app experience without app-store installation overhead.",
        body_style
    ))
    
    # Vector PWA Lifecycle Diagram
    elems.append(draw_pwa_lifecycle_diagram())
    elems.append(Spacer(1, 6))
    
    elems.append(Paragraph("10.2 Service Worker Caching Pipeline: Network-First with Cache Fallback", h2_style))
    elems.append(Paragraph(
        "The Service Worker (<code>sw.js</code> v4) operates under a strict <b>Network-First Strategy</b> for API endpoints and a <b>Stale-While-Revalidate</b> "
        "strategy for static assets. When a device requests data, the worker attempts to fetch fresh data from the server; if the network times out or drops, "
        "it immediately returns the cached snapshot stored under the <code>revati-app-v4</code> cache key.",
        body_style
    ))
    
    elems.append(Paragraph("10.3 Cache Invalidation & Automatic Version Upgrades", h2_style))
    elems.append(Paragraph(
        "During the <code>activate</code> lifecycle event, the service worker compares existing browser caches against the current version string. "
        "Any obsolete cache stores (such as <code>revati-app-v1</code>, <code>v2</code>, or <code>v3</code>) are automatically deleted via "
        "<code>caches.delete()</code>, preventing stale code accumulation and ensuring workers always run the latest security patches.",
        body_style
    ))
    return elems

def get_page_13():
    """Page 13: Chapter 11 - Dedicated Staff Mobile PWA (staff.html)"""
    elems = make_chapter_header("11", "Dedicated Staff Mobile PWA (staff.html)", "Field Attendant UX, Thumb Ergonomics, SOP Checklists & Digital ID Badges")
    
    elems.append(Paragraph("11.1 Mobile-First Thumb Ergonomics for Field Personnel", h2_style))
    elems.append(Paragraph(
        "The dedicated staff mobile app (<code>staff.html</code>) was built specifically for ground attendants, janitors, and technicians. "
        "Field workers frequently operate one-handed while carrying cleaning equipment; therefore, all essential navigation controls are consolidated "
        "into a fixed bottom navigation bar (height: 68px) with oversized touch targets (&gt; 52px).",
        body_style
    ))
    
    panes_data = [
        [Paragraph("Staff App View", table_header_style), Paragraph("Key Functional Components", table_header_style), Paragraph("Worker Action & Operational Benefit", table_header_style)],
        [Paragraph("<b>Punch Clock</b>", table_body_bold), Paragraph("Live Non-Freezing Clock<br/>Biometric GPS Punch Button<br/>Shift Stopwatch Display", table_body_style), Paragraph("1-tap punch in/out with instant GPS geotagging. Displays active elapsed shift hours with real-time seconds ticker.", table_body_style)],
        [Paragraph("<b>My Tasks</b>", table_body_bold), Paragraph("Interactive SOP Checklists<br/>Status Badges (Pending/Done)<br/>Inspection Sign-off", table_body_style), Paragraph("Displays daily cleaning schedules for assigned campus wings. Attendants tap checkmarks upon completing restroom, lab, or hallway sanitization.", table_body_style)],
        [Paragraph("<b>Leave Desk</b>", table_body_bold), Paragraph("Leave Application Form<br/>Casual/Sick/Paid Types<br/>Approval Status Tracker", table_body_style), Paragraph("Workers apply for time off directly from their phone with emergency contact notes, eliminating lost paper leave slips.", table_body_style)],
        [Paragraph("<b>Digital Staff ID</b>", table_body_bold), Paragraph("Photo Badge Preview<br/>REV-WORKER Code Barcode<br/>Blood Group & Contact", table_body_style), Paragraph("Serves as official campus identification for security guard gate checkpoints at Sheth L.U.J. College.", table_body_style)]
    ]
    t = styled_table(panes_data, [95, 140, 297])
    elems.append(t)
    elems.append(Spacer(1, 6))
    
    elems.append(Paragraph("11.2 High-Contrast Sunlight Visibility & Audio Haptics", h2_style))
    elems.append(Paragraph(
        "To ensure legibility under harsh outdoor sunlight during exterior campus cleaning, <code>staff.html</code> uses ultra-high contrast "
        "text tokens (<code>#F9FAFB</code> white text on <code>#07090E</code> deep dark background with <code>#D4AF37</code> gold borders). "
        "Upon successfully clocking in or marking a task complete, the app triggers a pleasant dual-tone audio chime and device vibration haptic.",
        body_style
    ))
    return elems

def get_page_14():
    """Page 14: Chapter 12 - Live Non-Freezing Clock & Shift Stopwatch Persistence Algorithm"""
    elems = make_chapter_header("12", "Shift Stopwatch Persistence Algorithm", "Solving Mobile OS Timer Throttling via Epoch Timestamp Subtraction")
    
    elems.append(Paragraph("12.1 The Technical Problem: Mobile Battery-Saver Throttling", h2_style))
    elems.append(Paragraph(
        "On mobile operating systems (Android Chrome and iOS Safari), background tabs and locked screens heavily throttle or completely "
        "freeze standard JavaScript timers (<code>setInterval</code> and <code>setTimeout</code>). Traditional incrementing stopwatches "
        "(e.g., <code>seconds++</code> every 1000ms) fall drastically behind or reset to zero when the worker puts their phone in their pocket, "
        "causing disputed labor hours and payroll errors.",
        body_style
    ))
    
    elems.append(Paragraph("12.2 The Architectural Solution: Epoch-Timestamp Subtraction", h2_style))
    elems.append(Paragraph(
        "To guarantee 100% precision regardless of device sleep or browser tab freezing, the Revati platform implements a "
        "<b>Mathematical Timestamp Subtraction Engine</b>. When a worker punches in, the exact current Unix epoch timestamp is committed "
        "to persistent storage:",
        body_style
    ))
    
    code_text = (
        "// 1. PUNCH-IN: Record Absolute Start Epoch in localStorage\n"
        "const shiftState = {\n"
        "  isPunchedIn: true,\n"
        "  startTimestamp: Date.now(), // e.g. 1775892000000\n"
        "  inTime: new Date().toLocaleTimeString('en-US', { hour: '2-digit', minute: '2-digit' }),\n"
        "  date: new Date().toISOString().split('T')[0]\n"
        "};\n"
        "localStorage.setItem('revati_staff_active_shift_v1', JSON.stringify(shiftState));\n\n"
        "// 2. TICKER ENGINE: Calculate Elapsed Seconds Directly from Wall-Clock Time\n"
        "function updateShiftStopwatch() {\n"
        "  const state = JSON.parse(localStorage.getItem('revati_staff_active_shift_v1'));\n"
        "  if (!state || !state.isPunchedIn) return;\n"
        "  const elapsedSeconds = Math.max(0, Math.floor((Date.now() - state.startTimestamp) / 1000));\n"
        "  const hrs = String(Math.floor(elapsedSeconds / 3600)).padStart(2, '0');\n"
        "  const mins = String(Math.floor((elapsedSeconds % 3600) / 60)).padStart(2, '0');\n"
        "  const secs = String(elapsedSeconds % 60).padStart(2, '0');\n"
        "  stopwatchDisplay.textContent = `${hrs}:${mins}:${secs}`;\n"
        "}"
    )
    elems.append(Paragraph(code_text.replace("\n", "<br/>").replace(" ", "&nbsp;"), code_style))
    elems.append(Spacer(1, 6))
    
    elems.append(Paragraph("12.3 Reboot, Crash & Battery-Drain Resilience", h2_style))
    elems.append(Paragraph(
        "Because elapsed time is derived directly from <code>Date.now() - startTimestamp</code> rather than an incremental counter, "
        "the worker can close the browser, reboot their smartphone, or let their battery drain to 0%; the instant the page reloads, "
        "the stopwatch reads the exact correct shift duration down to the exact second.",
        body_style
    ))
    return elems

def get_page_15():
    """Page 15: Chapter 13 - Biometric Attendance & GPS Geofencing Mechanism"""
    elems = make_chapter_header("13", "Biometric Attendance & GPS Geofencing", "HTML5 Geolocation Integration, Haversine Radius Validation & Fraud Defense")
    
    elems.append(Paragraph("13.1 HTML5 Geolocation API Integration", h2_style))
    elems.append(Paragraph(
        "To eradicate proxy attendance and ensure personnel are physically on-site before clocking in, <code>staff.html</code> queries "
        "the W3C Geolocation API (<code>navigator.geolocation.getCurrentPosition</code>) with high-accuracy mode enabled:",
        body_style
    ))
    
    elems.append(Paragraph("13.2 Mathematical Geofencing: The Haversine Distance Formula", h2_style))
    elems.append(Paragraph(
        "The system evaluates the straight-line spherical distance between the device's coordinates and the campus anchor point "
        "(e.g., Sheth L.U.J. College coordinates: Lat 19.1176° N, Lon 72.8631° E) using the <b>Haversine Formula</b>:",
        body_style
    ))
    
    math_text = (
        "d = 2 * R * arcsin( sqrt( sin²(Δlat/2) + cos(lat1) * cos(lat2) * sin²(Δlon/2) ) )\n"
        "Where R = 6,371 km (Earth's radius), Δlat = lat2 - lat1, Δlon = lon2 - lon1.\n"
        "Tolerance Radius: Threshold = 250 meters. If d &le; 250m &rarr; Punch Permitted."
    )
    elems.append(Paragraph(math_text.replace("\n", "<br/>").replace(" ", "&nbsp;"), code_style))
    elems.append(Spacer(1, 6))
    
    geo_data = [
        [Paragraph("Data Field", table_header_style), Paragraph("Data Type", table_header_style), Paragraph("Example Payload Value", table_header_style), Paragraph("Business Integrity Function", table_header_style)],
        [Paragraph("<b>empCode</b>", table_body_bold), Paragraph("VARCHAR(20)", table_body_style), Paragraph("\"REV-WORKER004\"", table_body_style), Paragraph("Foreign key linking attendance to verified employee profile.", table_body_style)],
        [Paragraph("<b>date</b>", table_body_bold), Paragraph("DATE", table_body_style), Paragraph("\"2026-10-10\"", table_body_style), Paragraph("Calendar shift partition for payroll calculation.", table_body_style)],
        [Paragraph("<b>timeIn</b>", table_body_bold), Paragraph("TIME / STRING", table_body_style), Paragraph("\"07:58 AM\"", table_body_style), Paragraph("Initial shift commencement time.", table_body_style)],
        [Paragraph("<b>timeOut</b>", table_body_bold), Paragraph("TIME / STRING", table_body_style), Paragraph("\"Active Shift\" / \"04:30 PM\"", table_body_style), Paragraph("Shift conclusion time; locked upon final punch-out.", table_body_style)],
        [Paragraph("<b>location</b>", table_body_bold), Paragraph("VARCHAR(100)", table_body_style), Paragraph("\"Sheth LUJ College - Science Wing\"", table_body_style), Paragraph("Resolved client facility site name.", table_body_style)],
        [Paragraph("<b>gpsCoords</b>", table_body_bold), Paragraph("VARCHAR(50)", table_body_style), Paragraph("\"19.11762, 72.86314\"", table_body_style), Paragraph("Exact latitude and longitude logged for audit trails.", table_body_style)]
    ]
    t = styled_table(geo_data, [85, 75, 145, 227])
    elems.append(t)
    elems.append(Spacer(1, 6))
    
    elems.append(Paragraph("13.3 Anti-Fraud & Mock Location Defense", h2_style))
    elems.append(Paragraph(
        "To defeat GPS spoofing apps, the client validates <code>position.coords.accuracy</code>. If accuracy exceeds 100 meters "
        "or if mock-location flags are detected, the system logs an audit warning and requires manual supervisor verification.",
        body_style
    ))
    return elems

def get_page_16():
    """Page 16: Chapter 14 - Master Administrative Operations Portal (admin.html)"""
    elems = make_chapter_header("14", "Admin Governance Portal (admin.html)", "Multi-Pane Executive Console, Live KPI Stat Counters & Roster Controls")
    
    elems.append(Paragraph("14.1 Multi-Pane Governance Console Layout", h2_style))
    elems.append(Paragraph(
        "The Administrative Operations Portal (<code>admin.html</code>) serves as the centralized command center for corporate management. "
        "It features a responsive sidebar navigation menu, executive stat cards, dynamic data tables, and modal dialogs for full CRUD lifecycle control.",
        body_style
    ))
    
    admin_views = [
        [Paragraph("Navigation Pane", table_header_style), Paragraph("Target Entity Managed", table_header_style), Paragraph("Key Authorizations & Management Operations", table_header_style)],
        [Paragraph("<b>Dashboard</b>", table_body_bold), Paragraph("High-level System KPIs", table_body_style), Paragraph("Live count of on-duty staff, active shift percentage, pending complaints, low-stock warnings.", table_body_style)],
        [Paragraph("<b>Employee Roster</b>", table_body_bold), Paragraph("DB_EMPLOYEES", table_body_style), Paragraph("View worker records, assign shifts, update designations, evaluate efficiency scores (90-99%).", table_body_style)],
        [Paragraph("<b>Attendance Ledger</b>", table_body_bold), Paragraph("DB_ATTENDANCE", table_body_style), Paragraph("Real-time log of daily punches, time-in, time-out, GPS site tags, and completed shift hours.", table_body_style)],
        [Paragraph("<b>Quality SLA Tasks</b>", table_body_bold), Paragraph("DB_TASKS", table_body_style), Paragraph("Assign daily campus cleaning routines; inspect completed tasks; mark verified or re-work.", table_body_style)],
        [Paragraph("<b>Service Tickets</b>", table_body_bold), Paragraph("DB_COMPLAINTS", table_body_style), Paragraph("Log customer defect reports; categorize severity (High/Med/Low); dispatch maintenance techs.", table_body_style)],
        [Paragraph("<b>Chemical Inventory</b>", table_body_bold), Paragraph("DB_INVENTORY", table_body_style), Paragraph("Monitor floor sanitizers, microfiber pads, mop heads; trigger reorder alerts at threshold.", table_body_style)],
        [Paragraph("<b>Leave Desk & OTP</b>", table_body_bold), Paragraph("DB_LEAVES", table_body_style), Paragraph("Review worker leave requisitions; approve/reject with supervisor notes; view OTP logs.", table_body_style)],
        [Paragraph("<b>Client Billing</b>", table_body_bold), Paragraph("DB_REPORTS", table_body_style), Paragraph("Generate monthly service invoices, square-footage maintenance contracts, and export CSVs.", table_body_style)]
    ]
    t = styled_table(admin_views, [105, 115, 312])
    elems.append(t)
    elems.append(Spacer(1, 6))
    
    elems.append(Paragraph("14.2 One-Click Spreadsheet Export Engine (excelExporter.js)", h2_style))
    elems.append(Paragraph(
        "Administrators can instantly export any live data table (attendance ledgers, employee rosters, or chemical inventory) into "
        "standard CSV / Excel spreadsheets via <code>js/excelExporter.js</code>. This utility converts DOM tables into formatted CSV data strings "
        "and triggers immediate browser downloads without requiring server compute resources.",
        body_style
    ))
    return elems

def get_page_17():
    """Page 17: Chapter 15 - Worker Onboarding, Verification & KYC Portal (register.html)"""
    elems = make_chapter_header("15", "Worker Onboarding & KYC Portal", "3-Step Registration Wizard, Identity Proof Uploads & OTP Phone Validation")
    
    elems.append(Paragraph("15.1 3-Stage Progressive Onboarding Wizard Architecture", h2_style))
    elems.append(Paragraph(
        "To streamline the recruitment and compliance auditing of housekeeping attendants, <code>register.html</code> implements a "
        "guided 3-step progressive onboarding wizard that enforces identity verification before creating staff credentials:",
        body_style
    ))
    
    step_data = [
        [Paragraph("Wizard Step", table_header_style), Paragraph("Form Category", table_header_style), Paragraph("Required Form Attributes", table_header_style), Paragraph("Validation Rules & Security Checks", table_header_style)],
        [Paragraph("<b>Step 1</b>", table_body_bold), Paragraph("Personal & Contact", table_body_style), Paragraph("Full Legal Name, Mobile Phone, Email, Current Address", table_body_style), Paragraph("Validates 10-digit Indian phone; checks for duplicate phone/email in system.", table_body_style)],
        [Paragraph("<b>Step 2</b>", table_body_bold), Paragraph("Identity Proof & KYC", table_body_style), Paragraph("Proof Type (Aadhaar, Voter ID, PAN), Document Number", table_body_style), Paragraph("Enforces 12-digit Aadhaar / 10-digit PAN regex; checks blacklist database.", table_body_style)],
        [Paragraph("<b>Step 3</b>", table_body_bold), Paragraph("Skills & OTP Auth", table_body_style), Paragraph("Housekeeping Experience, Specialty Skills, 6-Digit SMS OTP", table_body_style), Paragraph("Dispatches OTP via /api/auth/otp/send; validates token via /api/auth/otp/verify.", table_body_style)]
    ]
    t = styled_table(step_data, [60, 105, 160, 207])
    elems.append(t)
    elems.append(Spacer(1, 6))
    
    elems.append(Paragraph("15.2 Automated Worker Code Generation & Instant Credential Provisioning", h2_style))
    elems.append(Paragraph(
        "Upon successful OTP validation, the backend generates a sequential employee badge number: "
        "<code>REV-WORKER###</code> (e.g., <code>REV-WORKER005</code>), commits the full profile to <code>db_store.json</code>, "
        "adds a matching user record into <code>USER_DATABASE</code> with role <code>STAFF</code>, and issues an immediate 24-hour JWT token. "
        "The worker is immediately redirected to <code>staff.html</code> ready to clock in for their first shift.",
        body_style
    ))
    
    elems.append(make_callout(
        "<b>REGULATORY COMPLIANCE NOTE:</b><br/>"
        "Collecting verified Aadhaar / Voter ID proof numbers satisfies mandatory government labor contract regulations "
        "and client security clearance protocols for sensitive campus environments like Sheth L.U.J. College of Science.",
        bg="#FEF3C7", border="#D4AF37"
    ))
    return elems

def get_page_18():
    """Page 18: Chapter 16 - Commercial Facility Service Cost Estimator (estimator.html)"""
    elems = make_chapter_header("16", "Commercial Cost Estimator (estimator.html)", "Mathematical Pricing Formulation, Multi-Shift Models & jsPDF Quote Engine")
    
    elems.append(Paragraph("16.1 Mathematical Pricing Formula Engine", h2_style))
    elems.append(Paragraph(
        "The Commercial Cost Estimator (<code>estimator.html</code>) enables clients and sales executives to compute facility maintenance "
        "proposals transparently. The pricing engine calculates monthly contract charges based on square footage, property type, shift count, "
        "and mechanization tier:",
        body_style
    ))
    
    calc_text = (
        "Monthly Quote = (Base Rate + Labor Charge + Chemical Consumables + Machine Amortization) * Shift Multiplier + GST 18%\n"
        "Where:\n"
        "• Base Area Rate = Area (sq ft) * Rate/sq ft (Corporate: ₹2.20, Hospital: ₹3.10, College: ₹2.50, Industrial: ₹1.90)\n"
        "• Staffing Headcount = ceil( Area / 5,000 sq ft ) per shift\n"
        "• Supervisor Ratio = ceil( Staffing Headcount / 10 )\n"
        "• GST = Subtotal * 0.18"
    )
    elems.append(Paragraph(calc_text.replace("\n", "<br/>").replace(" ", "&nbsp;"), code_style))
    elems.append(Spacer(1, 6))
    
    quote_data = [
        [Paragraph("Property Category", table_header_style), Paragraph("Floor Area (Sq Ft)", table_header_style), Paragraph("Required Headcount", table_header_style), Paragraph("Estimated Monthly Cost (INR)", table_header_style)],
        [Paragraph("<b>Corporate Office</b>", table_body_bold), Paragraph("15,000 sq ft (1 Shift)", table_body_style), Paragraph("3 Attendants + 1 Supervisor", table_body_style), Paragraph("₹ 48,500 + GST", table_body_style)],
        [Paragraph("<b>Educational Campus</b>", table_body_bold), Paragraph("65,000 sq ft (2 Shifts)", table_body_style), Paragraph("13 Attendants + 2 Supervisors", table_body_style), Paragraph("₹ 1,85,000 + GST", table_body_style)],
        [Paragraph("<b>Multi-Specialty Hospital</b>", table_body_bold), Paragraph("40,000 sq ft (3 Shifts)", table_body_style), Paragraph("16 Attendants + 3 Supervisors", table_body_style), Paragraph("₹ 2,45,000 + GST", table_body_style)],
        [Paragraph("<b>Industrial Warehouse</b>", table_body_bold), Paragraph("120,000 sq ft (1 Shift)", table_body_style), Paragraph("12 Attendants + 2 Machine Ops", table_body_style), Paragraph("₹ 2,60,000 + GST", table_body_style)]
    ]
    t = styled_table(quote_data, [125, 115, 140, 152])
    elems.append(t)
    elems.append(Spacer(1, 6))
    
    elems.append(Paragraph("16.2 Instant 0ms Client-Side PDF Proposal Generation (jspdf.umd.min.js)", h2_style))
    elems.append(Paragraph(
        "To provide immediate proposals during client sales meetings, <code>estimator.html</code> bundles a local copy of "
        "<code>js/jspdf.umd.min.js</code>. Clicking 'Generate Official Quotation PDF' renders a branded corporate estimate complete with "
        "company letterhead, itemized cost tables, payment terms, and ISO certification seals without server latency.",
        body_style
    ))
    return elems

print("Pages 1 to 18 definitions compiled.")
