{% set usernames = _db.fetch.all_users().column('username') %}
SELECT fu.USERNAME, IDS.ID, IDS.KEYNAME AS profile_keyname, fptp.PERSPECTIVE_ID, fp.NAME,pptids.KEYNAME AS pptive_keyname, ccids.KEYNAME AS context_config_keyname
FROM FU_USER fu 
INNER join FD_USER_PROFILE_TYPE fupt ON fu.id = fupt.USER_ID 
INNER JOIN CCADMIN_IDMAP IDS ON fupt.PROFILE_TYPE_ID = IDS.ID AND IDS.KEYSET ='PROFILE'
LEFT JOIN FD_PROFILE_TYPE_PERSPECTIVE fptp ON fupt.PROFILE_TYPE_ID = fptp.PROFILE_ID 
LEFT JOIN FD_PERSPECTIVE fp ON fp.ID = fptp.PERSPECTIVE_ID 
LEFT JOIN CCADMIN_IDMAP pptids ON fp.ID = pptids.ID AND pptids.KEYSET = 'PPTIVE'
LEFT JOIN EVA_CONTEXT_CONFIG ecc ON ecc.ID = fp.CONTEXT_CONFIG_ID 
LEFT JOIN CCADMIN_IDMAP ccids ON ccids.ID  = ecc.ID  AND ccids.KEYSET ='CC'
WHERE fu.USERNAME ='{{username | suggest(usernames)}}'
