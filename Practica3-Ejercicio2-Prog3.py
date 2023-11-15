## Ejercicio 2. Sudoku
'''
El objetivo es completar los espacios en blanco de la grilla con números del 1 al 9, 
respetando las siguientes restricciones:

* No se pueden repetir números en cada fila.
* No se pueden repetir números en cada columna.
* No se pueden repetir números en cada caja (grilla 3x3 delimitada por las líneas en trazo grueso).



##### Ejercicio 2.1

Escribir en papel este problema como un CSP.

variables:  Fi = X
           {Fi,...,Fn}  ∀ 1 ≤ F,i ≤ 9 (F= fila, i=columna)

dominio: {1,....,9} ∀Fi 
         {1,...,9} para toda casilla perteneciente al rango Fi comprendido:
         entre {9,...,1} para F 
         y {9,...,1} para i

restricciones:
* No se pueden repetir números en cada fila.
* No se pueden repetir números en cada columna.

1) y 2)
    ((F1i,F2j), i ≠ j U F1 ≠ F2)     ∀1 ≤ i, j,F1,F2 ≤ n
    ((F1i,F2j,X,Y), i ≠ j U F1 ≠ F2 U X = Y 
                    OR 
                    i = j OR F1 = F2 U X ≠ Y)     ∀ 1 ≤ i, j, F1,F2, X,Y ≤ 9
    
3) * No se pueden repetir números en cada caja (grilla 3x3 delimitada por las líneas en trazo grueso).

X,Y --> No tiene que ser iguales en una caja 3x3

Cajas = 9 (1-3, 4-6, 7-9) ∀ F y i

((F1i,F2j,X,Y), X ≠ Y U ------------> PREGUNTAR COMO RESTRINGIR LOS BLOQUES 3X3. SEGMENTAR? VA EN EL DOMINIO?


##### Ejercicio 2.2

Escribir un programa que resuelva este Sudoku usando <code>python-constraint</code>.

**Ayuda.** Si el nombre de las variables son números de dos dígitos, 
donde la decena indica el número de fila y la unidad el número de columna, 
entonces los dominios de las variables ya fijadas están dadas 
por el siguiente diccionario:'''

import constraint as csp

variables_fijadas = {13:4, 14:7, 15:5, 19:3,
                     26:8, 27:4,
                     35:6, 38:7, 39:5,
                     41:6, 42:3, 47:5,
                     52:8, 58:6,
                     63:5, 68:9, 69:1,
                     71:8, 72:4, 75:3,
                     83:9, 84:8,
                     91:3, 95:9, 96:7, 97:1}

sudoku = csp.Problem()
# Completar
# ...

def sudoku():
    variables_fijadas = {13:4, 14:7, 15:5, 19:3,
                     26:8, 27:4,
                     35:6, 38:7, 39:5,
                     41:6, 42:3, 47:5,
                     52:8, 58:6,
                     63:5, 68:9, 69:1,
                     71:8, 72:4, 75:3,
                     83:9, 84:8,
                     91:3, 95:9, 96:7, 97:1}


    variables = range(1, 10)
    dominio = range(1,10)
    sudoku = csp.Problem()
    #reinas = csp.Problem(csp.BacktrackingSolver)

    for x in variables:
        sudoku.addVariable(x,dominio)

    # Restricción de diagonal
    for i in range(1,10):
        for j in range(1,10):
            # posicion = ij
            for x in range(1,10):
                sudoku.addConstraint(csp.FunctionConstraint(lambda i,j: i != j),variables)

            # reinas.addConstraint(csp.FunctionConstraint(lambda x, y: x != y),
            #                      [variables[i], variables[j]])

    return sudoku

# Testear si la definición de la función es correcta
reinas_obj = sudoku() 
# Medición de tiempo
# start = time.time()
solver = csp.BacktrackingSolver(reinas_obj)

# set solver: es un método utilizado para establecer el solucionador 
# que se utilizará para resolver un problema de restricción.
reinas_obj.setSolver(solver)

#soluciones = reinas_obj.getSolutions() # devuelve una lista de diccionarios
unica_sol = reinas_obj.getSolution()
# print(unica_sol)
# end = time.time()
# print("Tiempo total: ", end-start)
