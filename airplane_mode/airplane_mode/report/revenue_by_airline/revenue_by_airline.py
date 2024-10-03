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
			'lable':'Airline',
			'fieldname':'airline',
            'fieldtype':'Data',
		},
		{
			'lable': 'Revenue',
			'fieldname':'revenue',
            'fieldtype':'Currency'
		}
	]

def get_data():
	airT = frappe.qb.DocType("Airplane Ticket")
	airF = frappe.qb.DocType("Airplane Flight")
	air = frappe.qb.DocType("Airplane")

	result = frappe.db.sql(
		f"""
		SELECT air.airline,airT.total_amount 
		FROM airF
		INNER JOIN air ON air.name = airF.airplane
		INNER JOIN airT ON airT.flight = airF.name
		"""
		)
	print("Hello Result: ",result)
	return result

