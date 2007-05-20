"""
The DisasterSampler example.

"""
from numpy.testing import *
from pylab import *
PLOT=False

class test_Sampler(NumpyTestCase):
    def check(self):
        from PyMC2 import Sampler
        from PyMC2.examples import DisasterModel
        M = Sampler(DisasterModel)
        M.sample(5000,0,10)
        if PLOT:
            # It would be nicer to write plot(M.trace(switchpoint)), since switchpoint is local to M.
            plot(M.s.trace())
            title('switchpoint')
            figure()
            plot(M.e.trace())
            title('early mean')            
            figure()
            title('late mean')
            plot(M.l.trace())
            show()

if __name__ == '__main__':
    NumpyTest().run()
    
