from itertools import product, permutations

def f(x1,x2,x3,x4,x5):
    return (x1 or (x1 and x2 or x2 and x3) or (x1 and x3 and x4 or x2 and x4 and x5) or 
                  x1 and x2 and x3 and x5 or x2 and x3 and x4 and x5)

res = {}
for p in permutations(range(5)):
    func = tuple(f(*[v[p_i] for p_i in p]) for v in product([True, False], repeat=5))
    res.setdefault(func, []).append(p)

original = tuple(f(*v) for v in product([True, False], repeat=5))
res[original]
