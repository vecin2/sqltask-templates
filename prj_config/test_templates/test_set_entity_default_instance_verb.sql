--{"entity_keyname":"Content","default_verb_keyname":"ViewContent"}
UPDATE EVA_VERB
set (IS_INSTANCE_DEFAULT) = ('N')
where ENTITY_DEF_ID = @ED.Content;

UPDATE EVA_VERB
set (IS_INSTANCE_DEFAULT) = ('Y')
where ID = @V.ViewContent;
