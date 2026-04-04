api_response = {
    "status": 200,
    "data": {
        "orders": [
            {"id": 101, "total": 59.99, "status": "shipped", "items": ["shoes", "belt"]},
            {"id": 102, "total": 120.00, "status": "pending", "items": ["jacket"]},
            {"id": 103, "total": 35.50, "status": "shipped", "items": ["hat", "socks"]},
        ]
    }
}

orders = api_response["data"]["orders"]

shipped = [o for o in orders if o["status"] == "shipped"]

revenue = sum(o["total"] for o in orders )

all_items = [item for o in orders for item in o["items"]]
print(all_items)

expensive = [o["id"] for o in orders if o["total"] > 50]
print(expensive)