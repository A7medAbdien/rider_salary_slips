# Copyright (c) 2024, ahmed.g.abdin@gmail.com and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class RiderSalaryComponent(Document):
    def before_insert(self):
        self.amount = self.variable * self.rate
