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
import model
from DISClib.ADT import list as lt
from DISClib.DataStructures import bst as bst
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""
content_file = 'context_content_features-small.csv'
hashtags_file = 'user_track_hashtag_timestamp-small.csv'
sentiment_values_file = 'sentiment_values.csv'

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

def printGeneros(lst):
    number = 0
    print('')
    print('|=================|')
    print('|-----Generos-----|')
    print('|=================|')
    for elements in lt.iterator(lst):
        number += 1
        print(' _________________')
        print('|'+str(number) + '.' + elements)

def printGenerosData(genero, total_artist, total_songs,
 artist_10, min_tempo, max_tempo):
    num = 0
    print('======= '+genero.upper()+' =======')
    print('For '+genero+' the tempo is between '+str(min_tempo)+' and '+
    str(max_tempo)+' BPM')
    print(genero +' reproductions: ' + str(total_songs)+' with '+
    str(total_artist)+' different artists')
    print('----- Some artists for '+genero+' -----')
    for artist in lt.iterator(artist_10):
        num += 1
        print('Artist '+str(num)+': '+artist)
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
        controller.loadListGeneros(cont)
        controller.loadListTempos(cont)
        

    elif int(inputs[0]) == 2:
        model.updateTempoGenero(cont['tempo_genero'])
        controller.loadDataSentiment(cont, sentiment_values_file)
        controller.loadDataHashTrack(cont, hashtags_file)
        controller.loadData(cont, content_file)
        print('Registros cargados: ' + str(controller.content_size(cont)))
        
        model.req_5_v_2(cont,'07:15:00','09:45:00')
        


        
 
        #Terminar de implementar el requerimiento 5. El BST de VADER ya está listo: llaves son valores de VADER y valores son listas con hashtags.
        
    elif int(inputs[0]) == 3:

        feature = input('Ingrese la característica de contenido\n')
        min_value = float(input('Ingrese el valor mínimo de la característica de contenido\n'))
        max_value = float(input('Ingrese el valor máximo de la careacterística de contenido\n'))

        artist_amount = controller.R_1(feature, cont, min_value, max_value)
        print(artist_amount[0], artist_amount[1])
        glitter = []
        counter = 0
   

    elif int(inputs[0]) == 4:
        min_value1 = float(input('Ingrese el valor mínimo de la característica Energy\n'))
        max_value1 = float(input('Ingrese el valor máximo de la careacterística Energy\n'))
        min_value2 = float(input('Ingrese el valor mínimo de la característica Danceability\n'))
        max_value2 = float(input('Ingrese el valor máximo de la careacterística Danceability\n'))
        unique_tracks = controller.R_2y3('energy', 'danceability', cont, min_value1, 
        max_value1, min_value2, max_value2)
        random_tracks = controller.random_selector(unique_tracks[1])

        print('++++ Req No. 2 results ++++')
        print('Total of unique tracks in the events: ' +str(unique_tracks[0]))
        print('|=== Unique track id ===|')
        for track in lt.iterator(random_tracks):
            #print(track['track_id'])
            print('Track id: '+str(track['track_id']) +str(' with instrumentalness of ')+str(track['energy'])+str(' and tempo of ')+str(track['danceability']))
        print('')

    elif int(inputs[0]) == 5:
        min_value1 = float(input('Ingrese el valor mínimo del rango para energy\n'))
        max_value1 = float(input('Ingrese el valor máximo del rango para energy\n'))
        min_value2 = float(input('Ingrese el valor mínimo del rango para danceability\n'))
        max_value2 = float(input('Ingrese el valor máximo del rango para danceability\n'))
        unique_tracks = controller.R_2y3('instrumentalness', 'tempo', cont, min_value1, 
        max_value1, min_value2, max_value2)
        random_tracks = controller.random_selector(unique_tracks[1]) 
        # unique_tracks = controller.R_2('instrumentalness', 'tempo', cont, 0.6, 
        # 0.9, 40, 60)
        print('++++ Req No. 3 results ++++')
        print('Total of unique tracks in the events: ' +str(unique_tracks[0]))
        print('|=== Unique track id ===|')
        for track in lt.iterator(random_tracks):
            #print(track['track_id'])
            print('Track id: '+str(track['track_id']) +str(' with instrumentalness of ')+str(track['instrumentalness'])+str(' and tempo of ')+str(track['tempo']))
        print('')
    elif int(inputs[0]) == 6:
        printGeneros(cont['Nombre_generos'])
        print('')
        print('Escoja una de las siguientes opciones:')
        num = input('1. Escribir los numeros de los generos que desea buscar\n2. Agregar un nuevo genero musical\n')
        if num == '1':
            num_generos = input('Escriba los numeros de los generos que desea buscar, separe los números por comas\n'+
            'Ej.:1 2 3\n')
            generos = num_generos.split(' ')
            for num in generos:
                genero = lt.getElement(cont['Nombre_generos'], int(num))
                #print(controller.R_4(cont, genero))
                min_tempo = 60
                max_tempo = 90
                printing_data = controller.R_4(cont, genero)
                printGenerosData(genero, printing_data[0], printing_data[1],
                printing_data[2], min_tempo, max_tempo)
        elif num == '2':
            nuevo_genero = input('Nombre único para el nuevo género musical')
            min_value = input('Valor mínimo del Tempo del nuevo género musical')
            max_value = input('Valor máximo del Tempo del nuevo género musical')



    elif int(inputs[0]) == 7:
        pass

    else:
        sys.exit(0)
sys.exit(0)
