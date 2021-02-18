# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 12:31:08 2021

@author: kkhatua
"""

import pandas
import datetime
from sys import getsizeof   # This will help to determine how much memory (in MB) a variable consumes in the memory.
import zipfile
import os 


os.chdir("C:\\Users\\kkhatua\\Desktop\\Kaustav Khatua\\PUBG Finish Placement Prediction")

zf = zipfile.ZipFile("train_V2.csv.zip")

# Reading normally and getting the time and memory.
start_time = datetime.datetime.now()
data_table = pandas.read_csv(zf.open('train_V2.csv'))
print(datetime.datetime.now() - start_time)

# Getting the size of data_table in MB.
print(getsizeof(data_table) / (1024 * 1024))



# Getting the column names for future use.
print(data_table.columns)

# Deleting the table.
del data_table


# Specifying the data types of the columns to Pandas.
dtypes_list = ["object",  # Id
               "object",  #  groupId
               "object", #matchId
               "int8", #assists
               "int8", #boosts
               "float16",# damageDealt
               "int8", #DBNOs
               "int8", #headshotKills
               "int8", #heals
               "int8", #killPlace
               "int16", #killPoints
               "int8",#kills
               "int8", #killStreaks
               "float16",#longestKill
               "int16",#matchDuration
               "object",#matchType
               "int8", #maxPlace
               "int8",#numGroups
               "int16",#rankPoints
               "int8", #revives
               "float16", #rideDistance
               "int8",#roadKills
               "float16",#swimDistance
               "int8",#teamKills
               "int8",#vehicleDestroys
               "float16",#walkDistance
               "int8",#weaponsAcquired
               "int16",#winPoints
               "float16"#winPlacePerc
               ]

dtypes_dict = dict(zip(['Id', 'groupId', 'matchId', 'assists', 'boosts', 'damageDealt', 'DBNOs',
       'headshotKills', 'heals', 'killPlace', 'killPoints', 'kills',
       'killStreaks', 'longestKill', 'matchDuration', 'matchType', 'maxPlace',
       'numGroups', 'rankPoints', 'revives', 'rideDistance', 'roadKills',
       'swimDistance', 'teamKills', 'vehicleDestroys', 'walkDistance',
       'weaponsAcquired', 'winPoints', 'winPlacePerc'], dtypes_list))

# Modified approach to read the same data.
start_time = datetime.datetime.now()
#data_table = pandas.read_csv("train_V2.csv", dtype = dtypes_dict)
data_table = pandas.read_csv(zf.open('train_V2.csv'), dtype = dtypes_dict)
print(datetime.datetime.now() - start_time)

# Getting the size of data_table in MB.
print(getsizeof(data_table) / (1024 * 1024))