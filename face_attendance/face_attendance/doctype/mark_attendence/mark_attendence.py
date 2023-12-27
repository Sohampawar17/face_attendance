# Copyright (c) 2023, quantbit technologies pvt. ltd  and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class MarkAttendence(Document):
	
	def before_save(self):
		new_doc=frappe.new_doc('face Checkin')
		new_doc.employee_id=self.employee_id
		new_doc.insert()
		new_doc.save()