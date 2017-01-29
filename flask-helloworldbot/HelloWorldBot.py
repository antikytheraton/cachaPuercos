#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask, request,jsonify
from sklearn.externals import joblib
from sklearn import svm,metrics
import requests
import json
import traceback
import random
import ner

formulario=False
subject='---'
def returnText(array):
    text=''
    aux=True
    array.remove("*")
    if len(array)==0:
        return "no se como responder a eso"
    if "p" in array:
        if "a" in array:
            text = text+"debes pagar una multa, la multa por invadir el paso peatonal es de 1399 a 2098 pesos"# te podemos ayudar a llenar el formulario que te recuerde cuando pagar"
        elif "b" in array:
            text =text+"debes pagar una multa por no respetar la luz roja, el costo de la multa va de 699.5 a 2098.5 pesos" #te podemos ayudar a llenar el formulario que te recuerde cuando pagar"
        elif "c" in array:
            text=text+"debes pagar una multa por dar una vuelta prohibida, el costo va de 1399 a 2098.5 pesos" #te  podemos ayudar a llenar el formulario que te recuerde cuando pagar"
        elif "d" in array:
            text=text+"debes pagar una multa por no usar el cinturón de seguridad, el costo va de 345 a 699.5 pesos"# te  podemos ayudar a llenar el formulario que te recuerde cuando pagar"
        elif "e" in array:
            text=text+"debes pagar una multa por usar distractores mientras manejas, el costo va de 345 a 699.5 pesos" # te  podemos ayudar a llenar el formulario que te recuerde cuando pagar"
        else:
            text=text+"las razones para obtener una multa, dime que justificación de te el transito"
        aux=False

    if "j" in array and aux:
        text=text+" recuerda que no importa el motivo, un oficial sólo puede hacer que bajes de tu vehículo si cometiste un delito"
    if "k" in array and aux:
        text=text+" en el nuevo reglamento, solo hay dos razones para que te decomisen el vehículo es manejar bajo efecto del alcohol o invadir el carril del metrobus o bici"
    if "l" in array and aux:
        text=text+" si un oficial te pide tu licencia o papeles de tu auto, debes mostrarlos."
    if "a" in array and aux:
        text = text+" debes pagar una multa, la multa por invadir el paso peatonal es de 1399 a 2098 pesos, te podemos ayudar a llenar el formulario que te recuerde cuando pagar"
    if "b" in array and aux:
        text =text+" debes pagar una multa por no respetar la luz roja, el costo de la multa va de 699.5 a 2098.5 pesos, te podemos ayudar a llenar el formulario que te recuerde cuando pagar"
    if "c" in array and aux:
        text=text+" debes pagar una multa por dar una vuelta prohibida, el costo va de 1399 a 2098.5 pesos, te  podemos ayudar a llenar el formulario que te recuerde cuando pagar"
    if "d" in array and aux:
        text=text+" debes pagar una multa por no usar el cinturon de seguridad, el costo va de 345 a 699.5 pesos, te  podemos ayudar a llenar el formulario que te recuerde cuando pagar"
    if "e" in array and aux:
        text=text+" debes pagar una multa por usar distractores mientras manejas, el costo va de 345 a 699.5 pesos, te  podemos ayudar a llenar el formulario que te recuerde cuando pagar"
    return text





app = Flask(__name__)

token = "EAAaDD6sABdABAIW5W278rCMLMRhMZAZCvNi1AjZATJ64eDFlZBUNwuqMbDEGqnVwmg8X7e2XNpjYcDZCKHm4OVpfPU0AfYvvVUZBPMyRmr7l1wnLyygFTJMXZBLQYqkA0bVDG5bDr4L70HDOLAOsh3fdK6nDV4TVt6qADR4GfXpYQZDZD"

@app.route('/bot', methods=['GET', 'POST'])
def webhook():
  if request.method == 'POST':
    try:
      data = json.loads(request.data)
      print(data)

      text = data['entry'][0]['messaging'][0]['message']['text'] # Incoming Message Text
      sender = data['entry'][0]['messaging'][0]['sender']['id'] # Sender ID
      lista,clases=ner.getNer(text)
      payload = {'recipient': {'id': sender}, 'message': {'text':returnText(list(set(clases)))}} # We're going to send this back
      r = requests.post('https://graph.facebook.com/v2.6/me/messages/?access_token=' + token, json=payload) # Lets send it
    except Exception as e:
      print traceback.format_exc() # something went wrong
  elif request.method == 'GET': # For the initial verification
    if request.args.get('hub.verify_token') == 'cachaPuercos':
      return request.args.get('hub.challenge')
    return "Wrong Verify Token"
  return "Hello World" #Not Really Necessary
@app.route('/api', methods=['GET', 'POST'])
def api():
  if request.method == 'POST':
    try:
      data = json.loads(request.data)
      print(data)

      text = data['text']
      lista,clases=ner.getNer(text)
      resp ={}
      resp["text"]=returnText(list(set(clases)))
      resp["formulario"]=False
      resp["subject"]= "---"

      return jsonify(results=resp)

    except Exception as e:
      print traceback.format_exc() # something went wrong
  elif request.method == 'GET': # For the initial verification
    if request.args.get('hub.verify_token') == 'cachaPuercos':
      return request.args.get('hub.challenge')
    return "Wrong Verify Token"
  return "Hello World" #Not Really Necessary

if __name__ == '__main__':
  app.run(debug=True)
