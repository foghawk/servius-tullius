from __future__ import absolute_import, unicode_literals

from demo import db

from flask import Flask, redirect, render_template, request, url_for
app = Flask("demo")


@app.teardown_request
def shutdown_session(exception = None):
	db.session.remove()
	
	
@app.route("/")
def root():
    return render_template("index.html")
