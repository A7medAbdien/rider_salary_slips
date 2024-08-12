import frappe
from rider_salary_slips.rider_salary_slips.doctype.rider_salary_slip.calc_total import (
    calc_total,
)


def on_update_salary_slip(doc, ev):
    """Salary slip
    -rider id
    -month
    -total
    etc.
    Triggered when a rider salary slip is updated.
    """
    print("\n\n\n Salary slip updated")
    # Recalculate the total salary
    calc_total(doc, ev)
    update_rider_salary_slips_table(doc, ev)


def update_rider_salary_slips_table(doc, ev):
    """rider ss table
    - rider id
    - ss id
    - total
    - month

    doc: Salary slip

    Update the rider salary slip table with the latest data.

    notes: updatint salary slip name will crach it
    """
    print("\n\n\n Updating rider salary slip table")
    if frappe.db.exists("Rider Salary Slips Table", doc.name):
        ss_table = frappe.get_doc("Rider Salary Slips Table", doc.name)
        ss_table.parenttype = "Rider"
        ss_table.parentfield = "salary_slips"
        ss_table.parent = doc.rider_id
        ss_table.rider = doc.rider_id
        ss_table.total = doc.total
        ss_table.month = doc.payroll_month
        ss_table.save()
    else:
        ss_table = frappe.new_doc("Rider Salary Slips Table")
        ss_table.salary_slip = doc.name
        ss_table.parenttype = "Rider"
        ss_table.parentfield = "salary_slips"
        ss_table.parent = doc.rider_id
        ss_table.rider = doc.rider_id
        ss_table.total = doc.total
        ss_table.month = doc.payroll_month
        ss_table.save()
