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
                'Sentiment_values':None
                }

    analyzer['content_features'] = lt.newList('ARRAY_LIST')
    analyzer['track_hashtag'] = lt.newList('ARRAY_LIST')
    analyzer['Sentiment_values'] = lt.newList('ARRAY_LIST')
    analyzer['artist_id_index'] = om.newMap(omaptype='RBT')
    return analyzer
# Funciones para agregar informacion al catalogo

def addContent(analyzer, content):
    lt.addLast(analyzer['content_features'], content)
    updateArtistId(analyzer['artist_id_index'], content)
    return analyzer
    
def updateArtistId(map, content):

    artist_id = content['artist_id']
    entry = om.get(map, artist_id)
    if entry is None:
        artist_entry = newArtistEntry(content)
        om.put(map, artist_id, artist_entry)
    else:
        artist_entry = me.getValue(entry)
    addArtistIndex(artist_entry, content)
    return map    

def addArtistIndex(artist_entry, content):
    entry_content = mp.get(artist_entry['lstContent'], content['track_id'])
    if entry_content is None:
        entry = newTrackId(content['track_id'], content)
        lt.addLast(entry['lstContentTrack'], content)
        mp.put(artist_entry['lstContent'], content['track_id'], entry)
    else:
        entry = me.getValue(entry_content)
        lt.addLast(entry['lstContentTrack'], content)
    return artist_entry


def newArtistEntry(content):

    entry = {'artist_id': None, 'lstContent':None}
    entry['artist_id'] = content['artist_id']
    entry['lstContent'] = mp.newMap(numelements=30,
                                    maptype='PROBING',
                                    loadfactor=0.5)
    return entry

def newTrackId(track_id, content):
    entry = {'track_id':None, 'lstContentTrack':None}
    entry['track_id'] = track_id
    entry['lstContentTrack'] = lt.newList('ARRAY_LIST')
    return entry

# Funciones para creacion de datos

# Funciones de consulta

def artist_amount(analyzer):
    return om.size(analyzer['artist_id_index'])

def content_size(analyzer):
    return lt.size(analyzer['content_features'])

# def track_values(analyzer):
#     return om.valueSet(analyzer['artist_id_index'])

def unique_tracks_id(analyzer):
    tracks = 0
    lst_values = om.valueSet(analyzer['artist_id_index'])
    # for element in range(lt.size(lst_values)):
    #     map_values = lt.getElement(lst_values, element)
    #     #amount = me.size(map_values)
    #     print(map_values)
    #     tracks += 1
    #     if tracks >= 3:
    #         break
    for element in lt.iterator(lst_values):
        maps = element['lstContent']
        
        #tracks += int(mp.size(element))
        #print(element)
    return tracks
# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento
