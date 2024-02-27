from flask import Flask,render_template,request
app=Flask(__name__)


@app.route("/log")
def home():
    
    return render_template("new.html")

@app.route("/reg")
def new():
    return render_template("register.html")

@app.route("/view",methods=["POST","GET"])
def viw():

    if request.method=="POST":
        a=[1,2,3,4,5,6]
        name=request.form["username"]
        passw=request.form["password"]
        return render_template("view.html",name=name,passw=passw,a=a)
    return render_template("new.html")





if __name__=="__main__":
    app.run(debug=True)