import json


class JSONReads:

    @staticmethod
    def reader(json_file):
        """
        reads the self.json_file and
        :return: json data
        """
        with open(json_file, "r") as jf:
            js_data = json.load(jf)  # read the data
            return js_data

    @staticmethod
    def finder(js_data, key1, key2=None):
        """
        finds the ip addr in the json data
        key1: str
        key2: None - str
        :return: ip addr value
        """
        if not key2:  # one value provided
            return js_data[key1]
        else:  # looking for a nest
            return js_data[key1][key2]
