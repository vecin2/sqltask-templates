{% set _verb_keyname = verb_keyname | suggest(_keynames.V)%}
{%set verb = _db.find.v_by_keyname(_verb_keyname)%}
{% set _is_user_visible= is_user_visible | print(verb)%}
UPDATE EVA_VERB
set (IS_USER_VISIBLE) = ('{{is_user_visible}}')
where ID = @V.{{_verb_keyname}}
