# Copyright (c) 2022, sandra thomas and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class MoneyRedeem(Document):
	def before_save(self):
		doc=frappe.get_doc("Customer",self.customer)
		if doc.total_earned_cashback >= doc.balance_amount:
			self.amount == doc.total_earned_cashback
			doc.balance_amount = doc.balance_amount -self.amount
			doc.customer=self.customer,
			doc.save()
			
		else:
			frappe.throw("insufficient balance")

	def before_submit(self): 
		data=frappe.get_doc({'doctype':"Cashback Ledger",'customer':self.customer,'status':"Redeemed",'amount':self.amount})
		data.insert(ignore_permissions = True)
		data.submit()
	
	


