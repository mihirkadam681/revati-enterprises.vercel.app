/* ==========================================================================
   REVATI ENTERPRISES - Letterhead Studio & Document Generator Logic
   ========================================================================== */

let currentZoomLevel = 1;

// Preset Documents Data
const LETTER_PRESETS = {
    quotation: {
        ref: "REF: RE/2026/QS-9482",
        date: "10th August 2026",
        recipName: "Mr. Vikramaditya Sharma",
        recipOrg: "Vice President - Corporate Real Estate & Procurement",
        recipAddr: "Apex Tech Towers Pvt. Ltd., BKC Complex, Bandra East, Mumbai - 400051",
        subject: "PROPOSAL FOR COMPREHENSIVE COMMERCIAL HOUSEKEEPING & FACILITY MANAGEMENT SERVICES (FY 2026-27)",
        salutation: "Dear Mr. Sharma,",
        body: `<p>We express our sincere gratitude for inviting <strong>REVATI ENTERPRISES</strong> to submit our formal commercial proposal for facility management and housekeeping operations across your IT Park campus in Mumbai.</p>
<p>As an <strong>ISO 9001:2015 Certified</strong> industry leader with over a decade of operational excellence, Revati Enterprises delivers end-to-end commercial sanitation, mechanized floor scrubbing, high-rise facade cleaning, waste management, and trained supervisory manpower.</p>
<p><strong>Key Highlights of Our Operational Commitment:</strong></p>
<ul>
  <li><strong>Deployable Staff:</strong> 18 Trained Housekeeping Executives & 2 Certified Facility Supervisors.</li>
  <li><strong>Mechanized Equipment:</strong> Industrial Auto-Scrubber Dryers, High-Pressure Washers & HEPA Vacuum Units.</li>
  <li><strong>Eco-Friendly Chemical Standards:</strong> 100% EcoLab & Diversey Green-certified bio-degradable solutions.</li>
  <li><strong>Statutory Compliance:</strong> Complete ESIC, PF, Minimum Wages Act, and Workmen Compensation adherence.</li>
</ul>
<p>Attached herewith is our itemized monthly financial estimate. We welcome the opportunity to present our site deployment plan in person at your office.</p>`,
        signeeName: "MR. MIHIR R. KADAM",
        signeeTitle: "Founder & Managing Director"
    },

    offer: {
        ref: "REF: RE/2026/HR-OFFER-7712",
        date: "10th August 2026",
        recipName: "Mr. Rohan S. Deshmukh",
        recipOrg: "Facility Operations & Site Management Division",
        recipAddr: "Flat 204, Green Heights, Thane West, Maharashtra - 400601",
        subject: "OFFICIAL LETTER OF EMPLOYMENT OFFER - SENIOR FACILITY SUPERVISOR",
        salutation: "Dear Mr. Deshmukh,",
        body: `<p>We are pleased to offer you employment with <strong>REVATI ENTERPRISES</strong> as <strong>Senior Facility Supervisor</strong> for our Commercial Operations Division in Mumbai/Thane, effective from <strong>1st September 2026</strong>.</p>
<p><strong>Key Terms & Employment Package Summary:</strong></p>
<ul>
  <li><strong>Designation:</strong> Senior Facility Supervisor (Commercial & Corporate Division)</li>
  <li><strong>Gross Annual Remuneration (CTC):</strong> ₹ 4,80,000/- per annum (inclusive of ESIC, PF, Gratuity & Allowances).</li>
  <li><strong>Primary Duty Location:</strong> BKC & MIDC Commercial Complexes, Mumbai.</li>
  <li><strong>Probationary Period:</strong> Six (6) months from the date of joining.</li>
</ul>
<p>You will be responsible for overseeing daily housekeeping SLA standards, managing shift staff deployment, chemical inventory logistics, and client relations. Please sign and return a duplicate copy of this offer letter as acceptance of employment.</p>`,
        signeeName: "MR. MIHIR R. KADAM",
        signeeTitle: "Founder & Managing Director"
    },

    leave: {
        ref: "REF: RE/2026/HR-LV-4491",
        date: "10th August 2026",
        recipName: "Ms. Sneha V. Kulkarni",
        recipOrg: "Operations & Quality Control Department",
        recipAddr: "Revati Operations Hub, MIDC Zone, Andheri East, Mumbai - 400093",
        subject: "OFFICIAL SANCTION & APPROVAL OF PAID ANNUAL LEAVE",
        salutation: "Dear Ms. Kulkarni,",
        body: `<p>This is to formally inform you that your application for Paid Annual Leave dated 5th August 2026 has been reviewed and <strong>APPROVED</strong> by the Executive Board of <strong>REVATI ENTERPRISES</strong>.</p>
<p><strong>Sanctioned Leave Details:</strong></p>
<ul>
  <li><strong>Leave Period:</strong> 15th August 2026 to 22nd August 2026 (8 Calendar Days).</li>
  <li><strong>Type of Leave:</strong> Earned / Paid Privilege Leave (PL).</li>
  <li><strong>Date of Resuming Duties:</strong> Monday, 24th August 2026 (08:30 AM).</li>
  <li><strong>Temporary Duty Charge Handover:</strong> Mr. Subhash Rane (Assistant Operations Lead).</li>
</ul>
<p>We wish you a pleasant and restful break. Please ensure all pending quality audit files are handed over to your designated stand-in before your departure.</p>`,
        signeeName: "MR. MIHIR R. KADAM",
        signeeTitle: "Founder & Managing Director"
    },

    holidays: {
        ref: "REF: RE/2026/HR-HOL-2026",
        date: "10th August 2026",
        recipName: "All Valued Clients, Corporate Partners & Operations Staff",
        recipOrg: "Revati Enterprises Commercial Network",
        recipAddr: "Mumbai (HQ), Pune, Thane, Navi Mumbai & PAN-India Regional Hubs",
        subject: "OFFICIAL CORPORATE & NATIONAL PUBLIC HOLIDAYS CALENDAR (CY 2026-27)",
        salutation: "Dear Clients & Team Members,",
        body: `<p>Please find below the official schedule of <strong>Corporate & Public Holidays</strong> observed by <strong>REVATI ENTERPRISES</strong> for the calendar year 2026-27 across our corporate headquarters and regional operations.</p>
<p><strong>Official Declared Public Holidays:</strong></p>
<ol>
  <li><strong>Independence Day:</strong> 15th August 2026 (Saturday)</li>
  <li><strong>Ganesh Chaturthi:</strong> 27th August 2026 (Thursday)</li>
  <li><strong>Mahatma Gandhi Jayanti:</strong> 2nd October 2026 (Friday)</li>
  <li><strong>Dussehra (Vijayadashami):</strong> 20th October 2026 (Tuesday)</li>
  <li><strong>Diwali (Laxmi Pujan):</strong> 8th November 2026 (Sunday)</li>
  <li><strong>Christmas Day:</strong> 25th December 2026 (Friday)</li>
</ol>
<p><em>Note for Commercial Clients:</em> Essential 24/7 emergency facility management, hospital sanitation teams, and duty supervisors will remain fully operational on all holidays as per contracted SLA rosters.</p>`,
        signeeName: "MR. MIHIR R. KADAM",
        signeeTitle: "Founder & Managing Director"
    },

    sla: {
        ref: "REF: RE/2026/SLA-3021",
        date: "10th August 2026",
        recipName: "Board of Directors & Quality Audit Committee",
        recipOrg: "Grand Horizon Corporate Mall & Commercial Complex",
        recipAddr: "Vimannagar Central Hub, Viman Nagar, Pune, Maharashtra - 411014",
        subject: "MONTHLY SLA QUALITY ASSURANCE & HYGIENE COMPLIANCE CERTIFICATE - JULY 2026",
        salutation: "Respected Management Team,",
        body: `<p>This official letter certifies that <strong>REVATI ENTERPRISES</strong> has completed the monthly statutory and operational Service Level Agreement (SLA) audit for the period of 1st July 2026 to 31st July 2026 at Grand Horizon Mall & Office Suites.</p>
<p>Our quality verification audit assessed daily hygiene scores, washroom sanitation index, HVAC duct cleanliness, chemical safety protocol, and manpower attendance metrics across all 5 commercial floors.</p>
<p><strong>Audit Summary Metrics:</strong></p>
<ul>
  <li><strong>Overall SLA Hygiene Index Achieved:</strong> 99.4% (Benchmark: 95.0%)</li>
  <li><strong>Manpower Attendance Rate:</strong> 98.8% with zero unannounced shift shortages.</li>
  <li><strong>Client Complaint Resolution Time:</strong> 100% resolved within < 15 minutes response SLA.</li>
  <li><strong>Safety & Hazard Incidents:</strong> ZERO recorded lost-time injuries or chemical accidents.</li>
</ul>
<p>We confirm that all premises under our care adhere strictly to WHO environmental sanitation and ISO 9001:2015 quality standards.</p>`,
        signeeName: "Priya S. Nambiar",
        signeeTitle: "Quality Assurance & Compliance Head"
    },

    clearance: {
        ref: "REF: RE/2026/CLR-8819",
        date: "10th August 2026",
        recipName: "Facility & Admin Department",
        recipOrg: "Mahindra Logistics Hub & Warehousing Park",
        recipAddr: "Bhiwandi Logistics Zone, Thane, Maharashtra - 421302",
        subject: "DEEP SANITATION & HEAVY INDUSTRIAL MAINTENANCE CLEARANCE CERTIFICATE",
        salutation: "To Whomsoever It May Concern,",
        body: `<p>This is to formally certify that <strong>REVATI ENTERPRISES</strong> has successfully executed and completed the intensive quarterly Deep Cleaning, Epoxy Scrubbing, High-Bay Dust Extraction, and Chemical Disinfection drive for <strong>Logistics Bay 3 & 4</strong> at Mahindra Logistics Park, Bhiwandi.</p>
<p><strong>Scope of Works Completed:</strong></p>
<ol>
  <li>Heavy Duty Industrial Floor Scrubbing & Degreasing (Epoxy Coating Preservation).</li>
  <li>High-Bay Structural Beam Dusting & Overhead Lighting Assembly Cleansing at 12m height.</li>
  <li>Biological Disinfection & Odor Neutralization of employee cafeterias and rest facilities.</li>
  <li>Waste segregation and safe disposal of non-hazardous packaging debris.</li>
</ol>
<p>The inspected areas have passed all microbial surface swab tests and safety inspections, and are hereby declared <strong>Fully Operational & Hygiene Cleared</strong> for daily shift work.</p>`,
        signeeName: "Subhash C. Rane",
        signeeTitle: "Senior Operations Manager - Industrial Facilities"
    },

    contract: {
        ref: "REF: RE/2026/CTR-1104",
        date: "10th August 2026",
        recipName: "Head of Procurement & Contracts",
        recipOrg: "Star Health Care & Research Hospital",
        recipAddr: "S.V. Road, Malad West, Mumbai, Maharashtra - 400064",
        subject: "LETTER OF ACCEPTANCE & CONTRACT COMMENCEMENT - HOSPITAL SANITATION SERVICES",
        salutation: "Dear Procurement Committee,",
        body: `<p>We hereby acknowledge receipt of your Award Letter <strong>SH/PUR/2026/884</strong> and formally accept the contract for <em>Hospital Grade Deep Cleaning & Facility Support Services</em> at Star Health Care Hospital for a period of two (2) years commencing 1st September 2026.</p>
<p>Revati Enterprises confirms that all required specialized healthcare sanitation teams, infection-control certified supervisors, bio-medical waste compliance personnel, and heavy-duty floor care equipment will be mobilized on site 5 days prior to the official commencement date.</p>
<p>We assure you of our highest standard of medical hygiene, zero infection protocols, and round-the-clock facility monitoring.</p>`,
        signeeName: "MR. MIHIR R. KADAM",
        signeeTitle: "Founder & Managing Director"
    },

    general: {
        ref: "REF: RE/2026/GEN-5520",
        date: "10th August 2026",
        recipName: "Valued Clients & Corporate Partners",
        recipOrg: "Revati Enterprises Network",
        recipAddr: "Pan-India Operations Division",
        subject: "OFFICIAL CORPORATE ANNOUNCEMENT: EXPANSION OF PUNE & THANE REGIONAL HUBS",
        salutation: "Dear Partners,",
        body: `<p>We are delighted to inform you that <strong>REVATI ENTERPRISES</strong> is expanding its regional operations with state-of-the-art logistics hubs in Pune (Viman Nagar) and Thane (Wagle Estate).</p>
<p>This expansion enhances our emergency response time to under 30 minutes for all commercial real estate, corporate offices, and industrial logistics parks across Western Maharashtra.</p>
<p>We thank all our clients for their continued trust in Revati Enterprises as your preferred facility management partner.</p>`,
        signeeName: "MR. MIHIR R. KADAM",
        signeeTitle: "Founder & Managing Director"
    },

    blank: {
        ref: "REF: RE/2026/____",
        date: "___ ____________ 2026",
        recipName: "_________________________",
        recipOrg: "_________________________",
        recipAddr: "_________________________________________________________",
        subject: "OFFICIAL SUBJECT LINE HERE",
        salutation: "Dear Sir / Madam,",
        body: `<p style="color: #A0AEC0; font-style: italic; margin-top: 40px; text-align: center;">[ This is a Blank Letterhead Paper setup. Type your letter contents here or print directly to use as pre-printed company stationery. ]</p><br><br><br><br><br>`,
        signeeName: "MR. MIHIR R. KADAM",
        signeeTitle: "Founder & Managing Director"
    }
};

// Initialize Page & Digital Signature Canvas
function initLetterhead() {
    loadPresetDocument("quotation");
    const today = new Date();
    const formattedStampDate = today.getDate().toString().padStart(2, '0') + '-' + 
                               today.toLocaleString('en-US', { month: 'short' }).toUpperCase() + '-' + 
                               today.getFullYear();
    const stampDateEl = document.getElementById('stampDateDisplay');
    if (stampDateEl) stampDateEl.innerText = formattedStampDate;
    initSignatureCanvas();
}

let isDrawing = false;
let sigCanvas, sigCtx;

function initSignatureCanvas() {
    sigCanvas = document.getElementById('signatureCanvas');
    if (!sigCanvas) return;
    sigCtx = sigCanvas.getContext('2d');
    sigCtx.lineWidth = 2.5;
    sigCtx.lineCap = 'round';
    sigCtx.strokeStyle = '#1E3A8A';

    function getPos(e) {
        const rect = sigCanvas.getBoundingClientRect();
        const clientX = e.touches ? e.touches[0].clientX : e.clientX;
        const clientY = e.touches ? e.touches[0].clientY : e.clientY;
        return {
            x: (clientX - rect.left) * (sigCanvas.width / rect.width),
            y: (clientY - rect.top) * (sigCanvas.height / rect.height)
        };
    }

    function startDraw(e) {
        isDrawing = true;
        const pos = getPos(e);
        sigCtx.beginPath();
        sigCtx.moveTo(pos.x, pos.y);
    }

    function moveDraw(e) {
        if (!isDrawing) return;
        const pos = getPos(e);
        sigCtx.lineTo(pos.x, pos.y);
        sigCtx.stroke();
    }

    function stopDraw() {
        isDrawing = false;
    }

    sigCanvas.addEventListener('mousedown', startDraw);
    sigCanvas.addEventListener('mousemove', moveDraw);
    sigCanvas.addEventListener('mouseup', stopDraw);
    sigCanvas.addEventListener('mouseleave', stopDraw);

    sigCanvas.addEventListener('touchstart', startDraw, { passive: true });
    sigCanvas.addEventListener('touchmove', moveDraw, { passive: true });
    sigCanvas.addEventListener('touchend', stopDraw);
}

function clearSignatureCanvas() {
    if (!sigCanvas || !sigCtx) return;
    sigCtx.clearRect(0, 0, sigCanvas.width, sigCanvas.height);
}

function applyDrawnSignature() {
    if (!sigCanvas) return;
    const dataUrl = sigCanvas.toDataURL('image/png');
    const imgEl = document.getElementById('paperDrawnSignatureImg');
    const scriptEl = document.getElementById('paperScriptSignature');
    if (imgEl) {
        imgEl.src = dataUrl;
        imgEl.style.display = 'block';
    }
    if (scriptEl) scriptEl.style.display = 'none';
}

function switchSignatureType(type) {
    const drawContainer = document.getElementById('sigDrawContainer');
    const uploadContainer = document.getElementById('sigUploadContainer');
    const scriptEl = document.getElementById('paperScriptSignature');
    const imgEl = document.getElementById('paperDrawnSignatureImg');

    if (drawContainer) drawContainer.style.display = (type === 'draw') ? 'block' : 'none';
    if (uploadContainer) uploadContainer.style.display = (type === 'upload') ? 'block' : 'none';

    if (type === 'script') {
        if (scriptEl) scriptEl.style.display = 'block';
        if (imgEl) imgEl.style.display = 'none';
    } else if (type === 'none') {
        if (scriptEl) scriptEl.style.display = 'none';
        if (imgEl) imgEl.style.display = 'none';
    }
}

function handleSignatureFileUpload(event) {
    const file = event.target.files[0];
    if (!file) return;
    const reader = new FileReader();
    reader.onload = function(e) {
        const imgEl = document.getElementById('paperDrawnSignatureImg');
        const scriptEl = document.getElementById('paperScriptSignature');
        if (imgEl) {
            imgEl.src = e.target.result;
            imgEl.style.display = 'block';
        }
        if (scriptEl) scriptEl.style.display = 'none';
    };
    reader.readAsDataURL(file);
}

if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initLetterhead);
} else {
    initLetterhead();
}
window.onload = initLetterhead;

// Change Visual Template Layout
function changeTemplate(templateClass, btnElement) {
    const sheet = document.getElementById('paperSheet');
    if (!sheet) return;

    // Reset template classes
    sheet.className = "a4-sheet " + templateClass;

    // Highlight active preset button
    document.querySelectorAll('.preset-grid .btn-preset').forEach(btn => btn.classList.remove('active'));
    if (btnElement) btnElement.classList.add('active');
}

// Load Preset Document Text
function loadPresetDocument(key) {
    const preset = LETTER_PRESETS[key];
    if (!preset) return;

    // Fill Form Controls
    document.getElementById('inputRefNo').value = preset.ref;
    document.getElementById('inputDate').value = preset.date;
    document.getElementById('inputRecipName').value = preset.recipName;
    document.getElementById('inputRecipOrg').value = preset.recipOrg;
    document.getElementById('inputRecipAddr').value = preset.recipAddr;
    document.getElementById('inputSubject').value = preset.subject;
    document.getElementById('inputSalutation').value = preset.salutation;
    document.getElementById('inputBody').value = preset.body;
    document.getElementById('inputSigneeName').value = preset.signeeName;
    document.getElementById('inputSigneeTitle').value = preset.signeeTitle;

    // Update Paper
    syncLetterhead();
}

// Sync Left Panel Input with Printable Paper
function syncLetterhead() {
    const compName = document.getElementById('inputCompName') ? document.getElementById('inputCompName').value : "REVATI ENTERPRISES";
    const compTagline = document.getElementById('inputCompTagline') ? document.getElementById('inputCompTagline').value : "Commercial Housekeeping & Facility Management";
    const helpline = document.getElementById('inputHelpline') ? document.getElementById('inputHelpline').value : "+91 9769930626 / +91 9930023185";
    const email = document.getElementById('inputEmail') ? document.getElementById('inputEmail').value : "info@revatienterprises.com";
    const hqAddr = document.getElementById('inputHqAddr') ? document.getElementById('inputHqAddr').value : "MIDC Industrial Area, Andheri East, Mumbai - 400093";

    const refNo = document.getElementById('inputRefNo').value;
    const date = document.getElementById('inputDate').value;
    const recipName = document.getElementById('inputRecipName').value;
    const recipOrg = document.getElementById('inputRecipOrg').value;
    const recipAddr = document.getElementById('inputRecipAddr').value;
    const subject = document.getElementById('inputSubject').value;
    const salutation = document.getElementById('inputSalutation').value;
    const body = document.getElementById('inputBody').value;
    const signeeName = document.getElementById('inputSigneeName').value;
    const signeeTitle = document.getElementById('inputSigneeTitle').value;
    const closing = document.getElementById('inputClosing') ? document.getElementById('inputClosing').value : "Yours Sincerely,";
    const signoffOrg = document.getElementById('inputSignoffOrg') ? document.getElementById('inputSignoffOrg').value : "REVATI ENTERPRISES";

    // Update Header Fields
    if (document.getElementById('paperCompName')) document.getElementById('paperCompName').innerText = compName;
    if (document.getElementById('paperCompTagline')) document.getElementById('paperCompTagline').innerText = compTagline;
    if (document.getElementById('paperHelplineShort')) document.getElementById('paperHelplineShort').innerText = helpline;
    if (document.getElementById('paperEmailShort')) document.getElementById('paperEmailShort').innerText = email;
    if (document.getElementById('paperHqAddrShort')) document.getElementById('paperHqAddrShort').innerText = hqAddr;

    // Update Document Meta & Content
    document.getElementById('paperRefNo').innerText = refNo;
    document.getElementById('paperDate').innerText = date;
    document.getElementById('paperRecipName').innerText = recipName;
    document.getElementById('paperRecipOrg').innerText = recipOrg;
    document.getElementById('paperRecipAddr').innerText = recipAddr;
    document.getElementById('paperSubject').innerText = subject;
    document.getElementById('paperSalutation').innerText = salutation;
    document.getElementById('paperBody').innerHTML = body;
    document.getElementById('paperSigneeName').innerText = signeeName;
    document.getElementById('paperSigneeTitle').innerText = signeeTitle;
    if (document.getElementById('paperClosing')) document.getElementById('paperClosing').innerText = closing;
    if (document.getElementById('paperSignoffOrg')) document.getElementById('paperSignoffOrg').innerText = signoffOrg;
    const scriptSigEl = document.getElementById('paperScriptSignature');
    if (scriptSigEl) scriptSigEl.innerText = signeeName;
}

// Branding Toggles
function toggleWatermark(show) {
    const wm = document.getElementById('lhWatermark');
    if (wm) wm.style.display = show ? 'block' : 'none';
}

function toggleStamp(show) {
    const stamp = document.getElementById('paperStamp');
    if (stamp) stamp.style.display = show ? 'block' : 'none';
}

function toggleISO(show) {
    const iso = document.getElementById('lhIsoBadge');
    if (iso) iso.style.display = show ? 'block' : 'none';
}

// Trigger Print Function via Browser Print Engine
function triggerPrintLetterhead() {
    const sheet = document.getElementById('paperSheet');
    const prevTransform = sheet ? sheet.style.transform : '';
    if (sheet) sheet.style.transform = 'none';
    window.print();
    if (sheet) sheet.style.transform = prevTransform;
}

// Direct High-Resolution PDF Download (.pdf)
function downloadPDF() {
    const sheet = document.getElementById('paperSheet');
    if (!sheet) return;

    const prevTransform = sheet.style.transform;
    sheet.style.transform = 'none';

    const refVal = document.getElementById('inputRefNo') ? document.getElementById('inputRefNo').value : 'Letterhead';
    const filename = (refVal || 'Revati_Enterprises_Letterhead').replace(/[^a-zA-Z0-9_-]/g, '_') + '.pdf';

    const opt = {
        margin: 0,
        filename: filename,
        image: { type: 'jpeg', quality: 0.98 },
        html2canvas: { scale: 2, useCORS: true, logging: false },
        jsPDF: { unit: 'mm', format: 'a4', orientation: 'portrait' }
    };

    if (window.html2pdf) {
        html2pdf().set(opt).from(sheet).save().then(() => {
            sheet.style.transform = prevTransform;
        }).catch(err => {
            console.error('html2pdf error:', err);
            sheet.style.transform = prevTransform;
            triggerPrintLetterhead();
        });
    } else {
        triggerPrintLetterhead();
    }
}

// Export as Editable Microsoft Word Document (.doc)
function downloadWord() {
    const sheet = document.getElementById('paperSheet');
    if (!sheet) return;

    const refVal = document.getElementById('inputRefNo') ? document.getElementById('inputRefNo').value : 'Letterhead';
    const filename = (refVal || 'Revati_Enterprises_Letterhead').replace(/[^a-zA-Z0-9_-]/g, '_') + '.doc';

    const htmlHeader = `
        <html xmlns:o='urn:schemas-microsoft-com:office:office' xmlns:w='urn:schemas-microsoft-com:office:word' xmlns='http://www.w3.org/TR/REC-html40'>
        <head><meta charset='utf-8'><title>${filename}</title>
        <style>
            body { font-family: Arial, sans-serif; font-size: 11pt; line-height: 1.5; color: #111; padding: 20px; }
            .lh-brand-title { font-size: 20pt; font-weight: bold; color: #0A0E17; }
            .lh-brand-subtitle { font-size: 9pt; color: #D4AF37; font-weight: bold; text-transform: uppercase; }
            .lh-subject-bar { background: #F4E8C1; border-left: 4px solid #D4AF37; padding: 8px; font-weight: bold; margin: 15px 0; }
            .lh-rubber-stamp { border: 2px solid #1E3A8A; color: #1E3A8A; padding: 5px; font-weight: bold; font-size: 8pt; display: inline-block; }
            .lh-footer { border-top: 2px solid #D4AF37; margin-top: 30px; padding-top: 10px; font-size: 8pt; color: #555; }
        </style>
        </head>
        <body>
            ${sheet.innerHTML}
        </body>
        </html>
    `;

    const blob = new Blob(['\ufeff', htmlHeader], { type: 'application/msword' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = filename;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
}

// Zoom In/Out Paper Sheet
function zoomPaper(direction) {
    const sheet = document.getElementById('paperSheet');
    if (!sheet) return;

    if (direction === 1 && currentZoomLevel < 1.3) {
        currentZoomLevel += 0.1;
    } else if (direction === -1 && currentZoomLevel > 0.6) {
        currentZoomLevel -= 0.1;
    }

    sheet.style.transform = `scale(${currentZoomLevel})`;
}

// Copy Plain Text of Letter
function copyLetterText() {
    const paper = document.getElementById('paperSheet');
    if (!paper) return;

    const ref = document.getElementById('paperRefNo').innerText;
    const date = document.getElementById('paperDate').innerText;
    const recipient = document.getElementById('paperRecipName').innerText + "\n" +
                      document.getElementById('paperRecipOrg').innerText + "\n" +
                      document.getElementById('paperRecipAddr').innerText;
    const subject = document.getElementById('paperSubject').innerText;
    const salutation = document.getElementById('paperSalutation').innerText;
    const bodyText = document.getElementById('paperBody').innerText;
    const signee = document.getElementById('paperSigneeName').innerText + "\n" +
                   document.getElementById('paperSigneeTitle').innerText;

    const fullLetter = `REVATI ENTERPRISES - COMMERCIAL HOUSEKEEPING & FACILITY MANAGEMENT
${ref} | Date: ${date}

TO:
${recipient}

SUBJECT: ${subject}

${salutation}

${bodyText}

Yours Sincerely,
For REVATI ENTERPRISES
${signee}
Helpline: +91 9769930626 / +91 9930023185 | Web: www.revatienterprises.com`;

    navigator.clipboard.writeText(fullLetter).then(() => {
        alert("✅ Letterhead document text copied to clipboard successfully!");
    }).catch(err => {
        alert("Copied letter text:\n\n" + fullLetter);
    });
}
