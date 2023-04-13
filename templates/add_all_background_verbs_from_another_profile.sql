{% set source_profile = __source_profile | description("source_profile (all the background verbs will be copied from this profile") | suggest(_keynames.PROFILE) %}
{% set bv_list =_db.fetch.bv_keynames_by_profile(source_profile) %}
{% set profile_keyname = target_profile | description("target_profile (is the profile where all verbs will be added to") | suggest(_keynames.PROFILE) %}

{% for bv in bv_list %}
{%set background_verb_keyname =bv['BV_KEYNAME']%}
{% include 'add_background_verb_to_profile.sql' %}
{% endfor %}
