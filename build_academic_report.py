"""
====================================================================================================
COMMERCIAL FACILITY MANAGEMENT AND AUTOMATED HOUSEKEEPING SYSTEM
Academic Capstone Engineering Project Report - Master 35-Page PDF Builder
====================================================================================================
"""

import os
import sys
import re
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, PageBreak

from academic_framework import AcademicNumberedCanvas, PDF_PATH
import academic_pages_part1 as p1
import academic_pages_part2 as p2

def compile_academic_pdf():
    print("==========================================================================")
    print(" COMPILING ACADEMIC 35-PAGE PROJECT REPORT PDF")
    print(" Strict Academic Structure | Clean Running Headers & Footers")
    print("==========================================================================")
    
    doc = SimpleDocTemplate(
        PDF_PATH,
        pagesize=letter,
        leftMargin=40,
        rightMargin=40,
        topMargin=44,
        bottomMargin=44
    )
    
    story = []
    
    # Pages 1 to 18
    p1_funcs = [getattr(p1, f"get_page_{i}") for i in range(1, 19)]
    for i, func in enumerate(p1_funcs, start=1):
        print(f"-> Assembling Page {i}...")
        story.extend(func())
        story.append(PageBreak())
        
    # Pages 19 to 35
    p2_funcs = [getattr(p2, f"get_page_{i}") for i in range(19, 36)]
    for i, func in enumerate(p2_funcs, start=19):
        print(f"-> Assembling Page {i}...")
        story.extend(func())
        if i < 35:
            story.append(PageBreak())
            
    print("Building Document Canvas with AcademicNumberedCanvas...")
    doc.build(story, canvasmaker=AcademicNumberedCanvas)
    print(f"[SUCCESS] PDF Built successfully at: {PDF_PATH}")
    
    # Also write a copy to the earlier filename so both paths work
    alt_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Revati_Enterprises_Complete_35_Page_Documentation.pdf")
    with open(PDF_PATH, "rb") as f_src:
        data = f_src.read()
    with open(alt_path, "wb") as f_dst:
        f_dst.write(data)
    print(f"[SUCCESS] Synced companion copy at: {alt_path}")
    
    # Verify Page Count
    pages = re.findall(rb'/Type\s*/Page\b', data)
    print("==========================================================================")
    print(f" VERIFIED EXACT PAGE COUNT: {len(pages)} PAGES")
    print("==========================================================================")

if __name__ == '__main__':
    compile_academic_pdf()
