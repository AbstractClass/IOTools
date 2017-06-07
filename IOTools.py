__author__ = "Connor MacLeod"
__github__ = "https://github.com/AbstractClass/IOTools"
__version__ = "0.1"


import json
import csv


def file_io(file, permissions, io_function):
    try:
        with open(file, permissions) as target:
            result = io_function(target)

            return result if result else 1

    except Exception as e:
        print("I/O Error: ", e)

        return 0


def json2dict(json_file):
    return file_io(json_file, 'r', json.load)


def dict2json(a_dict, json_file, file_perms='w'):
    write_json = lambda target: json.dump(a_dict, target)

    return file_io(json_file, file_perms, write_json)


def csv2list_array(csv_file, delimiter=','):
    def _read_csv(target, delim=delimiter):
        reader = csv.reader(target, delimiter=delim)
        return [row for row in reader]

    return file_io(csv_file, 'r', _read_csv)


def list_array2csv(list_array, csv_file, file_perms='w', delimiter=','):
    def _write_csv(target, delim=delimiter):
        writer = csv.writer(target, delimiter=delim)
        for row in list_array:
            writer.writerow(row)

    return file_io(csv_file, file_perms, _write_csv)

if __name__  == "__main__":
    a_dict = {1: 2, "a": True, "Foo": [1,"bar"]}
    a_file = 'test.json'

    print("Sending {a_dict} to {a_file}".format(a_dict=a_dict, a_file=a_file))
    print("Success" if dict2json(a_dict, a_file, file_perms='w+') else "Failure")

    print("Reading it back into a dict")
    print("Success" if json2dict(a_file) else "Failure")

    a_list = [
        [1,2,3],
        ["a", "b", "c"],
        [1,
         ["Foo", "Bar"]]
    ]
    a_file = 'test.csv'

    print("Sending {a_list} to {a_file}".format(a_list=a_list, a_file=a_file))
    print("Success" if list_array2csv(a_list, a_file, file_perms='w+') else "Failure")

    print("Reading csv back into list")
    print("Success" if csv2list_array(a_file, delimiter=',') else "Failure")