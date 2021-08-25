from flask import Flask, render_template,redirect,request,url_for

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)  # creating the Flask class object
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///test5.db'
db=SQLAlchemy(app)


class Todo(db.Model):
    id= db.Column(db.Integer,primary_key=True)
    content=db.Column(db.String(200),nullable=False)
    uid=db.Column(db.String(200),nullable=False)
    email=db.Column(db.String(200),nullable=False)
    mobile=db.Column(db.Integer,nullable=False)
    branch=db.Column(db.String(30),nullable=False)
    #subject=db.Column(db.String(200),nullable=False)
    completed=db.Column(db.Integer,default=0)
    date_created=db.Column(db.DateTime,default=datetime.utcnow)
    
def __repr__(self):
    return f'<Task  {self.content} ,{self.uid},{self.email},{self.mobile},{self.branch} >'    
    
  

@app.route('/' , methods=['POST','GET'])  
def index():
    if request.method == 'POST':
        task_content = request.form['content']
        task_uid = request.form['uid']
        task_email = request.form['email']
        task_mobile = request.form['mobile']
        task_branch = request.form['branch']
        new_task =Todo(content=task_content, uid=task_uid, email=task_email, mobile=task_mobile,branch=task_branch)
       # task_subject = request.form['subject']
       # new_task1 =Todo(content=task_subject)
        
        try:
            db.session.add(new_task)
          #  db.session.add(new_task1)
            db.session.commit()
            return redirect('/')
        except:
            return "Data not inserted into database"
    else:
            
        return render_template("index.html")
        
@app.route('/view', methods=['GET', 'POST'])
def view():
    tasks =Todo.query.all()        
    return render_template("view.html",tasks=tasks)




@app.route('/delete/<int:id>')
def delete(id):
    task = Todo.query.get_or_404(id)
    try:
        db.session.delete(task)
        db.session.commit()
        return redirect('/view')
    except:
        return "The data is not deleted Successfully"

if __name__ == '__main__':
    app.run(debug=True)