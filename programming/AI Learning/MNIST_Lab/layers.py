import numpy as np

class Relu:

    def forward(self,x):
        self.mask = (x<=0)
        out = x.copy()
        out[self.mask]=0
        return out

    def backward(self,dout):
        dout[self.mask]=0
        return dout


class Affine:

    def __init__(self,W,b):
        self.W=W
        self.b=b

    def forward(self,x):
        self.x=x
        return np.dot(x,self.W)+self.b

    def backward(self,dout):

        dx = np.dot(dout,self.W.T)
        self.dW = np.dot(self.x.T,dout)
        self.db = np.sum(dout,axis=0)

        return dx


class SoftmaxWithLoss:

    def forward(self,x,t):

        self.t=t

        exp_x = np.exp(x-np.max(x,axis=1,keepdims=True))
        self.y = exp_x/np.sum(exp_x,axis=1,keepdims=True)

        batch_size = x.shape[0]

        loss = -np.sum(np.log(self.y[np.arange(batch_size),t]+1e-7))/batch_size

        return loss

    def backward(self,dout=1):

        batch_size = self.t.shape[0]

        dx = self.y.copy()
        dx[np.arange(batch_size),self.t] -=1
        dx = dx/batch_size

        return dx