import frappe

def get_context(context):
    context.shops = frappe.get_all("Shop", fields=["shop_name", "shop_number","rent_amount", "airport", "area_of_shop", "is_available",])
    
