import constants
from app import app
from flask import render_template, request


@app.route('/', methods=['GET'])
def index():
    name = ""
    gender = ""
    program_id = 0
    subject_id = []
    subjects_select = []
    is_shown = False

    if request.values.get('username'):
        name = request.values.get('username')
        is_shown = True
    if request.values.get('gender'):
        gender = request.values.get('gender')
        is_shown = True
    if request.values.get('program'):
        program_id = int(request.values.get('program'))
        is_shown = True
    if request.values.get('subject[]'):
        subject_id = request.values.getlist('subject[]')
        subjects_select = [constants.subjects[int(i)] for i in subject_id]
        is_shown = True

    if request.values.get('reset'):
        name = ""
        gender = ""
        program_id = 0
        subject_id = []
        subjects_select = []
        is_shown = False

    # выводим форму
    html = render_template(
        'index.html',
        program_list=constants.programs,
        subject_list=constants.subjects,
        gender=gender,
        name=name,
        subject_id=subject_id,
        program=constants.programs[int(program_id)],
        program_id=program_id,
        subjects_select=subjects_select,
        is_shown=is_shown,
        len=len
    )
    return html
