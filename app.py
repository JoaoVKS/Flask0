import requests
from bs4 import BeautifulSoup
from flask import Flask, session, url_for, redirect, render_template, request, abort, flash
app = Flask(__name__)

@app.route("/")
def page_index():
    return render_template("index.html", html="")

@app.route("/f1live")
def page_f1live():
    url = "https://f1.tfeed.net/live"
    html_content = requests. get(url).text
    return render_template("index.html", html=html_content)