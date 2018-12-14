from sqlalchemy import or_
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
import pymysql


pymysql.install_as_MySQLdb()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@localhost:3306/flask'
#指定当驶入执行完毕后,自动提交数据库操作
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True
#指定每次执行操作时打印原始的SQL语句
# app.config['SQLALCHEMY_ECHO']=True
#创建数据库的实例
db = SQLAlchemy(app)

class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False,unique=True)
    age = db.Column(db.Integer)
    email = db.Column(db.String(120),unique=True)

    def __init__(self,username,age,email):
        self.username = username
        self.age = age
        self.email = email

    def __repr__(self):
        return "<Users:%r>" %self.username

class Student(db.Model):
    __tablename__ = 'student'
    id = db.Column(db.Integer, primary_key=True)
    sname = db.Column(db.String(30), nullable=False)
    tage = db.Column(db.Integer)

    def __init__(self,sname,tage):
        self.sname = sname
        self.tage = tage

    def __repr__(self):
        return "<Student:%r>" %self.sname

class Teacher(db.Model):
    __tablename__ = 'teacher'
    id = db.Column(db.Integer, primary_key=True)
    tname = db.Column(db.String(30), nullable=False)
    tage = db.Column(db.Integer)
    tbirth = db.Column(db.Date)

    def __init__(self,tname,tage,tbirth):
        self.tname = tname
        self.tage = tage
        self.tbirth = tbirth

    def __repr__(self):
        return "<Teacher:%r>" % self.tname

class Course(db.Model):
    __tablename__ = 'course'
    id = db.Column(db.Integer, primary_key=True)
    cname = db.Column(db.String(30))

    def __init__(self,cname):
        self.cname = cname

    def __repr__(self):
        return "<Course:%r>" % self.cname

# 将创建好的实体类映射会数据库
db.create_all()

@app.route('/01-add')
def add_views():
    #创建Users对象,并插入到数据库中
    users = Users('王老师',35,'mrwang@163.com')
    db.session.add(users)
    db.session.commit()
    return "Add OK"

@app.route('/02-register',methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template('02-register.html')
    else:
        uname = request.form.get('uname')
        uage = request.form.get('uage')
        uemail = request.form.get('uemail')
        user = Users(uname,uage,uemail)
        db.session.add(user)
        # db.session.commit()
        return "Register Succcess"

@app.route('/03-query')
def query_views():
    # users = db.session.query(Users).all
    # for i in users:
    #     print(i)
    #测试first函数
    # user = db.session.query(Users).first()
    # print(user)
    #查询返回部分列
    # query = db.session.query(Users.username,Users.age)
    # print(query)

    #测试filter()函数
    #filter() -查询Users中年龄大于30的人的信息
    # users = db.session.query(Users).filter(Users.age>30).all()
    # for u in users:
    #     print("姓名:%s,年龄:%d,邮箱:%s"%(u.username,u.age,u.email))

    # users = db.session.query(Users).filter(Users.age > 25, Users.id > 1).all()
    # for u in users:
    #     print("姓名:%s,年龄:%d,邮箱:%s"%(u.username,u.age,u.email))
    #filter() -- 查询Users中id为1或者年龄大于30的人
    # users = db.session.query(Users).filter(or_(Users.age > 30, Users.id == 1)).all()
    # for u in users:
    #     print("姓名:%s,年龄:%d,邮箱:%s"%(u.username,u.age,u.email))

    # users = db.session.query(Users).filter(Users.email.like('%w%')).all()
    # for u in users:
    #     print("姓名:%s,年龄:%d,邮箱:%s"%(u.username,u.age,u.email))

    # users = db.session.query(Users).filter(Users.id.in_([1,2])).all()
    # for u in users:
    #     print("ID:%d,姓名:%s,年龄:%d,邮箱:%s"%(u.id,u.username,u.age,u.email))

    # users = db.session.query(Users).filter(Users.age.between(35,40)).all()
    # for u in users:
    #     print("姓名:%s,年龄:%d,邮箱:%s"%(u.username,u.age,u.email))

    #########
    #filter_by()
    #########
    # user = db.session.query(Users).filter_by(id=1).first()
    # print(user)
    #查询表中的前两条记录
    # users = db.session.query(Users).limit(2).all()
    # for u in users:
    #     print("ID:%d,姓名:%s,年龄:%d,邮箱:%s"%(u.id,u.username,u.age,u.email))

    # users = db.session.query(Users).limit(1).offset(1).all()
    # for u in users:
    #     print("ID:%d,姓名:%s,年龄:%d,邮箱:%s"%(u.id,u.username,u.age,u.email))
    #年龄倒序排列,id升序排列
    # users = db.session.query(Users).order_by("age desc,id asc")
    # for u in users:
    #     print("ID:%d,姓名:%s,年龄:%d,邮箱:%s"%(u.id,u.username,u.age,u.email))

    # users = db.session.query(Users.age).group_by('age').all()
    # print(users)

    ########
    #聚合函数
    # result = db.session.query(func.avg(Users.age)).all()
    # print(result)

    # result = db.session.query(func.avg(Users.age)).group_by('age').all()
    # print(result)
    # for u in users:
    #     print("ID:%d,姓名:%s,年龄:%d,邮箱:%s"%(u.id,u.username,u.age,u.email))

    users = Users.query.filter_by(id=3).all()
    for u in users:
        print("ID:%d,姓名:%s,年龄:%d,邮箱:%s"%(u.id,u.username,u.age,u.email))

    return "<script>alert('Query OK');</script>"

@app.route('/04-queryall')
def queryall():
    users = Users.query.all()
    return render_template('04-queryall.html', users=users)

@app.route("/05-update")
def update_views():
    #接收前端传递过来的参数id
    id = request.args.get('id')
    #根据id查询出对应的对象
    user = Users.query.filter_by(id=id).first()
    #将查询出来的随想发送到05-update.html中进行显示
    return render_template('05-update.html',user=user)

if __name__ == "__main__":
    app.run(debug=True)

