import uuid
import json
import bson
import traceback
import pymongo as py
from db_util.get_connection import mongodb_connection
from db_util.get_document import mongodb_document

def update(body,entity,params):
    conn = mongodb_connection()
    print("Info Base de datos: ", conn.server_info())
    
    if conn is None:
        return

    try:
        collection = conn.bmsDB[entity]
    except py.errors.CollectionInvalid as e:
        traceback.print_exc()
        print("No se encontró la colección en la base de datos: %s" %e)
    
    print(params)
    
    if "key" in params:
        key = params["key"]
    else:
        key = ""
    
    registerFound = mongodb_document(collection,key)
    print("Se encontró key?: ", registerFound)
    
    if registerFound:
        try:
            collection.update({'key':key}, {'$set': body})
            success = "true"
            code = "00"
            value = "Se actualizó satisfactoriamente."
        except Exception as e:
            print("Error al insertar documento en base de datos: %s" %e)
    else:
        success = "false"
        code = "01"
        value = "No se encontró registro en la base de datos."
    
    conn.close() 
    
    response = {
        "key":key,
        "success": success,
        "configuration": {
            "meta": {
                "status": {
                    "code": code,
                    "message_ilgn": [{
                        "locale": "es_PE",
                        "value": value
                    }]
                }
            }
        }
    }
    print("Response payload: ", json.dumps(response))
    return response