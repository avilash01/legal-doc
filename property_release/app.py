from flask import Flask, render_template, request, send_file
from generate_property_release import create_property_release_doc

app = Flask(__name__)

@app.route('/')
def property_release_form():
    return render_template('form_property_release.html')

@app.route('/submit-property-release', methods=['POST'])
def submit_property_release():
    data = {
        'day': request.form['day'],
        'month': request.form['month'],
        'year': request.form['year'],
        'grantor': request.form['grantor'],
        'grantor_address': request.form['grantor_address'],
        'grantee': request.form['grantee'],
        'grantee_address': request.form['grantee_address'],
        'property': request.form['property'],
        'vacancy_date': request.form['vacancy_date'],
        'witness': request.form['witness']
    }
    output_path = create_property_release_doc(data)
    return send_file(output_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
