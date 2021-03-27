import pytz
import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()


import numpy
import tflearn
import tensorflow
import random
import json
from types import SimpleNamespace
import pickle
import requests


def parseJson():
    with open("data.json") as file:
      data = json.load(file)

    print(data["data"])
    
    parsed_info = data["data"]
    return parsed_info

def leukocytesUp():
  # Magically tell to the assistant
  # to add more leukocytes
  print ("Success")

  
def leukocytesDown():
  # Magically tell to the assistant
  # to get some leukocytes
  print ("Success")

def controlHumanStats():
  data = parseJson()

  # Magically, with machine learning
  # Analyze data for every person
  # And Save the regular stats 
  recDataForSpecPerson = 2


  if data.leukocytes < 3.5:
    print("Leukocytes are too low")
    leukocytesUp()
  elif data.leukocytes > 10.5:
    print("Leukocytes are too high")
    leukocytesDown()

  # Also checks for other human stats

    
