from flask import Flask, jsonify,request
app=Flask(__name__)
def status():
    return{
        "status":"online",
        "project":"Delta-500",
        "week":9
    }

@app.route("/data/<int:id>", methods=["PUT"])
def update_data(id):
    data = request.json
    return {
        "id":id,
        "updated": data,
        "status":"updated"
    } 

if __name__=="__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)    
