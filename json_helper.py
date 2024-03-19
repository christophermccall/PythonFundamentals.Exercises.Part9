import os
import logging
import json
import pickle
def read_json(json_file):
    try:
        with open(json_file) as file:
            json_reader = json.load(file)
            json_object = json.dumps(json_reader)
            return json_object
    except FileNotFoundError as e:
        print("that didn't work,man")
        logging.error(e)


def read_all_json_files(file_path):
    #file_path = "/Users/chris/pyprojects/PythonFundamentals.Exercises.Part9/data/super_smash_bros/"
    json_files = os.listdir(file_path)
    print(json_files)
    json_list = []
    for file in json_files:
        json_list += [read_json(os.path.join(file_path, file))]
    return json_list


def write_pickle(file_path, create_pickle_file, json_data):
    try:
        with open(os.path.join(file_path, create_pickle_file), 'w') as pickle:
            for file in json_data:
                pickle.writelines(file+'\n')
    except EncodingWarning:
        print("cannot write encoded data")


def load_pickle(pickle_file):
    pickle_jar = ''
    try:
        with open(pickle_file) as file:
            for line in file:
                pickle_jar += line
            return pickle_jar
    except FileNotFoundError as e:
        print("that didn't work,man")
        logging.error(e)

        #     print(os.listdir(branch))
        # elif os.path.isfile(branch):
        #     print(branch)




    # try:
    #     with open("/Users/chris/pyprojects/PythonFundamentals.Exercises.Part9/data/super_smash_bros/") as file:
    #         json_reader = json.load(file)
    #
    #         json_object = json.dumps(json_reader)
    #         return json_object
    # except FileNotFoundError as e:
    #     print("that didn't work,man")
    #     logging.error(e)


# print(os.path.abspath("json_helper.py"))
# for item in os.listdir():
#     if os.path.isdir(item):
#        files = os.listdir()
# print(os.path.abspath("link.json"))
#
# read_all_json_file()
# print(os.listdir("/Users/chris/pyprojects/PythonFundamentals.Exercises.Part9/"))
#print(read_json("/Users/chris/pyprojects/PythonFundamentals.Exercises.Part9/data/super_smash_bros/mario.json"))
#print(read_all_json_files("/Users/chris/pyprojects/PythonFundamentals.Exercises.Part9/data/super_smash_bros/"))
#json_files = "/Users/chris/pyprojects/PythonFundamentals.Exercises.Part9/data/super_smash_bros/"
#write_pickle("/Users/chris/pyprojects/PythonFundamentals.Exercises.Part9/", "super_smash_characters.pickle", read_all_json_files(json_files))
#pickle_load_test =load_pickle('/Users/chris/pyprojects/PythonFundamentals.Exercises.Part9/super_smash_characters.pickle')
#print(pickle_load_test)
