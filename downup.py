import json
from pprint import pprint

def read_config():
	with open('config.json') as data_file:
		data = json.load(data_file)
	pprint(data)