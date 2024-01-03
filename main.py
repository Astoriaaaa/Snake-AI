import random 
from snake import *
generations = 100


def randompopulation():
    def myfunc(a): 
        return random.random()
    population = [] 
    for i in range(50): 
        snake = list (map(myfunc, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
        population.append(snake)
    return population

def fitness(population, num):
    scores = []
    for i in range(len(population)):
        points = run_game(population[i], i, num)
        scores.append(points)
    return scores 

def generateChildren(parents): 
    new_pop =[]

    while len(new_pop) < 45:
        parent1 = random.choice(parents)
        parent2 = random.choice(parents)

        child = []
        for i in range(18): 
            num = random.choice([0, 1])
            if num == 0: 
                child.append(parent1[i])
            else: 
                child.append(parent2[i])

        new_pop.append(child)

    new_pop.extend(parents)
    
    return new_pop

new_pop = randompopulation()

for i in range(1000): 
    parents = []
    scores = fitness(new_pop, i)
    topScores = list(reversed(sorted(scores.copy())))[0: 6]
    print(topScores)
    for i in range(len(topScores)): 
        for j in range(50): 
            if topScores[i] == scores[j]:
                parents.append(new_pop[j])
                break

    new_pop = generateChildren(parents)

    
    




 
    
    