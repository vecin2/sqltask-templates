--{"host_display_name":"My Local","protocol_property_name":"internal.connection.protocol","host_property_name":"external.agentdesktop.host","port_property_name":"external.agentdesktop.port"}
def output = properties['output']
def outwriter = new PrintWriter(output)
def preferredDefaultLocale = project.getProperty("preferred.default.locale")
def tenantId = project.getProperty("tenant.id")
def externalProtocol = project.getProperty("internal.connection.protocol")
def externalHostname = project.getProperty("external.agentdesktop.host")
def externalPort = project.getProperty("external.agentdesktop.port")

try {
    //Web Integration Host
    outwriter.println("INSERT INTO FWI_HOST (ID, ENV_ID, RELEASE_ID, UUID, PROTOCOL, HOSTNAME, PORT_NUMBER, IS_DELETED) VALUES (@FWIH.MyLocal, @ENV.Dflt, @RELEASE.ID, 'MyLocalUUID', '${externalProtocol}', '${externalHostname}', '${externalPort}', 'N');")
    outwriter.println("INSERT INTO LOCALISED_FIELD (OBJECT_TYPE, OBJECT_INSTANCE, OBJECT_VERSION, FIELD_NAME, LOCALE, LOOKUP_LOCALE, TEXT, IS_DELETED) VALUES ('WebIntegrationHostED', 'MyLocalUUID', @FWIH.MyLocal, 'displayName', '${preferredDefaultLocale}', 'default', 'My Local', 'N');")
    outwriter.println("INSERT INTO EVA_MIGRATABLE (ENTITY_ID, ENTITY_ENV_ID, RELEASE_ID, TYPE_NAME, MIGRATABLE_REFERENCE, VERSION, IS_REMOTE, ENTITY_VERSION, IS_DELETED, INCLUDE_IN_EXPORT, EXPORT_LOCALE, ENTITY_MINOR_VERSION, TENANT_ID) VALUES (@FWIH.MyLocal, @ENV.Dflt, @RELEASE.ID, 'WebIntegrationHostED', 'MyLocalUUID', '1', 'N', 0, 'N', 'Y', 'ALL', 0, '${tenantId}');")
} finally {
    outwriter.close()
}
