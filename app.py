from flask import Flask , request , make_response

app = Flask(__name__)


@app.route("/")
def index():
    return "this is the index page"

@app.get("/images/<int:id>")
def getImages(id):
       print(dir(request))
       return f"the id {id} has noddd images attached to it  and the request consists of {request}"

@app.post("/login")
def login():
      print(request.form)
      entities =len(request.form)
      return f"you have posted {entities} body elements"

@app.get("/cookie")
def cookie():
      resp = make_response("the cookie has been set mate")
      resp.set_cookie("token" , "sdfsdf8sdf8sg79879798sdf")
      return resp

@app.get("/cookieplay")
def cookiePlay():
      return request.cookies