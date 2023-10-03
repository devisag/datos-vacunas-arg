import pandas as pd
import csv

dataset_locate = r'C:\Users\alejo\OneDrive\Escritorio\data-vacunas\datset.csv'
new_dataset_locate = r'C:\Users\alejo\OneDrive\Escritorio\data-vacunas\newdatset.csv'
graphicdata_locate = r'C:\Users\alejo\OneDrive\Escritorio\data-vacunas\graphicdata.csv'

def read_csv():
   ##  Leemos el csv
   df = pd.read_csv(dataset_locate)
   
   ## Filtramos por columnas
   df =df[["vacuna_nombre", "dosis_unica_cantidad", "primera_dosis_cantidad", "segunda_dosis_cantidad", "dosis_adicional_cantidad", "dosis_refuerzo_cantidad"]]
   
   ## Guardamos en un nuevo csv para futuros analisis
   df.to_csv(new_dataset_locate, index=False)

   ## Sumamos cantidades de cada vacuna
   astrazeneca = df[df["vacuna_nombre"].str.contains("astrazeneca", case=False)].drop('vacuna_nombre', axis=1).sum(axis=1).sum(axis=0)
   covishield = df[df["vacuna_nombre"].str.contains("covishield", case=False)].drop('vacuna_nombre', axis=1).sum(axis=1).sum(axis=0)
   cansino = df[df["vacuna_nombre"].str.contains("cansino", case=False)].drop('vacuna_nombre', axis=1).sum(axis=1).sum(axis=0)
   moderna = df[df["vacuna_nombre"].str.contains("moderna", case=False)].drop('vacuna_nombre', axis=1).sum(axis=1).sum(axis=0)
   pfizer = df[df["vacuna_nombre"].str.contains("pfizer", case=False)].drop('vacuna_nombre', axis=1).sum(axis=1).sum(axis=0)
   sinopharm = df[df["vacuna_nombre"].str.contains("sinopharm", case=False)].drop('vacuna_nombre', axis=1).sum(axis=1).sum(axis=0)
   sputnik = df[df["vacuna_nombre"].str.contains("sputnik", case=False)].drop('vacuna_nombre', axis=1).sum(axis=1).sum(axis=0)
   
   # creando nuevo df
   data = {'Vacuna': ['Astrazeneca', 'Covishield', 'Cansino', 'Moderna', 'Pfizer', 'Sinopharm', 'Sputnik'], 'Cantidad': [astrazeneca, covishield, cansino, moderna, pfizer, sinopharm, sputnik]}
   
   data_df = pd.DataFrame(data).to_csv(graphicdata_locate, index=False)

read_csv()
      
