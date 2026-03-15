from sklearn.datasets import fetch_openml
import numpy as np

def load_mnist():
    # Adding as_frame=False forces the download to be a NumPy array
    mnist = fetch_openml('mnist_784', version=1, as_frame=False)

    X = mnist.data.astype(np.float32) / 255.0
    y = mnist.target.astype(np.int64)

    x_train = X[:60000]
    t_train = y[:60000]

    x_test = X[60000:]
    t_test = y[60000:]

    return (x_train, t_train), (x_test, t_test)