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


def check_device_health():
    items = get_items()
    
    for item in items:
        health_status = "NORMAL"
        problems = []      
        if item["temperature"] >= 70:
            health_status = "CRITICAL"
            problems.append("High temperature")

        if item["cpu"] >= 80:
           problems.append("High CPU")
           if health_status != "CRITICAL":
               health_status = "WARNING"

        if item["memory"] >= 80:
            problems.append("High Memory")
            if health_status != "CRITICAL":
              health_status = "WARNING"

        print(f"{item['name']} → {health_status}")
        if problems:
           print("Problems:")
           for problem in problems:
               print(f"- {problem}")


def filter_items(status):
    items = get_items()
    filtered_items = []
    
    for item in items:
        if item["status"] == status:
            filtered_items.append(item)
    return filtered_items 

def sort_items(items, x):
    copy_items = items.copy()
    copy_items.sort(key=lambda item: item[x])
    return copy_items

def sort_items_reverse(items, key_name):
    copy_items = items.copy()
    copy_items.sort(reverse=True, key=lambda item: item[key_name])
    
    return copy_items

def find_item_by_name(name):
    items = get_items()
    find_items = []
    
    for item in items:
        if item["name"] == name:
            find_items.append(item)
    return find_items 


def run_automation():
    print("=== Starting Automation ===")
    
    check_device_health()
    auto_fix_offline_items()
    check_device_health()
    check_items()
    automation_report()

    print("=== Automation Finished ===")

def menu():
    while True:
        print("""
=== Delta-500 Menu ===

1. Show Online Devices
2. Sort by Memory
3. Sort by Memory (Reverse)
4. Find Device by Name
5. Exit
""")

        choice = input("Enter your choice: ")

        if choice == "1":
            items = filter_items("online")
            print("=== Online Devices ===")

            for item in items:
                print(item["name"], "status:", item["status"])

        elif choice == "2":
            items = filter_items("online")
            sorted_items = sort_items(items, "memory")
            print("=== Sort by Memory ===")

            for item in sorted_items:
                print(item["name"], "memory:", item["memory"])

        elif choice == "3":
            items = filter_items("online")
            sorted_items_reverse = sort_items_reverse(items, "memory")
            print("=== Sort by Memory (Reverse) ===")

            for item in sorted_items_reverse:
                print(item["name"], "memory:", item["memory"])

        elif choice == "4":
            name = input("Enter Name: ")
            find_items = find_item_by_name(name)

            print("=== Find Device by Name ===")

            for item in find_items:
                print(item)

        elif choice == "5":
            print("Exiting Menu...")
            break
        else:
            print("Invalid choice. Please try again.")


def main():
    run_automation()
    menu()


if __name__ == "__main__":
    main()



