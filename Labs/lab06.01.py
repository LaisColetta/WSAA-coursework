from flask import Flask,request, jsonify
app = Flask (__name__)

@app.route ('/')
def index():
    return 'Hello'

@app.route ('/books',methods = ['GET'])
def getall():
    return 'get all'

@app.route ('/books/<int:id>',methods = ['GET'])
def findbyid(id):
    return 'find by id'

@app.route ('/books',methods = ['POST'])
def create():
    jsonstring = request.json
    return f'create {jsonstring}'

@app.route ('/books',methods = ['PUT'])
def update():
    jsonstring = request.json
    return f'update {id} {jsonstring}'

@app.route ('/books',methods = ['DELETE'])
def delete():
    return 'delete'

if __name__ == '__main__':
    app.run (debug = True)
