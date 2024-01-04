import requests as rq
from requests.auth import HTTPBasicAuth
import pandas as pd


#Agregar comentarios de funcionamiento del programa para ser revisado por cualquiera.

api_url_POSTULA= 'https://finanzas.uai.cl/internalservices/api/PostPostulacion/ObtenerPostulacionPorFiltros'

excel_file_path = "files\ArchivoSalida_Postula_v01.xlsx"
excel_file_path_2 = "files\ArchivoSalida_Postula_v02.xlsx"

json_body = {
              "Ano": 2023,
              "Usuario": "ernesto.jaramillo",
              "TamanoPagina": 20000,
              "NumeroPagina": 1,
              "FiltroEstadoNombre": "Matriculado"
            }

#campos = ["PostulacionId", "PostulanteNombre", "PostulanteApellidoPaterno","PostulanteApellidoMaterno", "FechaMatricula", "TipoDocumentoNombre", "NumeroDocumento", "Email", "Celular", "CohorteNombre", "EstadoNombre", "FechaPostulacion", "FechaMatricula","PlanDeCapacitacionId","PlanDeCapacitacionNombre"]
#CREAR definicion de funcion con retorno del DF de parte de Postula para comparar Oportunidades
def df_Postula(url, json):
    response = rq.post(url=url, auth=HTTPBasicAuth('TD2018', '2018TD'), data=json)
    if response.status_code == 200:
        response_dict = response.json()
        data_response = list(response_dict.items())[0][1]
        df = data_response
        #print(f"Df: ", df)
        return df
    else:
        print(f"Error: {response.status_code}")


listPostula = df_Postula(api_url_POSTULA, json_body)
dfPostula = pd.DataFrame.from_dict(listPostula)
dfPostula.to_excel(excel_file_path_2, index=False, index_label=True)



#response = rq.post(url=api_url_POSTULA, auth=HTTPBasicAuth('TD2018', '2018TD'), data=json_body)
#if response.status_code == 200:
#    response_dict = response.json() #Crea un diccionario de la respuesta JSON
#    data_response = list(response_dict.items())[0][1] #Toma los datos del diccionario correspondientes al JSON con la información de la postulación
#    df = pd.DataFrame.from_dict(data_response) #Crea un DataFrame con los items correspondientes al data_response
#    df.to_excel(excel_file_path_2,index=False, index_label=True) #Se genera un archivo excel con labels indicados, en la ruta indicada
#    print(f"Exportado en {excel_file_path_2}")
#    #pprint.pprint(response_dict)
#    #pprint.pprint(data_response)
#else:
#    print(f"Error: {response.status_code}")

