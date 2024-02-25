from flask import Flask
app = Flask(__name__)
@app.route("/game")
def game():
    return{"game":["Hello there!","2nd line"]}

if __name__=="__main__":
    app.run(debug=True)