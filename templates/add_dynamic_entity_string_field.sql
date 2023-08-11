{% set entity_field_type = 'StringField' %} 
{# No need to compute property type because we are adding string, consider this if we create a 'add_generic_field' template
{% set __has_property = has_property | print("Does this field have any property? For example limit the string length") | description("has_property (Y/N)") %}
{% if __has_property == "Y" %}
{% set property_types = _db.fetch.all_property_types().column("KEYNAME") %}
{% set __property_type = property_type | suggest(property_types) %}
#}
{% set property_type = "StringFieldProperties" %}
{% include 'hidden_templates/add_dynamic_entity_field_without_specific_props.sql' %} 


{% set dynamic_field_property_keyname = keyname %}
{% include 'hidden_templates/add_dynamic_string_field_property.sql' %}
