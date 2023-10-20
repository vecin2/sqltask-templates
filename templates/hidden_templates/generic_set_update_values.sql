{% set table_metadata = _db.fetch.table_metadata(table_name) %}
{% set column_names = table_metadata.column('COLUMN_NAME') %}
{% set __column_to_update = column_to_update | suggest(column_names)%}
{% set __data_type = table_metadata.find(column_name=__column_to_update)['DATA_TYPE'] %}
{% set __new_value = new_value | print("Wrap value on single quotes if value is a string, e.g. 'Action'")%}
SET ({{__column_to_update}}) = ({{__new_value}})
