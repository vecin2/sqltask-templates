{% set table_metadata = _db.fetch.table_metadata(table_name) %}
{% set column_names = table_metadata.column('COLUMN_NAME') %}
{% set __column_to_update = column_to_update | suggest(column_names)%}
{% set __data_type = table_metadata.find(column_name=__column_to_update)['DATA_TYPE'] %}
{% set __new_value = new_value %}
{% if 'CHAR' in __data_type | upper %}
{% set __new_value = "'"+__new_value+"'" %}
{% endif %}
SET ({{__column_to_update}}) = ({{__new_value}})
