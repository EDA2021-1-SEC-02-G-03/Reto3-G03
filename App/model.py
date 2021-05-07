﻿"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
import random
from DISClib.ADT import list as lt
from DISClib.ADT import orderedmap as om
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newAnalyzer():

    analyzer = {'content_features': None,
                'track_hashtag': None,
                'Sentiment_values':None,
                'instrumentalness':None,
                'liveness':None,
                'speechiness':None,
                'danceability':None,
                'valence':None,
                'acousticness':None,
                'energy':None,
                }

    #Lists
    analyzer['content_features'] = lt.newList('ARRAY_LIST')
    analyzer['track_hashtag'] = lt.newList('ARRAY_LIST')
    analyzer['Sentiment_values'] = lt.newList('ARRAY_LIST')

    #Binary Trees
    analyzer['instrumentalness'] = om.newMap(omaptype='BST')
    analyzer['liveness'] = om.newMap(omaptype='BST')
    analyzer['speechiness'] = om.newMap(omaptype='BST')
    analyzer['danceability'] = om.newMap(omaptype='BST')
    analyzer['valence'] = om.newMap(omaptype='BST')
    analyzer['acousticness'] = om.newMap(omaptype='BST')
    analyzer['energy'] = om.newMap(omaptype='BST')

    analyzer['artistas'] = om.newMap(omaptype='BST')

    #Binary Tree para generos
    analyzer['generos'] = om.newMap(omaptype='BST')
    analyzer['Reggae'] = mp.newMap(numelements=65,
                                   maptype='PROBING',
                                   loadfactor=0.3)
    analyzer['Down_tempo'] = mp.newMap(numelements=65,
                                   maptype='PROBING',
                                   loadfactor=0.3)
    analyzer['Chill_out'] = mp.newMap(numelements=65,
                                   maptype='PROBING',
                                   loadfactor=0.3)
    analyzer['Hip_hop'] = mp.newMap(numelements=65,
                                   maptype='PROBING',
                                   loadfactor=0.3)
    analyzer['Jazz and Funk'] = mp.newMap(numelements=65,
                                   maptype='PROBING',
                                   loadfactor=0.3)
    analyzer['Pop'] = mp.newMap(numelements=65,
                                   maptype='PROBING',
                                   loadfactor=0.3)
    analyzer['R&B'] = mp.newMap(numelements=65,
                                   maptype='PROBING',
                                   loadfactor=0.3)
    analyzer['Rock'] = mp.newMap(numelements=65,
                                   maptype='PROBING',
                                   loadfactor=0.3)
    analyzer['Metal'] = mp.newMap(numelements=65,
                                   maptype='PROBING',
                                   loadfactor=0.3)
    return analyzer

# Funciones para agregar informacion al catalogo

def addContent(analyzer, content):
    lt.addLast(analyzer['content_features'], content)

    #Update Binary Trees
    updateDescriptionMaps(analyzer['instrumentalness'], content, 'instrumentalness')
    updateDescriptionMaps(analyzer['liveness'], content, 'liveness')
    updateDescriptionMaps(analyzer['speechiness'], content, 'speechiness')
    updateDescriptionMaps(analyzer['danceability'], content, 'danceability')
    updateDescriptionMaps(analyzer['valence'], content, 'valence')
    updateDescriptionMaps(analyzer['acousticness'], content, 'acousticness')
    updateDescriptionMaps(analyzer['energy'], content, 'energy')

    #Update Binary Tree
    updateGeneralGeneros(analyzer['generos'], content)
    updateGeneros(analyzer['Reggae'], content, 60, 90)
    updateGeneros(analyzer['Down_tempo'], content, 70, 100)
    updateGeneros(analyzer['Chill_out'], content, 90, 120)
    updateGeneros(analyzer['Hip_hop'], content, 85, 115)
    updateGeneros(analyzer['Jazz and Funk'], content, 120, 125)
    updateGeneros(analyzer['Pop'], content, 100, 130)
    updateGeneros(analyzer['R&B'], content, 60, 80)
    updateGeneros(analyzer['Rock'], content, 110, 140)
    updateGeneros(analyzer['Metal'], content, 100, 160)

    return analyzer
    
def updateDescriptionMaps(map, content, feature):
    # #Se revisa el valor que va a ser llave de un nodo
    # Instrumental_value = float(content['instrumentalness'])
    # #Vemos si algún nodo ya tiene este valor
    # entry = om.get(map, Instrumental_value)
    # if entry is None:
    #     #Creamos la estructura del nodo que tendra como llave 
    #     #El valor de instrumentalidad visto previamente
    #     instrumental_entry = newInstrumentEntry(content)
    #     #Este valor se agraga al nodo y nos queda la siguiente estructura
    #     #Un nodo {Key-"Valor_Instrumentalidad":Valor-Mapa}
    #     #El mapa que esta como valor del nodo tiene la siguiente estructura
    #     #{Key-Artista_id:Valor-Lista con contendio del mismo artista}
    #     om.put(map, Instrumental_value, instrumental_entry)
    # else:
    #     instrumental_entry = me.getValue(entry)
    # #lt.addLast(instrumental_entry['lstContent'], content)
    # addInstrumentalIndex(instrumental_entry, content)
    # return map    
    Instrumental_value = float(content[feature])
    #artist = content['artist_id']
    exist_value = om.contains(map, Instrumental_value)

    if exist_value:
        entry = om.get(map, Instrumental_value)
        actual_value = me.getValue(entry)
    else:
        actual_value = newInstrumentEntry(content, Instrumental_value)
        om.put(map, Instrumental_value, actual_value)
    lt.addLast(actual_value['lstContent'], content)
    
    # exist_artist = mp.contains(actual_value['lstContent'], artist)

    # if exist_artist:
    #     entry_art = mp.get(actual_value['lstContent'], artist)
    #     actual_artist = me.getValue(entry_art)
    # else:
    #     actual_artist = newArtist(content)
    #     mp.put(actual_value['lstContent'], artist, actual_artist)
    # lt.addLast(actual_artist['instrumental_content'], content)



# def addInstrumentalIndex(Instrumental_entry, content):
#     entry_content = mp.get(Instrumental_entry['lstContent'], content['artist_id'])
#     if (entry_content is None):
#         entry = newArtist(content)
#         mp.put(Instrumental_entry['lstContent'], content['artist_id'], entry)
#     else:
#         entry = me.getValue(entry_content)
#     lt.addLast(entry['instrumental_content'], content)
#     return Instrumental_entry

def updateGeneralGeneros(map, content):
    Tempo_value = float(content['tempo'])
    entry = om.get(map, Tempo_value)
    if entry is None:
        actual_value = newTempo(content)
        om.put(map, Tempo_value, actual_value)
    else:
        actual_value = me.getValue(entry)
    lt.addLast(actual_value['lstContent'], content)

def updateGeneros(map, content, min_tempo, max_tempo):
    Tempo_value = float(content['tempo'])
    if Tempo_value >= min_tempo and Tempo_value <= max_tempo:
        entry = mp.get(map, content['artist_id'])
        if entry is None:
            actual_value = newArtist(content)
            mp.put(map, content['artist_id'], actual_value)
        else:
            actual_value = me.getValue(entry)
        lt.addLast(actual_value['lstContent'], content)

def newInstrumentEntry(content, Instrumental_value):

    entry = {'Instrument_value': None, 'lstContent':None}
    entry['Instrument_value'] = Instrumental_value
    # entry['lstContent'] = mp.newMap(numelements=65,
    #                                 maptype='PROBING',
    #                                 loadfactor=0.5)
    entry['lstContent'] = lt.newList('ARRAY_LIST')
    return entry

def newTempo(content):

    entry = {'Tempo_value':None, 'lstContent':None}
    entry['Tempo_value'] = float(content['tempo'])
    entry['lstContent'] = lt.newList('ARRAY_LIST')
    return entry

def newArtist(content):
    entry = {'Artist_id':None, 'lstContent':None}
    entry['Artist_id'] = content['artist_id']
    entry['lstContent'] = mp.newMap(numelements=65,
                                   maptype='PROBING',
                                   loadfactor=0.3)
    return entry

# def newArtist(content):
#     ofentry = {'Artist_id':None, 'instrumental_content':None}
#     ofentry['Artist_id'] = content['artist_id']
#     ofentry['instrumental_content'] = lt.newList('ARRAY_LIST')
#     return ofentry

# Funciones para creacion de datos

# Funciones de consulta

def content_size(analyzer):
    return lt.size(analyzer['content_features'])

def R_1(feature, analyzer, min_value, max_value):
    lst = om.values(analyzer[feature], min_value, max_value)
    total_artists, total_songs = 0, 0
    #pruebas = []
    #print(lt.getElement(lst, 3))
    unique_artists = lt.newList('ARRAY_LIST')
    tracks = lt.newList('ARRAY_LIST')
    for artist in lt.iterator(lst):
        #total_artists += 1
        #normal_brother = []
        #total_artists += lt.size(mp.keySet(artist['lstContent']))
        # if total_artists >= 7:
        #     print(mp.keySet(artist['lstContent']))
            #break
        total_songs += lt.size(artist['lstContent'])
        for artists in lt.iterator(artist['lstContent']):
            if not lt.isPresent(unique_artists, artists['artist_id']):
                 lt.addLast(unique_artists, artists['artist_id'])
            lt.addLast(tracks, artists)
        # for artists in lt.iterator(mp.keySet(artist['lstContent'])):
        #     normal_brother.append(artists)
        # pruebas.append(normal_brother)
        # for songs in lt.iterator(mp.valueSet(artist['lstContent'])):
        #     total_songs += lt.size(songs['instrumental_content'])
        #total_songs += lt.size(mp.valueSet(artist['lstContent']))
        # total_songs += mp.size(me.getValue())
        total_artists = lt.size(unique_artists)

    return total_artists, total_songs, lst, tracks#, pruebas

def R_2y3(feature_1, feature_2, analyzer, min_value1, 
    max_value1, min_value2, max_value2):
    content_f1 = R_1(feature_1, analyzer, min_value1, max_value1)[3]
    #content_f2 = R_1(feature_2, analyzer, min_value2, max_value2)[3]
    randomness = lt.newList('ARRAY_LIST')
    unique_tracks = lt.newList('ARRAY_LIST')
    #print(lt.size(content_f2))
    for content in lt.iterator(content_f1):
        #try:
        if float(content[feature_2]) >= min_value2 and float(content[feature_2]) <= max_value2:
        
        #if lt.isPresent(content_f2, content['track_id']):
        #     print('yas')
            if not lt.isPresent(unique_tracks, content['track_id']):
                lt.addLast(unique_tracks, content['track_id'])
                lt.addLast(randomness, content)
        #except:
        #    pass
    return lt.size(unique_tracks), randomness

def R_4(analyzer):
    # lst = om.values(analyzer['generos'], 60, 90)
    # total_songs = 0
    # for reps in lt.iterator(lst):
    #     total_songs += lt.size(reps['lstContent'])
    total_songs = mp.size(analyzer['Reggae'])

    return total_songs


def random_selector(lst):
    random_lst = lt.newList('ARRAY_LIST')
    random_content = lt.newList('ARRAY_LIST')
    find_number = True
    for i in range(5):
        while find_number:
            random_num = random.randint(0, lt.size(random_lst))
            if not lt.isPresent(random_lst, random_num):
                lt.addLast(random_lst, random_num)
                find_number = False
        find_number = True
        lt.addLast(random_content, lt.getElement(lst, random_num))
    return random_content

# def track_values(analyzer):
#     return om.valueSet(analyzer['artist_id_index'])

# def unique_tracks_id(analyzer):
#     tracks = 0
#     lst_values = om.valueSet(analyzer['artist_id_index'])
#     # for element in range(lt.size(lst_values)):
#     #     map_values = lt.getElement(lst_values, element)
#     #     #amount = me.size(map_values)
#     #     print(map_values)
#     #     tracks += 1
#     #     if tracks >= 3:
#     #         break
#     for element in lt.iterator(lst_values):
#         maps = element['lstContent']

#         #tracks += int(mp.size(element))
#         #print(element)
#     return tracks
# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento
