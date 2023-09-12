# python3 -m pip install theano
# python3 -m pip uninstall numpy
# python3 -m pip install numpy==1.23
import numpy as np
import theano.tensor as T
import theano as th
import operator
# th.config.openmp_elemwise_minsize = 1000
# th.config.openmp = True
# np.bool = np.bool_
x = T.vector('x')
y = T.vector('y')
hit_test = operator.le(x ** 2 + y ** 2)
# hit_test = hit_test.lte(1)
hits = hit_test.sum()
misses = x.shape[0]
pi_est = 4 * hits/misses
calculate_pi = th.function([x, y], pi_est)
x_val = np.random.uniform(-1, 1, 30000)
y_val = np.random.uniform(-1, 1, 30000)
output = calculate_pi(x_val, y_val)
print(output)      