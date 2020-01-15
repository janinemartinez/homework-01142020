"""Generate sales report showing total melons each salesperson sold."""

#creating empty lists to deposit the data for sales people and nuumber of melons sold.
salespeople = []
melons_sold = []

#a for loop which splits the lines from the source document into lists. 
f = open('sales-report.txt')
for line in f:
    line = line.rstrip()
    entries = line.split('|')
    #moves items from those lists into variables
    salesperson = entries[0]
    melons = int(entries[2])
    #increases running total of melons sold by sales persons if they already have indexes.
    if salesperson in salespeople:
        position = salespeople.index(salesperson)

        melons_sold[position] += melons

    #creates entries in the melons_sold list and the salesperson lists if they do not yet exist.
    else:
        salespeople.append(salesperson)
        melons_sold.append(melons)

#prints data from both lists relative to eachother in a statement.
for i in range(len(salespeople)):
    print(f'{salespeople[i]} sold {melons_sold[i]} melons')

#all this data ought to have been stored in a dictionary instead of two lists. it would be faster, easier to maintain, and more efficient.
