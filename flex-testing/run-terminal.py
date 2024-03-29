from datetime import datetime

import requests

def chat(chat_history):
    chat_history='\n'.join(chat_history)+'\nASSISTANT:'
    api_url = 'http://0.0.0.0:8007/completion'
    json_body = {
        "stream": False,
        "n_predict":400,
        "temperature":0.02,
        "stop": [
            "</s>",
            "Llama:",
            "User:",
            "ASSISTANT:",
            "USER:"],
        "repeat_last_n":256,
        "repeat_penalty":1.18,
        "top_k":40,
        "top_p":0.5,
        "tfs_z":1,
        "typical_p":1,
        "presence_penalty":0.18,
        "frequency_penalty":0.37,
        "mirostat":2,
        "mirostat_tau":5,
        "mirostat_eta":0.1,
        "grammar":"",
        "n_probs":1,
        "image_data": [],
        "cache_prompt":True,
        "slot_id":0,
        "prompt":f"{chat_history}"
    }
    r = requests.post(api_url, json=json_body)
    print(r.json())
    return r.json()['content']

chat_history = ["SYSTEM: You are a helpful assistant."]
while True:
    query = input('du:  ')
    if query == 'quit':
        exit()
    else:
        time_now = datetime.now().strftime("%H:%M:%S")
        chat_history.append(f"[{time_now}]USER:{query}")
        try:
            ai_response = chat(chat_history)
        except Exception as e :
            print(f"Exception: {e}")
            ai_response = "I'm sorry, I don't know what to say."
        print(f"ai: {ai_response}")
        time_now = datetime.now().strftime("%H:%M:%S")
        chat_history.append(f"[{time_now}]ASSISTANT:{ai_response}")
