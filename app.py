from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello,World"


@app.route("/hiraizumi")
def hello_hiraizumi():
    return "そうだ,平泉"


@app.route("/user/<name>")
def heyName(name):
    return name


@app.route("/user/age/<age>")
def heyAge(age):
    return age


@app.route("/user/<name>/<age>")
def heyNameAge(name, age):
    return name + age


@app.route("/html")
def html():
    return render_template("index.html")


@app.route("/html/name/<name>")
def htmlName(name):
    return render_template("name.html", name=name)


@app.route("/html/age/<age>")
def htmlAge(age):
    return render_template("age.html", age=age)


@app.route("/query")
def query():
    search_text = request.args.get("search_text")
    if search_text is not None:
        return search_text
    else:
        return ""


if __name__ == "__main__":
    app.run(debug=True)
