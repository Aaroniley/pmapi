# 请使用python3
import requests
import json


def PMapi(data):
    url = "http://www.medicalqa.xyz:19999/qa"
    headers = {'Content-Type': 'application/json'}
    json_data = json.dumps(data)
    request = requests.post(url, data=json_data, headers=headers)
    response = request.json()
    return response


if __name__ == '__main__':
    # 待处理文本
    data = {'query':'国家生物防御战略'}
    response = PMapi(data)
    for i in response['content']:
        print(i['_source']['Title'])
