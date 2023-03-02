{% set entity_keyset = "TEAM" %}
{% set ent_entity_type = "Team" %}
{% set entity_keyname = team | suggest(_keynames.TEAM) %}
{% include 'hidden_templates/add_entity_entitlement.sql' %}
