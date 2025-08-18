from scipy.optimize import minimize

def eqn(x):
  return x**2 + x + 2


#three arguments are required: the function to minimize, the initial guess, and the method
mymin = minimize(eqn, 0, method='BFGS') 

print(mymin) # Output the optimization result
print(mymin.x) # Output the minimum point found