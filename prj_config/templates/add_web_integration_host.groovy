{% set _host_display_name = host_display_name | print("This will be display to the user, e.g. localhost or Agent Service Host") %}
{% set _host_keyname = host_display_name.replace(" ","")%}
{% set _host_keyname_uuid = _host_keyname+"UUID"%}

{% set protocol_message ="Please enter the protocol property name where the protocol will be taken from. Examples of protocol_property_name: external.connection.protocol, internal.connection.protocol"%}
{% set protocol_examples =["external.connection.protocol", "internal.connection.protocol"]%}
{% set _protocol_property_name = protocol_property_name | print(protocol_message) | suggest(protocol_examples)%}

{% set host_message ="Please enter the host property name where the host will be taken from. Examples of host_property_name: external.agentdesktop.host"%}
{% set host_examples =["external.agentdesktop.host"]%}
{% set _host_property_name = host_property_name | print(host_message) | suggest(host_examples)%}

{% set port_message ="Please enter the port property name where the host will be taken from. Examples of port_property_name: external.agentdesktop.port"%}
{% set port_examples =["external.agentdesktop.port"]%}
{% set _port_property_name = port_property_name | print(port_message) | suggest(port_examples)%}

def output = properties['output']
def outwriter = new PrintWriter(output)
def preferredDefaultLocale = project.getProperty("preferred.default.locale")
def tenantId = project.getProperty("tenant.id")
def externalProtocol = project.getProperty("{{_protocol_property_name}}")
def externalHostname = project.getProperty("{{_host_property_name}}")
def externalPort = project.getProperty("{{_port_property_name}}")

try {
    //Web Integration Host
    outwriter.println("INSERT INTO FWI_HOST (ID, ENV_ID, RELEASE_ID, UUID, PROTOCOL, HOSTNAME, PORT_NUMBER, IS_DELETED) VALUES (@FWIH.{{_host_keyname}}, @ENV.Dflt, @RELEASE.ID, '{{_host_keyname_uuid}}', '${externalProtocol}', '${externalHostname}', '${externalPort}', 'N');")
    outwriter.println("INSERT INTO LOCALISED_FIELD (OBJECT_TYPE, OBJECT_INSTANCE, OBJECT_VERSION, FIELD_NAME, LOCALE, LOOKUP_LOCALE, TEXT, IS_DELETED) VALUES ('WebIntegrationHostED', '{{_host_keyname_uuid}}', @FWIH.{{_host_keyname}}, 'displayName', '${preferredDefaultLocale}', 'default', '{{_host_display_name}}', 'N');")
    outwriter.println("INSERT INTO EVA_MIGRATABLE (ENTITY_ID, ENTITY_ENV_ID, RELEASE_ID, TYPE_NAME, MIGRATABLE_REFERENCE, VERSION, IS_REMOTE, ENTITY_VERSION, IS_DELETED, INCLUDE_IN_EXPORT, EXPORT_LOCALE, ENTITY_MINOR_VERSION, TENANT_ID) VALUES (@FWIH.{{_host_keyname}}, @ENV.Dflt, @RELEASE.ID, 'WebIntegrationHostED', '{{_host_keyname_uuid}}', '1', 'N', 0, 'N', 'Y', 'ALL', 0, '${tenantId}');")
} finally {
    outwriter.close()
}
