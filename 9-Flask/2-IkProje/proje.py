from flask import Flask , flash, render_template, redirect, url_for, request,session
import sqlite3
from passlib.hash import   sha256_crypt
from ConvertDict import dict_factory
from forms import RegisterForm,LoginForm ,CityForm,PersonelForm
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
        con = sqlite3.connect("IK.db")
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
        con = sqlite3.connect("IK.db")
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
                return redirect(url_for("index"))
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
@app.route('/cities/list')
def list():
    con = sqlite3.connect("IK.db")
    con.row_factory = dict_factory
    cursor = con.cursor()
    sorgu = 'select * from city'
    cities  = cursor.execute(sorgu).fetchall()
    return render_template("cities/list.html" ,cities = cities)
@app.route('/cities/detail/<string:id>')
def detail(id):
    con = sqlite3.connect("IK.db")
    con.row_factory = dict_factory
    cursor = con.cursor()
    sorgu = 'select * from city where id = ?'
    city = cursor.execute(sorgu,(id,)).fetchone()
    return render_template("cities/detail.html" ,city = city)
@app.route('/cities/edit/<string:id>',methods = ["GET","POST"])
def edit(id):
    form = CityForm(request.form)
    con = sqlite3.connect("IK.db")
    con.row_factory = dict_factory
    cursor = con.cursor()
    if request.method == "GET":
        sorgu = 'select * from city where id = ?'
        city = cursor.execute(sorgu,(id,)).fetchone()
        form.name.data = city["name"]
        form.description.data = city["description"]
        return render_template("cities/edit.html" ,form = form)
    else:
        name  = form.name.data
        description = form.description.data
        sorgu = 'update city set name = ? ,description = ? where id = ?'
        cursor.execute(sorgu, (name,description,id))
        con.commit()
        flash("Güncelleme Başarılı " ,"success")
        return redirect(url_for("list"))
@app.route('/cities/delete/<string:id>',methods = ["GET","POST"])
def delete(id): 
    form = CityForm(request.form)   
    con = sqlite3.connect("IK.db")
    con.row_factory = dict_factory
    cursor = con.cursor()
    if request.method == "GET":
        sorgu = 'select * from city where id = ?'
        city = cursor.execute(sorgu,(id,)).fetchone()
        form.name.data = city["name"]
        form.description.data = city["description"]
        return render_template("cities/delete.html" ,form = form)
    else:
        sorgu = 'delete from city  where id = ?'
        cursor.execute(sorgu, (id,))
        con.commit()
        flash("Silme Başarılı " ,"success")
        return redirect(url_for("list"))
@app.route('/cities/add',methods = ["GET","POST"])
def add():
    form = CityForm(request.form)
    con = sqlite3.connect("IK.db")
    con.row_factory = dict_factory
    cursor = con.cursor()
    if request.method == "POST":
        name  = form.name.data
        description = form.description.data
        sorgu = 'insert into  city   (name, description ) values (? , ? )'
        cursor.execute(sorgu, (name,description))
        con.commit()
        flash("Yeni kayıt Eklendi" ,"success")
        return redirect(url_for("list"))
    return render_template("cities/add.html" ,form = form)
@app.route('/personel/list')
def perlist():
    con = sqlite3.connect("IK.db")
    con.row_factory = dict_factory
    cursor = con.cursor()
    sorgu = 'select * from personel'
    personel   = cursor.execute(sorgu).fetchall()
    return render_template("personel/list.html" ,personel = personel)  

@app.route('/personel/add',methods = ["GET","POST"])
def peradd():
    form = PersonelForm(request.form)
    con = sqlite3.connect("IK.db")
    con.row_factory = dict_factory
    cursor = con.cursor()
    sorgu = 'select id, name  from city'
    cities =  cursor.execute(sorgu).fetchall()
    
    if request.method == "POST" and form.validate():
        name  = form.name.data
        surname = form.surname.data
        salary = float(form.salary.data)
        birthdate = request.form.get("birthdate")
        cityid = request.form.get("cityid")

        sorgu = 'insert into  personel   (name, surname , salary , birthdate ,cityid) values (? ,? ,?,? ,?)'
        cursor.execute(sorgu, (name,surname,salary,birthdate,cityid))
        con.commit()
        flash("Yeni kayıt Eklendi" ,"success")
        return redirect(url_for("perlist"))
    return render_template("personel/add.html" ,form = form ,cities = cities ) 
@app.route('/personel/edit/<string:id>',methods = ["GET","POST"])
def peredit(id):
    form = PersonelForm(request.form)
    con = sqlite3.connect("IK.db")
    con.row_factory = dict_factory
    cursor = con.cursor()
    sorgu = 'select id, name  from city'
    cities =  cursor.execute(sorgu).fetchall()
    if request.method == "GET":
        sorgu = 'select * from personel where id = ?'
        personel  = cursor.execute(sorgu,(id,)).fetchone()
        form.name.data = personel["name"]
        form.surname.data = personel["surname"]
        form.salary.data = personel["salary"]
        birthdate = personel["birthdate"]
        cityid = personel["cityid"]
        return render_template("personel/edit.html" ,form = form , cities = cities ,
        birthdate = birthdate ,cityid = cityid)
    elif request.method == "POST" and form.validate():
        name  = form.name.data
        surname  = form.surname.data
        salary  = float(form.salary.data) 
        cityid = int(request.form.get("cityid"))
        birthdate = request.form.get("birthdate") 
        sorgu = 'update personel  set name = ? ,surname = ?, salary = ? , birthdate = ?,cityid =? where id = ? '
        cursor.execute(sorgu, (name,surname,salary,birthdate,cityid,id))
        con.commit()
        flash("Güncelleme Başarılı " ,"success")
        return redirect(url_for("perlist"))
@app.route('/personel/delete/<string:id>')
def perdelete(id):
    con = sqlite3.connect("IK.db")
    cursor = con.cursor()
    sorgu = 'delete from personel where id = ?'
    cursor.execute(sorgu, (id,))
    con.commit()
    flash("Güncelleme Başarılı " ,"success")
    return redirect(url_for("perlist"))
 
if __name__ =="__main__":
    #db.create_all()
    app.secret_key ="secret"
    app.run(debug = True)  



 


