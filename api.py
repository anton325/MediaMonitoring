import openai
import prepare_query

def ask_chatgpt(introduction,articles_to_be_judged,version = 3):
    key = "API_KEY"
    openai.api_key = key
    messages=[
            {"role": "system", "content": introduction},
            {"role": "user", "content": articles_to_be_judged}
        ]
    # print(openai.Model.list())
    if version == 3:
        model = "gpt-3.5-turbo"
    elif version == 4:
        model = "gpt-4"
    else:
        raise Exception("Select a version")
    chat = openai.ChatCompletion.create( 
                model=model, messages=messages 
            )
    reply = chat.choices[0].message.content 
    print(reply)
    prepare_query.save_answer(reply)
    return reply

