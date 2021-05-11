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
                'Nombre_generos':None
                }

    #Lists
    analyzer['content_features'] = lt.newList('ARRAY_LIST')
    analyzer['track_hashtag_lst'] = lt.newList('ARRAY_LIST')


    #Binary Trees
    analyzer['instrumentalness'] = om.newMap(omaptype='BST')
    analyzer['liveness'] = om.newMap(omaptype='BST')
    analyzer['speechiness'] = om.newMap(omaptype='BST')
    analyzer['danceability'] = om.newMap(omaptype='BST')
    analyzer['valence'] = om.newMap(omaptype='BST')
    analyzer['acousticness'] = om.newMap(omaptype='BST')
    analyzer['energy'] = om.newMap(omaptype='BST')

    analyzer['artistas'] = mp.newMap(numelements=65,
                                   maptype='PROBING',
                                   loadfactor=0.3)
    analyzer['unique_tracks_init'] = mp.newMap(numelements=65,
                                   maptype='PROBING',
                                   loadfactor=0.3)

    #Binary Trees para generos
    analyzer['generos'] = om.newMap(omaptype='BST')
    analyzer['Reggae'] = mp.newMap(numelements=65,
                                   maptype='PROBING',
                                   loadfactor=0.3)
    analyzer['Down-tempo'] = mp.newMap(numelements=65,
                                   maptype='PROBING',
                                   loadfactor=0.3)
    analyzer['Chill-out'] = mp.newMap(numelements=65,
                                   maptype='PROBING',
                                   loadfactor=0.3)
    analyzer['Hip-hop'] = mp.newMap(numelements=65,
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
    #Lista para generos                                   
    analyzer['Nombre_generos'] = lt.newList('ARRAY_LIST')
    analyzer['generos_tempos'] = mp.newMap(numelements=65,
                                   maptype='PROBING',
                                   loadfactor=0.3)
    #arbol binario hash table
    analyzer['track_hashtag'] = om.newMap(omaptype='RBT')
    analyzer['Sentiment_values'] = om.newMap(omaptype='BST')

    analyzer['ferrari'] = mp.newMap(numelements=65,
                                   maptype='PROBING',
                                   loadfactor=0.3)

    return analyzer



def addContent(analyzer, content):
    #Update Binary Trees
    car = content['user_id']+content['track_id']+content['created_at']

    cars = mp.contains(analyzer['ferrari'], car)
    if not cars:

        lt.addLast(analyzer['content_features'], content)
        mp.put(analyzer['artistas'], content['artist_id'], 0)
        mp.put(analyzer['unique_tracks_init'], content['track_id'], 0)
        #Update Binary Trees de caracterización
        updateDescriptionMaps(analyzer['instrumentalness'], content, 'instrumentalness')
        updateDescriptionMaps(analyzer['liveness'], content, 'liveness')
        updateDescriptionMaps(analyzer['speechiness'], content, 'speechiness')
        updateDescriptionMaps(analyzer['danceability'], content, 'danceability')
        updateDescriptionMaps(analyzer['valence'], content, 'valence')
        updateDescriptionMaps(analyzer['acousticness'],content, 'acousticness')
        updateDescriptionMaps(analyzer['energy'], content, 'energy')
        
        #Update Binary Tree
        updateGeneralGeneros(analyzer['generos'], content)
        updateGeneros(analyzer['Reggae'], content, 60, 90)
        updateGeneros(analyzer['Down-tempo'], content, 70, 100)
        updateGeneros(analyzer['Chill-out'], content, 90, 120)
        updateGeneros(analyzer['Hip-hop'], content, 85, 115)
        updateGeneros(analyzer['Jazz and Funk'], content, 120, 125)
        updateGeneros(analyzer['Pop'], content, 100, 130)
        updateGeneros(analyzer['R&B'], content, 60, 80)
        updateGeneros(analyzer['Rock'], content, 110, 140)
        updateGeneros(analyzer['Metal'], content, 100, 160)    

        #Update Binary Tree Tiem
        updateHash(analyzer['track_hashtag'], content)
        mp.put(analyzer['ferrari'], car, 0)
    return analyzer


def addContent_hash(analyzer, content):


    updateHash(analyzer['track_hashtag'], content)
    lt.addLast(analyzer['track_hashtag_lst'], content)

def addSentiment(analyzer, content):
    updateSentiment(analyzer['Sentiment_values'], content)

def updateHash(map, content):
    Hour_value = content['created_at']
    Hour_value = convertHour_to_Node(Hour_value)

    exist_value = om.contains(map, Hour_value)

    if exist_value:
        entry = om.get(map, Hour_value)
        actual_value = me.getValue(entry)
    else:
        actual_value = newHourEntry(content, Hour_value)
        om.put(map, Hour_value, actual_value)
    lt.addLast(actual_value['lstContent'], content)

def updateSentiment(map, content):
    pass

def updateDescriptionMaps(map, content, feature):

    Instrumental_value = float(content[feature])

    exist_value = om.contains(map, Instrumental_value)

   

    if exist_value:
        entry = om.get(map, Instrumental_value)
        actual_value = me.getValue(entry)
    else:
        actual_value = newInstrumentEntry(content, Instrumental_value)
        om.put(map, Instrumental_value, actual_value)

    lt.addLast(actual_value['lstContent'], content)
 




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

def newHourEntry(content, Hour_value):
    entry = {'Hour_value':None, 'lstContent':None}
    entry['Hour_value'] = Hour_value
    entry['lstContent'] = lt.newList('ARRAY_LIST')
    return entry


def content_size(analyzer):
    return lt.size(analyzer['content_features'])

def R_1(feature, analyzer, min_value, max_value):
    lst = om.values(analyzer[feature], min_value, max_value)
    total_artists, total_songs = 0, 0

    unique_artists = mp.newMap(numelements=65,
                                   maptype='PROBING',
                                   loadfactor=0.3)
    tracks = lt.newList('ARRAY_LIST')
    for artist in lt.iterator(lst):

        total_songs += lt.size(artist['lstContent'])
        for artists in lt.iterator(artist['lstContent']):
            if mp.get(unique_artists, artists['artist_id']) is None: 
                 mp.put(unique_artists, artists['artist_id'], 0)
     

            lt.addLast(tracks, artists)

        total_artists = mp.size(unique_artists)

    return total_artists, total_songs, lst, tracks 

def R_2y3(feature_1, feature_2, analyzer, min_value1, 
    max_value1, min_value2, max_value2):
    content_f1 = R_1(feature_1, analyzer, min_value1, max_value1)[3]

    randomness = lt.newList('ARRAY_LIST')

    unique_tracks = mp.newMap(numelements=65,
                                   maptype='PROBING',
                                   loadfactor=0.3)
   
    for content in lt.iterator(content_f1):
        
        if float(content[feature_2]) >= min_value2 and float(content[feature_2]) <= max_value2:
        

            if mp.get(unique_tracks, content['track_id']) is None:   
                mp.put(unique_tracks, content['track_id'], 0)
                lt.addLast(randomness, content)
     
    return mp.size(unique_tracks), randomness

def R_4(analyzer, genero, num, min_value, max_value):

    artist_10 = lt.newList('ARRAY_LIST')

    unique_artists = mp.newMap(numelements=65,
                                   maptype='PROBING',
                                   loadfactor=0.3)
    total_songs, artists, total_artists = 0, 0, 0
    
    if num == 1:
        total_artists = mp.size(analyzer[genero])

        for songs in lt.iterator(mp.valueSet(analyzer[genero])):
            total_songs += lt.size(songs['lstContent'])
            artists += 1
            if artists <= 10:
                artist_id = lt.getElement(songs['lstContent'], 1)
                lt.addLast(artist_10, artist_id['artist_id'])
    else:
        lst = om.values(analyzer['generos'], min_value, max_value)
        
        for artists_lst in lt.iterator(lst):
         
            total_songs += lt.size(artists_lst['lstContent'])
            artists += 1
            for elements in lt.iterator(artists_lst['lstContent']):
                if mp.get(unique_artists, elements['artist_id']) is None:  
                    mp.put(unique_artists, elements['artist_id'], 0)
          
            if artists <= 10:
                artist_id = lt.getElement(artists_lst['lstContent'], 1)
                lt.addLast(artist_10, artist_id['artist_id'])
        total_artists = lt.size(unique_artists)
        

    return total_artists, total_songs, artist_10

def R_5(analyzer, min_hour, max_hour):
    lst = om.values(analyzer['track_hashtag'], min_hour, max_hour)
    total_songs = 0
    for node in lt.iterator(lst):

        total_songs += lt.size(node['lstContent'])
    return total_songs 

def addNewGenero(analyzer, genero):
    lt.addLast(analyzer['Nombre_generos'], genero)

def addNewGenero_Tempo(analyzer, genero, min_tempo, max_tempo):
    tempos = lt.newList('ARRAY_LIST')
    lt.addLast(tempos, min_tempo)
    lt.addLast(tempos, max_tempo)
    mp.put(analyzer['generos_tempos'], genero, tempos)

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

def convertHour_to_Node(Hour_value):
    Hour_value = Hour_value.split(' ')
    Hour_value = Hour_value[1]
    Hour_value = Hour_value.split(':')
    Hour_value = float(Hour_value[0]+'.'+Hour_value[1])
    return Hour_value

def videos_carga(analyzer):
    events = lt.newList('ARRAY_LIST')
    for event in range(1, 11):
        if event < 6:
            video = lt.getElement(analyzer['content_features'], event)
        else:
            video = lt.getElement(analyzer['content_features'], lt.size(analyzer['content_features'])-event)
        lt.addLast(events, video)
    return events


