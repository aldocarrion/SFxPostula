import requests as rq
import json
import pandas
import pprint
from simple_salesforce import Salesforce



ck = '3MVG9xOCXq4ID1uFLDIihD8SFf9FJQwOFtAVVWV2r98uL4zSBeN5CRr0Rg6NfgsQUGtAHHnL2EaXh_ny.czHw'
cs = 'C1BB690B6EC810BFB3FD1C39EC3E359EF4EE760F9CE1B447D5D68DF3F0A708AA'


loginInfo =({
    "username" : "aldo.carrion@uai.cl",
    "password" : "",
    "consumer-key" : "3MVG9xOCXq4ID1uFLDIihD8SFf9FJQwOFtAVVWV2r98uL4zSBeN5CRr0Rg6NfgsQUGtAHHnL2EaXh_ny.czHw",
    "consumer-secret": "C1BB690B6EC810BFB3FD1C39EC3E359EF4EE760F9CE1B447D5D68DF3F0A708AA",
    "domain": "login"
})

pprint.pprint(loginInfo)



sf = Salesforce(username="aldo.carrion@uai.cl", password='Pochita.@21', consumer_key=ck, consumer_secret=cs)
print(sf)
