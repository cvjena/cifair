---
layout: default
title: ciFAIR
---

The test sets of the popular [CIFAR-10 and CIFAR-100 datasets][1] contain 3.25% and 10% duplicate images, respectively, i.e., images that can also be found in very similar form in the training set or the test set itself.
ciFAIR-10 and ciFAIR-100 are variants of these datasets with modified test sets, where all these duplicates have been replaced with new images.

The training sets have remained unchanged and are identical to those of CIFAR.

We encourage everyone training models on CIFAR to evaluate them on the ciFAIR test sets for an unbiased comparison.


Leaderboard & Pre-Trained Models
--------------------------------

We maintain a community-driven leaderboard of CNN architectures for image classification on ciFAIR.
Methods are sorted by their *error rate* on the ciFAIR-100 test set and the best value in each column is highlighted in bold font.  
Architectures are linked to the corresponding paper.
Clicking on the name of the CNN framework used for a certain architecture will bring you to the source code used for training the model.

{% include leaderboard.md %}

If you think a certain architecture should be included in this leaderboard, your [pull request][2] is very welcome.



[1]: https://www.cs.toronto.edu/~kriz/cifar.html
[2]: https://github.com/cvjena/cifair