import pandas as pd
import numpy as np
import requests as rq


#import
from extract import listPostula
from extract_SF import listOp



sf_file = pd.read_excel('files\SalesForce_Postulacion_2.xlsx')
pos_file = pd.read_excel('files\Postula_Postulacion.xlsx')
arr_f=[]
arr_nf = []

def addHTML_SF(valueTxt):
    valueTxt = 'https://postgrados.lightning.force.com/lightning/r/Opportunity/'+valueTxt+'/view'
#    print(valueTxt)
    return valueTxt
#Debe quedar: https://postgrados.lightning.force.com/lightning/r/Opportunity/0065c00001NpacEAAR/view

def addHTML_Postula(valueTxt):
    link = str(valueTxt).split('.')[0]
    valueTxt = 'https://fin.uai.cl/Postgrado/Admin/administracion/postulaciones/ver_postulacion.aspx?postulacionid='+ link
#    print(valueTxt)
    return valueTxt

def addLink(valueTxt):
    LinkExcel = "=HIPERVINCULO('Link', '"+valueTxt+"')"
    return LinkExcel

#funcion para transformar un arreglo en arreglo numpy
def np_arr(arr):
    arr = np.array(arr)
    #generar funcion de reshape para generar una matriz con la información desde los arreglos
    return arr

def compareOp(listOp, listPostula):
    #print(listOp)
    #print(listPostula)
    num=0
    numyes=0
    dfPostula = pd.DataFrame(listPostula)
    dfSalesforce = pd.DataFrame(listOp)
    listPost = []
    for postPostula in listPostula:
        idPostulacionPostula = str(postPostula['PostulacionId'])
        listPost.append(idPostulacionPostula)
        #print(f"Postulacion Postula ::: {postPostula['PostulacionId']} :::")
    #print(f"dfSalesforce ::: {dfSalesforce}")
    print(listPost)
    for postulacion in dfSalesforce.values:
        idPostulacion = postulacion[1]
        if idPostulacion in listPost:
            link_postula = addHTML_Postula(idPostulacion)
            arrPostulacion = [idPostulacion, link_postula]
            arr_f.append(arrPostulacion)
            numyes+=1
            print(f"Yes :: {idPostulacion} :: {numyes}")
        if idPostulacion not in listPost:
            link_postula = addHTML_Postula(idPostulacion)
            arrPostulacion = [idPostulacion, link_postula]
            arr_nf.append(arrPostulacion)
            num+=1
            print(f"No ::: {idPostulacion} :: {num}")
        #print(f"Postulacion Salesforce ::: {postulacion[1]} :::")
    return True

#for pos in sf_file.values:
#    if pos[0] in pos_file.values:
#        link_sf = addHTML_SF(pos[1])
#        link_postula = addHTML_Postula(pos[0])
#        arrOportunidad = [pos[0], (link_sf), (link_postula)]
#        arr_f.append(arrOportunidad)
#    else:
#        link_sf = addHTML_SF(pos[1])
#        link_postula = addHTML_Postula(pos[0])
#        arrOportunidad = [pos[0], link_sf, link_postula]
#        for i in range(len(pos)):
#            arrOportunidad.append(pos[i])
        #arrOportunidad.append(pos[2:])
#        arr_nf.append(arrOportunidad)

compareOp(listOp, listPostula)
df_casesFound = pd.DataFrame(arr_f)
df_casesNotFound = pd.DataFrame(arr_nf)
#Generar un contexto para escribir los DataFrames en un único archivo con distintas hojas. merge_cells permite que index_label aparezca en la primera fila.
with pd.ExcelWriter("files\ArchivoSalida_v01.xlsx") as writer:
    df_casesFound.to_excel(writer, sheet_name="Casos Encontrados", index_label="Postulaciones", merge_cells=False)
    df_casesNotFound.to_excel(writer, sheet_name="Casos No Encontrados", index_label="Postulaciones", merge_cells=False)
    
print("DONE")






        

    






