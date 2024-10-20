import random
import string

import pytest
import requests
from jsonschema import validate


class BaseEndpoint:
    def __init__(self):
        self.response_json = None
        self.response = None

    def get_request(self, url, headers):
        self.response = requests.get(url, headers=headers, verify=False)
        self.response_json = self.response.json()
        return self.response_json

    def post_request(self, url, headers, data):
        self.response = requests.post(url, headers=headers, data=data, verify=False)
        self.response_json = self.response.json()
        return self.response_json

    def put_request(self, url, headers, data):
        self.response = requests.put(url, headers=headers, data=data, verify=False)
        self.response_json = self.response.json()
        return self.response_json

    def delete_request(self, url, headers):
        self.response = requests.delete(url, headers=headers, verify=False)
        self.response_json = self.response.json()
        return self.response_json

    def check_status_code(self, code):
        if self.response.status_code == code:
            pass
        else:
            pytest.fail(f'Error: {self.response.status_code}')

    def check_response_headers(self):
        if self.response.headers['Content-Type'] == 'application/json':
            pass
        else:
            pytest.fail(f'Error: Headers != application/json')

    def extract_id_from_response(self):
        return self.response_json.get('id')

    def equals(self, request, response):
        if request == response:
            pass
        else:
            pytest.fail("requset body != response body")

    def validate_json_schema(self, data):
        schema = {
            "type": "object",
            "properties": {
                "id": {"type": "integer"},
                "category": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "integer"},
                        "name": {"type": "string"}
                    },
                    "required": ["id", "name"]
                },
                "name": {"type": "string"},
                "photoUrls": {
                    "type": "array",
                    "items": {"type": "string"}
                },
                "tags": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "id": {"type": "integer"},
                            "name": {"type": "string"}
                        },
                        "required": ["id", "name"]
                    }
                },
                "status": {"type": "string"}
            },
            "required": ["id", "category", "name", "photoUrls", "tags", "status"]
        }

        # Валидация данных по схеме
        try:
            validate(instance=data, schema=schema)
            print("Данные валидны!")
        except Exception as e:
            print(f"Ошибка валидации: {e}")
