<<<<<<< HEAD
from flask import Flask,render_template,redirect
import pytube
=======
from flask import Flask
from flask import render_template, redirect, request, session,url_for,Response
>>>>>>> 6b359dac4da4673bcb4312c268d0f685bb6a8fb1

app = Flask(__name__)

def down():
	link = "https://www.youtube.com/watch?v=mpjREfvZiDs"
	yt = pytube.YouTube(link)
	stream = yt.streams.first()
	stream.download("../Downloads")

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/download")
def download():
	# Run download.py file
	down()
	return redirect("/")

if __name__ == "__main__":
	app.run(debug=True)