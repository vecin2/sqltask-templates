{% set ent_entity_type = "Agent" %}
{% set entity_keyset = "PERSON" %}
{% set entity_keyname = agent | suggest(_keynames.PERSON) %}
{% include 'hidden_templates/add_entity_entitlement.sql' %}
