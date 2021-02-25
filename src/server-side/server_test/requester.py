import requests

API_URL = 'http://127.0.0.1:5000/'


def post_file(filename):
	files = {'file': open(filename, 'rb')}
	r = requests.post(API_URL + filename, files=files)
	print(r.status_code)
	print(r.text)


if __name__ == "__main__":
	filename = 'image.png'
	post_file(filename)