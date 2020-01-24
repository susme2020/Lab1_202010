"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
 * 
 * Contribución de:
 *
 * Cristian Camilo Castellanos
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

"""
  Este módulo es una aplicación básica con un menú de opciones para cargar datos, contar elementos, y hacer búsquedas sobre una lista.
"""

import config as cf
import sys
import csv
from time import process_time 

def loadCSVFile (file, lst, sep=";"):
    """
    Carga un archivo csv a una lista
    """
    del lst[:]
    print("Cargando archivo ....")
    t1_start = process_time() #tiempo inicial
    dialect = csv.excel()
    dialect.delimiter=sep
    with open(file, encoding="utf-8") as csvfile:
        spamreader = csv.DictReader(csvfile, dialect=dialect)
        for row in spamreader: 
            lst.append(row)
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos")

def printMenu():
    """
    Imprime el menu de opciones
    """
    print("\nBienvenido")
    print("1- Cargar Datos")
    print("2- Contar los elementos de la Lista")
    print("3- Contar elementos filtrados por palabra clave")
    print("4- Consultar elementos a partir de dos listas")
    print("0- Salir")

def countElementsFilteredByColumn(criteria, column, lst):
    """
    Retorna cuantos elementos coinciden con un criterio para una columna dada  
    """
    if len(lst)==0:
        print("La lista esta vacía")  
        return 0
    else:
        t1_start = process_time() #tiempo inicial
        counter=0
        for element in lst:
            if criteria.lower() in element[column].lower(): #filtrar por palabra clave 
                counter+=1
        t1_stop = process_time() #tiempo final
        print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    return counter

def countElementsByCriteria(criteria, column, lst, lst2):
    """
    Retorna la cantidad de elementos que cumplen con un criterio para una columna dada
    """
    counter=countElementsFilteredByColumn(criteria, "director_name", lst) #contar películas del director  
    print("Coinciden ",counter," elementos con el criterio: ", criteria, " en la lista de directores" )
    num_prom_alto = 0
    counter_elemento = 0
    while counter != 0 or counter_elemento <= (len(lst) - 1):
        elemento = lst[counter_elemento]
        elemento2 = lst2[counter_elemento]
        if criteria in elemento["director_name"]:
            counter -= 1
            if float(elemento2[column]) >= 6.0:
                num_prom_alto += 1
        counter_elemento += 1
    return num_prom_alto


def main():
    lista = [] #instanciar una lista vacia, la lista 1 (directores)
    lista2 = [] #instanciar una lista vacia, la lista 2 (voto promedio)
    datos_cargados = False
    while True:
        printMenu() #imprimir el menu de opciones en consola
        inputs =input('Seleccione una opción para continuar\n') #leer opción ingresada
        if len(inputs)>0:
            if int(inputs[0])==1: #opcion 1
                loadCSVFile("Data/MoviesCastingRaw-small.csv", lista) #llamar funcion cargar datos para lista 1 (Directores)
                print("Datos cargados, lista 1 (Directores) con "+str(len(lista))+" elementos cargados")
                loadCSVFile("Data/AllMoviesDetailsCleaned.csv", lista2) #llamar funcion cargar datos para lista 2 (Voto Promedio)
                print("Datos cargados, lista 2 (Voto Promedio) con "+str(len(lista2))+" elementos cargados")
                datos_cargados = True
            elif int(inputs[0])==2: #opcion 2
                if not datos_cargados:
                    print("Debe cargar los datos primero\n")
                else:
                    if len(lista)==0: #obtener la longitud de la lista
                        print("La lista esta vacía")    
                    else: print("La lista tiene "+str(len(lista))+" elementos")
            elif int(inputs[0])==3: #opcion 3
                if not datos_cargados:
                    print("Debe cargar los datos primero\n")
                else:
                    criteria =input('Ingrese el criterio de búsqueda\n')
                    counter=countElementsFilteredByColumn(criteria, "director_name", lista) #filtrar una columna por criterio  
                    print("Coinciden ",counter," elementos con el criterio: ", criteria  )
            elif int(inputs[0])==4: #opcion 4
                if not datos_cargados:
                    print("Debe cargar los datos primero\n")
                else:
                    criteria =input('Ingrese el nombre del director\n')
                    counter=countElementsByCriteria(criteria,"vote_average",lista, lista2)
                    print("El director ", criteria, " tiene ", counter, " películas con promedio de votos igual o mayor a 6")
            elif int(inputs[0])==0: #opcion 0, salir
                sys.exit(0)

if __name__ == "__main__":
    main()
