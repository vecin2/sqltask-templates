{% set default_display_name =  verb_name | split_uppercase() 
				| description ("verb_name (e.g inlineEdit)")%}
{% set __verb_display_name = verb_display_name | description("verb_display_name")
			       | default(default_display_name)%}
{% set __verb_description = verb_description | description("verb_description")
			       | default(default_display_name)%}

{% set __entity_def_id = entity_def_id | suggest(_keynames.ED) %}

{# next line capitalize only the first letter. We cant user capitalize or title because 
they put the  rest of the letter to lower case, but we want to leave them as they are #}
{% set titled_verb_name = verb_name[0].upper() + verb_name[1:] %}
{% set default_verb_id = __entity_def_id+titled_verb_name %}
{% set __verb_id = default_verb_id %}
{% set process_descriptor_ref_id = process_desc_ref_id | default(__verb_id) | suggest(_keynames.PDR) %}
{% set process_descriptor_id = process_desc_id | default(__verb_id)  | suggest(_keynames.PD)%}

{% if process_descriptor_id not in _keynames.PD %}
  {% include 'add_process_descriptor.sql' %}
{% endif %}

{% if process_descriptor_ref_id not in _keynames.PDR %}
  {% include 'hidden_templates/add_process_descriptor_ref.sql' %}
{% endif %}


{% set entity_ids = _keynames.ED %}
INSERT INTO EVA_VERB (ID, NAME, PROCESS_DESC_REF_ID, ENTITY_DEF_ID, ENTITY_DEF_ENV_ID, IS_INSTANCE, IS_DEFAULT, IS_INSTANCE_DEFAULT, IS_USER_VISIBLE,RECORD_FOR_WRAPUP) VALUES (
@V.{{__verb_id}}, --ID
'{{verb_name}}', -- NAME
@PDR.{{process_descriptor_ref_id}}, --PROCESS_DESC_REF_ID
@ED.{{__entity_def_id | suggest(entity_ids)}}, -- ENTITY_DEF_ID
@ENV.Dflt, -- ENTITY_DEF_ENV_ID
'{{is_instance | description("is_instance (Y/N)")}}', --IS_INSTANCE
'N', -- IS_DEFAULT
{% if is_instance == 'N'%} {% set is_instance_default = 'N' %} {%endif%}
'{{is_instance_default | description("is_instance_default (Y/N)")}}', -- IS_INSTANCE_DEFAULT
'{{is_user_visible | description("is_user_visible (Y/N)")}}', -- IS_USER_VISIBLE
'{{record_for_wrapup | description("record_for_wrappup (Y/N)")}}' -- RECORD_FOR_WRAPUP
);

{% set entity = _db.find.ed_by_keyname(__entity_def_id) %}
{% set object_type = "VerbED" %}
{% set object_instance =  entity["NAME"]+"__"+verb_name %}
{% set object_version = "@V."+__verb_id %}
{% set text = __verb_display_name %}
{% set field_name= 'displayName'  %}
{% include 'add_localised_field.sql' %}

{% set field_name= 'description'  %}
{% set text = __verb_description %}
{% include 'add_localised_field.sql' %}
