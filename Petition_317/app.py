from flask import Flask, render_template, request, send_file
from docx import Document
from docx.shared import Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
import os
from datetime import datetime

app = Flask(__name__)
GENERATED_DIR = 'generated_docs'
os.makedirs(GENERATED_DIR, exist_ok=True)

# Helper function to add centered, bold, black text
def add_centered_heading(doc, text, size=12, bold=True):
    para = doc.add_paragraph()
    para.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = para.add_run(text)
    run.bold = bold
    run.font.size = Pt(size)
    run.font.color.rgb = RGBColor(0, 0, 0)

@app.route('/', methods=['GET', 'POST'])
def form_317():
    if request.method == 'POST':
        # Collect form data
        court = request.form['court']
        location = request.form['location']
        mp_no = request.form['mp_no']
        cc_no = request.form['cc_no']
        petitioner = request.form['petitioner']
        respondent = request.form['respondent']
        reason = request.form['reason']
        place = request.form['place']
        date = request.form['date']

        # Create the Word document
        doc = Document()

        # Add formatted header
        add_centered_heading(doc, f"IN THE COURT OF {court.upper()}", size=14)
        add_centered_heading(doc, location.upper(), size=12)
        doc.add_paragraph()

        add_centered_heading(doc, f"M. P. No. {mp_no} of 20")
        add_centered_heading(doc, "In")
        add_centered_heading(doc, f"No. {cc_no} of 20")
        doc.add_paragraph()

        doc.add_paragraph(f"{petitioner} … PETITIONER/ACCUSED.")
        doc.add_paragraph("VS")
        doc.add_paragraph(f"{respondent} … RESPONDENT/COMPLAINANT.")
        doc.add_paragraph()

        add_centered_heading(doc, "PETITION FILED UNDER SEC. 317 Cr.P.C.", size=12)

        # Body content
        doc.add_paragraph("The Petitioner/Accused above named most respectfully state as follows:\n")
        doc.add_paragraph("1. That the Petitioner states that the above case is posted today for further proceedings.")
        doc.add_paragraph(f"2. The Petitioner further states that petitioner is unable to appear before this Hon’ble Court today due to {reason}")
        doc.add_paragraph("3. That the absence of the Petitioner before this Hon’ble Court is neither willful nor wanton but purely due to the reason stated above.")

        doc.add_paragraph(
            "\nIn these circumstances, it is prayed that this Hon’ble Court may be pleased to dispense with "
            "the personal appearance of the accused for today only and thus render justice.\n"
        )

        doc.add_paragraph(f"Place : {place}")
        doc.add_paragraph(f"Date  : {date}")
        doc.add_paragraph("\nCounsel for Petitioner/Accused")

        # Save file
        filename = f"petition_317_{datetime.now().strftime('%Y%m%d%H%M%S')}.docx"
        filepath = os.path.join(GENERATED_DIR, filename)
        doc.save(filepath)

        return send_file(filepath, as_attachment=True)

    # Pass today's date as a string to the template
    today = datetime.now().strftime('%d-%m-%Y')
    return render_template('form_317.html', today=today)

if __name__ == '__main__':
    app.run(debug=True)
