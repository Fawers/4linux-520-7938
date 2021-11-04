from bson.objectid import ObjectId
from bson import json_util as bson
import pymongo

client = pymongo.MongoClient()
timers_db = client.timers
timers_coll = timers_db.timers


def criar_timer(timer):
    timer_doc = dict(vars(timer))
    timer_doc['duracao'] = timer_doc['duracao'].total_seconds()
    timer_doc['concluido'] = False

    result = timers_coll.insert_one(timer_doc)
    return result.inserted_id


def concluir_timer(obj_id):
    busca = {'_id': obj_id}
    substituicao = {'$set': {'concluido': True}}
    res = timers_coll.update_one(busca, substituicao)
    return res.acknowledged


def listar_todos():
    return timers_coll.find()
