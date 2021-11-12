import math
import pandas as pd
import numpy as np
import statsmodels.api as sm
from statsmodels.base.model import GenericLikelihoodModel
from scipy.stats import poisson
from scipy.stats import binom
from patsy import dmatrices
import statsmodels.graphics.tsaplots as tsa
from matplotlib import pyplot as plt


class INAR(GenericLikelihoodModel):
    def __init__(self, endog, exog, **kwds):
        super(INAR, self).__init__(endog, exog, **kwds)
        
        
        
class PoissonINAR(GenericLikelihoodModel):
    def __init__(self, endog, exog, **kwds):
        super(INAR, self).__init__(endog, exog, **kwds)

    def nloglikeobs(self, params):
        #Fetch the parameters gamma and beta 
        #that we would be optimizing
        gamma = params[-1]
        beta = params[:-1]
        
        #Set y and X
        y = self.endog
        y = np.array(y)
        X = self.exog
        
        #Compute rho as a function of gamma
        rho = 1.0/(1.0+math.exp(-gamma))
        
        #Compute the Poisson mean mu as a dot 
        #product of X and Beta
        mu = np.exp(X.dot(beta))

        #Init the list of log-likelihhod values, 
        #one value for each y
        ll = []

        #Compute all the log-likelihood values for 
        #the Poisson INAR(1) model
        for t in range(len(y)-1,0,-1):
            prob_y_t = 0
            for j in range(int(min(y[t], y[t-1])+1)):
                prob_y_t += poisson.pmf((y[t]-j), mu[t]) *  
                            binom.pmf(j, y[t-1], rho)
            ll.append(math.log(prob_y_t))
        ll = np.array(ll)
        #return the negated array of log-likelihoods
        return -ll
      
 def fit(self, start_params=None, maxiter=1000, maxfun=5000, **kwds):
    #Add the gamma parameter to the list of 
    #exogneous variables that the model will optimize
    self.exog_names.append('gamma')
    if start_params == None:
        #Start with some initial values of Beta and gamma
        start_params = np.append(np.ones(self.exog.shape[1]), 1.0)
#Call super.fit() to start the training
    return super(PoissonINAR, self).fit(start_params=start_params,
               maxiter=maxiter, maxfun=maxfun, **kwds)   
               
               
               
               
      
      
      
      
      
