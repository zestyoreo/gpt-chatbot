API_KEY = "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"
import openai
import os

os.environ["OPENAI_API_KEY"] = API_KEY
openai.api_key = os.environ["OPENAI_API_KEY"]

_prompt = True
while _prompt:
    prompt = input("You: (type 'bye' to exit)")
    if prompt=="bye":
        _prompt = False
    else:
        response = openai.Completion.create(engine="text-davinci-003", prompt=prompt, max_tokens=150)
        print("Bot: " + response.choices[0].text)