import frappe

def get_context(context):
    context.csrf_token = frappe.sessions.get_csrf_token()
    # context.passengers = frappe.get_all("Flight Passenger", fields = {"name","full_name"})
    context.flights = frappe.get_all("Airplane Flight", fields = {"name","airplane"})
    

@frappe.whitelist()
def post():
    data = frappe.parse_json(frappe.local.request.get_data(as_text = True))

    passenger_name = data.get('passenger_name')
    seat_no = data.get('seat_no')
    flight_name = data.get('flight_name')

    if not passenger_name or not seat_no or not flight_name:
        frappe.local.response["http_status_code"] = 400 
        return {"message": "All fields are required"}
    
    try:
        booking = frappe.get_doc({
            'doctype': 'Airplane Ticket',
            'passenger_name': passenger_name,
            'seat_no': seat_no,
            'flight': flight_name
        })
        booking.insert()

        return {"message": "Booking added successfully!"}
    except Exception as e:
        frappe.local.response["http_status_code"] = 500 
        return {"message": f"An error occurred: {str(e)}"}

@frappe.whitelist()
def addPassenger():
    data = frappe.parse_json(frappe.local.request.get_data(as_text=True))

    first_name = data.get('first_name')
    last_name = data.get('last_name')
    dob = data.get('dob')

    if not first_name or not last_name or not dob:
        frappe.local.response["http_status_code"] = 400
        return {"message": "All fields are required"}

    try:
        passenger = frappe.get_doc({
            'doctype': 'Flight Passenger',
            'first_name': first_name,
            'last_name': last_name,
            'date_of_birth': dob
        })
        passenger.insert()

        return {"message": "Passenger added successfully!"}
    except Exception as e:
        frappe.local.response["http_status_code"] = 500 
        return {"message": f"An error occurred: {str(e)}"}
