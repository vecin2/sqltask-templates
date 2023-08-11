import java.sql.Clob
import groovy.sql.Sql
import groovy.json.JsonSlurper
import groovy.json.JsonOutput
import groovy.sql.GroovyRowResult

def url = project.getProperty("database.url")
def driver = project.getProperty("database.driver")
def user = project.getProperty("database.user")
def pass = project.getProperty("database.pass")
Sql sql = Sql.newInstance(url, user, pass, driver)
def output = properties['output']
def outwriter = new PrintWriter(output)

{% set __action = action | description("Are you creating an index, mapping an existing index to a field, or both?") | suggest(["INDEX","MAP","BOTH"])%}
{% set __index_name = index_name | suggest(["tags","title","..."])%}
{% if __action == "INDEX" or __action == "BOTH" %}
{% set help_message =
' This are some sample of index values
		{
			"name": "chatbot_body",
			"type": "stemmed",
			"weight": 1.0,
			"weightAsString": "Medium",
			"system": false
		},
		{
			"name": "must_read",
			"type": "boolean",
			"weight": 1.0,
			"weightAsString": "Medium",
			"system": true
		},
		{
			"name": "tags",
			"type": "multi-tag",
			"weight": 0.1,
			"weightAsString": "Low",
			"system": true
		},
		{
			"name": "title",
			"type": "stemmed",
			"weight": 10.0,
			"weightAsString": "High",
			"system": true
		}
'
%}
{% set suggested_types= ["boolean","multi-tag","stemmed","multi-keyword","keyword","date","int","float"]%}
{% set __type = type | suggest(suggested_types) | print("Suggesting some possible types, could be other types")%}
{% set __weight = weight | print("samples of weight: 1.0, 0.1...") %}
{% set __weight_as_string = weight_as_string | suggest(["Low","Medium","High"])%}
{% set __is_system_field = is_system_field | suggest(["true","false"])%}
// Add index field  {"name":"{{__index_name}}","type":"{{__type}}","weight":{{__weight}},"weightAsString":"{{__weight_as_string}}","system":{{__is_system_field}}}
def indexfields = sql.rows("SELECT ITEM_VALUE FROM SEARCH_CONFIGURATION WHERE ITEM_TYPE = 'IndexFlds'")
for ( GroovyRowResult result: indexfields ) {
    def rawItemValue = result.ITEM_VALUE
    def itemValue

    if (rawItemValue instanceof Clob) {
        def clob = result.ITEM_VALUE as Clob
        itemValue = clob.characterStream.text
    } else {
        itemValue = rawItemValue.toString()
    }

    def jsonSlurper = new JsonSlurper()
    def object = jsonSlurper.parseText(itemValue)
    def hasIndex = false
    for ( Map x : object.indexFields ) {
        if (x.name == "{{__index_name}}") { hasIndex = true }
    }
    if ( !hasIndex ) {
        object.indexFields.push( ["name":"{{__index_name}}","type":"{{__type}}","weight":{{__weight}},"weightAsString":"{{__weight_as_string}}","system":{{__is_system_field}}] )
        outwriter.println "UPDATE SEARCH_CONFIGURATION SET (ITEM_VALUE) = ( '${JsonOutput.toJson(object)}' ) " +
             "WHERE ITEM_TYPE = 'IndexFlds' AND ITEM_NAME = 'IndexFlds';"

    }

}
{% endif %}
{% if __action == "MAP" or __action == "BOTH" %}
{% set content_types_help_msg = "You can add multiple content types with comma separated list (this value will be input into an IN clause), for example: 'KnowledgeAlertED','KnowledgeArticleED','KnowledgeFAQED','KnowledgeUploadED','KnowledgeSegmentED' "%}
{% set content_type_names =["'KnowledgeAlertED'","'KnowledgeArticleED'","'KnowledgeFAQED'","'KnowledgeUploadED'","'KnowledgeSegmentED'"] %}
{% set __content_types = content_types | suggest(content_type_names) | print(content_types_help_msg)%}
{% set field_names = _db.fetch.fields_by_ed_names(__content_types).column("NAME")%}
{% set __field_name = field_name | suggest(field_names) %}
{% set entitlement_names = _db.fetch.all_entitlements().column("SYSTEM_NAME") %}
{% set __entitlement = entitlement | suggest(entitlement_names) %}
{% set quoted_entitlement = "\""+__entitlement+"\"" %}
{% set help_entitled_search = "Select 'none' does not add entitled_search attribute"%}
{% set __entitled_search = entitled_search | suggest(["none","true","false"]) | print(help_entitled_search)%}
{% set and_entitled_search = ""%}
{% if __entitled_search !="none"%}
{% set and_entitled_search = ', "entitledSearch" : '+__entitled_search %}
{%endif%}
//Map the field for each content type { "contentField": "{{__field_name}}", "indexField": "{{__index_name}}", "shared": [], "entitlements": [{{quoted_entitlement}}]{{and_entitled_search}} }
sql.eachRow("SELECT ITEM_VALUE, ITEM_NAME FROM SEARCH_CONFIGURATION WHERE ITEM_TYPE = 'ContentFormat' AND ITEM_NAME IN ({{__content_types}})") { row ->
	def rawItemValue = row.ITEM_VALUE
    def itemValue

    if (rawItemValue instanceof Clob) {
        def clob = row.ITEM_VALUE as Clob
        itemValue = clob.characterStream.text
    } else {
        itemValue = rawItemValue.toString()
    }

	def jsonSlurper = new JsonSlurper()
    def object = jsonSlurper.parseText(itemValue)

	def hasMapping = false
	
    for ( Map x : object.mapping ) {
		// println("Map has" + x.toString())
        if (x.contentField == "{{__field_name}}" && x.indexField == "{{__index_name}}") { hasMapping = true }
    }

	if( !hasMapping) {
		object.mapping.push( ["contentField" : "{{__field_name}}", "indexField" : "{{__index_name}}", "shared" : [], "entitlements" : [{{quoted_entitlement}}]{{and_entitled_search}} ] )
        outwriter.println "UPDATE SEARCH_CONFIGURATION SET (ITEM_VALUE) = ( '${JsonOutput.toJson(object)}' ) " +
             "WHERE ITEM_TYPE = 'ContentFormat' AND ITEM_NAME = '" + row.ITEM_NAME + "';"
	}
}
{%endif%}

outwriter.close()
DBUtil.cleanup()

