# Copyright (c) 2024, ahmed.g.abdin@gmail.com and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
from datetime import datetime
from frappe.utils import add_to_date


class RiderSalarySlip(Document):
    def validate(self):
        if not self.start_date:
            today = datetime.today()
            first_day_of_month = datetime(today.year, today.month, 1)
            self.start_date = first_day_of_month.strftime("%Y-%m-%d")
        if not self.end_date:
            today = datetime.today()
            first_day_of_next_month = datetime(today.year, today.month + 1, 1)
            last_day_of_month = add_to_date(first_day_of_next_month, days=-1)
            self.end_date = last_day_of_month
        if not self.payroll_month:
            date = datetime.strptime(self.start_date, "%Y-%m-%d")
            self.payroll_month = date.strftime("%B")
