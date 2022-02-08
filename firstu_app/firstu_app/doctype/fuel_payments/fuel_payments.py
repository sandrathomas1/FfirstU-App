# Copyright (c) 2022, sandra thomas and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class FuelPayments(Document):
	def before_save(self): 
		doc=frappe.get_doc("Customer",self.customer)
		a=frappe.db.get_single_value("Fuel Price","petrol_price")
		b=frappe.db.get_single_value("Fuel Price","diesel_price")
		c=frappe.db.get_single_value("Fuel Price","petrol_privilage_price")
		d=frappe.db.get_single_value("Fuel Price","deisel_privilage_price")
		e=frappe.db.get_single_value("Fuel Price","petrol_status_price")
		f=frappe.db.get_single_value("Fuel Price","deisel_status_price")
		if doc.membership_type =='PRIVILAGE':
			if doc.fuel_type =='PETROL':
				self.current_fuel_price = a
				self.firstu_price=c
				self.litre =self.amount/ c
				self.cashback=(self.litre * a)-(self.litre * c)
			else:
				self.current_fuel_price = a
				self.firstu_price=d
				self.litre =self.amount/d
				self.cashback=(self.litre * a)-(self.litre * d)
		else: 
			if doc.fuel_type == 'DIESEL':
				self.current_fuel_price=b
				self.firstu_price= f
				self.litre =self.amount / f
				self.cashback=(self.litre * b)-(self.litre * f)
				
			else:
				self.current_fuel_price=b
				self.firstu_price = e
				self.litre =self.amount /int(e)
				self.cashback=(self.litre * b)-(self.litre * e)
				#doc.save()
	def before_submit(self): 
		data=frappe.get_doc({'doctype':"Cashback Ledger",'customer':self.customer,'status':"Received",'amount':self.amount})
		data.insert(ignore_permissions = True)
		data.submit()
	def update(self,d,customer):
		d = frappe.get_doc({"doctype":"Customer",'customer_name':self.customer,"total_earned_cashback":self.cashback})
		#a=frappe.db.get_value("Fuel Payment","cashback")
		#d.total_earned_cashback = a
		d.update()
		#d.save()

