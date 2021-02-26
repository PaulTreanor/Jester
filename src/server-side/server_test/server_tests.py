import os
import requester#
import requests

API_URL = 'http://192.168.43.219:5000/'

def test_connection():
	r = requests.get(API_URL)
	assert r.status_code == 200

def test_ood_image():
	filename = 'test_image1.jpg'
	r = requester.post_file(filename)
	assert r.status_code == 201 and r.text == "OOD"

def test_gesture_image():
	filename = 'test_image2.jpg'
	r = requester.post_file(filename)
	assert r.status_code == 201 and r.text == "palm"

def test_400_error():
	filename = 'test_text.txt'
	r = requester.post_file(filename)
	assert r.status_code == 422
