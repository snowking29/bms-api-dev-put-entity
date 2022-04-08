import bson
import traceback
import pymongo as py
import json

def mongodb_document(collection,key):
    try:
        register = json.loads(json.dumps(list(collection.find({"key":key},{"_id":0}))))
        
        if len(register) == 0:
            foundkey = False
        else:
            foundkey = True
        return foundkey
    
    except Exception as e:
        traceback.print_exc()
        print("Error al intentar obtener documento: %s" %e)