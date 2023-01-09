--{"profile_name":"GTX Admin","desktop_process":"","add_perspectives":"n"}
INSERT INTO FD_PROFILE_TYPE (ID,ENV_ID,DESKTOP_PROCESS,IS_DELETED,NAME,RELEASE_ID,TENANT_ID,SYSTEM_NAME) 
VALUES (
	@PROFILE.GTXAdmin, --ID
	@ENV.Dflt, --ENV_ID
	'FrameworkDesktop.Implementation.ProfileProcess.DesktopProfileProcess', --DESKTOP_PROCESS
	'N', --IS_DELETED
	'GTX Admin', --NAME
	@RELEASE.ID, --RELEASE_ID
	'default', --TENANT_ID
	'GTXAdmin' --SYSTEM_NAME
);

