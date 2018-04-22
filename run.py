import os
import numpy as np
from matplotlib import pyplot as plt

from flask import Flask, render_template, request
from flask_uploads import UploadSet, configure_uploads, IMAGES
from pyt.detectBlur import Preprocessing
from pyt.metadata import Metadata

app = Flask(__name__, static_url_path='') # create the application instance

photos = UploadSet('photos', IMAGES)

app.config['UPLOADED_PHOTOS_DEST'] = 'static/public/images'
configure_uploads(app, photos)


@app.route("/")
def index(name="phlox"):
    return render_template('index.html', name=name)

@app.route("/upload", methods=['GET', 'POST'])
def upload(name="upload"):
	if request.method == 'POST' and 'photo' in request.files:
		# namabaru = "upload.jpg"
		filename = photos.save(request.files['photo'])
		
		pre = Preprocessing()
		image = pre.readImages(filename)
		# print (image)
		resize = pre.resize(image)
		height = np.size(resize, 0)
		width = np.size(resize, 1)
		# print (height)
		gray = pre.filterGray(resize)
		blur = pre.filterGaus(gray)
		deteksiTepi = pre.sobel(blur)
		deteksiBlur = pre.blurDetection(deteksiTepi, height, width)
		# print (deteksiBlur)
		# return "asu"
		# return image

		med = Metadata()
		exposureTime, focalLength, ccd = med.exif(filename)
		return render_template('blur.html', panjangBlur = deteksiBlur, exposureTime = exposureTime, focalLength = focalLength, ccd = ccd)

@app.route("/result", methods=['GET', 'POST'])
def result(name="result"):
	if request.method=='GET':
		K=float(request.args.get('blur', ''))
		T=request.args.get('shutterSpeed', '')
		shutter1 = int(T[0])
		shutter2 = int(T[2:5])
		print (shutter1)
		print (shutter2)
		f=float(request.args.get('focalLength', ''))
		sx=float(request.args.get('ccd', ''))
		z=float(request.args.get('distance', ''))
		
		v = round((z*K*sx)/((shutter1/shutter2)*f),3)
		# return "Kecepatan objek : "+str(v)
		return render_template('result.html', kecepatan = v)
		# return "blur : "+a+" ,  shutterSpeed :  "+b+", focalLength : "+c+", ccd : "+d+", distance : "+e
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

if __name__ == "__main__":
    app.run(debug=True)