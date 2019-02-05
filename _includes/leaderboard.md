{% comment %}Unzip site.data.models and sort by ciFAIR-100 test error{% endcomment -%}
{% assign models = "" | split: "," -%}
{% for model_hash in site.data.models -%}
{% assign models = models | push: model_hash[1] -%}
{% endfor -%}
{% assign models = models | sort: "cifair100_error" -%}

{% comment %}Very hacky code to find the model with the lowest error rate on each dataset{% endcomment -%}
{% capture best_cifar10 %}{% for model in models %}{% capture err %}{% include fmtpct.md num=model.cifar10_error %}{% endcapture %}{{ err | prepend:"0000" | slice:-6,6 }}:{{ model.cifar10_error }}{% unless forloop.last %},{% endunless %}{% endfor %}{% endcapture -%}
{% assign best_cifar10 = best_cifar10 | split:"," | sort %}{% assign best_cifar10 = best_cifar10.first | split:":" %}{% assign best_cifar10 = best_cifar10.last | plus: 0.0 -%}
{% capture best_cifair10 %}{% for model in models %}{% capture err %}{% include fmtpct.md num=model.cifair10_error %}{% endcapture %}{{ err | prepend:"0000" | slice:-6,6 }}:{{ model.cifair10_error }}{% unless forloop.last %},{% endunless %}{% endfor %}{% endcapture -%}
{% assign best_cifair10 = best_cifair10 | split:"," | sort %}{% assign best_cifair10 = best_cifair10.first | split:":" %}{% assign best_cifair10 = best_cifair10.last | plus: 0.0 -%}
{% capture best_cifar100 %}{% for model in models %}{% capture err %}{% include fmtpct.md num=model.cifar100_error %}{% endcapture %}{{ err | prepend:"0000" | slice:-6,6 }}:{{ model.cifar100_error }}{% unless forloop.last %},{% endunless %}{% endfor %}{% endcapture -%}
{% assign best_cifar100 = best_cifar100 | split:"," | sort %}{% assign best_cifar100 = best_cifar100.first | split:":" %}{% assign best_cifar100 = best_cifar100.last | plus: 0.0 -%}
{% capture best_cifair100 %}{% for model in models %}{% capture err %}{% include fmtpct.md num=model.cifair100_error %}{% endcapture %}{{ err | prepend:"0000" | slice:-6,6 }}:{{ model.cifair100_error }}{% unless forloop.last %},{% endunless %}{% endfor %}{% endcapture -%}
{% assign best_cifair100 = best_cifair100 | split:"," | sort %}{% assign best_cifair100 = best_cifair100.first | split:":" %}{% assign best_cifair100 = best_cifair100.last | plus: 0.0 -%}

{% comment %}Format the actual table{% endcomment -%}

| Architecture | Code | Params | CIFAR-10 | ciFAIR-10 | CIFAR-100 | ciFAIR-100 | Pre-Trained Models |
|--------------|------|-------:|---------:|----------:|----------:|-----------:|:------------------:|
{% for model in models -%}
{% if model.cifar10_error == best_cifar10 %}{% assign is_best_cifar10 = true %}{% else %}{% assign is_best_cifar10 = false %}{% endif -%}
{% if model.cifair10_error == best_cifair10 %}{% assign is_best_cifair10 = true %}{% else %}{% assign is_best_cifair10 = false %}{% endif -%}
{% if model.cifar100_error == best_cifar100 %}{% assign is_best_cifar100 = true %}{% else %}{% assign is_best_cifar100 = false %}{% endif -%}
{% if model.cifair100_error == best_cifair100 %}{% assign is_best_cifair100 = true %}{% else %}{% assign is_best_cifair100 = false %}{% endif -%}
| {% if model.paper %}[{{ model.name }}]({{ model.paper }}){% else %}{{ model.name }}{% endif %} | {% if model.framework and model.code %}[{{ model.framework }}]({{ model.code }}){% elsif model.framework %}{{ model.framework }}{% endif %} | {% if model.num_params %}{% include fmtbignum.md num=model.num_params %}{% endif %} | {% include fmtpct.md num=model.cifar10_error hl=is_best_cifar10 %} | {% include fmtpct.md num=model.cifair10_error hl=is_best_cifair10 %} | {% include fmtpct.md num=model.cifar100_error hl=is_best_cifar100 %} | {% include fmtpct.md num=model.cifair100_error hl=is_best_cifair100 %} | {% if model.cifar10_model %}[CIFAR-10]({{ model.cifar10_model }}){% endif %} {% if model.cifar10_model and model.cifar100_model %}/{% endif %} {% if model.cifar100_model %}[CIFAR-100]({{ model.cifar100_model }}){% endif %} |
{% endfor %}