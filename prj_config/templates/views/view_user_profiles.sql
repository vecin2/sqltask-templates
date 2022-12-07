{% set usernames = _db.fetch.all_users().column('username') %}
SELECT fu.USERNAME, IDS.ID, IDS.KEYNAME AS profile_keyname, fptp.PERSPECTIVE_ID, fp.NAME,pptids.KEYNAME AS pptive_keyname, ccids.KEYNAME AS context_config_keyname
FROM FU_USER fu 
INNER join FD_USER_PROFILE_TYPE fupt ON fu.id = fupt.USER_ID 
INNER JOIN CCADMIN_IDMAP IDS ON fupt.PROFILE_TYPE_ID = IDS.ID AND IDS.KEYSET ='PROFILE'
INNER JOIN FD_PROFILE_TYPE_PERSPECTIVE fptp ON fupt.PROFILE_TYPE_ID = fptp.PROFILE_ID 
INNER JOIN FD_PERSPECTIVE fp ON fp.ID = fptp.PERSPECTIVE_ID 
INNER JOIN CCADMIN_IDMAP pptids ON fp.ID = pptids.ID AND pptids.KEYSET = 'PPTIVE'
INNER JOIN EVA_CONTEXT_CONFIG ecc ON ecc.ID = fp.CONTEXT_CONFIG_ID 
INNER JOIN CCADMIN_IDMAP ccids ON ccids.ID  = ecc.ID  AND ccids.KEYSET ='CC'
AND fu.USERNAME ='{{username | suggest(usernames)}}'
