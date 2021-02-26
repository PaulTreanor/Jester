import os
import time
from flask import Flask, request, abort
from get_class import getClass

api = Flask(__name__)
upload_path = 'C:\\Users\\trean\\Desktop\\College\\4YP\\2021-ca400-ptreanor-cgorman\\src\\server-side\\classifier\\uploads'

@api.route("/<filename>", methods=["POST"])
def post_file(filename):
	"""Upload a file."""

	if "/" in filename:
		# Return 400 BAD REQUEST
		print(filename)
		abort(400, "no subdirectories allowed")

	file = request.files['file']
	file.save('./uploads/cool.png')
	classification = getClass(upload_path)
	# 201 CREATED
	return classification, 201

@api.route("/")
def test_connection():
	return "Connection OK", 200

if __name__ == "__main__":
	api.run(host='0.0.0.0', debug=True, port=5000)