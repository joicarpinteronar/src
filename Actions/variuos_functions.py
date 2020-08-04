import random
import string
import json


class VariousFunctions:

    def random_string(self, string_size, chars=string.ascii_uppercase + string.digits):
        self.string_size = string_size
        final_string = ''.join(random.choice(chars) for i in range(string_size))
        return final_string

    def create_json(self, json_data, json_path):
        self.json_data = json_data
        self.json_path = json_path

        with open(self.json_path, 'w') as json_file:
            json.dump(self.json_data, json_file, indent=4)
            json_file.close()

    def random(self, pref):
        value = self.random_string(random.randint(5, 10))
        return pref + value
