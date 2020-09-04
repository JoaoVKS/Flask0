from flask import Flask, session, url_for, redirect, render_template, request, abort, flash
app = Flask(__name__)

@app.route("/")
def page_index():
    return render_template("index.html")

@app.route("/fretes")
def page_fretes():
    return 'PAREI AQUI'