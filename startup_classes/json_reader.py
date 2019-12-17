import json


class JSONReads:
    def __init__(self, json_file):
        self.json_data = json_file

    @property
    def json_data(self):
        return self.__json_data

    @json_data.setter
    def json_data(self, json_file):
        with open(json_file, "r") as f:
            self.__json_data = json.load(f)

    # TODO: BE SMARTER
    def finder(self, key1, key2=None):
        """
        key1: key
        key2: None - key
        :return: value
        """
        if not key2:  # one value provided
            return self.json_data[key1]
        else:  # looking for a nest
            return self.json_data[key1][key2]
