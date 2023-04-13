{% set keysets = _db.fetch.all_keysets().column('KEYSET') %}
{% set __keyset = keyset | suggest(keysets) %}
{% set __keynames = _db.fetch.keynames_by_keyset(__keyset).column('KEYNAME') %}
SELECT * FROM CCADMIN_IDMAP 
where keyset = '{{__keyset}}'
and keyname like '%{{keyname | description ("keyname: (it will be use within a like \"%%\")") | suggest(__keynames)}}%'
