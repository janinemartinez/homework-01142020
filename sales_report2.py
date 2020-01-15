from pprint import pprint, pformat

"""Generate sales report showing total melons each salesperson sold."""

#creating empty lists to deposit the data for sales people and nuumber of melons sold.
salespeople = {}

#a for loop which splits the lines from the source document into lists. 
f = open('sales-report.txt')
for line in f:
    line = line.rstrip()
    person, amount, qty = line.split('|')
    #moves items from those lists into variables
    if person not in salespeople:
        # initiaize
        salespeople[person] = {"num_melons" : int(qty), "total" : float(amount)}
    else:
        salespeople[person]["num_melons"] += int(qty)
        salespeople[person]["total"] += float(amount)


pprint(salespeople)


