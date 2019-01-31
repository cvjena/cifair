---
layout: page
title: ciFAIR
---

ciFAIR
======

A duplicate-free variant of the CIFAR test set
----------------------------------------------

The test sets of the popular [CIFAR-10 and CIFAR-100 datasets][1] contain 3.25% and 10% duplicate images, respectively, i.e., images that can also be found in very similar form in the training set or the test set itself.
ciFAIR-10 and ciFAIR-100 are variants of these datasets with modified test sets, where all these duplicates have been replaced with new images.

The training sets have remained unchanged and are identical to those of CIFAR.

We encourage everyone training models on CIFAR to evaluate them on the ciFAIR test sets for an unbiased comparison.


Leaderboard & Pre-Trained Models
--------------------------------

| Architecture | Code / Framework | CIFAR-10 | ciFAIR-10 | CIFAR-100 | ciFAIR-100 | Pre-Trained Models |
|--------------|------------------|---------:|----------:|----------:|-----------:|--------------------|
{% for model_hash in site.data.models -%}
{% assign model = model_hash[1] -%}
| [{{ model.name }}]({{ model.paper }}) | [{{ model.framework }}]({{ model.code }}) | {{ model.cifar10_error }}% | {{ model.cifair10_error }}% | {{ model.cifar100_error }}% | {{ model.cifair100_error }}% | [CIFAR-10]({{ model.cifar10_model }}) / [CIFAR-100]({{ model.cifar100_model }})
{% endfor %}



[1]: https://www.cs.toronto.edu/~kriz/cifar.html