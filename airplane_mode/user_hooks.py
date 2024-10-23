import frappe

def on_user_create(doc, method):
    passenger = frappe.get_doc({
            'doctype': 'Flight Passenger',
            'first_name': doc.first_name,
            'last_name': doc.last_name,
        })
    passenger.insert() 