import os
import openai

# API_KEY = os.environ['OPENAI_API_KEY']
API_KEY = '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'
openai.api_key = API_KEY


def get_response(prompt, model="gpt-3.5-turbo"):
    messages = [
        {"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message['content']
