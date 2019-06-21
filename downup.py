import json
import requests
import pprint as pprint
import objectpath

get = []
ping = []


def read_config():
    with open('config.json') as data_file:
        data = json.load(data_file)

    if pprint.isreadable(data):
        print('read config file')
    # print(pprint.pformat(data))

    for (x, y) in data.items():
        if x == 'http.get':
            for (z,a) in y.items():
                for b in a.items():
                    get.append(b[1])

            # for a in z[]:
            # print(a)
        if x == 'ping':
            for (z, a) in y.items():
                for b in a.items():
                    ping.append(b[1])


def run():
    with open("config.json") as datafile:
        data = json.load(datafile)
    jsonnn_tree = objectpath.Tree(data['http.get'])
    result_tuple = tuple(jsonnn_tree.execute('$..duration'))
    print(result_tuple)

# read_config()
run()
