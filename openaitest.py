import os
import openai

openai.api_key = os.getenv("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")

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