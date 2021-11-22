import numpy as np
import pandas as pd

#cargando
df_18 =pd.read_csv("G:/Mi unidad/datos/OutBehavior/OutBehavior_1_mes/Anuales/OutBehavioral_2018_1.csv")
df_19 =pd.read_csv("G:/Mi unidad/datos/OutBehavior/OutBehavior_1_mes/Anuales/OutBehavioral_2019_1.csv")
df_20 =pd.read_csv("G:/Mi unidad/datos/OutBehavior/OutBehavior_1_mes/Anuales/OutBehavioral_2020_1.csv")
df_21 =pd.read_csv("G:/Mi unidad/datos/OutBehavior/OutBehavior_1_mes/Anuales/OutBehavioral_2021_1.csv")
#cargandoend

archivos = glob.glob("G:/Mi unidad/datos/OutBehavior/OutBehavior_1_mes/Anuales*.csv")
archivos
def concatenar(file1, file2):
    with open(file2, 'r') as filename2:
        data = file2.read()
    with open(file1, 'a') as filename1:
        file.write(data)

files =
with open(filepath, 'w', newline='') as f:
    for i, partial_df in enumerate(pd.read_csv(query, conn, chunksize=chunksize)):
        print('Writing chunk %s' % i)
        partial_df.to_csv(f, index=False, header=(i == 0))


with open(filepath, 'w', newline='') as f:
    for i, partial_df in enumerate(pd.read_sql(query, conn, chunksize=chunksize)):
        print('Writing chunk %s' % i)
        partial_df.to_csv(f, index=False, header=(i == 0))

filepath='G:/Mi unidad/datos/OutBehavior/OutBehavior_1_mes/Anuales/OutBehavioral_2021_1.csv'
with open(filepath, 'w', newline='') as f:
    for i, partial_df in enumerate(pd.read_csv('OutBehavioral_2021_1.csv')):
        print('Writing chunk %s' % i)
        #partial_df.to_csv(f, index=False, header=(i == 0))