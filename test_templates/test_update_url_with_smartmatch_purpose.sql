-- {'url_to_update':'MyTestCustomerURL','url_path':'{"@type": "vcust:Customer" }'}
UPDATE FWI_URL
set 
PATH =('{"@type": "vcust:Customer" }')
WHERE ID = @WIU.MyTestCustomerURL
