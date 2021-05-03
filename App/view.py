"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
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
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""
content_file = 'context_content_features-small.csv'

def printMenu():
    print("Bienvenido")
    print("1- Crear catalogo")
    print("2- Cargar información en el catálogo")
    print("3- Caracterizar las reproducciones")
    print("4- Encontrar música para festejar")
    print("5- Encontrar música para estudiar")
    print("6- Estudiar los géneros musicales")
    print("7- Indicar el género musical más escuchado en el tiempo")
    print("0- Salir")

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')

    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        cont = controller.init()

    elif int(inputs[0]) == 2:
        controller.loadData(cont, content_file)
        print('Registros cargados: ' + str(controller.content_size(cont)))
        #print('Artistas únicos cargados:' + str(controller.artist_amount(cont)))
        #tracks = controller.track_values(cont)
        # tracks_amount = controller.unique_tracks_id(cont)
        #print('Tracks únicos cargados: ' + str(controller.tracks_amount(cont)))


    elif int(inputs[0]) == 3:
        #La estructura de datos que se escogió
        #para avanzar en la solución del requerimienot 1
        #fue un árbol de tipo RBT
        caracteristica = input('Ingrese la característica de contenido\n')
        min_value = float(input('Ingrese el valor mínimo de la característica de contenido\n'))
        max_value = float(input('Ingrese el valor máximo de la careacterística de contenido\n'))

        artist_amount = controller.getArtistByCategory(cont, min_value, max_value)
        #print('La altura del arbol es: ' + str(controller.tracks_amount(cont)))
        #print('La cantidad de elementos son: ' + str(controller.content_size(cont)))
        print(artist_amount[0], artist_amount[1])
        glitter = []
        counter = 0
        for i in artist_amount[2][7]:
            counter += 1
            if i not in glitter:
                glitter.append(i)
        print(counter, len(glitter))
        #======================
        #Solución Python Normal
        #======================
        # bad_list = []
        # counter = 0
        # for track in lt.iterator(cont['content_features']):
        #     if float(track['instrumentalness']) >= 0.75 and float(track['instrumentalness']) <= 1.0: # and track['artist_id'] not in bad_list:
        #         counter += 1
        #         bad_list.append(track['artist_id'])
        # print(len(bad_list))
        # print(counter)

    elif int(inputs[0]) == 4:
        pass

    elif int(inputs[0]) == 5:
        pass

    elif int(inputs[0]) == 6:
        pass

    elif int(inputs[0]) == 7:
        pass

    else:
        sys.exit(0)
sys.exit(0)
