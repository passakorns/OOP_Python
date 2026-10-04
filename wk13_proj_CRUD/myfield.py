from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length, Email, NumberRange
from wtforms import (StringField, PasswordField, SubmitField, 
                     BooleanField, RadioField,SelectField, 
                     TextAreaField, IntegerField)


class RegisterForm(FlaskForm):
    username = StringField("ชื่อ-สกุล", validators=[DataRequired(message="กรอกชื่อของคุณ")])
    password = PasswordField("รหัสผ่าน", validators=[DataRequired("กรอกรหัสผ่าน")])

    isAgree = BooleanField("ยอมรับเงื่อนไข")
    gender = RadioField("เพศ", 
                        choices=[("M", "ชาย"),
                                 ("F", "หญิง"),
                                 ("O","อื่น ๆ")
                                 ]
                        )
    #Dropdown
    province = SelectField("จังหวัด",
                            choices=[("กรุงเทพมหานคร","กรุงเทพมหานคร"),
                                        ("เชียงใหม่", "เชียงใหม่"),
                                        ("สงขลา","สงขลา"),
                                        ("ขอนแก่น","ขอนแก่น")
                                     ]
                           )
    address = TextAreaField("ที่อยู่")
    submit = SubmitField("ลงทะเบียน")


# ---------- Forms ----------

class MyForm(FlaskForm):
    name = StringField(
        "ชื่อสมาชิก",
        validators=[DataRequired(), Length(max=100)]
    )
    email = StringField(
        "อีเมล",
        validators=[DataRequired(), Email(), Length(max=120)]
    )
    password = PasswordField(
        "รหัสผ่าน",
        validators=[DataRequired(), Length(min=8)]
    )
    submit = SubmitField("สมัครสมาชิก")


class LoginForm(FlaskForm):
    username = StringField(
        "ชื่อผู้ใช้",
        validators=[DataRequired()]
    )
    password = PasswordField(
        "รหัสผ่าน",
        validators=[DataRequired()]
    )
    submit = SubmitField("เข้าสู่ระบบ")


class BookForm(FlaskForm):
    title = StringField(
        "ชื่อหนังสือ",
        validators=[DataRequired(), Length(max=200)]
    )
    author = StringField(
        "ผู้แต่ง",
        validators=[DataRequired(), Length(max=100)]
    )
    price = IntegerField(
        "ราคา (บาท)",
        validators=[DataRequired(), NumberRange(min=0)]
    )
    stock = IntegerField(
        "จำนวนคงเหลือ",
        validators=[DataRequired(), NumberRange(min=0)]
    )
    submit = SubmitField("บันทึก")


class MemberEditForm(FlaskForm):
    username = StringField("ชื่อ-สกุล", validators=[DataRequired(message="กรอกชื่อของคุณ")])

    isAgree = BooleanField("ยอมรับเงื่อนไข")
    gender = RadioField("เพศ", 
                            choices=[("M", "ชาย"),
                                     ("F", "หญิง"),
                                     ("O","อื่น ๆ")
                                     ]
                            )
    #Dropdown
    province = SelectField("จังหวัด",
                                choices=[("กรุงเทพมหานคร","กรุงเทพมหานคร"),
                                            ("เชียงใหม่", "เชียงใหม่"),
                                            ("สงขลา","สงขลา"),
                                            ("ขอนแก่น","ขอนแก่น")
                                         ]
                               )
    address = TextAreaField("ที่อยู่", validators=[DataRequired()])
    submit = SubmitField("บันทึกการแก้ไข")
