from openai import OpenAI

# Use OpenAI API Key
client = OpenAI(
    api_key="<OpenAI Key를 여기에 붙혀넣기하세요.>"
)

# Ask the user for question
question = input("당신이 하고 싶은 Task에 대하여 요청해주세요? ")
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": f"{question}"},
    ],
    max_tokens=512,
    n=1,
    stop=None,
    temperature=0.8,
)
print(response)
answer = response.choices[0].message.content
print("OpenAI:" + answer)
