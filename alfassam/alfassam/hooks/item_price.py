import frappe

def on_update(doc, method):
    if doc.price_list == 'Standard Selling' and doc.selling == 1:
        frappe.db.set_value("Item", doc.item_code, "standard_rate", doc.price_list_rate)