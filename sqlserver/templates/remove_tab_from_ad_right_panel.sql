
{% set __perspective_id = perspective_id | suggest(_keynames.PPTIVE)%}
{% set tab_verbs = _db.fetch.ad_right_panel_verbs(__perspective_id) %}
{% set tab_verb_keynames =tab_verbs.column("verb_keyname")%}

DELETE FROM FD_ENTITY__AUX_VERBS 
where entity_id= @PPTIVE.{{__perspective_id}}
and AUXILIARY_VERB_ID = @V.{{verb_keyname | suggest(tab_verb_keynames)}}

