import os, json

from flask import Flask, request, Response, jsonify, json
from flask import render_template, url_for, redirect, send_from_directory
from flask import make_response, abort, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename

# from project import app
# from project.core import db


# from cbir.indexing import Indexing
# from cbir.colordescriptor import ColorDescriptor
# from cbir.searcher import Searcher
# from cbir.search import Search

# from multiband.mband_img_cluster import MultibandImageCluster as MIC
from pyt.mband_img_cluster import MultibandImageCluster as MIC
from multiband.mband_img_cluster import MultibandImageCluster as MIC2
# from sklearn.cluster import AgglomerativeClustering

# Web Profile
@app.route('/')
def index():
    return render_template('index.php', title="julioTA")


# # Sepatumu Image Search
# @app.route('/nyareh-helm/')
# def sepatu_image():
#     return render_template('sepatumu/image.html', title="Gambar Helm")

@app.route('/features/')
def features():
    data = None
    with open('dataset_features.json') as f:
        data = json.load(f)
        f.close()

    return render_template('sepatumu/features.html', title="Fitur Gambar", data=data)

@app.route('/process_features/')
def process_features():
    indexer = Indexing.indexer()

    return redirect('/features/')

@app.route('/result', methods=['GET', 'POST'])
def image_result():
    result = None
    if request.method == 'POST':
        
        f = request.files['search']
        name = secure_filename(f.filename)
        img = f.read()

        print(img)
        
        result, query = Search.query_search(img, name)
    return render_template('sepatumu/result_image.html', title=name, data=result, query=query['query'])


    # Multiband Image Clustering
@app.route('/multiband/')
def multiband():
    cluster, cluster_img, result_img = [], [], []

    for i in range(2, 7):
        cluster.append(i)
        cluster_img.append(url_for('static', filename='multiband/cluster' + str(i) + '.jpg'))
        result_img.append(url_for('static', filename='multiband/result-multiband' + str(i) + '.jpg'))

    return render_template('multiband/index.html', title='Multiband Image Clustering', cluster=cluster, clusterimg=cluster_img, resultimg=result_img)

@app.route('/multiband/process/')
def process_mic():
    try:
        app = MIC('project/static/landsat7/')
        image = app.read_images()
        features = app.feature_space_transformation(image)
        feature_copy = features.copy()
        for i in range(2, 7):
            label = app.KMeans_clustering(features, cluster=i, iteration=100)
            app.image_creation(feature_copy, features, label, cluster=i)\
  
    except RuntimeError:
        print('runtime error')

    return redirect(url_for('multiband'))