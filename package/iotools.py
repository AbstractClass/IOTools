import json
import csv


"""Factory function
    Generic file opener, executes a given function against the file object
    It's goal is to remove the try/except and 'with open()' boilerplate
"""


def file_io(file, permissions, io_function, print_err=True):
    assert callable(io_function)

    try:
        with open(file, permissions) as target:
            result = io_function(target)

            return result if result else 1

    except Exception as e:
        if print_err:
            print("I/O Error: ", e)

        return 0


"""
    All of the below functions are simple applications of the above factory.
    I chose these conversions because they are the easiest and IMO the most common.
"""


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


def csv2dicts(csv_file, delimiter=','):
    _read_csv = lambda target: [row for row in csv.DictReader(target, delimiter=delimiter)]

    return file_io(csv_file, 'r', _read_csv)


# If headers is left unspecified, the first dicts key will be used as the fieldnames
def dicts2csv(list_of_dicts, csv_file, file_perms='w', headers=None, delimiter=',', write_headers = False):
    def _write_csv(target, head=headers, dict_list=list_of_dicts, delim=delimiter, w_headers=write_headers):
        if not head:
            head = dict_list[0].keys()

        writer = csv.DictWriter(target, fieldnames=head, delimiter=delim)
        if w_headers:
            writer.writeheader()

        writer.writerows(dict_list)

    return file_io(csv_file, file_perms, _write_csv)
