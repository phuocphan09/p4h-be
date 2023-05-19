import os

import openai
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.environ.get('OPENAI_API_KEY')

completion = openai.ChatCompletion()

def ask_gpt(question, messages=None):
    if messages is None:
        messages = [{
            'role': 'system',
            'content': 'You are a intelligent assistant.',
        }]
    messages.append(
        {"role": "user", "content": question},
    )
    chat = completion.create(
        model="gpt-3.5-turbo", messages=messages
    )
    reply = chat.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})
    return reply, messages
