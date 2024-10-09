# Copyright (c) 2024, skyscanner and contributors
# For license information, please see license.txt

import frappe
from frappe.query_builder import DocType
from frappe.query_builder.functions import Count, Sum
from pypika.terms import Case


def execute(filters=None):
	columns = get_coulmn()
	data = get_data()
	return columns, data

def get_coulmn():
	return [
		{
			'fieldname':'airline',
			'lable':'Airline',
            'fieldtype':'Data',
			'options': ''
		},
		{
			'fieldname':'revenue',
			'lable': 'Revenue',
            'fieldtype':'Currency'
		}
	]

def get_data():

	result = frappe.db.sql(
		f"""
		SELECT air.airline,airT.total_amount 
		FROM `tabAirplane Flight` AS airF
		INNER JOIN `tabAirplane` AS air ON air.name = airF.airplane
		INNER JOIN `tabAirplane Ticket` AS airT ON airT.flight = airF.name
		GROUP BY air.airline
		"""
		)
	print("Hello Result: ",result)
	return result