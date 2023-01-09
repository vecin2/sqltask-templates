DELETE FROM CE_TEAM_ROLE_TYPE WHERE ID = @TEAMROLETYPE.{{role_type_keyname | suggest(_keynames.TEAMROLETYPE)}};
