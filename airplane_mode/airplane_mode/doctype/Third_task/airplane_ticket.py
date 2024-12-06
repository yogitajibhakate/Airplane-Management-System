

# Copyright (c) 2024, Yogita and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class AirplaneTicket(Document):
    def validate(self):
        self.check_flight_capacity()
        self.calculate_total_amount()
        self.validate_airplane_ticket()

    def check_flight_capacity(self):
        flight = frappe.get_doc("Airplane Flight", self.flight)
        airplane = frappe.get_doc("Airplane", flight.airplane)
        capacity = airplane.capacity
        tickets_count = frappe.db.count('Airplane Ticket', filters={'flight': self.flight})
        if tickets_count >= capacity:
            frappe.throw(f"This flight is full. Cannot book more than {capacity} tickets for this flight.")

    def calculate_total_amount(self):
        total_add_ons = 0
        if self.add_ons:
            for add_on in self.add_ons:
                total_add_ons += add_on.amount
        self.total_amount = self.flight_price + total_add_ons

    def validate_airplane_ticket(self):
        if self.status != "Boarded":
            frappe.throw("The Airplane Ticket cannot be submitted unless the status is 'Boarded'.")

    # def before_insert(self):
    #     random_number = random.randint(1, 100)
    #     random_letter = random.choice(['A', 'B', 'C', 'D', 'E'])
    #     self.seat = f"{random_number}{random_letter}"


