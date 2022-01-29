--{"profile_name":"GTX Admin","desktop_process":"","add_perspectives":"n"}
INSERT INTO FD_PROFILE_TYPE (ID,ENV_ID,DESKTOP_PROCESS,IS_DELETED,NAME,SYSTEM_NAME,RELEASE_ID,TENANT_ID) 
VALUES (
	@PROFILE.GTXAdmin, --ID
	@ENV.Dflt, --ENV_ID
	'FrameworkDesktop.Implementation.ProfileProcess.DesktopProfileProcess', --DESKTOP_PROCESS
	'N', --IS_DELETED
	'GTX Admin', --NAME
	'GTXAdmin', --SYSTEM_NAME
	@RELEASE.ID, --RELEASE_ID
	'default' --TENANT_ID
);

