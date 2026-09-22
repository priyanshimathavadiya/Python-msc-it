from flask import Flask,render_template,request


app = Flask(__name__)

@app.route("/")
def home():
    print("Welcome to TO-DO Application")

    task_name = request.form.get("task")
    due_date = request.form.get("date")
    status = request.form.get("status")

    print(task_name)
    print(due_date)
    print(status)

    return render_template("home.html",task=task_name,date=due_date,status=status)

if __name__=='__main__':
    app.run() 

