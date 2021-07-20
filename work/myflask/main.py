import uuid
from flask import Flask,render_template,request,session,redirect,send_file
from pymongo import MongoClient
import os
import time


mc=MongoClient("127.0.0.1",27017)
db=mc['xs']
app = Flask(__name__)
app.config['SECRET_KEY']='78912312#KLH$@KHkhdad'

@app.before_request
def before():
    if  not request.path in ["/static/02.jpg","/static/jquery.min.js","/static/dl.css","/dl","/zc","/"]:
        if session:
            use=session['use']
            if use:
                return None
            else:
                return "请先登录"
        else:
            return "请先登录"
    else:
        None
@app.route("/")
def index():
    return render_template('index.html')

@app.route('/dl',methods=['POST','GET'])
def dl():
    if request.method == 'GET':
        return render_template("dl.html")
    if request.method == 'POST':
        use=request.form.to_dict()
        print(db['user'].find_one({'name':use.get("user")},{'pwassord':use.get("password")}))
        if db['user'].find_one({'user':use.get("user")},{'pwassord':use.get("password")}):
        # if use.get('user') == '123' and use.get('password') == '123':
            session['use']=use.get('user')
            return redirect("/home")
        else:
            return render_template("dl.html",erro="用户密码错误")

def xs_use_crea(user,password):
    gs={"user":user,"password":password}
    a=db['user'].insert_one(gs)

@app.route("/zc",methods=['POST','GET'])
def zc():
    if request.method == 'GET':
        return render_template("zc.html")
    if request.method == 'POST':
        a=request.form.to_dict()
        print(a)
        xs_use_crea(a["user"],a['password'])
        return redirect("/")

@app.route("/xs")
def xs():
    return send_file("static/1.txt")
@app.route("/lswj",methods=['POST','GET'])
def lswj():
    if request.method== "GET":
        wj=db["wj"].find()
        jl=[]
        for i in wj:
            jl.append(i)
        print(jl)
        return render_template("lswj.html",jl=jl)
    else: 
        bz=request.form["bz"]
        uuid_str=str(uuid.uuid4())
        data=request.files["wj"]
        f=data.filename
        os.mkdir("work/myflask/static/"+uuid_str)
        data.save("work/myflask/static/"+uuid_str+"/"+f)
        lswj_crea(f,uuid_str,bz)
        return redirect("/home")
def lswj_crea(f,uuid,bz):
    t=time.time()
    if db["wj"].find_one({"name":f}):
        db["wj"].update_one({"name":f},{"$push":{"jl":{"bz":bz,"uuid":uuid,"time":t}}})
    else:
        db["wj"].insert_one({"name":f,"jl":[{"bz":bz,"uuid":uuid,"time":t},]})
@app.route('/home')
def home():
    use=session['use']
    return render_template("home.html",use=use)
@app.route("/xs/<a>/<b>")
def xz(a,b):
    return send_file("static/"+a+"/"+b)
if __name__ == "__main__":
    app.run()
