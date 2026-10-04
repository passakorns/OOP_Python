from connectdb import *
from myFormField import *
from flask import Flask, render_template, session, redirect, url_for, request
from flask_wtf.csrf import CSRFProtect



myapp = Flask(__name__)

myapp.secret_key = "my_secret_key"
csrf = CSRFProtect(myapp)

DB_Name = 'myshop.db'

@myapp.route('/')
def index():

    return render_template("index.html")



@myapp.route('/members')
def members():
    if not login_required():
            return redirect(url_for("login"))
    
    with get_db(DB_Name) as db:
        sql = "SELECT * FROM members ORDER BY id DESC"
        data = db.execute(sql).fetchall()

    return render_template("members.html", members = data)

@myapp.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        with get_db(DB_Name) as db:
            sql ='INSERT INTO members (name, password, isAgree, gender, province, address) VALUES(?,?,?,?,?,?)'

            name = form.username.data.strip()
            password = form.password.data
            isAgree = form.isAgree.data
            gender = form.gender.data
            province = form.province.data
            address = form.address.data
            db.execute(sql, (name, password, isAgree, gender, province, address))

        flash("ลงทะเบียนสำเร็จ")
        return redirect(url_for("index"))

    return render_template("register.html", form = form)

@myapp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for("login"))

@myapp.route('/members/member_edit/<int:member_id>', methods=["GET", "POST"])
def member_edit(member_id):
    
    #ตรวจสอบการเข้าสู่ระบบ
    if not login_required():
        return redirect(url_for("login"))
    
    
    sql = "SELECT * FROM members WHERE id = ?"
    with get_db(DB_Name) as db:
        member = db.execute(sql, (member_id,)).fetchone()

    if member is None:
        flash("ไม่พบข้อมูลสมาชิก")
        return redirect(url_for("members"))

    form = MemberEditForm(obj=member)
    #แสดงข้อมูลเดิมเมื่อเปิดหน้าแก้ไข
    if request.method == "GET":
        form.username.data = member["name"]
        form.gender.data = member["gender"]
        form.isAgree.data = member["isAgree"]
        form.address.data = member["address"]
        form.province.data = member["province"]

    if form.validate_on_submit():
        sql = "UPDATE members SET name=?, isAgree=?, gender=?, province=?, address=? WHERE id=?"
        name = form.username.data.strip()
        isAgree = form.isAgree.data
        gender = form.gender.data
        province = form.province.data
        address = form.address.data
        with get_db(DB_Name) as db:
            db.execute(sql, (name, isAgree, gender, province, address, member_id))
        
        flash("แก้ไขสมาชิกสำเร็จ")
        return redirect(url_for("members"))
    
    return render_template("member_edit.html", form=form)

@myapp.route('/members/member_delete/<int:member_id>', methods=["POST"])
def member_delete(member_id):
    sql = "DELETE FROM members WHERE id = ?"
        
    if not login_required():
        return redirect(url_for("login"))
        
    with get_db(DB_Name) as db:
            db.execute(sql, (member_id, ))

    flash("ลบสมาชิกแล้ว")
    session.clear()
    return redirect(url_for("index"))


if __name__ == "__main__":
    init_db(DB_Name)
    myapp.run(debug=True)
