 {# Compute current pd #}
	{% set verb_keynames= _db.fetch.v_names_by_ed(entity_def_id | suggest(_keynames.ED)).column("KEYNAME") %}
{% set _verb_keyname = verb_keyname | suggest(verb_keynames) %}
{% set _new_process_desc_ref= new_process_descriptor_reference |  suggest(_keynames.PDR)%}
{% set old_pd = _db.fetch.pd_by_v_keyname(verb_keyname)%}
{% if old_pd | length ==1%}
{% set description = "This verb is currently point to:\n"+old_pd| string%}
{% else %}
{% set description = "This verb is currently not pointing to any process descriptor reference"%}
{% endif %}

UPDATE EVA_VERB
SET (PROCESS_DESC_REF_ID) = (@PDR.{{_new_process_desc_ref | print(description)}})
WHERE ID = @V.{{_verb_keyname}};
