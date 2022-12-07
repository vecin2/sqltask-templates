{% set __context_config_id = context_config_id | suggest(_keynames.CC) %}
{% set __entity_type = entity_type | suggest(_keynames.ET) %}
{% set verb_names = _db.fetch.v_names_by_et(__entity_type).column('NAME') %}
{% set __verb_name = verb_name | suggest(verb_names)%}
{% set context_config_verbs = _db.fetch.v_by_pers_keyname(__context_config_id) %}
{%set seq_no_desc ="All the activities sequence numbers are 1 by default which will display them in alphabetical order. Please notice that changing the Context within 'Manage Context' admin screen overrides sequence numbers"+
				   " and set them matching the screen order.\n"
				   "\nShould we display the activities in alphabetical order?(Y/N)?"%}
{% set __sequence_number = 1 %}

--inserting new activity in specific sequence no
{% include 'hidden_templates/insert_context_verb_entry.sql' %}
