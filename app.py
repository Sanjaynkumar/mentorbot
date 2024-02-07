#from chatbot import CB
from flask import Flask, render_template, request
import backend as svhs
#import blender as blender

app = Flask(__name__)

@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/")
def homepage():
    return render_template("home.html")

@app.route("/get")
def get_bot_response():
    #print("\n \n Please enter the query\n")
    query = request.args.get('msg')
    response1 = svhs.query_engine.query(query)
    # print("response 1")
    # print(response1)
    #query_results = svhs.query_engine.query(query)
    score = response1.source_nodes[0].score
    # response2 = blender.llm_chain.run(query)
    response2 = "Hi"
    # print("response 2")
    # print(response2)
    final =""

    if(score > -1):
        final = response1
    else:
        prompt = " I'm sorry! I am still a beta version & you are asking something out of my knowledge base (Zero to IPO by David Smith).  Please stick to the domain knowledge. However, I can converse with my artfical inteligence. "
        final = prompt+ "\n"+ response2
    print(final)
    return str(final)



app.run(debug = False)
