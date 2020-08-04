from Actions.variuos_functions import VariousFunctions, random
from uuid import uuid4
import json
import lorem
from datetime import datetime

various_functions = VariousFunctions()
date_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


class DeviceActions:

    def create_ms_system(self):
        device_id = various_functions.random('Device_')
        service_point = various_functions.random('ServicePoint_')

        json_data = {
            "owner": {
                "hes": "AMRDEF",
                "owner": "ALL",
                "guidFile": str(uuid4())
            },
            "device": [
                {
                    "brand": "Elster",
                    "model": "EAGas",
                    "deviceCategory": "METER",
                    "deviceId": device_id,
                    "deviceDescription": str(lorem.sentence()),
                    "deviceStatus": "ENABLE",
                    "deviceComments": str(lorem.sentence()),
                }
            ],
            "servicePoint": [
                {
                    "servicePointId": service_point,
                    "servicePointDescription": str(lorem.sentence())
                }
            ],
            "relationDevice": [
                {
                    "servicePointId": service_point,
                    "deviceId": device_id,
                    "meteringType": "MAIN",
                    "relationStartDate": str(date_now),
                    "relationEndDate": ""
                }
            ]
        }
        various_functions.create_json(json_data, './Data/device_structure.json')
        return json.dumps(json_data, indent=4)

    def update_ms_system(self):
        with open('./Data/device_details.json', 'r') as json_file:
            json_data = json.load(json_file)
            json_file.close()

        device_id = json_data['device_id']
        service_point = json_data['service_point']

        json_data = {
            "owner": {
                "hes": "AMRDEF",
                "owner": "ALL",
                "guidFile": str(uuid4())
            },
            "device": [
                {
                    "brand": "Elster",
                    "model": "EAGas",
                    "deviceCategory": "METER",
                    "deviceId": device_id,
                    "deviceDescription": str(lorem.sentence()),
                    "deviceStatus": "ENABLE",
                    "deviceComments": str(lorem.sentence()),
                }
            ],
            "servicePoint": [
                {
                    "servicePointId": service_point,
                    "servicePointDescription": str(lorem.sentence())
                }
            ]
        }
        various_functions.create_json(json_data, './Data/device_structure.json')
        return json.dumps(json_data, indent=4)

    def profile_variable(self, service_point):
        self.service_point = service_point
        variable_id = various_functions.random('Variable_')
        custom_name = various_functions.random('CustomName_')

        json_data = {
            "owner": {
                "hes": 'AMRDEF',
                "owner": "PRIME",
                "guidFile": str(uuid4())
            },
            "servicePointVariable": [
                {
                    "readingType": "LOAD PROFILE READING",
                    "variableId": variable_id,
                    "customName": custom_name,
                    "servicePointId": self.service_point,
                    "meteringType": "MAIN",
                    "unitOfMeasure": random.randint(1, 74),
                    "channel": random.randint(1, 250),
                    "intervalSize": random.randint(1, 15),
                    "logNumber": 1
                }
            ]
        }
        various_functions.create_json(json_data, './Data/variable_structure.json')
        return json.dumps(json_data, indent=4)

    def update_profile_variable(self):
        with open('./Data/variable_details.json', 'r') as json_file:
            json_data = json.load(json_file)
            json_file.close()

        variable_id = json_data['variable_id']
        custom_name = various_functions.random('CustomName_')

        json_data = {
            "owner": {
                "hes": 'AMRDEF',
                "owner": "PRIME",
                "guidFile": str(uuid4())
            },
            "servicePointVariable": [
                {
                    "readingType": "LOAD PROFILE READING",
                    "variableId": variable_id,
                    "customName": custom_name,
                    "servicePointId": self.service_point,
                    "meteringType": "MAIN",
                    "unitOfMeasure": random.randint(1, 74),
                    "channel": random.randint(1, 250),
                    "intervalSize": random.randint(1, 15),
                    "logNumber": 1
                }
            ]
        }
        various_functions.create_json(json_data, './Data/variable_structure.json')
        return json.dumps(json_data, indent=4)


