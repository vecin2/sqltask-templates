{% set __host_keyname = host_keyname | suggest(_keynames.FWIH) %}
{% set __host_urls = _db.fetch.host_urls(__host_keyname) %}
{% set __suggested_url_keynames = __host_urls.column("URL_KEYNAME") %}
{% set __url_keyname = url_keyname | suggest(__suggested_url_keynames) | print(__host_urls)%}

DELETE FROM EVA_ENTITY__TAGSET_SELECTION
WHERE ENTITY_ID = @WIU.{{__url_keyname}};

DELETE FROM LOCALISED_FIELD
WHERE OBJECT_VERSION = @WIU.{{__url_keyname}}
and OBJECT_TYPE = 'WebIntegrationURLED';

DELETE FROM FWI_URL
WHERE ID = @WIU.{{__url_keyname}};

DELETE FROM EVA_TAGSET_SELECTION
WHERE ID = @WIU.{{__url_keyname}};

