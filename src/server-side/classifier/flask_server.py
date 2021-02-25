import os
import time
from flask import Flask, request, abort


api = Flask(__name__)


@api.route("/<filename>", methods=["POST"])
def post_file(filename):
	"""Upload a file."""

	if "/" in filename:
		# Return 400 BAD REQUEST
		print(filename)
		abort(400, "no subdirectories allowed")

	file = request.files['file']
	file.save('cool.png')

	# 201 CREATED
	return "it worked!", 201


if __name__ == "__main__":
	api.run(debug=True, port=5000)