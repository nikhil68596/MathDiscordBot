from multiprocessing.dummy import Array
from typing import Dict
from mongoengine import *
import os
import pymongo
connect("https://cloud.mongodb.com/v2/6259feff28500970d443cfe3#metrics/replicaSet/627182de6a9ed048960ed289/explorer/LinearCombsDiscord")
import json 

class matricesvectors(Document):
    id = StringField(unique = True, required = True)
    nameOnDiscord = StringField(unique = True, required = True)
    matrix = DictField()
    vectorOfRN = DictField()
    resultingVectorOfRM = DictField()

def json(self):
    user_dict = {
        "id": self.id,
        "nameOnDiscord": self.nameOnDiscord,
        "matrix": self.matrix, 
        "vectorOfR^N": self.vectorOfRN,
        "resultingVectorOfR^M": self.resultingVectorOfRM
    }
    return json.dumps(user_dict)

meta = {
    "indexes": ["id"],
    "ordering": ["nameOnDiscord"]
}