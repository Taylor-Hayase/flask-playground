from flask import Flask
app = Flask(__name__)

users = { 
    "users_list" :
    [
        {  
            "id" : "xyz567",
            "username" : "teddy",
            "email" : "xyzteddy@calpoly.edu",
            "university" : "Cal Poly"
        },
        {
            "id" : "abc567",
            "username" : "bcdasilv",
            "email" : "bcdasilv@calpoly.edu",
            "university" : "Cal Poly"
        },
        {
            "id" : "yat999",
            "username" : "qwerty",
            "email" : "qwerty@mit.edu",
            "university" : "MIT"
        },
        {
            "id" : "oxz888",
            "username" : "gaby",
            "email" : "gaby33333@cuesta.edu",
            "university" : "Cuesta"
        }, 
        {
            "id" : "zap555",
            "username" : "gaby",
            "email" : "gaby5555@cuesta.edu",
            "university" : "Cuesta"
        } 
    ]
}

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/users')
@app.route('/users/<name>')
def get_users(name=None):
    if name :
        subdict = {"users_list" : []}
        for user in users["users_list"]:
            if user["username"] == name:
                subdict["users_list"].append(user)
        return subdict
    return users

# @app.route('/users/<username>')
# def get_users():
#     return users