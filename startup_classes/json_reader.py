import json


class JSONReads:
    """
    Example: JSONReads(json_file).json_data["connection"]["ip_add"]
    """
    def __init__(self, json_file):
        """
        json_file: Path OBJ to file
        """
        self.json_data = json_file

    @property
    def json_data(self):
        return self.__json_data

    @json_data.setter
    def json_data(self, json_file):
        with open(json_file, "r") as f:
            self.__json_data = json.load(f)
