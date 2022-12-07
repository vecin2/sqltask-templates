{% set __entitlement_system_name = entitlement_system_name | suggest(_keynames.ENTLMNT) %}
	SELECT
		eed.TYPE_ID,
		eed.name AS ENTITY_TYPE,
		ee.ENTITY_ID,
		fpt.SYSTEM_NAME as entity_name
	FROM
		EVA_ENTITLEMENT e INNER JOIN CCADMIN_IDMAP idmap ON e.id = idmap.id 
		INNER JOIN EVA_ENTITY__ENTITLEMENT ee ON ee.ENTITLEMENT_ID = e.ID
		INNER JOIN EVA_ENTITY_DEFINITION eed ON  eed.TYPE_ID  = ee.ENTITY_TYPE_ID 
		LEFT JOIN FD_PROFILE_TYPE fpt  ON ee.ENTITY_ID = fpt.ID 
	WHERE		
		idmap.keyset = 'ENTLMNT'
		AND e.SYSTEM_NAME  LIKE '%{{__entitlement_system_name}}%'
		
