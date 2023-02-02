import sqlite3
from flask import Flask, request, jsonify
from flask_cors import CORS

# Function to connect to database
def connect_to_db():
    conn = sqlite3.connect('census.db')
    return conn

# Function to fetch all data entries depending on table mentioned in route
def get_data(table):
    data = []
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        select_all_demographic = "SELECT * FROM Demographic"
        select_all_income = "SELECT * FROM Income"
        if(table == 'demographic'):
            cur.execute(select_all_demographic)
        elif(table == 'income'):
            cur.execute(select_all_income)
        rows = cur.fetchall()

        # convert row objects to dictionary
        if(table == 'demographic'):
            for i in rows:
                dict = {}
                dict['id'] = i['id']
                dict['fnlwgt'] = i['fnlwgt']
                dict['age'] = i['age']
                dict['gender'] = i['gender']
                dict['race'] = i['race']
                dict['marital_status'] = i['marital_status']
                dict['relationship'] = i['relationship']
                dict['native_country'] = i['native_country']
                dict['education_level'] = i['education_level']
                data.append(dict)
        elif(table == 'income'):
            for i in rows:
                dict = {}
                dict['id'] = i['id']
                dict['d_id'] = i['d_id']
                dict['occupation'] = i['occupation']
                dict['workclass'] = i['workclass']
                dict['hours_per_week'] = i['hours_per_week']
                dict['capital'] = i['capital']
                dict['total_income'] = i['total_income']
                data.append(dict)

    except:
        data = []

    return data

# Function to fetch data entries from Demographic table by input age in route
def get_data_by_age(age):
    data = []
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM Demographic WHERE age = ?", (age,))
        rows = cur.fetchall()

        # convert row object to dictionary
        for i in rows:
            dict = {}
            dict['id'] = i['id']
            dict['fnlwgt'] = i['fnlwgt']
            dict['age'] = i['age']
            dict['gender'] = i['gender']
            dict['race'] = i['race']
            dict['marital_status'] = i['marital_status']
            dict['relationship'] = i['relationship']
            dict['native_country'] = i['native_country']
            dict['education_level'] = i['education_level']
            data.append(dict)
    except:
        data = []

    return data


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/api/data/demographic', methods=['GET'])
def api_get_demographic_data():
    return jsonify(get_data('demographic'))

@app.route('/api/data/income', methods=['GET'])
def api_get_income_data():
    return jsonify(get_data('income'))

@app.route('/api/data/<age>', methods=['GET'])
def api_get_data_by_age(age):
    return jsonify(get_data_by_age(age))

if __name__ == "__main__":
    app.run()