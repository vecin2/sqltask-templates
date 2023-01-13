--{"entity_keyname":"Content","verb_keyname":"ViewContent","is_user_visible":"Y"}
UPDATE EVA_VERB
set (IS_USER_VISIBLE) = ('Y')
where ID = @V.ViewContent;
