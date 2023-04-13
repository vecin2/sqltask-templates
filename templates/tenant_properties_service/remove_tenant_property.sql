{% set property_names = _tps.fetch.property_names().column('NAME') %}
DELETE FROM TENANT_PROPERTY
WHERE name = '{{ name | suggest(property_names) }}';
