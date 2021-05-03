"""
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


    return analyzer
# Funciones para agregar informacion al catalogo

def addContent(analyzer, content):
    lt.addLast(analyzer['content_features'], content)

    #Update Binary Trees
    updateInstrumental(analyzer['instrumentalness'], content)
    # updateLiveness(analyzer['liveness'], content)
    # updateSpeechiness(analyzer['speechiness'], content)
    # updateDanceabilitiy(analyzer['danceability'], content)
    # updateValence(analyzer['valence'], content)
    # updateAcousticness(analyzer['acousticness'], content)
    # updateEnergy(analyzer['energy'], content)

    return analyzer
    
def updateInstrumental(map, content):
    #Se revisa el valor que va a ser llave de un nodo
    Instrumental_value = float(content['instrumentalness'])
    #Vemos si algún nodo ya tiene este valor
    entry = om.get(map, Instrumental_value)
    if entry is None:
        #Creamos la estructura del nodo que tendra como llave 
        #El valor de instrumentalidad visto previamente
        instrumental_entry = newInstrumentEntry(content)
        #Este valor se agraga al nodo y nos queda la siguiente estructura
        #Un nodo {Key-"Valor_Instrumentalidad":Valor-Mapa}
        #El mapa que esta como valor del nodo tiene la siguiente estructura
        #{Key-Artista_id:Valor-Lista con contendio del mismo artista}
        om.put(map, Instrumental_value, instrumental_entry)
    else:
        instrumental_entry = me.getValue(entry)
    #lt.addLast(instrumental_entry['lstContent'], content)
    addInstrumentalIndex(instrumental_entry, content)
    return map    

def addInstrumentalIndex(Instrumental_entry, content):
    entry_content = mp.get(Instrumental_entry['lstContent'], content['artist_id'])
    if (entry_content is None):
        entry = newArtist(content)
        lt.addLast(entry['instrumental_content'], content)
        mp.put(Instrumental_entry['lstContent'], content['artist_id'], entry)
    else:
        entry = me.getValue(entry_content)
        lt.addLast(entry['instrumental_content'], content)
    return Instrumental_entry

def newInstrumentEntry(content):

    entry = {'Instrument_value': None, 'lstContent':None}
    entry['Instrument_value'] = float(content['instrumentalness'])
    entry['lstContent'] = mp.newMap(numelements=100,
                                    maptype='PROBING',
                                    loadfactor=0.3)
    #entry['lstContent'] = lt.newList('ARRAY_LIST')
    return entry

def newArtist(content):
    ofentry = {'Artist_id':None, 'instrumental_content':None}
    ofentry['Artist_id'] = content['artist_id']
    ofentry['instrumental_content'] = lt.newList('ARRAY_LIST')
    return ofentry

# Funciones para creacion de datos

# Funciones de consulta

def content_size(analyzer):
    return lt.size(analyzer['content_features'])

def getArtistByCategory(analyzer, min_value, max_value):
    lst = om.values(analyzer['instrumentalness'], min_value, max_value)
    total_artists, total_songs = 0, 0
    pruebas = []
    for artist in lt.iterator(lst):
        normal_brother = []
        #total_artists += lt.size(mp.keySet(artist['lstContent']))
        # if total_artists >= 7:
        #     print(mp.keySet(artist['lstContent']))
            #break
        for artists in lt.iterator(mp.keySet(artist['lstContent'])):
            normal_brother.append(artists)
        pruebas.append(normal_brother)

        for songs in lt.iterator(mp.valueSet(artist['lstContent'])):
            total_songs += lt.size(songs['instrumental_content'])
        #total_songs += lt.size(mp.valueSet(artist['lstContent']))
        # total_songs += mp.size(me.getValue())
    return total_artists, total_songs, pruebas
    

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
