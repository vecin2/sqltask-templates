SELECT pdrid.keyname AS PDR_KEYNAME,pdid.keyname AS PD_KEYNAME,epdr.config_id, epd.CONFIG_PROCESS_ID
FROM EVA_PROCESS_DESCRIPTOR epd
INNER JOIN CCADMIN_IDMAP pdId ON epd.ID = pdid.id AND pdid.keyset='PD'
INNER JOIN EVA_PROCESS_DESC_REFERENCE epdr ON epd.ID  = epdr.PROCESS_DESCRIPTOR_ID
INNER JOIN CCADMIN_IDMAP pdrId ON epdr.ID = pdrid.id AND pdrid.keyset='PDR'
WHERE epd.REPOSITORY_PATH  ='{{repository_path | codepath()}}'
