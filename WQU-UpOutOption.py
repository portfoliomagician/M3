import scipy as sp
import numpy as np
from scipy import log,exp,sqrt,stats

s0=100             # Stock price today
x=100              # Strike price
barrier=150         # Barrier level
T=1             # Maturity in years
r=0.08              # Risk-free rate
sigma=0.3        # Annualized volatility
n_simulation = 1000  # number of simulations

def bs_call(S,X,T,r,sigma):   
    d1=(log(S/X)+(r+sigma*sigma/2)*T)/(sigma*sqrt(T))
    d2=d1-sigma*sqrt(T)
    return S*stats.norm.cdf(d1)-X*exp(-r*T)*stats.norm.cdf(d2)

def up_and_out_call(s0,x,T,r,sigma,n_simulation,barrier):
    """Returns: Call value of an up-and-out barrier option with European call
    """
    n_steps= 12 # Define number of steps.
    dt = T/n_steps
    total=0
    for j in range(0,n_simulation):
        sT=s0
        out=False
        for i in range(0,int(n_steps)):
            e= sp.random.normal()
            sT*=sp.exp((r-0.5*sigma**2)*dt+sigma*e*sp.sqrt(dt))
            if sT>barrier:
                out=True
        if out==False:
            total+=bs_call(s0,x,T,r,sigma)
    return total/n_simulation

result = up_and_out_call (s0,x,T,r,sigma,n_simulation,barrier)
print('Price for the Up-and-out Call = ', result)