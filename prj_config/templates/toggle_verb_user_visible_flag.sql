{% set _verb_keyname = verb_keyname | suggest(_keynames.V)%}
{%set verb = _db.find.v_by_keyname(_verb_keyname)%}

{% if verb['IS_USER_VISIBLE'] == 'Y' %} 
{% set is_user_visible= 'N'%}
{% else %}
{% set is_user_visible= 'Y'%}
{% endif %}

UPDATE EVA_VERB
set (IS_USER_VISIBLE) = ('{{is_user_visible}}')
where ID = @V.{{_verb_keyname}}
