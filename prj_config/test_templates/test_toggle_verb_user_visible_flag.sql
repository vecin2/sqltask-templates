--{"verb_keyname":"ViewContent"}
UPDATE EVA_VERB
set (IS_USER_VISIBLE) = ('Y')
where ID = @V.ViewContent
