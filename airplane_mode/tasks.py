import frappe
from frappe.utils import nowdate, getdate

def rent_reminder():
    today = getdate(nowdate())
    
    # Check if today is the 1st of the month
    if today.day == 1:
        contracts = frappe.get_all('Contract', filters={'expiry_date': ['>=', today]}, fields=['tenant_email', 'expiry_date'])
            
        for contract in contracts:
            tenant_email = contract['tenant_email']
                
            frappe.sendmail(
                    recipients=[tenant_email],
                    subject="Monthly Rent Reminder",
                    message="This is a reminder that your rent is due. Please make the necessary arrangements."
                )

