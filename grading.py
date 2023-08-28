import numpy as np
problems = {}
random_square_complex = lambda       : np.random.uniform(-1,1) + 1j * np.random.uniform(-1,1)
multiply_generators   = lambda n,f,l: multiply_generators(n-1,f,[f()]+l) if n else tuple(l)
l2_norm               = lambda z1,z2 : np.abs(z1-z2) < 1E-3

''' HW2: P1'''
problems["hw2_p1"] ={"generator" : random_square_complex,
                     "solution"  : lambda z : 1/z,
                     "checker"   : l2_norm }


''' HW2: P2 '''
problems["hw2_p2"] ={"generator" : lambda  : multiply_generators(3,random_square_complex,[]),
                     "solution"  : lambda a,b,c : np.array((-b+np.sqrt(b**2-4*a*c))/(2*a),(-b-np.sqrt(b**2-4*a*c))/(2*a)),
                    "checker" : lambda rroots,sroots : np.sum(l2_norm(sroots,rroots)) }

def grade(problem,function,ntries=20):
    correct = 0
    for i in range(ntries):
        z = problems[problem]["generator"]()
        ssol = function(*z)
        rsol = problems[problem]["solution"](*z)
        if (problems[problem]["checker"](ssol,rsol)):
            correct += 1
    print(("Correct!" if correct==ntries else "Incorrect!"))
    print("({}/{}) Test cases passed".format(correct,ntries))