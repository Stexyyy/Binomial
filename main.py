from scipy.stats import binom
import matplotlib.pyplot as plt
#binomial distribution


n = 6 #number of trials
p = 0.37 #probability

#figure out how line 8 works by and what it prints (note for myself)
values = list(range(n+1))
print("Values are:", values)

# "pmf" stands for "probabulity mass function"
# it's the probability that a discrete random variable will be exactly equal to a particular value
# the binomial distribution is a kind of pmf!!!!
#here r is our iterator, n is trials, and p is probability
dist = [binom.pmf(r, n, p) for r in values ]
print("binomial distribution is:", dist)

#plotting the graph
plt.bar(values, dist)
plt.show()
