import requests as rq
import pandas as pd
from simple_salesforce import Salesforce, SalesforceLogin, SFType



ck = '3MVG9xOCXq4ID1uFLDIihD8SFf9FJQwOFtAVVWV2r98uL4zSBeN5CRr0Rg6NfgsQUGtAHHnL2EaXh_ny.czHw'
cs = 'C1BB690B6EC810BFB3FD1C39EC3E359EF4EE760F9CE1B447D5D68DF3F0A708AA'


loginInfo =({
    "username" : "aldo.carrion@uai.cl",
    "password" : "",
    "consumer-key" : "3MVG9xOCXq4ID1uFLDIihD8SFf9FJQwOFtAVVWV2r98uL4zSBeN5CRr0Rg6NfgsQUGtAHHnL2EaXh_ny.czHw",
    "consumer-secret": "C1BB690B6EC810BFB3FD1C39EC3E359EF4EE760F9CE1B447D5D68DF3F0A708AA",
    "domain": "login"
})

#pprint.pprint(loginInfo)



#sf = Salesforce(username="aldo.carrion@uai.cl", password='Pochita.@21', consumer_key=ck, consumer_secret=cs)
#print(sf)

#Atributos de SF
session_id, instance = SalesforceLogin(username="aldo.carrion@uai.cl", password="Pochita.@21", consumer_key=ck, consumer_secret=cs)
sf = Salesforce(instance=instance, session_id=session_id)

#print(sf)

#for element in dir(sf):
#    if not element.startswith('_'):
#        if isinstance(getattr(sf, element), str):
#            print('Property Name: {0}  ;Value: {1}'.format(element, getattr(sf,element)))

#metadata_org = sf.describe()
#print(metadata_org['encoding'])
#print(metadata_org['maxBatchSize'])
#print(metadata_org['sobjects'])

#df_sobjects.to_excel('org_metadata_info.xlsx', index=False)

#method of extract information
#account = sf.account
#print("Account: ", account)
#account_metadata = account.describe()
#df_account_metadata = pd.DataFrame(account_metadata.get('fields'))
#df_account_metadata.to_excel('sf_metadata_account.xlsx', index_label=True)

#oportunidad = sf.Opportunity
#oportunidad_metadata = oportunidad.describe()
#df_opportunity_metadata = pd.DataFrame(oportunidad_metadata.get('fields'))
#df_account_metadata.to_excel('sf_oportunidad_metadata.xlsx', index_label=True)

#query = "This method do not return archived records"
#query_more = "This method do not return archived records"
#query_all = "Returns all the records wether they're archived or not "

#recordsOp = sf.query(query) 


def df_oportunidades(query):
    response = sf.query(query)
    listOp = response.get('records')
    
    return listOp

#Definir funcion donde retorne DF con el listado de Oportunidades
queryOportunidades = "SELECT Numero_de_postulacion_eda__c, Id, CreatedDate, StageName, AccountId, Name FROM OPPORTUNITY WHERE StageName = 'Matriculado' ORDER BY CreatedDate DESC LIMIT 15000"
listOp = df_oportunidades(queryOportunidades)
df_listOp = pd.DataFrame(listOp)
df_listOp.to_excel('Oportunidades.xlsx', index_label=True)

