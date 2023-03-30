{#
[oneline_description]
Reorder dynamic view field by moving it up or down to a given position


[long_description]
If we take as example the following fields:

|            KEYNAME            | VIEW_FIELD_SEQUENCE |
|-------------------------------|---------------------|
|   KnowledgeSegmentCreateBody  |          1          |
|  KnowledgeSegmentCreateKBase  |          2          |
| KnowledgeSegmentCreateProduct |          3          |
|  KnowledgeSegmentCreateTopic  |          4          |
|  KnowledgeSegmentCreateRegion |          5          |


**Moving Up**

Selecting 'KnowledgeSegmentCreateTopic' and entering sequence_no '2' will change to:

|            KEYNAME            | VIEW_FIELD_SEQUENCE |
|-------------------------------|---------------------|
|   KnowledgeSegmentCreateBody  |          1          |
|  KnowledgeSegmentCreateTopic  |          2          |
|  KnowledgeSegmentCreateKBase  |          3          |
| KnowledgeSegmentCreateProduct |          4          |
|  KnowledgeSegmentCreateRegion |          5          |


**Moving Down**

Now we can move 'KnowledgeSegmentCreateTopic' back to his original place by selecting 'KnowledgeSegmentCreateTopic' and entering sequence_no '4'.

[related_tasks]
add_dynamic_entity_view_field.sql
#}

{% set _entity_keynames = _db.fetch.all_dynamic_eds().column('KEYNAME') %}
{% set _entity_keyname= dynamic_entity | suggest(_entity_keynames) %}
{% set __dyn_view_keynames = _db.fetch.dynamic_views_by_ed(_entity_keyname).column('KEYNAME') %}
{% set __dyn_view_keyname = view | suggest(__dyn_view_keynames) %}
{% set __view_fields = _db.fetch.dynamic_view_fields_by_view(__dyn_view_keyname) %}
{% set __view_field_keynames = __view_fields.column('KEYNAME') %}
{% set __view_field = view_field | print(__view_fields) | suggest(__view_field_keynames) %}
{% set __sequence_numbers = __view_fields.column('VIEW_FIELD_SEQUENCE') %}

{% set __sequence_no = view_field_sequence | print(__sequence_numbers) %}

{% set __current_seq_no = __view_fields.find(keyname=__view_field)['VIEW_FIELD_SEQUENCE'] | string %}
--Changing View {{__dyn_view_keyname}}
--make space for field  {{__view_field}}
{% if __current_seq_no | int > __sequence_no | int %}
{# Fields is being moved up#}
 {% set increasing_factor = 1 %}
{% set __fields_to_update = __view_fields.where("VIEW_FIELD_SEQUENCE>="+__sequence_no)%}
 {% set __fields_to_update = __fields_to_update.where("VIEW_FIELD_SEQUENCE<"+__current_seq_no)%}
{%else%}
{# Fields is being moved down#}
 {% set increasing_factor = -1 %}
{% set __fields_to_update = __view_fields.where("VIEW_FIELD_SEQUENCE<="+__sequence_no)%}
 {% set __fields_to_update = __fields_to_update.where("VIEW_FIELD_SEQUENCE>"+__current_seq_no)%}
{% endif %}
{% for item in __fields_to_update %}
UPDATE EVA_DYNAMIC_ENTITY_VIEW_FIELD 
SET (VIEW_FIELD_SEQUENCE) =({{item.VIEW_FIELD_SEQUENCE + increasing_factor }})
WHERE ID = @EDEVF.{{item.KEYNAME}};
{% endfor %}

--move field {{__dyn_view_keyname}} to position
 UPDATE EVA_DYNAMIC_ENTITY_VIEW_FIELD 
 SET (VIEW_FIELD_SEQUENCE) =({{__sequence_no}})
 WHERE ID = @EDEVF.{{__view_field}};

