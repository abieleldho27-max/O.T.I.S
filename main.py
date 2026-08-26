from fastapi import FastAPI
from pydantic import BaseModel
import requests
import json
print ("starting")
app = FastAPI()
url = "http://localhost:11434/api/chat"
systemPrompt = "Your response should be in sentence form, and no more than 100 words long. respond with minimal information. If you would like to move, create a json element titled 'actions' with all directions and the amount of time in milliseconds you would like to move in that direction for in the order that is provided. you can repeat elements/directions if necessary. The 4 directions are forward, backward, spin left, and spin right. Title the direction element as 'direction', and the time element as 'time'. If you want to respond to a question, include your actions with a json titled 'response' with your response."
history = []
historyElementCount = 0
class promptData(BaseModel):
    model: str
    role: str
    prompt: str
    images: str = None
    stream: bool
@app.post("/post/")
def recieve_ESPdata(promptdata : promptData):
    print("sending data")
    history.append({'role': 'system', 'content': systemPrompt})
    if (promptdata.images != None):
        history.append({'role': promptdata.role, 'content': promptdata.prompt, 'images': [promptdata.images]})
    else:
        history.append({'role': promptdata.role, 'content': promptdata.prompt})
    directionsFormat = {'forward': {'type': 'integer'}, 'backward': {'type': 'integer'}, 'spin left': {'type': 'integer'}, 'spin right': {'type': 'integer'}, 'response': {'type': 'string'}}
    jsonFormat = {'type': 'object', 'required': ['response', 'directions']}
    headers = {'content-type' : 'application/json'}
    messages = {'role': 'user', 'content': 'what is the capital of france'}
    jsonData = {'model': promptdata.model, 'messages': history, 'format': 'json', 'stream': False}
    response = requests.post(url=url, json=jsonData, headers=headers)
    result = json.loads(response.text)
    history.append(result)
    if (len(history) >= 12):
        while (len(history) > 10):
            history.pop(1)
    print("response: ")
    print(result['message']['content'])
    return(result['message']['content'])
    
    
   
                    
    