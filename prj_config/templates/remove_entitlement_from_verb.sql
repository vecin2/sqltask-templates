{% set entitled_verbs= _db.fetch.v_with_entitlements().column('KEYNAME')%}
DELETE FROM EVA_VERB_ENTITLEMENT
WHERE VERB_ID = @V.{{verb | suggest(entitled_verbs)}}
{% set verb_entitlements= _db.fetch.verb_entitlements(verb).column('KEYNAME')%}
and ENTITLEMENT_ID = @ENTLMNT.{{entitlement |suggest(verb_entitlements)}};
