import os
import openai
#openai.organization = "YOUR_ORG_ID"
openai.api_key = 'YOUR_API_KEY'
#openai.Model.list()

#response = openai.Image.create(
  prompt="a baby panda",
  n=1,
  size="1024x1024"
)
image_url = response['data'][0]['url']

print(response)
