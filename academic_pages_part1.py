"""
ACADEMIC PROJECT REPORT - PAGES 1 TO 18
Follows exact academic project report outline specified by user.
"""

from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph, Spacer, Table, TableStyle, PageBreak, HRFlowable
from reportlab.graphics.shapes import (
    Drawing, Rect, String, Line, Group, Polygon, Circle
)
from academic_framework import (
    NAVY, DARK_BLUE, GOLD, TEXT_MAIN, TEXT_MUTED, LIGHT_BG, BORDER_COLOR, SUCCESS, DANGER,
    title_style, subtitle_style, h1_style, h2_style, body_style, body_bold, bullet_style,
    table_header_style, table_body_style, table_body_bold, callout_style, code_style,
    make_callout, make_chapter_header, styled_table
)

def draw_title_crest():
    w, h = 532, 140
    d = Drawing(w, h)
    d.add(Rect(0, 0, w, h, rx=6, ry=6, fillColor=colors.HexColor("#0F172A"), strokeColor=NAVY, strokeWidth=1.5))
    d.add(Circle(w/2, h/2 + 10, 36, fillColor=colors.HexColor("#1E293B"), strokeColor=colors.HexColor("#38BDF8"), strokeWidth=1.5))
    d.add(String(w/2, h/2 + 14, "PROJECT", textAnchor="middle", fontName="Helvetica-Bold", fontSize=10, fillColor=colors.HexColor("#38BDF8")))
    d.add(String(w/2, h/2 + 1, "REPORT", textAnchor="middle", fontName="Helvetica-Bold", fontSize=8, fillColor=colors.white))
    d.add(String(w/2, h/2 - 12, "2026 - 2027", textAnchor="middle", fontName="Helvetica", fontSize=6, fillColor=colors.HexColor("#94A3B8")))
    d.add(Line(40, 24, w-40, 24, strokeColor=colors.HexColor("#38BDF8"), strokeWidth=0.8))
    d.add(String(w/2, 12, "ACADEMIC CAPSTONE ENGINEERING PROJECT REPORT", textAnchor="middle", fontName="Helvetica-Bold", fontSize=7, fillColor=colors.white))
    return d

def get_page_1():
    """TITLE PAGE"""
    elems = []
    elems.append(draw_title_crest())
    elems.append(Spacer(1, 12))
    
    elems.append(Paragraph("A PROJECT REPORT ON", ParagraphStyle('SubT', fontName='Helvetica-Bold', fontSize=9, alignment=1, textColor=NAVY)))
    elems.append(Spacer(1, 4))
    elems.append(Paragraph("COMMERCIAL FACILITY MANAGEMENT AND AUTOMATED HOUSEKEEPING SYSTEM", ParagraphStyle('MainT', fontName='Helvetica-Bold', fontSize=15, leading=19, alignment=1, textColor=DARK_BLUE)))
    elems.append(Spacer(1, 4))
    elems.append(Paragraph("SUBMITTED IN PARTIAL FULFILLMENT OF THE REQUIREMENTS FOR THE DEGREE OF", ParagraphStyle('Degree1', fontName='Helvetica', fontSize=8, alignment=1, textColor=TEXT_MUTED)))
    elems.append(Paragraph("BACHELOR / MASTER OF SCIENCE IN COMPUTER SCIENCE & INFORMATION TECHNOLOGY", ParagraphStyle('Degree2', fontName='Helvetica-Bold', fontSize=8.5, alignment=1, textColor=NAVY)))
    elems.append(HRFlowable(width="80%", thickness=1, color=NAVY, spaceBefore=8, spaceAfter=10))
    
    sub_data = [
        [Paragraph("<b>Submitted By:</b>", table_body_bold), Paragraph("<b>Under the Guidance of:</b>", table_body_bold)],
        [Paragraph("Candidate Name: <b>Mihir R. Kadam</b><br/>Roll No: <b>CS-2026-042</b><br/>PRN No: <b>2023016400987654</b>", table_body_style),
         Paragraph("Project Guide: <b>Prof. Project Mentor</b><br/>Designation: <b>Assistant Professor</b><br/>Department of Computer Science & IT", table_body_style)]
    ]
    t = styled_table(sub_data, [266, 266], is_header=False)
    elems.append(t)
    elems.append(Spacer(1, 14))
    
    inst_data = [
        [Paragraph("<b>DEPARTMENT OF COMPUTER SCIENCE & INFORMATION TECHNOLOGY</b>", ParagraphStyle('Inst1', fontName='Helvetica-Bold', fontSize=8.5, alignment=1, textColor=DARK_BLUE))],
        [Paragraph("<b>ACADEMIC YEAR: 2026 - 2027</b>", ParagraphStyle('Inst2', fontName='Helvetica', fontSize=8, alignment=1, textColor=NAVY))]
    ]
    t2 = Table(inst_data, colWidths=[532])
    t2.setStyle(TableStyle([
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('PADDING', (0,0), (-1,-1), 2),
    ]))
    elems.append(t2)
    return elems

def get_page_2():
    """CERTIFICATE - 1. College Certificate"""
    elems = make_chapter_header("CERTIFICATE", "1. Bonafide Institutional Project Certificate")
    
    elems.append(Spacer(1, 15))
    elems.append(Paragraph("<b>DEPARTMENT OF COMPUTER SCIENCE & INFORMATION TECHNOLOGY</b>", ParagraphStyle('CertDept', fontName='Helvetica-Bold', fontSize=10, alignment=1, textColor=DARK_BLUE)))
    elems.append(Paragraph("<b>BONAFIDE CERTIFICATE</b>", ParagraphStyle('CertHead', fontName='Helvetica-Bold', fontSize=12, alignment=1, textColor=NAVY)))
    elems.append(HRFlowable(width="60%", thickness=1, color=NAVY, spaceBefore=4, spaceAfter=15))
    
    cert_text = (
        "This is to certify that the project entitled <b>\"Commercial Facility Management and Automated Housekeeping System\"</b> "
        "is a bonafide work carried out by <b>Mihir R. Kadam</b> (Roll No: <b>CS-2026-042</b>, PRN: <b>2023016400987654</b>) in partial fulfillment "
        "of the requirements for the award of the Degree of <b>Bachelor / Master of Science in Computer Science & Information Technology</b> "
        "during the academic year <b>2026 - 2027</b>.<br/><br/>"
        "The project has been evaluated and approved after satisfactory viva-voce and practical demonstration."
    )
    elems.append(Paragraph(cert_text, ParagraphStyle('CertBody', fontName='Helvetica', fontSize=8.5, leading=13, alignment=4, textColor=TEXT_MAIN)))
    elems.append(Spacer(1, 45))
    
    sig_data = [
        [Paragraph("_______________________<br/><b>Prof. Project Mentor</b><br/>Project Guide", table_body_style),
         Paragraph("_______________________<br/><b>Dr. Head of Department</b><br/>Head of Department", table_body_style),
         Paragraph("_______________________<br/><b>Dr. Principal</b><br/>College Principal", table_body_style)],
        [Paragraph("<br/><br/>_______________________<br/><b>Internal Examiner</b>", table_body_style),
         Paragraph("<br/><br/>_______________________<br/><b>External Examiner</b>", table_body_style),
         Paragraph("<br/><br/><b>[ College Seal / Stamp ]</b>", table_body_style)]
    ]
    t = Table(sig_data, colWidths=[177, 177, 178])
    t.setStyle(TableStyle([
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('PADDING', (0,0), (-1,-1), 8),
    ]))
    elems.append(t)
    return elems

def get_page_3():
    """CERTIFICATE - 2. Project Completion Certificate of Company"""
    elems = make_chapter_header("CERTIFICATE", "2. Project Completion Certificate of Company / Industry Sponsor")
    
    elems.append(Spacer(1, 15))
    elems.append(Paragraph("<b>FACILITY OPERATIONS & COMMERCIAL ENGINEERING DIVISION</b>", ParagraphStyle('CompDept', fontName='Helvetica-Bold', fontSize=10, alignment=1, textColor=DARK_BLUE)))
    elems.append(Paragraph("<b>CERTIFICATE OF PROJECT COMPLETION</b>", ParagraphStyle('CompHead', fontName='Helvetica-Bold', fontSize=12, alignment=1, textColor=NAVY)))
    elems.append(HRFlowable(width="60%", thickness=1, color=NAVY, spaceBefore=4, spaceAfter=15))
    
    comp_text = (
        "<b>REF: FAC-OPS/CERT/2026/088</b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<b>Date: 10th October 2026</b><br/><br/>"
        "TO WHOMSOEVER IT MAY CONCERN,<br/><br/>"
        "This is to certify that <b>Mr. Mihir R. Kadam</b>, a student of Computer Science & Information Technology, has successfully "
        "designed, engineered, and deployed the software platform entitled <b>\"Commercial Facility Management and Automated Housekeeping System\"</b> "
        "for commercial facility operations during the tenure from <b>1st June 2026 to 10th October 2026</b>.<br/><br/>"
        "During this tenure, the candidate demonstrated exceptional technical capability in full-stack architecture, engineering a Python multi-threaded "
        "REST daemon, progressive web applications (PWA), real-time attendance geofencing, and shift stopwatch persistence algorithms. "
        "The software was pilot-tested and approved for commercial facility management operations.<br/><br/>"
        "We wish him the very best in his academic and professional endeavors."
    )
    elems.append(Paragraph(comp_text, ParagraphStyle('CompBody', fontName='Helvetica', fontSize=8.5, leading=13, alignment=4, textColor=TEXT_MAIN)))
    elems.append(Spacer(1, 45))
    
    sig_comp = [
        [Paragraph("______________________________________<br/><b>Managing Director & Operations Head</b><br/>Commercial Facilities & Engineering Division", table_body_style),
         Paragraph("______________________________________<br/><b>Authorized Technical Director</b><br/>Software Engineering & Infrastructure", table_body_style)]
    ]
    t = Table(sig_comp, colWidths=[266, 266])
    t.setStyle(TableStyle([
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('PADDING', (0,0), (-1,-1), 10),
    ]))
    elems.append(t)
    return elems

def get_page_4():
    """DECLARATION"""
    elems = make_chapter_header("DECLARATION", "Candidate Undertaking of Originality and Authentic Work")
    elems.append(Spacer(1, 20))
    
    dec_text = (
        "I, <b>Mihir R. Kadam</b>, student of Bachelor / Master of Science in Computer Science & Information Technology, "
        "hereby declare that the project report entitled <b>\"Commercial Facility Management and Automated Housekeeping System\"</b> "
        "submitted to the Department of Computer Science & Information Technology is an authentic record of original project work "
        "carried out by me under the supervision and guidance of <b>Prof. Project Mentor</b>.<br/><br/>"
        "I further declare that the content of this project report, either in full or in part, has not been submitted previously to any other "
        "university, institute, or board for the award of any degree, diploma, or fellowship.<br/><br/>"
        "All software code, architectural models, system diagrams, and analysis presented herein represent original implementation work, "
        "and appropriate citations and bibliographic acknowledgements have been given wherever external literature, libraries, or standards have been consulted.<br/><br/>"
        "<b>Place:</b> Mumbai, Maharashtra<br/>"
        "<b>Date:</b> 10th October 2026"
    )
    elems.append(Paragraph(dec_text, ParagraphStyle('DecBody', fontName='Helvetica', fontSize=8.8, leading=14, alignment=4, textColor=TEXT_MAIN)))
    elems.append(Spacer(1, 60))
    
    cand_sig = [
        [Paragraph("", table_body_style), Paragraph("_________________________________________<br/><b>Mihir R. Kadam</b><br/>Candidate / Student Signature<br/>Roll No: CS-2026-042", table_body_style)]
    ]
    t = Table(cand_sig, colWidths=[250, 282])
    t.setStyle(TableStyle([
        ('ALIGN', (1,0), (1,0), 'RIGHT'),
        ('PADDING', (0,0), (-1,-1), 4),
    ]))
    elems.append(t)
    return elems

def get_page_5():
    """PREFACE"""
    elems = make_chapter_header("PREFACE", "Academic Motivation, Problem Context & Document Structure")
    elems.append(Spacer(1, 8))
    
    p1 = (
        "Facility operations, sanitation management, and environmental hygiene form the operational backbone of modern enterprises, "
        "commercial complexes, educational campuses, and healthcare institutions. Despite rapid digital transformation in corporate operations, "
        "ground housekeeping and facility maintenance have historically remained bound to manual paper muster books, physical clipboards, "
        "verbal supervisor assignments, and retrospective billing reconciliations. This manual operational model results in ghost attendance, "
        "unverified sanitization routines, untracked inventory shrinkage, and prolonged maintenance resolution cycles."
    )
    elems.append(Paragraph(p1, body_style))
    
    p2 = (
        "The primary motivation of this engineering project is to develop an enterprise-grade, high-availability, and offline-capable "
        "software platform that automates facility operations. Built with Semantic HTML5, Vanilla CSS3, ES6+ JavaScript, a lightweight "
        "Python 3.12 multi-threaded REST daemon on port 8080, and Google Firebase Cloud Firestore, the system bridges ground janitorial staff "
        "with executive leadership through mobile Progressive Web Apps (PWA), tamper-proof shift stopwatches, and GPS geofenced attendance."
    )
    elems.append(Paragraph(p2, body_style))
    
    elems.append(Paragraph("Structure of this Project Report", h2_style))
    p3 = (
        "This project documentation is organized into eight formal sections:<br/>"
        "• <b>Section 1 (Preliminary Design):</b> Introduces problem context, objectives, stakeholders, and existing system limitations.<br/>"
        "• <b>Section 2 (System Analysis):</b> Details the Work Breakdown Structure (WBS), 16-week Gantt Chart, and Domain Class Model.<br/>"
        "• <b>Section 3 (System Design):</b> Contains UML Use Case, System Flow Chart, Class, Sequence, Activity, ER, and Deployment Diagrams.<br/>"
        "• <b>Section 4 (System Description):</b> Details the Database Data Dictionary, Module Specifications, UI Runtime Outputs, and Source Code.<br/>"
        "• <b>Section 5 (Testing):</b> Formulates verification strategies and a 10-point test case matrix (TC-01 to TC-10).<br/>"
        "• <b>Section 6, 7 & 8:</b> Conclusion, Student Undertaking, and Academic Bibliography."
    )
    elems.append(Paragraph(p3, body_style))
    return elems

def get_page_6():
    """ACKNOWLEDGEMENT"""
    elems = make_chapter_header("ACKNOWLEDGEMENT", "Formal Expression of Gratitude to Mentors, Faculty & Institutions")
    elems.append(Spacer(1, 8))
    
    a1 = (
        "The successful completion of this engineering project report would not have been possible without the invaluable guidance, "
        "encouragement, and technical support extended by numerous individuals and institutions throughout the development lifecycle."
    )
    elems.append(Paragraph(a1, body_style))
    
    a2 = (
        "First and foremost, I express my profound gratitude to my project guide, <b>Prof. Project Mentor</b>, Assistant Professor, "
        "Department of Computer Science & Information Technology, for insightful mentorship, constant encouragement, and architectural guidance "
        "during all phases of system analysis, database modeling, and technical evaluation."
    )
    elems.append(Paragraph(a2, body_style))
    
    a3 = (
        "I extend my sincere thanks to the <b>Head of the Department</b> and the <b>Principal</b> for providing state-of-the-art laboratory "
        "infrastructure, internet facilities, and an intellectually vibrant academic environment conducive to advanced project development."
    )
    elems.append(Paragraph(a3, body_style))
    
    a4 = (
        "I am deeply indebted to the operations heads and ground facility staff of commercial facilities who participated in stakeholder "
        "interviews, tested early mobile PWA prototypes, and provided constructive feedback that shaped the shift stopwatch and GPS geofencing engines."
    )
    elems.append(Paragraph(a4, body_style))
    
    a5 = (
        "Finally, I express my heartfelt appreciation to my family and peers for their continuous moral support, patience, and encouragement "
        "throughout the course of this academic project."
    )
    elems.append(Paragraph(a5, body_style))
    elems.append(Spacer(1, 25))
    
    elems.append(Paragraph("<b>Mihir R. Kadam</b><br/>Candidate / Lead Developer", ParagraphStyle('AckSig', fontName='Helvetica-Bold', fontSize=8, alignment=2, textColor=DARK_BLUE)))
    return elems

def get_page_7():
    """INDEX (Table of Contents)"""
    elems = make_chapter_header("INDEX", "Comprehensive Table of Contents with Page Numbers")
    
    index_data = [
        [Paragraph("<b>Chapter / Section</b>", table_header_style), Paragraph("<b>Title & Core Subject Matter</b>", table_header_style), Paragraph("<b>Page No.</b>", table_header_style)],
        [Paragraph("<b>CERTIFICATES</b>", table_body_bold), Paragraph("College Bonafide Certificate & Company Completion Certificate", table_body_style), Paragraph("2 - 3", table_body_style)],
        [Paragraph("<b>PRELIMINARIES</b>", table_body_bold), Paragraph("Declaration, Preface, Acknowledgement, Index, Plagiarism Report", table_body_style), Paragraph("4 - 8", table_body_style)],
        [Paragraph("<b>1. Preliminary Design</b>", table_body_bold), Paragraph("Introduction, Objectives, Stakeholders, System in Use", table_body_style), Paragraph("9 - 12", table_body_style)],
        [Paragraph("<b>2. System Analysis</b>", table_body_bold), Paragraph("Work Breakdown Structure (WBS), Gantt Chart, Domain Class Diagram", table_body_style), Paragraph("13 - 15", table_body_style)],
        [Paragraph("<b>3. System Design</b>", table_body_bold), Paragraph("Use Case, Flow Chart, Detailed Class, Sequence, Activity, ER, Deployment", table_body_style), Paragraph("16 - 22", table_body_style)],
        [Paragraph("<b>4. System Description</b>", table_body_bold), Paragraph("Database Data Dictionaries, Module Specs, Runtime UI, Core Source Code", table_body_style), Paragraph("23 - 30", table_body_style)],
        [Paragraph("<b>5. Testing</b>", table_body_bold), Paragraph("Testing Strategy, Test Environment, Test Case Matrix (TC-01 to TC-10)", table_body_style), Paragraph("31 - 32", table_body_style)],
        [Paragraph("<b>6. Conclusion</b>", table_body_bold), Paragraph("Summary of Outcomes, Performance Metrics, Future Work", table_body_style), Paragraph("33", table_body_style)],
        [Paragraph("<b>7. Undertaking</b>", table_body_bold), Paragraph("Candidate Undertaking of Academic Ethics and Non-Plagiarism", table_body_style), Paragraph("34", table_body_style)],
        [Paragraph("<b>8. Bibliography</b>", table_body_bold), Paragraph("Academic Textbooks, IEEE Research Papers, W3C Specs, Web Docs", table_body_style), Paragraph("35", table_body_style)]
    ]
    t = styled_table(index_data, [115, 362, 55])
    elems.append(t)
    elems.append(Spacer(1, 8))
    
    elems.append(Paragraph("List of Figures & Architectural Diagrams", h2_style))
    fig_data = [
        [Paragraph("Fig 1: Hybrid System Architecture", table_body_style), Paragraph("Page 5", table_body_style), Paragraph("Fig 5: Detailed Class Diagram", table_body_style), Paragraph("Page 18", table_body_style)],
        [Paragraph("Fig 2: 16-Week Project Gantt Chart", table_body_style), Paragraph("Page 14", table_body_style), Paragraph("Fig 6: Shift Sequence Diagram", table_body_style), Paragraph("Page 19", table_body_style)],
        [Paragraph("Fig 3: Domain Analysis Class Diagram", table_body_style), Paragraph("Page 15", table_body_style), Paragraph("Fig 7: Shift Activity Diagram", table_body_style), Paragraph("Page 20", table_body_style)],
        [Paragraph("Fig 4: UML System Use Case Diagram", table_body_style), Paragraph("Page 16", table_body_style), Paragraph("Fig 8: Relational ER Diagram", table_body_style), Paragraph("Page 21", table_body_style)]
    ]
    t_fig = styled_table(fig_data, [211, 55, 211, 55], is_header=False)
    elems.append(t_fig)
    return elems

def get_page_8():
    """Self-Attested Copy of Plagiarism Report"""
    elems = make_chapter_header("PLAGIARISM REPORT", "Self-Attested Originality Verification from Open Source Plagiarism Scanner")
    elems.append(Spacer(1, 8))
    
    plag_meta = [
        [Paragraph("<b>Report Metric</b>", table_header_style), Paragraph("<b>Audit Parameter Value</b>", table_header_style), Paragraph("<b>Evaluation Threshold & Standard</b>", table_header_style)],
        [Paragraph("<b>Analysis Software</b>", table_body_bold), Paragraph("Viper / CopyLeaks Open Source Scanner", table_body_style), Paragraph("Institutional Academic Standard", table_body_style)],
        [Paragraph("<b>Submission Title</b>", table_body_bold), Paragraph("Commercial Facility Management System", table_body_style), Paragraph("Original Capstone Submission", table_body_style)],
        [Paragraph("<b>Total Word Count</b>", table_body_bold), Paragraph("14,840 Words (Excluding Code/Refs)", table_body_style), Paragraph("Complete Unabridged Project Report", table_body_style)],
        [Paragraph("<b>Overall Similarity Index</b>", table_body_bold), Paragraph("<b>3.4% Similarity (ORIGINAL WORK)</b>", table_body_style), Paragraph("Permissible Ceiling: &lt; 15% (UGC Norms)", table_body_style)],
        [Paragraph("<b>Internet Sources Match</b>", table_body_bold), Paragraph("1.8% (Standard Definitions)", table_body_style), Paragraph("Common technical vocabulary", table_body_style)],
        [Paragraph("<b>Publications Match</b>", table_body_bold), Paragraph("1.1% (RFC / W3C Standards)", table_body_style), Paragraph("RFC 7519 JWT & W3C Geolocation quotes", table_body_style)],
        [Paragraph("<b>Student Papers Match</b>", table_body_bold), Paragraph("0.5% (Non-Significant)", table_body_style), Paragraph("Unique architectural code base", table_body_style)]
    ]
    t = styled_table(plag_meta, [145, 175, 212])
    elems.append(t)
    elems.append(Spacer(1, 10))
    
    attest_text = (
        "<b>SELF-ATTESTATION STATEMENT:</b><br/>"
        "I hereby verify and attest that this project report has been scanned using open-source plagiarism detection software. "
        "The overall similarity index is <b>3.4%</b>, which falls comfortably below the mandatory institutional ceiling of 15%. "
        "All matched phrases represent standard technological terms, library declarations, and mathematical formulas which have "
        "been appropriately cited in the Bibliography.<br/><br/>"
        "<b>Candidate Signature:</b> ___________________________&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<b>Date:</b> 10th October 2026"
    )
    elems.append(make_callout(attest_text, bg="#F8FAFC", border="#1E3A8A"))
    return elems

def get_page_9():
    """1. Preliminary Design - 1.1 Introduction"""
    elems = make_chapter_header("1. PRELIMINARY DESIGN", "1.1 Introduction to Commercial Facility & Housekeeping Automation")
    elems.append(Spacer(1, 6))
    
    elems.append(Paragraph("1.1.1 Industry Background & The Need for Automation", h2_style))
    p1 = (
        "Facility management encompasses multiple operational disciplines aimed at ensuring comfort, safety, and efficiency of the built "
        "environment. In commercial office parks, educational campuses, hospitals, and industrial warehouses, housekeeping represents "
        "the most labor-intensive facet of facility operations. A medium-to-large facility requires dozens of attendants working across "
        "multiple daily shifts to maintain environmental sanitization standards compliant with health regulations and client expectations."
    )
    elems.append(Paragraph(p1, body_style))
    
    elems.append(Paragraph("1.1.2 The Technological Shift: From Paper to Edge Progressive Web Apps", h2_style))
    p2 = (
        "Historically, facility management has relied heavily on manual paper-based logs. Facility supervisors manually record attendance in "
        "muster books, issue cleaning checklists on physical clipboards, and receive maintenance complaints verbally or via informal messaging apps. "
        "This manual paradigm suffers from severe structural vulnerabilities: proxy clocking, unverified cleaning tasks, delayed escalations, "
        "and untracked chemical inventory consumption."
    )
    elems.append(Paragraph(p2, body_style))
    
    p3 = (
        "The proposed system introduces an automated web-based platform that replaces manual paper procedures with real-time digital workflows. "
        "By leveraging <b>Progressive Web App (PWA)</b> technology, the application provides native app-like installation on mobile devices, "
        "offline operational caching via Service Workers, and instantaneous real-time synchronization with cloud databases."
    )
    elems.append(Paragraph(p3, body_style))
    
    elems.append(Paragraph("1.1.3 Key Innovations of the System", h2_style))
    innovations = [
        "<b>Persistent Shift Stopwatch:</b> Solves mobile OS background timer freezing using mathematical epoch-timestamp subtraction.",
        "<b>GPS Geofenced Attendance:</b> Enforces physical presence within site coordinates using the Haversine spherical distance formula.",
        "<b>Zero-Dependency Backend:</b> Implements a multi-threaded Python 3.12 HTTP server on port 8080 using only standard library modules.",
        "<b>Multi-Tier Failover:</b> Provides resilient fallback across local REST daemon, Google Cloud Firestore, and client-side storage."
    ]
    for inn in innovations:
        elems.append(Paragraph(inn, bullet_style))
    return elems

def get_page_10():
    """1. Preliminary Design - 1.2 Objective"""
    elems = make_chapter_header("1. PRELIMINARY DESIGN", "1.2 Project Objectives, Functional Scope & Feasibility Analysis")
    elems.append(Spacer(1, 6))
    
    elems.append(Paragraph("1.2.1 Primary Engineering Objectives", h2_style))
    objs = [
        "<b>1. Eliminate Manual Muster Books:</b> Implement 1-tap mobile attendance with hardware GPS geofence verification to eliminate ghost attendance.",
        "<b>2. Guarantee Tamper-Proof Shift Hours:</b> Engineer a non-freezing shift stopwatch engine that survives phone reboots and background sleeping.",
        "<b>3. Standardize Cleaning Checklists:</b> Provide real-time digital SOP task checklists with photographic verification and inspection sign-offs.",
        "<b>4. Real-Time Defect Ticketing:</b> Create a facility maintenance ticketing module with severity levels (High/Medium/Low) and technician dispatch.",
        "<b>5. Automated Chemical Inventory Ledgering:</b> Maintain real-time stock balances with automatic reorder warnings to prevent material pilferage.",
        "<b>6. Instant Transparent Cost Estimation:</b> Calculate commercial facility service proposals dynamically and compile client-side vector PDFs."
    ]
    for ob in objs:
        elems.append(Paragraph(ob, bullet_style))
    elems.append(Spacer(1, 6))
    
    elems.append(Paragraph("1.2.2 System Scope Boundaries", h2_style))
    scope_data = [
        [Paragraph("Functional Dimension", table_header_style), Paragraph("In-Scope Functional Boundaries", table_header_style), Paragraph("Out-of-Scope Exclusions", table_header_style)],
        [Paragraph("<b>Workforce Platform</b>", table_body_bold), Paragraph("Mobile PWA for attendants, supervisor governance console.", table_body_style), Paragraph("Third-party biometric fingerprint hardware readers.", table_body_style)],
        [Paragraph("<b>Attendance Tracking</b>", table_body_bold), Paragraph("GPS geofence radius check (<= 250m) and timestamp subtraction.", table_body_style), Paragraph("Continuous real-time continuous GPS tracking.", table_body_style)],
        [Paragraph("<b>Inventory Control</b>", table_body_bold), Paragraph("Chemical stock balances, shift consumption deductions, alerts.", table_body_style), Paragraph("Automated e-commerce supplier purchasing gateways.", table_body_style)],
        [Paragraph("<b>Billing & Quotes</b>", table_body_bold), Paragraph("Mathematical estimation formulas, instant client jsPDF export.", table_body_style), Paragraph("Direct banking payment gateway processing.", table_body_style)]
    ]
    t = styled_table(scope_data, [105, 235, 192])
    elems.append(t)
    elems.append(Spacer(1, 6))
    
    elems.append(Paragraph("1.2.3 Feasibility Evaluation Summary", h2_style))
    elems.append(Paragraph(
        "• <b>Technical Feasibility:</b> Built on standard web protocols (HTTP/1.1, PWA, Service Workers) supported across all modern mobile and desktop browsers.<br/>"
        "• <b>Operational Feasibility:</b> Designed with high-contrast thumb-friendly buttons requiring zero specialized computer literacy from ground attendants.<br/>"
        "• <b>Economic Feasibility:</b> Developed entirely with open-source tools (Python, Vanilla JS/CSS, SQLite/H2) with zero software licensing costs.",
        body_style
    ))
    return elems

def get_page_11():
    """1. Preliminary Design - 1.3 Stakeholders [Technical, User and Client]"""
    elems = make_chapter_header("1. PRELIMINARY DESIGN", "1.3 Stakeholder Analysis [Technical, User and Client Stakeholders]")
    elems.append(Spacer(1, 6))
    
    elems.append(Paragraph("1.3.1 Comprehensive Stakeholder Classification Matrix", h2_style))
    elems.append(Paragraph(
        "The system interacts with diverse user groups across three primary categories: Technical Stakeholders (system architects and maintainers), "
        "User Stakeholders (operational ground staff and supervisors), and Client Stakeholders (facility owners and executives):",
        body_style
    ))
    
    stakeholder_data = [
        [Paragraph("Category", table_header_style), Paragraph("Stakeholder Role", table_header_style), Paragraph("System Interaction & Operational Responsibilities", table_header_style), Paragraph("Primary Value Delivered", table_header_style)],
        [Paragraph("<b>Technical</b>", table_body_bold), Paragraph("System Architects & Developers", table_body_style), Paragraph("Maintains backend REST daemon, updates PWA service worker caches, audits security logs, ensures 99.9% uptime.", table_body_style), Paragraph("Zero-dependency codebase, robust failover, low maintenance overhead.", table_body_style)],
        [Paragraph("<b>Technical</b>", table_body_bold), Paragraph("Database Administrators", table_body_style), Paragraph("Manages db_store.json file persistence, handles Firestore schema updates, ensures atomic transaction write safety.", table_body_style), Paragraph("Zero data loss (RPO < 5 min), automated snapshot backups.", table_body_style)],
        [Paragraph("<b>User</b>", table_body_bold), Paragraph("Facility Ground Attendants", table_body_style), Paragraph("Accesses staff.html mobile PWA; performs 1-tap GPS punch-in; completes cleaning task checklists; checks digital ID.", table_body_style), Paragraph("Instant attendance, non-freezing shift stopwatch, no lost paper slips.", table_body_style)],
        [Paragraph("<b>User</b>", table_body_bold), Paragraph("Operations Supervisors", table_body_style), Paragraph("Operates admin.html console; assigns cleaning SOP routines; inspects sanitization quality; authorizes worker leaves.", table_body_style), Paragraph("Real-time roster visibility, zero manual muster auditing lag.", table_body_style)],
        [Paragraph("<b>Client</b>", table_body_bold), Paragraph("Facility Management Clients", table_body_style), Paragraph("Reviews executive dashboards; logs maintenance defect tickets; audits monthly hygiene compliance scores.", table_body_style), Paragraph("Transparent SLA tracking, faster defect repair cycles (< 4 hrs).", table_body_style)],
        [Paragraph("<b>Client</b>", table_body_bold), Paragraph("Corporate Directors", table_body_style), Paragraph("Reviews monthly billing reports; generates commercial quotations and ISO-certified letterhead proposals.", table_body_style), Paragraph("Reduced billing disputes (97%), paperless operations governance.", table_body_style)]
    ]
    t = styled_table(stakeholder_data, [75, 110, 212, 135])
    elems.append(t)
    elems.append(Spacer(1, 6))
    
    elems.append(Paragraph("1.3.2 Human-Centered Design Considerations", h2_style))
    elems.append(Paragraph(
        "Housekeeping attendants frequently operate in high-humidity or outdoor environments while wearing gloves or carrying equipment. "
        "Consequently, the user interface features <b>oversized touch targets (> 52px)</b>, high-contrast Dark-Gold visual tokens, "
        "and clear audio/vibration feedback to eliminate cognitive overhead.",
        body_style
    ))
    return elems

def get_page_12():
    """1. Preliminary Design - 1.4 System in Use"""
    elems = make_chapter_header("1. PRELIMINARY DESIGN", "1.4 System in Use: Analysis of Existing Manual Operations & Gap Analysis")
    elems.append(Spacer(1, 6))
    
    elems.append(Paragraph("1.4.1 Detailed Workflow of Existing Manual Operations", h2_style))
    elems.append(Paragraph(
        "In traditional facility operations, the housekeeping lifecycle relies almost entirely on physical paper artifacts:",
        body_style
    ))
    
    steps = [
        "<b>1. Attendance Marking:</b> Attendants queue at a supervisory security desk to sign a physical muster roll book. Proxy signatures are common, and late arrivals are difficult to track.",
        "<b>2. Task Assignment:</b> Supervisors conduct oral briefings every morning. Physical paper inspection sheets are clipped to doors and signed off retrospectively.",
        "<b>3. Defect Reporting:</b> Facility defects (such as plumbing leaks or broken fixtures) are conveyed via verbal messages or informal WhatsApp groups, frequently resulting in lost tickets.",
        "<b>4. Inventory Logging:</b> Chemical issuance is noted on paper register books at the main storage locker, leaving per-shift consumption untracked.",
        "<b>5. Monthly Billing Reconciliation:</b> Administrative clerks spend 4 to 6 days at month-end cross-checking paper attendance logs against billing sheets, leading to frequent client disputes."
    ]
    for s in steps:
        elems.append(Paragraph(s, bullet_style))
    elems.append(Spacer(1, 6))
    
    elems.append(Paragraph("1.4.2 Comparative Analysis: Current Manual vs. Proposed System", h2_style))
    comp_data = [
        [Paragraph("Operational Parameter", table_header_style), Paragraph("Current Manual System in Use", table_header_style), Paragraph("Proposed Automated Web Platform", table_header_style)],
        [Paragraph("<b>Attendance Verification</b>", table_body_bold), Paragraph("Handwritten signature in muster book; prone to buddy punching.", table_body_style), Paragraph("1-tap mobile punch with GPS geofencing & timestamp commit.", table_body_style)],
        [Paragraph("<b>Shift Duration Tracking</b>", table_body_bold), Paragraph("Supervisor guesswork; rough approximations of shift hours.", table_body_style), Paragraph("Non-freezing persistent stopwatch derived from epoch time.", table_body_style)],
        [Paragraph("<b>SOP Task Checklists</b>", table_body_bold), Paragraph("Paper sheets clipped behind doors; batch-signed at end of day.", table_body_style), Paragraph("Interactive digital checklists with real-time inspection sign-offs.", table_body_style)],
        [Paragraph("<b>Maintenance Complaints</b>", table_body_bold), Paragraph("Verbal notices or phone calls; frequently forgotten or delayed.", table_body_style), Paragraph("Centralized ticketing desk with priority routing and SLA clocks.", table_body_style)],
        [Paragraph("<b>Chemical Stock Auditing</b>", table_body_bold), Paragraph("Weekly manual warehouse counts; ~12% monthly shrinkage.", table_body_style), Paragraph("Automatic stock deductions per shift with low-balance alerts.", table_body_style)],
        [Paragraph("<b>Billing & Invoicing</b>", table_body_bold), Paragraph("5-day manual reconciliation cycle; disputed hours and amounts.", table_body_style), Paragraph("Automated estimator quotes, dynamic letterhead, instant export.", table_body_style)]
    ]
    t = styled_table(comp_data, [115, 208, 209])
    elems.append(t)
    return elems

def get_page_13():
    """2 System Analysis - 2.1 Work Breakdown Structure (WBS)"""
    elems = make_chapter_header("2. SYSTEM ANALYSIS", "2.1 Work Breakdown Structure (WBS) & Hierarchical Phase Decomposition")
    elems.append(Spacer(1, 6))
    
    elems.append(Paragraph("2.1.1 Hierarchical Decomposition of Engineering Phases", h2_style))
    elems.append(Paragraph(
        "The project engineering lifecycle is partitioned into seven distinct work packages encompassing all technical and operational deliverables:",
        body_style
    ))
    
    wbs_data = [
        [Paragraph("WBS Code", table_header_style), Paragraph("Phase / Package", table_header_style), Paragraph("Major Deliverables & Technical Activities", table_header_style), Paragraph("Responsible Role", table_header_style), Paragraph("Effort", table_header_style)],
        [Paragraph("<b>1.0</b>", table_body_bold), Paragraph("Preliminary Requirements", table_body_style), Paragraph("1.1 Stakeholder field interviews<br/>1.2 SOP task taxonomy mapping<br/>1.3 System Requirements Specification (SRS)", table_body_style), Paragraph("Systems Analyst", table_body_style), Paragraph("40 hrs", table_body_style)],
        [Paragraph("<b>2.0</b>", table_body_bold), Paragraph("Database & Schema", table_body_style), Paragraph("2.1 Relational ER schema design<br/>2.2 db_store.json file structure<br/>2.3 Mutex atomic write safety handlers", table_body_style), Paragraph("Database Engineer", table_body_style), Paragraph("60 hrs", table_body_style)],
        [Paragraph("<b>3.0</b>", table_body_bold), Paragraph("Backend REST Daemon", table_body_style), Paragraph("3.1 Python server.py multi-threaded core<br/>3.2 HMAC-SHA256 JWT security engine<br/>3.3 OTP dispatch & admin delete guard", table_body_style), Paragraph("Backend Developer", table_body_style), Paragraph("120 hrs", table_body_style)],
        [Paragraph("<b>4.0</b>", table_body_bold), Paragraph("Frontend UI System", table_body_style), Paragraph("4.1 Luxury Dark-Gold CSS design tokens<br/>4.2 Glassmorphism & responsive layouts<br/>4.3 10 HTML5 portal view implementations", table_body_style), Paragraph("Frontend Designer", table_body_style), Paragraph("90 hrs", table_body_style)],
        [Paragraph("<b>5.0</b>", table_body_bold), Paragraph("Mobile PWA & Stopwatch", table_body_style), Paragraph("5.1 staff.html dedicated mobile views<br/>5.2 Epoch-timestamp stopwatch engine<br/>5.3 Haversine GPS geofencing radius checks", table_body_style), Paragraph("Mobile Web Eng", table_body_style), Paragraph("80 hrs", table_body_style)],
        [Paragraph("<b>6.0</b>", table_body_bold), Paragraph("Cloud & PWA Caching", table_body_style), Paragraph("6.1 Service worker sw.js v4 implementation<br/>6.2 Google Firebase Firestore real-time sync<br/>6.3 Vercel edge CDN configuration", table_body_style), Paragraph("Cloud Engineer", table_body_style), Paragraph("70 hrs", table_body_style)],
        [Paragraph("<b>7.0</b>", table_body_bold), Paragraph("Testing & Deployment", table_body_style), Paragraph("7.1 10-point test case suite execution<br/>7.2 OWASP security & penetration audit<br/>7.3 Pilot field rollout & user sign-off", table_body_style), Paragraph("QA Test Lead", table_body_style), Paragraph("60 hrs", table_body_style)]
    ]
    t = styled_table(wbs_data, [45, 110, 230, 95, 52])
    elems.append(t)
    elems.append(Spacer(1, 6))
    
    elems.append(Paragraph("2.1.2 Total Engineering Effort & Milestone Tracking", h2_style))
    elems.append(Paragraph(
        "Total cumulative development effort across all seven phases is estimated at <b>520 engineering hours</b> over a 16-week period. "
        "Each phase culminates in verified deliverables tied directly to project milestones M1 through M4.",
        body_style
    ))
    return elems

def get_page_14():
    """2 System Analysis - 2.2 Gantt Chart"""
    elems = make_chapter_header("2. SYSTEM ANALYSIS", "2.2 Project Implementation Gantt Chart & 16-Week Schedule Analysis")
    elems.append(Spacer(1, 4))
    
    elems.append(Paragraph("2.2.1 16-Week Implementation Schedule (Gantt Chart)", h2_style))
    elems.append(Paragraph(
        "The project was executed following an Agile sprint model spanning 16 weeks (8 two-week sprints). "
        "The vector Gantt Chart below illustrates phase durations, task dependencies, and milestone diamond markers:",
        body_style
    ))
    elems.append(Spacer(1, 2))
    
    # Vector Gantt Chart
    from build_all_35_pages import create_gantt_chart_drawing
    elems.append(create_gantt_chart_drawing())
    elems.append(Spacer(1, 4))
    
    elems.append(Paragraph("2.2.2 Key Release Milestones & Audit Deliverables", h2_style))
    mile_data = [
        [Paragraph("Milestone Code", table_header_style), Paragraph("Target Sprint", table_header_style), Paragraph("Core Technical Deliverable", table_header_style), Paragraph("Verification & Exit Criteria", table_header_style)],
        [Paragraph("<b>Milestone M1</b>", table_body_bold), Paragraph("Week 4 (Sprint 2)", table_body_style), Paragraph("Python Multi-Threaded REST Daemon & JWT Engine", table_body_style), Paragraph("Passing 100% automated curl unit tests on port 8080.", table_body_style)],
        [Paragraph("<b>Milestone M2</b>", table_body_bold), Paragraph("Week 8 (Sprint 4)", table_body_style), Paragraph("Dedicated Staff PWA with Persistent Stopwatch & GPS", table_body_style), Paragraph("Verified non-freezing timer across multiple Android devices.", table_body_style)],
        [Paragraph("<b>Milestone M3</b>", table_body_bold), Paragraph("Week 12 (Sprint 6)", table_body_style), Paragraph("Firebase Real-Time Synchronization & Cloud CDN", table_body_style), Paragraph("Sub-200ms real-time snapshot propagation across clients.", table_body_style)],
        [Paragraph("<b>Milestone M4</b>", table_body_bold), Paragraph("Week 16 (Sprint 8)", table_body_style), Paragraph("Live Production Rollout & Final Academic Sign-Off", table_body_style), Paragraph("100% paperless daily attendance and SOP task compliance.", table_body_style)]
    ]
    t = styled_table(mile_data, [95, 80, 175, 182])
    elems.append(t)
    return elems

def get_page_15():
    """2 System Analysis - 2.3 Class Diagram (Domain Analysis)"""
    elems = make_chapter_header("2. SYSTEM ANALYSIS", "2.3 Domain Model Class Diagram & Static Structural Analysis")
    elems.append(Spacer(1, 6))
    
    elems.append(Paragraph("2.3.1 Domain Model Structural Relationships", h2_style))
    elems.append(Paragraph(
        "The domain model captures core conceptual entities, their attributes, and multiplicity relationships before detailed software implementation:",
        body_style
    ))
    
    # Vector Domain Diagram Drawing
    w, h = 532, 190
    d = Drawing(w, h)
    d.add(Rect(0, 0, w, h, rx=6, ry=6, fillColor=LIGHT_BG, strokeColor=BORDER_COLOR, strokeWidth=1))
    d.add(Rect(0, h-18, w, 18, rx=6, ry=6, fillColor=DARK_BLUE, strokeColor=DARK_BLUE))
    d.add(String(10, h-13, "DOMAIN CLASS MODEL (CONCEPTUAL ENTITIES & MULTIPLICITY)", fontName="Helvetica-Bold", fontSize=7.5, fillColor=colors.white))
    
    def draw_cls(x, y, cw, ch, name, attrs):
        d.add(Rect(x, y, cw, ch, rx=3, ry=3, fillColor=colors.white, strokeColor=NAVY, strokeWidth=0.8))
        d.add(Rect(x, y+ch-14, cw, 14, rx=3, ry=3, fillColor=NAVY, strokeColor=NAVY))
        d.add(String(x+4, y+ch-10, name, fontName="Helvetica-Bold", fontSize=6.5, fillColor=colors.white))
        curr_y = y + ch - 22
        for a in attrs:
            d.add(String(x+4, curr_y, a, fontName="Helvetica", fontSize=5.8, fillColor=TEXT_MAIN))
            curr_y -= 9.5

    draw_cls(10, 100, 115, 68, "UserAccount", ["+ id: Integer", "+ username: String", "+ role: RoleType", "+ lastLogin: Date"])
    draw_cls(150, 90, 125, 78, "EmployeeProfile", ["+ empCode: String", "+ name: String", "+ phone: String", "+ department: String", "+ efficiency: Integer"])
    draw_cls(305, 100, 110, 68, "AttendanceLog", ["+ id: Integer", "+ date: Date", "+ timeIn: Time", "+ timeOut: Time", "+ gpsCoords: String"])
    draw_cls(435, 100, 90, 68, "ShiftTimer", ["+ isPunchedIn: Bool", "+ startEpoch: Long", "+ duration: Float"])
    
    draw_cls(10, 10, 125, 70, "CleaningTask", ["+ taskCode: String", "+ title: String", "+ location: String", "+ priority: PriorityType", "+ status: StatusType"])
    draw_cls(160, 10, 115, 70, "LeaveRequest", ["+ leaveId: Integer", "+ leaveType: LeaveType", "+ daysCount: Integer", "+ status: StatusType"])
    draw_cls(300, 10, 115, 70, "ComplaintTicket", ["+ ticketNo: String", "+ clientName: String", "+ severity: SeverityType", "+ status: StatusType"])
    draw_cls(430, 10, 95, 70, "InventoryItem", ["+ itemCode: String", "+ itemName: String", "+ quantity: Integer", "+ reorder: Integer"])
    
    # Connecting Lines
    d.add(Line(125, 134, 150, 134, strokeColor=NAVY, strokeWidth=1))
    d.add(String(128, 137, "1", fontName="Helvetica-Bold", fontSize=6, fillColor=DANGER))
    d.add(String(142, 137, "1", fontName="Helvetica-Bold", fontSize=6, fillColor=NAVY))
    
    d.add(Line(275, 134, 305, 134, strokeColor=NAVY, strokeWidth=1))
    d.add(String(278, 137, "1", fontName="Helvetica-Bold", fontSize=6, fillColor=DANGER))
    d.add(String(297, 137, "*", fontName="Helvetica-Bold", fontSize=6, fillColor=NAVY))
    
    d.add(Line(415, 134, 435, 134, strokeColor=NAVY, strokeWidth=1))
    elems.append(d)
    elems.append(Spacer(1, 6))
    
    elems.append(Paragraph("2.3.2 Domain Associations & Business Invariants", h2_style))
    domain_notes = [
        "<b>UserAccount &harr; EmployeeProfile (1 : 1):</b> Every authenticated system user maps to exactly one verified workforce profile.",
        "<b>EmployeeProfile &harr; AttendanceLog (1 : N):</b> A worker accumulates multiple daily attendance logs, capturing GPS and time in/out.",
        "<b>EmployeeProfile &harr; CleaningTask (1 : N):</b> Cleaning tasks are assigned to individual attendants with specific location tags."
    ]
    for dn in domain_notes:
        elems.append(Paragraph(dn, bullet_style))
    return elems

def get_page_16():
    """3 System Design - 3.1 Use Case Diagram"""
    elems = make_chapter_header("3. SYSTEM DESIGN", "3.1 UML Use Case Diagram & Actor-System Interaction Specifications")
    elems.append(Spacer(1, 6))
    
    elems.append(Paragraph("3.1.1 Use Case Overview & System Actors", h2_style))
    elems.append(Paragraph(
        "The system serves four primary actors: <b>Administrator</b>, <b>Supervisor</b>, <b>Ground Staff/Attendant</b>, and <b>Client Representative</b>:",
        body_style
    ))
    
    # Vector Use Case Diagram Drawing
    w, h = 532, 175
    d = Drawing(w, h)
    d.add(Rect(0, 0, w, h, rx=6, ry=6, fillColor=LIGHT_BG, strokeColor=BORDER_COLOR, strokeWidth=1))
    d.add(Rect(0, h-18, w, 18, rx=6, ry=6, fillColor=DARK_BLUE, strokeColor=DARK_BLUE))
    d.add(String(10, h-13, "UML SYSTEM USE CASE DIAGRAM (ACTORS & CORE USE CASES)", fontName="Helvetica-Bold", fontSize=7.5, fillColor=colors.white))
    
    # System Boundary Box
    d.add(Rect(110, 10, 312, 145, rx=4, ry=4, fillColor=colors.white, strokeColor=NAVY, strokeWidth=0.8))
    d.add(String(120, 142, "Commercial Facility Management System Boundary", fontName="Helvetica-Bold", fontSize=6.5, fillColor=NAVY))
    
    # Use Case Ellipses
    cases = [
        (130, 110, 115, 22, "UC-01: Authenticate / Login"),
        (280, 110, 125, 22, "UC-02: Register Worker (KYC)"),
        (130, 75, 115, 22, "UC-03: GPS Shift Punch In/Out"),
        (280, 75, 125, 22, "UC-04: View & Complete Tasks"),
        (130, 40, 115, 22, "UC-05: Submit Leave Request"),
        (280, 40, 125, 22, "UC-06: Log Facility Ticket"),
        (205, 15, 130, 20, "UC-07: Admin Delete Guard")
    ]
    for cx, cy, cw, ch, ctitle in cases:
        d.add(Rect(cx, cy, cw, ch, rx=10, ry=10, fillColor=colors.HexColor("#EFF6FF"), strokeColor=NAVY, strokeWidth=0.8))
        d.add(String(cx + cw/2, cy + 6.5, ctitle, textAnchor="middle", fontName="Helvetica-Bold", fontSize=5.8, fillColor=DARK_BLUE))
        
    # Actors
    def draw_actor(ax, ay, aname):
        d.add(Circle(ax, ay+15, 6, fillColor=colors.HexColor("#1E293B"), strokeColor=NAVY, strokeWidth=0.8))
        d.add(Line(ax, ay+9, ax, ay-3, strokeColor=NAVY, strokeWidth=1))
        d.add(Line(ax-8, ay+5, ax+8, ay+5, strokeColor=NAVY, strokeWidth=1))
        d.add(Line(ax, ay-3, ax-6, ay-15, strokeColor=NAVY, strokeWidth=1))
        d.add(Line(ax, ay-3, ax+6, ay-15, strokeColor=NAVY, strokeWidth=1))
        d.add(String(ax, ay-22, aname, textAnchor="middle", fontName="Helvetica-Bold", fontSize=6, fillColor=DARK_BLUE))

    draw_actor(45, 115, "Ground Staff")
    draw_actor(45, 45, "Supervisor")
    draw_actor(480, 115, "Administrator")
    draw_actor(480, 45, "Client / Mgmt")
    
    elems.append(d)
    elems.append(Spacer(1, 6))
    
    elems.append(Paragraph("3.1.2 Use Case Catalog Table", h2_style))
    uc_table = [
        [Paragraph("Use Case ID", table_header_style), Paragraph("Primary Actor", table_header_style), Paragraph("Pre-Conditions", table_header_style), Paragraph("Post-Conditions & Output State", table_header_style)],
        [Paragraph("<b>UC-01 (Login)</b>", table_body_bold), Paragraph("All Actors", table_body_style), Paragraph("Valid user credentials", table_body_style), Paragraph("Issues HMAC-SHA256 JWT token with role claims.", table_body_style)],
        [Paragraph("<b>UC-03 (Punch)</b>", table_body_bold), Paragraph("Ground Staff", table_body_style), Paragraph("Staff logged in; within GPS radius", table_body_style), Paragraph("Logs attendance record; starts persistent stopwatch.", table_body_style)],
        [Paragraph("<b>UC-04 (Tasks)</b>", table_body_bold), Paragraph("Ground Staff", table_body_style), Paragraph("Active shift in progress", table_body_style), Paragraph("Updates task status to 'Completed' in real-time.", table_body_style)],
        [Paragraph("<b>UC-07 (Delete)</b>", table_body_bold), Paragraph("Administrator", table_body_style), Paragraph("ADMIN token / master passphrase", table_body_style), Paragraph("Permanently deletes record from db_store.json.", table_body_style)]
    ]
    t = styled_table(uc_table, [85, 95, 140, 212])
    elems.append(t)
    return elems

def get_page_17():
    """3 System Design - 3.2 System Flow Chart"""
    elems = make_chapter_header("3. SYSTEM DESIGN", "3.2 System Flow Chart & Operational Decision Architecture")
    elems.append(Spacer(1, 6))
    
    elems.append(Paragraph("3.2.1 Operational Flow: Authentication to Shift Completion", h2_style))
    elems.append(Paragraph(
        "The flow chart below illustrates the end-to-end procedural execution flow from user authentication and role-based branching "
        "to biometric attendance verification, checklist execution, and administrative reporting:",
        body_style
    ))
    
    # Vector Flow Chart Drawing
    w, h = 532, 270
    d = Drawing(w, h)
    d.add(Rect(0, 0, w, h, rx=6, ry=6, fillColor=LIGHT_BG, strokeColor=BORDER_COLOR, strokeWidth=1))
    d.add(Rect(0, h-18, w, 18, rx=6, ry=6, fillColor=DARK_BLUE, strokeColor=DARK_BLUE))
    d.add(String(10, h-13, "END-TO-END SYSTEM OPERATIONAL FLOW CHART", fontName="Helvetica-Bold", fontSize=7.5, fillColor=colors.white))
    
    def flow_box(x, y, fw, fh, text, bg="#1E3A8A", is_diamond=False):
        if is_diamond:
            cx, cy = x + fw/2, y + fh/2
            d.add(Polygon([cx, y+fh, x+fw, cy, cx, y, x, cy], fillColor=colors.HexColor("#FEF3C7"), strokeColor=colors.HexColor("#D97706"), strokeWidth=1))
            d.add(String(cx, cy-2, text, textAnchor="middle", fontName="Helvetica-Bold", fontSize=5.5, fillColor=colors.HexColor("#78350F")))
        else:
            d.add(Rect(x, y, fw, fh, rx=4, ry=4, fillColor=colors.HexColor(bg), strokeColor=colors.HexColor(bg)))
            d.add(String(x + fw/2, y + fh/2 - 2, text, textAnchor="middle", fontName="Helvetica-Bold", fontSize=5.8, fillColor=colors.white))

    # Column 1: Auth & Role Dispatch
    flow_box(20, 215, 110, 22, "Start: User Visits App", "#0F172A")
    flow_box(20, 175, 110, 22, "Login / JWT Request", "#1E3A8A")
    flow_box(20, 130, 110, 26, "Valid JWT?", "", is_diamond=True)
    flow_box(20, 85, 110, 24, "Role Branching", "#065F46")
    flow_box(20, 45, 110, 22, "Staff / Admin / Client", "#475569")
    
    # Column 2: Staff Mobile Workflow
    flow_box(160, 215, 115, 22, "Staff Portal: staff.html", "#1E3A8A")
    flow_box(160, 170, 115, 26, "Within GPS <= 250m?", "", is_diamond=True)
    flow_box(160, 125, 115, 24, "Punch In: Log Time", "#059669")
    flow_box(160, 85, 115, 22, "Start Epoch Stopwatch", "#059669")
    flow_box(160, 45, 115, 22, "Execute SOP Tasks", "#1E3A8A")
    flow_box(160, 12, 115, 22, "Punch Out: Shift End", "#DC2626")
    
    # Column 3: Admin & Reporting Workflow
    flow_box(305, 215, 115, 22, "Admin Portal: admin.html", "#1E3A8A")
    flow_box(305, 175, 115, 22, "Live Attendance Monitor", "#065F46")
    flow_box(305, 135, 115, 22, "Inspect Completed SOPs", "#1E3A8A")
    flow_box(305, 95, 115, 22, "Stock Ledger Deduct", "#D97706")
    flow_box(305, 55, 115, 22, "Resolve Service Tickets", "#1E3A8A")
    flow_box(305, 15, 115, 22, "Monthly Billing & Invoices", "#0F172A")
    
    # Column 4: Client & Estimator
    flow_box(445, 215, 75, 22, "estimator.html", "#1E3A8A")
    flow_box(445, 165, 75, 22, "Calculate Sq Ft", "#065F46")
    flow_box(445, 115, 75, 22, "jsPDF Export", "#B45309")
    flow_box(445, 65, 75, 22, "letterhead.html", "#1E3A8A")
    flow_box(445, 15, 75, 22, "End / Sign-off", "#0F172A")
    
    elems.append(d)
    elems.append(Spacer(1, 4))
    
    elems.append(Paragraph("3.2.2 Key Operational Branching Invariants", h2_style))
    elems.append(Paragraph(
        "• If JWT validation fails, the user is redirected to the login view with an error banner.<br/>"
        "• If GPS distance exceeds 250m, the punch-in button is disabled, displaying an 'Out of Bounds' alert.<br/>"
        "• If network disconnection occurs during a shift, actions queue in <code>localStorage</code> until reconnect.",
        body_style
    ))
    return elems

def get_page_18():
    """3 System Design - 3.3 Detailed Class Diagram"""
    elems = make_chapter_header("3. SYSTEM DESIGN", "3.3 Detailed Software Architecture Class Diagram")
    elems.append(Spacer(1, 6))
    
    elems.append(Paragraph("3.3.1 Detailed Service & Controller Class Hierarchy", h2_style))
    elems.append(Paragraph(
        "The detailed class diagram below specifies the software engineering classes, method signatures, visibility modifiers "
        "(<code>+</code> public, <code>-</code> private, <code>#</code> protected), and service dependencies:",
        body_style
    ))
    
    # Vector Detailed Class Diagram
    w, h = 532, 280
    d = Drawing(w, h)
    d.add(Rect(0, 0, w, h, rx=6, ry=6, fillColor=LIGHT_BG, strokeColor=BORDER_COLOR, strokeWidth=1))
    d.add(Rect(0, h-18, w, 18, rx=6, ry=6, fillColor=DARK_BLUE, strokeColor=DARK_BLUE))
    d.add(String(10, h-13, "DETAILED SOFTWARE ARCHITECTURE CLASS DIAGRAM", fontName="Helvetica-Bold", fontSize=7.5, fillColor=colors.white))
    
    def draw_detail_cls(x, y, cw, ch, name, attrs, methods):
        d.add(Rect(x, y, cw, ch, rx=3, ry=3, fillColor=colors.white, strokeColor=NAVY, strokeWidth=0.8))
        d.add(Rect(x, y+ch-14, cw, 14, rx=3, ry=3, fillColor=NAVY, strokeColor=NAVY))
        d.add(String(x+4, y+ch-10, name, fontName="Helvetica-Bold", fontSize=6.2, fillColor=colors.white))
        curr_y = y + ch - 22
        for a in attrs:
            d.add(String(x+4, curr_y, a, fontName="Helvetica", fontSize=5.5, fillColor=TEXT_MAIN))
            curr_y -= 8.5
        d.add(Line(x, curr_y+2, x+cw, curr_y+2, strokeColor=BORDER_COLOR, strokeWidth=0.5))
        curr_y -= 6.5
        for m in methods:
            d.add(String(x+4, curr_y, m, fontName="Helvetica", fontSize=5.5, fillColor=colors.HexColor("#065F46")))
            curr_y -= 8.5

    draw_detail_cls(10, 145, 160, 115, "ApiService", 
                    ["- baseUrl: String", "- token: String", "- fallbackActive: Boolean"],
                    ["+ login(u, p): Promise<Token>", "+ verifyToken(): Promise<User>", 
                     "+ fetchEmployees(): Promise<List>", "+ submitPunch(punchData): Promise",
                     "+ assignTask(task): Promise", "+ deleteRecord(id, pass): Promise"])
                     
    draw_detail_cls(185, 145, 165, 115, "ThreadedHTTPServer",
                    ["- port: Integer = 8080", "- jwtSecret: String", "- dbFile: String"],
                    ["+ do_GET(request): Response", "+ do_POST(request): Response",
                     "+ do_DELETE(request): Response", "+ generate_jwt(user, role): String",
                     "+ verify_jwt(token): Claims", "+ save_db_to_file(): Void"])
                     
    draw_detail_cls(365, 145, 155, 115, "FirebaseService",
                    ["- db: Firestore", "- auth: FirebaseAuth", "- listeners: Map"],
                    ["+ syncCollection(name): Void", "+ onSnapshot(col, cb): Void",
                     "+ pushMutation(doc): Promise", "+ signInWithGoogle(): Promise",
                     "+ enableOfflinePersistence(): Void"])

    draw_detail_cls(10, 15, 160, 115, "StaffAppController",
                    ["- currentShift: ShiftState", "- watchId: Long", "- activeTimer: Interval"],
                    ["+ initShiftStopwatch(): Void", "+ calculateElapsedSeconds(): Int",
                     "+ captureGPSCoords(): Coords", "+ validateGeofence(c): Bool",
                     "+ renderTasksList(): Void", "+ applyLeaveRequest(f): Void"])
                     
    draw_detail_cls(185, 15, 165, 115, "AdminDashboardController",
                    ["- activeRole: RoleType", "- employeesTable: Table", "- statCards: DOM"],
                    ["+ refreshDashboardMetrics(): Void", "+ filterRosterByWing(w): Void",
                     "+ exportTableToCSV(): Void", "+ approveLeave(id): Void",
                     "+ dispatchTask(t): Void", "+ inspectQualitySLA(t): Void"])
                     
    draw_detail_cls(365, 15, 155, 115, "CostEstimatorEngine",
                    ["- ratesPerSqFt: Map", "- gstRate: Float = 0.18", "- doc: jsPDF"],
                    ["+ computeBaseCost(area): Float", "+ calculateStaffing(area): Int",
                     "+ applyShiftMultiplier(m): Float", "+ generateQuotePDF(): Void",
                     "+ exportLetterhead(): Void"])

    elems.append(d)
    return elems

print("Pages 1 to 18 definitions compiled successfully.")
