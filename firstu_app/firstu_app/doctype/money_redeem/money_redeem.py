# Copyright (c) 2022, sandra thomas and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class MoneyRedeem(Document):
	def before_save(self):
		doc=frappe.get_doc("Customer",self.customer)
		#a=frappe.db.get_value("Money Redeem","amount")
		if doc.balance_amount > self.amount:
			self.amount == doc.balance_amount
			doc.balance_amount = doc.balance_amount-self.amount
			#d = frappe.get_doc({"doctype":"Customer",'customer':self.customer,"balance_amount":doc.balance_amount})
			#d.insert(ignore_permissions = True)
			#d.submit()
			#doc.update()
		else:
			frappe.throw("insufficient balance")

	def before_submit(self): 
		data=frappe.get_doc({'doctype':"Cashback Ledger",'customer':self.customer,'status':"Redeemed",'amount':self.amount})
		data.insert(ignore_permissions = True)
		data.submit()
	#def update(self):

		#d = frappe.get_doc({"doctype":"Customer",'customer':self.customer,"total_earned_cashback":doc.balance_amount})
        #a=frappe.db.get_value("Fuel Payment","cashback")
        #d.total_earned_cashback = a
		#d.insert(ignore_permissions = True)
		#d.save()


