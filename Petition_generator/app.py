from flask import Flask, render_template, request, send_file
from docx import Document
from docx.shared import Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
import os
from datetime import datetime

app = Flask(__name__)
GENERATED_DIR = 'generated_docs'
os.makedirs(GENERATED_DIR, exist_ok=True)

# Function to add centered heading text with black color
def add_centered_heading(doc, text, size=12, bold=True):
    para = doc.add_paragraph()
    para.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = para.add_run(text)
    run.bold = bold
    run.font.size = Pt(size)
    run.font.color.rgb = RGBColor(0, 0, 0)  # Black

@app.route('/', methods=['GET', 'POST'])
def form_311():
    if request.method == 'POST':
        # Get form data
        court = request.form['court']
        location = request.form['location']
        mp_no = request.form['mp_no']
        mp_year = request.form['mp_year']
        cc_no = request.form['cc_no']
        cc_year = request.form['cc_year']
        petitioner = request.form['petitioner']
        respondent = request.form['respondent']
        reason1 = request.form['reason1']
        reason3 = request.form['reason3']

        # Create the Word document
        doc = Document()

        # Add formatted headings
        add_centered_heading(doc, f"IN THE COURT OF {court.upper()}", size=14)
        add_centered_heading(doc, f"{location.upper()}", size=13)
        doc.add_paragraph()  # blank line
        add_centered_heading(doc, f"M. P. No. {mp_no} of {mp_year}")
        add_centered_heading(doc, "In")
        add_centered_heading(doc, f"C. C. No. {cc_no} of {cc_year}")
        doc.add_paragraph()

        doc.add_paragraph(f"{petitioner} … PETITIONERS/ACCUSED.")
        doc.add_paragraph("VS")
        doc.add_paragraph(f"{respondent} .. RESPONDENT/COMPLAINANT.")
        doc.add_paragraph()

        add_centered_heading(doc, "PETITION FILED UNDER SEC. 311 Cr.P.C.", size=12)

        # Add petition body
        doc.add_paragraph("The petitioner above named states as follows:\n")

        doc.add_paragraph(f"1. The petitioner states that {reason1}")
        doc.add_paragraph("2. The petitioner states that it is neither willful nor wanton but due to the reason stated above.")
        doc.add_paragraph(f"3. The petitioner states that {reason3}")

        doc.add_paragraph(
            "\nIn these circumstances it is therefore prayed that this Hon’ble Court may be pleased to "
            "permit the petitioner to reopen and recall the PW – and cross examine in the interest of justice "
            "and thus render justice."
        )

        # Save the file
        filename = f"petition_311_{datetime.now().strftime('%Y%m%d%H%M%S')}.docx"
        filepath = os.path.join(GENERATED_DIR, filename)
        doc.save(filepath)

        return send_file(filepath, as_attachment=True)

    return render_template('form_311.html')

if __name__ == '__main__':
    app.run(debug=True)
