{% set keysets = _db.fetch.all_keysets().column('KEYSET') %}
SELECT * FROM CCADMIN_IDMAP 
where keyset = '{{keyset | suggest(keysets)}}'
