{#
[related_tasks]
toggle_verb_user_visible_flag.sql,add_activity_to_perspective.sql

[related_views]
view_entity_displayed_verbs.sql,view_entity_verbs.sql

[oneline_description]
Determines what verb runs when user clicks on a entity displayed on context

[long_description]
This template prompts to select an entity keyname and then it prompts the instance verbs for that entity. Once the user has selected a verb, the generated SQL runs an update that sets the default instance flag on all the entity verbs to 'N' and then updates the specified verb to 'Y'.

### What is an Entity Default Instance Verb?
On agent desktop, when entity is added into context it displays on the left hand side activities panel showing as title the entities `toString()` result and underneath its "user visible" intance verbs.
User can run each verb by clicking on the verb title. User can also click on the entities title and it will run the default instance verb.
#}

{%set _entity_keyname = entity_keyname | suggest(_keynames.ED) %}
{% set entity_verb_keynames = _db.fetch.instance_verbs_by_ed(_entity_keyname).column('KEYNAME') %}
{% set _verb_keyname = verb_keyname | suggest(entity_verb_keynames)%}

--make {{_verb_keyname}} default verb
UPDATE EVA_VERB
set (IS_INSTANCE_DEFAULT) = ('N')
where ENTITY_DEF_ID = @ED.{{_entity_keyname}};

UPDATE EVA_VERB
set (IS_INSTANCE_DEFAULT) = ('Y')
where ID = @V.{{_verb_keyname}};
