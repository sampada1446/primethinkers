from flask import Flask, request, jsonify, render_template
import pymysql
from db_connection import getConnection

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/save_project', methods=['POST'])
def save_project():

    project_name = request.form['project_name']
    location = request.form['location']
    area = request.form['area']
    budget = request.form['budget']

    plan = "AI Generated Construction Plan"

    connection = getConnection()
    cursor = connection.cursor()

    sql = "INSERT INTO projects(project_name,location,area,budget,plan) VALUES(%s,%s,%s,%s,%s)"
    
    cursor.execute(sql,(project_name,location,area,budget,plan))

    connection.commit()

    cursor.close()
    connection.close()

    return jsonify({"message":"Project Saved Successfully"})


if __name__ == "__main__":
    app.run(debug=True)