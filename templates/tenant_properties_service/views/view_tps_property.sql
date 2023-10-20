{% set property_names = _tps.fetch.all_properties().column('NAME') %}
SELECT * FROM TENANT_PROPERTY tp WHERE name='{{property_name | suggest(property_names)}}'
