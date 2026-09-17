import requests

url = "http://127.0.0.1:5000/data"


def get_items():
    response = requests.get(url)

    print(response.status_code)

    data = response.json()
    return data["items"]

def show_items():
    items = get_items()
    online_count = 0

    for item in items:
        print("Device:", item["name"])
        print("status:", item["status"])
        if item["status"] == "online":
           online_count += 1
    print("online items:", online_count)



def create_item(item):
    response = requests.post(url, json=item)

    print(response.status_code)
    print(response.json())

    if response.status_code == 200:
        print("Item created successfully")
    else:
        print("Failed to create item")





def update_item(item_id, item):
    put_response = requests.put(
        f"{url}/{item_id}",
        json=item
    )

    print(put_response.status_code)
    print(put_response.json())

def delete_item(item_id):
    delete_response = requests.delete(
        f"{url}/{item_id}"
    )

    print(delete_response.status_code)
    print(delete_response.json())

while True:
  choice = input("""
1. Show Items
2. Create Item
3. Update Item
4. Delete Item
5. Exist

Enter your choice:
""")
  if  choice == "1" :
     show_items()
  elif choice == "2" :
      items = get_items()
      if items:
          new_id = max(item["id"] for item in items) +1
      else:
         new_id = 1
      name = input("Enter divice name: ")
      create_item({
         "id": new_id,
         "name": name,
         "status": "online"
       })
  elif choice == "3" :
      item_id = int(input("Enter item ID to update:"))
      new_name = input("Enter new device:")
      update_item(item_id, {
         "name": new_name,
         "status": "offline"
       })
  elif choice == "4" :
      item_id = int(input("Enter item ID to delete:"))
      delete_item(item_id)
  elif choice == "5" :
      print("Existing...")
      break
  else:
    print("Invalid chice. Please try agin.")