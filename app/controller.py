import logging
from app import app
from flask import request, jsonify, render_template
from app import schema

database = '0'  # The default database is the BUP


@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')


@app.route('/api/v1/bupschema/schema', methods=['GET'])
def api_change_database():
    params = request.args
    db = params.get('database')
    if db is not None:
        global database
        database = str(db)
        logging.info(f'Changed to database to: {database}')

        return f'Changed to database to: {database}'

    return 'No change to database has done'


@app.route('/api/v1/bupschema/question', methods=['GET'])
def api_question():
    params = request.args
    question = params.get('question')
    if question is not None:
        global database
        logging.info(f'Using database: {database}')
        sc = schema.Schema(database)
        answer = sc.ask(question)

        return answer
