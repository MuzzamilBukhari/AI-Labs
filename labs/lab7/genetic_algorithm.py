import operator
import math
import random
import numpy as np

from deap import base, creator, gp, tools, algorithms

# Step 1: Define target function
def target_function(x):
    return 5 * x**3 - 6 * x**2 + 8 * x

# Step 2: Generate training data
x_vals = [x / 10.0 for x in range(-100, 101)]
y_vals = [target_function(x) for x in x_vals]

# Step 3: Create primitive set
pset = gp.PrimitiveSet("MAIN", 1)
pset.addPrimitive(operator.add, 2)
pset.addPrimitive(operator.sub, 2)
pset.addPrimitive(operator.mul, 2)
pset.addPrimitive(operator.neg, 1)
pset.addEphemeralConstant("rand101", lambda: random.uniform(-10, 10))
pset.renameArguments(ARG0='x')

# Step 4: Define fitness and individual
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", gp.PrimitiveTree, fitness=creator.FitnessMin)

# Step 5: Register toolbox methods
toolbox = base.Toolbox()
toolbox.register("expr", gp.genHalfAndHalf, pset=pset, min_=1, max_=3)
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.expr)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)
toolbox.register("compile", gp.compile, pset=pset)

def evalSymbReg(individual):
    func = toolbox.compile(expr=individual)
    sqerrors = ((func(x) - y) ** 2 for x, y in zip(x_vals, y_vals))
    return math.sqrt(sum(sqerrors) / len(x_vals)),

toolbox.register("evaluate", evalSymbReg)
toolbox.register("select", tools.selTournament, tournsize=3)
toolbox.register("mate", gp.cxOnePoint)
toolbox.register("mutate", gp.mutUniform, expr=toolbox.expr, pset=pset)

toolbox.decorate("mate", gp.staticLimit(key=len, max_value=17))
toolbox.decorate("mutate", gp.staticLimit(key=len, max_value=17))

# Step 6: Run evolution
random.seed(42)
population = toolbox.population(n=300)
hof = tools.HallOfFame(1)

stats = tools.Statistics(lambda ind: ind.fitness.values)
stats.register("avg", np.mean)
stats.register("std", np.std)
stats.register("min", np.min)
stats.register("max", np.max)

print("Evolution process starts")
population, log = algorithms.eaSimple(
    population, toolbox, 0.5, 0.2, 10, stats=stats, halloffame=hof, verbose=True
)
print("- Evolution ends")

# Step 7: Output best solution
best_ind = tools.selBest(population, 1)[0]
print("\nBest individual:")
print(best_ind)

# Evaluate number of ones in a 0/1 list representation (optional adaptation)
def count_ones(individual):
    try:
        return sum(1 for val in individual if val == 1)
    except:
        return "N/A"

print("\nNumber of ones:", count_ones(best_ind))

# Step 8: (Optional) Plot result
try:
    import matplotlib.pyplot as plt
    compiled_func = toolbox.compile(expr=best_ind)
    predicted = [compiled_func(x) for x in x_vals]

    plt.plot(x_vals, y_vals, label="Target Function")
    plt.plot(x_vals, predicted, label="GP Approximation")
    plt.legend()
    plt.title("Symbolic Regression using Genetic Programming")
    plt.show()
except ImportError:
    print("matplotlib not installed. Skipping plot.")