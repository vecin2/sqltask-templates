
{%set _person_keyname = person | suggest(_keynames.PERSON)%}
{%set _user_keyname = user | suggest(_keynames.USER)%}

DELETE FROM AGENT where username ='{{username}}';
DELETE FROM FD_USER_PROFILE_TYPE where USER_ID = @USER.{{_user_keyname}};
DELETE FROM FU_USER where username = '{{username}}';
DELETE FROM CE_PERSON where ID = @PERSON.{{_person_keyname}};
DELETE FROM CE_AGENT where ID = @PERSON.{{_person_keyname}};
DELETE  FROM FD_AGENT_SESSION_AUDIT WHERE AGENT_ID = @PERSON.{{_person_keyname}};
