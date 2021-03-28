import os
import requests
import pytest 
import socket

LOCAL_IP_ADDRESS = socket.gethostbyname(socket.gethostname())
API_URL = 'http://'+LOCAL_IP_ADDRESS+':5000/'

# Status codes 
OK_STATUS_CODE = 200
SUCCESS_STATUS_CODE = 201
FILETYPE_ERROR_STATUS_CODE = 422

def post_file(filename, filepath="./"):
	files = {'file': open(filepath+filename, 'rb')}
	r = requests.post(API_URL + filename, files=files)
	print(r.status_code)
	print(r.text)
	return r

def test_connection():
	r = requests.get(API_URL)
	assert r.status_code == OK_STATUS_CODE

def test_ood_image():
	filepath = "C:\\Users\\trean\\Desktop\\College\\4YP\\2021-ca400-ptreanor-cgorman\\src\\server-side\\test-images\\ood/"
	filename = 'image.jpg'
	r = post_file(filename, filepath)
	assert r.status_code == SUCCESS_STATUS_CODE and r.text == "OOD"


def test_gesture_image():
	filepath = "C:\\Users\\trean\\Desktop\\College\\4YP\\2021-ca400-ptreanor-cgorman\\src\\server-side\\test-images\\alt-palm/"
	filename = 'image.jpg'
	r = post_file(filename, filepath)
	assert r.status_code == SUCCESS_STATUS_CODE and r.text == "palm"

def test_400_error():
	filename = 'test_text.txt'
	r = post_file(filename)
	assert r.status_code == FILETYPE_ERROR_STATUS_CODE

if __name__ == "__main__":
	# Test connection
	r = requests.get(API_URL)
	print(r.status_code, r.text)
	# Send file
	filepath = "C:\\Users\\trean\\Desktop\\College\\4YP\\2021-ca400-ptreanor-cgorman\\src\\server-side\\test-images\\alt-palm/"
	filename = 'image.jpg'
	post_file(filename, filepath)

