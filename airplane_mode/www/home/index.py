import frappe

def get_context(context):
    context.flights = frappe.get_all("Airplane Flight", fields={"name","airplane","source_airport", "destination_airport", "date_of_departure","time_of_departure", "price"})
    
