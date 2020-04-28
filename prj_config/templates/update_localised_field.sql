{% set object_types = _db.fetch.lf_object_types().column('OBJECT_TYPE') %}
{% set __object_type = object_type | suggest(object_types)%}
{% set object_instances = _db.fetch.lf_object_instances_by_ot(__object_type).column('OBJECT_INSTANCE') %}
{% set __object_instance = object_instance | suggest(object_instances)%}
{% set field_names = _db.fetch.lf_field_names_by_ot_and_oi(__object_type,__object_instance).column('FIELD_NAME') %}
{% set __field_name = field_name | description("field_name (leave blank to update all fields)") | default("") | suggest(field_names)%}
{% set __locale =locale | default(_locale)%}
UPDATE LOCALISED_FIELD
{% set table_name="LOCALISED_FIELD" %}
{% include '/hidden_templates/generic_set_update_values.sql' %}
where OBJECT_TYPE ='{{object_type}}' 
and OBJECT_INSTANCE = '{{object_instance}}'
{% if __field_name %}
and FIELD_NAME ='{{__field_name}}'
{% endif %}
and LOCALE = '{{__locale}}';
