import json


class JSONReads:

    def __init__(self, json_file):
        self.json_file = json_file

    def reader(self):
        # TODO: ADD DOCSTRING
        with open(self.json_file, "r") as jf:
            js_data = json.load(jf)  # read the data
            return js_data
