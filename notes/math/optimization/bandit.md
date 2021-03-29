# Multi-Armed Bandit


## The Problem Definition
For a given number of times, you are allowed to draw samples from $k$ unknown distributions.
Each time you can choose one of the $k$ distributions to draw a new sample.
The target is to get the maximum sum of all the samples you can draw.

## Regret
The regret is the measure of how good your strategy is.
It is the difference between the sum your strategy gets and the optimal strategy gets.
Therefore, we would like to have a strategy that minimizes the regret.
The regret is usually noted as $\rho$.

## Solution
As you draw more samples, we would like to estimate the parameters of the distributions so that we can figure out which one is the best to draw.
