import os
from flask import Flask,redirect,render_template,request,url_for
import openai

app = Flask(__name__)

openai.api_key=os.getenv("OPENAI_API_KEY")

#route
@app.route("/",methods=("GET","POST"))
def index():
    if request.method=="POST":
        chat=request.form["chat"]
        try:
            response = openai.Completion.create(
                model="text-davinci-001",
                prompt=generate_prompt(chat),    
            )
            print(response)
            return redirect(url_for("index", result=response.choices[0].text))
        except Exception as e:
            error_message = f"Error:{e}"
            return redirect(url_for("index", result=error_message))
    result = request.args.get("result")
    return render_template("index.html", result=result)    

def generate_prompt(chat): 
        return """
        Emojify Movie name:
    movie: lion king
    emoji:🦁👑
    movie:The dark knight
    emoji:🌃🦇🗡️ 
    movie:{}
    emoji:""".format(chat.capitalize()
                          )

