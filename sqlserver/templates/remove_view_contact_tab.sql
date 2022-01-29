{% set contact_edvlds = _db.fetch.edvl_by_type_id('InlineViewContactConfig')%}
{% set entity_verbs = contact_edvlds.column('entity_verb') %}
{% set __entity_verb =  entity_verb | suggest(entity_verbs) %}
{% set edvl_id = contact_edvlds.find(entity_verb=__entity_verb)['edvl_keyname'] %}
{% include 'hidden_templates/remove_dynamic_verb_list.sql' %}
