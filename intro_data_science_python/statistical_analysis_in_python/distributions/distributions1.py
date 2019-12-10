# distribution - set of all possible random variables together

import numpy as np

# evenly distributed binomial distributions - flipping a coin

print(np.random.binomial(1, 0.5))
# Here we ask for a number from the NumPy binomial distribution. We have two parameters to pass in. The first is the
# number of times we want it to run. The second is the chance we get a zero, which we will use to represent heads here.
# Let's run one round of this simulation.

# What if we run the simulation a thousand times and divided the result by a thousand. Well you see a number pretty
# close to 0.5 which means half of the time we had a heads and half of the time we had a tails.
print(np.random.binomial(1000, 0.5) / 1000)


# Suppose we want to simulate the probability of flipping a fair coin 20 times, and getting a number greater than or
# equal to 15. Use np.random.binomial(n, p, size) to do 10000 simulations of flipping a fair coin 20 times, then see
# what proportion of the simulations are 15 or greater.
x = np.random.binomial(20, 0.5, 10000)
j=0
for i in x:
    if i>=15:
        j+=1
print(j)
# or
print((x>=15).mean())


# unevenly distributed binomial distribution

chance_of_tornado = 0.01 / 100
print(np.random.binomial(100000, chance_of_tornado))

# Let's say the chance of a tornado here in Ann Arbor on any given day, is 1% regardless of the time of year
# So what's the chance of this happening two days in a row?
chance_of_tornado = 0.01
tornado_events = np.random.binomial(1, chance_of_tornado, 100000)
# using 100000 days
two_days_in_a_row = 0
for j in range(1, len(tornado_events)):
    if tornado_events[j] == 1 and tornado_events[j-1] == 1:
        two_days_in_a_row += 1
print(two_days_in_a_row)

# uniform distribution -  flat line
print(np.random.uniform(0, 1))

# normal distribution - bell curve
print(np.random.normal(0.75))   # exepected value

# Let's draw 1,000 samples from a normal distribution with an expected value of 0.75 and a standard deviation of 1.
distribution = np.random.normal(0.75, size=1000)
# Standard Devaition formula = calculate the actual mean using NumPy's mean feature. The part inside the summation says xi- x bar. Xi is the
# current item in the list and x bar is the mean. So we calculate the difference, then we square the result, then we sum
# all of these.
print(np.sqrt(np.sum((np.mean(distribution)-distribution)**2)/len(distribution)))
# OR
print(np.std(distribution))

# There's a couple more measures of distribution that are interesting to talk about. One of these is the shape of the
# tales of the distribution and this is called the kurtosis. We can measure the kurtosis using the statistics functions
# in the SciPy package. A negative value means the curve is slightly more flat than a normal distribution, and a
# positive value means the curve is slightly more peaky than a normal distribution. Remember that we aren't measuring
# the kurtosis of the distribution per se, but of the thousand values which we sampled out of the distribution. This is
# a sublet but important distinction.
import scipy.stats as stats
print(stats.kurtosis(distribution))

# We could also move out of the normal distributions and push the peak of the curve one way or the other.
# And this is called the skew.
print(stats.skew(distribution))

# Chi squared distribution
# The Chi Squared Distribution has only one parameter called the degrees of freedom. The degrees of freedom is closely
# related to the number of samples that you take from a normal population. It's important for significance testing.
# But what I would like you to observe, is that as the degrees of freedom increases, the shape of the Chi Squared
# distribution changes. In particular, the skew to the left begins to move towards the center. We can observe this
# through simulation.
# First we'll sample 1,000 values from a Chi Squared distribution with degrees of freedom 2. Now we can see that the
# skew is quite large. Now if we re-sample changing degrees of freedom to 5.
# We see that the skew has decreased significantly.
chi_squared_df2 = np.random.chisquare(2, size=1000)
print(stats.skew(chi_squared_df2))
chi_squared_df5 = np.random.chisquare(5, size=1000)
print(stats.skew(chi_squared_df5))

# Bimodal distributions - two peaks
# These are really interesting distributions and happen regularly in data mining. We're going to talk a bit more about
# them in course three. But a useful insight is that we can actually model these using two normal distributions with
# different parameters. These are called Gaussian Mixture Models and are particularly useful when clustering data.

