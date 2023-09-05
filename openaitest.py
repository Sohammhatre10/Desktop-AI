import os
import openai

openai.api_key = os.getenv("your api-key here")

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Write an apllication for artificial intelligence internship",
  temperature=0.7,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
print(response)
