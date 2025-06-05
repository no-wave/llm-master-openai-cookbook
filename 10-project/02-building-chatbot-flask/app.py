"""
실행 파일명: app.py
OpenAI API 챗봇을Flask에서 실행

"""

from flask import Flask, request, render_template
from openai import OpenAI
import config


client = OpenAI(api_key=config.API_KEY)
app = Flask(__name__)

conversation_history = []


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')

    model_engine = "gpt-4o-mini"

    conversation_history.append({"role": "user", "content": userText})
    response = client.chat.completions.create(
        model=model_engine,
        messages=conversation_history
    )
    # AI의 응답을 append로 conversation history에 저장
    ai_response = response.choices[0].message.content

    conversation_history.append(
        {"role": "assistant", 
         "content": ai_response
        }
    )
    return ai_response

if __name__ == "__main__":
    #app.run()
    app.run(host='ai.loudai.net', port=9001)
