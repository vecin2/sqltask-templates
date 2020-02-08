from sql_gen.database.sqlparser import SQLParser
from sql_gen.app_project import AppProject
from sql_gen.database.sqlparser import SQLParser, RelativeIdLoader
import sqlparse


def test_rendering_add_activity_to_perspective_matches_expected_sql():
    expected=("UPDATE EVA_CONTEXT_VERB_ENTRY\n"
	"SET (SEQUENCE_NUMBER) = (1)\n"
	"where CONFIG_ID = @CC.Home;\n"
	"\n"
	"INSERT INTO EVA_CONTEXT_VERB_ENTRY (CONFIG_ID,CONFIG_ENV_ID,VERB,ENTITY_DEF_TYPE_ID,ENTITY_DEF_TYPE_ENV_ID,SEQUENCE_NUMBER,RELEASE_ID)\n"
	"VALUES (\n"
	"	 @CC.Home, @ENV.Dflt, 'inlineCreate', @ET.Customer, @ENV.Dflt, 1, @RELEASE.ID  );")
    sqlparser =SQLParser()
    expected =sqlparser.parse_assertable_statements(expected)
    
    actual=("--update all sequence_numbers to 1 so they display in alphabetical order\n"
	"UPDATE EVA_CONTEXT_VERB_ENTRY\n"
	"SET (SEQUENCE_NUMBER) = (1)\n"
	"where CONFIG_ID = @CC.Home;\n"
	"\n"
	"--inserting new activity in specific sequence no\n"
	"INSERT INTO EVA_CONTEXT_VERB_ENTRY (CONFIG_ID,CONFIG_ENV_ID,VERB,ENTITY_DEF_TYPE_ID,ENTITY_DEF_TYPE_ENV_ID,SEQUENCE_NUMBER,RELEASE_ID) \n"
	"VALUES (\n"
	"	 @CC.Home,--config_id\n"
	"  	 @ENV.Dflt, --config_env_id\n"
	"  	 'inlineCreate', --verbname\n"
	"  	 @ET.Customer, --entity_type\n"
	"  	 @ENV.Dflt, --entity_def_type_env_id\n"
	"  	 1, --sequence_number\n"
	"  	 @RELEASE.ID --release_id\n"
	"       );")
    actual =sqlparser.parse_assertable_statements(actual)
    
    assert expected == actual

def test_add_activity_to_perspective_runs_succesfully():
    query=("UPDATE EVA_CONTEXT_VERB_ENTRY\n"
	"SET (SEQUENCE_NUMBER) = (1)\n"
	"where CONFIG_ID = @CC.Home;\n"
	"\n"
	"INSERT INTO EVA_CONTEXT_VERB_ENTRY (CONFIG_ID,CONFIG_ENV_ID,VERB,ENTITY_DEF_TYPE_ID,ENTITY_DEF_TYPE_ENV_ID,SEQUENCE_NUMBER,RELEASE_ID)\n"
	"VALUES (\n"
	"	 @CC.Home, @ENV.Dflt, 'inlineCreate', @ET.Customer, @ENV.Dflt, 1, @RELEASE.ID  );")
    emprj_path=("/mnt/c/em//projects/pacificorp")
    app_project = AppProject(emprj_path=emprj_path)
    sqlparser =SQLParser(RelativeIdLoader())
    app_project.addb.execute(query,sqlparser=sqlparser)

def test_rendering_add_agent_for_dev_matches_expected_sql():
    expected=("INSERT INTO FU_USER (ID, USERNAME, LOCALE_ID, LOCALE_ENV_ID, IS_DELETED, VIRTUAL_ENVIRONMENT_ID, VIRTUAL_ENVIRONMENT_ENV_ID, TENANT_ID, CONTENT_LOCALE) VALUES (@USER.ccagentdemo2, 'ccagentdemo2', @LOC.en_US, 666, 'N', 1, 666, 'default', 'en-US');\n"
	"\n"
	"INSERT INTO FD_USER_PROFILE_TYPE (TENANT_ID, USER_ID, PROFILE_TYPE_ID, PROFILE_TYPE_ENV_ID, IS_DELETED) VALUES ('default', @USER.ccagentdemo2, @PROFILE.AGENT, 666, 'N');\n"
	"\n"
	"INSERT INTO CE_PERSON (ID, FIRST_NAME, FIRST_NAME_UPPER, LAST_NAME, LAST_NAME_UPPER, GENDER_ID, GENDER_ENV_ID, TITLE_ID, TITLE_ENV_ID, IS_DELETED, TENANT_ID, DO_NOT_DELETE) VALUES (@PERSON.ccagentdemo2, 'John', 'JOHN', 'Demo', 'DEMO', 0, 666, 0, 666, 'N', 'default', 'N');\n"
	"\n"
	"INSERT INTO CE_AGENT (ID, USER_ID, TENANT_ID, ORG_REALM_ID) VALUES (@PERSON.ccagentdemo2, @USER.ccagentdemo2, 'default', 'organisat');\n"
	"\n"
	"INSERT INTO AGENT (USERNAME,PASSWORD,FULLNAME,EXPIRES,PERSON_ID,CONNECTON,DISABLED,GRACE,CREATED,ALLOWCONCURRENT,CONSISTENTIPONLY,LOGINFAILURES,LASTLOGGEDIN,SALT,ENCRYPTION_CLASSNAME,EXTERNALLY_AUTHENTICATED,TENANT_ID)\n"
	"VALUES ('ccagentdemo2','0ef489f','John Demo',TO_DATE('12/15/2075','MM/DD/YYYY'),@USER.ccagentdemo2,1,'no',0,TO_DATE('12/15/2015','MM/DD/YYYY'),1,'no',0,CURRENT_DATE,'wkhvmgQLLhY=','com.gtnet.common.security.algorithms.SHA256','no','default');\n"
	"\n"
	"update agent\n"
	"set PASSWORD = (select PASSWORD from AGENT where username ='admin'),\n"
	" SALT = (select SALT from agent where username = 'admin'),\n"
	" EXPIRES = (select EXPIRES from AGENT where USERNAME = 'admin'),\n"
	" DISABLED ='no',\n"
	" LASTLOGGEDIN = SYSDATE\n"
	"where USERNAME in ('ccagentdemo2');")
    sqlparser =SQLParser()
    expected =sqlparser.parse_assertable_statements(expected)
    
    actual=("--creates an agent with the same password as 'admin' user\n"
	"INSERT INTO FU_USER (ID, USERNAME, LOCALE_ID, LOCALE_ENV_ID, IS_DELETED, VIRTUAL_ENVIRONMENT_ID, VIRTUAL_ENVIRONMENT_ENV_ID, TENANT_ID, CONTENT_LOCALE) VALUES (@USER.ccagentdemo2, 'ccagentdemo2', @LOC.en_US, 666, 'N', 1, 666, 'default', 'en-US');\n"
	"\n"
	"INSERT INTO FD_USER_PROFILE_TYPE (TENANT_ID, USER_ID, PROFILE_TYPE_ID, PROFILE_TYPE_ENV_ID, IS_DELETED)\n"
	"VALUES ('default',\n"
	"        @USER.ccagentdemo2, \n"
	"        @PROFILE.AGENT, 666, 'N');\n"
	"\n"
	"INSERT INTO CE_PERSON (ID, FIRST_NAME, FIRST_NAME_UPPER, LAST_NAME, LAST_NAME_UPPER, GENDER_ID, GENDER_ENV_ID, TITLE_ID, TITLE_ENV_ID, IS_DELETED, TENANT_ID, DO_NOT_DELETE) VALUES (@PERSON.ccagentdemo2, 'John', 'JOHN', 'Demo', 'DEMO', 0, 666, 0, 666, 'N', 'default', 'N');\n"
	"\n"
	"INSERT INTO CE_AGENT (ID, USER_ID, TENANT_ID, ORG_REALM_ID) VALUES (@PERSON.ccagentdemo2, @USER.ccagentdemo2, 'default', 'organisat');\n"
	"\n"
	"INSERT INTO AGENT (USERNAME,PASSWORD,FULLNAME,EXPIRES,PERSON_ID,CONNECTON,DISABLED,GRACE,CREATED,ALLOWCONCURRENT,CONSISTENTIPONLY,LOGINFAILURES,LASTLOGGEDIN,SALT,ENCRYPTION_CLASSNAME,EXTERNALLY_AUTHENTICATED,TENANT_ID) \n"
	"VALUES ('ccagentdemo2','0ef489f','John Demo',TO_DATE('12/15/2075','MM/DD/YYYY'),@USER.ccagentdemo2,1,'no',0,TO_DATE('12/15/2015','MM/DD/YYYY'),1,'no',0,CURRENT_DATE,'wkhvmgQLLhY=','com.gtnet.common.security.algorithms.SHA256','no','default');\n"
	"\n"
	"--update agent password\n"
	"update agent\n"
	"set PASSWORD = (select PASSWORD from AGENT where username ='admin'),\n"
	" SALT = (select SALT from agent where username = 'admin'),\n"
	" EXPIRES = (select EXPIRES from AGENT where USERNAME = 'admin'),\n"
	" DISABLED ='no',\n"
	" LASTLOGGEDIN = SYSDATE\n"
	"where USERNAME in ('ccagentdemo2');\n"
	"\n"
	"\n"
	"--This script is run against the reporting schema when an agent is added via the admin screens and is left here for reference\n"
	"--INSERT INTO DIM_AGENT (TENANT_ID, ID, USERNAME, FIRST_NAME, LAST_NAME, PARENT_AGENT_ID) VALUES ('default', 2, 'ccdev', 'Mark', 'Johson', 1000000).")
    actual =sqlparser.parse_assertable_statements(actual)
    
    assert expected == actual

def test_add_agent_for_dev_runs_succesfully():
    query=("INSERT INTO FU_USER (ID, USERNAME, LOCALE_ID, LOCALE_ENV_ID, IS_DELETED, VIRTUAL_ENVIRONMENT_ID, VIRTUAL_ENVIRONMENT_ENV_ID, TENANT_ID, CONTENT_LOCALE) VALUES (@USER.ccagentdemo2, 'ccagentdemo2', @LOC.en_US, 666, 'N', 1, 666, 'default', 'en-US');\n"
	"\n"
	"INSERT INTO FD_USER_PROFILE_TYPE (TENANT_ID, USER_ID, PROFILE_TYPE_ID, PROFILE_TYPE_ENV_ID, IS_DELETED) VALUES ('default', @USER.ccagentdemo2, @PROFILE.AGENT, 666, 'N');\n"
	"\n"
	"INSERT INTO CE_PERSON (ID, FIRST_NAME, FIRST_NAME_UPPER, LAST_NAME, LAST_NAME_UPPER, GENDER_ID, GENDER_ENV_ID, TITLE_ID, TITLE_ENV_ID, IS_DELETED, TENANT_ID, DO_NOT_DELETE) VALUES (@PERSON.ccagentdemo2, 'John', 'JOHN', 'Demo', 'DEMO', 0, 666, 0, 666, 'N', 'default', 'N');\n"
	"\n"
	"INSERT INTO CE_AGENT (ID, USER_ID, TENANT_ID, ORG_REALM_ID) VALUES (@PERSON.ccagentdemo2, @USER.ccagentdemo2, 'default', 'organisat');\n"
	"\n"
	"INSERT INTO AGENT (USERNAME,PASSWORD,FULLNAME,EXPIRES,PERSON_ID,CONNECTON,DISABLED,GRACE,CREATED,ALLOWCONCURRENT,CONSISTENTIPONLY,LOGINFAILURES,LASTLOGGEDIN,SALT,ENCRYPTION_CLASSNAME,EXTERNALLY_AUTHENTICATED,TENANT_ID)\n"
	"VALUES ('ccagentdemo2','0ef489f','John Demo',TO_DATE('12/15/2075','MM/DD/YYYY'),@USER.ccagentdemo2,1,'no',0,TO_DATE('12/15/2015','MM/DD/YYYY'),1,'no',0,CURRENT_DATE,'wkhvmgQLLhY=','com.gtnet.common.security.algorithms.SHA256','no','default');\n"
	"\n"
	"update agent\n"
	"set PASSWORD = (select PASSWORD from AGENT where username ='admin'),\n"
	" SALT = (select SALT from agent where username = 'admin'),\n"
	" EXPIRES = (select EXPIRES from AGENT where USERNAME = 'admin'),\n"
	" DISABLED ='no',\n"
	" LASTLOGGEDIN = SYSDATE\n"
	"where USERNAME in ('ccagentdemo2');")
    emprj_path=("/mnt/c/em//projects/pacificorp")
    app_project = AppProject(emprj_path=emprj_path)
    sqlparser =SQLParser(RelativeIdLoader())
    app_project.addb.execute(query,sqlparser=sqlparser)

def test_rendering_add_category_matches_expected_sql():
    expected=("INSERT INTO EVA_CATEGORY (ID,ENV_ID,PARENT_CATEGORY_ID,PARENT_CATEGORY_ENV_ID,ENTITY_DEF_ID,ENTITY_DEF_ENV_ID,RELEASE_ID,SYSTEM_NAME)\n"
	"VALUES (\n"
	"	@EC.Finance, @ENV.Dflt, @EC.System, @ENV.Dflt, @ED.EntityDefinition, @ENV.Dflt, @RELEASE.ID,\n"
	"	'Categories->System->Finance' );\n"
	"\n"
	"INSERT INTO LOCALISED_FIELD (OBJECT_TYPE, OBJECT_INSTANCE, OBJECT_VERSION, FIELD_NAME, LOCALE, LOOKUP_LOCALE,TEXT,IS_DELETED) VALUES (\n"
	"'CategoryED', 'Categories->System->Finance', @EC.Finance, 'displayName', 'en-US', 'default', 'Finance', 'N' );\n"
	"\n"
	"INSERT INTO LOCALISED_FIELD (OBJECT_TYPE, OBJECT_INSTANCE, OBJECT_VERSION, FIELD_NAME, LOCALE, LOOKUP_LOCALE,TEXT,IS_DELETED) VALUES (\n"
	"'CategoryED', 'Categories->System->Finance', @EC.Finance, 'description', 'en-US', 'default', 'Finance', 'N' );")
    sqlparser =SQLParser()
    expected =sqlparser.parse_assertable_statements(expected)
    
    actual=("INSERT INTO EVA_CATEGORY (ID,ENV_ID,PARENT_CATEGORY_ID,PARENT_CATEGORY_ENV_ID,ENTITY_DEF_ID,ENTITY_DEF_ENV_ID,RELEASE_ID,SYSTEM_NAME)\n"
	"VALUES (\n"
	"	@EC.Finance, --ID\n"
	"	@ENV.Dflt, --ENV_ID\n"
	"	@EC.System, --PARENT_CATEGORY_ID\n"
	"	@ENV.Dflt, --PARENT_CATEGORY_ENV_ID\n"
	"	@ED.EntityDefinition, --ENTITY_DEF_ID\n"
	"	@ENV.Dflt, --ENTITY_DEF_ENV_ID\n"
	"	@RELEASE.ID,\n"
	"	'Categories->System->Finance' --SYSTEM_NAME\n"
	"       );\n"
	"\n"
	"\n"
	"INSERT INTO LOCALISED_FIELD (OBJECT_TYPE, OBJECT_INSTANCE, OBJECT_VERSION, FIELD_NAME, LOCALE, LOOKUP_LOCALE,TEXT,IS_DELETED) VALUES (\n"
	"'CategoryED', -- OBJECT_TYPE\n"
	"'Categories->System->Finance', -- OBJECT_INSTANCE\n"
	"@EC.Finance, -- OBJECT_VERSION\n"
	"'displayName', -- FIELD_NAME\n"
	"'en-US', -- LOCALE\n"
	"'default', -- LOOKUP_LOCALE\n"
	"'Finance', --TEXT\n"
	"'N' --IS_DELETED\n"
	");\n"
	"\n"
	"\n"
	"INSERT INTO LOCALISED_FIELD (OBJECT_TYPE, OBJECT_INSTANCE, OBJECT_VERSION, FIELD_NAME, LOCALE, LOOKUP_LOCALE,TEXT,IS_DELETED) VALUES (\n"
	"'CategoryED', -- OBJECT_TYPE\n"
	"'Categories->System->Finance', -- OBJECT_INSTANCE\n"
	"@EC.Finance, -- OBJECT_VERSION\n"
	"'description', -- FIELD_NAME\n"
	"'en-US', -- LOCALE\n"
	"'default', -- LOOKUP_LOCALE\n"
	"'Finance', --TEXT\n"
	"'N' --IS_DELETED\n"
	");\n"
	"")
    actual =sqlparser.parse_assertable_statements(actual)
    
    assert expected == actual

def test_add_category_runs_succesfully():
    query=("INSERT INTO EVA_CATEGORY (ID,ENV_ID,PARENT_CATEGORY_ID,PARENT_CATEGORY_ENV_ID,ENTITY_DEF_ID,ENTITY_DEF_ENV_ID,RELEASE_ID,SYSTEM_NAME)\n"
	"VALUES (\n"
	"	@EC.Finance, @ENV.Dflt, @EC.System, @ENV.Dflt, @ED.EntityDefinition, @ENV.Dflt, @RELEASE.ID,\n"
	"	'Categories->System->Finance' );\n"
	"\n"
	"INSERT INTO LOCALISED_FIELD (OBJECT_TYPE, OBJECT_INSTANCE, OBJECT_VERSION, FIELD_NAME, LOCALE, LOOKUP_LOCALE,TEXT,IS_DELETED) VALUES (\n"
	"'CategoryED', 'Categories->System->Finance', @EC.Finance, 'displayName', 'en-US', 'default', 'Finance', 'N' );\n"
	"\n"
	"INSERT INTO LOCALISED_FIELD (OBJECT_TYPE, OBJECT_INSTANCE, OBJECT_VERSION, FIELD_NAME, LOCALE, LOOKUP_LOCALE,TEXT,IS_DELETED) VALUES (\n"
	"'CategoryED', 'Categories->System->Finance', @EC.Finance, 'description', 'en-US', 'default', 'Finance', 'N' );")
    emprj_path=("/mnt/c/em//projects/pacificorp")
    app_project = AppProject(emprj_path=emprj_path)
    sqlparser =SQLParser(RelativeIdLoader())
    app_project.addb.execute(query,sqlparser=sqlparser)

def test_rendering_add_content_type_matches_expected_sql():
    expected=("INSERT INTO AKCB_CONTENT_TYPE (ID,ENV_ID,RELEASE_ID,SYSTEM_NAME,DEFAULT_CATEGORY_NAME,ENTITY_DEF_TYPE_ID,ENTITY_DEF_TYPE_ENV_ID,RELATIVE_URL,IS_DELETED,PREFIX,TENANT_ID)\n"
	"VALUES (@AKCBCT.MyInfo, @ENV.Dflt, @RELEASE.ID, 'KnowledgeMyInfoED', 'content_myinfo', @ED.Content, @ENV.Dflt, 'live.kana.com?:ws/', 'N', 'KM', 'default');\n"
	"INSERT INTO AKCB_CONTENT_TYPE_LOC (ID,ENV_ID,RELEASE_ID,LOCALE,DISPLAY_NAME,DESCRIPTION,TENANT_ID)\n"
	"VALUES (@AKCBCT.MyInfo, @ENV.Dflt, @RELEASE.ID, 'en-US',\n"
	"	'MyInfo',\n"
	"	'MyInfo',\n"
	"	'default');\n"
	"\n"
	"INSERT INTO AKCB_CONTENT_CATEGORY (ID,ENV_ID,RELEASE_ID,SYSTEM_NAME,SMALL_ICON_CLASS,LARGE_ICON_CLASS,ICON_CLASS,TENANT_ID)\n"
	"VALUES (@AKCBCC.MyInfo, @ENV.Dflt, @RELEASE.ID, 'content_myinfo', 'knowledgeCategoryIcon iconSmall iconMyInfo', 'knowledgeCategoryIcon iconLarge iconMyInfo', 'tabIconMyInfo', 'default');\n"
	"\n"
	"INSERT INTO AKI_INDEX_CONTENT_TYPE (ID,ENV_ID,TYPE_NAME,ENTITY_DEF_TYPE_ID,ENTITY_DEF_TYPE_ENV_ID,RELEASE_ID,TENANT_ID)\n"
	"VALUES (@AKIT.KnowledgeMyInfoED,\n"
	"	@ENV.Dflt, 'KnowledgeMyInfoED', @ED.ContentAuthoringWorkItem,\n"
	"	@ENV.Dflt, @RELEASE.ID, 'default');")
    sqlparser =SQLParser()
    expected =sqlparser.parse_assertable_statements(expected)
    
    actual=("INSERT INTO AKCB_CONTENT_TYPE (ID,ENV_ID,RELEASE_ID,SYSTEM_NAME,DEFAULT_CATEGORY_NAME,ENTITY_DEF_TYPE_ID,ENTITY_DEF_TYPE_ENV_ID,RELATIVE_URL,IS_DELETED,PREFIX,TENANT_ID) \n"
	"VALUES (@AKCBCT.MyInfo, --ID\n"
	"	@ENV.Dflt, --ENV_ID\n"
	"	@RELEASE.ID, --RELEASE_ID\n"
	"	'KnowledgeMyInfoED',--SYSTEM_NAME\n"
	"	'content_myinfo', --DEFAULT_CATEGORY_NAME\n"
	"	@ED.Content,--ENTITY_DEF_TYPE_ID\n"
	"	@ENV.Dflt, --ENTITY_DEF_TYPE_ENV_ID\n"
	"	'live.kana.com?:ws/', --RELATIVE_URL\n"
	"	'N',--IS_DELETED\n"
	"	'KM',--PREFIX\n"
	"	'default'--TENANT_ID\n"
	");\n"
	"INSERT INTO AKCB_CONTENT_TYPE_LOC (ID,ENV_ID,RELEASE_ID,LOCALE,DISPLAY_NAME,DESCRIPTION,TENANT_ID)\n"
	"VALUES (@AKCBCT.MyInfo, --ID\n"
	"	@ENV.Dflt, --ENV_ID\n"
	"	@RELEASE.ID, --RELEASE_ID\n"
	"	'en-US',\n"
	"	'MyInfo',\n"
	"	'MyInfo',\n"
	"	'default');\n"
	"\n"
	"INSERT INTO AKCB_CONTENT_CATEGORY (ID,ENV_ID,RELEASE_ID,SYSTEM_NAME,SMALL_ICON_CLASS,LARGE_ICON_CLASS,ICON_CLASS,TENANT_ID)\n"
	"VALUES (@AKCBCC.MyInfo, --ID\n"
	"	@ENV.Dflt, --ENV_ID\n"
	"	@RELEASE.ID, --RELEASE_ID\n"
	"	'content_myinfo', --SYSTEM_NAME\n"
	"	'knowledgeCategoryIcon iconSmall iconMyInfo', --SMALL_ICON_CLASS\n"
	"	'knowledgeCategoryIcon iconLarge iconMyInfo', --LARGE_ICON_CLASS\n"
	"	'tabIconMyInfo',--ICON_CLASS\n"
	"	'default');\n"
	"\n"
	"INSERT INTO AKI_INDEX_CONTENT_TYPE (ID,ENV_ID,TYPE_NAME,ENTITY_DEF_TYPE_ID,ENTITY_DEF_TYPE_ENV_ID,RELEASE_ID,TENANT_ID) \n"
	"VALUES (@AKIT.KnowledgeMyInfoED,\n"
	"	@ENV.Dflt, --ENV_ID\n"
	"	'KnowledgeMyInfoED',--TYPE_NAME\n"
	"	@ED.ContentAuthoringWorkItem,\n"
	"	@ENV.Dflt, --ENTITY_DEF_TYPE_ENV_ID\n"
	"	@RELEASE.ID, --RELEASE_ID\n"
	"	'default');\n"
	"")
    actual =sqlparser.parse_assertable_statements(actual)
    
    assert expected == actual

def test_add_content_type_runs_succesfully():
    query=("INSERT INTO AKCB_CONTENT_TYPE (ID,ENV_ID,RELEASE_ID,SYSTEM_NAME,DEFAULT_CATEGORY_NAME,ENTITY_DEF_TYPE_ID,ENTITY_DEF_TYPE_ENV_ID,RELATIVE_URL,IS_DELETED,PREFIX,TENANT_ID)\n"
	"VALUES (@AKCBCT.MyInfo, @ENV.Dflt, @RELEASE.ID, 'KnowledgeMyInfoED', 'content_myinfo', @ED.Content, @ENV.Dflt, 'live.kana.com?:ws/', 'N', 'KM', 'default');\n"
	"INSERT INTO AKCB_CONTENT_TYPE_LOC (ID,ENV_ID,RELEASE_ID,LOCALE,DISPLAY_NAME,DESCRIPTION,TENANT_ID)\n"
	"VALUES (@AKCBCT.MyInfo, @ENV.Dflt, @RELEASE.ID, 'en-US',\n"
	"	'MyInfo',\n"
	"	'MyInfo',\n"
	"	'default');\n"
	"\n"
	"INSERT INTO AKCB_CONTENT_CATEGORY (ID,ENV_ID,RELEASE_ID,SYSTEM_NAME,SMALL_ICON_CLASS,LARGE_ICON_CLASS,ICON_CLASS,TENANT_ID)\n"
	"VALUES (@AKCBCC.MyInfo, @ENV.Dflt, @RELEASE.ID, 'content_myinfo', 'knowledgeCategoryIcon iconSmall iconMyInfo', 'knowledgeCategoryIcon iconLarge iconMyInfo', 'tabIconMyInfo', 'default');\n"
	"\n"
	"INSERT INTO AKI_INDEX_CONTENT_TYPE (ID,ENV_ID,TYPE_NAME,ENTITY_DEF_TYPE_ID,ENTITY_DEF_TYPE_ENV_ID,RELEASE_ID,TENANT_ID)\n"
	"VALUES (@AKIT.KnowledgeMyInfoED,\n"
	"	@ENV.Dflt, 'KnowledgeMyInfoED', @ED.ContentAuthoringWorkItem,\n"
	"	@ENV.Dflt, @RELEASE.ID, 'default');")
    emprj_path=("/mnt/c/em//projects/pacificorp")
    app_project = AppProject(emprj_path=emprj_path)
    sqlparser =SQLParser(RelativeIdLoader())
    app_project.addb.execute(query,sqlparser=sqlparser)

def test_rendering_add_dynamic_content_verb_matches_expected_sql():
    expected=("INSERT INTO EVA_PROCESS_DESCRIPTOR (ID, ENV_ID, NAME, REPOSITORY_PATH, CONFIG_PROCESS_ID, IS_DELETED,TYPE) VALUES (\n"
	"@PD.DynamicContentCaseCreateInfo2, @ENV.Dflt, 'DynamicContentCaseCreateInfo2', 'AddKnowContentCase.Implementation.DynamicContentCase.Verbs.Create', NULL, 'N', @PDT.Verb  );\n"
	"\n"
	"INSERT INTO LOCALISED_FIELD (OBJECT_TYPE, OBJECT_INSTANCE, OBJECT_VERSION, FIELD_NAME, LOCALE, LOOKUP_LOCALE,TEXT,IS_DELETED) VALUES (\n"
	"'ProcessDescriptorED', 'DynamicContentCaseCreateInfo2__AddKnowContentCase/Implementation/DynamicContentCase/Verbs/Create', @PD.DynamicContentCaseCreateInfo2, 'displayName', 'en-US', 'default', 'DynamicContentCaseCreateInfo2', 'N'\n"
	");\n"
	"\n"
	"INSERT INTO LOCALISED_FIELD (OBJECT_TYPE, OBJECT_INSTANCE, OBJECT_VERSION, FIELD_NAME, LOCALE, LOOKUP_LOCALE,TEXT,IS_DELETED) VALUES (\n"
	"'ProcessDescriptorED', 'DynamicContentCaseCreateInfo2__AddKnowContentCase/Implementation/DynamicContentCase/Verbs/Create', @PD.DynamicContentCaseCreateInfo2, 'description', 'en-US', 'default', 'DynamicContentCaseCreateInfo2', 'N'\n"
	");\n"
	"\n"
	"INSERT INTO EVA_PROCESS_DESC_REFERENCE (ID, PROCESS_DESCRIPTOR_ID, PROCESS_DESCRIPTOR_ENV_ID, CONFIG_ID, IS_SHARED) VALUES (\n"
	"@PDR.DynamicContentCaseCreateInfo2, @PD.DynamicContentCaseCreateInfo2, @ENV.Dflt, @ED.KnowledgeArticle, 'N' );\n"
	"\n"
	"INSERT INTO EVA_VERB (ID, NAME, PROCESS_DESC_REF_ID, ENTITY_DEF_ID, ENTITY_DEF_ENV_ID, IS_INSTANCE, IS_DEFAULT, IS_INSTANCE_DEFAULT, IS_USER_VISIBLE) VALUES (\n"
	"@V.DynamicContentCaseCreateInfo2, 'createInfo2', @PDR.DynamicContentCaseCreateInfo2, @ED.DynamicContentCase, @ENV.Dflt, 'N', 'N', 'N', 'Y' );\n"
	"\n"
	"INSERT INTO LOCALISED_FIELD (OBJECT_TYPE, OBJECT_INSTANCE, OBJECT_VERSION, FIELD_NAME, LOCALE, LOOKUP_LOCALE,TEXT,IS_DELETED) VALUES (\n"
	"'VerbED', 'DynamicContentCaseED__createInfo2', @V.DynamicContentCaseCreateInfo2, 'displayName', 'en-US', 'default', 'Info', 'N'\n"
	");\n"
	"\n"
	"INSERT INTO LOCALISED_FIELD (OBJECT_TYPE, OBJECT_INSTANCE, OBJECT_VERSION, FIELD_NAME, LOCALE, LOOKUP_LOCALE,TEXT,IS_DELETED) VALUES (\n"
	"'VerbED', 'DynamicContentCaseED__createInfo2', @V.DynamicContentCaseCreateInfo2, 'description', 'en-US', 'default', 'Create Info 2', 'N'\n"
	");\n"
	"\n"
	"UPDATE EVA_CONTEXT_VERB_ENTRY\n"
	"SET (SEQUENCE_NUMBER) = (1)\n"
	"where CONFIG_ID = @CC.KMAuthoringHome;\n"
	"\n"
	"INSERT INTO EVA_CONTEXT_VERB_ENTRY (CONFIG_ID,CONFIG_ENV_ID,VERB,ENTITY_DEF_TYPE_ID,ENTITY_DEF_TYPE_ENV_ID,SEQUENCE_NUMBER,RELEASE_ID)\n"
	"VALUES (\n"
	"	 @CC.KMAuthoringHome, @ENV.Dflt, 'createInfo2', @ET.DynamicContentCase, @ENV.Dflt, 1, @RELEASE.ID  );")
    sqlparser =SQLParser()
    expected =sqlparser.parse_assertable_statements(expected)
    
    actual=("\n"
	"\n"
	"\n"
	"INSERT INTO EVA_PROCESS_DESCRIPTOR (ID, ENV_ID, NAME, REPOSITORY_PATH, CONFIG_PROCESS_ID, IS_DELETED, TYPE)\n"
	"VALUES (\n"
	"	 @PD.DynamicContentCaseCreateInfo2, --id\n"
	"	 @ENV.Dflt, --env_id,\n"
	"	 'DynamicContentCaseCreateInfo2', --process_descriptor_name\n"
	"	 'AddKnowContentCase.Implementation.DynamicContentCase.Verbs.Create', --repository_path\n"
	"	 NULL, --config_id\n"
	"	 'N', --is_deleted\n"
	"	 @PDT.Verb --type\n"
	"       );\n"
	"\n"
	"INSERT INTO LOCALISED_FIELD (OBJECT_TYPE, OBJECT_INSTANCE, OBJECT_VERSION, FIELD_NAME, LOCALE, LOOKUP_LOCALE,TEXT,IS_DELETED) VALUES (\n"
	"'ProcessDescriptorED', -- OBJECT_TYPE\n"
	"'DynamicContentCaseCreateInfo2__AddKnowContentCase/Implementation/DynamicContentCase/Verbs/Create', -- OBJECT_INSTANCE\n"
	"@PD.DynamicContentCaseCreateInfo2, -- OBJECT_VERSION\n"
	"'displayName', -- FIELD_NAME\n"
	"'en-US', -- LOCALE\n"
	"'default', -- LOOKUP_LOCALE\n"
	"'DynamicContentCaseCreateInfo2', --TEXT\n"
	"'N' --IS_DELETED\n"
	");\n"
	"\n"
	"\n"
	"INSERT INTO LOCALISED_FIELD (OBJECT_TYPE, OBJECT_INSTANCE, OBJECT_VERSION, FIELD_NAME, LOCALE, LOOKUP_LOCALE,TEXT,IS_DELETED) VALUES (\n"
	"'ProcessDescriptorED', -- OBJECT_TYPE\n"
	"'DynamicContentCaseCreateInfo2__AddKnowContentCase/Implementation/DynamicContentCase/Verbs/Create', -- OBJECT_INSTANCE\n"
	"@PD.DynamicContentCaseCreateInfo2, -- OBJECT_VERSION\n"
	"'description', -- FIELD_NAME\n"
	"'en-US', -- LOCALE\n"
	"'default', -- LOOKUP_LOCALE\n"
	"'DynamicContentCaseCreateInfo2', --TEXT\n"
	"'N' --IS_DELETED\n"
	");\n"
	"\n"
	"\n"
	"\n"
	"INSERT INTO EVA_PROCESS_DESC_REFERENCE (ID, PROCESS_DESCRIPTOR_ID, PROCESS_DESCRIPTOR_ENV_ID, CONFIG_ID, IS_SHARED) \n"
	"VALUES (\n"
	"        @PDR.DynamicContentCaseCreateInfo2, --id\n"
	"        @PD.DynamicContentCaseCreateInfo2, --process_descriptor_id\n"
	"	@ENV.Dflt, --process_descriptor_env_id\n"
	"	@ED.KnowledgeArticle, --config_id\n"
	"       	'N' --is_shared\n"
	"       );\n"
	"\n"
	"\n"
	"\n"
	"INSERT INTO EVA_VERB (ID, NAME, PROCESS_DESC_REF_ID, ENTITY_DEF_ID, ENTITY_DEF_ENV_ID, IS_INSTANCE, IS_DEFAULT, IS_INSTANCE_DEFAULT, IS_USER_VISIBLE) VALUES (\n"
	"@V.DynamicContentCaseCreateInfo2, --ID\n"
	"'createInfo2', -- NAME\n"
	"@PDR.DynamicContentCaseCreateInfo2, --PROCESS_DESC_REF_ID\n"
	"@ED.DynamicContentCase, -- ENTITY_DEF_ID\n"
	"@ENV.Dflt, -- ENTITY_DEF_ENV_ID\n"
	"'N', --IS_INSTANCE\n"
	"'N', -- IS_DEFAULT\n"
	"  'N', -- IS_INSTANCE_DEFAULT\n"
	" \n"
	"'Y' -- IS_USER_VISIBLE\n"
	");\n"
	"\n"
	"INSERT INTO LOCALISED_FIELD (OBJECT_TYPE, OBJECT_INSTANCE, OBJECT_VERSION, FIELD_NAME, LOCALE, LOOKUP_LOCALE,TEXT,IS_DELETED) VALUES (\n"
	"'VerbED', -- OBJECT_TYPE\n"
	"'DynamicContentCaseED__createInfo2', -- OBJECT_INSTANCE\n"
	"@V.DynamicContentCaseCreateInfo2, -- OBJECT_VERSION\n"
	"'displayName', -- FIELD_NAME\n"
	"'en-US', -- LOCALE\n"
	"'default', -- LOOKUP_LOCALE\n"
	"'Info', --TEXT\n"
	"'N' --IS_DELETED\n"
	");\n"
	"\n"
	"\n"
	"INSERT INTO LOCALISED_FIELD (OBJECT_TYPE, OBJECT_INSTANCE, OBJECT_VERSION, FIELD_NAME, LOCALE, LOOKUP_LOCALE,TEXT,IS_DELETED) VALUES (\n"
	"'VerbED', -- OBJECT_TYPE\n"
	"'DynamicContentCaseED__createInfo2', -- OBJECT_INSTANCE\n"
	"@V.DynamicContentCaseCreateInfo2, -- OBJECT_VERSION\n"
	"'description', -- FIELD_NAME\n"
	"'en-US', -- LOCALE\n"
	"'default', -- LOOKUP_LOCALE\n"
	"'Create Info 2', --TEXT\n"
	"'N' --IS_DELETED\n"
	");\n"
	"\n"
	"\n"
	"\n"
	"--update all sequence_numbers to 1 so they display in alphabetical order\n"
	"UPDATE EVA_CONTEXT_VERB_ENTRY\n"
	"SET (SEQUENCE_NUMBER) = (1)\n"
	"where CONFIG_ID = @CC.KMAuthoringHome;\n"
	"\n"
	"--inserting new activity in specific sequence no\n"
	"INSERT INTO EVA_CONTEXT_VERB_ENTRY (CONFIG_ID,CONFIG_ENV_ID,VERB,ENTITY_DEF_TYPE_ID,ENTITY_DEF_TYPE_ENV_ID,SEQUENCE_NUMBER,RELEASE_ID) \n"
	"VALUES (\n"
	"	 @CC.KMAuthoringHome,--config_id\n"
	"  	 @ENV.Dflt, --config_env_id\n"
	"  	 'createInfo2', --verbname\n"
	"  	 @ET.DynamicContentCase, --entity_type\n"
	"  	 @ENV.Dflt, --entity_def_type_env_id\n"
	"  	 1, --sequence_number\n"
	"  	 @RELEASE.ID --release_id\n"
	"       );")
    actual =sqlparser.parse_assertable_statements(actual)
    
    assert expected == actual

def test_add_dynamic_content_verb_runs_succesfully():
    query=("INSERT INTO EVA_PROCESS_DESCRIPTOR (ID, ENV_ID, NAME, REPOSITORY_PATH, CONFIG_PROCESS_ID, IS_DELETED,TYPE) VALUES (\n"
	"@PD.DynamicContentCaseCreateInfo2, @ENV.Dflt, 'DynamicContentCaseCreateInfo2', 'AddKnowContentCase.Implementation.DynamicContentCase.Verbs.Create', NULL, 'N', @PDT.Verb  );\n"
	"\n"
	"INSERT INTO LOCALISED_FIELD (OBJECT_TYPE, OBJECT_INSTANCE, OBJECT_VERSION, FIELD_NAME, LOCALE, LOOKUP_LOCALE,TEXT,IS_DELETED) VALUES (\n"
	"'ProcessDescriptorED', 'DynamicContentCaseCreateInfo2__AddKnowContentCase/Implementation/DynamicContentCase/Verbs/Create', @PD.DynamicContentCaseCreateInfo2, 'displayName', 'en-US', 'default', 'DynamicContentCaseCreateInfo2', 'N'\n"
	");\n"
	"\n"
	"INSERT INTO LOCALISED_FIELD (OBJECT_TYPE, OBJECT_INSTANCE, OBJECT_VERSION, FIELD_NAME, LOCALE, LOOKUP_LOCALE,TEXT,IS_DELETED) VALUES (\n"
	"'ProcessDescriptorED', 'DynamicContentCaseCreateInfo2__AddKnowContentCase/Implementation/DynamicContentCase/Verbs/Create', @PD.DynamicContentCaseCreateInfo2, 'description', 'en-US', 'default', 'DynamicContentCaseCreateInfo2', 'N'\n"
	");\n"
	"\n"
	"INSERT INTO EVA_PROCESS_DESC_REFERENCE (ID, PROCESS_DESCRIPTOR_ID, PROCESS_DESCRIPTOR_ENV_ID, CONFIG_ID, IS_SHARED) VALUES (\n"
	"@PDR.DynamicContentCaseCreateInfo2, @PD.DynamicContentCaseCreateInfo2, @ENV.Dflt, @ED.KnowledgeArticle, 'N' );\n"
	"\n"
	"INSERT INTO EVA_VERB (ID, NAME, PROCESS_DESC_REF_ID, ENTITY_DEF_ID, ENTITY_DEF_ENV_ID, IS_INSTANCE, IS_DEFAULT, IS_INSTANCE_DEFAULT, IS_USER_VISIBLE) VALUES (\n"
	"@V.DynamicContentCaseCreateInfo2, 'createInfo2', @PDR.DynamicContentCaseCreateInfo2, @ED.DynamicContentCase, @ENV.Dflt, 'N', 'N', 'N', 'Y' );\n"
	"\n"
	"INSERT INTO LOCALISED_FIELD (OBJECT_TYPE, OBJECT_INSTANCE, OBJECT_VERSION, FIELD_NAME, LOCALE, LOOKUP_LOCALE,TEXT,IS_DELETED) VALUES (\n"
	"'VerbED', 'DynamicContentCaseED__createInfo2', @V.DynamicContentCaseCreateInfo2, 'displayName', 'en-US', 'default', 'Info', 'N'\n"
	");\n"
	"\n"
	"INSERT INTO LOCALISED_FIELD (OBJECT_TYPE, OBJECT_INSTANCE, OBJECT_VERSION, FIELD_NAME, LOCALE, LOOKUP_LOCALE,TEXT,IS_DELETED) VALUES (\n"
	"'VerbED', 'DynamicContentCaseED__createInfo2', @V.DynamicContentCaseCreateInfo2, 'description', 'en-US', 'default', 'Create Info 2', 'N'\n"
	");\n"
	"\n"
	"UPDATE EVA_CONTEXT_VERB_ENTRY\n"
	"SET (SEQUENCE_NUMBER) = (1)\n"
	"where CONFIG_ID = @CC.KMAuthoringHome;\n"
	"\n"
	"INSERT INTO EVA_CONTEXT_VERB_ENTRY (CONFIG_ID,CONFIG_ENV_ID,VERB,ENTITY_DEF_TYPE_ID,ENTITY_DEF_TYPE_ENV_ID,SEQUENCE_NUMBER,RELEASE_ID)\n"
	"VALUES (\n"
	"	 @CC.KMAuthoringHome, @ENV.Dflt, 'createInfo2', @ET.DynamicContentCase, @ENV.Dflt, 1, @RELEASE.ID  );")
    emprj_path=("/mnt/c/em//projects/pacificorp")
    app_project = AppProject(emprj_path=emprj_path)
    sqlparser =SQLParser(RelativeIdLoader())
    app_project.addb.execute(query,sqlparser=sqlparser)

def test_rendering_add_dynamic_entity_matches_expected_sql():
    expected=("INSERT INTO EVA_ENTITY_DEFINITION (ID, ENV_ID, NAME, UUID, TYPE_UUID, TYPE_ID, TYPE_ENV_ID, LOGICAL_OBJ_PATH, INTERFACE_PATH, SUPER_ENTITY_DEFINITION, SUPER_ENTITY_DEFINITION_ENV_ID, IS_DELETED, IS_BASIC, SUPPORTS_READONLY,IS_EXPANDABLE, ICON_PATH, INSTANCE_ICON_PATH) VALUES (\n"
	"@ED.Agreement, @ENV.Dflt, 'AgreementED', 'AgreementED', 'AgreementED', @ET.Agreement, @ENV.Dflt, 'FrameworkDynamicEntities.Implementation.DynamicEntity.Objects.DynamicEntity', 'FrameworkDynamicEntities.API.EntityInterfaces.EIDynamicEntity', @ED.BaseDynamicEntity, @ENV.Dflt, 'N', 'N', 'Y', 'N', NULL, NULL );\n"
	"\n"
	"INSERT INTO EVA_CATEGORY_ENTRY(CATEGORY_ID, CATEGORY_ENV_ID, ENTITY_ID, ENTITY_ENV_ID) VALUES (\n"
	"@EC.DynamicEntity, @ENV.Dflt, @ED.Agreement, @ENV.Dflt  );\n"
	"\n"
	"INSERT INTO LOCALISED_FIELD (OBJECT_TYPE, OBJECT_INSTANCE, OBJECT_VERSION, FIELD_NAME, LOCALE, LOOKUP_LOCALE,TEXT,IS_DELETED) VALUES (\n"
	"'DynamicEntityDefinitionED', 'AgreementED', @ED.Agreement, 'displayName', 'en-US', 'default', 'Agreement', 'N' );\n"
	"\n"
	"INSERT INTO LOCALISED_FIELD (OBJECT_TYPE, OBJECT_INSTANCE, OBJECT_VERSION, FIELD_NAME, LOCALE, LOOKUP_LOCALE,TEXT,IS_DELETED) VALUES (\n"
	"'DynamicEntityDefinitionED', 'AgreementED', @ED.Agreement, 'description', 'en-US', 'default', 'Agreement Description', 'N' );\n"
	"\n"
	"INSERT INTO LOCALISED_FIELD (OBJECT_TYPE, OBJECT_INSTANCE, OBJECT_VERSION, FIELD_NAME, LOCALE, LOOKUP_LOCALE,TEXT,IS_DELETED) VALUES (\n"
	"'DynamicEntityDefinitionED', 'AgreementED', @ED.Agreement, 'summaryExpression', 'en-US', 'default', 'Article2 [title]', 'N' );\n"
	"\n"
	"INSERT INTO EVA_DYNAMIC_ENTITY_DEF (ID,ENV_ID,RELEASE_ID)\n"
	"VALUES (\n"
	"	@ED.Agreement,\n"
	"	@ENV.Dflt, @RELEASE.ID  );")
    sqlparser =SQLParser()
    expected =sqlparser.parse_assertable_statements(expected)
    
    actual=("\n"
	"INSERT INTO EVA_ENTITY_DEFINITION (ID, ENV_ID, NAME, UUID, TYPE_UUID, TYPE_ID, TYPE_ENV_ID, LOGICAL_OBJ_PATH, INTERFACE_PATH, SUPER_ENTITY_DEFINITION, SUPER_ENTITY_DEFINITION_ENV_ID, IS_DELETED, IS_BASIC, SUPPORTS_READONLY,IS_EXPANDABLE,ICON_PATH, INSTANCE_ICON_PATH) VALUES (\n"
	"@ED.Agreement, -- ID\n"
	"@ENV.Dflt, -- ENV_ID\n"
	"'AgreementED', -- NAME\n"
	"'AgreementED', -- UUID\n"
	"'AgreementED', -- TYPE_UUID\n"
	"@ET.Agreement, -- TYPE_ID\n"
	"@ENV.Dflt, -- TYPE_ENV_ID\n"
	"'FrameworkDynamicEntities.Implementation.DynamicEntity.Objects.DynamicEntity', -- LOGICAL_OBJECT_PATH\n"
	"'FrameworkDynamicEntities.API.EntityInterfaces.EIDynamicEntity', -- INTERFACE_PATH\n"
	"@ED.BaseDynamicEntity, -- SUPER_ENTITY_DEFINITION\n"
	"@ENV.Dflt, -- SUPER_ENTITY_DEFINITION_ENV_ID\n"
	"'N', -- IS_DELETED\n"
	"'N', -- IS_BASIC\n"
	"'Y', -- SUPPORTS_READ_ONLY\n"
	"'N', --IS_EXPANDABLE\n"
	"NULL, -- ICON_PATH\n"
	"NULL -- INSTANCE_ICON_PATH\n"
	");\n"
	"\n"
	"\n"
	"  INSERT INTO EVA_CATEGORY_ENTRY(CATEGORY_ID, CATEGORY_ENV_ID, ENTITY_ID, ENTITY_ENV_ID) VALUES (\n"
	"  @EC.DynamicEntity, -- CATEGORY_ID\n"
	"  @ENV.Dflt, -- CATEGORY_ENV_ID\n"
	"  @ED.Agreement, -- ENTITY_ID\n"
	"  @ENV.Dflt -- ENTITY_ENV_ID\n"
	"  );\n"
	"\n"
	"INSERT INTO LOCALISED_FIELD (OBJECT_TYPE, OBJECT_INSTANCE, OBJECT_VERSION, FIELD_NAME, LOCALE, LOOKUP_LOCALE,TEXT,IS_DELETED) VALUES (\n"
	"'DynamicEntityDefinitionED', -- OBJECT_TYPE\n"
	"'AgreementED', -- OBJECT_INSTANCE\n"
	"@ED.Agreement, -- OBJECT_VERSION\n"
	"'displayName', -- FIELD_NAME\n"
	"'en-US', -- LOCALE\n"
	"'default', -- LOOKUP_LOCALE\n"
	"'Agreement', --TEXT\n"
	"'N' --IS_DELETED\n"
	");\n"
	"\n"
	"\n"
	"INSERT INTO LOCALISED_FIELD (OBJECT_TYPE, OBJECT_INSTANCE, OBJECT_VERSION, FIELD_NAME, LOCALE, LOOKUP_LOCALE,TEXT,IS_DELETED) VALUES (\n"
	"'DynamicEntityDefinitionED', -- OBJECT_TYPE\n"
	"'AgreementED', -- OBJECT_INSTANCE\n"
	"@ED.Agreement, -- OBJECT_VERSION\n"
	"'description', -- FIELD_NAME\n"
	"'en-US', -- LOCALE\n"
	"'default', -- LOOKUP_LOCALE\n"
	"'Agreement Description', --TEXT\n"
	"'N' --IS_DELETED\n"
	");\n"
	"\n"
	"\n"
	"\n"
	"INSERT INTO LOCALISED_FIELD (OBJECT_TYPE, OBJECT_INSTANCE, OBJECT_VERSION, FIELD_NAME, LOCALE, LOOKUP_LOCALE,TEXT,IS_DELETED) VALUES (\n"
	"'DynamicEntityDefinitionED', -- OBJECT_TYPE\n"
	"'AgreementED', -- OBJECT_INSTANCE\n"
	"@ED.Agreement, -- OBJECT_VERSION\n"
	"'summaryExpression', -- FIELD_NAME\n"
	"'en-US', -- LOCALE\n"
	"'default', -- LOOKUP_LOCALE\n"
	"'Article2 [title]', --TEXT\n"
	"'N' --IS_DELETED\n"
	");\n"
	"\n"
	"\n"
	"INSERT INTO EVA_DYNAMIC_ENTITY_DEF (ID,ENV_ID,RELEASE_ID) \n"
	"VALUES (\n"
	"	@ED.Agreement,\n"
	"	@ENV.Dflt, --ENV_ID\n"
	"	@RELEASE.ID --RELEASE_ID\n"
	"	);")
    actual =sqlparser.parse_assertable_statements(actual)
    
    assert expected == actual

def test_add_dynamic_entity_runs_succesfully():
    query=("INSERT INTO EVA_ENTITY_DEFINITION (ID, ENV_ID, NAME, UUID, TYPE_UUID, TYPE_ID, TYPE_ENV_ID, LOGICAL_OBJ_PATH, INTERFACE_PATH, SUPER_ENTITY_DEFINITION, SUPER_ENTITY_DEFINITION_ENV_ID, IS_DELETED, IS_BASIC, SUPPORTS_READONLY,IS_EXPANDABLE, ICON_PATH, INSTANCE_ICON_PATH) VALUES (\n"
	"@ED.Agreement, @ENV.Dflt, 'AgreementED', 'AgreementED', 'AgreementED', @ET.Agreement, @ENV.Dflt, 'FrameworkDynamicEntities.Implementation.DynamicEntity.Objects.DynamicEntity', 'FrameworkDynamicEntities.API.EntityInterfaces.EIDynamicEntity', @ED.BaseDynamicEntity, @ENV.Dflt, 'N', 'N', 'Y', 'N', NULL, NULL );\n"
	"\n"
	"INSERT INTO EVA_CATEGORY_ENTRY(CATEGORY_ID, CATEGORY_ENV_ID, ENTITY_ID, ENTITY_ENV_ID) VALUES (\n"
	"@EC.DynamicEntity, @ENV.Dflt, @ED.Agreement, @ENV.Dflt  );\n"
	"\n"
	"INSERT INTO LOCALISED_FIELD (OBJECT_TYPE, OBJECT_INSTANCE, OBJECT_VERSION, FIELD_NAME, LOCALE, LOOKUP_LOCALE,TEXT,IS_DELETED) VALUES (\n"
	"'DynamicEntityDefinitionED', 'AgreementED', @ED.Agreement, 'displayName', 'en-US', 'default', 'Agreement', 'N' );\n"
	"\n"
	"INSERT INTO LOCALISED_FIELD (OBJECT_TYPE, OBJECT_INSTANCE, OBJECT_VERSION, FIELD_NAME, LOCALE, LOOKUP_LOCALE,TEXT,IS_DELETED) VALUES (\n"
	"'DynamicEntityDefinitionED', 'AgreementED', @ED.Agreement, 'description', 'en-US', 'default', 'Agreement Description', 'N' );\n"
	"\n"
	"INSERT INTO LOCALISED_FIELD (OBJECT_TYPE, OBJECT_INSTANCE, OBJECT_VERSION, FIELD_NAME, LOCALE, LOOKUP_LOCALE,TEXT,IS_DELETED) VALUES (\n"
	"'DynamicEntityDefinitionED', 'AgreementED', @ED.Agreement, 'summaryExpression', 'en-US', 'default', 'Article2 [title]', 'N' );\n"
	"\n"
	"INSERT INTO EVA_DYNAMIC_ENTITY_DEF (ID,ENV_ID,RELEASE_ID)\n"
	"VALUES (\n"
	"	@ED.Agreement,\n"
	"	@ENV.Dflt, @RELEASE.ID  );")
    emprj_path=("/mnt/c/em//projects/pacificorp")
    app_project = AppProject(emprj_path=emprj_path)
    sqlparser =SQLParser(RelativeIdLoader())
    app_project.addb.execute(query,sqlparser=sqlparser)

def test_rendering_add_dynamic_entity_field_matches_expected_sql():
    expected=("INSERT INTO EVA_DYNAMIC_ENTITY_FIELD (ID, ENTITY_DEF_ID, NAME, INITIAL_VALUE, FIELD_TYPE_ID, FIELD_SEQUENCE, ENTITY_DEF_ENV_ID)\n"
	"VALUES (@EDEF.KnowledgeArticleTitle2, @ED.KnowledgeArticle, 'title2', '', @EFT.StringField, 1, @ENV.Dflt);\n"
	"\n"
	"INSERT INTO LOCALISED_FIELD (OBJECT_TYPE,OBJECT_INSTANCE,OBJECT_VERSION,FIELD_NAME,LOCALE,LOOKUP_LOCALE,TEXT,IS_DELETED) VALUES ('DynamicEntityDefinitionED','KnowledgeArticleED',@ED.KnowledgeArticle,'fields.title2.displayName','en-US','default','Title2','N');\n"
	"\n"
	"\n"
	"INSERT INTO EVA_DYN_ENT_FIELD_PROPERTIES (ID, RELEASE_ID, FIELD_ID, ENTITY_DEF_TYPE_ID,ENTITY_DEF_TYPE_ENV_ID)\n"
	"VALUES (@EDEFP.KnowledgeArticleTitle2, @RELEASE.ID, @EDEF.KnowledgeArticleTitle2, @ET.StringFieldProperties,@ENV.Dflt);\n"
	"\n"
	"INSERT INTO EVA_DYN_ENTITY_FIELD_STRING_PR (ID, RELEASE_ID, MAX_LENGTH) VALUES (@EDEFP.KnowledgeArticleTitle2, @RELEASE.ID, 125);")
    sqlparser =SQLParser()
    expected =sqlparser.parse_assertable_statements(expected)
    
    actual=("\n"
	"\n"
	"INSERT INTO EVA_DYNAMIC_ENTITY_FIELD (ID, ENTITY_DEF_ID, NAME, INITIAL_VALUE, FIELD_TYPE_ID, FIELD_SEQUENCE, ENTITY_DEF_ENV_ID)\n"
	"VALUES (@EDEF.KnowledgeArticleTitle2, @ED.KnowledgeArticle, 'title2', '', @EFT.StringField, 1, @ENV.Dflt);\n"
	"\n"
	"\n"
	"INSERT INTO LOCALISED_FIELD (OBJECT_TYPE, OBJECT_INSTANCE, OBJECT_VERSION, FIELD_NAME, LOCALE, LOOKUP_LOCALE,TEXT,IS_DELETED) VALUES (\n"
	"'DynamicEntityDefinitionED', -- OBJECT_TYPE\n"
	"'KnowledgeArticleED', -- OBJECT_INSTANCE\n"
	"@ED.KnowledgeArticle, -- OBJECT_VERSION\n"
	"'fields.title2.displayName', -- FIELD_NAME\n"
	"'en-US', -- LOCALE\n"
	"'default', -- LOOKUP_LOCALE\n"
	"'Title2', --TEXT\n"
	"'N' --IS_DELETED\n"
	");\n"
	" \n"
	"\n"
	"\n"
	"INSERT INTO EVA_DYN_ENT_FIELD_PROPERTIES (ID, RELEASE_ID, FIELD_ID, ENTITY_DEF_TYPE_ID,ENTITY_DEF_TYPE_ENV_ID) \n"
	"VALUES (@EDEFP.KnowledgeArticleTitle2, @RELEASE.ID, @EDEF.KnowledgeArticleTitle2, @ET.StringFieldProperties,@ENV.Dflt);\n"
	"\n"
	"INSERT INTO EVA_DYN_ENTITY_FIELD_STRING_PR (ID, RELEASE_ID, MAX_LENGTH) VALUES (@EDEFP.KnowledgeArticleTitle2, @RELEASE.ID, 125);")
    actual =sqlparser.parse_assertable_statements(actual)
    
    assert expected == actual

def test_add_dynamic_entity_field_runs_succesfully():
    query=("INSERT INTO EVA_DYNAMIC_ENTITY_FIELD (ID, ENTITY_DEF_ID, NAME, INITIAL_VALUE, FIELD_TYPE_ID, FIELD_SEQUENCE, ENTITY_DEF_ENV_ID)\n"
	"VALUES (@EDEF.KnowledgeArticleTitle2, @ED.KnowledgeArticle, 'title2', '', @EFT.StringField, 1, @ENV.Dflt);\n"
	"\n"
	"INSERT INTO LOCALISED_FIELD (OBJECT_TYPE,OBJECT_INSTANCE,OBJECT_VERSION,FIELD_NAME,LOCALE,LOOKUP_LOCALE,TEXT,IS_DELETED) VALUES ('DynamicEntityDefinitionED','KnowledgeArticleED',@ED.KnowledgeArticle,'fields.title2.displayName','en-US','default','Title2','N');\n"
	"\n"
	"\n"
	"INSERT INTO EVA_DYN_ENT_FIELD_PROPERTIES (ID, RELEASE_ID, FIELD_ID, ENTITY_DEF_TYPE_ID,ENTITY_DEF_TYPE_ENV_ID)\n"
	"VALUES (@EDEFP.KnowledgeArticleTitle2, @RELEASE.ID, @EDEF.KnowledgeArticleTitle2, @ET.StringFieldProperties,@ENV.Dflt);\n"
	"\n"
	"INSERT INTO EVA_DYN_ENTITY_FIELD_STRING_PR (ID, RELEASE_ID, MAX_LENGTH) VALUES (@EDEFP.KnowledgeArticleTitle2, @RELEASE.ID, 125);")
    emprj_path=("/mnt/c/em//projects/pacificorp")
    app_project = AppProject(emprj_path=emprj_path)
    sqlparser =SQLParser(RelativeIdLoader())
    app_project.addb.execute(query,sqlparser=sqlparser)

def test_rendering_add_dynamic_entity_view_matches_expected_sql():
    expected=("INSERT INTO EVA_DYNAMIC_ENTITY_VIEW (ID,ENTITY_DEF_ID,ENTITY_DEF_ENV_ID,NAME,RELEASE_ID,VIEW_TYPE_ID,VIEW_TYPE_ENV_ID,USE_TABS,TENANT_ID)\n"
	"VALUES (\n"
	"	@DEV.KnowledgeArticleCreate2, @ED.KnowledgeArticle, @ENV.Dflt, 'Create2', @RELEASE.ID, @ET.ContentView, @ENV.Dflt, 'N', 'default');\n"
	"\n"
	"INSERT INTO EVA_DYNAMIC_ENTITY_VIEW_LAYOUT (ID,RELEASE_ID,LAYOUT_TYPE_ID,TENANT_ID)\n"
	"VALUES (\n"
	"	@DEV.KnowledgeArticleCreate2,\n"
	"	@RELEASE.ID, @ELT.ContentAuthoringLayout,\n"
	"	'default');\n"
	"\n"
	"INSERT INTO LOCALISED_FIELD (OBJECT_TYPE, OBJECT_INSTANCE, OBJECT_VERSION, FIELD_NAME, LOCALE, LOOKUP_LOCALE,TEXT,IS_DELETED) VALUES (\n"
	"'DynamicEntityDefinitionED', 'KnowledgeArticleED', @ED.KnowledgeArticle, 'views.Create2.displayName', 'en-US', 'default', 'KnowledgeArticleCreate2', 'N' );")
    sqlparser =SQLParser()
    expected =sqlparser.parse_assertable_statements(expected)
    
    actual=("INSERT INTO EVA_DYNAMIC_ENTITY_VIEW (ID,ENTITY_DEF_ID,ENTITY_DEF_ENV_ID,NAME,RELEASE_ID,VIEW_TYPE_ID,VIEW_TYPE_ENV_ID,USE_TABS,TENANT_ID) \n"
	"VALUES (\n"
	"	@DEV.KnowledgeArticleCreate2, --ID\n"
	"	@ED.KnowledgeArticle, --ENTITY_DEF_ID\n"
	"	@ENV.Dflt, --ENTITY_DEF_ENV_ID\n"
	"	'Create2', --NAME\n"
	"	@RELEASE.ID, --RELEASE_ID\n"
	"	@ET.ContentView, --VIEW_TYPE_ID\n"
	"	@ENV.Dflt, --VIEW_TYPE__ENV_ID\n"
	"	'N', --USE_TABS\n"
	"	'default');\n"
	"\n"
	"INSERT INTO EVA_DYNAMIC_ENTITY_VIEW_LAYOUT (ID,RELEASE_ID,LAYOUT_TYPE_ID,TENANT_ID) \n"
	"VALUES (\n"
	"	@DEV.KnowledgeArticleCreate2,\n"
	"	@RELEASE.ID, --RELEASE_ID\n"
	"	@ELT.ContentAuthoringLayout,\n"
	"	'default');\n"
	"\n"
	"INSERT INTO LOCALISED_FIELD (OBJECT_TYPE, OBJECT_INSTANCE, OBJECT_VERSION, FIELD_NAME, LOCALE, LOOKUP_LOCALE,TEXT,IS_DELETED) VALUES (\n"
	"'DynamicEntityDefinitionED', -- OBJECT_TYPE\n"
	"'KnowledgeArticleED', -- OBJECT_INSTANCE\n"
	"@ED.KnowledgeArticle, -- OBJECT_VERSION\n"
	"'views.Create2.displayName', -- FIELD_NAME\n"
	"'en-US', -- LOCALE\n"
	"'default', -- LOOKUP_LOCALE\n"
	"'KnowledgeArticleCreate2', --TEXT\n"
	"'N' --IS_DELETED\n"
	");")
    actual =sqlparser.parse_assertable_statements(actual)
    
    assert expected == actual

def test_add_dynamic_entity_view_runs_succesfully():
    query=("INSERT INTO EVA_DYNAMIC_ENTITY_VIEW (ID,ENTITY_DEF_ID,ENTITY_DEF_ENV_ID,NAME,RELEASE_ID,VIEW_TYPE_ID,VIEW_TYPE_ENV_ID,USE_TABS,TENANT_ID)\n"
	"VALUES (\n"
	"	@DEV.KnowledgeArticleCreate2, @ED.KnowledgeArticle, @ENV.Dflt, 'Create2', @RELEASE.ID, @ET.ContentView, @ENV.Dflt, 'N', 'default');\n"
	"\n"
	"INSERT INTO EVA_DYNAMIC_ENTITY_VIEW_LAYOUT (ID,RELEASE_ID,LAYOUT_TYPE_ID,TENANT_ID)\n"
	"VALUES (\n"
	"	@DEV.KnowledgeArticleCreate2,\n"
	"	@RELEASE.ID, @ELT.ContentAuthoringLayout,\n"
	"	'default');\n"
	"\n"
	"INSERT INTO LOCALISED_FIELD (OBJECT_TYPE, OBJECT_INSTANCE, OBJECT_VERSION, FIELD_NAME, LOCALE, LOOKUP_LOCALE,TEXT,IS_DELETED) VALUES (\n"
	"'DynamicEntityDefinitionED', 'KnowledgeArticleED', @ED.KnowledgeArticle, 'views.Create2.displayName', 'en-US', 'default', 'KnowledgeArticleCreate2', 'N' );")
    emprj_path=("/mnt/c/em//projects/pacificorp")
    app_project = AppProject(emprj_path=emprj_path)
    sqlparser =SQLParser(RelativeIdLoader())
    app_project.addb.execute(query,sqlparser=sqlparser)

def test_rendering_add_dynamic_entity_view_field_matches_expected_sql():
    expected=("INSERT INTO EVA_DYNAMIC_ENTITY_VIEW_GROUP (ID,VIEW_ID,GROUP_NAME,RELEASE_ID)\n"
	"VALUES (@EDEVG.KnowledgeArticleCreateGroupPublicInformation2,@DEV.KnowledgeArticleCreate,'Public Information 2',@RELEASE.ID);\n"
	"\n"
	"INSERT INTO LOCALISED_FIELD (OBJECT_TYPE,OBJECT_INSTANCE,OBJECT_VERSION,FIELD_NAME,LOCALE,LOOKUP_LOCALE,TEXT,LONG_TEXT,LAST_MODIFIED,IS_DELETED) VALUES (\n"
	"	'DynamicEntityDefinitionED',\n"
	"	'KnowledgeArticleED',\n"
	"	@ED.KnowledgeArticle,\n"
	"	'views.Create.groups.PublicInformation2.displayGroupName',\n"
	"	'en-US',\n"
	"	'default',\n"
	"	'Public Information 2',\n"
	"	null,\n"
	"	null,\n"
	"	'N');\n"
	"\n"
	"INSERT INTO EVA_PROCESS_DESC_REFERENCE (ID, PROCESS_DESCRIPTOR_ID, PROCESS_DESCRIPTOR_ENV_ID, CONFIG_ID, IS_SHARED)\n"
	"VALUES (@PDR.FieldEditorRichTextCreateKnowledgeArticlePublic, @PD.FieldEditorRichText, @ENV.Dflt, NULL, 'N');\n"
	"INSERT INTO EVA_DYNAMIC_ENTITY_VIEW_FIELD (ID, DYN_ENTITY_VIEW_ID, DYN_ENTITY_FIELD_ID, COMPONENT_TYPE_ID, PROCESS_DESC_REF_ID, SHOW_LABEL, IS_MANDATORY, VIEW_FIELD_SEQUENCE, GROUP_ID)\n"
	"VALUES (\n"
	"	@EDEVF.KnowledgeArticleCreatePublic2, @DEV.KnowledgeArticleCreate, @EDEF.KnowledgeArticlePublic, NULL, @PDR.FieldEditorRichTextCreateKnowledgeArticlePublic, 'Y', 'Y', 3, @EDEVG.KnowledgeArticleCreateGroupPublicInformation2  );")
    sqlparser =SQLParser()
    expected =sqlparser.parse_assertable_statements(expected)
    
    actual=("\n"
	"\n"
	"\n"
	"INSERT INTO EVA_DYNAMIC_ENTITY_VIEW_GROUP (ID,VIEW_ID,GROUP_NAME,RELEASE_ID) \n"
	"VALUES (@EDEVG.KnowledgeArticleCreateGroupPublicInformation2,@DEV.KnowledgeArticleCreate,'Public Information 2',@RELEASE.ID);\n"
	"\n"
	"INSERT INTO LOCALISED_FIELD (OBJECT_TYPE,OBJECT_INSTANCE,OBJECT_VERSION,FIELD_NAME,LOCALE,LOOKUP_LOCALE,TEXT,LONG_TEXT,LAST_MODIFIED,IS_DELETED) VALUES (\n"
	"	'DynamicEntityDefinitionED',\n"
	"	'KnowledgeArticleED',\n"
	"	@ED.KnowledgeArticle,\n"
	"	'views.Create.groups.PublicInformation2.displayGroupName',\n"
	"	'en-US',\n"
	"	'default',\n"
	"	'Public Information 2',\n"
	"	null,\n"
	"	null,\n"
	"	'N');\n"
	"\n"
	"	INSERT INTO EVA_PROCESS_DESC_REFERENCE (ID, PROCESS_DESCRIPTOR_ID, PROCESS_DESCRIPTOR_ENV_ID, CONFIG_ID, IS_SHARED) \n"
	"	VALUES (@PDR.FieldEditorRichTextCreateKnowledgeArticlePublic, @PD.FieldEditorRichText, @ENV.Dflt, NULL, 'N');\n"
	"INSERT INTO EVA_DYNAMIC_ENTITY_VIEW_FIELD (ID, DYN_ENTITY_VIEW_ID, DYN_ENTITY_FIELD_ID, COMPONENT_TYPE_ID, PROCESS_DESC_REF_ID, SHOW_LABEL, IS_MANDATORY, VIEW_FIELD_SEQUENCE, GROUP_ID) VALUES (\n"
	"	@EDEVF.KnowledgeArticleCreatePublic2, --ID\n"
	"	@DEV.KnowledgeArticleCreate, --DYN_ENTITY_VIEW_ID\n"
	"       	@EDEF.KnowledgeArticlePublic, --DYN_ENTITY_FIELD_ID\n"
	"       	NULL, --COMPONENT_TYPE_ID\n"
	"       	@PDR.FieldEditorRichTextCreateKnowledgeArticlePublic, --PROCESS_DESC_REF_ID\n"
	"       	'Y', --SHOW_LABEL\n"
	"	'Y', --IS_MANDATORY\n"
	"       	3, --VIEW_FIELD_SEQUENCE\n"
	"       	@EDEVG.KnowledgeArticleCreateGroupPublicInformation2 --GROUP_ID\n"
	");\n"
	"")
    actual =sqlparser.parse_assertable_statements(actual)
    
    assert expected == actual

def test_add_dynamic_entity_view_field_runs_succesfully():
    query=("INSERT INTO EVA_DYNAMIC_ENTITY_VIEW_GROUP (ID,VIEW_ID,GROUP_NAME,RELEASE_ID)\n"
	"VALUES (@EDEVG.KnowledgeArticleCreateGroupPublicInformation2,@DEV.KnowledgeArticleCreate,'Public Information 2',@RELEASE.ID);\n"
	"\n"
	"INSERT INTO LOCALISED_FIELD (OBJECT_TYPE,OBJECT_INSTANCE,OBJECT_VERSION,FIELD_NAME,LOCALE,LOOKUP_LOCALE,TEXT,LONG_TEXT,LAST_MODIFIED,IS_DELETED) VALUES (\n"
	"	'DynamicEntityDefinitionED',\n"
	"	'KnowledgeArticleED',\n"
	"	@ED.KnowledgeArticle,\n"
	"	'views.Create.groups.PublicInformation2.displayGroupName',\n"
	"	'en-US',\n"
	"	'default',\n"
	"	'Public Information 2',\n"
	"	null,\n"
	"	null,\n"
	"	'N');\n"
	"\n"
	"INSERT INTO EVA_PROCESS_DESC_REFERENCE (ID, PROCESS_DESCRIPTOR_ID, PROCESS_DESCRIPTOR_ENV_ID, CONFIG_ID, IS_SHARED)\n"
	"VALUES (@PDR.FieldEditorRichTextCreateKnowledgeArticlePublic, @PD.FieldEditorRichText, @ENV.Dflt, NULL, 'N');\n"
	"INSERT INTO EVA_DYNAMIC_ENTITY_VIEW_FIELD (ID, DYN_ENTITY_VIEW_ID, DYN_ENTITY_FIELD_ID, COMPONENT_TYPE_ID, PROCESS_DESC_REF_ID, SHOW_LABEL, IS_MANDATORY, VIEW_FIELD_SEQUENCE, GROUP_ID)\n"
	"VALUES (\n"
	"	@EDEVF.KnowledgeArticleCreatePublic2, @DEV.KnowledgeArticleCreate, @EDEF.KnowledgeArticlePublic, NULL, @PDR.FieldEditorRichTextCreateKnowledgeArticlePublic, 'Y', 'Y', 3, @EDEVG.KnowledgeArticleCreateGroupPublicInformation2  );")
    emprj_path=("/mnt/c/em//projects/pacificorp")
    app_project = AppProject(emprj_path=emprj_path)
    sqlparser =SQLParser(RelativeIdLoader())
    app_project.addb.execute(query,sqlparser=sqlparser)

def test_rendering_add_entity_definition_matches_expected_sql():
    expected=("INSERT INTO EVA_ENTITY_DEFINITION (ID, ENV_ID, NAME, UUID, TYPE_UUID, TYPE_ID, TYPE_ENV_ID, LOGICAL_OBJ_PATH, INTERFACE_PATH, SUPER_ENTITY_DEFINITION, SUPER_ENTITY_DEFINITION_ENV_ID, IS_DELETED, IS_BASIC, SUPPORTS_READONLY,IS_EXPANDABLE, ICON_PATH, INSTANCE_ICON_PATH) VALUES (\n"
	"@ED.Agreement, @ENV.Dflt, 'AgreementED', 'AgreementED', 'AgreementED', @ET.Agreement, @ENV.Dflt, 'PacificorpAccount.Implementation.Objects.Agreement', 'PacificorpAccount.API.EIAgreement', @ED.PersistableEntity, @ENV.Dflt, 'N', 'Y', 'Y', 'N', NULL, NULL );\n"
	"INSERT INTO EVA_CATEGORY (ID,ENV_ID,PARENT_CATEGORY_ID,PARENT_CATEGORY_ENV_ID,ENTITY_DEF_ID,ENTITY_DEF_ENV_ID,RELEASE_ID,SYSTEM_NAME)\n"
	"VALUES (\n"
	"	@EC.Pacificorp5, @ENV.Dflt, @EC.System, @ENV.Dflt, @ED.EntityDefinition, @ENV.Dflt, @RELEASE.ID,\n"
	"	'Categories->System->Pacificorp5' );\n"
	"\n"
	"INSERT INTO LOCALISED_FIELD (OBJECT_TYPE, OBJECT_INSTANCE, OBJECT_VERSION, FIELD_NAME, LOCALE, LOOKUP_LOCALE,TEXT,IS_DELETED) VALUES (\n"
	"'CategoryED', 'Categories->System->Pacificorp5', @EC.Pacificorp5, 'displayName', 'en-US', 'default', 'Pacificorp5', 'N' );\n"
	"\n"
	"INSERT INTO LOCALISED_FIELD (OBJECT_TYPE, OBJECT_INSTANCE, OBJECT_VERSION, FIELD_NAME, LOCALE, LOOKUP_LOCALE,TEXT,IS_DELETED) VALUES (\n"
	"'CategoryED', 'Categories->System->Pacificorp5', @EC.Pacificorp5, 'description', 'en-US', 'default', 'Pacificorp5', 'N' );\n"
	"\n"
	"INSERT INTO EVA_CATEGORY_ENTRY(CATEGORY_ID, CATEGORY_ENV_ID, ENTITY_ID, ENTITY_ENV_ID) VALUES (\n"
	"@EC.Pacificorp5, @ENV.Dflt, @ED.Agreement, @ENV.Dflt  );\n"
	"\n"
	"INSERT INTO LOCALISED_FIELD (OBJECT_TYPE, OBJECT_INSTANCE, OBJECT_VERSION, FIELD_NAME, LOCALE, LOOKUP_LOCALE,TEXT,IS_DELETED) VALUES (\n"
	"'EntityDefinitionED', 'AgreementED', @ED.Agreement, 'displayName', 'en-US', 'default', 'Agreement', 'N' );\n"
	"\n"
	"INSERT INTO LOCALISED_FIELD (OBJECT_TYPE, OBJECT_INSTANCE, OBJECT_VERSION, FIELD_NAME, LOCALE, LOOKUP_LOCALE,TEXT,IS_DELETED) VALUES (\n"
	"'EntityDefinitionED', 'AgreementED', @ED.Agreement, 'description', 'en-US', 'default', 'Agreement Description', 'N' );")
    sqlparser =SQLParser()
    expected =sqlparser.parse_assertable_statements(expected)
    
    actual=("INSERT INTO EVA_ENTITY_DEFINITION (ID, ENV_ID, NAME, UUID, TYPE_UUID, TYPE_ID, TYPE_ENV_ID, LOGICAL_OBJ_PATH, INTERFACE_PATH, SUPER_ENTITY_DEFINITION, SUPER_ENTITY_DEFINITION_ENV_ID, IS_DELETED, IS_BASIC, SUPPORTS_READONLY,IS_EXPANDABLE,ICON_PATH, INSTANCE_ICON_PATH) VALUES (\n"
	"@ED.Agreement, -- ID\n"
	"@ENV.Dflt, -- ENV_ID\n"
	"'AgreementED', -- NAME\n"
	"'AgreementED', -- UUID\n"
	"'AgreementED', -- TYPE_UUID\n"
	"@ET.Agreement, -- TYPE_ID\n"
	"@ENV.Dflt, -- TYPE_ENV_ID\n"
	"'PacificorpAccount.Implementation.Objects.Agreement', -- LOGICAL_OBJECT_PATH\n"
	"'PacificorpAccount.API.EIAgreement', -- INTERFACE_PATH\n"
	"@ED.PersistableEntity, -- SUPER_ENTITY_DEFINITION\n"
	"@ENV.Dflt, -- SUPER_ENTITY_DEFINITION_ENV_ID\n"
	"'N', -- IS_DELETED\n"
	"'Y', -- IS_BASIC\n"
	"'Y', -- SUPPORTS_READ_ONLY\n"
	"'N', --IS_EXPANDABLE\n"
	"NULL, -- ICON_PATH\n"
	"NULL -- INSTANCE_ICON_PATH\n"
	");\n"
	"\n"
	"\n"
	"INSERT INTO EVA_CATEGORY (ID,ENV_ID,PARENT_CATEGORY_ID,PARENT_CATEGORY_ENV_ID,ENTITY_DEF_ID,ENTITY_DEF_ENV_ID,RELEASE_ID,SYSTEM_NAME)\n"
	"VALUES (\n"
	"	@EC.Pacificorp5, --ID\n"
	"	@ENV.Dflt, --ENV_ID\n"
	"	@EC.System, --PARENT_CATEGORY_ID\n"
	"	@ENV.Dflt, --PARENT_CATEGORY_ENV_ID\n"
	"	@ED.EntityDefinition, --ENTITY_DEF_ID\n"
	"	@ENV.Dflt, --ENTITY_DEF_ENV_ID\n"
	"	@RELEASE.ID,\n"
	"	'Categories->System->Pacificorp5' --SYSTEM_NAME\n"
	"       );\n"
	"\n"
	"\n"
	"INSERT INTO LOCALISED_FIELD (OBJECT_TYPE, OBJECT_INSTANCE, OBJECT_VERSION, FIELD_NAME, LOCALE, LOOKUP_LOCALE,TEXT,IS_DELETED) VALUES (\n"
	"'CategoryED', -- OBJECT_TYPE\n"
	"'Categories->System->Pacificorp5', -- OBJECT_INSTANCE\n"
	"@EC.Pacificorp5, -- OBJECT_VERSION\n"
	"'displayName', -- FIELD_NAME\n"
	"'en-US', -- LOCALE\n"
	"'default', -- LOOKUP_LOCALE\n"
	"'Pacificorp5', --TEXT\n"
	"'N' --IS_DELETED\n"
	");\n"
	"\n"
	"\n"
	"INSERT INTO LOCALISED_FIELD (OBJECT_TYPE, OBJECT_INSTANCE, OBJECT_VERSION, FIELD_NAME, LOCALE, LOOKUP_LOCALE,TEXT,IS_DELETED) VALUES (\n"
	"'CategoryED', -- OBJECT_TYPE\n"
	"'Categories->System->Pacificorp5', -- OBJECT_INSTANCE\n"
	"@EC.Pacificorp5, -- OBJECT_VERSION\n"
	"'description', -- FIELD_NAME\n"
	"'en-US', -- LOCALE\n"
	"'default', -- LOOKUP_LOCALE\n"
	"'Pacificorp5', --TEXT\n"
	"'N' --IS_DELETED\n"
	");\n"
	"\n"
	"\n"
	"\n"
	"  INSERT INTO EVA_CATEGORY_ENTRY(CATEGORY_ID, CATEGORY_ENV_ID, ENTITY_ID, ENTITY_ENV_ID) VALUES (\n"
	"  @EC.Pacificorp5, -- CATEGORY_ID\n"
	"  @ENV.Dflt, -- CATEGORY_ENV_ID\n"
	"  @ED.Agreement, -- ENTITY_ID\n"
	"  @ENV.Dflt -- ENTITY_ENV_ID\n"
	"  );\n"
	"\n"
	"INSERT INTO LOCALISED_FIELD (OBJECT_TYPE, OBJECT_INSTANCE, OBJECT_VERSION, FIELD_NAME, LOCALE, LOOKUP_LOCALE,TEXT,IS_DELETED) VALUES (\n"
	"'EntityDefinitionED', -- OBJECT_TYPE\n"
	"'AgreementED', -- OBJECT_INSTANCE\n"
	"@ED.Agreement, -- OBJECT_VERSION\n"
	"'displayName', -- FIELD_NAME\n"
	"'en-US', -- LOCALE\n"
	"'default', -- LOOKUP_LOCALE\n"
	"'Agreement', --TEXT\n"
	"'N' --IS_DELETED\n"
	");\n"
	"\n"
	"\n"
	"INSERT INTO LOCALISED_FIELD (OBJECT_TYPE, OBJECT_INSTANCE, OBJECT_VERSION, FIELD_NAME, LOCALE, LOOKUP_LOCALE,TEXT,IS_DELETED) VALUES (\n"
	"'EntityDefinitionED', -- OBJECT_TYPE\n"
	"'AgreementED', -- OBJECT_INSTANCE\n"
	"@ED.Agreement, -- OBJECT_VERSION\n"
	"'description', -- FIELD_NAME\n"
	"'en-US', -- LOCALE\n"
	"'default', -- LOOKUP_LOCALE\n"
	"'Agreement Description', --TEXT\n"
	"'N' --IS_DELETED\n"
	");\n"
	"")
    actual =sqlparser.parse_assertable_statements(actual)
    
    assert expected == actual

def test_add_entity_definition_runs_succesfully():
    query=("INSERT INTO EVA_ENTITY_DEFINITION (ID, ENV_ID, NAME, UUID, TYPE_UUID, TYPE_ID, TYPE_ENV_ID, LOGICAL_OBJ_PATH, INTERFACE_PATH, SUPER_ENTITY_DEFINITION, SUPER_ENTITY_DEFINITION_ENV_ID, IS_DELETED, IS_BASIC, SUPPORTS_READONLY,IS_EXPANDABLE, ICON_PATH, INSTANCE_ICON_PATH) VALUES (\n"
	"@ED.Agreement, @ENV.Dflt, 'AgreementED', 'AgreementED', 'AgreementED', @ET.Agreement, @ENV.Dflt, 'PacificorpAccount.Implementation.Objects.Agreement', 'PacificorpAccount.API.EIAgreement', @ED.PersistableEntity, @ENV.Dflt, 'N', 'Y', 'Y', 'N', NULL, NULL );\n"
	"INSERT INTO EVA_CATEGORY (ID,ENV_ID,PARENT_CATEGORY_ID,PARENT_CATEGORY_ENV_ID,ENTITY_DEF_ID,ENTITY_DEF_ENV_ID,RELEASE_ID,SYSTEM_NAME)\n"
	"VALUES (\n"
	"	@EC.Pacificorp5, @ENV.Dflt, @EC.System, @ENV.Dflt, @ED.EntityDefinition, @ENV.Dflt, @RELEASE.ID,\n"
	"	'Categories->System->Pacificorp5' );\n"
	"\n"
	"INSERT INTO LOCALISED_FIELD (OBJECT_TYPE, OBJECT_INSTANCE, OBJECT_VERSION, FIELD_NAME, LOCALE, LOOKUP_LOCALE,TEXT,IS_DELETED) VALUES (\n"
	"'CategoryED', 'Categories->System->Pacificorp5', @EC.Pacificorp5, 'displayName', 'en-US', 'default', 'Pacificorp5', 'N' );\n"
	"\n"
	"INSERT INTO LOCALISED_FIELD (OBJECT_TYPE, OBJECT_INSTANCE, OBJECT_VERSION, FIELD_NAME, LOCALE, LOOKUP_LOCALE,TEXT,IS_DELETED) VALUES (\n"
	"'CategoryED', 'Categories->System->Pacificorp5', @EC.Pacificorp5, 'description', 'en-US', 'default', 'Pacificorp5', 'N' );\n"
	"\n"
	"INSERT INTO EVA_CATEGORY_ENTRY(CATEGORY_ID, CATEGORY_ENV_ID, ENTITY_ID, ENTITY_ENV_ID) VALUES (\n"
	"@EC.Pacificorp5, @ENV.Dflt, @ED.Agreement, @ENV.Dflt  );\n"
	"\n"
	"INSERT INTO LOCALISED_FIELD (OBJECT_TYPE, OBJECT_INSTANCE, OBJECT_VERSION, FIELD_NAME, LOCALE, LOOKUP_LOCALE,TEXT,IS_DELETED) VALUES (\n"
	"'EntityDefinitionED', 'AgreementED', @ED.Agreement, 'displayName', 'en-US', 'default', 'Agreement', 'N' );\n"
	"\n"
	"INSERT INTO LOCALISED_FIELD (OBJECT_TYPE, OBJECT_INSTANCE, OBJECT_VERSION, FIELD_NAME, LOCALE, LOOKUP_LOCALE,TEXT,IS_DELETED) VALUES (\n"
	"'EntityDefinitionED', 'AgreementED', @ED.Agreement, 'description', 'en-US', 'default', 'Agreement Description', 'N' );")
    emprj_path=("/mnt/c/em//projects/pacificorp")
    app_project = AppProject(emprj_path=emprj_path)
    sqlparser =SQLParser(RelativeIdLoader())
    app_project.addb.execute(query,sqlparser=sqlparser)

def test_rendering_add_menu_matches_expected_sql():
    expected=("INSERT INTO FD_MENU (ID, ENV_ID, NAME, IMAGE_PATH, PARENT_ID, PARENT_ENV_ID, IS_DELETED)\n"
	"VALUES(\n"
	"	@MN.manageToolsMenu, @ENV.Dflt, 'manageTools', '/CorePageSetEditor/Implementation/ScriptingMenu/UI/Images/sciboodleManageScriptingPageSetsUp64x64', @MN.RootMenu, @ENV.Dflt, 'N');\n"
	"\n"
	"INSERT INTO EVA_PROCESS_DESC_REFERENCE (ID, PROCESS_DESCRIPTOR_ID, PROCESS_DESCRIPTOR_ENV_ID, CONFIG_ID, IS_SHARED) VALUES (\n"
	"@PDR.menuManageTools, @PD.DefaultRunPanel, @ENV.Dflt, @MN.manageToolsMenu, 'N' );\n"
	"INSERT INTO EVA_VERB (ID, NAME, PROCESS_DESC_REF_ID, ENTITY_DEF_ID, ENTITY_DEF_ENV_ID, IS_INSTANCE, IS_DEFAULT, IS_INSTANCE_DEFAULT, IS_USER_VISIBLE) VALUES (\n"
	"@V.menuManageTools, 'manageTools', @PDR.menuManageTools, @ED.Menu, @ENV.Dflt, 'N', 'N', 'N', 'Y' );\n"
	"\n"
	"INSERT INTO LOCALISED_FIELD (OBJECT_TYPE, OBJECT_INSTANCE, OBJECT_VERSION, FIELD_NAME, LOCALE, LOOKUP_LOCALE,TEXT,IS_DELETED) VALUES (\n"
	"'VerbED', 'MenuED__manageTools', @V.menuManageTools, 'displayName', 'en-US', 'default', 'Manage Tools', 'N'\n"
	");\n"
	"\n"
	"INSERT INTO LOCALISED_FIELD (OBJECT_TYPE, OBJECT_INSTANCE, OBJECT_VERSION, FIELD_NAME, LOCALE, LOOKUP_LOCALE,TEXT,IS_DELETED) VALUES (\n"
	"'VerbED', 'MenuED__manageTools', @V.menuManageTools, 'description', 'en-US', 'default', 'Manage Tools Description', 'N'\n"
	");")
    sqlparser =SQLParser()
    expected =sqlparser.parse_assertable_statements(expected)
    
    actual=("INSERT INTO FD_MENU (ID, ENV_ID, NAME, IMAGE_PATH, PARENT_ID, PARENT_ENV_ID, IS_DELETED)\n"
	"VALUES(\n"
	"	@MN.manageToolsMenu,--ID\n"
	"	@ENV.Dflt,--ENV_ID\n"
	"	'manageTools',--NAME\n"
	"	'/CorePageSetEditor/Implementation/ScriptingMenu/UI/Images/sciboodleManageScriptingPageSetsUp64x64',--IMAGE_PATH\n"
	"       	@MN.RootMenu,--PARENT_ID\n"
	"       	@ENV.Dflt,--IS_DELETED\n"
	"       	'N'\n"
	");\n"
	"\n"
	"\n"
	"\n"
	"\n"
	"\n"
	"  INSERT INTO EVA_PROCESS_DESC_REFERENCE (ID, PROCESS_DESCRIPTOR_ID, PROCESS_DESCRIPTOR_ENV_ID, CONFIG_ID, IS_SHARED) \n"
	"VALUES (\n"
	"        @PDR.menuManageTools, --id\n"
	"        @PD.DefaultRunPanel, --process_descriptor_id\n"
	"	@ENV.Dflt, --process_descriptor_env_id\n"
	"	@MN.manageToolsMenu, --config_id\n"
	"       	'N' --is_shared\n"
	"       );\n"
	"\n"
	"\n"
	"\n"
	"INSERT INTO EVA_VERB (ID, NAME, PROCESS_DESC_REF_ID, ENTITY_DEF_ID, ENTITY_DEF_ENV_ID, IS_INSTANCE, IS_DEFAULT, IS_INSTANCE_DEFAULT, IS_USER_VISIBLE) VALUES (\n"
	"@V.menuManageTools, --ID\n"
	"'manageTools', -- NAME\n"
	"@PDR.menuManageTools, --PROCESS_DESC_REF_ID\n"
	"@ED.Menu, -- ENTITY_DEF_ID\n"
	"@ENV.Dflt, -- ENTITY_DEF_ENV_ID\n"
	"'N', --IS_INSTANCE\n"
	"'N', -- IS_DEFAULT\n"
	"  'N', -- IS_INSTANCE_DEFAULT\n"
	"'Y' -- IS_USER_VISIBLE\n"
	");\n"
	"\n"
	"INSERT INTO LOCALISED_FIELD (OBJECT_TYPE, OBJECT_INSTANCE, OBJECT_VERSION, FIELD_NAME, LOCALE, LOOKUP_LOCALE,TEXT,IS_DELETED) VALUES (\n"
	"'VerbED', -- OBJECT_TYPE\n"
	"'MenuED__manageTools', -- OBJECT_INSTANCE\n"
	"@V.menuManageTools, -- OBJECT_VERSION\n"
	"'displayName', -- FIELD_NAME\n"
	"'en-US', -- LOCALE\n"
	"'default', -- LOOKUP_LOCALE\n"
	"'Manage Tools', --TEXT\n"
	"'N' --IS_DELETED\n"
	");\n"
	"\n"
	"\n"
	"INSERT INTO LOCALISED_FIELD (OBJECT_TYPE, OBJECT_INSTANCE, OBJECT_VERSION, FIELD_NAME, LOCALE, LOOKUP_LOCALE,TEXT,IS_DELETED) VALUES (\n"
	"'VerbED', -- OBJECT_TYPE\n"
	"'MenuED__manageTools', -- OBJECT_INSTANCE\n"
	"@V.menuManageTools, -- OBJECT_VERSION\n"
	"'description', -- FIELD_NAME\n"
	"'en-US', -- LOCALE\n"
	"'default', -- LOOKUP_LOCALE\n"
	"'Manage Tools Description', --TEXT\n"
	"'N' --IS_DELETED\n"
	");\n"
	"")
    actual =sqlparser.parse_assertable_statements(actual)
    
    assert expected == actual

def test_add_menu_runs_succesfully():
    query=("INSERT INTO FD_MENU (ID, ENV_ID, NAME, IMAGE_PATH, PARENT_ID, PARENT_ENV_ID, IS_DELETED)\n"
	"VALUES(\n"
	"	@MN.manageToolsMenu, @ENV.Dflt, 'manageTools', '/CorePageSetEditor/Implementation/ScriptingMenu/UI/Images/sciboodleManageScriptingPageSetsUp64x64', @MN.RootMenu, @ENV.Dflt, 'N');\n"
	"\n"
	"INSERT INTO EVA_PROCESS_DESC_REFERENCE (ID, PROCESS_DESCRIPTOR_ID, PROCESS_DESCRIPTOR_ENV_ID, CONFIG_ID, IS_SHARED) VALUES (\n"
	"@PDR.menuManageTools, @PD.DefaultRunPanel, @ENV.Dflt, @MN.manageToolsMenu, 'N' );\n"
	"INSERT INTO EVA_VERB (ID, NAME, PROCESS_DESC_REF_ID, ENTITY_DEF_ID, ENTITY_DEF_ENV_ID, IS_INSTANCE, IS_DEFAULT, IS_INSTANCE_DEFAULT, IS_USER_VISIBLE) VALUES (\n"
	"@V.menuManageTools, 'manageTools', @PDR.menuManageTools, @ED.Menu, @ENV.Dflt, 'N', 'N', 'N', 'Y' );\n"
	"\n"
	"INSERT INTO LOCALISED_FIELD (OBJECT_TYPE, OBJECT_INSTANCE, OBJECT_VERSION, FIELD_NAME, LOCALE, LOOKUP_LOCALE,TEXT,IS_DELETED) VALUES (\n"
	"'VerbED', 'MenuED__manageTools', @V.menuManageTools, 'displayName', 'en-US', 'default', 'Manage Tools', 'N'\n"
	");\n"
	"\n"
	"INSERT INTO LOCALISED_FIELD (OBJECT_TYPE, OBJECT_INSTANCE, OBJECT_VERSION, FIELD_NAME, LOCALE, LOOKUP_LOCALE,TEXT,IS_DELETED) VALUES (\n"
	"'VerbED', 'MenuED__manageTools', @V.menuManageTools, 'description', 'en-US', 'default', 'Manage Tools Description', 'N'\n"
	");")
    emprj_path=("/mnt/c/em//projects/pacificorp")
    app_project = AppProject(emprj_path=emprj_path)
    sqlparser =SQLParser(RelativeIdLoader())
    app_project.addb.execute(query,sqlparser=sqlparser)

def test_rendering_add_menu_item_matches_expected_sql():
    expected=("INSERT INTO FD_MENU_ITEM (ID, ENV_ID, MENU_ID, MENU_ENV_ID, NAME, IMAGE_PATH, IMAGE_PATH_ROLLOVER, VERB_NAME, VERB_ENTITY_DEF_TYPE_ID, VERB_ENTITY_DEF_TYPE_ENV_ID, IS_DELETED)\n"
	"VALUES (\n"
	"	@MNI.OrganisationMenuinlineSearch, @ENV.Dflt, @MN.OrganisationMenu, @ENV.Dflt, 'OrganisationMenuinlineSearch', '/FrameworkDesktop/Skin/ControlPanelImages/sciboodleControlPanelFieldEditorsUp64x64', '/FrameworkDesktop/Skin/ControlPanelImages/sciboodleControlPanelFieldEditorsUp64x64', 'inlineSearch', @ET.Customer, @ENV.Dflt, 'N' );\n"
	"INSERT INTO LOCALISED_FIELD (OBJECT_TYPE, OBJECT_INSTANCE, OBJECT_VERSION, FIELD_NAME, LOCALE, LOOKUP_LOCALE,TEXT,IS_DELETED)\n"
	"VALUES (\n"
	"       	'MenuItemED',\n"
	"	'OrganisationMenuinlineSearch',\n"
	"	@MNI.OrganisationMenuinlineSearch,\n"
	"	'displayName',\n"
	"	'en-US',\n"
	"	'default',\n"
	"	'Inline Search',\n"
	"	'N'\n"
	");\n"
	"INSERT INTO LOCALISED_FIELD (OBJECT_TYPE, OBJECT_INSTANCE, OBJECT_VERSION, FIELD_NAME, LOCALE, LOOKUP_LOCALE,TEXT,IS_DELETED)\n"
	"VALUES (\n"
	"       	'MenuItemED',\n"
	"	'OrganisationMenuinlineSearch',\n"
	"	@MNI.OrganisationMenuinlineSearch,\n"
	"	'description',\n"
	"	'en-US',\n"
	"	'default',\n"
	"	'Inline Search Desc',\n"
	"	'N'\n"
	");")
    sqlparser =SQLParser()
    expected =sqlparser.parse_assertable_statements(expected)
    
    actual=("--[]\n"
	"INSERT INTO FD_MENU_ITEM (ID, ENV_ID, MENU_ID, MENU_ENV_ID, NAME, IMAGE_PATH, IMAGE_PATH_ROLLOVER, VERB_NAME, VERB_ENTITY_DEF_TYPE_ID, VERB_ENTITY_DEF_TYPE_ENV_ID, IS_DELETED) \n"
	"VALUES (\n"
	"	@MNI.OrganisationMenuinlineSearch, --ID\n"
	"       	@ENV.Dflt, --ENV_ID\n"
	"       	@MN.OrganisationMenu, --MENU_ID\n"
	"       	@ENV.Dflt, --MENU_ENV_ID\n"
	"       	'OrganisationMenuinlineSearch', --NAME\n"
	"       	'/FrameworkDesktop/Skin/ControlPanelImages/sciboodleControlPanelFieldEditorsUp64x64', --IMAGE_PATH\n"
	"	'/FrameworkDesktop/Skin/ControlPanelImages/sciboodleControlPanelFieldEditorsUp64x64',--IMAGE_PATH_ROLLOVER\n"
	"       	'inlineSearch', --VERB_NAME\n"
	"       	@ET.Customer, --ENTITY_DEF_ID\n"
	"       	@ENV.Dflt, --ENTITY_DEF_ENV_ID\n"
	"       	'N' --IS_DELETED\n"
	");\n"
	"INSERT INTO LOCALISED_FIELD (OBJECT_TYPE, OBJECT_INSTANCE, OBJECT_VERSION, FIELD_NAME, LOCALE, LOOKUP_LOCALE,TEXT,IS_DELETED) VALUES (\n"
	"'MenuItemED', -- OBJECT_TYPE\n"
	"'OrganisationMenuinlineSearch', -- OBJECT_INSTANCE\n"
	"@MNI.OrganisationMenuinlineSearch, -- OBJECT_VERSION\n"
	"'displayName', -- FIELD_NAME\n"
	"'en-US', -- LOCALE\n"
	"'default', -- LOOKUP_LOCALE\n"
	"'Inline Search', --TEXT\n"
	"'N' --IS_DELETED\n"
	");\n"
	"\n"
	"\n"
	"INSERT INTO LOCALISED_FIELD (OBJECT_TYPE, OBJECT_INSTANCE, OBJECT_VERSION, FIELD_NAME, LOCALE, LOOKUP_LOCALE,TEXT,IS_DELETED) VALUES (\n"
	"'MenuItemED', -- OBJECT_TYPE\n"
	"'OrganisationMenuinlineSearch', -- OBJECT_INSTANCE\n"
	"@MNI.OrganisationMenuinlineSearch, -- OBJECT_VERSION\n"
	"'description', -- FIELD_NAME\n"
	"'en-US', -- LOCALE\n"
	"'default', -- LOOKUP_LOCALE\n"
	"'Inline Search Desc', --TEXT\n"
	"'N' --IS_DELETED\n"
	");")
    actual =sqlparser.parse_assertable_statements(actual)
    
    assert expected == actual

def test_add_menu_item_runs_succesfully():
    query=("INSERT INTO FD_MENU_ITEM (ID, ENV_ID, MENU_ID, MENU_ENV_ID, NAME, IMAGE_PATH, IMAGE_PATH_ROLLOVER, VERB_NAME, VERB_ENTITY_DEF_TYPE_ID, VERB_ENTITY_DEF_TYPE_ENV_ID, IS_DELETED)\n"
	"VALUES (\n"
	"	@MNI.OrganisationMenuinlineSearch, @ENV.Dflt, @MN.OrganisationMenu, @ENV.Dflt, 'OrganisationMenuinlineSearch', '/FrameworkDesktop/Skin/ControlPanelImages/sciboodleControlPanelFieldEditorsUp64x64', '/FrameworkDesktop/Skin/ControlPanelImages/sciboodleControlPanelFieldEditorsUp64x64', 'inlineSearch', @ET.Customer, @ENV.Dflt, 'N' );\n"
	"INSERT INTO LOCALISED_FIELD (OBJECT_TYPE, OBJECT_INSTANCE, OBJECT_VERSION, FIELD_NAME, LOCALE, LOOKUP_LOCALE,TEXT,IS_DELETED)\n"
	"VALUES (\n"
	"       	'MenuItemED',\n"
	"	'OrganisationMenuinlineSearch',\n"
	"	@MNI.OrganisationMenuinlineSearch,\n"
	"	'displayName',\n"
	"	'en-US',\n"
	"	'default',\n"
	"	'Inline Search',\n"
	"	'N'\n"
	");\n"
	"INSERT INTO LOCALISED_FIELD (OBJECT_TYPE, OBJECT_INSTANCE, OBJECT_VERSION, FIELD_NAME, LOCALE, LOOKUP_LOCALE,TEXT,IS_DELETED)\n"
	"VALUES (\n"
	"       	'MenuItemED',\n"
	"	'OrganisationMenuinlineSearch',\n"
	"	@MNI.OrganisationMenuinlineSearch,\n"
	"	'description',\n"
	"	'en-US',\n"
	"	'default',\n"
	"	'Inline Search Desc',\n"
	"	'N'\n"
	");")
    emprj_path=("/mnt/c/em//projects/pacificorp")
    app_project = AppProject(emprj_path=emprj_path)
    sqlparser =SQLParser(RelativeIdLoader())
    app_project.addb.execute(query,sqlparser=sqlparser)

def test_rendering_add_process_descriptor_matches_expected_sql():
    expected=("INSERT INTO EVA_PROCESS_DESCRIPTOR (ID, ENV_ID, NAME, REPOSITORY_PATH, CONFIG_PROCESS_ID, IS_DELETED, TYPE)\n"
	"VALUES (\n"
	"         @PD.PRJsearchBasicCustomer, @ENV.Dflt, 'PRJsearchBasicCustomer', 'Customer.Process.SearchBasicCustomer', NULL, 'N', @PDT.Verb  );\n"
	"\n"
	"\n"
	"INSERT INTO LOCALISED_FIELD (OBJECT_TYPE, OBJECT_INSTANCE, OBJECT_VERSION, FIELD_NAME, LOCALE, LOOKUP_LOCALE,TEXT,IS_DELETED) VALUES (\n"
	"'ProcessDescriptorED', 'PRJsearchBasicCustomer__Customer/Process/SearchBasicCustomer', @PD.PRJsearchBasicCustomer, 'displayName', 'en-US', 'default', 'PRJsearchBasicCustomer', 'N'\n"
	");\n"
	"\n"
	"INSERT INTO LOCALISED_FIELD (OBJECT_TYPE, OBJECT_INSTANCE, OBJECT_VERSION, FIELD_NAME, LOCALE, LOOKUP_LOCALE,TEXT,IS_DELETED) VALUES (\n"
	"'ProcessDescriptorED', 'PRJsearchBasicCustomer__Customer/Process/SearchBasicCustomer', @PD.PRJsearchBasicCustomer, 'description', 'en-US', 'default', 'PRJsearchBasicCustomer', 'N'\n"
	");")
    sqlparser =SQLParser()
    expected =sqlparser.parse_assertable_statements(expected)
    
    actual=("INSERT INTO EVA_PROCESS_DESCRIPTOR (ID, ENV_ID, NAME, REPOSITORY_PATH, CONFIG_PROCESS_ID, IS_DELETED, TYPE)\n"
	"VALUES (\n"
	"	 @PD.PRJsearchBasicCustomer, --id\n"
	"	 @ENV.Dflt, --env_id,\n"
	"	 'PRJsearchBasicCustomer', --process_descriptor_name\n"
	"	 'Customer.Process.SearchBasicCustomer', --repository_path\n"
	"	 NULL, --config_id\n"
	"	 'N', --is_deleted\n"
	"	 @PDT.Verb --type\n"
	"       );\n"
	"\n"
	"INSERT INTO LOCALISED_FIELD (OBJECT_TYPE, OBJECT_INSTANCE, OBJECT_VERSION, FIELD_NAME, LOCALE, LOOKUP_LOCALE,TEXT,IS_DELETED) VALUES (\n"
	"'ProcessDescriptorED', -- OBJECT_TYPE\n"
	"'PRJsearchBasicCustomer__Customer/Process/SearchBasicCustomer', -- OBJECT_INSTANCE\n"
	"@PD.PRJsearchBasicCustomer, -- OBJECT_VERSION\n"
	"'displayName', -- FIELD_NAME\n"
	"'en-US', -- LOCALE\n"
	"'default', -- LOOKUP_LOCALE\n"
	"'PRJsearchBasicCustomer', --TEXT\n"
	"'N' --IS_DELETED\n"
	");\n"
	"\n"
	"\n"
	"INSERT INTO LOCALISED_FIELD (OBJECT_TYPE, OBJECT_INSTANCE, OBJECT_VERSION, FIELD_NAME, LOCALE, LOOKUP_LOCALE,TEXT,IS_DELETED) VALUES (\n"
	"'ProcessDescriptorED', -- OBJECT_TYPE\n"
	"'PRJsearchBasicCustomer__Customer/Process/SearchBasicCustomer', -- OBJECT_INSTANCE\n"
	"@PD.PRJsearchBasicCustomer, -- OBJECT_VERSION\n"
	"'description', -- FIELD_NAME\n"
	"'en-US', -- LOCALE\n"
	"'default', -- LOOKUP_LOCALE\n"
	"'PRJsearchBasicCustomer', --TEXT\n"
	"'N' --IS_DELETED\n"
	");")
    actual =sqlparser.parse_assertable_statements(actual)
    
    assert expected == actual

def test_add_process_descriptor_runs_succesfully():
    query=("INSERT INTO EVA_PROCESS_DESCRIPTOR (ID, ENV_ID, NAME, REPOSITORY_PATH, CONFIG_PROCESS_ID, IS_DELETED, TYPE)\n"
	"VALUES (\n"
	"         @PD.PRJsearchBasicCustomer, @ENV.Dflt, 'PRJsearchBasicCustomer', 'Customer.Process.SearchBasicCustomer', NULL, 'N', @PDT.Verb  );\n"
	"\n"
	"\n"
	"INSERT INTO LOCALISED_FIELD (OBJECT_TYPE, OBJECT_INSTANCE, OBJECT_VERSION, FIELD_NAME, LOCALE, LOOKUP_LOCALE,TEXT,IS_DELETED) VALUES (\n"
	"'ProcessDescriptorED', 'PRJsearchBasicCustomer__Customer/Process/SearchBasicCustomer', @PD.PRJsearchBasicCustomer, 'displayName', 'en-US', 'default', 'PRJsearchBasicCustomer', 'N'\n"
	");\n"
	"\n"
	"INSERT INTO LOCALISED_FIELD (OBJECT_TYPE, OBJECT_INSTANCE, OBJECT_VERSION, FIELD_NAME, LOCALE, LOOKUP_LOCALE,TEXT,IS_DELETED) VALUES (\n"
	"'ProcessDescriptorED', 'PRJsearchBasicCustomer__Customer/Process/SearchBasicCustomer', @PD.PRJsearchBasicCustomer, 'description', 'en-US', 'default', 'PRJsearchBasicCustomer', 'N'\n"
	");")
    emprj_path=("/mnt/c/em//projects/pacificorp")
    app_project = AppProject(emprj_path=emprj_path)
    sqlparser =SQLParser(RelativeIdLoader())
    app_project.addb.execute(query,sqlparser=sqlparser)

def test_rendering_add_profile_to_agent_matches_expected_sql():
    expected=("INSERT INTO FD_USER_PROFILE_TYPE (TENANT_ID, USER_ID, PROFILE_TYPE_ID, PROFILE_TYPE_ENV_ID, IS_DELETED) VALUES ('default', @USER.admin, @PROFILE.AGENT, 666, 'N');")
    sqlparser =SQLParser()
    expected =sqlparser.parse_assertable_statements(expected)
    
    actual=("INSERT INTO FD_USER_PROFILE_TYPE (TENANT_ID, USER_ID, PROFILE_TYPE_ID, PROFILE_TYPE_ENV_ID, IS_DELETED)\n"
	"VALUES ('default',\n"
	"        @USER.admin, \n"
	"        @PROFILE.AGENT, 666, 'N');")
    actual =sqlparser.parse_assertable_statements(actual)
    
    assert expected == actual

def test_add_profile_to_agent_runs_succesfully():
    query=("INSERT INTO FD_USER_PROFILE_TYPE (TENANT_ID, USER_ID, PROFILE_TYPE_ID, PROFILE_TYPE_ENV_ID, IS_DELETED) VALUES ('default', @USER.admin, @PROFILE.AGENT, 666, 'N');")
    emprj_path=("/mnt/c/em//projects/pacificorp")
    app_project = AppProject(emprj_path=emprj_path)
    sqlparser =SQLParser(RelativeIdLoader())
    app_project.addb.execute(query,sqlparser=sqlparser)

def test_rendering_add_tag_matches_expected_sql():
    expected=("INSERT INTO eva_tag (ID,ENV_ID,RELEASE_ID,TAGSET_ID,TAGSET_ENV_ID,TAGSET_RELEASE_ID,PARENT_TAG,PARENT_TAG_ENV_ID,PARENT_TAG_RELEASE_ID,PREVIOUS_TAG,PREVIOUS_TAG_ENV_ID,PREVIOUS_TAG_RELEASE_ID,NAME,IS_SYSTEM,IS_DELETED,IS_RETIRED,EXPAND_DIRECTION,CREATED_DATE,LAST_MODIFIED_DATE,LEFT_VAL,RIGHT_VAL,DEPTH_VAL,DISPLAY_ORDER,SYSTEM_CODE)\n"
	"VALUES (@TAG.pepe3, @ENV.Dflt, @RELEASE.ID, @TAG.CONTENTCAT, @ENV.Dflt, @RELEASE.ID, @TAG.CONTENTCAT, @ENV.Dflt, @RELEASE.ID, @TAG.CCDOCUP, @ENV.Dflt, @RELEASE.ID, 'content_pepe3', 'N', 'N', 'N', null, sysdate, sysdate, 15, 16, 1, null, 'content_pepe3' );\n"
	"update eva_tag\n"
	"set (RIGHT_VAL)=(17)\n"
	"where id =@TAG.CONTENTCAT;\n"
	"\n"
	"INSERT INTO eva_tag_loc (ID,ENV_ID,RELEASE_ID,LOCALE,DESCRIPTION,ICON_URI,REPORTING_LABEL)\n"
	"VALUES (@TAG.pepe3, @ENV.Dflt, @RELEASE.ID, 'en-US', 'pepe3', null, 'pepe3' );\n"
	"INSERT INTO EVA_TAG_DISPLAY_NAME (ID,ENV_ID,RELEASE_ID,DISPLAY_NAME_TYPE_ID,DISPLAY_NAME_TYPE_ENV_ID,DISPLAY_NAME_TYPE_RELEASE_ID)\n"
	"VALUES (@TAG.pepe3, @ENV.Dflt, @RELEASE.ID, 1, @ENV.Dflt, @RELEASE.ID );\n"
	"\n"
	"INSERT INTO EVA_TAG_DISPLAY_NAME_LOC (ID,ENV_ID,RELEASE_ID,LOCALE,DISPLAY_NAME,DISPLAY_NAME_TYPE_ID,DISPLAY_NAME_TYPE_ENV_ID,DISPLAY_NAME_TYPE_RELEASE_ID)\n"
	"VALUES (@TAG.pepe3, @ENV.Dflt, @RELEASE.ID, 'en-US', 'pepe3', 1, @ENV.Dflt, @RELEASE.ID );")
    sqlparser =SQLParser()
    expected =sqlparser.parse_assertable_statements(expected)
    
    actual=("INSERT INTO eva_tag (ID,ENV_ID,RELEASE_ID,TAGSET_ID,TAGSET_ENV_ID,TAGSET_RELEASE_ID,PARENT_TAG,PARENT_TAG_ENV_ID,PARENT_TAG_RELEASE_ID,PREVIOUS_TAG,PREVIOUS_TAG_ENV_ID,PREVIOUS_TAG_RELEASE_ID,NAME,IS_SYSTEM,IS_DELETED,IS_RETIRED,EXPAND_DIRECTION,CREATED_DATE,LAST_MODIFIED_DATE,LEFT_VAL,RIGHT_VAL,DEPTH_VAL,DISPLAY_ORDER,SYSTEM_CODE) \n"
	"VALUES (@TAG.pepe3, --ID\n"
	"	@ENV.Dflt, --ENV_ID\n"
	"	@RELEASE.ID, --RELEASE_ID\n"
	"	@TAG.CONTENTCAT, -- TAGSET_ID\n"
	"	@ENV.Dflt,-- TAGSET_ENV_ID\n"
	"	@RELEASE.ID,-- TAGSET_RELEASE_ID\n"
	"	@TAG.CONTENTCAT,--PARENT_TAG_ID\n"
	"	@ENV.Dflt,--PARENT_TAG_ENV_ID\n"
	"	@RELEASE.ID,--PARENT_TAG_RELEASE_ID\n"
	"	@TAG.CCDOCUP,--PREVIOUS_TAG\n"
	"	@ENV.Dflt,--PREVIOUS_TAG_ENV_ID\n"
	"	@RELEASE.ID,--PREVIOUS_TAG_RELEASE_ID\n"
	"	'content_pepe3', --NAME\n"
	"	'N', --IS_SYSTEM\n"
	"	'N',--IS_DELETED\n"
	"	'N',--IS_RETIRED\n"
	"	null,--EXPAND_DIRECTION\n"
	"	sysdate, -- created\n"
	"	sysdate, --LAST_MODIFIED\n"
	" \n"
	"	15, --LEFT_VAL\n"
	"	16, --RIGHT_VAL\n"
	"	1, --DEPTH_VAL\n"
	"	null, -- DISPLAY_ORDER\n"
	"	'content_pepe3' --SYSTEM_CODE\n"
	");\n"
	"update eva_tag\n"
	"set (RIGHT_VAL)=(17)\n"
	"where id =@TAG.CONTENTCAT;\n"
	"\n"
	"INSERT INTO eva_tag_loc (ID,ENV_ID,RELEASE_ID,LOCALE,DESCRIPTION,ICON_URI,REPORTING_LABEL) \n"
	"VALUES (@TAG.pepe3,--id\n"
	"	   @ENV.Dflt,--env_id\n"
	"	   @RELEASE.ID,--release_id\n"
	"	   'en-US',--locale\n"
	"	   'pepe3',--description\n"
	"	   null,--icon_uri\n"
	"	   'pepe3' --reporting_label\n"
	");\n"
	"INSERT INTO EVA_TAG_DISPLAY_NAME (ID,ENV_ID,RELEASE_ID,DISPLAY_NAME_TYPE_ID,DISPLAY_NAME_TYPE_ENV_ID,DISPLAY_NAME_TYPE_RELEASE_ID)\n"
	"VALUES (@TAG.pepe3,--id\n"
	"	   @ENV.Dflt,--env_id\n"
	"	   @RELEASE.ID,--release_id\n"
	"	   1,--display_name_type_id\n"
	"	   @ENV.Dflt, --display_name_type_env_id\n"
	"	   @RELEASE.ID--display_name_type_release_id\n"
	");\n"
	"\n"
	"INSERT INTO EVA_TAG_DISPLAY_NAME_LOC (ID,ENV_ID,RELEASE_ID,LOCALE,DISPLAY_NAME,DISPLAY_NAME_TYPE_ID,DISPLAY_NAME_TYPE_ENV_ID,DISPLAY_NAME_TYPE_RELEASE_ID)\n"
	"VALUES (@TAG.pepe3,--id\n"
	"	   @ENV.Dflt,--env_id\n"
	"	   @RELEASE.ID,--release_id\n"
	"	   'en-US',--locale\n"
	"	   'pepe3',--display_name\n"
	"	   1, --display_name_type_id\n"
	"	   @ENV.Dflt,--display_name_type_env_id\n"
	"	   @RELEASE.ID--display_name_type_release_id\n"
	");")
    actual =sqlparser.parse_assertable_statements(actual)
    
    assert expected == actual

def test_add_tag_runs_succesfully():
    query=("INSERT INTO eva_tag (ID,ENV_ID,RELEASE_ID,TAGSET_ID,TAGSET_ENV_ID,TAGSET_RELEASE_ID,PARENT_TAG,PARENT_TAG_ENV_ID,PARENT_TAG_RELEASE_ID,PREVIOUS_TAG,PREVIOUS_TAG_ENV_ID,PREVIOUS_TAG_RELEASE_ID,NAME,IS_SYSTEM,IS_DELETED,IS_RETIRED,EXPAND_DIRECTION,CREATED_DATE,LAST_MODIFIED_DATE,LEFT_VAL,RIGHT_VAL,DEPTH_VAL,DISPLAY_ORDER,SYSTEM_CODE)\n"
	"VALUES (@TAG.pepe3, @ENV.Dflt, @RELEASE.ID, @TAG.CONTENTCAT, @ENV.Dflt, @RELEASE.ID, @TAG.CONTENTCAT, @ENV.Dflt, @RELEASE.ID, @TAG.CCDOCUP, @ENV.Dflt, @RELEASE.ID, 'content_pepe3', 'N', 'N', 'N', null, sysdate, sysdate, 15, 16, 1, null, 'content_pepe3' );\n"
	"update eva_tag\n"
	"set (RIGHT_VAL)=(17)\n"
	"where id =@TAG.CONTENTCAT;\n"
	"\n"
	"INSERT INTO eva_tag_loc (ID,ENV_ID,RELEASE_ID,LOCALE,DESCRIPTION,ICON_URI,REPORTING_LABEL)\n"
	"VALUES (@TAG.pepe3, @ENV.Dflt, @RELEASE.ID, 'en-US', 'pepe3', null, 'pepe3' );\n"
	"INSERT INTO EVA_TAG_DISPLAY_NAME (ID,ENV_ID,RELEASE_ID,DISPLAY_NAME_TYPE_ID,DISPLAY_NAME_TYPE_ENV_ID,DISPLAY_NAME_TYPE_RELEASE_ID)\n"
	"VALUES (@TAG.pepe3, @ENV.Dflt, @RELEASE.ID, 1, @ENV.Dflt, @RELEASE.ID );\n"
	"\n"
	"INSERT INTO EVA_TAG_DISPLAY_NAME_LOC (ID,ENV_ID,RELEASE_ID,LOCALE,DISPLAY_NAME,DISPLAY_NAME_TYPE_ID,DISPLAY_NAME_TYPE_ENV_ID,DISPLAY_NAME_TYPE_RELEASE_ID)\n"
	"VALUES (@TAG.pepe3, @ENV.Dflt, @RELEASE.ID, 'en-US', 'pepe3', 1, @ENV.Dflt, @RELEASE.ID );")
    emprj_path=("/mnt/c/em//projects/pacificorp")
    app_project = AppProject(emprj_path=emprj_path)
    sqlparser =SQLParser(RelativeIdLoader())
    app_project.addb.execute(query,sqlparser=sqlparser)

def test_rendering_add_verb_to_entity_matches_expected_sql():
    expected=("INSERT INTO EVA_PROCESS_DESCRIPTOR (ID, ENV_ID, NAME, REPOSITORY_PATH, CONFIG_PROCESS_ID, IS_DELETED,TYPE) VALUES (\n"
	"@PD.PCCustomerInlineEdit, @ENV.Dflt, 'PCCustomerInlineEdit', 'PCCustomer.Verbs.CustomerInlineEdit', NULL, 'N', @PDT.Verb  );\n"
	"\n"
	"INSERT INTO LOCALISED_FIELD (OBJECT_TYPE, OBJECT_INSTANCE, OBJECT_VERSION, FIELD_NAME, LOCALE, LOOKUP_LOCALE,TEXT,IS_DELETED) VALUES (\n"
	"'ProcessDescriptorED', 'PCCustomerInlineEdit__PCCustomer/Verbs/CustomerInlineEdit', @PD.PCCustomerInlineEdit, 'displayName', 'en-US', 'default', 'PCCustomerInlineEdit', 'N'\n"
	");\n"
	"\n"
	"INSERT INTO LOCALISED_FIELD (OBJECT_TYPE, OBJECT_INSTANCE, OBJECT_VERSION, FIELD_NAME, LOCALE, LOOKUP_LOCALE,TEXT,IS_DELETED) VALUES (\n"
	"'ProcessDescriptorED', 'PCCustomerInlineEdit__PCCustomer/Verbs/CustomerInlineEdit', @PD.PCCustomerInlineEdit, 'description', 'en-US', 'default', 'PCCustomerInlineEdit', 'N'\n"
	");\n"
	"\n"
	"INSERT INTO EVA_PROCESS_DESC_REFERENCE (ID, PROCESS_DESCRIPTOR_ID, PROCESS_DESCRIPTOR_ENV_ID, CONFIG_ID, IS_SHARED) VALUES (\n"
	"@PDR.PCCustomerInlineEdit, @PD.PCCustomerInlineEdit, @ENV.Dflt, NULL, 'N' );\n"
	"\n"
	"INSERT INTO EVA_VERB (ID, NAME, PROCESS_DESC_REF_ID, ENTITY_DEF_ID, ENTITY_DEF_ENV_ID, IS_INSTANCE, IS_DEFAULT, IS_INSTANCE_DEFAULT, IS_USER_VISIBLE) VALUES (\n"
	"@V.PCCustomerInlineEdit, 'inlineEdit', @PDR.PCCustomerInlineEdit, @ED.Customer, @ENV.Dflt, 'Y', 'N', 'N', 'Y' );\n"
	"\n"
	"INSERT INTO LOCALISED_FIELD (OBJECT_TYPE, OBJECT_INSTANCE, OBJECT_VERSION, FIELD_NAME, LOCALE, LOOKUP_LOCALE,TEXT,IS_DELETED) VALUES (\n"
	"'VerbED', 'CustomerED__inlineEdit', @V.PCCustomerInlineEdit, 'displayName', 'en-US', 'default', 'Inline Edit', 'N'\n"
	");\n"
	"\n"
	"INSERT INTO LOCALISED_FIELD (OBJECT_TYPE, OBJECT_INSTANCE, OBJECT_VERSION, FIELD_NAME, LOCALE, LOOKUP_LOCALE,TEXT,IS_DELETED) VALUES (\n"
	"'VerbED', 'CustomerED__inlineEdit', @V.PCCustomerInlineEdit, 'description', 'en-US', 'default', 'Allows editing the customer inline', 'N'\n"
	");")
    sqlparser =SQLParser()
    expected =sqlparser.parse_assertable_statements(expected)
    
    actual=("\n"
	"\n"
	"\n"
	"  INSERT INTO EVA_PROCESS_DESCRIPTOR (ID, ENV_ID, NAME, REPOSITORY_PATH, CONFIG_PROCESS_ID, IS_DELETED, TYPE)\n"
	"VALUES (\n"
	"	 @PD.PCCustomerInlineEdit, --id\n"
	"	 @ENV.Dflt, --env_id,\n"
	"	 'PCCustomerInlineEdit', --process_descriptor_name\n"
	"	 'PCCustomer.Verbs.CustomerInlineEdit', --repository_path\n"
	"	 NULL, --config_id\n"
	"	 'N', --is_deleted\n"
	"	 @PDT.Verb --type\n"
	"       );\n"
	"\n"
	"INSERT INTO LOCALISED_FIELD (OBJECT_TYPE, OBJECT_INSTANCE, OBJECT_VERSION, FIELD_NAME, LOCALE, LOOKUP_LOCALE,TEXT,IS_DELETED) VALUES (\n"
	"'ProcessDescriptorED', -- OBJECT_TYPE\n"
	"'PCCustomerInlineEdit__PCCustomer/Verbs/CustomerInlineEdit', -- OBJECT_INSTANCE\n"
	"@PD.PCCustomerInlineEdit, -- OBJECT_VERSION\n"
	"'displayName', -- FIELD_NAME\n"
	"'en-US', -- LOCALE\n"
	"'default', -- LOOKUP_LOCALE\n"
	"'PCCustomerInlineEdit', --TEXT\n"
	"'N' --IS_DELETED\n"
	");\n"
	"\n"
	"\n"
	"INSERT INTO LOCALISED_FIELD (OBJECT_TYPE, OBJECT_INSTANCE, OBJECT_VERSION, FIELD_NAME, LOCALE, LOOKUP_LOCALE,TEXT,IS_DELETED) VALUES (\n"
	"'ProcessDescriptorED', -- OBJECT_TYPE\n"
	"'PCCustomerInlineEdit__PCCustomer/Verbs/CustomerInlineEdit', -- OBJECT_INSTANCE\n"
	"@PD.PCCustomerInlineEdit, -- OBJECT_VERSION\n"
	"'description', -- FIELD_NAME\n"
	"'en-US', -- LOCALE\n"
	"'default', -- LOOKUP_LOCALE\n"
	"'PCCustomerInlineEdit', --TEXT\n"
	"'N' --IS_DELETED\n"
	");\n"
	"\n"
	"\n"
	"\n"
	"  INSERT INTO EVA_PROCESS_DESC_REFERENCE (ID, PROCESS_DESCRIPTOR_ID, PROCESS_DESCRIPTOR_ENV_ID, CONFIG_ID, IS_SHARED) \n"
	"VALUES (\n"
	"        @PDR.PCCustomerInlineEdit, --id\n"
	"        @PD.PCCustomerInlineEdit, --process_descriptor_id\n"
	"	@ENV.Dflt, --process_descriptor_env_id\n"
	"	NULL, --config_id\n"
	"       	'N' --is_shared\n"
	"       );\n"
	"\n"
	"\n"
	"\n"
	"INSERT INTO EVA_VERB (ID, NAME, PROCESS_DESC_REF_ID, ENTITY_DEF_ID, ENTITY_DEF_ENV_ID, IS_INSTANCE, IS_DEFAULT, IS_INSTANCE_DEFAULT, IS_USER_VISIBLE) VALUES (\n"
	"@V.PCCustomerInlineEdit, --ID\n"
	"'inlineEdit', -- NAME\n"
	"@PDR.PCCustomerInlineEdit, --PROCESS_DESC_REF_ID\n"
	"@ED.Customer, -- ENTITY_DEF_ID\n"
	"@ENV.Dflt, -- ENTITY_DEF_ENV_ID\n"
	"'Y', --IS_INSTANCE\n"
	"'N', -- IS_DEFAULT\n"
	"'N', -- IS_INSTANCE_DEFAULT\n"
	"'Y' -- IS_USER_VISIBLE\n"
	");\n"
	"\n"
	"INSERT INTO LOCALISED_FIELD (OBJECT_TYPE, OBJECT_INSTANCE, OBJECT_VERSION, FIELD_NAME, LOCALE, LOOKUP_LOCALE,TEXT,IS_DELETED) VALUES (\n"
	"'VerbED', -- OBJECT_TYPE\n"
	"'CustomerED__inlineEdit', -- OBJECT_INSTANCE\n"
	"@V.PCCustomerInlineEdit, -- OBJECT_VERSION\n"
	"'displayName', -- FIELD_NAME\n"
	"'en-US', -- LOCALE\n"
	"'default', -- LOOKUP_LOCALE\n"
	"'Inline Edit', --TEXT\n"
	"'N' --IS_DELETED\n"
	");\n"
	"\n"
	"\n"
	"INSERT INTO LOCALISED_FIELD (OBJECT_TYPE, OBJECT_INSTANCE, OBJECT_VERSION, FIELD_NAME, LOCALE, LOOKUP_LOCALE,TEXT,IS_DELETED) VALUES (\n"
	"'VerbED', -- OBJECT_TYPE\n"
	"'CustomerED__inlineEdit', -- OBJECT_INSTANCE\n"
	"@V.PCCustomerInlineEdit, -- OBJECT_VERSION\n"
	"'description', -- FIELD_NAME\n"
	"'en-US', -- LOCALE\n"
	"'default', -- LOOKUP_LOCALE\n"
	"'Allows editing the customer inline', --TEXT\n"
	"'N' --IS_DELETED\n"
	");")
    actual =sqlparser.parse_assertable_statements(actual)
    
    assert expected == actual

def test_add_verb_to_entity_runs_succesfully():
    query=("INSERT INTO EVA_PROCESS_DESCRIPTOR (ID, ENV_ID, NAME, REPOSITORY_PATH, CONFIG_PROCESS_ID, IS_DELETED,TYPE) VALUES (\n"
	"@PD.PCCustomerInlineEdit, @ENV.Dflt, 'PCCustomerInlineEdit', 'PCCustomer.Verbs.CustomerInlineEdit', NULL, 'N', @PDT.Verb  );\n"
	"\n"
	"INSERT INTO LOCALISED_FIELD (OBJECT_TYPE, OBJECT_INSTANCE, OBJECT_VERSION, FIELD_NAME, LOCALE, LOOKUP_LOCALE,TEXT,IS_DELETED) VALUES (\n"
	"'ProcessDescriptorED', 'PCCustomerInlineEdit__PCCustomer/Verbs/CustomerInlineEdit', @PD.PCCustomerInlineEdit, 'displayName', 'en-US', 'default', 'PCCustomerInlineEdit', 'N'\n"
	");\n"
	"\n"
	"INSERT INTO LOCALISED_FIELD (OBJECT_TYPE, OBJECT_INSTANCE, OBJECT_VERSION, FIELD_NAME, LOCALE, LOOKUP_LOCALE,TEXT,IS_DELETED) VALUES (\n"
	"'ProcessDescriptorED', 'PCCustomerInlineEdit__PCCustomer/Verbs/CustomerInlineEdit', @PD.PCCustomerInlineEdit, 'description', 'en-US', 'default', 'PCCustomerInlineEdit', 'N'\n"
	");\n"
	"\n"
	"INSERT INTO EVA_PROCESS_DESC_REFERENCE (ID, PROCESS_DESCRIPTOR_ID, PROCESS_DESCRIPTOR_ENV_ID, CONFIG_ID, IS_SHARED) VALUES (\n"
	"@PDR.PCCustomerInlineEdit, @PD.PCCustomerInlineEdit, @ENV.Dflt, NULL, 'N' );\n"
	"\n"
	"INSERT INTO EVA_VERB (ID, NAME, PROCESS_DESC_REF_ID, ENTITY_DEF_ID, ENTITY_DEF_ENV_ID, IS_INSTANCE, IS_DEFAULT, IS_INSTANCE_DEFAULT, IS_USER_VISIBLE) VALUES (\n"
	"@V.PCCustomerInlineEdit, 'inlineEdit', @PDR.PCCustomerInlineEdit, @ED.Customer, @ENV.Dflt, 'Y', 'N', 'N', 'Y' );\n"
	"\n"
	"INSERT INTO LOCALISED_FIELD (OBJECT_TYPE, OBJECT_INSTANCE, OBJECT_VERSION, FIELD_NAME, LOCALE, LOOKUP_LOCALE,TEXT,IS_DELETED) VALUES (\n"
	"'VerbED', 'CustomerED__inlineEdit', @V.PCCustomerInlineEdit, 'displayName', 'en-US', 'default', 'Inline Edit', 'N'\n"
	");\n"
	"\n"
	"INSERT INTO LOCALISED_FIELD (OBJECT_TYPE, OBJECT_INSTANCE, OBJECT_VERSION, FIELD_NAME, LOCALE, LOOKUP_LOCALE,TEXT,IS_DELETED) VALUES (\n"
	"'VerbED', 'CustomerED__inlineEdit', @V.PCCustomerInlineEdit, 'description', 'en-US', 'default', 'Allows editing the customer inline', 'N'\n"
	");")
    emprj_path=("/mnt/c/em//projects/pacificorp")
    app_project = AppProject(emprj_path=emprj_path)
    sqlparser =SQLParser(RelativeIdLoader())
    app_project.addb.execute(query,sqlparser=sqlparser)

def test_rendering_change_max_count_work_area_matches_expected_sql():
    expected=("UPDATE FD_WORK_AREA SET (MAX_COUNT) = (2) WHERE ID = 9;")
    sqlparser =SQLParser()
    expected =sqlparser.parse_assertable_statements(expected)
    
    actual=("UPDATE FD_WORK_AREA SET (MAX_COUNT) = (2) WHERE ID = 9;")
    actual =sqlparser.parse_assertable_statements(actual)
    
    assert expected == actual

def test_change_max_count_work_area_runs_succesfully():
    query=("UPDATE FD_WORK_AREA SET (MAX_COUNT) = (2) WHERE ID = 9;")
    emprj_path=("/mnt/c/em//projects/pacificorp")
    app_project = AppProject(emprj_path=emprj_path)
    sqlparser =SQLParser(RelativeIdLoader())
    app_project.addb.execute(query,sqlparser=sqlparser)

def test_rendering_extend_customer_matches_expected_sql():
    expected=("UPDATE EVA_ENTITY_DEFINITION\n"
	"SET (LOGICAL_OBJ_PATH) = ('GSCCoreEntities.Implementation.Customer.GSCCustomer')\n"
	"WHERE ID = @ED.Customer AND ENV_ID = @ENV.Dflt;\n"
	"\n"
	"UPDATE EVA_ENTITY_DEFINITION\n"
	"SET (INTERFACE_PATH) = ('GSCCoreEntities.API.EIGSCCustomer')\n"
	"WHERE ID = @ED.Customer AND ENV_ID = @ENV.Dflt;")
    sqlparser =SQLParser()
    expected =sqlparser.parse_assertable_statements(expected)
    
    actual=("--No need to create a new entity definition, because  pre-extended \n"
	"--customer object is provided OTB to facilate customer extensions\n"
	"UPDATE EVA_ENTITY_DEFINITION \n"
	"SET (LOGICAL_OBJ_PATH) = ('GSCCoreEntities.Implementation.Customer.GSCCustomer') \n"
	"WHERE ID = @ED.Customer AND ENV_ID = @ENV.Dflt;\n"
	"\n"
	"UPDATE EVA_ENTITY_DEFINITION \n"
	"SET (INTERFACE_PATH) = ('GSCCoreEntities.API.EIGSCCustomer') \n"
	"WHERE ID = @ED.Customer AND ENV_ID = @ENV.Dflt;")
    actual =sqlparser.parse_assertable_statements(actual)
    
    assert expected == actual

def test_extend_customer_runs_succesfully():
    query=("UPDATE EVA_ENTITY_DEFINITION\n"
	"SET (LOGICAL_OBJ_PATH) = ('GSCCoreEntities.Implementation.Customer.GSCCustomer')\n"
	"WHERE ID = @ED.Customer AND ENV_ID = @ENV.Dflt;\n"
	"\n"
	"UPDATE EVA_ENTITY_DEFINITION\n"
	"SET (INTERFACE_PATH) = ('GSCCoreEntities.API.EIGSCCustomer')\n"
	"WHERE ID = @ED.Customer AND ENV_ID = @ENV.Dflt;")
    emprj_path=("/mnt/c/em//projects/pacificorp")
    app_project = AppProject(emprj_path=emprj_path)
    sqlparser =SQLParser(RelativeIdLoader())
    app_project.addb.execute(query,sqlparser=sqlparser)

def test_rendering_extend_entity_matches_expected_sql():
    expected=("INSERT INTO EVA_ENTITY_DEFINITION (ID, ENV_ID, NAME, UUID, TYPE_UUID, TYPE_ID, TYPE_ENV_ID, LOGICAL_OBJ_PATH, INTERFACE_PATH, SUPER_ENTITY_DEFINITION, SUPER_ENTITY_DEFINITION_ENV_ID, IS_DELETED, IS_BASIC, SUPPORTS_READONLY,IS_EXPANDABLE,ICON_PATH, INSTANCE_ICON_PATH) VALUES (\n"
	"@ED.BaseVirtualEnvironment, @ENV.Dflt, 'BaseVirtualEnvironmentED', 'BaseVirtualEnvironmentED', 'BaseVirtualEnvironmentED', @ET.BaseVirtualEnvironment, @ENV.Dflt, 'FrameworkEVA.Implementation.VirtualEnvironment.Objects.VirtualEnvironment', 'FrameworkEVA.API.Interfaces.EIVirtualEnvironment', NULL, @ENV.Dflt, 'N', 'Y', 'Y', 'N', NULL, NULL );\n"
	"INSERT INTO EVA_CATEGORY_ENTRY(CATEGORY_ID, CATEGORY_ENV_ID, ENTITY_ID, ENTITY_ENV_ID) VALUES (\n"
	"  @EC.SystemGeneral, @ENV.Dflt, @ED.BaseVirtualEnvironment, @ENV.Dflt  );\n"
	"\n"
	"INSERT INTO LOCALISED_FIELD (OBJECT_TYPE, OBJECT_INSTANCE, OBJECT_VERSION, FIELD_NAME, LOCALE, LOOKUP_LOCALE,TEXT,IS_DELETED) VALUES (\n"
	"'EntityDefinitionED', 'BaseVirtualEnvironmentED', @ED.BaseVirtualEnvironment, 'displayName', 'en-US', 'default', 'Virtual Environment Base Class', 'N' );\n"
	"INSERT INTO LOCALISED_FIELD (OBJECT_TYPE, OBJECT_INSTANCE, OBJECT_VERSION, FIELD_NAME, LOCALE, LOOKUP_LOCALE,TEXT,IS_DELETED) VALUES (\n"
	"'EntityDefinitionED', 'BaseVirtualEnvironmentED', @ED.BaseVirtualEnvironment, 'description', 'en-US', 'default', 'System can contain a number of virtual environments. Base Class', 'N' );\n"
	"UPDATE EVA_ENTITY_DEFINITION\n"
	"SET (LOGICAL_OBJ_PATH, INTERFACE_PATH, SUPER_ENTITY_DEFINITION, SUPER_ENTITY_DEFINITION_ENV_ID) = ('PRJFrameworkEVA.Implementation.VirtualEnvironment.Objects.PRJVirtualEnvironment', 'PRJFrameworkEVA.API.Interfaces.EIPRJVirtualEnvironment', @ED.BaseVirtualEnvironment, @ENV.Dflt) WHERE ID = @ED.VirtualEnvironment AND ENV_ID = @ENV.Dflt AND RELEASE_ID = @RELEASE.ID;")
    sqlparser =SQLParser()
    expected =sqlparser.parse_assertable_statements(expected)
    
    actual=("\n"
	"INSERT INTO EVA_ENTITY_DEFINITION (ID, ENV_ID, NAME, UUID, TYPE_UUID, TYPE_ID, TYPE_ENV_ID, LOGICAL_OBJ_PATH, INTERFACE_PATH, SUPER_ENTITY_DEFINITION, SUPER_ENTITY_DEFINITION_ENV_ID, IS_DELETED, IS_BASIC, SUPPORTS_READONLY,IS_EXPANDABLE,ICON_PATH, INSTANCE_ICON_PATH) VALUES (\n"
	"@ED.BaseVirtualEnvironment, -- ID\n"
	"@ENV.Dflt, -- ENV_ID\n"
	"'BaseVirtualEnvironmentED', -- NAME\n"
	"'BaseVirtualEnvironmentED', -- UUID\n"
	"'BaseVirtualEnvironmentED', -- TYPE_UUID\n"
	"@ET.BaseVirtualEnvironment, -- TYPE_ID\n"
	"@ENV.Dflt, -- TYPE_ENV_ID\n"
	"'FrameworkEVA.Implementation.VirtualEnvironment.Objects.VirtualEnvironment', -- LOGICAL_OBJECT_PATH\n"
	"'FrameworkEVA.API.Interfaces.EIVirtualEnvironment', -- INTERFACE_PATH\n"
	"NULL, -- SUPER_ENTITY_DEFINITION\n"
	"@ENV.Dflt, -- SUPER_ENTITY_DEFINITION_ENV_ID\n"
	"'N', -- IS_DELETED\n"
	"'Y', -- IS_BASIC\n"
	"'Y', -- SUPPORTS_READ_ONLY\n"
	"'N', --IS_EXPANDABLE\n"
	"NULL, -- ICON_PATH\n"
	"NULL -- INSTANCE_ICON_PATH\n"
	");\n"
	"\n"
	"\n"
	"  INSERT INTO EVA_CATEGORY_ENTRY(CATEGORY_ID, CATEGORY_ENV_ID, ENTITY_ID, ENTITY_ENV_ID) VALUES (\n"
	"  @EC.SystemGeneral, -- CATEGORY_ID\n"
	"  @ENV.Dflt, -- CATEGORY_ENV_ID\n"
	"  @ED.BaseVirtualEnvironment, -- ENTITY_ID\n"
	"  @ENV.Dflt -- ENTITY_ENV_ID\n"
	"  );\n"
	"\n"
	"INSERT INTO LOCALISED_FIELD (OBJECT_TYPE, OBJECT_INSTANCE, OBJECT_VERSION, FIELD_NAME, LOCALE, LOOKUP_LOCALE,TEXT,IS_DELETED) VALUES (\n"
	"'EntityDefinitionED', -- OBJECT_TYPE\n"
	"'BaseVirtualEnvironmentED', -- OBJECT_INSTANCE\n"
	"@ED.BaseVirtualEnvironment, -- OBJECT_VERSION\n"
	"'displayName', -- FIELD_NAME\n"
	"'en-US', -- LOCALE\n"
	"'default', -- LOOKUP_LOCALE\n"
	"'Virtual Environment Base Class', --TEXT\n"
	"'N' --IS_DELETED\n"
	");\n"
	"\n"
	"\n"
	"INSERT INTO LOCALISED_FIELD (OBJECT_TYPE, OBJECT_INSTANCE, OBJECT_VERSION, FIELD_NAME, LOCALE, LOOKUP_LOCALE,TEXT,IS_DELETED) VALUES (\n"
	"'EntityDefinitionED', -- OBJECT_TYPE\n"
	"'BaseVirtualEnvironmentED', -- OBJECT_INSTANCE\n"
	"@ED.BaseVirtualEnvironment, -- OBJECT_VERSION\n"
	"'description', -- FIELD_NAME\n"
	"'en-US', -- LOCALE\n"
	"'default', -- LOOKUP_LOCALE\n"
	"'System can contain a number of virtual environments. Base Class', --TEXT\n"
	"'N' --IS_DELETED\n"
	");\n"
	"\n"
	"\n"
	"\n"
	"\n"
	"UPDATE EVA_ENTITY_DEFINITION\n"
	"SET (LOGICAL_OBJ_PATH, INTERFACE_PATH, SUPER_ENTITY_DEFINITION, SUPER_ENTITY_DEFINITION_ENV_ID) = ('PRJFrameworkEVA.Implementation.VirtualEnvironment.Objects.PRJVirtualEnvironment', 'PRJFrameworkEVA.API.Interfaces.EIPRJVirtualEnvironment', @ED.BaseVirtualEnvironment, @ENV.Dflt) WHERE ID = @ED.VirtualEnvironment AND ENV_ID = @ENV.Dflt AND RELEASE_ID = @RELEASE.ID;")
    actual =sqlparser.parse_assertable_statements(actual)
    
    assert expected == actual

def test_extend_entity_runs_succesfully():
    query=("INSERT INTO EVA_ENTITY_DEFINITION (ID, ENV_ID, NAME, UUID, TYPE_UUID, TYPE_ID, TYPE_ENV_ID, LOGICAL_OBJ_PATH, INTERFACE_PATH, SUPER_ENTITY_DEFINITION, SUPER_ENTITY_DEFINITION_ENV_ID, IS_DELETED, IS_BASIC, SUPPORTS_READONLY,IS_EXPANDABLE,ICON_PATH, INSTANCE_ICON_PATH) VALUES (\n"
	"@ED.BaseVirtualEnvironment, @ENV.Dflt, 'BaseVirtualEnvironmentED', 'BaseVirtualEnvironmentED', 'BaseVirtualEnvironmentED', @ET.BaseVirtualEnvironment, @ENV.Dflt, 'FrameworkEVA.Implementation.VirtualEnvironment.Objects.VirtualEnvironment', 'FrameworkEVA.API.Interfaces.EIVirtualEnvironment', NULL, @ENV.Dflt, 'N', 'Y', 'Y', 'N', NULL, NULL );\n"
	"INSERT INTO EVA_CATEGORY_ENTRY(CATEGORY_ID, CATEGORY_ENV_ID, ENTITY_ID, ENTITY_ENV_ID) VALUES (\n"
	"  @EC.SystemGeneral, @ENV.Dflt, @ED.BaseVirtualEnvironment, @ENV.Dflt  );\n"
	"\n"
	"INSERT INTO LOCALISED_FIELD (OBJECT_TYPE, OBJECT_INSTANCE, OBJECT_VERSION, FIELD_NAME, LOCALE, LOOKUP_LOCALE,TEXT,IS_DELETED) VALUES (\n"
	"'EntityDefinitionED', 'BaseVirtualEnvironmentED', @ED.BaseVirtualEnvironment, 'displayName', 'en-US', 'default', 'Virtual Environment Base Class', 'N' );\n"
	"INSERT INTO LOCALISED_FIELD (OBJECT_TYPE, OBJECT_INSTANCE, OBJECT_VERSION, FIELD_NAME, LOCALE, LOOKUP_LOCALE,TEXT,IS_DELETED) VALUES (\n"
	"'EntityDefinitionED', 'BaseVirtualEnvironmentED', @ED.BaseVirtualEnvironment, 'description', 'en-US', 'default', 'System can contain a number of virtual environments. Base Class', 'N' );\n"
	"UPDATE EVA_ENTITY_DEFINITION\n"
	"SET (LOGICAL_OBJ_PATH, INTERFACE_PATH, SUPER_ENTITY_DEFINITION, SUPER_ENTITY_DEFINITION_ENV_ID) = ('PRJFrameworkEVA.Implementation.VirtualEnvironment.Objects.PRJVirtualEnvironment', 'PRJFrameworkEVA.API.Interfaces.EIPRJVirtualEnvironment', @ED.BaseVirtualEnvironment, @ENV.Dflt) WHERE ID = @ED.VirtualEnvironment AND ENV_ID = @ENV.Dflt AND RELEASE_ID = @RELEASE.ID;")
    emprj_path=("/mnt/c/em//projects/pacificorp")
    app_project = AppProject(emprj_path=emprj_path)
    sqlparser =SQLParser(RelativeIdLoader())
    app_project.addb.execute(query,sqlparser=sqlparser)

def test_rendering_register_channel_state_manager_listener_matches_expected_sql():
    expected=("INSERT INTO EVA_DYNAMIC_VERB_LIST (ID,ENV_ID,RELEASE_ID,TYPE_ID,TYPE_ENV_ID,ENTITY_TYPE_ID,ENTITY_TYPE_ENV_ID,VERB_NAME,SEQUENCE_NO,TENANT_ID)\n"
	"VALUES (@EDVL.TelephonyConfigStart, @ENV.Dflt, @RELEASE.ID, @EDVLT.RegisterContactListeners, @ENV.Dflt, @ET.TelephonyConfig, @ENV.Dflt, 'start', @RELEASE.ID, 'default');")
    sqlparser =SQLParser()
    expected =sqlparser.parse_assertable_statements(expected)
    
    actual=("\n"
	" \n"
	"INSERT INTO EVA_DYNAMIC_VERB_LIST (ID,ENV_ID,RELEASE_ID,TYPE_ID,TYPE_ENV_ID,ENTITY_TYPE_ID,ENTITY_TYPE_ENV_ID,VERB_NAME,SEQUENCE_NO,TENANT_ID)\n"
	"VALUES (@EDVL.TelephonyConfigStart, --ID\n"
	"		@ENV.Dflt, --ENV_ID\n"
	"		@RELEASE.ID, --RELEASE_ID\n"
	"		@EDVLT.RegisterContactListeners, -- TYPE_ID\n"
	"		@ENV.Dflt, --TYPE_ENV_ID\n"
	"		@ET.TelephonyConfig, --ENTITY_TYPE_ID\n"
	"		@ENV.Dflt,--ENTITY_TYPE_ENV_ID\n"
	"		'start',--VERB_NAME\n"
	"		@RELEASE.ID,--RELEASE_ID\n"
	"		'default'--TENANT_ID\n"
	"		);")
    actual =sqlparser.parse_assertable_statements(actual)
    
    assert expected == actual

def test_register_channel_state_manager_listener_runs_succesfully():
    query=("INSERT INTO EVA_DYNAMIC_VERB_LIST (ID,ENV_ID,RELEASE_ID,TYPE_ID,TYPE_ENV_ID,ENTITY_TYPE_ID,ENTITY_TYPE_ENV_ID,VERB_NAME,SEQUENCE_NO,TENANT_ID)\n"
	"VALUES (@EDVL.TelephonyConfigStart, @ENV.Dflt, @RELEASE.ID, @EDVLT.RegisterContactListeners, @ENV.Dflt, @ET.TelephonyConfig, @ENV.Dflt, 'start', @RELEASE.ID, 'default');")
    emprj_path=("/mnt/c/em//projects/pacificorp")
    app_project = AppProject(emprj_path=emprj_path)
    sqlparser =SQLParser(RelativeIdLoader())
    app_project.addb.execute(query,sqlparser=sqlparser)

def test_rendering_remove_base_entity_matches_expected_sql():
    expected=("UPDATE EVA_ENTITY_DEFINITION\n"
	"SET (LOGICAL_OBJ_PATH, INTERFACE_PATH, SUPER_ENTITY_DEFINITION, SUPER_ENTITY_DEFINITION_ENV_ID) = ('CoreEntities.Implementation.Customer.Customer', 'CoreEntities.API.Interfaces.EICustomer', @ED.Person, @ENV.Dflt)\n"
	"WHERE ID = @ED.Customer AND ENV_ID = @ENV.Dflt AND RELEASE_ID = @RELEASE.ID;\n"
	"\n"
	"DELETE FROM EVA_ENTITY_DEFINITION\n"
	"WHERE ID = @ED.PreExtendedBaseCustomer;\n"
	"\n"
	"DELETE FROM EVA_CATEGORY_ENTRY WHERE ENTITY_ID = @ED.PreExtendedBaseCustomer;\n"
	"\n"
	"DELETE FROM LOCALISED_FIELD\n"
	"WHERE OBJECT_VERSION = @ED.PreExtendedBaseCustomer\n"
	"AND OBJECT_TYPE = 'EntityDefinitionED';\n"
	"\n"
	"DELETE\n"
	"FROM CCADMIN_IDMAP\n"
	"WHERE KEYSET = 'ED'\n"
	"AND ID =@ED.PreExtendedBaseCustomer;")
    sqlparser =SQLParser()
    expected =sqlparser.parse_assertable_statements(expected)
    
    actual=("\n"
	"UPDATE EVA_ENTITY_DEFINITION\n"
	"SET (LOGICAL_OBJ_PATH, INTERFACE_PATH, SUPER_ENTITY_DEFINITION, SUPER_ENTITY_DEFINITION_ENV_ID) = ('CoreEntities.Implementation.Customer.Customer', 'CoreEntities.API.Interfaces.EICustomer', @ED.Person, @ENV.Dflt) \n"
	"WHERE ID = @ED.Customer AND ENV_ID = @ENV.Dflt AND RELEASE_ID = @RELEASE.ID;\n"
	"\n"
	"DELETE\n"
	"FROM EVA_ENTITY_DEFINITION\n"
	"WHERE ID = @ED.PreExtendedBaseCustomer;\n"
	"\n"
	"DELETE FROM EVA_CATEGORY_ENTRY WHERE ENTITY_ID = @ED.PreExtendedBaseCustomer;\n"
	"\n"
	"DELETE\n"
	"FROM LOCALISED_FIELD\n"
	"WHERE OBJECT_VERSION = @ED.PreExtendedBaseCustomer\n"
	"AND OBJECT_TYPE = 'EntityDefinitionED';\n"
	"\n"
	"DELETE\n"
	"FROM CCADMIN_IDMAP\n"
	"WHERE KEYSET = 'ED'\n"
	"AND ID =@ED.PreExtendedBaseCustomer;\n"
	"\n"
	"")
    actual =sqlparser.parse_assertable_statements(actual)
    
    assert expected == actual

def test_remove_base_entity_runs_succesfully():
    query=("UPDATE EVA_ENTITY_DEFINITION\n"
	"SET (LOGICAL_OBJ_PATH, INTERFACE_PATH, SUPER_ENTITY_DEFINITION, SUPER_ENTITY_DEFINITION_ENV_ID) = ('CoreEntities.Implementation.Customer.Customer', 'CoreEntities.API.Interfaces.EICustomer', @ED.Person, @ENV.Dflt)\n"
	"WHERE ID = @ED.Customer AND ENV_ID = @ENV.Dflt AND RELEASE_ID = @RELEASE.ID;\n"
	"\n"
	"DELETE FROM EVA_ENTITY_DEFINITION\n"
	"WHERE ID = @ED.PreExtendedBaseCustomer;\n"
	"\n"
	"DELETE FROM EVA_CATEGORY_ENTRY WHERE ENTITY_ID = @ED.PreExtendedBaseCustomer;\n"
	"\n"
	"DELETE FROM LOCALISED_FIELD\n"
	"WHERE OBJECT_VERSION = @ED.PreExtendedBaseCustomer\n"
	"AND OBJECT_TYPE = 'EntityDefinitionED';\n"
	"\n"
	"DELETE\n"
	"FROM CCADMIN_IDMAP\n"
	"WHERE KEYSET = 'ED'\n"
	"AND ID =@ED.PreExtendedBaseCustomer;")
    emprj_path=("/mnt/c/em//projects/pacificorp")
    app_project = AppProject(emprj_path=emprj_path)
    sqlparser =SQLParser(RelativeIdLoader())
    app_project.addb.execute(query,sqlparser=sqlparser)

def test_rendering_remove_entity_definition_matches_expected_sql():
    expected=("DELETE FROM EVA_ENTITY_DEFINITION\n"
	"WHERE ID = @ED.VerbAudit;\n"
	"\n"
	"DELETE FROM EVA_CATEGORY_ENTRY WHERE ENTITY_ID = @ED.VerbAudit;\n"
	"\n"
	"DELETE FROM LOCALISED_FIELD\n"
	"WHERE OBJECT_VERSION = @ED.VerbAudit\n"
	"AND OBJECT_TYPE = 'EntityDefinitionED';\n"
	"\n"
	"DELETE\n"
	"FROM CCADMIN_IDMAP\n"
	"WHERE KEYSET = 'ED'\n"
	"AND ID =@ED.VerbAudit;")
    sqlparser =SQLParser()
    expected =sqlparser.parse_assertable_statements(expected)
    
    actual=("DELETE\n"
	"FROM EVA_ENTITY_DEFINITION\n"
	"WHERE ID = @ED.VerbAudit;\n"
	"\n"
	"DELETE FROM EVA_CATEGORY_ENTRY WHERE ENTITY_ID = @ED.VerbAudit;\n"
	"\n"
	"DELETE\n"
	"FROM LOCALISED_FIELD\n"
	"WHERE OBJECT_VERSION = @ED.VerbAudit\n"
	"AND OBJECT_TYPE = 'EntityDefinitionED';\n"
	"\n"
	"DELETE\n"
	"FROM CCADMIN_IDMAP\n"
	"WHERE KEYSET = 'ED'\n"
	"AND ID =@ED.VerbAudit;")
    actual =sqlparser.parse_assertable_statements(actual)
    
    assert expected == actual

def test_remove_entity_definition_runs_succesfully():
    query=("DELETE FROM EVA_ENTITY_DEFINITION\n"
	"WHERE ID = @ED.VerbAudit;\n"
	"\n"
	"DELETE FROM EVA_CATEGORY_ENTRY WHERE ENTITY_ID = @ED.VerbAudit;\n"
	"\n"
	"DELETE FROM LOCALISED_FIELD\n"
	"WHERE OBJECT_VERSION = @ED.VerbAudit\n"
	"AND OBJECT_TYPE = 'EntityDefinitionED';\n"
	"\n"
	"DELETE\n"
	"FROM CCADMIN_IDMAP\n"
	"WHERE KEYSET = 'ED'\n"
	"AND ID =@ED.VerbAudit;")
    emprj_path=("/mnt/c/em//projects/pacificorp")
    app_project = AppProject(emprj_path=emprj_path)
    sqlparser =SQLParser(RelativeIdLoader())
    app_project.addb.execute(query,sqlparser=sqlparser)

def test_rendering_remove_verb_from_entity_matches_expected_sql():
    expected=("DELETE\n"
	"FROM EVA_VERB\n"
	"WHERE ID =@V.InlineSearchCustomer\n"
	"and ENTITY_DEF_ID=@ED.Customer;\n"
	"\n"
	"DELETE\n"
	"FROM CCADMIN_IDMAP\n"
	"WHERE KEYSET = 'V'\n"
	"AND ID =@V.InlineSearchCustomer;")
    sqlparser =SQLParser()
    expected =sqlparser.parse_assertable_statements(expected)
    
    actual=("\n"
	"DELETE\n"
	"FROM EVA_VERB\n"
	"WHERE ID = @V.InlineSearchCustomer\n"
	"and ENTITY_DEF_ID=@ED.Customer;\n"
	"\n"
	"\n"
	"DELETE\n"
	"FROM CCADMIN_IDMAP\n"
	"WHERE KEYSET = 'V'\n"
	"AND ID =@V.InlineSearchCustomer;")
    actual =sqlparser.parse_assertable_statements(actual)
    
    assert expected == actual

def test_remove_verb_from_entity_runs_succesfully():
    query=("DELETE\n"
	"FROM EVA_VERB\n"
	"WHERE ID =@V.InlineSearchCustomer\n"
	"and ENTITY_DEF_ID=@ED.Customer;\n"
	"\n"
	"DELETE\n"
	"FROM CCADMIN_IDMAP\n"
	"WHERE KEYSET = 'V'\n"
	"AND ID =@V.InlineSearchCustomer;")
    emprj_path=("/mnt/c/em//projects/pacificorp")
    app_project = AppProject(emprj_path=emprj_path)
    sqlparser =SQLParser(RelativeIdLoader())
    app_project.addb.execute(query,sqlparser=sqlparser)

def test_rendering_rewire_verb_matches_expected_sql():
    expected=("INSERT INTO EVA_PROCESS_DESCRIPTOR (ID, ENV_ID, NAME, REPOSITORY_PATH, CONFIG_PROCESS_ID, IS_DELETED, TYPE)\n"
	"VALUES (\n"
	"	 @PD.PRJCustomerIdentifycustomer, @ENV.Dflt, 'PRJCustomerIdentifycustomer', 'PRJCoreEntities.Implementation.Customer.Verbs.IdentifyCustomerWrapper', NULL, 'N', @PDT.Verb  );\n"
	"\n"
	"INSERT INTO LOCALISED_FIELD (OBJECT_TYPE, OBJECT_INSTANCE, OBJECT_VERSION, FIELD_NAME, LOCALE, LOOKUP_LOCALE,TEXT,IS_DELETED) VALUES (\n"
	"'ProcessDescriptorED', 'PRJCustomerIdentifycustomer__PRJCoreEntities/Implementation/Customer/Verbs/IdentifyCustomerWrapper', @PD.PRJCustomerIdentifycustomer, 'displayName', 'en-US', 'default', 'PRJCustomerIdentifycustomer', 'N'\n"
	");\n"
	"\n"
	"INSERT INTO LOCALISED_FIELD (OBJECT_TYPE, OBJECT_INSTANCE, OBJECT_VERSION, FIELD_NAME, LOCALE, LOOKUP_LOCALE,TEXT,IS_DELETED) VALUES (\n"
	"'ProcessDescriptorED', 'PRJCustomerIdentifycustomer__PRJCoreEntities/Implementation/Customer/Verbs/IdentifyCustomerWrapper', @PD.PRJCustomerIdentifycustomer, 'description', 'en-US', 'default', 'PRJCustomerIdentifycustomer', 'N'\n"
	");\n"
	"\n"
	"INSERT INTO EVA_PROCESS_DESC_REFERENCE (ID, PROCESS_DESCRIPTOR_ID, PROCESS_DESCRIPTOR_ENV_ID, CONFIG_ID, IS_SHARED)\n"
	"VALUES (\n"
	"	@PDR.PRJCustomerIdentifycustomer, @PD.PRJCustomerIdentifycustomer, @ENV.Dflt, NULL, 'N' );\n"
	"\n"
	"\n"
	"UPDATE EVA_VERB\n"
	"SET (PROCESS_DESC_REF_ID) = (@PDR.PRJCustomerIdentifycustomer)\n"
	"WHERE ENTITY_DEF_ID = @ED.Customer AND NAME ='identifyCustomer';")
    sqlparser =SQLParser()
    expected =sqlparser.parse_assertable_statements(expected)
    
    actual=("\n"
	"\n"
	"\n"
	"\n"
	"INSERT INTO EVA_PROCESS_DESCRIPTOR (ID, ENV_ID, NAME, REPOSITORY_PATH, CONFIG_PROCESS_ID, IS_DELETED, TYPE)\n"
	"VALUES (\n"
	"	 @PD.PRJCustomerIdentifycustomer, --id\n"
	"	 @ENV.Dflt, --env_id,\n"
	"	 'PRJCustomerIdentifycustomer', --process_descriptor_name\n"
	"	 'PRJCoreEntities.Implementation.Customer.Verbs.IdentifyCustomerWrapper', --repository_path\n"
	"	 NULL, --config_id\n"
	"	 'N', --is_deleted\n"
	"	 @PDT.Verb --type\n"
	"       );\n"
	"\n"
	"INSERT INTO LOCALISED_FIELD (OBJECT_TYPE, OBJECT_INSTANCE, OBJECT_VERSION, FIELD_NAME, LOCALE, LOOKUP_LOCALE,TEXT,IS_DELETED) VALUES (\n"
	"'ProcessDescriptorED', -- OBJECT_TYPE\n"
	"'PRJCustomerIdentifycustomer__PRJCoreEntities/Implementation/Customer/Verbs/IdentifyCustomerWrapper', -- OBJECT_INSTANCE\n"
	"@PD.PRJCustomerIdentifycustomer, -- OBJECT_VERSION\n"
	"'displayName', -- FIELD_NAME\n"
	"'en-US', -- LOCALE\n"
	"'default', -- LOOKUP_LOCALE\n"
	"'PRJCustomerIdentifycustomer', --TEXT\n"
	"'N' --IS_DELETED\n"
	");\n"
	"\n"
	"\n"
	"INSERT INTO LOCALISED_FIELD (OBJECT_TYPE, OBJECT_INSTANCE, OBJECT_VERSION, FIELD_NAME, LOCALE, LOOKUP_LOCALE,TEXT,IS_DELETED) VALUES (\n"
	"'ProcessDescriptorED', -- OBJECT_TYPE\n"
	"'PRJCustomerIdentifycustomer__PRJCoreEntities/Implementation/Customer/Verbs/IdentifyCustomerWrapper', -- OBJECT_INSTANCE\n"
	"@PD.PRJCustomerIdentifycustomer, -- OBJECT_VERSION\n"
	"'description', -- FIELD_NAME\n"
	"'en-US', -- LOCALE\n"
	"'default', -- LOOKUP_LOCALE\n"
	"'PRJCustomerIdentifycustomer', --TEXT\n"
	"'N' --IS_DELETED\n"
	");\n"
	"\n"
	"\n"
	"\n"
	"INSERT INTO EVA_PROCESS_DESC_REFERENCE (ID, PROCESS_DESCRIPTOR_ID, PROCESS_DESCRIPTOR_ENV_ID, CONFIG_ID, IS_SHARED) \n"
	"VALUES (\n"
	"        @PDR.PRJCustomerIdentifycustomer, --id\n"
	"        @PD.PRJCustomerIdentifycustomer, --process_descriptor_id\n"
	"	@ENV.Dflt, --process_descriptor_env_id\n"
	"	NULL, --config_id\n"
	"       	'N' --is_shared\n"
	"       );\n"
	"\n"
	"\n"
	"\n"
	"UPDATE EVA_VERB \n"
	"SET (PROCESS_DESC_REF_ID) = (@PDR.PRJCustomerIdentifycustomer)\n"
	"WHERE ENTITY_DEF_ID = @ED.Customer AND NAME ='identifyCustomer';\n"
	"\n"
	"\n"
	"\n"
	"")
    actual =sqlparser.parse_assertable_statements(actual)
    
    assert expected == actual

def test_rewire_verb_runs_succesfully():
    query=("INSERT INTO EVA_PROCESS_DESCRIPTOR (ID, ENV_ID, NAME, REPOSITORY_PATH, CONFIG_PROCESS_ID, IS_DELETED, TYPE)\n"
	"VALUES (\n"
	"	 @PD.PRJCustomerIdentifycustomer, @ENV.Dflt, 'PRJCustomerIdentifycustomer', 'PRJCoreEntities.Implementation.Customer.Verbs.IdentifyCustomerWrapper', NULL, 'N', @PDT.Verb  );\n"
	"\n"
	"INSERT INTO LOCALISED_FIELD (OBJECT_TYPE, OBJECT_INSTANCE, OBJECT_VERSION, FIELD_NAME, LOCALE, LOOKUP_LOCALE,TEXT,IS_DELETED) VALUES (\n"
	"'ProcessDescriptorED', 'PRJCustomerIdentifycustomer__PRJCoreEntities/Implementation/Customer/Verbs/IdentifyCustomerWrapper', @PD.PRJCustomerIdentifycustomer, 'displayName', 'en-US', 'default', 'PRJCustomerIdentifycustomer', 'N'\n"
	");\n"
	"\n"
	"INSERT INTO LOCALISED_FIELD (OBJECT_TYPE, OBJECT_INSTANCE, OBJECT_VERSION, FIELD_NAME, LOCALE, LOOKUP_LOCALE,TEXT,IS_DELETED) VALUES (\n"
	"'ProcessDescriptorED', 'PRJCustomerIdentifycustomer__PRJCoreEntities/Implementation/Customer/Verbs/IdentifyCustomerWrapper', @PD.PRJCustomerIdentifycustomer, 'description', 'en-US', 'default', 'PRJCustomerIdentifycustomer', 'N'\n"
	");\n"
	"\n"
	"INSERT INTO EVA_PROCESS_DESC_REFERENCE (ID, PROCESS_DESCRIPTOR_ID, PROCESS_DESCRIPTOR_ENV_ID, CONFIG_ID, IS_SHARED)\n"
	"VALUES (\n"
	"	@PDR.PRJCustomerIdentifycustomer, @PD.PRJCustomerIdentifycustomer, @ENV.Dflt, NULL, 'N' );\n"
	"\n"
	"\n"
	"UPDATE EVA_VERB\n"
	"SET (PROCESS_DESC_REF_ID) = (@PDR.PRJCustomerIdentifycustomer)\n"
	"WHERE ENTITY_DEF_ID = @ED.Customer AND NAME ='identifyCustomer';")
    emprj_path=("/mnt/c/em//projects/pacificorp")
    app_project = AppProject(emprj_path=emprj_path)
    sqlparser =SQLParser(RelativeIdLoader())
    app_project.addb.execute(query,sqlparser=sqlparser)

def test_rendering_unregister_channel_state_manager_listener_matches_expected_sql():
    expected=("DELETE FROM EVA_DYNAMIC_VERB_LIST\n"
	"WHERE ID = @EDVL.StartInteractionFactMonitor;\n"
	"\n"
	"DELETE FROM CCADMIN_IDMAP\n"
	"WHERE KEYSET = 'EDVL' AND KEYNAME='StartInteractionFactMonitor';")
    sqlparser =SQLParser()
    expected =sqlparser.parse_assertable_statements(expected)
    
    actual=("DELETE FROM EVA_DYNAMIC_VERB_LIST \n"
	"WHERE ID = @EDVL.StartInteractionFactMonitor;\n"
	"\n"
	"DELETE FROM CCADMIN_IDMAP \n"
	"WHERE KEYSET = 'EDVL' AND KEYNAME='StartInteractionFactMonitor';")
    actual =sqlparser.parse_assertable_statements(actual)
    
    assert expected == actual

def test_unregister_channel_state_manager_listener_runs_succesfully():
    query=("DELETE FROM EVA_DYNAMIC_VERB_LIST\n"
	"WHERE ID = @EDVL.StartInteractionFactMonitor;\n"
	"\n"
	"DELETE FROM CCADMIN_IDMAP\n"
	"WHERE KEYSET = 'EDVL' AND KEYNAME='StartInteractionFactMonitor';")
    emprj_path=("/mnt/c/em//projects/pacificorp")
    app_project = AppProject(emprj_path=emprj_path)
    sqlparser =SQLParser(RelativeIdLoader())
    app_project.addb.execute(query,sqlparser=sqlparser)

def test_rendering_update_agent_password_matches_expected_sql():
    expected=("update agent\n"
	"set PASSWORD = (select PASSWORD from AGENT where username ='admin'),\n"
	" SALT = (select SALT from agent where username = 'admin'),\n"
	" EXPIRES = (select EXPIRES from AGENT where USERNAME = 'admin'),\n"
	" DISABLED ='no',\n"
	" LASTLOGGEDIN = SYSDATE\n"
	"where USERNAME in ('ccagent');")
    sqlparser =SQLParser()
    expected =sqlparser.parse_assertable_statements(expected)
    
    actual=("--update agent password\n"
	"update agent\n"
	"set PASSWORD = (select PASSWORD from AGENT where username ='admin'),\n"
	" SALT = (select SALT from agent where username = 'admin'),\n"
	" EXPIRES = (select EXPIRES from AGENT where USERNAME = 'admin'),\n"
	" DISABLED ='no',\n"
	" LASTLOGGEDIN = SYSDATE\n"
	"where USERNAME in ('ccagent');")
    actual =sqlparser.parse_assertable_statements(actual)
    
    assert expected == actual

def test_update_agent_password_runs_succesfully():
    query=("update agent\n"
	"set PASSWORD = (select PASSWORD from AGENT where username ='admin'),\n"
	" SALT = (select SALT from agent where username = 'admin'),\n"
	" EXPIRES = (select EXPIRES from AGENT where USERNAME = 'admin'),\n"
	" DISABLED ='no',\n"
	" LASTLOGGEDIN = SYSDATE\n"
	"where USERNAME in ('ccagent');")
    emprj_path=("/mnt/c/em//projects/pacificorp")
    app_project = AppProject(emprj_path=emprj_path)
    sqlparser =SQLParser(RelativeIdLoader())
    app_project.addb.execute(query,sqlparser=sqlparser)

def test_rendering_update_ccadmin_version_matches_expected_sql():
    expected=("update ccadmin_version\n"
	"set upgrade_version =345\n"
	"where RELEASE_NAME = 'Pacificorp_R_0_0_1';")
    sqlparser =SQLParser()
    expected =sqlparser.parse_assertable_statements(expected)
    
    actual=(" \n"
	"\n"
	"update ccadmin_version\n"
	"set upgrade_version =345\n"
	"where RELEASE_NAME = 'Pacificorp_R_0_0_1';")
    actual =sqlparser.parse_assertable_statements(actual)
    
    assert expected == actual

def test_update_ccadmin_version_runs_succesfully():
    query=("update ccadmin_version\n"
	"set upgrade_version =345\n"
	"where RELEASE_NAME = 'Pacificorp_R_0_0_1';")
    emprj_path=("/mnt/c/em//projects/pacificorp")
    app_project = AppProject(emprj_path=emprj_path)
    sqlparser =SQLParser(RelativeIdLoader())
    app_project.addb.execute(query,sqlparser=sqlparser)