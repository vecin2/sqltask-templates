{#
[oneline_description]
Adds a host which can then be used when building a URL within Rules
#}
{%set _hostname = hostname | print("Enter a valid hostname,for example localhost") %}
{%set portname = hostname | print("Enter a valid port number,for example 8280") %}
{%set protocols = ["http","https"] %}
{%set _protocol = protocol | suggest(protocols) %}
{%set _keyname = _hostname + _protocol %}
INSERT INTO FWI_HOST
(ID, ENV_ID, RELEASE_ID, UUID, PROTOCOL, HOSTNAME, PORT_NUMBER, IS_DELETED)
VALUES(@FWIH.{{_keyname}}, @ENV.Dflt, @RELEASE.ID, 'abc', 'http', '{{_hostname}}', '{{protocol}}', 'N');
