
def mortalRabbits(months, lifespan):

    generations = [1] + [0]*(lifespan - 1) #[1, 0, ... , lifespan - 1]

    for i in range(months-1): #every month except initial

        newborn_rabbits = sum(generations[1:]) # sum of every gen except initial

        generations = [newborn_rabbits] + generations[:-1] # creates new initial gen and shifts every other gen "off the list" each month

    return sum(generations)

print(mortalRabbits(100,20))
