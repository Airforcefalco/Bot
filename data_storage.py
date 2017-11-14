# -*- coding: utf-8 -*-
import json

def read_json(path):
	with open(path, 'r') as f:
		try:
			return json.load(f)
		except:
			pass

def writeto_json(path, data):
	with open(path, 'w') as f:
		try:
			json.dump(data, f)
		except:
			pass