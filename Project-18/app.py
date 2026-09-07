from flask import Flask, jsonify,request
app=Flask(__name__)
def status():
    return{
        "status":"online",
        "project":"Delta-500",
        "week":9
    }

@app.route("/data/<int:id>", methods=["DELETE"])
def delete_data(id):
    return {
        "id":id,
        "status":"deleted"
    } 

if __name__=="__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)    
