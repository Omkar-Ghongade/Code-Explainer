from flask import Flask, jsonify, redirect,render_template,request
import openai
import isvalid
# from dotenv import load_dotenv
openai.api_key =""



app = Flask(__name__)

def openAI(question):
    print("In AI")
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k",  
        messages=[
            {
            "role": "system",
            "content": question
            },
            {
            "role": "user",
            "content": ""
            }
        ],
        temperature=1,
        max_tokens=13952,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response["choices"][0]["message"]["content"]



@app.route('/')
def index():
	return render_template('index.html',data="",Heading="",Details="",ApiKey="")

@app.route('/', methods=['POST','GET'])
def code():
    input_text = request.form['code-input']
    apikey=request.form['input-box']
    if isvalid.valid(apikey)==0:
        return render_template('index.html',data=input_text,Heading="Enter Correct API Key",Details="",ApiKey=apikey)
    openai.api_key=apikey
    print(input_text)
    input_text+="                                         "
    input_text+="\n Explain me this code step by step"
    Ans=openAI(input_text)
    Answer=[]
    S=""
    pos=int(0)
    print(Ans)
    hding="Code Explanation"
    Data=request.form['code-input']
    return render_template('index.html',data=Data,Heading=hding,Details=Ans,ApiKey=apikey)




# main driver function
if __name__ == '__main__':
	app.run(debug=True)
