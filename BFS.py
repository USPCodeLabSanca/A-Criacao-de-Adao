import requests
import os

headers = {
    "Authorization": f"Bearer {os.environ['API_BEARER'].strip()}"
}

# https://api.twitter.com/2/users/by?username=sdjalsdjsajd
# header 'authorization: OAuth oauth_consumer_key="CONSUMER_API_KEY", 
# oauth_nonce="OAUTH_NONCE", oauth_signature="OAUTH_SIGNATURE", 
# oauth_signature_method="HMAC-SHA1", 
# oauth_timestamp="OAUTH_TIMESTAMP", 
# oauth_token="ACCESS_TOKEN", oauth_version="1.0"

data = requests.get('https://api.twitter.com/2/users/by/username/bermudesviana', headers=headers)
data = data.json()
#print(data)
#print(data['data']['id'])
seguindo = requests.get(f"https://api.twitter.com/2/users/{data['data']['id']}/following", headers=headers)
seguindo = seguindo.json()
dataList = seguindo['data']


for index in range(len(dataList)):

    
    for key in dataList[index]:
        if key == 'username':
            print(dataList[index][key])





'''

A partir do A:

Fila = {
    
}

graph = {
	'A' = {'B', 'C', 'D'},
    'B' = {}
    'C' = {'G'}
    'D' = {'H'}
    'G' = {}
    'H' = {'J'}
    'J' = {}
}

Visitados = {
    'A', 'B', 'C', 'D', 'G', 'H', 'J'
}


A partir do J:

Fila = {
    'J'
}

graph = {
	'H' = {'J'}
    'I' = {'J'}
}

Visitados = {
    'J',
}

Fazer com que o J seja o mais famoso









seguindo['data']

{
    'data': 
    [
        {
            'id': '218229279', 
            'name': 'MTST', 
            'username': 'mtst'
        },
        {},
        {}
    ], 
    'meta': {
        'result_count': 100, 
        'next_token': '2HI1VVQ14O71GZZZ'
    }
}

'''