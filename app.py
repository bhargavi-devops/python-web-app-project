from flask import Flask

app = Flask(_name_)

@app.route("/")
def hello():
    return "Hello, Better DevOps Team! This is my assignment project."

if _name_ == "_main_":
    app.run(host="0.0.0.0", port=5000)
