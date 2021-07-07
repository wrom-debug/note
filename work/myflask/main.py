from flask import Flask,render_template,request,session,redirect,send_file
from pymongo import MongoClient



mc=MongoClient("127.0.0.1",27017)
db=mc['xs']
app = Flask(__name__)
app.config['SECRET_KEY']='78912312#KLH$@KHkhdad'

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/dl',methods=['POST','GET'])
def u():
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
        return "注册成功"

@app.route('/home')
def home():
    use=session['use']
    return send_file("static/1.txt")


if __name__ == "__main__":
    app.run()
