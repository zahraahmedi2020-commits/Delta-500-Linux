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

def check_items():
    items = get_items()

    for item in items:
        if item["status"] == "online":
            print(f'{item["name"]} is online')
        else:
            print(f'{item["name"]} is offline')

def find_offline_items():
    items = get_items()

    for item in items:
        if item["status"] == "offline":
            print(f'{item["name"]} is offline')

def count_offline_items():
    items = get_items()
    offline_count = 0

    for item in items:
        if item["status"] == "offline":
            offline_count += 1

    print("offline items:", offline_count)

def monitor_items():
    items = get_items()
    offline_count = 0

    for item in items:
        if item["status"] == "offline":
            offline_count += 1
            print(f'ALERT: {item["name"]} is offline')

    if offline_count == 0:
        print("All devices are online")
    else:
        print(f"Total offline items: {offline_count}")

def update_item(item_id, name, status):
    data = {
        "id": item_id,
        "name": name,
        "status": status
    }

    response = requests.put(
        f"{url}/{item_id}",
        json=data
    )

    print(response.status_code)
    print(response.json())

def auto_fix_offline_items():
    items = get_items()
    fixed_count = 0
    for item in items:
        if item["status"] == "offline":
            print(f'Fixing: {item["name"]}')

            update_item(
                item["id"],
                item["name"],
                "online"
                )
        fixed_count += 1
    print(f'Fixed items: {fixed_count}')

def automation_report():
    items = get_items()

    online_count = 0
    offline_count = 0

    for item in items:
        if item["status"] == "online":
            online_count += 1
        elif item["status"] == "offline":
            offline_count += 1

    print("=== Automation Report ===")
    print(f"Online devices: {online_count}")
    print(f"Offline devices: {offline_count}")

def run_automation():
    print("=== Starting Automation ===")

    auto_fix_offline_items()
    check_items()
    automation_report()

    print("=== Automation Finished ===")

run_automation()