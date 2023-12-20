import constants
from app import app
from flask import render_template, request


@app.route('/hello', methods=['GET'])
def hello():
    name = ""
    gender = ""
    program_id = 0
    subject_id = []
    subjects_select = []

    name = request.values.get('username')
    gender = request.values.get('gender')
    program_id = request.values.get('program')
    subject_id = request.values.getlist('subject[]')
    subjects_select = [constants.subjects[int(i)] for i in subject_id]
    html = render_template(
        'hello.html',
        gender=gender,
        name=name,
        program=constants.programs[int(program_id)],
        program_list=constants.programs,
        subjects_select=subjects_select,
        subject_list=constants.subjects,
        len=len
    )
    return html
