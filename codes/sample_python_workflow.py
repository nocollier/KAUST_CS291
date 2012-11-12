import numpy as np
import pylab as plt
import pickle
import os,sys

def YourCodeHere(N):
    A = np.random.rand(N,N)
    F = np.random.rand(N)
    return np.linalg.solve(A,F)

fname = 'data.pkl'
try:
    fname = sys.argv[1]
except:
    None
    
# Part I: Run the numeric examples
if os.path.exists(fname) == False:
    f = open(fname,'wb')
    for i in range(10):
        print "Running code..."
        pickle.dump(YourCodeHere(4),f)
    f.close()

# Part II: Plot the results
f = open(fname,'rb')
i = 0
while True:
    try:
        x = pickle.load(f)
        if i % 2 == 0:
            plt.subplot(121)
            plt.plot(x,'--or')
        else:
            plt.subplot(122)
            plt.plot(x,'--ob')
        i += 1
    except:
        break
        
plt.savefig("myfig.pdf")
plt.show()
