people = 30
cars = 40
trucks = 15

if cars > people:
    print("We should take the cars")
elif cars < people:
    print("We shouldn't take the cars")
else:
    print("We can't decide")

if trucks > cars:
    print("that is too many trucks")
elif trucks < cars:
    print("maybe we could take the trucks")
else:
    print("We still can't decide.")

if people > trucks:
    print("Alright, lets just take the trucks.")
else:
    print("Fine, let's stay home then.")
