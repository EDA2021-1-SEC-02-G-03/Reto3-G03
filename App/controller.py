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
 """

import config as cf
import model
import datetime
import csv
import time
import tracemalloc


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""



def init():

    analyzer = model.newAnalyzer()
    return analyzer


def loadData(analyzer, content_file):

    content_file = cf.data_dir + content_file
    input_file = csv.DictReader(open(content_file, encoding="utf-8"), delimiter=",")

    for content in input_file:
        model.addContent(analyzer, content)
    return analyzer

def loadDataHashTrack(analyzer, hashtags_file):
    hashtags_file = cf.data_dir + hashtags_file
    input_file = csv.DictReader(open(hashtags_file, encoding='utf-8'), delimiter=',')

    for content in input_file:
        model.addContent_Hash(analyzer,content)
    return analyzer

def loadDataSentiment(analyzer, sentiment_values_file):
    sentiment_values_file = cf.data_dir + sentiment_values_file
    input_file = csv.DictReader(open(sentiment_values_file, encoding='utf-8'), delimiter=',')
    for hashtag in input_file:
        model.addContent_Sentiment(analyzer,hashtag)
    return analyzer
    

def loadListGeneros(analyzer):
    addNewGenero(analyzer, 'Reggae')
    addNewGenero(analyzer, 'Down-tempo')
    addNewGenero(analyzer, 'Chill-out')
    addNewGenero(analyzer, 'Hip-hop')
    addNewGenero(analyzer, 'Jazz and Funk')
    addNewGenero(analyzer, 'Pop')
    addNewGenero(analyzer, 'R&B')
    addNewGenero(analyzer, 'Rock')
    addNewGenero(analyzer, 'Metal') 

def loadListTempos(analyzer):
    addNewGenero_Tempo(analyzer, 'Reggae', 60, 90)
    addNewGenero_Tempo(analyzer, 'Down-tempo', 70, 100)
    addNewGenero_Tempo(analyzer, 'Chill-out', 90, 120)
    addNewGenero_Tempo(analyzer, 'Hip-hop', 85, 115)
    addNewGenero_Tempo(analyzer, 'Jazz and Funk', 120, 125)
    addNewGenero_Tempo(analyzer, 'Pop', 100, 130)
    addNewGenero_Tempo(analyzer, 'R&B', 60, 80)
    addNewGenero_Tempo(analyzer, 'Rock', 110, 140)
    addNewGenero_Tempo(analyzer, 'Metal', 100, 160)


def content_size(analyzer):
    return model.content_size(analyzer)

def R_1(feature, analyzer, min_value, max_value):
    return model.R_1(feature, analyzer, min_value, max_value)

def R_2y3(feature_1, feature_2, analyzer, min_value1, 
    max_value1, min_value2, max_value2):
    return model.R_2y3(feature_1, feature_2, analyzer, min_value1, 
    max_value1, min_value2, max_value2)

def R_4(analyzer, genero, num, min_value, max_value):
    return model.R_4(analyzer, genero, num, min_value, max_value)

def R_5(analyzer,start_time,end_time):
    return model.req_5_v_2(analyzer,start_time,end_time)


def random_selector(lst):
    return model.random_selector(lst)

def addNewGenero(analyzer, genero):
    return model.addNewGenero(analyzer, genero)

def addNewGenero_Tempo(analyzer, genero, min_tempo, max_tempo):
    return model.addNewGenero_Tempo(analyzer, genero, min_tempo, max_tempo)

def convertHour_to_Node(Hour_value):
    return model.convertHour_to_Node(Hour_value)

def videos_carga(analyzer):
    return model.videos_carga(analyzer)

def getTime():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)

def getMemory():
    """
    toma una muestra de la memoria alocada en instante de tiempo
    """
    return tracemalloc.take_snapshot()

def deltaMemory(start_memory, stop_memory):
    """
    calcula la diferencia en memoria alocada del programa entre dos
    instantes de tiempo y devuelve el resultado en bytes (ej.: 2100.0 B)
    """
    memory_diff = stop_memory.compare_to(start_memory, "filename")
    delta_memory = 0.0

    # suma de las diferencias en uso de memoria
    for stat in memory_diff:
        delta_memory = delta_memory + stat.size_diff
    # de Byte -> kByte
    delta_memory = delta_memory/1024.0
    return delta_memory
