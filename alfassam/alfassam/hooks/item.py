import frappe

def validate(doc, method):
    if doc.supplier_items:
        doc.supplier = doc.supplier_items[0].supplier