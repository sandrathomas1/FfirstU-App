# Copyright (c) 2022, sandra thomas and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Customer(Document):
	pass
	def validate(self): 
#pass
#doc=frappe.get_doc("Trophy Ledger",self.trophy_ledger)
		a=frappe.db.get_single_value("Trophy Settings","refuel_frequency")
		b=frappe.db.get_single_value("Trophy Settings","number_of_trophy")
		if self.refuel_frequency >= a:
			self.number_of_trophies = b
			self.refuel_frequency=self.refuel_frequency - a
			data=frappe.get_doc({'doctype':"trophy_ledger",'customer':self.customer,'number_of_trophies':self.number_of_trophies,'status':"CREDITED"})
			data.insert(ignore_permissions = True)
			data.submit()

