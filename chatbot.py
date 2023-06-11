import gradio as gr
import openai

openai.api_key = ' ' #enter your API-Key here

message_history = [{"role": "user", "content": f"You are a therapy bot. Where I will tell you the problem you must give a solution. If you understand, say OK."},
                   {"role": "assistant", "content": f"OK"}]

def predict(input):
    message_history.append({"role": "user", "content": f"{input}"})

    completion = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=message_history
    )
    reply_content = completion.choices[0].message.content
    print(reply_content)
    message_history.append({"role": "assistant", "content": f"{reply_content}"}) 
    response = [(message_history[i]["content"], message_history[i+1]["content"]) for i in range(2, len(message_history)-1, 2)]
    return response

with gr.Blocks() as demo: 

    TherapyBot = gr.Chatbot() 

    with gr.Row(): 
        txt = gr.Textbox(show_label=False, placeholder="Enter text and press enter").style(container=False)

    txt.submit(predict, txt, TherapyBot)
    txt.submit(None, None, txt, _js="() => {''}")

demo.launch()
