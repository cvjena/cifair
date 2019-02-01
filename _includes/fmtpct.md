{% assign num_split = include.num | round: 2 | split: "." -%}
{% assign integral = num_split[0] -%}
{% assign fractional = num_split[1] | append: "00" | truncate: 2, "" -%}
{% if include.hl %}**{% endif -%}
{{ integral }}.{{ fractional }}%
{%- if include.hl %}**{% endif %}