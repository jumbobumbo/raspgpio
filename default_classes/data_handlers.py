class HandleData:

    @staticmethod
    def dict_to_value_list(dict_1):
        """ feed it a dict, returns a list of the values"""
        value_list = []
        for key, value in dict_1.items():
            value_list.append(value)
        return value_list
