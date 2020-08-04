import requests
import json
from uuid import uuid4
from Actions.device_actions import DeviceActions
from Actions.variuos_functions import VariousFunctions
import allure

device = DeviceActions()
various_functions = VariousFunctions()

headers_data = {'Content-type': 'application/json',
                'Transaction-Id': str(uuid4()),
                'Owner': 'PRIME',
                'User-Id': 'PRIME'
                }

response_code = {
    200: "OK",
    201: "Created",
    204: "No Content",
    304: "Not Modified",
    400: "Bad Request",
    401: "Unauthorized",
    403: "Forbidden",
    404: "Not Found",
    409: "Conflict",
    500: "Internal Server Error"
}


class ApiActions:

    def put_api_url(self, api_url):
        """Inserta la url del endpoint a ser usado"""
        self.api_url = api_url

        data = {
            'apiUrl': api_url
        }

        various_functions.create_json(data, './Data/config.json')

    def obtain_url(self):
        """Obtiene la url del endpoint configurado en el archivo json"""
        with open('./Data/config.json', 'r') as json_file:
            json_data = json.load(json_file)
            json_file.close()
            return json_data['apiUrl']

    def create_device(self):
        """Crea el dispositivo con sus respectivas asociaciones"""
        device_structure = device.create_ms_system()
        response = requests.post(self.obtain_url(), device_structure, headers=headers_data)
        response_dict = json.loads(response.text)

        data_response = {
            "device_id": response_dict['data']['relationDevice'][0]['deviceId'],
            "service_point": response_dict['data']['relationDevice'][0]['servicePointId'],
            "device_result": response_dict['data']['device'][0]['result'],
            "relation_result": response_dict['data']['relationDevice'][0]['result'],
            "device_response": response_dict['statusCode']
        }

        various_functions.create_json(response_dict, './Data/device_response.json')
        various_functions.create_json(data_response, './Data/device_details.json')

        allure.attach(open('./Data/device_structure.json', 'rb').read(), attachment_type=allure.attachment_type.JSON)

    def update_device(self):
        """Actualiza la descripción del punto de servicio y el dispositivo"""
        response = requests.post(self.obtain_url(), device.update_ms_system(), headers=headers_data)
        response_dict = json.loads(response.text)
        various_functions.create_json(response_dict, './Data/device_response.json')

        data_response = {
            "device_id": response_dict['data']['device'][0]['deviceId'],
            "service_point": response_dict['data']['servicePoint'][0]['servicePointId'],
            "device_result": response_dict['data']['device'][0]['result'],
            "service_result": response_dict['data']['servicePoint'][0]['result'],
            "device_response": response_dict['statusCode']
        }

        various_functions.create_json(data_response, './Data/device_details.json')

    def create_profile_variable(self):
        """Crea una variable de perfil asociada a un dispositivo"""
        with open('./Data/device_details.json', 'r') as json_file:
            json_data = json.load(json_file)
            json_file.close()

        service_point = json_data['service_point']

        response = requests.post(self.obtain_url(), device.profile_variable(service_point), headers=headers_data)

        response_dict = json.loads(response.text)

        various_functions.create_json(response_dict, './Data/variable_response.json')

        data_response = {
            "variable_dictionary_action": response_dict['data'][2]['action'],
            "variable_id": response_dict['data'][2]['entity_1_id'],
            "variable_custom_name": response_dict['data'][2]['entity_2_id'],
            "variable_result": response_dict['data'][2]['result'],
            "variable_response": response_dict['statusCode']
        }

        various_functions.create_json(response_dict, './Data/variable_response.json')
        various_functions.create_json(data_response, './Data/variable_details.json')

        allure.attach(open('./Data/variable_structure.json', 'rb').read(), attachment_type=allure.attachment_type.JSON)

    def update_profile_variable(self):
        """Actualiza una variable de perfil asociada a un dispositivo"""
        response = requests.post(self.obtain_url(), device.update_profile_variable(), headers=headers_data)

        response_dict = json.loads(response.text)

        various_functions.create_json(response_dict, './Data/variable_response.json')

        data_response = {
            "variable_dictionary_action": response_dict['data'][3]['action'],
            "variable_id": response_dict['data'][2]['entity_1_id'],
            "variable_custom_name": response_dict['data'][2]['entity_2_id'],
            "variable_result": response_dict['data'][2]['result'],
            "variable_response": response_dict['statusCode']
        }

        various_functions.create_json(data_response, './Data/variable_details.json')

    def evaluate_device_result(self, operation, expected_response):
        """Evalúa la respuesta recibida al momento de crear/actualizar un dispositivo"""
        self.operation = operation
        self.expected_response = expected_response

        with open('./Data/device_details.json', 'r') as json_file:
            json_data = json.load(json_file)
            json_file.close()

        allure.attach(open('./Data/device_response.json', 'rb').read(), attachment_type=allure.attachment_type.JSON)

        if json_data['device_response'] == 200:
            if self.operation == 'Create':
                if bool(json_data['device_result']) is True:
                    if bool(json_data['relation_result']) is True:
                        return 'Successful'
                    else:
                        return 'La asociación no pudo realizarse'
                else:
                    return json_data['device_result']
            elif self.operation == 'Update':
                if bool(json_data['device_result']) and bool(json_data['service_result']) is True:
                    return 'Successful'
                else:
                    return 'La actualización no pudo realizarse'
        else:
            return response_code[json_data['device_response']]

    def evaluate_variable_result(self, operation, expected_response):
        self.operation = operation
        self.expected_response = expected_response

        with open('./Data/variable_details.json', 'r') as json_file:
            json_data = json.load(json_file)
            json_file.close()

        allure.attach(open('./Data/variable_response.json', 'rb').read(), attachment_type=allure.attachment_type.JSON)

        if json_data['variable_response'] == 200:
            if self.operation == 'Create' and self.operation == json_data['variable_dictionary_action']:
                if json_data['variable_result'] == 'Successful':
                    return json_data['variable_result']
                else:
                    return json_data['variable_result']
            elif self.operation == 'Update' and self.operation == json_data['variable_dictionary_action']:
                if json_data['variable_result'] == 'Successful':
                    return json_data['variable_result']
                else:
                    return json_data['variable_result']
        else:
            return response_code[json_data['variable_response']]
