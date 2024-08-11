def calc_total(doc, event):
    salary_components = doc.salary_components
    total = 0
    for comp in salary_components:
        if (comp.rate != None and comp.rate != 0) and (
            comp.variable != None and comp.variable != 0
        ):
            comp.amount = comp.variable * comp.rate
        if comp.amount != None and comp.amount != 0:
            total += comp.amount
    # print(total)
    doc.total = total
