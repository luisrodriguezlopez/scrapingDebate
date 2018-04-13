import requests
import json
import bs4
from bs4 import BeautifulSoup
from flask import Flask, jsonify
from flask import make_response
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait

app = Flask(__name__)

@app.route('/gethot', methods=['GET'])
def get_hot():
    return get_news()

@app.route('/getrising', methods=['GET'])
def get_rising():
    return get_news('rising/')

@app.route('/gettop', methods=['GET'])
def get_top():
    return get_news('top/')

@app.route('/r/<string:subreddit>', methods=['GET'])
def get_funny(subreddit):
    return get_news('r/'+subreddit+'/',1)

def get_news(category='',cattype=0):
    URL = "https://www.debate.com.mx/seccion/policiaca/"
    browser = webdriver.Firefox()
    browser.get("https://www.debate.com.mx/seccion/policiaca/")
    elem = browser.find_element_by_class_name("entry-take-part")
    time.sleep(5)
    elem.click();


    req = requests.get(URL)
    ret = []
    html = BeautifulSoup(req.text, "html.parser")
    articles  = html.find_all('article' , {'class' : 'entry entry-box entry2 col col4 blue '})
    for article in articles:
        ret.append(article.find('h1').get_text())
#        elem.click();

    return json.dumps(ret)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(debug=True)



