# 请使用python3
import requests
import json


def PMapi(data):
    url = "http://www.medicalqa.xyz:8894/PMapi/NER_REL_POST"
    headers = {'Content-Type': 'application/json'}
    json_data = json.dumps(str(data))
    request = requests.post(url, data=json_data, headers=headers)
    response = request.json()
    return response


if __name__ == '__main__':
    # 待处理文本
    data = "1Hepatocellular carcinoma (HCC) is a primary tumor of the liver that usually develops in the setting of chronic liver disease"
    response = PMapi(data)
    print('='*10, '实体识别结果', '='*10)
    print(response['entity_list'])
    print('='*10, '关系抽取结果', '='*10)
    print(response['triple_list'])
