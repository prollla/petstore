import json

import allure

from conftest import base_url


@allure.title("Тестовый сценарий CRUD")
def test_post_add_new_pet_to_the_store(base_endpoint_fixture, headers):
    with allure.step("Добавление питомца в магазин"):
        with allure.step("Cоздание url запроса"):
            url = f'{base_url}/pet'
        with allure.step("Создание тела запроса"):
            data = {
                "id": 15,
                "category": {
                    "id": 15,
                    "name": "Anton"
                },
                "name": "doggie",
                "photoUrls": [
                    "string"
                ],
                "tags": [
                    {
                        "id": 15,
                        "name": "Anton"
                    }
                ],
                "status": "available"
            }
        with allure.step("Отправка запроса"):
            response_body = base_endpoint_fixture.post_request(url, headers, json.dumps(data))
        with allure.step("Проверка статус кода"):
            base_endpoint_fixture.check_status_code(200)
        with allure.step("Проверка заголовка"):
            base_endpoint_fixture.check_response_headers()
        with allure.step("Сравнение тела запроса и тела ответа"):
            base_endpoint_fixture.equals(data, response_body)
        with allure.step("Валидация тела ответа по json схеме"):
            base_endpoint_fixture.validate_json_schema(response_body)
    with allure.step("Обновление питомца в магазине"):
        with allure.step("Создание тела запроса"):
            data = {
                "id": 15,
                "category": {
                    "id": 15,
                    "name": "Anton"
                },
                "name": "doggie",
                "photoUrls": [
                    "string"
                ],
                "tags": [
                    {
                        "id": 15,
                        "name": "Anton"
                    }
                ],
                "status": "available"
            }
        with allure.step("Отправка запроса"):
            base_endpoint_fixture.put_request(url, headers, json.dumps(data))
        with allure.step("Проверка статус кода"):
            base_endpoint_fixture.check_status_code(200)
        with allure.step("Проверка заголовка"):
            base_endpoint_fixture.check_response_headers()
        with allure.step("Сравнение тела запроса и тела ответа"):
            base_endpoint_fixture.equals(data, response_body)
        with allure.step("Валидация тела ответа по json схеме"):
            base_endpoint_fixture.validate_json_schema(response_body)
        with allure.step("Получение ID питомца"):
            pet_id = base_endpoint_fixture.extract_id_from_response()
    with allure.step("Получение питомца по ID"):
        with allure.step("Создание url"):
            url = f'{base_url}/pet/{pet_id}'
        with allure.step("Отправка запроса"):
            response_body = base_endpoint_fixture.get_request(url, headers)
        with allure.step("Проверка статус кода"):
            base_endpoint_fixture.check_status_code(200)
        with allure.step("Проверка заголовка"):
            base_endpoint_fixture.check_response_headers()
        with allure.step("Сравнение тела запроса и тела ответа"):
            base_endpoint_fixture.equals(data, response_body)
    with allure.step("Удаление питомца по ID"):
        with allure.step("Отправка запроса"):
            base_endpoint_fixture.delete_request(url, headers)
        with allure.step("Проверка статус кода"):
            base_endpoint_fixture.check_status_code(200)
        with allure.step("Проверка заголовка"):
            base_endpoint_fixture.check_response_headers()
