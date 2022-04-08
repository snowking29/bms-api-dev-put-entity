import json
import traceback
from service.entity import update

def handler(event, context):
    print("Evento recibido: ",json.dumps(event))
    path = event["pathParameters"]["entity"]
    params = event["queryStringParameters"]
    try:
        body = json.loads(event['body'])
        response = update(body,path,params)
        
    except Exception as e:
        traceback.print_exc()
        response = {"exception",str(e)}
    
    return {
        "statusCode": 200,
        "body": json.dumps(response)
    }