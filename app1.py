from flask import Flask, request
import sqlite3
import math
app = Flask(__name__)

def gcd(a, h):
    temp = 0
    while(1):
        temp = a % h
        if (temp == 0):
            return h
        a = h
        h = temp

def encrypt(msg):
    p = 3
    q = 7
    n = p*q+5
    e = 2
    phi = (p-1)*(q-1)

    while (e < phi):
  
    
     if(gcd(e, phi) == 1):
        break
     else:
        e = e+1
    k = 2
    d = (1 + (k*phi))/e

   # print("Message data = ", msg)

    c = pow(msg, e)
    c = math.fmod(c, n)
   # print("Encrypted data = ", c)

    m = pow(c, d)
    m = math.fmod(m, n)
   # print("Original Message Sent = ", m)
    
    return int(c)

def decrypt(c):
    p = 3
    q = 7
    n = p*q+5
    e = 2
    phi = (p-1)*(q-1)

    while (e < phi):
  
    
     if(gcd(e, phi) == 1):
        break
     else:
        e = e+1
    k = 2
    d = (1 + (k*phi))/e


    m = pow(c, d)
    m = math.fmod(m, n)
   # print("Original Message Sent = ", m)
    
    return int(m)

@app.route("/sendData", methods=['GET'])
def sendData():
    args = request.args
    p=args.get("data")
    r=""
    print (p)
    for element in p:
        q=chr(encrypt(ord(element)-97)+97)
        print(element)
        print (q)
        print("..")
        r=r+q
    return "The data is saved as </p>" + r

@app.route("/")
def welcomePage():
    return "<h1>Welcome to Cloud Service </h1><p>/sendData?data= to save a data and /getData?data= to fetch a data</p>"

@app.route("/getData", methods=['GET'])
def getData():
    args = request.args
    p=args.get("data")
    r = ""
    print (p)
    for element in p:
        q=chr(decrypt(ord(element)-97)+97)
        print(element)
        print (q)
        print("..")
        r=r+q
    return "The data after decrypting is fetched as </p>"+r

# main driver function
if __name__ == "__main__":

    app.run()
