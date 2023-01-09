--{"hostname":"mylocalhost","protocol":"8280"}
INSERT INTO FWI_HOST
(ID, ENV_ID, RELEASE_ID, UUID, PROTOCOL, HOSTNAME, PORT_NUMBER, IS_DELETED)
VALUES(@FWIH.mylocalhost8280, @ENV.Dflt, @RELEASE.ID, 'abc', 'http', 'mylocalhost', '8280', 'N');
