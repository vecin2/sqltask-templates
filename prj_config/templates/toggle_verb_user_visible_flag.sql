{%set _entity_keyname = entity_keyname | suggest(_keynames.ED) %}
{% set entity_verb_keynames = _db.fetch.v_names_by_ed(_entity_keyname).column('KEYNAME') %}
{% set _verb_keyname = verb_keyname | suggest(entity_verb_keynames)%}
{%set verb = _db.find.v_by_keyname(_verb_keyname)%}

{% if verb['IS_USER_VISIBLE'] == 'Y' %} 
{% set is_user_visible= 'N'%}
{% else %}
{% set is_user_visible= 'Y'%}
{% endif %}

UPDATE EVA_VERB
set (IS_USER_VISIBLE) = ('{{is_user_visible}}')
where ID = @V.{{_verb_keyname}}
