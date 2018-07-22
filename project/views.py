import os
import numpy as np
import json
import base64
import cv2

from project import app
from matplotlib import pyplot as plt
from flask import Flask, render_template, request, url_for, redirect, send_from_directory, Response, session, Blueprint
from flask_uploads import UploadSet, configure_uploads, IMAGES
from pyt.detectBlur import Preprocessing
from pyt.metadata import Metadata

from project.session.controllers import check_login_session as check_login_session
from flask_login import LoginManager

photos = UploadSet('photos', IMAGES)

app.config['UPLOADED_PHOTOS_DEST'] = 'project/static/public/images/test/'
configure_uploads(app, photos)

# @app.route("/",methods=['GET','POST'])
# def index(name="phlox"):
	
#     return render_template('index.html', name=name)

@app.route("/",methods=['GET','POST'])
def index(name="phlox"):
	if check_login_session():
        # return "Sudah Login"
		return render_template('index.html', name=name)
	else:
		return redirect("/signin")
    # return render_template('index.html', name=name)

@app.route('/signin',methods=['GET','POST'])
def signin():
	if check_login_session() is False:
		if request.method == "GET":
			return render_template("login.html")
		else:
			if request.form['email'] == "julio@gmail.com" and request.form['password'] == "sapehkerrap123":
				session['email'] = request.form['email']
				return redirect("/")
			else:
				return render_template("login.html")
	else:
		return redirect("/")

@app.route('/logout',methods=['GET'])
def logout():
    session.pop('email')
    return redirect("/")

@app.route("/upload", methods=['POST'])
def upload(name="upload"):
	if request.method == 'POST':
		# namabaru = "upload.jpg"
		filename = photos.save(request.files['photo'])
		# filename = request.files['photo']
		# img = filename.read()
		# print (img)

		pre = Preprocessing()
		image = pre.readImages(filename)
		
		resize = pre.resize(image)
		height = np.size(resize, 0)
		width = np.size(resize, 1)
		
		gray = pre.filterGray(resize)
		blur = pre.filterGaus(gray)
		deteksiTepi = pre.sobel(blur)
		deteksiBlur = pre.blurDetection(deteksiTepi, height, width)

		med = Metadata()
		exposureTime, focalLength, ccd = med.exif(filename)

		img = open('project//static/public/images/test/resize.png', 'rb')
		f = img.read()
		dataOri = base64.b64encode(f)
		dataOri = dataOri.decode('utf-8')

		img2 = open('project//static/public/images/test/hasil.png', 'rb')
		f2 = img2.read()
		dataHasil = base64.b64encode(f2)
		dataHasil = dataHasil.decode('utf-8')
		return render_template('blur.html', panjangBlur = deteksiBlur, exposureTime = exposureTime, focalLength = focalLength, ccd = ccd, dataOri=dataOri, dataHasil=dataHasil)

@app.route("/result", methods=['GET', 'POST'])
def result(name="result"):
	if request.method=='GET':
		K=float(request.args.get('blur', ''))
		T=request.args.get('shutterSpeed', '')
		shutter1 = int(T[0])
		shutter2 = int(T[2:5])
		# print (shutter1)
		# print (shutter2)
		f=float(request.args.get('focalLength', ''))
		sx=float(request.args.get('ccd', ''))
		z=float(request.args.get('distance', ''))
		
		img = open('project//static/public/images/test/resize.png', 'rb')
		ftp = img.read()
		dataOri = base64.b64encode(ftp)
		dataOri = dataOri.decode('utf-8')

		v = round(
			((z*K*(sx/1000))/
				((shutter1/shutter2)*(f/1000))
				),1)
		v = round(v*3600/1000, 1)
		return render_template('result.html', kecepatan = v, dataOri=dataOri, blur=K)
	else:
		return "Not get method"

@app.route("/login")
def login(name="login"):
	return render_template("login.html")

@app.route("/hasil")
def hasil(name="hasil"):
	# kata = 'sayabcde'
	# ai = kata[2:5]
	# print (ai)
	return render_template("result.html")
	
@app.route("/chart")
def chart(name="chart"):
	return render_template("chart.html")

@app.route("/coba")
def coba(name="coba"):
	return render_template("hasil.html")