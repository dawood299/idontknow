"""Generate the Forte Institute recommendation letter as a PDF.

Edit the variables below, then run:  python make_letter.py
"""
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.colors import HexColor
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle

STUDENT = "[Student Full Name]"
SUBJECTS = "[Subject 1], [Subject 2], [Subject 3] and [Subject 4]"
DATE = "30 September 2026"
OUT = "Recommendation_Letter_Forte_Institute.pdf"

NAVY = HexColor("#1F3A5F")

body = ParagraphStyle("body", fontName="Times-Roman", fontSize=11.5, leading=16.5,
                      alignment=TA_JUSTIFY, spaceAfter=10)
plain = ParagraphStyle("plain", parent=body, alignment=0, spaceAfter=0)


def header(canvas, doc):
    w, h = A4
    canvas.saveState()
    canvas.setFillColor(NAVY)
    canvas.setFont("Times-Bold", 20)
    canvas.drawCentredString(w / 2, h - 2.2 * cm, "FORTE INSTITUTE")
    canvas.setFont("Times-Italic", 10)
    canvas.setFillColor(HexColor("#555555"))
    canvas.drawCentredString(w / 2, h - 2.8 * cm, "[Institute Address]  |  [Phone]  |  [Email]")
    canvas.setStrokeColor(NAVY)
    canvas.setLineWidth(1.5)
    canvas.line(2.2 * cm, h - 3.2 * cm, w - 2.2 * cm, h - 3.2 * cm)
    canvas.restoreState()


doc = SimpleDocTemplate(OUT, pagesize=A4, leftMargin=2.5 * cm, rightMargin=2.5 * cm,
                        topMargin=4 * cm, bottomMargin=2 * cm,
                        title="Letter of Recommendation", author="Forte Institute")

paras = [
    f"It is my pleasure to recommend <b>{STUDENT}</b>, who studied at Forte Institute under my "
    f"instruction. Over this period I came to know {STUDENT} well, both as a student in my classes "
    "and as a young person of genuine character, and I write this letter with complete confidence.",

    f"Academically, {STUDENT} is among the most accomplished students I have taught. This is reflected "
    f"in an outstanding result of <b>four A* grades</b> in the A Level examinations, in {SUBJECTS}. "
    "Achieving the highest possible grade across four demanding subjects requires far more than "
    "ability; it requires discipline, consistency and a real commitment to understanding the material "
    "rather than simply memorising it. These were qualities I saw in every class.",

    f"What distinguishes {STUDENT} is intellectual curiosity. Questions in class went beyond what was "
    "needed for the examination, and difficult problems were treated as a challenge rather than an "
    "obstacle. Assignments were always submitted on time and completed to a high standard, and "
    f"feedback was taken seriously and acted on. {STUDENT} also worked well with classmates, often "
    "helping peers understand difficult concepts with patience and clarity.",

    f"Beyond academics, {STUDENT} is respectful, dependable and mature. I have always found "
    f"{STUDENT} honest, courteous and willing to take responsibility, qualities that will serve "
    "well in any university or professional environment.",

    f"I recommend {STUDENT} highly and without reservation. I am confident that {STUDENT} will "
    "make a valuable contribution to your institution and will continue to excel. Please feel free "
    "to contact me should you require any further information.",
]

story = [
    Paragraph(DATE, plain), Spacer(1, 14),
    Paragraph("To Whom It May Concern,", plain), Spacer(1, 12),
    Paragraph("<b><u>Subject: Letter of Recommendation for " + STUDENT + "</u></b>", plain),
    Spacer(1, 14),
]
story += [Paragraph(p, body) for p in paras]
story += [Spacer(1, 4), Paragraph("Yours sincerely,", plain), Spacer(1, 70)]

# Signature and stamp area (left: signature, right: institute stamp)
sig = Table(
    [["", "", ""],
     [Paragraph("<b>Yousaf Memon</b><br/>Teacher, Forte Institute<br/>"
                "Email: [email]  |  Phone: [phone]", plain),
      "",
      Paragraph("Institute Stamp", ParagraphStyle("st", parent=plain, alignment=1,
                                                  textColor=HexColor("#888888")))]],
    colWidths=[8 * cm, 2 * cm, 6 * cm])
sig.setStyle(TableStyle([
    ("LINEABOVE", (0, 1), (0, 1), 0.8, HexColor("#000000")),
    ("LINEABOVE", (2, 1), (2, 1), 0.8, HexColor("#000000")),
    ("LEFTPADDING", (0, 0), (-1, -1), 0),
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
]))
story.append(sig)

doc.build(story, onFirstPage=header, onLaterPages=header)
print("wrote", OUT)
