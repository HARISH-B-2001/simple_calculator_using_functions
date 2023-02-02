from flask import Flask, render_template,url_for,request,redirect
from db_functions import add_content,get_content_name,get_content_qn
import create_db


def zero(f = None): return 0 if not f else f(0)
def one(f = None): return 1 if not f else f(1)
def two(f = None): return 2 if not f else f(2)
def three(f = None): return 3 if not f else f(3)
def four(f = None): return 4 if not f else f(4)
def five(f = None): return 5 if not f else f(5)
def six(f = None): return 6 if not f else f(6)
def seven(f = None): return 7 if not f else f(7)
def eight(f = None): return 8 if not f else f(8)
def nine(f = None): return 9 if not f else f(9)

def plus(y): return lambda x: x+y
def minus(y): return lambda x: x-y
def times(y): return lambda  x: x*y
def divided_by(y): return lambda  x: x//y

database={'nachi':'123','james':'aac','karthik':'asdsf'}

app = Flask(__name__,
    template_folder='templates'
    )

@app.route('/logout', methods=['POST'])
def logout():
    return render_template('index.html')

@app.route('/student',methods=['POST','GET'])
def student():
    name = get_content_name()
    qn = get_content_qn()
    count=len(name)
    return render_template('student.html', name=name,qn=qn, count=count)


@app.route('/')
def helloworld():
    return render_template('index.html')



@app.route('/form_login',methods=['POST','GET'])
def login():
    name1=request.form['username']
    pwd=request.form['password']
    if name1 not in database:
        return render_template('index.html',info='Invalid User')
    else:
        if database[name1]!=pwd:
            return render_template('index.html',info='Invalid Password')
        else:
            return redirect(url_for('student'))
            
@app.route('/page_signup',methods=['POST'])
def signup_page():
    return render_template('signup.html')

@app.route('/form_signup',methods=['POST','GET'])
def signup():
    sname1=request.form['susername']
    spwd=request.form['spassword']
    database[sname1] = spwd
    return redirect(url_for('helloworld'))



@app.route('/add', methods=["POST"])
def add():
    content_name = request.form["post_name"]
    a=eval(content_name)
    add_content(a,content_name)
    return redirect(url_for('student'))

if __name__ == '__main__':
    create_db.execute_query(create_db.sql_query)
    app.run(debug=True)
    
