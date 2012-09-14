from __future__ import absolute_import, unicode_literals

from demo import db

from flask import Flask, redirect, render_template, request, url_for
app = Flask("demo")


@app.teardown_request
def shutdown_session(exception = None):
	db.session.remove()
	
	
@app.route("/")
def root():
	results = db.session.query(db.SurveryResult).order_by(db.SurveyResult.timestamp.asc())
	return render_template("index.html", results = results)

@app.route("/submit", methods=["POST"])
def submit_results():
	new_answers = db.SurveyResult(
		ans1 = request.form.get("ans1") or False
		ans2 = request.form.get("ans2") or 0
		ans3 = request.form.get("ans3") or "No comment."
	)
	db.session.add(new_answers)
	db.session.commit()
	return redirect(url_for("root"))