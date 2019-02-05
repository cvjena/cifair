{% if include.num < 100 -%}
{{ include.num }}
{%- else %}
{%- if include.num >= 1000000000 %}{% assign suffix = "G" %}{% assign num = include.num | divided_by: 1000000000.0 %}
{%- elsif include.num >= 100000 %}{% assign suffix = "M" %}{% assign num = include.num | divided_by: 1000000.0 %}
{%- else %}{% assign suffix = "K" %}{% assign num = include.num | divided_by: 1000.0 %}
{%- endif -%}
{% assign num_split = num | round: 1 | split: "." -%}
{% assign integral = num_split[0] -%}
{% assign fractional = num_split[1] | append: "0" | truncate: 1, "" -%}
{{ integral }}.{{ fractional }} {{ suffix }}
{%- endif %}