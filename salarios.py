#Import libraries for manipulate and plot a CSV file.
import csv
import matplotlib.pyplot as plt

#Initalize lists for storing values stored on CSV file.
x = []
y = []

#Iterate on CSV file and append 'mes' and 'asignacion_mensual' values on each list.
with open('salarios-2016.csv','r') as csvFile:
    salarios = csv.reader(csvFile, delimiter=',')
    #Skip CSV header.
    next(salarios)
    for salario in salarios:
        x.append(int(salario[1]))
        y.append(float(salario[6]))

#Lists output for debugging purposes.
print(x)
print(y)

#Customize and show plot attributes.
plt.style.use('ggplot')
plt.plot(x,y, label='Salarios')
plt.xlabel('Mes')
plt.ylabel('Sueldos')
plt.title('Autoridades PEN\n2016')
plt.legend()
plt.show()