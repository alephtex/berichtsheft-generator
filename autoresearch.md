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
- **Filter**: `(&(cn=benedict.heldt)(objectClass=user))`
- **Root Cause**: `objectClass=user` existiert NICHT in Authentik

### Run 2 - SOLUTION FOUND
- **Extended Query**: `(objectClass=inetOrgPerson)`
- **Confidence**: 95%

### Run 3 - Technical Optimization
- User naming: `cn` (NICHT `uid`)
- SSL: Port 636, SSL-encrypted
- Groups: Synchronize + Read properties
- Case insensitive: ENABLE
- Auto-create users: ENABLE

### Run 4 - SSL/TLS Setup
- Cert export: `openssl s_client -connect host:636 -showcerts`
- Import: System > Trust > Authorities > Import

### Run 5 - Group Authentication
- memberOf: Supported in Authentik LDAP
- Nested groups: Limitiert
- Group constraint via Extended Query: `memberOf=cn=group,ou=groups,...`

### Run 6 - Troubleshooting Guide
- ldapsearch commands ready
- Log locations documented
- Debug commands compiled

## FINAL SOLUTION CHECKLIST

1. **Extended Query**: LEER oder `(objectClass=inetOrgPerson)`
2. **User naming attribute**: `cn`
3. **SSL**: Port 636, import cert to Trust
4. **Groups**: Synchronize groups + Read properties
5. **Case insensitive**: Match case insensitive = YES
6. **Auto-create**: Automatic user creation = YES (optional)
7. **Search scope**: Entire Subtree
8. **Containers**: OU=users + OU=groups
