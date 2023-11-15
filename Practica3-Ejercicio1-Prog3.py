import constraint as csp
import time

# Ejercicio 1.2
'''def n_queens(n):
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

print('set solver: ',reinas.setSolver(solver)) # objeto
print(reinas.getSolution()) #{1: 8, 2: 8, 3: 8, 4: 8, 5: 8, 6: 8, 7: 8, 8: 8}

print(reinas)'''

def n_queens2(n):
    
    variables = range(1, n+1)
    dominio = range(1,n+1)
    reinas = csp.Problem()
    #reinas = csp.Problem(csp.BacktrackingSolver)

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
reinas_obj = n_queens2(100) 
# Medición de tiempo
start = time.time()
solver = csp.BacktrackingSolver(reinas_obj)

# set solver: es un método utilizado para establecer el solucionador 
# que se utilizará para resolver un problema de restricción.
reinas_obj.setSolver(solver)

#soluciones = reinas_obj.getSolutions() # devuelve una lista de diccionarios
unica_sol = reinas_obj.getSolution()
print(unica_sol)
end = time.time()
print("Tiempo total: ", end-start)

#print(soluciones)

# El tiempo de ejecución con 8 reinas es de : Tiempo total:  0.04182076454162598 segundos
# Al aumentar el número de reinas tarda mas ya que el espacio de estados aumenta exponencialmente. 
# Por ejemplo: para 12 reinas tarda 14.34572982788086 segundos

# Ejercicio 1.4}
# Repita el ejercicio anterior, esta vez encontrando una única solución.
# Qué sucede con el tiempo al aumentar el número de reinas? ¿Por qué cree que sucede esto?
# Respuesta:
# Encontrando una única solución tarda 0.0 sgundos y al aumentar el número de reinas funciona rápido.
# Ejemplo: con 100 reinas tarda  0.36558961868286133 segundos.
# Creemos que esto puede suceder por el algoritmo DFS no garantiza optimalidad pero es el 
# más rápido en encontrar una solución. --> PREGUNTAR.
