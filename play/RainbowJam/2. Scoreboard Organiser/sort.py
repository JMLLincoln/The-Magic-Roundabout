from random import shuffle

goal = [
    "TOP",
    "JUNGLE",
    "MID",
    "ADC",
    "SUPPORT"
    ]

init = [
    "TOP",
    "JUNGLE",
    "MID",
    "ADC",
    "SUPPORT"
    ]

shuffle(init)


print ("From:")
for item in init:
    print (item)
    
print ("\nTo")
for item in goal:
    print (item)
    
print ("\nMoves: ")
counter = 0
for item in init:
    a, b = init.index(item), goal.index(item)
    if a != b:
        print ("Swapping %s with %s" % (init[a], init[b]))
        init[b], init[a] = init[a], init[b]
        counter += 1

print ("\nCompleted in %s moves:" % counter)


