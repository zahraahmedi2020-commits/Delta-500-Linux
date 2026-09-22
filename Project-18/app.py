from flask import Flask, jsonify,request
app=Flask(__name__)
items = [
    {
        "id": 1,
        "name": "Server",
        "status": "online",
        "cpu": 35,
        "memory": 45,
        "temperature": 42
    },
    {
        "id": 2,
        "name": "Router",
        "status": "online",
        "cpu": 85,
        "memory": 60,
        "temperature": 50
    },
    {
        "id": 3,
        "name": "Switch",
        "status": "online",
        "cpu": 40,
        "memory": 82,
        "temperature": 73
    }
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
@app.route("/data/<int:item_id>", methods=["PUT"])
def update_data(item_id):
   data = request.json

   for item in items:
      if item["id"] == item_id:
         item["name"] = data["name"]
         item["status"] = data["status"]

         return {
            "id": item_id,
            "updated": data,
            "status": "updated"
        }

   else:
      return {
        "status": "error",
        "message": "Item not found"
    }, 404

@app.route("/data/<int:item_id>", methods=["DELETE"])
def delete_data(item_id):
    for item in items:
      if item["id"] == item_id:
         items.remove(item)

         return {
            "id": item_id,
            "status": "deleted"
        }
 
    return {
        "status": "error",
        "message": "Item not found"
    }, 404

if __name__=="__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)    
