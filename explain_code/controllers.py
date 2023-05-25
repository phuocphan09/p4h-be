import os

import openai
from dotenv import load_dotenv
load_dotenv()
# openai.api_key = os.environ.get('OPENAI_API_KEY')

openai.api_key = "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"
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
