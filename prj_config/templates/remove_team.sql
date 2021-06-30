{% set __team_keyname = team_keyname | suggest(_keynames.TEAM) %}
DELETE FROM CWQ_ENTITY__QUEUE WHERE ENTITY_ID = @TEAM.{{__team_keyname}} and ENTITY_TYPE_ID= @ET.Team;
DELETE FROM FD_HOMEPAGE_ASSIGNMENT WHERE ENTITY_ID=@TEAM.{{__team_keyname}} and ENTITY_TYPE_ID= @ET.Team;
DELETE FROM LOCALISED_FIELD WHERE OBJECT_TYPE='TeamED' and OBJECT_VERSION=@TEAM.{{__team_keyname}};
DELETE FROM CE_TEAM WHERE ID = @TEAM.{{__team_keyname}};
DELETE FROM LOCALISED_FIELD WHERE OBJECT_TYPE='QueueED' and OBJECT_VERSION=@QUEUE.{{__team_keyname}}TeamQueue;
DELETE FROM CWQ_QUEUE where ID = @QUEUE.{{__team_keyname}}TeamQueue;
DELETE FROM FRB_RULE_SET where ID = @RS.{{__team_keyname}}TeamQueue;
