{% set contact_edvlds = _db.fetch.edvl_by_type_id('InlineViewContactConfig')%}
{% set entity_verbs = contact_edvlds.column('ENTITY_VERB') %}
{% set __entity_verb =  entity_verb | suggest(entity_verbs) %}
{% set edvl_id = contact_edvlds.find(ENTITY_VERB=__entity_verb)['EDVL_KEYNAME'] %}
{% include 'hidden_templates/remove_dynamic_verb_list.sql' %}
