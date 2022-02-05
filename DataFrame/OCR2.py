from PIL import Image
from pandas.core.frame import DataFrame

import pytesseract
import numpy as np

import pandas as pd


#import cv2 

from re import split

def facturas(num_imagen):
    filename = f'camada5/{num_imagen}.jpg'
    img1 = np.array(Image.open(filename))
    text = pytesseract.image_to_string(img1)

    print(text)

    #------------------------------
    #rescatamos los números
    tarjeta=split('\D+',text)
    #----------------------------
    #quitamos los espacios en blanco:
    for i in tarjeta:
        if i=='':
            tarjeta.remove('')  
    #-----------------------------
    #convertimos a integer los elementos:

    #for i in range(len(tarjeta)):
        #9tarjeta[i] = int(tarjeta[i])


    #añadimos el num de tarjeta como indice:
    tarjeta.insert(0,f'tarjeta {num_imagen}')
    #----------------------------
    #convertimos a dataframe

    

    df=pd.DataFrame(tarjeta)
    df=df.transpose()
    

    
    print(df)
#========================================================
    from csv import writer
    with open('registro_tarjetas.csv', 'a', newline='') as f_object:  
        # Pass the CSV  file object to the writer() function
        writer_object = writer(f_object)
        # Result - a writer object
        # Pass the data in the list as an argument into the writerow() function
        writer_object.writerow(tarjeta)  
        # Close the file object
        f_object.close()
#========================================================

def leer_registro():
    df=pd.read_csv('camada total.csv')
    print(df)
    #_____________________________________________________________
    serie=df['NIT'].sort_values() # selecciono la serie
    serie_pornit=serie.value_counts()  # cuento los valores repetidos
    
    #print(type(df_pornit))
    empresas=("Nuevatel","TIGO","ENTEL S.A.")
    df_pornit=pd.DataFrame(serie_pornit) #convierto la serie seleccionada en DF
    df_pornit.sort_index(inplace=True) #ordeno el indice de menor a mayor
    df_pornit['empresa']=empresas #añado la columan empresas(tuple)  en ese orden
    print(df_pornit)
    #----------------------------------------
    serie=df['N factura'].sort_values() # selecciono la serie
    serie_pornit=serie.value_counts()  # cuento los valores repetidos
    print(type(serie_pornit))
    print('suma de valores unicos de factura',serie_pornit.sum())
    #print(type(df_pornit))
    empresas=("Nuevatel","TIGO","ENTEL S.A.")
    df_pornit=pd.DataFrame(serie_pornit) #convierto la serie seleccionada en DF
    df_pornit.sort_index(inplace=True) #ordeno el indice de menor a mayor
    print(df_pornit)

    #----------------------------------------
    serie=df['N autorizacion'].sort_values() # selecciono la serie
    serie_pornit=serie.value_counts()  # cuento los valores repetidos
    
    #print(type(df_pornit))

    df_pornit=pd.DataFrame(serie_pornit) #convierto la serie seleccionada en DF
    df_pornit.sort_index(inplace=True) #ordeno el indice de menor a mayor
    print(df_pornit)

    print('suma de camada',df['monto'].sum())
    
leer_registro()

