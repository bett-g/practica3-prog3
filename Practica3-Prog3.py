import constraint as csp

def n_queens(n):
    variables = range(1, n+1)
    print(variables)
    dominio = range(1,n+1)
    reinas = csp.Problem()

    for v in variables:
        reinas.addVariable(v,dominio)

    # Restricción de diagonal
    for i in range(n-1):
        for j in range(i+1,n):
            reinas.addConstraint(csp.FunctionConstraint(lambda x, y, w=i, z=j: abs(x-y) != z-w), 
                                 [variables[i], variables[j]])
            reinas.addConstraint(csp.FunctionConstraint(lambda x, y: x != y),
                                 [variables[i], variables[j]])
    return reinas

# Testear si la definición de la función es correcta
reinas = n_queens(8) 
solver = csp.BacktrackingSolver()
print('solver: ',solver)
print('set solver: ',reinas.setSolver(solver)) # objeto
print(reinas.getSolution()) #{1: 8, 2: 8, 3: 8, 4: 8, 5: 8, 6: 8, 7: 8, 8: 8}
print('get solutions: ', reinas.getSolutions()) # devuelve una lista de diccionarios
print('getSolutionIter: ', reinas.getSolutionIter()) # objeto

print(reinas)


#import time

#start = time.time()
# Completar
# ...
#end = time.time()
#print("Tiempo total: ", end-start)

def n_queens2(n):
    variables = range(1, n+1)
    print(variables)
    dominio = range(1,n+1)
    problem = csp.Problem()
    reinas = problem(csp.BacktrackingSolver())
    

    for v in variables:
        reinas.addVariable(v,dominio)

    # Restricción de diagonal
    for i in range(n-1):
        for j in range(i+1,n):
            reinas.addConstraint(csp.FunctionConstraint(lambda x, y, w=i, z=j: abs(x-y) != z-w), 
                                 [variables[i], variables[j]])
            reinas.addConstraint(csp.FunctionConstraint(lambda x, y: x != y),
                                 [variables[i], variables[j]])
    return reinas

# Testear si la definición de la función es correcta
reinas = n_queens2(8) 
solver = csp.BacktrackingSolver(reinas)
print('solver: ',solver)
print('set solver: ',reinas.setSolver(solver)) # objeto
print(reinas.getSolution()) #{1: 8, 2: 8, 3: 8, 4: 8, 5: 8, 6: 8, 7: 8, 8: 8}
print('get solutions: ', reinas.getSolutions()) # devuelve una lista de diccionarios
print('getSolutionIter: ', reinas.getSolutionIter()) # objeto

print(reinas)
