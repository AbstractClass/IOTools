__author__ = "Connor MacLeod"
__github__ = "https://github.com/AbstractClass/IOTools"
__version__ = "0.1"


import json
import csv


# Get it?  handdle-err?  I am so funny.
def handle_err(function):
    def handle_problem():
        try:
            function()

        except Exception as e:
            print("Error: ", e)

            return 0

    return handle_problem()


@handle_err
def file_io(file, permissions, io_function):
    with open(file, permissions) as target:
        return io_function(target)


def json2dict(json_file):
    file_io(json_file, 'r', json.loads)


def dict2json(a_dict, json_file, file_perms='w'):
    file_io(json_file, file_perms, lambda x: json.dump(a_dict, x))


def csv2list_array(csv_file):
    pass



def list_array2csv(list_array, csv_file, file_perms='w'):
    pass