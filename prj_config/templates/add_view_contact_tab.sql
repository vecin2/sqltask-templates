{% set  edvl_type_keyname ='InlineViewContactConfig' %}
{% set  entity_id ='Contact' %}
{% set verb_names = _db.fetch.v_names_by_et(entity_id).column('NAME') %}
{% set description ="Verbs suggested are Contact verbs, since the entity passed to this process  is Contact.\nMake sure the process implementing this verb has a parameter called 'contact'."%}
{%set __verb_name = verb_name | suggest(verb_names) | print(description)%} 
{% include 'hidden_templates/insert_dynamic_verb_list.sql'%}
{% set parameter_source_name = "contact"%}
{% set parameter_destination_name = "contact"%}
{% set parameter_is_mandatory = "Y"%}
{% include 'hidden_templates/insert_dynamic_verb_parameter.sql'%}

