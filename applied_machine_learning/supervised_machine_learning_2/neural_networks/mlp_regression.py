import numpy as np
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPRegressor
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split

# Sample regression problem with one input variable
X_R1, y_R1 = make_regression(n_samples = 100, n_features=1,
                             n_informative=1, bias = 150.0,
                             noise = 30, random_state=0)
X_train, X_test, y_train, y_test = train_test_split(X_R1[0::5],y_R1[0::5], random_state=0)
X_input = np.linspace(-3, 3, 50).reshape(-1, 1)
fig, subaxes = plt.subplots(2, 3, figsize=(11, 8), dpi=80)
for thisaxisrow, thisactivation in zip(subaxes, ['tanh', 'relu']):
    for thisalpha, thisaxis in zip([0.0001, 1.0, 100], thisaxisrow):
        mlpreg = MLPRegressor(hidden_layer_sizes=[10, 10],
                              activation=thisactivation,
                              alpha=thisalpha,
                              solver='lbfgs',
                              max_iter=10000).fit(X_train, y_train)

        y_predict_output = mlpreg.predict(X_input)

        thisaxis.set_xlim([-2.5, 0.75])
        thisaxis.plot(X_input, y_predict_output, '^', markersize=10)
        thisaxis.plot(X_train, y_train, 'o')
        thisaxis.set_xlabel('Input feature')
        thisaxis.set_ylabel('Target value')
        thisaxis.set_title('MLP regression\nalpha={}, activation={}'.format(thisalpha, thisactivation))
        plt.tight_layout()
plt.show()
