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


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros

def init():

    analyzer = model.newAnalyzer()
    return analyzer

# Funciones para la carga de datos

def loadData(analyzer, content_file):

    content_file = cf.data_dir + content_file
    #Aquí se genera el error, no encuentra el archivo
    input_file = csv.DictReader(open(content_file, encoding="utf-8"), delimiter=",")

    for content in input_file:
        model.addContent(analyzer, content)
    return analyzer

# Funciones de consulta sobre el catálogo

def content_size(analyzer):
    return model.content_size(analyzer)

def R_1(feature, analyzer, min_value, max_value):
    return model.R_1(feature, analyzer, min_value, max_value)

def R_2(feature_1, feature_2, analyzer, min_value1, 
    max_value1, min_value2, max_value2):
    return model.R_2(feature_1, feature_2, analyzer, min_value1, 
    max_value1, min_value2, max_value2)

def random_selector(lst):
    return model.random_selector(lst)
# Funciones de ordenamiento