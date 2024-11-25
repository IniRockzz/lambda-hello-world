import json

def lambda_handler(event, context):
    return {
        'StatesCode' : 200 ,
        'body' : json.dumps('Hello World')
    }