# pso_and_aco_algorithms
PSO and ACO algorithms (made for AI course)

## PSO:

pso.py gets multiple parameters in order to maximize a specific function (in this case is f(x) = 1 + 2x + x^2)

I use V(i+1) = (w * V(i)) + (c1 * r1 * (pbest - X(i))) + (c2 * r2 * (gbest - X(i))) for calculating the current speed and X(i+1) = X(i) + V(i+1)

## where:

  w = weight
  
  V(x) = particles speed (vector)
  
  X(x) = particles position (vector)
  
  c1, c2, r1, r2 = predetermined constants
  
  pbest = local best position (vector)
  
  gbest = global best position
  
  gbf = global best fitness of function


## ACO:

aco.py gets an NxN "fully-connected" matrix and find the best path, with its probs.
