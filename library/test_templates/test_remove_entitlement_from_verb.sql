--{"verb":"IdentifyCustomer","entitlement":"TelephonyAutoAnswer"}
DELETE FROM EVA_VERB_ENTITLEMENT
WHERE VERB_ID = @V.IdentifyCustomer
and ENTITLEMENT_ID = @ENTLMNT.TelephonyAutoAnswer;
