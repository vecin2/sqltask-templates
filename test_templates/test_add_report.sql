--{"report_keyname":"Agent Performance","report_description":"Displays an overview of chat performance for agents along with their availability durations.", "report_menu_keyname":"ChatReports","report_url":"<JASPER_UI_URL>/jasperserver-pro/flow.html?_flowId=viewReportFlow&reportUnit=/KANA_Reporting/du_Jasper_Studio_Reporting/reports/du_Agent_Performance"}
INSERT INTO CR_REPORT (ID,REPORT_NAME,REPORT_TYPE,IS_AGENT_DEPENDED,ICON_PATH,RELEASE_ID,ENV_ID,MENU_ITEM_ID,MENU_ITEM_ENV_ID,REPORT_URL,IS_DELETED) VALUES 
(
	@RPRT.AgentPerformance,
	'AgentPerformance',
	'R',
	'Y',
	'/CoreReports/UI/Images/chart_column',
	@RELEASE.ID,
	@ENV.Dflt,
	@MNI.ChatReports,
	@ENV.Dflt,
	'<JASPER_UI_URL>/jasperserver-pro/flow.html?_flowId=viewReportFlow&reportUnit=/KANA_Reporting/du_Jasper_Studio_Reporting/reports/du_Agent_Performance',
	'N'
);

INSERT INTO CR_REPORT_LOC (ID, LOCALE, DISPLAY_NAME, DESCRIPTION, RELEASE_ID)
VALUES (
	@RPRT.AgentPerformance,
	'en-GB',
	'Agent Performance',
	'Displays an overview of chat performance for agents along with their availability durations.',
	@RELEASE.ID
);
