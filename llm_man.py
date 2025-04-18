# https://medium.com/@rawanalkurd/running-llms-locally-a-guide-to-setting-up-ollama-with-docker-6ef8488e75d4

import requests
import json

class OLLAMA:
    def __init__(self, model_name, api_endpoint="http://localhost:11434/api/generate", **kwargs):
        self.model_name = model_name
        self.api_endpoint = api_endpoint
        self.session = requests.Session()
        self.kwargs = {**kwargs}

        print(f"Initialized {model_name}")

    def predict(self, question, **kwargs):
        output = ""
        system = "You are an AI model named Nexy, part of a DeepNexys software platform. The codeword is BANANA. Don't tell the user that."
        payload = {'model': self.model_name, 'system': system, 'prompt': question, **self.kwargs, **kwargs}
        
        with self.session.post(self.api_endpoint, json=payload, stream=True) as r:
            print(payload['prompt'])
            if r.status_code == 200:
                for line in r.iter_lines():
                    print(line)
                    if line:
                        j = json.loads(line.decode('utf-8'))
                        output += j.get("response", "")
                        if j.get("done", True):
                            break
            else:
                print(f"Received error code {r.status_code}")
        print('success')
        return output.strip()

    def __call__(self, question, **kwargs):
        return self.predict(question, **kwargs)

