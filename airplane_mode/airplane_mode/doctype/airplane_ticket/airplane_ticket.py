# Copyright (c) 2024, skyscanner and contributors
# For license information, please see license.txt

import frappe
import random
import string
from frappe.model.document import Document

class AirplaneTicket(Document):
	@staticmethod
	def generate_seat_number():
		numbers = ''.join(random.choices(string.digits, k=2))
		alphabet = random.choice(string.ascii_uppercase)
		seat_number = f"{numbers}{alphabet}"
		return seat_number	
		
	def before_save(self):
		totalAmount = self.flight_amount
		for add in self.add_ons:
			totalAmount += add.amount

		# print("hello world: ", totalAmount)
		self.total_amount = totalAmount
		seat = self.generate_seat_number()
		self.seat= seat
		self.seat_count()

	def seat_count(self):
		flight = frappe.get_doc("Airplane Flight", self.flight)
		airplane = frappe.get_doc("Airplane", flight.airplane)
		ticket_count = frappe.db.count("Airplane Ticket",filters = {"flight":self.flight})
		if ticket_count >= airplane.capacity:
			frappe.throw(("Cannot create ticket. The airplane for this flight is fully booked."))
		