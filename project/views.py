import os
import numpy as np
import json
import base64
import cv2

from project import app
from matplotlib import pyplot as plt
from flask import Flask, render_template, request, url_for, redirect, send_from_directory, Response
from flask_uploads import UploadSet, configure_uploads, IMAGES
from pyt.detectBlur import Preprocessing
from pyt.metadata import Metadata


photos = UploadSet('photos', IMAGES)

app.config['UPLOADED_PHOTOS_DEST'] = 'project/static/public/images/test/'
configure_uploads(app, photos)


@app.route("/")
def index(name="phlox"):
    return render_template('index.html', name=name)

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
		
		v = round(
			((z*K*(sx/1000))/
				((shutter1/shutter2)*(f/1000))
				),1)
		return render_template('result.html', kecepatan = v)
	else:
		return "Not get method"

@app.route("/student")
def student(name="student"):
	return render_template("student.html")

@app.route("/hasil")
def hasil(name="hasil"):
	kata = 'sayabcde'
	ai = kata[2:5]
	print (ai)
	return render_template("result.html")