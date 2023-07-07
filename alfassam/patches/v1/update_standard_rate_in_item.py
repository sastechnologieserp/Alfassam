import frappe

def execute():
    try:
        item_list = frappe.db.get_list("Item")
        for item in item_list:
            item_price = frappe.db.get_value("Item Price", 
                {
                    'item_code': item.name, 
                    'price_list': 'Standard Selling', 
                    'selling': 1
                },
                'price_list_rate'
            )
            if item_price:
                frappe.db.set_value("Item", item.name, "standard_rate", item_price)
                frappe.db.commit()
    except Exception as e:
        frappe.db.rollback()
        print(e)