
def negation(p):
    # returns the opposite truth value for p (i.e. not(p))
    return not(p)

def conjunction(p, q):
    # return the AND value i.e. p∧q
    return (p and q)

def orLogic(p, q):
    return(p or q)

def implication(p, q):
        return (not p) or q

def biconditional(p, q):
    return p==q

#""" Displaying negation results"""
print("p     not(p)")
print("------------")
for p in [True, False]:
    notp = negation(p)
    print(p,notp)
print()

#display or result
print("p     q     pvq")
print("---------------")
for p in [True, False]:
    for q in [True, False]:
        pNq = orLogic(p, q)
        print(p,q,pNq)
print()

#diplay and result
print("p     q     p∧q")
print("---------------")
for p in [True, False]:
    for q in [True, False]:
        pNq = conjunction(p, q)
        print(p,q,pNq)
print()

#diplay implication result
print("p     q     p->q")
print("---------------")
for p in [True, False]:
    for q in [True, False]:
        pNq = implication(p, q)
        print(p,q,pNq)
print()

#display bi-conditional result
print("p     q     p<->q")
print("---------------")
for p in [True, False]:
    for q in [True, False]:
        pNq = biconditional(p, q)
        print(p,q,pNq)
print()
