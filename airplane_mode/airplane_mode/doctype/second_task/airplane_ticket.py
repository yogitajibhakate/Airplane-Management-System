

# Copyright (c) 2024, Yogita and contributors
# For license information, please see license.txt

import frappe
import random
import string
from frappe.model.document import Document

class AirplaneTicket(Document):
    def validate(self):
        self.calculate_total_amount()
        self.validate_airplane_ticket()
        self.before_insert()


    def calculate_total_amount(self):
        total_add_ons = 0
        if self.add_ons:
            for add_on in self.add_ons:
                total_add_ons += add_on.amount
        self.total_amount = self.flight_price + total_add_ons

    def validate_airplane_ticket(self):
        if self.status != "Boarded":
            frappe.throw("The Airplane Ticket cannot be submitted unless the status is 'Boarded'.")

    def before_insert(self):
        random_number = random.randint(1, 100)
        random_letter = random.choice(['A', 'B', 'C', 'D', 'E'])
        self.seat = f"{random_number}{random_letter}"


