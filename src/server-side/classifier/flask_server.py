import os
import time
from flask import Flask, request, abort
from get_class import getClass

api = Flask(__name__)
root_upload_path = 'C:\\Users\\trean\\Desktop\\College\\4YP\\2021-ca400-ptreanor-cgorman\\src\\server-side\\classifier\\uploads'

@api.route("/<filename>", methods=["POST"])
def post_file(filename):
	# Create new directory for each request (OpenPose only reads images)
	filename, fileExtension = os.path.splitext(filename)
	upload_path = root_upload_path + '/' + filename	
	os.mkdir(upload_path)

	file = request.files['file']
	file.save(upload_path +'/cool.png')
	classification = getClass(upload_path)

	# Delete directory
	os.rmdir(upload_path)
	# 201 CREATED
	return classification, 201

@api.route("/")
def test_connection():
	return "Connection OK", 200

if __name__ == "__main__":
	api.run(host='0.0.0.0', debug=True, port=5000)