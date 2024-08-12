from rider_salary_slips.rider_salary_slips.doctype.rider_salary_slip.calc_total import (
    calc_total,
)


def on_update_salary_slip(doc, ev):
    """
    Triggered when a rider salary slip is updated.
    """
    print("\n\n\n Salary slip updated")
    # Recalculate the total salary
    calc_total(doc, ev)
