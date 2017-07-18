from package.iotools import *

a_dict = {1: 2, "a": True, "Foo": [1, "bar"]}
a_file = 'test.json'

print("Sending {a_dict} to {a_file}".format(a_dict=a_dict, a_file=a_file))
print("Success" if dict2json(a_dict, a_file, file_perms='w+') else "Failure")

print("Reading it back into a dict")
print("Success" if json2dict(a_file) else "Failure")

a_list = [
    [1, 2, 3],
    ["a", "b", "c"],
    [1,
     ["Foo", "Bar"]]
]
a_file = 'test.csv'

print("Sending {a_list} to {a_file}".format(a_list=a_list, a_file=a_file))
print("Success" if list_array2csv(a_list, a_file, file_perms='w+') else "Failure")

print("Reading csv back into list")
print("Success" if csv2list_array(a_file, delimiter=',') else "Failure")

a_list_of_dicts = [
    {"first_name": "Robberto (the 3rd)", "last_name": "Bobbert", "age": 20},
    {"first_name": "Steve", "last_name": "Stevenson", "age": -1},
    {"first_name": "Alice", "last_name": "Alison", "age": 300},
]
a_nother_file = 'test2.csv'

print("Sending {dict_list} to {file}".format(dict_list=a_list_of_dicts, file=a_nother_file))
print("Success" if dicts2csv(a_list_of_dicts, a_nother_file, write_headers=True) else "Failure")

print("Reading csv back into list of dicts")
print("Success" if csv2dicts(a_nother_file) else "Failure")
