"""
ACADEMIC PROJECT REPORT - CORE BUILD FRAMEWORK
Commercial Facility Management and Automated Housekeeping System
Academic Project Report Generator - Exactly 35 Pages
"""

import os
import sys
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

PDF_FILENAME = "Commercial_Facility_Management_System_Project_Report_35_Pages.pdf"
PDF_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), PDF_FILENAME)

class AcademicNumberedCanvas(canvas.Canvas):
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
        # Omit header and footer on Title Page (Page 1)
        if self._pageNumber > 1:
            # Clean Academic Running Header
            self.setFont("Helvetica-Bold", 8)
            self.setFillColor(colors.HexColor("#1E3A8A"))
            self.drawString(40, 762, "COMMERCIAL FACILITY MANAGEMENT & HOUSEKEEPING SYSTEM")
            self.setFont("Helvetica", 7.5)
            self.setFillColor(colors.HexColor("#64748B"))
            self.drawRightString(572, 762, "FINAL YEAR PROJECT REPORT")
            
            self.setStrokeColor(colors.HexColor("#CBD5E1"))
            self.setLineWidth(0.65)
            self.line(40, 755, 572, 755)
            
            # Clean Academic Running Footer
            self.setStrokeColor(colors.HexColor("#E2E8F0"))
            self.setLineWidth(0.5)
            self.line(40, 36, 572, 36)
            
            self.setFont("Helvetica", 7)
            self.setFillColor(colors.HexColor("#64748B"))
            self.drawString(40, 24, "Department of Computer Science & Information Technology | Academic Project")
            page_text = f"Page {self._pageNumber} of {page_count}"
            self.setFont("Helvetica-Bold", 7.2)
            self.setFillColor(colors.HexColor("#0F172A"))
            self.drawRightString(572, 24, page_text)
            
        self.restoreState()

# Palette Constants
NAVY = colors.HexColor("#1E3A8A")
DARK_BLUE = colors.HexColor("#0F172A")
GOLD = colors.HexColor("#B45309")
TEXT_MAIN = colors.HexColor("#1E293B")
TEXT_MUTED = colors.HexColor("#475569")
LIGHT_BG = colors.HexColor("#F8FAFC")
BORDER_COLOR = colors.HexColor("#CBD5E1")
SUCCESS = colors.HexColor("#059669")
DANGER = colors.HexColor("#DC2626")

styles = getSampleStyleSheet()

# Typography Styles
title_style = ParagraphStyle(
    'DocTitle', parent=styles['Normal'],
    fontName='Helvetica-Bold', fontSize=18, leading=22, textColor=DARK_BLUE, spaceAfter=2
)
subtitle_style = ParagraphStyle(
    'DocSubtitle', parent=styles['Normal'],
    fontName='Helvetica-Bold', fontSize=8.5, leading=11, textColor=NAVY, spaceAfter=4
)
h1_style = ParagraphStyle(
    'Heading1_Custom', parent=styles['Normal'],
    fontName='Helvetica-Bold', fontSize=10.2, leading=12.5, textColor=DARK_BLUE, spaceBefore=2, spaceAfter=2
)
h2_style = ParagraphStyle(
    'Heading2_Custom', parent=styles['Normal'],
    fontName='Helvetica-Bold', fontSize=8, leading=10, textColor=NAVY, spaceBefore=2, spaceAfter=1.5
)
body_style = ParagraphStyle(
    'Body_Custom', parent=styles['Normal'],
    fontName='Helvetica', fontSize=7.2, leading=9.6, textColor=TEXT_MAIN, spaceAfter=2.5
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
    fontName='Helvetica-Bold', fontSize=6.8, leading=8.4, textColor=colors.white
)
table_body_style = ParagraphStyle(
    'TableBody', parent=styles['Normal'],
    fontName='Helvetica', fontSize=6.4, leading=8, textColor=TEXT_MAIN
)
table_body_bold = ParagraphStyle(
    'TableBodyBold', parent=table_body_style,
    fontName='Helvetica-Bold'
)
callout_style = ParagraphStyle(
    'CalloutText', parent=styles['Normal'],
    fontName='Helvetica-Oblique', fontSize=6.8, leading=8.8, textColor=DARK_BLUE
)
code_style = ParagraphStyle(
    'CodeText', parent=styles['Normal'],
    fontName='Courier', fontSize=6.2, leading=7.8, textColor=colors.HexColor("#0F172A")
)

def make_callout(text, bg="#F1F5F9", border="#94A3B8", width=532):
    t = Table([[Paragraph(text, callout_style)]], colWidths=[width])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor(bg)),
        ('BOX', (0,0), (-1,-1), 0.75, colors.HexColor(border)),
        ('PADDING', (0,0), (-1,-1), 3),
    ]))
    return t

def make_chapter_header(chap_title, subtitle_text=""):
    elems = []
    elems.append(Paragraph(chap_title.upper(), h1_style))
    if subtitle_text:
        elems.append(Paragraph(subtitle_text, subtitle_style))
    elems.append(HRFlowable(width="100%", thickness=1, color=NAVY, spaceBefore=0, spaceAfter=3))
    return elems

def styled_table(data, col_widths, is_header=True):
    t = Table(data, colWidths=col_widths)
    t_style = [
        ('GRID', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('PADDING', (0,0), (-1,-1), 2.5),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ]
    if is_header:
        t_style.append(('BACKGROUND', (0,0), (-1,0), DARK_BLUE))
        t_style.append(('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, LIGHT_BG]))
    else:
        t_style.append(('ROWBACKGROUNDS', (0,0), (-1,-1), [colors.white, LIGHT_BG]))
    t.setStyle(TableStyle(t_style))
    return t

print("Academic Framework Base Compiled.")
