from twilio.rest import Client
from flask import Flask, request

app = Flask(__name__)

client = Client("ACba8845135b32a9bbfa6dff910dde7a7a", "c6f1d0f3e944eb394a435b9464a4512b")

@app.route('/', methods=["GET"])
def GETfunc():

    print("Fatema Malu Bhai Wala")
    
    var = client.messages.create(to="whatsapp:+918217245874", from_="whatsapp:+14155238886", body="Hello")

    print(var)

    return "Hello world"

@app.route('/', methods=["POST"])
def POSTfunc():
    print("something")
    receivedMsg = request.values.get("Body")

    print(receivedMsg)
    
    if(receivedMsg=="Hi"):
        print(client.messages.create(to="whatsapp:+918217245874", from_="whatsapp:+14155238886", body="Hello! How are you doing?"))

    return "<Response></Response>"



if __name__ == "__main__":
    app.run(debug=True)
