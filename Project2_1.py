import numpy as np

with open('input.txt', 'r') as file:            #open input text file
    equations = file.read().splitlines()        #split the input file by line

constants = []                                  #initialize constants array and coeffs array
A = []

for i in range(len(equations)):                 #iterate through input file
    equations[i] = equations[i].replace(" ", "").replace("+", "")\
    .replace("=", "").replace("x", "$").replace("y", "$")\
    .replace("z", "$").replace("w", "$")        #replace each variable with $ and each mathematical operation with blank space
    if i == 0:                                  #if we're on the first line/equation
        eq1 = equations[i].split("$")           #split coefficients up by added $ symbols
        eq1 = [float(num) for num in eq1[:]]    #iterate through each coefficient
        constants.append(eq1[len(eq1) -1])      #add final value to constants
        eq1.pop()                               #remove final value (constant) from list
        A.append(eq1)                           #add first coefficient values to final array
    elif i ==1:                                 #else if we're on line two, do the same with second equation
        eq2 = equations[i].split("$")
        eq2 = [float(num) for num in eq2[:]]
        constants.append(eq2[len(eq2) -1])
        eq2.pop()
        A.append(eq2)
    elif i ==2:                                 #add third equation
        eq3 = equations[i].split("$")
        eq3 = [float(num) for num in eq3[:]]
        constants.append(eq3[len(eq3) -1])
        eq3.pop()
        A.append(eq3)
    elif i ==3:                                 #add fourth equation
        eq4 = equations[i].split("$")
        eq4 = [float(num) for num in eq4[:]]
        constants.append(eq4[len(eq4) -1])
        eq4.pop()
        A.append(eq4)

try:                                            #try to solve system
    A = np.array (A)                            #code from class
    A_Inverse = np.linalg.inv(A)
    sol = np.dot(A_Inverse , constants)
    print('x = ' + str(sol[0]))
    print('y = ' + str(sol[1]))
    print('z = ' + str(sol[2]))
    print('w = ' + str(sol[3]))
except:                                         #if there isnt one solution (LinAlgError)
    print('System does not have exactly one solution.')          #print error message
