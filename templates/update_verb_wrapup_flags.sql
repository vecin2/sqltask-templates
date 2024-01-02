{% set _entity_definition_keyname = entity_definition_keyname | suggest(_keynames.ED) %}
{% set verb_keynames = _db.fetch.verbs_by_ed(_entity_definition_keyname).column("KEYNAME") %}
{% set _verb_keyname = verb_keyname | suggest(verb_keynames) %}
{% set _record_for_wrapup = record_for_wrapup | description("record_for_wrapup (y/n)")%}
{% set _display_at_wrapup = display_at_wrapup | description("display_at_wrapup (y/n)")%}

UPDATE EVA_VERB 
SET (RECORD_FOR_WRAPUP, DISPLAY_AT_WRAPUP) = ('{{_record_for_wrapup}}','{{_display_at_wrapup}}')
WHERE ID = @V.{{_verb_keyname}};
