{% set __report_display_name = report_display_name %}
{% set report_keyname = report_display_name.replace(" ","") %}
{% set report_desc_sample = "Sample report description:\nDisplays an overview of chat performance for agents along with their availability durations." %}
{% set __report_description =report_description | print(report_desc_sample) %}
INSERT INTO CR_REPORT (ID,REPORT_NAME,REPORT_TYPE,IS_AGENT_DEPENDED,ICON_PATH,RELEASE_ID,ENV_ID,MENU_ITEM_ID,MENU_ITEM_ENV_ID,REPORT_URL,IS_DELETED) VALUES 
(
	@RPRT.{{report_keyname}},
	'{{report_keyname}}',
	'R',
	'Y',
	'/CoreReports/UI/Images/chart_column',
	@RELEASE.ID,
	@ENV.Dflt,
	@MNI.{{report_menu_keyname | suggest(_keynames.MNI)}},
	@ENV.Dflt,
	{% set report_url_help_message = "This is a sample of a URL:\n <JASPER_UI_URL>/jasperserver-pro/flow.html?_flowId=viewReportFlow&reportUnit=/KANA_Reporting/du_Jasper_Studio_Reporting/reports/du_Agent_Performance" %}
	{% set __report_url = report_url | print(report_url_help_message) %}
	'{{__report_url}}',
	'N'
);

INSERT INTO CR_REPORT_LOC (ID, LOCALE, DISPLAY_NAME, DESCRIPTION, RELEASE_ID)
VALUES (
	@RPRT.{{report_keyname}},
	'en-GB',
	'{{__report_display_name}}',
	'{{__report_description}}',
	@RELEASE.ID
);
