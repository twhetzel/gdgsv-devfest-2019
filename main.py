from flask import Flask, render_template, request


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
    ''' Show speakers page. '''
    return render_template('speakers-temp.html')