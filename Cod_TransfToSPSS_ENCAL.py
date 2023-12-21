# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 12:35:15 2023

@author: juan.mayaf
"""

import pandas as pd
import pyreadstat
import os
os.chdir('C:/Users/juan.mayaf/Documents/CIE/2023/04_ENCAL SS 2023/02_BD/_Py')


##Base en formato csv/xlsx/SAV... 
#df, meta = pyreadstat.read_sav("BD_rec\\Completas\\MM_ENSUI 2023_F1.sav")
df = pd.read_csv("CORTE_211223\\ENCAL SS 2023_.csv")#,encoding='utf-8', engine='python'
                 #converters={'Nombre de Variable A texto':str})
                 #dtype={'probsal_t':str, 'sat3_mot_t':str, 'mot_no_federal_t':str})
                 
##archivo con nombres de variables y etiquetas de variables
metavar = pd.read_excel('Var_Name_Label.xlsx',
                        sheet_name='ENCAL_SS_2023')
    
df = df.drop( 0, 0)
#print(df)

dic_metada = dict(zip(metavar.name_variable,metavar.label_variable))
df['date_created']=df['date_created'].astype('datetime64[ns]')
df['date_modified']=df['date_modified'].astype('datetime64[ns]')


df.columns=metavar['name_variable']
pyreadstat.write_sav(df,"CORTE_211223\\ENCAL_SS_2023_Python_211223.sav", column_labels=dic_metada)