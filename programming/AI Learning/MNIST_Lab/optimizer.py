import numpy as np

class SGD:

    def __init__(self,lr=0.01):
        self.lr = lr

    def update(self,params,grads):

        for key in params.keys():
            params[key] -= self.lr * grads[key]


class Momentum:

    def __init__(self,lr=0.01,momentum=0.9):

        self.lr = lr
        self.momentum = momentum
        self.v = None

    def update(self,params,grads):

        if self.v is None:
            self.v={}
            for key,val in params.items():
                self.v[key]=np.zeros_like(val)

        for key in params.keys():
            self.v[key]=self.momentum*self.v[key]-self.lr*grads[key]
            params[key]+=self.v[key]


class AdaGrad:

    def __init__(self,lr=0.01):

        self.lr=lr
        self.h=None

    def update(self,params,grads):

        if self.h is None:
            self.h={}
            for key,val in params.items():
                self.h[key]=np.zeros_like(val)

        for key in params.keys():

            self.h[key]+=grads[key]*grads[key]

            params[key]-=self.lr*grads[key]/(np.sqrt(self.h[key])+1e-7)


class Adam:

    def __init__(self,lr=0.001):

        self.lr=lr
        self.m=None
        self.v=None
        self.beta1=0.9
        self.beta2=0.999
        self.iter=0

    def update(self,params,grads):

        if self.m is None:

            self.m={}
            self.v={}

            for key,val in params.items():
                self.m[key]=np.zeros_like(val)
                self.v[key]=np.zeros_like(val)

        self.iter+=1

        for key in params.keys():

            self.m[key]=self.beta1*self.m[key]+(1-self.beta1)*grads[key]
            self.v[key]=self.beta2*self.v[key]+(1-self.beta2)*(grads[key]**2)

            m_hat=self.m[key]/(1-self.beta1**self.iter)
            v_hat=self.v[key]/(1-self.beta2**self.iter)

            params[key]-=self.lr*m_hat/(np.sqrt(v_hat)+1e-7)