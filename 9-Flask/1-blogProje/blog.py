from flask import Flask , flash, render_template, redirect, url_for, request,session
import sqlite3

from passlib.hash import   sha256_crypt
from ConvertDict import dict_factory
from forms import RegisterForm,LoginForm,ArticleForm
from datetime import date
from functools import wraps

app = Flask(__name__)
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "logged_in" in session:
            return f(*args, **kwargs)
        else:
            flash("Bu sayfaya gitmek için giriş yapmalısınız", "danger")
            return redirect(url_for("login"))
    return decorated_function 
@app.route('/')
def index():
    return render_template("index.html")
@app.route('/register' , methods = ["GET","POST"])
def register():
    form = RegisterForm(request.form)
    if request.method == "POST" and form.validate():
        username = form.username.data
        email = form.username.data
        password = sha256_crypt.encrypt(form.password.data) 
        con = sqlite3.connect("blog.db")
        cursor = con.cursor() 
        cursor.execute('insert into user (username,email,password) values(? , ? ,?)', (username,email,password))
        con.commit()
        cursor.close()
        flash("Kayıt İşlemi Başarılı.." ,"success")
        return redirect(url_for("index"))
    else:
        return render_template("register.html" , form = form) 
@app.route('/login' , methods = ["GET" ,"POST"] )
def login():
    form = LoginForm(request.form)
    if request.method == "POST":
        username = form.username.data
        password_entered = form.password.data
        con = sqlite3.connect("blog.db")
        cursor = con.cursor()
        #con.row_factory = sqlite3.Row
         
        sorgu = 'select * from user where username = ?'
        result = cursor.execute(sorgu  ,(username,)).fetchone()
        if result:
            password_real = result[3]
            print(password_real)
            if sha256_crypt.verify(password_entered , password_real):
                session["logged_in"] = True
                session["username"] = username
                flash("Login Başarılı ...", "success") 
                return redirect(url_for("dashboard"))
            else:
                flash("yanlış şifre ", "danger") 
                return redirect(url_for("login"))
        else:
            flash("Böyle Bir Kullanıcı Yok....", "danger") 
            return redirect(url_for("login"))
    else:
        return render_template("login.html" , form = form )
@app.route('/logout' , methods = ["GET" ,"POST"] )
def logout():
    session.clear()
    return redirect(url_for("index"))

@app.route('/article/dashboard')
@login_required
def dashboard():
    #con = sqlite3.connect("blog.db")
    # cursor = con.cursor()
    # sorgu = 'select * from articles where author  = ?'
    # result = cursor.execute(sorgu  ,(username,)).fetchall()
    con = sqlite3.connect("blog.db")
    con.row_factory = dict_factory
    cursor = con.cursor()
    sorgu = 'select * from articles where author  = ?'
    result  = cursor.execute(sorgu, (session["username"],)).fetchall()
    return render_template("article/dashboard.html", articles = result)
@app.route("/article/detail/<string:id>")
def detail(id):
    con = sqlite3.connect("blog.db")
    con.row_factory = dict_factory
    cursor = con.cursor()
    sorgu = 'select * from articles where id = ?'
    article = cursor.execute(sorgu , (id,)).fetchone()
    return render_template("article/detail.html", article = article)
@app.route("/article/addarticle/" ,methods =["GET", "POST"])
@login_required
def addarticle ():
    form = ArticleForm(request.form)
    if request.method =="POST":
        title  = form.title.data
        content = form.content.data
        con = sqlite3.connect("blog.db")
        cursor = con.cursor()
        sorgu = ' insert into articles (author , title, content, created_date)  values(?,?,?,?) '
        cursor.execute(sorgu, (session["username"],title,content,date.today()))
        con.commit()
        flash("Kayıt Başarılı bir şekilde Eklendi ...","success")
        return redirect(url_for("dashboard"))
    else:
        return render_template("article/addarticle.html", form = form)
@app.route("/article/delete/<string:id>")
@login_required
def delete(id):
    con = sqlite3.connect("blog.db")
    cursor = con.cursor()
    sorgu = 'delete  from articles where id = ?'
    cursor.execute(sorgu , (id,)).fetchone()
    con.commit()
    flash("Kayıt Başarılı bir şekilde silindi ...","success")
    return redirect(url_for("dashboard"))
@app.route("/article/edit/<string:id>" ,methods =["GET", "POST"] )
@login_required
def edit(id):
    if request.method == "GET":
        form = ArticleForm()
        con = sqlite3.connect("blog.db")
        con.row_factory = dict_factory
        cursor = con.cursor()
        sorgu = 'select *  from articles where id = ?'
        article = cursor.execute(sorgu , (id,)).fetchone()
        form.content.data = article["content"]
        form.title.data = article["title"]
        return render_template("article/edit.html", form = form)
    else:
        form = ArticleForm(request.form)
        content = form.content.data
        title = form.title.data
        print(title)
        con = sqlite3.connect("blog.db")
        cursor = con.cursor()
        sorgu = 'update articles set title = ? , content = ? where id = ?'
        cursor.execute(sorgu,(title,content,id))
        con.commit()
        flash("Güncelleme Başarılı " ,"success")
        return redirect(url_for("dashboard"))
@app.route("/article/articles" ,methods =["GET", "POST"])
def articles():
    con = sqlite3.connect("blog.db")
    con.row_factory = dict_factory
    cursor = con.cursor()
    if request.method == "GET":
        sorgu = 'select * from articles'
        articles = cursor.execute(sorgu).fetchall()
        return render_template("article/articles.html" , articles = articles)
    else:
        keyword = request.form.get("keyword")
        sorgu = "select * from articles where title like  '%" + keyword + "%' "
        articles = cursor.execute(sorgu)
        return render_template("article/articles.html" , articles = articles)
if __name__ =="__main__":
    #db.create_all()
    app.secret_key ="secret"
    app.run(debug = True)  



 


