from typing import Any
from fastapi import APIRouter, Depends,Form
from pymongo import MongoClient
import json
from bson import ObjectId
from datetime import datetime

# CONNECTION_STRING = "mongodb+srv://patilharshad:VgEyLG5StaSiFHLG@cluster.mongodb.net/rabbitmq_messages"
CONNECTION_STRING = "mongodb://localhost:27017/rabbitmq_messages"  

client = MongoClient(CONNECTION_STRING)

db = client["rabbitmq_messages"]

router = APIRouter()

class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        if isinstance(obj, datetime):
            return obj.isoformat()
        return json.JSONEncoder.default(self, obj)

@router.post("/read_api")
def read_api(start_time:str =Form(),
             end_time:str =Form()
    ) -> Any:

    query =   [
    {
        "$match": {
            "time": {
                "$gte": start_time,
                "$lte": end_time
            }
        }
    },
    {
        "$addFields": {
            "Values": {"$toInt": "$status"}
        }
    },
    {
        "$group": {
            "_id": "$Values",
            "count": {"$sum": 1}
        }
    }
    ]
    results = db.message.aggregate(query)
    
    response = []

    for document in results:
        response.append(document)
    
    res = json.dumps(response,cls=JSONEncoder)
    
    return {
        "data":json.loads(res)
    }