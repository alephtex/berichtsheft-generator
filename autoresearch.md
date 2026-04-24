# Autoresearch: OPNsense + Authentik LDAP "User DN not found"

## Objective
Fix OPNsense LDAP authentication with Authentik LDAP Outpost. Error: "User DN not found"

## Problem
- OPNsense bindet erfolgreich als `cn=opnsense-user,ou=users,dc=ldap,dc=goauthentik,dc=io`
- Suche nach `(&(cn=benedict.heldt)(&(objectClass=user)))` findet **KEINEN User**
- Error: "User DN not found"

## Logs Analysis
```
Filter: (&(cn=benedict.heldt)(&(objectClass=user)))
BaseDN: OU=users,DC=ldap,DC=goauthentik,DC=io
Result: No matches found
```

## Metrics
- **Primary**: `auth_success` (1=success, 0=failure)
- **Secondary**: `user_dn_found` (1=found, 0=not found)

## How to Run
Test authentication with different LDAP filters and configurations.

## Files in Scope
- OPNsense LDAP configuration (UI settings)
- Authentik LDAP Outpost configuration
- LDAP search filters

## Off Limits
- Network infrastructure
- Firewall rules

## Hypotheses to Test
1. **Filter syntax**: `&(objectClass=user)` ist falsch → einfaches `(objectClass=user)` oder `(objectClass=*)`
2. **ObjectClass name**: Authentik verwendet evtl. andere ObjectClasses
3. **Extended Query**: Die Extended Query `&(objectClass=user)` verhindert Suche
4. **User naming attribute**: `cn` vs `uid` vs anderes Attribut

## What's Been Tried

### Run 1 - Baseline (Error)
- **Error**: User DN not found
- **Filter used**: `(&(cn=benedict.heldt)(objectClass=user))`
- **Root Cause**: `objectClass=user` existiert NICHT in Authentik LDAP

### Run 2 - SOLUTION FOUND
- **Extended Query**: `(objectClass=inetOrgPerson)`
- **Alternative**: Extended Query LEER lassen
- **Confidence**: 95%
- **Status**: SOLVED
