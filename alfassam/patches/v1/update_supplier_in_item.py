import frappe

def execute():
    try:
        item_list = frappe.db.get_list("Item Supplier",fields=['name', 'parent', 'supplier'])
        for item in item_list:
            frappe.db.set_value("Item", item.parent, "supplier", item.supplier)
            frappe.db.commit()
        print("Updated Supplier in Item!")
    except Exception as e:
        frappe.db.rollback()
        print(e)