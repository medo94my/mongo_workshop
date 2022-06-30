from flask import Flask, jsonify, redirect, render_template, request, url_for
from pymongo import MongoClient
from datetime import datetime
from bson.objectid import ObjectId
app = Flask(__name__)

myclient = MongoClient(
    'mongodb+srv://workshp:workshop123@cluster0.shpuc.mongodb.net/?retryWrites=true&w=majority')
mydb = myclient['test_db']
mycol = mydb['customers']


@app.route("/", methods = ["POST", "GET"])
def home():
    if request.method =="POST":
        result = request.form
        current_date =datetime.now()
        data={
            "task":result.get('task'),
            "status":False,
            "create_at":current_date,
            "updated_at":current_date,
        }
        mycol.insert_one(data)
        print("posted data",data)
        return redirect(url_for("home"))
    result=mycol.find().sort('status',1)

    return render_template("home.html", result=result)
@app.route("/update/<id>", methods = ["GET"])
def update(id):
    current_data=mycol.find_one({'_id':ObjectId(id)})
    newvalues = {  "$set": { "status":not current_data['status']} }
    x=mycol.update_one({"_id":ObjectId(id)},newvalues)
    return redirect(url_for('home'))    
@app.route("/delete/<id>", methods = ["POST"])
def delete(id):
    x=mycol.delete_one({'_id':ObjectId(id)})
    print(x.deleted_count, " documents deleted.")
    return redirect(url_for('home'))    


if __name__ == "__main__":
    app.run(debug = True)