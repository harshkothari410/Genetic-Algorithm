import random
import math

n = 0

#initilization of population
def initialization():
	population = []
	global n
	for x in range(n+1):
		individual = [random.randint(0,1) for x in range(8)]
		population.append(individual)
	return population

def fitness(population):
	pop_fit = []
	global n
	for x in range(n):
		pop_fitind = 0
		weight = [128,64,32,16,8,4,2,1]
		j = 0
		for var in population[x]:
			pop_fitind = pop_fitind +  var*weight[j]
			j = j+ 1
		pop_fit.append(pop_fitind)
	return pop_fit

def make_dic(population,pop_fit):
	return dict(zip(pop_fit,population))

def best_individual(pop_fit,pop_dict):
	global n 
	pop_fit.sort(reverse = True)
	best_pop = []
	n = n - 2
	print pop_fit
	for x in pop_fit[:n]:
		best_pop.append(pop_dict[x])
	return best_pop

def crossover(best_pop):
	global n
	x =0
	child_pop=[]
	while x<n:
		father = best_pop[x]
		mother = best_pop[x+1]
		x = x+2
		child1 = father[:5] + mother[5:]
		child2 = father[5:] + mother[:5]
		child_pop.append(child1)
		child_pop.append(child2)
	return child_pop

n = 50
population = initialization()
pop_size = 10
goal = [1,1,1,1,1,1,1,1]
print "Inital population:\n",population
for generation in range(10):
	print "Generation", generation+1
	pop_fit = fitness(population)
	print "fitness:\n",  pop_fit
	pop_dict = make_dic(population,pop_fit)
	#print "\nDict of Pop:\n", pop_dict
	best_pop = best_individual(pop_fit,pop_dict)
	if best_pop[0]==goal:
		print "Goal State is received after %d generation:%r" %(generation, best_pop[0])
		break
	#print "\nBest Pop:\n",best_pop
	population = crossover(best_pop)
	#print "\nChild population after crossover:\n", population


'''
pop_fit = fitness(population,10)
print "fitness:\n",  pop_fit
pop_dict = make_dic(population,pop_fit)
print "\nDict of Pop:\n", pop_dict
best_pop = best_individual(pop_fit,pop_dict)
print "\nBest Pop:\n",best_pop
child_pop = crossover(best_pop)
print "\nChild population after crossover:\n", child_pop
'''

