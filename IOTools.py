__author__ = "Connor MacLeod"
__github__ = "https://github.com/AbstractClass/IOTools"
__version__ = "0.1"


import json
import csv
import sys


def json2dict(json_file):
    try:
        with open(json_file, 'r') as json_str:
            a_dict = json.load(json_str)

        return a_dict

    except Exception as e:
        print("Error could not open {file}: {err}".format(file=json_file, err=e))

        return {"Error": e}


def dict2json(a_dict, json_file, file_perms='w'):
    try:
        with open(json_file, file_perms) as file:
            file.write(json.dumps(a_dict))

        return 1

    except Exception as e:
        print("Error could write to {file}: {err}".format(file=json_file, err=e))

        return 0
