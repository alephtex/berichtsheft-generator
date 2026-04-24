#!/bin/bash
set -euo pipefail

# Autoresearch: Test LDAP authentication with different filters

TARGET_USER="benedict.heldt"
BASE_DN="ou=users,dc=ldap,dc=goauthentik,dc=io"
BIND_DN="cn=opnsense-user,ou=users,dc=ldap,dc=goauthentik,dc=io"
LDAP_HOST="192.168.66.13"
LDAP_PORT="636"

echo "=== Testing LDAP filters for Authentik ==="
echo "Target: $TARGET_USER"
echo "BaseDN: $BASE_DN"

# Test different filters
FILTERS=(
    "(&(cn=$TARGET_USER)(objectClass=user))"
    "(cn=$TARGET_USER)"
    "(uid=$TARGET_USER)"
    "(objectClass=*)"
    "(&(cn=$TARGET_USER)(objectClass=*))"
    "(displayName=$TARGET_USER)"
)

for filter in "${FILTERS[@]}"; do
    echo ""
    echo "=== Testing filter: $filter ==="
    result=$(ldapsearch -H "ldaps://$LDAP_HOST:$LDAP_PORT" \
        -D "$BIND_DN" \
        -w "$LDAP_PASSWORD" \
        -b "$BASE_DN" \
        -s sub \
        "$filter" \
        2>&1 | head -30 || true)
    echo "$result"
done
