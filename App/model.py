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
from DISClib.DataStructures import heap as hp
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
    #analyzer['content_features_req5'] = lt.newList('ARRAY_LIST')
    analyzer['track_hashtag'] = lt.newList('ARRAY_LIST')
    analyzer['Sentiment_values'] = lt.newList('ARRAY_LIST')

    #Binary Trees
    analyzer['time_of_event'] = om.newMap(omaptype='BST')
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
    #Árbol Binario Hashtags
    analyzer['track_hashtags'] = om.newMap(omaptype='BST')

    #Árbol Binario Sentiment
    analyzer['sentiment_values'] = om.newMap(omaptype='BST')

    #Árbol Binario Llave Tempo Valor Género
    analyzer['tempo_genero']=om.newMap(omaptype='BST')

    #Arbol Binario Completo Req 5
    analyzer['hash_generos']=om.newMap(omaptype='BST')

  


    return analyzer



        
        #Update Binary Trees de caracterización
# Funciones para agregar informacion al catalogo
def addContent_Hash(analyzer, content):
    updateTrackHash(analyzer,analyzer['track_hashtags'], content)

def addContent_Sentiment(analyzer, content):
    updateSentiment(analyzer['sentiment_values'], content)

def addContent(analyzer, content):
    #lt.addLast(analyzer['content_features'], content)

    car=content['user_id']+content['track_id']+content['created_at']
    cars=mp.contains(analyzer['ferrari'],car)
    if not cars:
        lt.addLast(analyzer['content_features'], content)
        mp.put(analyzer['artistas'], content['artist_id'], 0)
        mp.put(analyzer['unique_tracks_init'], content['track_id'], 0)
        #Update Binary Trees
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
        updateTimeOfEvent(analyzer['time_of_event'], content)
        updateHashGeneros(analyzer,analyzer['hash_generos'],content)
        
    

    return analyzer

'''
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
'''

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

        

#BST con Tablas de Hash
def updateHashGeneros(analyzer,omap,content):
    time = content['created_at']
    newtime = time[11:17]+'00'
    entry = om.get(omap,newtime)
    if entry is None:
        timeentry=newHashTimeEntry(content)
        om.put(omap,newtime,timeentry)
    else:
        timeentry=me.getValue(entry)
    addContent_Hash_Generos(analyzer,timeentry,content)

def addContent_Hash_Generos(analyzer,timeentry,content):
    hash_table=timeentry['mapContent']
    generos=genre_by_tempo(analyzer,content)
    if generos is not None:
        generos=generos['lstContent']['elements'][0]
        for i in lt.iterator(generos):
            entry=mp.get(hash_table,i)
            if entry is None:
                entry={'genero':None,'lstContent':None}
                entry['genero']=i
                entry['lstContent']=lt.newList('ARRAY_LIST')
                newentry=entry
                if i is not None:
                    mp.put(hash_table,i,newentry)
            else:
                newentry=me.getValue(entry)
            addGenreIndex(analyzer,newentry,content)
            

def addGenreIndex(analyzer,entry,content):
    lst0=entry['lstContent']
    #Encontrar el video en el BST de track hash
    track_id=content['track_id']
    user_id=content['user_id']
    created_at=content['created_at']
    keytime=created_at[11:17]+'00'
    entryy=om.get(analyzer['track_hashtags'],content['track_id'])
    if entryy is not None:
        value=me.getValue(entryy)
        hashtags_list=value['lstContent']
        if 'hashtag' not in content:
            content['hashtag']=lt.newList('ARRAY_LIST')
            for i in lt.iterator(hashtags_list):
                if i['created_at']==content['created_at'] and i['user_id']==content['user_id'] and not lt.isPresent(content['hashtag'],i['hashtag']):
                    lt.addLast(content['hashtag'],i['hashtag'])
        elif 'hashtag' in content:
            for i in lt.iterator(hashtags_list):
                if i['created_at']==content['created_at'] and i['user_id']==content['user_id'] and not lt.isPresent(content['hashtag'],i['hashtag']):
                    lt.addLast(content['hashtag'],i['hashtag'])

        lt.addLast(lst0,content)
        
'''
    if entry is not None:
        value=me.getValue(entry)
        hashtable=value['mapContent']
        if mp.contains(hashtable,track_id):
            if 'hashtag' not in content:
                content['hashtag']=lt.newList('ARRAY_LIST')
            entry2=mp.get(hashtable,track_id)
            value2=me.getValue(entry2)
            lst1=value2['lstContent']
            for video in lt.iterator(lst1):
                if video['user_id']==user_id and type(video['hashtag'])==str and (lt.isPresent(content['hashtag'],video['hashtag'])==False):
                    entryvader=om.get(analyzer['sentiment_values'],video['hashtag'])
                    if entryvader is not None:
                        valuevader=(me.getValue(entryvader))
                        valuevaderlist=valuevader['lstContent']
                        element=lt.getElement(valuevaderlist,1)
                        #lt.addLast(content['hashtag'],video['hashtag'].lower())
                        vader_avg=element['vader_avg']
                        if len(vader_avg)>0:
                            lt.addLast(content['hashtag'],video['hashtag'].lower())
            lt.addLast(lst0,content)
'''
           

def newHashTimeEntry(content):
    entry={'created_at':None,'mapContent':None}
    entry['created_at']=content['created_at'][11:17]+'00'
    entry['mapContent']=mp.newMap(numelements=65,
                                maptype='PROBING',
                                loadfactor=0.3)
    return entry 

def genre_by_tempo(analyzer,content):
    tempo=str(round(float(content['tempo'])))
    if float(tempo)>59 and float(tempo)<161:
        genre_entry=om.get(analyzer['tempo_genero'],tempo)
        genre_list=me.getValue(genre_entry)
        return genre_list

def req_5_v_2(analyzer,start_time,end_time):




   
    keys=om.valueSet(analyzer['sentiment_values'])
 
    

    list_of_maps=om.values(analyzer['hash_generos'],start_time,end_time)
    
    registropy = mp.newMap(numelements=65,
                        maptype='PROBING',
                        loadfactor=0.3)

    for hash_table in lt.iterator(list_of_maps):
        keyset=mp.keySet(hash_table['mapContent'])
        for key in lt.iterator(keyset):
            entry=mp.get(hash_table['mapContent'],key)
            videos_list=me.getValue(entry)
            size=lt.size(videos_list['lstContent'])
            lamborghini = mp.get(registropy, key)
            
            if lamborghini is not None: 
                lamborghini = me.getValue(lamborghini)
                lamborghini += size
                mp.put(registropy, key, lamborghini)
            elif lamborghini is None: 
                mp.put(registropy, key, size)

    print('There is a total of '+str(totalreps)+' reproductions between '+start_time+' and '+end_time)
    print('================================ GENRES SORTED REPRODUCTIONS ================================')
    print('Metal unique: '+str(me.getValue(mp.get(registropy, 'Metal_unique'))))
    print('Metal: '+str(me.getValue(mp.get(registropy, 'Metal'))))
    print('Reggae: '+str(me.getValue(mp.get(registropy, 'Reggae'))))
    print('Down-tempo: '+str(me.getValue(mp.get(registropy, 'Down-tempo'))))
    print('Chill-out: '+str(me.getValue(mp.get(registropy, 'Chill-out'))))
    print('Hip-hop: '+str(me.getValue(mp.get(registropy, 'Hip-hop'))))
    print('Pop: '+str(me.getValue(mp.get(registropy, 'Pop'))))
    print('R&B: '+str(me.getValue(mp.get(registropy, 'R&B'))))
    print('Rock: '+str(me.getValue(mp.get(registropy, 'Rock'))))
    print('Jazz and Funk: '+str(me.getValue(mp.get(registropy, 'Jazz and Funk'))))
 
    
    totalreps=0
    genres=mp.keySet(registropy)
    mayor=''
    repsmax=0
    repstemp=0
    for genre in lt.iterator(genres):
        repstemp=me.getValue(mp.get(registropy,genre))
        if repstemp>repsmax:
            repsmax=repstemp
            mayor=genre
        if 'unique' not in genre:
            totalreps+=repstemp
    
    

    all_videos=hp.newHeap(heap_compare)
    for hash_table in lt.iterator(list_of_maps):
        keyset=mp.keySet(hash_table['mapContent'])
        for key in lt.iterator(keyset):
            if key==mayor:
                entry=mp.get(hash_table['mapContent'],key)
                videos_list=me.getValue(entry)
                for video in lt.iterator(videos_list['lstContent']):
                    hp.insert(all_videos,video)
    
    for i in range(1,11):
        video=hp.delMin(all_videos)
        vader_avg=0
        count=0
        for hashtag in lt.iterator(video['hashtag']):
            entry=om.get(analyzer['sentiment_values'],hashtag)
            if entry is not None:
                value=me.getValue(entry)
                lst=value['lstContent']['elements'][0]['vader_avg']
                if lst!='':
                    vader_avg+=float(lst)
                    count+=1
        if count>0:
            vader_avg/=count
        else:
            vader_avg=0
        print('TOP '+str(i)+' track: '+video['track_id']+' with '+str(lt.size(video['hashtag']))+' and VADER = '+str(vader_avg))
        #print(video['track_id'],lt.size(video['hashtag']),video['hashtag']['elements'])
    
    
    
    
    


def heap_compare(video1,video2):
    if lt.size(video1['hashtag'])==lt.size(video2['hashtag']):
        return 0
    elif lt.size(video1['hashtag'])<lt.size(video2['hashtag']):
        return 1
    else:
        return -1


def updateTempoGenero(omap):
    tempo=60
    while tempo<=160:
        tempolist=lt.newList('ARRAY_LIST')
        if tempo>=60 and tempo<=90:
            lt.addLast(tempolist,'Reggae')
        if tempo>=70 and tempo<=100:
            lt.addLast(tempolist,'Down-tempo')
        if tempo>=90 and tempo <=120:
            lt.addLast(tempolist,'Chill-out')
        if tempo>=85 and tempo<=115:
            lt.addLast(tempolist,'Hip-hop')
        if tempo>=120 and tempo<=125:
            lt.addLast(tempolist,'Jazz and Funk')
        if tempo>=100 and tempo<=130:
            lt.addLast(tempolist,'Pop')
        if tempo>=60 and tempo<=80:
            lt.addLast(tempolist,'R&B')
        if tempo>=110 and tempo<=140:
            lt.addLast(tempolist,'Rock')
        if tempo>=100 and tempo<=160:
            lt.addLast(tempolist,'Metal')
        if tempo>140 and tempo<=160:
            lt.addLast(tempolist, 'Metal_unique')
        entry=om.get(omap,str(tempo))
        if entry is None:
            tempoentry=newTempoEntry(str(tempo))
            om.put(omap,str(tempo),tempoentry)
        else:
            tempoentry=me.getValue(entry)
        lt.addLast(tempoentry['lstContent'],tempolist)
        tempo+=1

def newTempoEntry(tempo):
    entry={'tempo':None,'lstContent':None}
    entry['tempo']=str(tempo)
    entry['lstContent']=lt.newList('ARRAY_LIST')
    return entry


def updateTimeOfEvent(omap,content):
    time = content['created_at']
    newtime = time[11:17]+'00'
    entry = om.get(omap,newtime)
    if entry is None:
        timeentry=newTimeEntry(content)
        om.put(omap,newtime,timeentry)
    else:
        timeentry=me.getValue(entry)
    addTimeIndex(timeentry,content)

def addTimeIndex(timeentry,content):
    lst=timeentry['lstContent']
    lt.addLast(lst,content)

def newTimeEntry(content):
    entry={'created_at':None,'lstContent':None}
    entry['created_at']=content['created_at'][11:17]+'00'
    entry['lstContent']=lt.newList('ARRAY_LIST')
    return entry 

    





def updateHash(omap,content):
    updateTimeOfEvent(omap,content)

def updateSentiment(omap,row):
    hashtag=row['hashtag']
    entry=om.get(omap,hashtag)
    if entry is None:
        sentiment_entry=newSentimentEntry(row)
        om.put(omap,hashtag,sentiment_entry)
    else:
        sentiment_entry=me.getValue(entry)
    lt.addLast(sentiment_entry['lstContent'],row)
    

def newSentimentEntry(row):
    entry={'hashtag':None,'lstContent':None}
    entry['hashtag']=row['hashtag']
    entry['lstContent']=lt.newList('ARRAY_LIST')
    return entry
'''
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
'''
'''
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
'''
'''
def newInstrumentEntry(content, Instrumental_value):

    entry = {'Instrument_value': None, 'lstContent':None}
    entry['Instrument_value'] = Instrumental_value
''' 

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


#Carga BST Track Hashtags

def updateTrackHash(analyzer,omap,content):
    trackid = content['track_id']
    entry = om.get(omap,trackid)
    if entry is None:
        timeentry=newHashTrackIDEntry(content)
        om.put(omap,trackid,timeentry)
    else:
        timeentry=me.getValue(entry)
    addContent_Track_Hash(analyzer,timeentry,content)

def addContent_Track_Hash(analyzer,timeentry,content):
    lst=timeentry['lstContent']
    track_id=content['track_id']
    dicti_revision={'hashtag':content['hashtag'].lower(),'created_at':content['created_at'],'user_id':content['user_id']}
    estaono=False
    for i in lt.iterator(lst):
        if i==dicti_revision:
            estaono=True
    if not estaono:
        lt.addLast(lst,{'hashtag':content['hashtag'].lower(),'created_at':content['created_at'],'user_id':content['user_id']})


def newHashTrackIDEntry(content):
    entry={'track_id':None,'lstContent':None}
    entry['track_id']=content['track_id']
    entry['lstContent']=lt.newList('ARRAY_LIST')
    return entry 
