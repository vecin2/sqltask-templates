--{"_person":"CCADMIN","_user":"admin","username":"admin"}

DELETE FROM AGENT where username ='admin';
DELETE FROM FD_USER_PROFILE_TYPE where USER_ID = @USER.admin;
DELETE FROM FU_USER where username = 'admin';
DELETE FROM CE_PERSON where ID = @PERSON.CCADMIN;
DELETE FROM CE_AGENT where ID = @PERSON.CCADMIN;
DELETE  FROM FD_AGENT_SESSION_AUDIT WHERE AGENT_ID = @PERSON.CCADMIN;