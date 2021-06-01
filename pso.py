
# parametros
w = 0.70
c1 = 0.20
c2 = 0.60
r1 = 0.4657
r2 = 0.5319
n = 5
iterations = 10
#f(x) = 1 + 2x - x*x

#vetor inicial
X = [0.4657, 0.8956, 0.3877, 0.4902, 0.5039]
V = [0.5319, 0.8185, 0.8331, 0.7677, 0.1708]

gbest = 0
gbf = 0

#randomizacao opicional
for j in range(n):
    X[j] = X[j] - 0.5
    X[j] = X[j] * 10
    X[j] = round(X[j],4)
    V[j] = V[j] - 0.5
    V[j] = round(V[j],4)
    result = 1 + 2*X[j] - pow(X[j],2)
    result = round(result,4)
    if(result > gbf):
        gbest = X[j]
        gbf = result

pbest = X

print("iteracao 01:")
print(f'Local best position (pbest) = {pbest}')
print(f'Global best fitness = {gbf}')
print(f'Global best position (gbest) = {gbest}')
print()

#funcao para maximizar f(x) = 1 + 2x - x^2
for i in range(iterations-1):
    for j in range(n):
        V[j] = (w*V[j]) + (c1*r1*(pbest[j] - X[j])) + (c2*r2*(gbest - X[j]))     # calcula o valor de v[i+1]   
        V[j] = round(V[j],4)
        X[j] = X[j] + V[j]                                                       # calcula o valor de x[i+1]
        X[j] = round(X[j],4)
        if(X[j] > pbest[j]):                                                     # verifica se x[i+1] é um local best position
            pbest[j] = X[j]

    for j in range(n):
        result = 1 + 2*X[j] - pow(X[j],2)                                        # calcula a funcao de fitness
        result = round(result,4)
        if(result > gbf):                                                        # verifica se result é um global best fitness
            gbest = X[j]                                            
            gbf = result

    print(f"iteracao 0{i+2}:")
    print(f'Local best position (pbest) = {pbest}')
    print(f'Global best fitness = {gbf}')
    print(f'Global best position (gbest) = {gbest}')
    print()
