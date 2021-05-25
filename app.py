# https://stackoverflow.com/questions/25149493/how-to-call-another-webservice-api-from-flask
# https://thispointer.com/python-three-ways-to-check-if-a-file-is-empty/
# https://www.geeksforgeeks.org/how-to-create-a-pop-up-message-when-a-button-is-pressed-in-python-tkinter/
# https://stackoverflow.com/questions/23112316/using-flask-how-do-i-modify-the-cache-control-header-for-all-output
# https://dbader.org/blog/python-check-if-file-exists#:~:text=The%20most%20common%20way%20to%20check%20for%20the,search%20engine%20on%20how%20to%20solve%20this%20problem.
# fixing word cloud multi thread issues:
# https://www.shanelynn.ie/using-python-threading-for-multiple-results-queue/
# https://stackoverflow.com/questions/31264826/start-a-flask-application-in-separate-thread
# https://izziswift.com/start-a-flask-application-in-separate-thread/
# other changes
# https://stackoverflow.com/questions/29104107/upload-image-using-post-form-data-in-python-requests
# https://stackoverflow.com/questions/29104107/upload-image-using-post-form-data-in-python-requests
# https://stackoverflow.com/questions/55265779/how-to-jsonify-a-picture-in-flask
# http://whitenoise.evans.io/en/stable/flask.html
# Lazy Loading images in HTML
# https://htmlf1.com/snippet/lazy-loading-images-in-html


import os
import requests
import os.path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import requests
from flask import Flask, jsonify, render_template, redirect, url_for, request, abort
import flask_restful
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
from urllib.request import urlopen
from flask import flash
import threading
import base64
import io
import logging
import numpy as np
from PIL import Image
from io import BytesIO
import webbrowser
import PIL.Image
data = 'foo'

#application flask run
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 300
app.config['SECRET_KEY'] = 'oTv!5ox8LB#A&@cBHpa@onsKU'

def random_color_func(word=None, font_size=None, position=None, orientation=None, font_path=None, random_state=None):
    h = int(360.0 * 45.0 / 255.0)
    s = int(100.0 * 255.0 / 255.0)
    l = int(100.0 * float(random_state.randint(60, 120)) / 255.0)

    return "hsl({}, {}%, {}%)".format(h, s, l)


@app.route('/', methods=['GET', 'POST'])
def index():
    #flash('in the index')
    try:
        f = open('game.json')
        f.close()
    except IOError:
        print('File is not accessible')
    print('File is accessible')
    return render_template('index.html')

#this needs to be the landing page for the word cloud- this is where the user hits the "submit" button
@app.route("/wordcloud", methods=['POST', 'GET'])
def wordcloud():
    flash('Welcome!')
    return render_template('wordcloud.html')

r = ""
counter = 0

@app.route("/resetCount")
def resetCount(wordCountRuns):
    wordCountRuns = 0
    return(wordCountRuns)

def increment(counter):
    counter = counter + 1
    print(counter)
    return(counter)

# accessing web scraper data service
@app.route("/getValerie", methods=['POST', 'GET'])
def getValerie():
    #update the following web address to whatever team members web address will be
    r = requests.get("http://127.0.0.4:80/wordcloud")
    return(r)

# loads after submit button pressed, creates word cloud
@app.route("/wordcloud2", methods=['POST', 'GET'])
def wordcloud2():
    # verify that json data available from website scraper
    try:
        requests.get('http://valchin.com/sendjson2021')
    #when error happens then flashing this error will be helpful
    except IOError:
        print('File is not accessible')
        flash('Files not found or readable.')
        return render_template('wordcloud.html')
    print('File is accessible')
    flash('You created a word cloud')
    jsonData = requests.get('http://valchin.com/sendjson2021')
    print("jsonData successful")
    file_content = jsonData.text
    # Check the data file by printing to local console
    print(file_content)
    print('File data above this line')

    #this section generates the word cloud
    wordcloud = WordCloud(
        stopwords=STOPWORDS,
        background_color='white',
        width=1200,
        height=1000,
        color_func=random_color_func
    ).generate(file_content)
    plt.imshow(wordcloud)
    plt.axis('off')

    # saves picture file to picture format
    plt.savefig('static/wordCloud.png')
    print("wordCloud.png created")
    #increment(counter)
    #print(counter)
    flash('Success! Word Cloud has been processed and is loading')
    return render_template('wordcloud2.html')

# this is the only word cloud get method that works
@app.route('/wordcloud66', methods=['POST', 'GET'])
def wordcloudGet66():
    # verify that json data available from website scraper
    try:
        requests.get('http://valchin.com/sendjson2021')
    #when error happens then flashing this error will be helpful
    except IOError:
        print('File is not accessible')
        flash('Files not found or readable.')
        return render_template('wordcloud.html')
    print('File is accessible')
    flash('You created a word cloud')
    jsonData = requests.get('http://valchin.com/sendjson2021')
    print("jsonData successful")
    file_content = jsonData.text
    # Check the data file by printing to local console
    print(file_content)
    print('File data above this line')

    #this section generates the word cloud
    wordcloud = WordCloud(
        stopwords=STOPWORDS,
        background_color='white',
        width=1200,
        height=1000,
        color_func=random_color_func
    ).generate(file_content)
    plt.imshow(wordcloud)
    plt.axis('off')
    # plt.show()
    # saves picture file to picture format
    plt.savefig('static/wordCloud.png')
    print("wordCloud.png created")

    file_content = open("static/wordCloud.png", 'rb')

    with open('static/wordCloud.png', 'rb') as image_file:
        print('file_content')
        encoded_string = base64.b64encode(image_file.read())

        print('file content created')

        print('checking if file can be written')
        #image decoding from recent encoding - this is to prove that
        #encoded string will actually return back to the original picture
        newImage = Image.open(BytesIO(base64.b64decode(encoded_string)))
        print('Encoding completed')

        #image is successfully printed to static folder proving that data can be decoded
        newImage.save('static/noob.png', 'PNG')
        print('PNG created')

        return (encoded_string)

# get request for static PNG - does not generate new image
@app.route('/wordcloud67', methods=['POST', 'GET'])
def wordcloudGet67():
    try:
        requests.get('http://valchin.com/sendjson2021')
    #when error happens then flashing this error will be helpful
    except IOError:
        print('File is not accessible')
        flash('picture file not found')
        return ('File is not accessible')
    print('pre file content opening of word cloud')
    file_content = open("static/wordCloud.png", 'rb')
    with open('static/wordCloud.png', 'rb') as image_file:
        print('file_content')
        encoded_string = base64.b64encode(image_file.read())

        print('file content created')

        print('checking if file can be written')
        #image decoding from recent encoding - this is to prove that
        #encoded string will actually return back to the original picture
        newImage = Image.open(BytesIO(base64.b64decode(encoded_string)))
        print('Encoding completed')

        print("test")
        #image is successfully printed to static folder proving that data can be decoded
        newImage.save('static/noob.png', 'PNG')
        print('PNG created')

        return (encoded_string)

@app.route("/")
def main():
    return data

if __name__ == "__main__":
    threading.Thread(target=app.run).start()