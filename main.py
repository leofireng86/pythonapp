import requests
import json
import random
import string

url = "https://3auvqg06yk.execute-api.ap-southeast-1.amazonaws.com/test/student"

randomString = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))


data = {'name': 'student-'+randomString,
        'description':'description-'+randomString}

dataJSON = json.dumps(data).encode('utf8')

r = requests.post(url=url, data = dataJSON)

print(r.text)