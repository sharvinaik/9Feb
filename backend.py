from flask import Flask, jsonify, request, json
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from datetime import datetime
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_jwt_extended import (create_access_token)
from TweetsExtractor import *
import json
import pickle
from pymongo import MongoClient
from CheckTwitterHandle import checkTwitterID

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'bigfiveUser'
app.config['MONGO_URI'] = 'mongodb://127.0.0.1:27017/bigfiveUser'
app.config['JWT_SECRET_KEY'] = 'secret'

mongo = PyMongo(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

CORS(app)
traits = []
@app.route('/register', methods=['POST', 'GET'])
def register():
    users = mongo.db.users
    
    uname = request.get_json()['uname']
    print (uname)
    
    if users.find({"uname": uname}).count() > 0:
        print("Not Unique")
    else:
        print("Unique")
    
    email = request.get_json()['email']
    print (email)
    twitterID = request.get_json()['twitterID']
    print (twitterID)
    if checkTwitterID(twitterID) == True:
        print("Valid")
    else:
        print("Invalid")
        
    gender = request.get_json()['gender']
    print (gender)
    age = request.get_json()['age']
    print (age)
    password = bcrypt.generate_password_hash(request.get_json()['psw']).decode('utf-8')
    created = datetime.utcnow()
    traits = postTwitterID(twitterID)
    user_id = users.insert({
        'uname': uname,
        'email': email,
        'twitterID' : twitterID,
        'age': age,
        'gender': gender,
        'password' : password,
        'created'  :created,
        'openness' : traits[0],
        'conscientiousness' : traits[1],
        'extraversion' : traits[2],
        'agreeableness' : traits[3],
        'neuroticism' : traits[4],
    })

    new_user = users.find_one({'_id': user_id})

    result = {'uname': new_user['uname'] + " registered"}

    json_data = uiTwitterID(twitterID)
    return json_data #jsonify({'result': uname})

@app.route('/login', methods=['POST', 'GET'])
def login():
    users = mongo.db.users
    uname = request.get_json()['uname']
    password = request.get_json()['psw']
    result = ""

    response = users.find_one({'uname': uname})

    if response:
        if bcrypt.check_password_hash(response['password'], password):
            access_token = create_access_token(identity = {
                'email': response['email'],
                'contact': response['contact'],
            })
            result = jsonify({"token": access_token})
        else:
            result = jsonify({"error": "Invalid username or password"})
    else:
        result = jsonify({"result": "No result found"})
    return result

# @app.route('/twitterID', methods=['POST', 'GET'])
def postTwitterID(twitterID):
    # twitterID = request.get_json()['twitterID']
    print (twitterID)
    i = PersonalityInsights()
    traits = i.watsonSubmission(i.pullTweets(twitterID), twitterID) 
    return traits
    # data = {}
    # index = 0
    # for i in range(0, 5):
    #     for r in recommendations[i]:
    #         data[r['url']] = r['title']
    #         json_data = json.dumps(data)    
    #         print(r['title'])
    #         index+=1
    
    # return jsonify(json_data)


# @app.route('/twitterID', methods=['POST', 'GET'])
def uiTwitterID(twitterID):
    # twitterID_card = request.get_json()['twitterID_Card']
    # if twitterID_card == "":
    
    connection = MongoClient("localhost", 27017)
    db = connection.bigfiveUser
    userTable = db.users        
    myquery = {"twitterID" : twitterID}
    user = userTable.find(myquery)
    print("USER INFORMATION")
    print(user)
    traits = []
    for u in user:
        traits.append(u['openness'])
        traits.append(u['conscientiousness'])
        traits.append(u['extraversion'])
        traits.append(u['agreeableness'])
        traits.append(u['neuroticism'])
    # print (twitterID)
    i = PersonalityInsights()
    print(traits)
    recommendations = i.getRecommendations(traits)
    complete_list = []
    for i in range(0, 5):
        for r in recommendations[i]:            
            data = {}       
            data['title'] = r['title']
            data['url'] = r['url']
            complete_list.append(data)
    json_data = json.dumps(complete_list) 
    print(complete_list)
    return json_data


@app.route('/twitterID', methods=['POST', 'GET'])
def uiLoginTwitterID():
    twitterID_card = request.get_json()['id']
    print(twitterID_card)
    
    i = PersonalityInsights()
    # print(traits)
    traits = i.watsonSubmission(i.pullTweets(twitterID_card), twitterID_card)
    print(traits)
    recommendations = i.getRecommendations(traits)
    complete_list = []
    for i in range(0, 5):
        for r in recommendations[i]:            
            data = {}       
            data['title'] = r['title']
            data['url'] = r['url']
            complete_list.append(data)
    json_data = json.dumps(complete_list) 
    print(complete_list)
    return json_data
   


if __name__ == '__main__':
    app.run(debug=True)