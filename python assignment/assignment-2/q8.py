# 8. Access the nested key ‘salary’ from the following JSON

import json

sampleJson = '''{
    "company":{
        "employee01":{
            "name":"Bittu",
            "payable":{
                "salary":7000,
                 "bonus":800
            }
        },
         "employee02":{
            "name":"Pitambar",
            "payable":{
                "salary":8000,
                 "bonus":900
            }
        },
         "employee03":{
            "name":"Bhadra",
            "payable":{
                "salary":9000, 
                "bonus":1000
            }
        }
    }
}'''


def salary_acc(data):
    for i,first in data.items():
        for p,second in first.items():
            print(second['payable']['salary'])


data = json.loads(sampleJson)
salary_acc(data)

