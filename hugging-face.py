import requests

API_URL = "https://api-inference.huggingface.co/models/rasa/LaBSE"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
output = query({
	"inputs": "Today is a sunny day and I'll get some ice cream.",
})

print(output)