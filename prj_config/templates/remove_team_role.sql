
DELETE FROM LOCALISED_FIELD WHERE OBJECT_TYPE = 'TeamRoleED' and OBJECT_VERSION = @TEAMROLE.{{team_role_keyname | suggest(_keynames.TEAMROLE)}};
DELETE FROM CE_TEAM_ROLE WHERE ID = @TEAMROLE.{{team_role_keyname}};
