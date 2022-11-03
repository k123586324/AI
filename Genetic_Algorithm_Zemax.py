import random
import pyzdde.zdde as pyz

ln = pyz.createLink()
ln.apr = True
def foo(x):
    ln.zSetSurfaceData(surfNum=2, code=ln.SDAT_THICK, value=x)
    value = ln.zGetOperand(1, 10)
    return value


def fitness(x):
    ans = foo(x)
    error=8.653732854633850E-001-ans
    return error

# 基因定序
solutions = []
for s in range(100):
    solutions.append(random.uniform(0, 1000))

for i in range(1000):
    rankedsolutions = []
    for s in solutions:
        rankedsolutions.append((fitness(s), s))
        #print(f'{fitness(s),s}')
    rankedsolutions.sort()
    #rankedsolutions.reverse()

    print(f'=== Gen {i} best solutions ===')
    print(rankedsolutions[0])
    if rankedsolutions[0][0] < 0.001:
        ln.zSetSurfaceData(surfNum=2, code=ln.SDAT_THICK, value=rankedsolutions[0][1])
        break
    bestsolutions = rankedsolutions[:100]
    elements = []
    for s in bestsolutions:
        elements.append(s[1])
    newGen = []
    for _ in range(1000):
        e1 = random.choice(elements) * random.uniform(0.99, 1.01)#突變率
        newGen.append(e1)
    solutions = newGen

ln.close()
exit(0)
