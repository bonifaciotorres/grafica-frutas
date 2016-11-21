# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt


numero = []
while True:
    print"Selecione una opcion"
    print"1- Lista de numeros nombres de votantes"
    print"2- numeros de votos en total"
    print"3- crear lista para grafica"
    print"4- existencia lista"
    print"5- Grafico de votantes"
    print"6- Salir"
    
    
    sp = int(raw_input("Ingrese opcion: "))
    
    if sp ==1:
        fh = open('/home/bonifacio/Escritorio/encuesta_espanol.txt')
        for line in fh:
            linea = line.split(' - ')
            nombre = linea[0]
            apellido = linea[1]
            numero.append(nombre)
            print numero
	
    elif sp==2:
       vegetal = raw_input("Ingrese la fruta o vegetal: ")
       def count_votes(vegetal):
           print ("Numero de votos para "+vegetal+ "...")
           count = 0
           for line in open('/home/bonifacio/Escritorio/encuesta_espanol.txt'):
               line = line.strip()
               nombre, voto = line.split(" - ")
               if voto == vegetal:
                   count = count + 1
	   return count
	   
       print (count_votes(vegetal)) 
    elif sp==3:
        
       def count_vote(vegetal):
           print ("Numero de votos para "+vegetal+ "...")
           count = 0
           for line in open('/home/bonifacio/Escritorio/encuesta_espanol.txt'):
               line = line.strip()
               nombre, voto = line.split(" - ")
               if voto == vegetal:
                   count = count + 1
	   return count
	
       print (count_vote("Kiwi"))
       print (count_vote("Aguacate"))
       print (count_vote("Fresas"))
       print (count_vote("Rabano"))
       print (count_vote("Tomates"))
       print (count_vote("Frijoles"))
       print (count_vote("Brocoli"))
       print (count_vote("Lechuga"))
       print (count_vote("Sandia"))
       print (count_vote("Papas"))
       print (count_vote("Pepinos"))
       
       visitas = []
       a=(count_vote("Kiwi"))
       b=(count_vote("Aguacate"))
       c=(count_vote("Fresas"))
       d=(count_vote("Rabano"))
       e=(count_vote("Tomates"))
       f=(count_vote("Frijoles"))
       g=(count_vote("Brocoli"))
       h=(count_vote("Lechuga"))
       i=(count_vote("Sandia"))
       j=(count_vote("Papas"))
       k=(count_vote("Pepinos"))
       visitas.append(a)
       visitas.append(b)
       visitas.append(c)
       visitas.append(d)
       visitas.append(e)
       visitas.append(f)
       visitas.append(g)
       visitas.append(h)
       visitas.append(i)
       visitas.append(j)
       visitas.append(k)
       print visitas
    elif sp==4:
       print visitas
    elif sp==5: 
        labels = 'Kiwi', 'Aguacate', 'Fresas', 'Rabano', 'Tomates', 'Frijoles','Brocoli','Lechuga','Sandia','Papas','Pepinos'
        
        colors = ['lightskyblue', 'lightskyblue', 'lightskyblue', 'lightskyblue', 'lightskyblue', 'lightskyblue', 'lightskyblue', 'lightskyblue', 'lightskyblue', 'lightskyblue','lightskyblue']
      
        
        plt.pie(visitas, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=90)
        plt.axis('equal')
        fig = plt.figure()
        ax = fig.gca()
        plt.show()   

    elif sp==6:
        break          
