{% set edvld_id = edvl_id | suggest(_keynames.EDVL) %}
{% include 'hidden_templates/remove_dynamic_verb_list.sql' %}
