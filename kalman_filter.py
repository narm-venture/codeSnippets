from math import *
def f(mu,sigma2,x):
    k=sqrt(2*pi*sigma2)
    k=1./k
    k1=((x-mu)**2)/sigma2
    f=k*exp(-0.5*k1)
    return f

def update(mean1,var1,mean2,var2):
    mean=(mean1*var2+mean2*var1)/(var1+var2)
    var=(var1*var2)/(var1+var2)
    return (mean,var)

def predict(mean1,var1,mean2,var2):
    mean=mean1+mean2
    var=var1+var2
    return (mean,var)

measurements=[5.,6.,7.,9.,10.]
motion=[1.,1.,2.,1.,1.]
measurement_sig=4.
motion_sig=2.
mu=0.
sig=1000.

for x in range(len(measurements)):
    mu,var=update(measurements[x],measurement_sig**2,mu,sig**2)
    sig=sqrt(var)
    print 'update: [',mu,' : ',sig,']'
    mu,var=predict(motion[x],motion_sig**2,mu,sig**2)
    sig=sqrt(var)
    print 'predict:[',mu,' : ',sig,']'
    
