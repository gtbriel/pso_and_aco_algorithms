def search(x,path):
    for k in range(len(path)):
        if(x == path[k][1]):
            return True
    return False

alpha = 1
beta = 1
rho = 0.5
tau = [[0,2,2,2,2],[2,0,2,2,2],[2,2,0,2,2],[2,2,2,0,2],[2,2,2,2,0]]
tau_init = 2

qlt = [[0,2,10,8,3],
       [1,0,2,5,7],
       [9,1,0,3,6],
       [10,4,3,0,2],
       [2,7,5,1,0]]

somatorios = []
probs = []

i = 4
path = [[1.0, i]]


def summ(index):
  sumx = 0          
  for j in range(len(qlt)):
    if (search(j, path)):
      continue
    if(qlt[i][j] == 0):
      continue
    sumx = round(sumx + ((alpha * tau[index][j]) * (beta * 1/qlt[index][j])), 4)
  return sumx

while len(path) < len(qlt):
    temp = []
    for j in range(len(qlt)):
        if qlt[i][j] == 0 or search(j, path):
          continue
        prob = round(((alpha * tau[i][j]) * (beta * 1/qlt[i][j])) / summ(i) , 2)
        temp.append([prob,j])        
    
    probs.append(temp)
    i = max(temp)[1]
    path.append(max(temp))

print(path)