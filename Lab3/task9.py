sequenceList = [[],[4],(1,2),[3,4],(5,6,7),[29,12,12],(1,1,1,1,1,-9,123)]
results = []
for element in sequenceList:
    results.append(sum(element))
print("Sum of elements:",results)