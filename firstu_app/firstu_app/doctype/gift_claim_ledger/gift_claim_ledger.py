# Copyright (c) 2022, sandra thomas and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class GiftClaimLedger(Document):
	def before_save(self):
		doc=frappe.get_doc("Customer",self.customer)
		a=frappe.db.get_value("Gift Ledger","trophies_number")
		b=frappe.db.get_value("Gift Ledger","gift_number")
		if  doc.number_of_trophies >= a :
			if self.gift_ledger==b:
				doc.submit()
		else:
			frappe.throw("insufficient Trophy")
	def before_submit(self): 
		data=frappe.get_doc({'doctype':"Trophy Ledger",'customer':self.customer,'status':"DEBITED",self.number_of_trophies:"number_of_trophies"})
		data.insert(ignore_permissions = True)
		data.submit()
