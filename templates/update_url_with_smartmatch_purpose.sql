{% set _url_keyname= url_to_update | suggest(_keynames.WIU) %}
{% set json_body_sample='{
  "@type": "vcust:Customer",
  "vcust:familyName": "[[::_workitem.channelInteraction.customerLastName_::]]",
  "vcust:givenName": "[[::_workitem.channelInteraction.customerFirstName_::]]",
  "vchan:phoneNumbers": [
    {
      "@type": "vchan:PhoneNumber",
      "vchan:isPreferred": true,
      "vchan:contactDetailType": "Home",
      "vchan:phoneNumber": "[[::_workitem.channelInteraction.launchEntity.duMobileNumber_::]]"
    }
  ],
	"vchan:emailAddresses" : [ {
			"@type" : "vchan:EmailAddress",
			"vchan:isPreferred" : true,
			"vchan:contactDetailType" : "Home",
			"vchan:emailAddress" : "[[::_workitem.channelInteraction.customerEmail_::]]"
		}]
}' %}
{% set url_path_help =  "This is the  url's body, don't include quotes around the text, for example for json request type:\n" + json_body_sample %}

{% set _url_path = url_path  | print(url_path_help) %}
UPDATE FWI_URL
set 
PATH =('{{_url_path}}')
WHERE ID = @WIU.{{_url_keyname}}
