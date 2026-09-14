import requests

url = "http://127.0.0.1:5000/data"
response = requests.get(url)

print(response.status_code)
data = response.json()
items = data["items"]
online_count = 0
for item in items:
    print("Device:", item["name"])
    print("status:", item["status"])
    if item["status"] == "online":
        online_count += 1
print("online items:", online_count)
item_exists = False

for item in items:
    if item["id"] ==3:
        item_exists = True
        break
if not item_exists:
    new_item = {
       "id": 3,
       "name": "Switch",
       "status": "online"
    }

    post_response = requests.post(url, json=new_item)

    print(post_response.status_code)
    print(post_response.json())

    if post_response.status_code == 200:
       print("Item created successfully")
    else:
       print("Failed to create item")
else:
    print("item Whith ID 3 lready exists")


update_item = {
    "name": "Main Switch",
    "status": "offline"
}

put_response = requests.put(
    "http://127.0.0.1:5000/data/3",
    json=update_item
)

print(put_response.status_code)
print(put_response.json())


delete_response = requests.delete(
    "http://127.0.0.1:5000/data/1",)

print(delete_response.status_code)
print(delete_response.json())