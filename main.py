from flask import Flask, render_template, request
import json


app = Flask(__name__)


@app.route('/')
@app.route('/home')
def show_home():
    ''' Show Home page. '''
    return render_template('index-temp.html')


@app.route('/schedule')
def display_schedule():
    ''' Show schedule page. '''
    return render_template('schedule-temp.html')


@app.route('/speakers')
def display_speakers():
    ''' Show speakers page.'''
    with open ('./data/speakers.json') as speakers_file:
        speakers_data = json.load(speakers_file)
    with open('./data/sessions.json') as sessions_file:
        session_data = json.load(sessions_file)

    return render_template('speakers-temp.html', data=speakers_data, session_data=session_data)


@app.route('/sessions')
def display_sessions():
    ''' Show all sessions.'''
    with open ('./data/speakers.json') as speakers_file:
        speakers_data = json.load(speakers_file)
    with open('./data/sessions.json') as sessions_file:
        session_data = json.load(sessions_file)

    return render_template('sessions.html',
        speakers_data=speakers_data, session_data=session_data)



