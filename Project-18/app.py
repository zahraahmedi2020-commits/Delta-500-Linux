from flask import Flask, jsonify
app=Flask(__name__)
def status():
    return{
        "status":"online",
        "project":"Delta-500",
        "week":9
    }
@app.route("/status", methods=["GET"])
def get_status():
    return jsonify(status())

if __name__=="__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)    
