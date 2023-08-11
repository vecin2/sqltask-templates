--{"action":"BOTH","index_name":"chatbot_body","type":"stemmed","weight":"1.0","weigth_as_string":"Medium", "system":"false", "content_types":"'KnowledgeAlertED', 'KnowledgeArticleED', 'KnowledgeFAQED'","field_name":"region","entitlements":"ManageAgents","entitled_search":"true"}
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

// Add index field  {"name":"chatbot_body","type":"stemmed","weight":1.0,"weightAsString":"Medium","system":false}
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
        if (x.name == "chatbot_body") { hasIndex = true }
    }
    if ( !hasIndex ) {
        object.indexFields.push( ["name":"chatbot_body","type":"stemmed","weight":1.0,"weightAsString":"Medium","system":false] )
        outwriter.println "UPDATE SEARCH_CONFIGURATION SET (ITEM_VALUE) = ( '${JsonOutput.toJson(object)}' ) " +
             "WHERE ITEM_TYPE = 'IndexFlds' AND ITEM_NAME = 'IndexFlds';"

    }

}
//Map the field for each content type { "contentField": "region", "indexField": "chatbot_body", "shared": [], "entitlements": [ManageAgents] }
sql.eachRow("SELECT ITEM_VALUE, ITEM_NAME FROM SEARCH_CONFIGURATION WHERE ITEM_TYPE = 'ContentFormat' AND ITEM_NAME IN ('KnowledgeAlertED', 'KnowledgeArticleED', 'KnowledgeFAQED')") { row ->
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
        if (x.contentField == "region" && x.indexField == "chatbot_body") { hasMapping = true }
    }

	if( !hasMapping) {
		object.mapping.push( ["contentField" : "region", "indexField" : "chatbot_body", "shared" : [], "entitlements" : ["ManageAgents"], "entitledSearch" : true ] )
        outwriter.println "UPDATE SEARCH_CONFIGURATION SET (ITEM_VALUE) = ( '${JsonOutput.toJson(object)}' ) " +
             "WHERE ITEM_TYPE = 'ContentFormat' AND ITEM_NAME = '" + row.ITEM_NAME + "';"
	}
}

outwriter.close()
DBUtil.cleanup()
