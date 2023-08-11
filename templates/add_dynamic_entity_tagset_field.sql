{% set entity_field_type = 'TagSetSelectionField' %} 
{% set property_type = "TagSetFieldProperties" %}
{% include 'hidden_templates/add_dynamic_entity_field_without_specific_props.sql' %} 
{% set dynamic_field_property_keyname = keyname %}
{% include 'hidden_templates/add_dynamic_tagset_field_property.sql' %} 
