from flask import Flask

from threading import Thread

app2 = Flask('')

@app2.route('/')

def home():
 return "@RexDev , congratulazioni!"
  
  
def run():
  app2.run(host="0.0.0.0",port=8080)


def keep_alive():
   t = Thread(target=run)
   t.start()
