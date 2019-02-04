---
layout: default
title: ciFAIR
---

The test sets of the popular [CIFAR-10 and CIFAR-100 datasets][1] contain 3.25% and 10% duplicate images, respectively, i.e., images that can also be found in very similar form in the training set or the test set itself.
ciFAIR-10 and ciFAIR-100 are variants of these datasets with modified test sets, where all these duplicates have been replaced with new images.

{% if site.paper %}
Details about how we found duplicates in CIFAR and created ciFAIR can be found in the following paper:

> [*{{ site.paper.title }}*]({{ site.paper.url }})  
> {{ site.paper.authors }}.  
> {{ site.paper.venue }}, {{ site.paper.year }}.
{% endif %}

The training sets have remained unchanged and are identical to those of CIFAR.

We encourage everyone training models on CIFAR to evaluate them on the ciFAIR test sets for an unbiased comparison.
Download links can be found at the top of the page.
{% if site.paper %}If you use ciFAIR, please cite the paper mentioned above.{% endif %}

Both datasets have the same structure as CIFAR and are intended to be used as drop-in replacements.
However, there are two compatibility issues:

- The test set pickle files do not contain an item `'filenames'`.
- The test set pickle files cannot be loaded with Python 2. We were not able to save them in a compatible pickle format due to [this bug][3]. If you find a way to achieve this, please create a [pull request][2].

If you are interested in the actual duplicate images we have found in the original CIFAR datasets, you can find lists of these [here][4].


Leaderboard & Pre-Trained Models
--------------------------------

We maintain a community-driven leaderboard of CNN architectures for image classification on ciFAIR.
Methods are sorted by their *error rate* on the ciFAIR-100 test set and the best value in each column is highlighted in bold font.  
Architectures are linked to the corresponding paper.
Clicking on the name of the CNN framework used for a certain architecture will bring you to the source code used for training the model.

{% include leaderboard.md %}

If you think a certain architecture should be included in this leaderboard, your [pull request][2] is very welcome.



[1]: https://www.cs.toronto.edu/~kriz/cifar.html
[2]: {{ site.github.repository_url }}
[3]: https://bugs.python.org/issue13566
[4]: {{ site.github.repository_url }}/tree/master/meta