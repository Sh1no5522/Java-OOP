import numpy as np
import matplotlib.pyplot as plt
from load_mnist import load_mnist
from multi_layer_net import MultiLayerNet
from optimizer import SGD, Momentum, AdaGrad, Adam

(x_train, t_train), (x_test, t_test) = load_mnist()

train_size = x_train.shape[0]
batch_size = 128
max_iterations = 1000

optimizers = {}
optimizers['SGD'] = SGD(lr=0.1)
optimizers['Momentum'] = Momentum(lr=0.01)
optimizers['AdaGrad'] = AdaGrad(lr=0.01)
optimizers['Adam'] = Adam(lr=0.001)

networks = {}
train_loss = {}

for key in optimizers.keys():
    networks[key] = MultiLayerNet(
        input_size=784,
        hidden_size_list=[50,50,50],
        output_size=10
    )
    train_loss[key] = []

for i in range(max_iterations):

    batch_mask = np.random.choice(train_size, batch_size)

    x_batch = x_train[batch_mask]
    t_batch = t_train[batch_mask]

    for key in optimizers.keys():

        grads = networks[key].gradient(x_batch, t_batch)

        optimizers[key].update(networks[key].params, grads)

        loss = networks[key].loss(x_batch, t_batch)

        train_loss[key].append(loss)

    if i % 100 == 0:

        print("iteration:", i)

        for key in optimizers.keys():

            loss = networks[key].loss(x_batch, t_batch)

            train_acc = networks[key].accuracy(x_train[:1000], t_train[:1000])
            test_acc = networks[key].accuracy(x_test[:1000], t_test[:1000])

            print(key, "loss:", loss)
            print("train acc:", train_acc)
            print("test acc:", test_acc)

markers = {"SGD":"o","Momentum":"x","AdaGrad":"s","Adam":"D"}

x = np.arange(max_iterations)

for key in optimizers.keys():

    plt.plot(x, train_loss[key], label=key)

plt.xlabel("iterations")
plt.ylabel("loss")
plt.legend()
plt.show()