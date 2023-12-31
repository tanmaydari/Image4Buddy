from flask import Flask, jsonify
import openai
from flask import render_template
from config import key

openai.api_key = key
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html',)
@app.route('/generateimages/<prompt>')
def generate(prompt):
  print("Prompt :",prompt)
  response=openai.Image.create(prompt=prompt,n=5,size="256x256")
  print(response)
  return jsonify(response)


app.run(host='0.0.0.0', port=81)
