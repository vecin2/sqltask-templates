{% set property_names = _tps.fetch.all_properties().column('NAME') %}
DELETE FROM TENANT_PROPERTY
WHERE name = '{{ name | suggest(property_names) }}';
