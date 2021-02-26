import requests

API_URL = 'http://192.168.43.105:5000/'


def post_file(filename):
	files = {'file': open(filename, 'rb')}
	r = requests.post(API_URL + filename, files=files)
	print(r.status_code)
	print(r.text)


if __name__ == "__main__":
	# Test connection
	r = requests.get(API_URL)
	print(r.status_code, r.text)
	# Send file
	filename = 'image.png'
	post_file(filename)