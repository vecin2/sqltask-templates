{% set entity_keyset = "PROFILE" %}
{% set ent_entity_type = "ProfileType" %}
{% set entity_keyname = profile | suggest(_keynames.PROFILE) %}
{% include 'hidden_templates/add_entity_entitlement.sql' %}
