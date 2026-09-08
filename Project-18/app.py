from flask import Flask, jsonify,request
app=Flask(__name__)
items = [
    {"id": 1, "name": "Server", "status": "online"},
    {"id": 2, "name": "Router", "status": "online"}
]
def data():
    return{
        "status":"online",
        "project":"Delta-500",
        "week":10
    }
@app.route("/data", methods=["GET"])
def get_data():
    return {
        "items": items
    } 
@app.route("/data", methods=["POST"])
def receive_data():
    data = request.json
    items.append(data)
    return {
        "resived": data,
        "status": "success"
    }

if __name__=="__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)    
