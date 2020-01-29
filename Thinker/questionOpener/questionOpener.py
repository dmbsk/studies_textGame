import json
import os.path


def openQuestionsJson(filepath):
    if os.path.isfile(filepath):
        if filepath.endswith('.json'):
            with open(filepath, encoding='utf-8') as file:
                data = json.load(file)
                return data['questions']
        print("Wrong file extension must be .json")
        return False
    else:
        print("%s cant be found" % filepath)
        return False
