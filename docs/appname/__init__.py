#Jude Rizzo
#Sofdev1 pd9
#K08 -- Lemme Flask You Sump’n
#2019--9--19
import os
os.path.dirname(__file__)
DIR = os.path.dirname(__file__) or ‘.’
DIR += ‘/’



from flask import Flask
app = Flask(__name__)
#print("Printing this in the flask console")

#you set a route with the decorator, which is marked by an @
#each one seems to have one fcuntion under it
@app.route("/")
def hello_world():
  print(__name__)
  return  "1"

 #also every string in the decorator begins with a /


if __name__ == "__main__":
  app.debug = True
  app.run()
