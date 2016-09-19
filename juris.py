#Import Pandas for CSV manipulation and matplotlib for plotting.
import pandas as pd
import matplotlib.pyplot as plt

#Create a dataframe from CSV file.
df = pd.read_csv("salarios-2016.csv")

#Drop unwanted columns from dataframe.
df.drop(df.columns[[0,1,2,4,5]], axis=1, inplace=True)

#Customize data using GROUP BY ("jurisdiccion") and SUM ("asignaciones_mensuales") functions. 
data = df.groupby("jurisdiccion").sum()

#Print data for debugging purposes.
print(data)

#Customize plot attributes and show results. 
data = df.groupby("jurisdiccion").sum().plot(kind='barh', fontsize=7, color='green', title='Jurisdiccion PEN\n2016')
plt.show()
