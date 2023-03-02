{% set __entity_id = entity_id | suggest(_keynames.ED) %}
{% set entity_verbs = _db.fetch.v_with_pdr_and_pd(__entity_id) %}
{% set verb_ids = entity_verbs.column('V_KEYNAME') %}
{% set __verb_id = verb_id | suggest(verb_ids) %}
{% set __verb = entity_verbs.find(V_KEYNAME=__verb_id) %}

DELETE FROM LOCALISED_FIELD where OBJECT_TYPE ='VerbED' and OBJECT_VERSION =@V.{{__verb_id}};

DELETE
FROM EVA_VERB
WHERE ID = @V.{{__verb_id}}
and ENTITY_DEF_ID=@ED.{{__entity_id}};

{% set verbs_by_pdr = _db.fetch.v_names_by_pdr(__verb['PDR_KEYNAME']) %}
{% if verbs_by_pdr | length ==1 %}
DELETE FROM EVA_PROCESS_DESC_REFERENCE WHERE ID =@PDR.{{__verb['PDR_KEYNAME']}};
{% endif %}

{% set pdrs_by_pd = _db.fetch.pdrs_by_pd(__verb['PD_KEYNAME']) %}
{% if pdrs_by_pd | length ==1 %}
DELETE FROM LOCALISED_FIELD where OBJECT_TYPE ='ProcessDescriptorED' and OBJECT_VERSION =@PD.{{__verb['PD_KEYNAME']}};

DELETE FROM EVA_PROCESS_DESCRIPTOR WHERE ID = @PD.{{__verb['PD_KEYNAME']}};
{% endif %}

