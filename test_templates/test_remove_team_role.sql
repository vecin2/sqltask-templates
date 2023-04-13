--{"team_role_keyname":"TestConsultant"}
DELETE FROM LOCALISED_FIELD WHERE OBJECT_TYPE = 'TeamRoleED' and OBJECT_VERSION = @TEAMROLE.TestConsultant;
DELETE FROM CE_TEAM_ROLE WHERE ID = @TEAMROLE.TestConsultant;
