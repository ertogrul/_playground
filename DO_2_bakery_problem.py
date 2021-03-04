import cplex 

# create an instance of a linear problem to solve
problem = cplex.Cplex()

# set maximum in objective function
problem.objective.set_sense(problem.objective.sense.maximize)

# set decision variables
names = ["torte", "pie"]

# set coefficients of the objective function.
# note that we are casting to floats.
objective = [3.0, 5.0]

# lower bounds.
# all zeroes is the default.
lower_bounds = [0.0, 0.0]

# upper bounds. 
# cplex.infinity, or 1e+20 is the default.
upper_bounds = [40.0, 30.0]    #  SHOULD I PUT DEMAND LIMITS AS UPPER BONDS? RATHER YES.<------------

problem.variables.add(obj = objective,
                      lb = lower_bounds,
                      ub = upper_bounds,
                      names = names)

# Constraints

# Constraints are entered as two parts of equations. In our case, we have:
# 2x + 3y <= 100
# 1x + 2y <= 60
# 1x + 1y <= 50
# 2x + 3y <= 100


# First, we name the constraints
constraint_names = ["c1", "c2", "c3", "c4"]

# The actual constraints are now added. Each constraint is actually a list
# consisting of two objects, each of which are themselves lists. The first list
# represents each of the variables in the constraint, and the second list is the
# coefficient of the respective variable. Data is entered in this way as the
# constraints matrix is often sparse.

# Constraints
con_1 = [["torte", "pie"], [2.0, 3.0]]
con_2 = [["torte", "pie"], [1.0, 2.0]]
con_3 = [["torte", "pie"], [1.0, 1.0]]
# con_4 = [["torte", "pie"], [40.0, 30.0]] - THIS WAS DEMAND BUT IT DOES NOT FIT HERE.<-----------------------
con_4 = [["torte", "pie"], [1.0, 1.0]]

constraints = [con_1,con_2,con_3,con_4]

# Right side of constraint equations:
rhs = [100.0, 60.0, 50.0, 0.0]

# The sign for the contraint equation:
# ≤ is less then:    "L"
# ≥ is greater then: "G"
# = is equal to:     "E"
constraint_senses = [ "L", "L", "L", "G" ]

# Note that we can actually set senses as a string. That is, we could also use
#     constraint_senses = "LL"
# to pass in our constraints

# And add the constraints
problem.linear_constraints.add(lin_expr = constraints,
                               senses = constraint_senses,
                               rhs = rhs,
                               names = constraint_names)

# Solve the problem
problem.solve()

# And print the solutions
print(problem.solution.get_values())

# number of tortes and/or pies to eat  
best_conf = []
best_conf = problem.solution.get_values()
max_profit = problem.solution.get_objective_value()
# print('* * *')
# print()
# print("BAKERY SHOULD USE FOLLOWINF CONF: " + \
#     str(best_conf[0]) + " HOURS FOR APPLE PREPARATION " + \
#     str(best_conf[1]) + " PIES TO GET MAXIMUM OF " + \
#     str(max_points) + " POINTS.")
# print()
# print('* * *')
