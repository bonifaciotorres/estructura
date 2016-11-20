#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv

while True:
	print "|-------------------------------------------------------------------------|"
	print "|Selecione una opcion                                                     |"
	print "|-------------------------------------------------------------------------|"
	print "|1- Mostrar cantidad entre hombres y mujeres y la grafica                 |"
	print "|-------------------------------------------------------------------------|"
	print "|2- Mostrar la cantidad de estudiantes agrupados por carrera y su grafica |"
	print "|-------------------------------------------------------------------------|"
	print "|3- Mostrar la cantidad de errores null                                   |"
	print "|-------------------------------------------------------------------------|"
	print "|4- Ordenamiento por incercion                                            |"
	print "|-------------------------------------------------------------------------|"
	print "|5- Salir                                                                 |"
	print "|-------------------------------------------------------------------------|"
	
	sp = int(raw_input("Ingrese opcion: "))
	if sp ==1:
		fh = open('/home/bonifacio/Escritorio/borrowers_test.csv')
		mujer= []
		hombre=[]
		m=[]
		h=[]
		
		for line  in fh:
			linea2 = line.split(',')
			sexo = linea2[4]
			if sexo == "F":
				mujer.append(sexo)
		fh.close()
		
		f = open('/home/bonifacio/Escritorio/borrowers_test.csv')
		for line  in f:
			linea = line.split(',')
			sexo = linea[4]
			if sexo == "M":
				hombre.append(sexo)
		f.close()
		
		m.append(len(mujer))
		h.append(len(hombre))
		print "MUJERES:",m,"color grafrica:Azul"
		print "HOMBRES:",h,"color grafrica:Rojo"
		
		from numpy.random import beta
		import matplotlib.pyplot as plt
		plt.style.use('bmh')
		
		def plot_beta_hist(a, b):
			plt.hist(beta(a, b, size=20000), histtype="stepfilled",
			         bins=25, alpha=0.8, normed=True)
			return
			
		plot_beta_hist(m,m)
		plot_beta_hist(h,h)
		plt.show()
		
		
	elif sp==2:
		file = open('/home/bonifacio/Escritorio/borrowers_test.csv')
		lista = []
		wwe=[]
		v = raw_input("Ingrese nombre de la carrera: ")
		def buscaPalabras(str, file):
			for line in file:
				for part in line.split(','):
					if str in part:
						lista.append(line)
		        return lista
		
		
		buscaPalabras(v, file)
		wwe.append(len(lista))
		print wwe,"de la carrera:",v
		print ""  
		
		
		from numpy.random import beta
		import matplotlib.pyplot as plt
		plt.style.use('bmh')
		
		def plot_beta_hist(a, b):
			plt.hist(beta(a, b, size=20000), histtype="stepfilled",
			         bins=25, alpha=0.8, normed=True)
			return
			
		plot_beta_hist(wwe,wwe)
		
		
		
		plt.show()
	elif sp==3:
		file = open('/home/bonifacio/Escritorio/borrowers_test.csv')
		lista = []
		wwe=[]
		v = raw_input("Ingrese nombre de dato erroneo:")
		def buscaPalabras(str, file):
			for line in file:
				for part in line.split(','):
					if str in part:
						lista.append(line)
		        return lista
		
		buscaPalabras(v, file)
		wwe.append(len(lista))
		print wwe,"DE LOS ARCHIVOS ERRONEOS:",v
		print ""  
		
		
		from numpy.random import beta
		import matplotlib.pyplot as plt
		plt.style.use('bmh')
		
		def plot_beta_hist(a, b):
			plt.hist(beta(a, b, size=20000), histtype="stepfilled",
			         bins=25, alpha=0.8, normed=True)
			return
			
		plot_beta_hist(wwe,wwe)
		
		plt.show()
	elif sp==4:
		import sys
		sys.setrecursionlimit(20000)
		print "|-------------------|"
		print "|buscar por numero  |"
		print "|-------------------|"
		print "|0- apellidos       |"
		print "|-------------------|"
		print "|1- nombres         |"
		print "|-------------------|"
		print "|2- codigo_categoria|"
		print "|-------------------|"
		print "|3- fecha_registro  |"
		print "|-------------------|"
		print "|4- sexo            |"
		print "|-------------------|"
		print "|5- cod_carrera     |"
		print "|-------------------|"
		print "|6- nombre_carrera  |"
		print "|-------------------|"
		
		sx=int(raw_input("ingrese numero: "))
		fh= open('/home/bonifacio/Escritorio/borrowers_test.csv')
		lis=[]
		
		for line in fh:
			linea = line.split(",")
			s=linea[sx]
			lis.append(s)
		fh.close()
		print lis
		
		numeros=lis
		def Insercion(numeros): #numeros es una lista
			tama = len(numeros) #tamaño de la lista
			i=0
			for i in range(tama):
				indice = numeros[i]
				a = i-1
				while (a >= 0 and numeros[a] > indice):
					numeros[a+1] = numeros[a]
					a = a-1
					numeros[a+1] = indice
		print Insercion(numeros)
		print numeros #imprime la lista ordenada
	elif sp==5:
		break 
             
