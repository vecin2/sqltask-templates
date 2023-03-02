{% set keysets = _db.fetch.all_keysets().column('KEYSET') %}
SELECT * FROM CCADMIN_IDMAP 
where keyset = '{{keyset | suggest(keysets)}}'
and keyname like '%{{keyname | description ("keyname: (it will be use within a like \"%%\")") | suggest(_keynames.PDR)}}%'
