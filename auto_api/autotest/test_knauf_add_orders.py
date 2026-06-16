import requests
import unittest
import json


class TestTenders(unittest.TestCase):

    def test_get_list_tenders(self):

        base_url = 'https://api-tms-master.stage.trucker.group/cargo_owner_api/v1/ac8326d4-1115-4a38-b64a-942ba0d2fce1/tenders'
        token = ''

        result = requests.get(base_url, headers={'Authorization': token})
        check_joke = result.json()

        print(f'Статус-код: {result.status_code}')
        self.assertEqual(result.status_code, 200, 'ОШИБКА, Статус-код не совпадает')
        print('Статус-код корректен')

        self.assertIsInstance(check_joke, list)
        print(f'Всего тендеров: {len(check_joke)}')

        self.assertGreater(len(check_joke), 0, 'Список тендеров пустой')
        first_tender = check_joke[0]
        print(f'Последний тендер: {first_tender.get("name")}')

        print('\n======')
        print(json.dumps(result.json(), indent=2, ensure_ascii=False))
        print('======\n')