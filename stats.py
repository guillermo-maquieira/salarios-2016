#Import Pandas for CSV manipulation and matplotlib for plotting.
import pandas as pd
import matplotlib.pyplot as plt

#Create a dataframe from CSV file.
df = pd.read_csv("salarios-2016.csv")

#Drop unwanted columns from dataframe.
df.drop(df.columns[[0,1,2,3,5]], axis=1, inplace=True)

#Customize data using GROUP BY ("apellido_nombre") and SUM ("asignaciones_mensuales") functions. 
data = df.groupby("apellido_nombre").sum()

#Print data for debugging purposes.
print(data)

#Customize plot attributes and show results. 
data = df.groupby("apellido_nombre").sum().plot(kind='barh', fontsize=10, title='Autoridades PEN\n2016')
plt.show()
