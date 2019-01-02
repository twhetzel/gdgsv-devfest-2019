from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
@app.route('/home')
def show_home():
    ''' Show Home page. '''
    return render_template('index.html')


@app.route('/schedule')
def display_schedule():
    ''' Show schedule page. '''
    return render_template('schedule.html')

