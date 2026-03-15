import numpy as np
from collections import OrderedDict
from layers import Affine, Relu, SoftmaxWithLoss

class MultiLayerNet:

    def __init__(self, input_size, hidden_size_list, output_size):

        self.params = {}

        layer_sizes = [input_size] + hidden_size_list + [output_size]

        for i in range(1,len(layer_sizes)):

            self.params['W'+str(i)] = 0.01*np.random.randn(layer_sizes[i-1],layer_sizes[i])
            self.params['b'+str(i)] = np.zeros(layer_sizes[i])

        self.layers = OrderedDict()

        for i in range(1,len(layer_sizes)-1):

            self.layers['Affine'+str(i)] = Affine(self.params['W'+str(i)],self.params['b'+str(i)])
            self.layers['Relu'+str(i)] = Relu()

        last = len(layer_sizes)-1
        self.layers['Affine'+str(last)] = Affine(self.params['W'+str(last)],self.params['b'+str(last)])

        self.last_layer = SoftmaxWithLoss()

    def predict(self,x):

        for layer in self.layers.values():
            x = layer.forward(x)

        return x

    def loss(self,x,t):

        y = self.predict(x)
        return self.last_layer.forward(y,t)

    def accuracy(self,x,t):

        y = self.predict(x)
        y = np.argmax(y,axis=1)

        if t.ndim != 1:
            t = np.argmax(t,axis=1)

        return np.sum(y==t)/float(x.shape[0])

    def gradient(self,x,t):

        self.loss(x,t)

        dout = 1
        dout = self.last_layer.backward(dout)

        layers = list(self.layers.values())
        layers.reverse()

        for layer in layers:
            dout = layer.backward(dout)

        grads = {}

        for i in range(1, len(self.params)//2 +1):
            grads['W'+str(i)] = self.layers['Affine'+str(i)].dW
            grads['b'+str(i)] = self.layers['Affine'+str(i)].db

        return grads