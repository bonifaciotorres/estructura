#!/usr/bin/env python
# -*- coding: Windows-1252 -*-
# -*- coding: cp1252 -*-
# -*- coding: utf-8 -*-
# -*- coding: IBM850 -*-

import csv

while True:
    print"Selecione una opcion"
    print"01- Mostrar cantidad de registros con clasificando entre hombres y mujeres"
    print ""
    print"02- Hacer búsquedas en el archivo por nombre o apellidos y mostrar las coincidencias"
    print ""
    print"03- Mostrar la cantidad de estudiantes agrupados por carrera"
    print ""
    print"04- Mostrar cantidad de datos erróneos es decir NULL, o vacíos u otros errores"
    print ""
    print"05- Agregar registros al final del archivo proporcionado pidiendo los datos desde el teclado"
    print ""
    print"6- Ordene los registros por orden alfabéticov Quickshort"
    print ""
    print"7- Ordene los registros por orden alfabético burbuja"
    print ""
    print"8- Ordene los registros por orden alfabético usando quicksort, pero que pida la columna a ordenar"
    print ""
    print"9- Salir"
    
    sp = int(raw_input("Ingrese opcion: "))
       
    if sp ==1:
		fh = open('/home/bonifacio/Escritorio/borrowers_test.csv')
		mujer= []
		hombre=[]
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
		print "MUJERES:",len(mujer)
		print "HOMBRES:",len(hombre)
           
    elif sp==2:
	print ""
        l=[]
        sps = raw_input("Ingrese NOMBRE O APELLIDO COMPLETO: ")
        def buscaPalabra(str, file):
            for line in file:
                for part in line.split(','):
                    if str in part:
                        l.append(line)
                        return l
	file = open('/home/bonifacio/Escritorio/borrowers_test.csv')
	print buscaPalabra(sps, file)
	print ""   
    elif sp==3:
		print""
		lista = []
		v = raw_input("Ingrese nombre de la carrera: ")
		def buscaPalabras(str, file):
			for line in file:
				for part in line.split(','):
					if str in part:
						lista.append(line)
		        return lista
		
		file = open('/home/bonifacio/Escritorio/borrowers_test.csv')
		buscaPalabras(v, file)
		print len(lista),"de la carrera",v 
		print ""     
    elif sp==4:
        lista = []
        def buscaPalabrass(str, file):
            for line in file:
                for part in line.split(','):
                    if str in part:
                        lista.append(line)
            return lista
        file = open('/home/bonifacio/Escritorio/borrowers_test.csv')
        print buscaPalabrass("NULL", file)
        
	
    elif sp==5:
		sp = str(raw_input("Ingrese apellido: "))
		sp1 = str(raw_input("Ingrese nombre: "))
		sp2 = str(raw_input("Ingrese codigo_categoria: "))
		sp3 = str(raw_input("Ingrese fecha_registro: "))
		sp4 = str(raw_input("Ingrese sexo: "))
		sp5 = str(raw_input("Ingrese cod_carrera: "))
		sp6 = str(raw_input("Ingrese nombre_carrera: "))
		f = open('/home/bonifacio/Escritorio/borrowers_test.csv','a')
		obj = csv.writer(f, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)
		obj.writerow([sp,sp1,sp2,sp3,sp4,sp5,sp6])
		f.close()
    elif sp==6:
        fh = open('/home/bonifacio/Escritorio/borrowers_test.csv')
        busqueda = []
        for line  in fh:
            linea2 = line.split(',')
            apellido = linea2[1]
            busqueda.append(apellido)
        fh.close()
        alist=busqueda
        def quickSort(alist):
            quickSortHelper(alist,0,len(alist)-1)
            
        def quickSortHelper(alist,first,last):
            if first<last:
                splitpoint = partition(alist,first,last)

                quickSortHelper(alist,first,splitpoint-1)
                quickSortHelper(alist,splitpoint+1,last)


        def partition(alist,first,last):
            pivotvalue = alist[first]
            
            leftmark = first+1
            rightmark = last

            done = False
            while not done:
				while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
					leftmark = leftmark + 1
					
				while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
						rightmark = rightmark -1
				if rightmark < leftmark:
					done = True
				else:
					temp = alist[leftmark]
					alist[leftmark] = alist[rightmark]
					alist[rightmark] = temp

            temp = alist[first]
            alist[first] = alist[rightmark]
            alist[rightmark] = temp


            return rightmark
                        
        quickSort(alist)
        print(alist)     
    elif sp==7:
		fh = open('/home/bonifacio/Escritorio/borrowers_test.csv')
		busqueda = []
		for line  in fh:
			linea2 = line.split(',')
			apellido = linea2[1]
			busqueda.append(apellido)
		fh.close()
		alist=busqueda	
		def shortBubbleSort(alist):
			exchanges = True
			passnum = len(alist)-1
			while passnum > 0 and exchanges:
				exchanges = False
				for i in range(passnum):
					if alist[i]>alist[i+1]:
						exchanges = True
						temp = alist[i]
						alist[i] = alist[i+1]
						alist[i+1] = temp
				passnum = passnum-1
		
		print shortBubbleSort(alist)
		print(alist)
        
    elif sp==8:
		s=int(raw_input("escribr la columna: "))
		fh = open('/home/bonifacio/Escritorio/borrowers_test.csv')
		busqueda = []
		for line  in fh:
			linea2 = line.split(",")
			apellido = linea2[s]
			busqueda.append(apellido)
		fh.close()
		alist=busqueda
		def quickSort(alist):
			quickSortHelper(alist,0,len(alist)-1)
			
		def quickSortHelper(alist,first,last):
			if first<last:
				splitpoint = partition(alist,first,last)
				
				quickSortHelper(alist,first,splitpoint-1)
				quickSortHelper(alist,splitpoint+1,last)
		
		def partition(alist,first,last):
			pivotvalue = alist[first]
			leftmark = first+1
			rightmark = last
			done = False
			while not done:
				while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
					leftmark = leftmark + 1
				while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
					rightmark = rightmark -1
					
				if rightmark < leftmark:
					done = True
				else:
					temp = alist[leftmark]
					alist[leftmark] = alist[rightmark]
					alist[rightmark] = temp
					
			temp = alist[first]
			alist[first] = alist[rightmark]
			alist[rightmark] = temp
			
			return rightmark
			
		quickSort(alist)
		print(alist) 
    elif sp==9:
        break 
             
