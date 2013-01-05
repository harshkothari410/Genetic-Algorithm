#Next FUnction
#for Graph
from pylab import *
import random
import math

n = 0
max_pop = []
avg_pop = []

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
	global n,max_pop,avg_pop
	temp = 0
	for x in range(n):
		pop_fitind = 0
		weight = [128,64,32,16,8,4,2,1]
		j = 0
		for var in population[x]:
			pop_fitind = pop_fitind +  var*weight[j]
			j = j+ 1
		pop_fit.append(pop_fitind)
		temp = temp + pop_fitind
	#find average of population
	average = temp/n
	avg_pop.append(average)
	return pop_fit

def make_dic(population,pop_fit):
	return dict(zip(pop_fit,population))

def best_individual(pop_fit,pop_dict):
	global n,max_pop,avg_pop
	pop_fit.sort(reverse = True)
	max_pop.append(pop_fit[0])
	
	best_pop = []
	#n = n - 2
	print pop_fit
	for x in pop_fit[:n-1]:
		best_pop.append(pop_dict[x])
	best_pop.append(pop_dict[pop_fit[0]])
	return best_pop

def crossover(best_pop):
	global n
	x =0
	child_pop=[]
	while x<n:
		father = best_pop[x]
		mother = best_pop[x+1]
		x = x+2
		child1 = father[:4] + mother[4:]
		child2 = mother[:4] + father[4:]
		child_pop.append(child1)
		child_pop.append(child2)
		print "Father:",father
		print "mother:",mother
		print "child 1:",child1
		print "child 2:",child2
	return child_pop

#Mutation
def mutation(child_pop):
	y = random.randint(0,7)
	z = random.randint(0,3)
	bit = child_pop[z][y]
	print "\nChild:%d bit:%d"%(z,y)
	print "Child for Mutation:",child_pop[z]
	print "Bit to change:",bit
	if bit==1:
		child_pop[z][y] = 0
	else:
		child_pop[z][y] = 1
	print "After Mutation:",child_pop[z]
	return child_pop

n = 4
population = initialization()
pop_size = 10
gen_count = 0
flag = 0
goal = [1,1,1,1,1,1,1,1]
print "Inital population:\n",population
while 1:
	gen_count = gen_count +1
	print "----------"
	print "Generation:", gen_count+1
	pop_fit = fitness(population)
	#print "fitness:\n", pop_fit
	
	pop_dict = make_dic(population,pop_fit)
	#print "\nDict of Pop:\n", pop_dict
	best_pop = best_individual(pop_fit,pop_dict)
	
	
	if best_pop[0]==goal:
		print "Goal State is received after %d generation:%r" %(gen_count, best_pop[0])
		flag = 1
		data = gen_count
		break

	
	print "\nBest Pop:\n",best_pop
	child_pop = crossover(best_pop)
	#population = child_pop
	population = mutation(child_pop)
	#print "\nChild population after crossover:\n", population

print "Maximum Fitness:",max_pop
print "AVerage FItenss:",avg_pop
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

'''
Drawing Plot
'''
x=arange(1,gen_count+1,1)
y=max_pop
z =avg_pop
print x
print y

plot(x,y, 'k',color="red" ,linewidth=2.5 ,label="Max",lw=300)
plot(x,y, 'ro',color="red" ,linewidth=2.5 ,label="Max")
plot(x,z,'bo',color="blue",linewidth=2.5 ,label="Avg")
plot(x,z,'k',color="blue",linewidth=2.5 ,label="Avg")
if flag ==1:
	annotate("Goal State",xy=(data, max_pop[data-1]),xytext=(data-1,max_pop[data-1]+20),arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
	print "I am in annotate"
xlabel('Generation')
ylabel('Best Gene')
title('Genetic Algorithm')
plt.ylim(avg_pop[0]+20,300)

show()