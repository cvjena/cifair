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

{% capture best_cifar10 %}{% for model in site.data.models %}{{ model[1].cifar10_error | prepend:"0000" | slice:-6,6 }}:{{ model[0] }}{% unless forloop.last %},{% endunless %}{% endfor %}{% endcapture -%}
{% assign best_cifar10 = best_cifar10 | split:"," | sort %}{% assign best_cifar10 = best_cifar10.first | split:":" %}{% assign best_cifar10 = best_cifar10.last -%}
{% capture best_cifair10 %}{% for model in site.data.models %}{{ model[1].cifair10_error | prepend:"0000" | slice:-6,6 }}:{{ model[0] }}{% unless forloop.last %},{% endunless %}{% endfor %}{% endcapture -%}
{% assign best_cifair10 = best_cifair10 | split:"," | sort %}{% assign best_cifair10 = best_cifair10.first | split:":" %}{% assign best_cifair10 = best_cifair10.last -%}
{% capture best_cifar100 %}{% for model in site.data.models %}{{ model[1].cifar100_error | prepend:"0000" | slice:-6,6 }}:{{ model[0] }}{% unless forloop.last %},{% endunless %}{% endfor %}{% endcapture -%}
{% assign best_cifar100 = best_cifar100 | split:"," | sort %}{% assign best_cifar100 = best_cifar100.first | split:":" %}{% assign best_cifar100 = best_cifar100.last -%}
{% capture best_cifair100 %}{% for model in site.data.models %}{{ model[1].cifair100_error | prepend:"0000" | slice:-6,6 }}:{{ model[0] }}{% unless forloop.last %},{% endunless %}{% endfor %}{% endcapture -%}
{% assign best_cifair100 = best_cifair100 | split:"," | sort %}{% assign best_cifair100 = best_cifair100.first | split:":" %}{% assign best_cifair100 = best_cifair100.last -%}

| Architecture | Code | CIFAR-10 | ciFAIR-10 | CIFAR-100 | ciFAIR-100 | Pre-Trained Models |
|--------------|------|---------:|----------:|----------:|-----------:|--------------------|
{% for model_hash in site.data.models -%}
{% assign model = model_hash[1] -%}
| {% if model.paper %}[{{ model.name }}]({{ model.paper }}){% else %}{{ model.name }}{% endif %} | {% if model.framework and model.code %}[{{ model.framework }}]({{ model.code }}){% elsif model.framework %}{{ model.framework }}{% endif %} | {{ model.cifar10_error }}% | {{ model.cifair10_error }}% | {{ model.cifar100_error }}% | {{ model.cifair100_error }}% | {% if model.cifar10_model %}[CIFAR-10]({{ model.cifar10_model }}){% endif %} {% if model.cifar10_model and model.cifar100_model %}/{% endif %} {% if model.cifar100_model %}[CIFAR-100]({{ model.cifar100_model }}){% endif %}
{% endfor %}



[1]: https://www.cs.toronto.edu/~kriz/cifar.html