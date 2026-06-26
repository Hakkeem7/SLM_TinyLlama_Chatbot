from flask import Flask,render_template,request
import requests
app=Flask(__name__)


@app.route("/",methods=["GET","POST"])
def home():
    output=""
    if request.method=="POST":
        name=request.form.get("user")
        url="http://localhost:11434/api/generate"
        response=requests.post(url,json={
            "model":"tinyllama",
            "prompt":name,
            "stream":False,
        })
        output=response.json().get(response)
    return render_template("ui.html",output=output)

if __name__=="__main__":
    app.run(debug=True)