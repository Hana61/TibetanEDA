# -*- coding: utf-8 -*-

# This simple app uses the '/translate' resource to translate text from
# one language to another.

# This sample runs on Python 2.7.x and Python 3.x.
# You may need to install requests and uuid.
# Run: pip install requests uuid

import os, requests, uuid, json

def translate(text, dst):
    key_var_name = 'TRANSLATOR_TEXT_RESOURCE_KEY'
    if not key_var_name in os.environ:
        raise Exception('Please set/export the environment variable: {}'.format(key_var_name))
    resource_key = os.environ[key_var_name]

    region_var_name = 'TRANSLATOR_TEXT_REGION'
    if not region_var_name in os.environ:
        raise Exception('Please set/export the environment variable: {}'.format(region_var_name))
    region = os.environ[region_var_name]

    endpoint_var_name = 'TRANSLATOR_TEXT_ENDPOINT'
    if not endpoint_var_name in os.environ:
        raise Exception('Please set/export the environment variable: {}'.format(endpoint_var_name))
    endpoint = os.environ[endpoint_var_name]

    # If you encounter any issues with the base_url or path, make sure
    # that you are using the latest endpoint: https://docs.microsoft.com/azure/cognitive-services/translator/reference/v3-0-translate
    path = '/translate?api-version=3.0'
    # params = '&from=%s&to=%s' % (src, dst)
    params = '&to=%s' % (dst)
    constructed_url = endpoint + path + params

    headers = {
        'Ocp-Apim-Subscription-Key': resource_key,
        'Ocp-Apim-Subscription-Region': region,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    # You can pass more than one object in body.
    body = [{
        'text' : text
    }]
    request = requests.post(constructed_url, headers=headers, json=body)
    response = request.json()

    return response[0]['translations'][0]['text']

if __name__ == '__main__':
    print(translate('འཛམ་གླིང་བཀྲ་ཤིས་བདེ་ལེགས།', 'zh'))