from frappe.model.naming import make_autoname
import frappe

def autoname(doc, method):
    if doc.division:
        doc.cost_center = doc.division
    if doc.cost_center == "HOE - AT&IC":
        doc.name= make_autoname(f"H-{doc.naming_series}")
    elif doc.cost_center == "Real Estate - AT&IC":
        doc.name= make_autoname(f"R-{doc.naming_series}")
    elif doc.cost_center == "Investment - AT&IC":
        doc.name= make_autoname(f"I-{doc.naming_series}")

def validate(doc, method):
    if doc.division:
        doc.cost_center = doc.division
    set_cost_center(doc)


def set_cost_center(doc):
		for item in doc.get("accounts"):
			item.cost_center = doc.cost_center