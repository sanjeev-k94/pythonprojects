# Billing System Logic

import json
from datetime import datetime

class BillingSystem:
    def __init__(self):
        self.items = []
        self.varOcg = 0  # example variable

    def add_item(self, name, price, quantity):
        self.items.append({
            "name": name,
            "price": price,
            "quantity": quantity,
            "total": price * quantity
        })

    def generate_bill(self):
        total_amount = sum(item["total"] for item in self.items)
        bill = {
            "items": self.items,
            "total_amount": total_amount,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        return bill

    def save_bill(self, bill):
        with open("bill_output.json", "w") as f:
            json.dump(bill, f, indent=4)

    def run(self):
        print("==== Smart Billing System ====")
        while True:
            name = input("Enter item name (or 'done' to finish): ")
            if name.lower() == "done":
                break
            price = float(input("Enter price: "))
            quantity = int(input("Enter quantity: "))
            self.add_item(name, price, quantity)

        bill = self.generate_bill()
        self.save_bill(bill)
        print("Bill generated and saved as bill_output.json")
