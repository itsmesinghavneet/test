---
id: api8
title: API Keys
sidebar_label: API Keys
---

An API Key provides access to the MayaOnline API if access control has been turned on. The access key and secret key pair are created per environment and can be used to directly call the API.

## Resource Fields

### Writeable Fields

| FIELD       | TYPE   | UPDATE |
| ----------- | ------ | ------ |
| description | string | Yes    |
| name        | string | Yes    |

### Read only Fields

| FIELD                | TYPE                                     |
| -------------------- | ---------------------------------------- |
| accountId            | reference[[account](https://dev.mayacloud.io/v3/accounts)] |
| clusterId            | reference[[cluster](https://dev.mayacloud.io/v3/clusters)] |
| created              | date                                     |
| id                   | integer                                  |
| kind                 | string                                   |
| publicValue          | string                                   |
| removed              | date                                     |
| secretValue          | password                                 |
| state                | enum                                     |
| transitioning        | enum                                     |
| transitioningMessage | string                                   |
| uuid                 | string                                   |

## Operations

#### CREATE &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;POST: /v3/apikeys/1ak46

```
curl -u "${API_ACCESS_KEY}:${API_SECRET_KEY}" \
-X POST \
-H 'Accept: application/json' \
-H 'Content-Type: application/json' \
-d '{}' \
'https://dev.mayacloud.io/v3/apikey'
```

#### EDIT &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; PUT: /v3/apikeys/1ak46

```
curl -u "${API_ACCESS_KEY}:${API_SECRET_KEY}" \
-X PUT \
-H 'Accept: application/json' \
-H 'Content-Type: application/json' \
-d '{"accountId":"1a86", "clusterId":null, "created":"2018-01-29T06:21:27Z", "id":0, "kind":"apikey", "name":"slack_api_key", "publicValue":"312BD6C58B6773DFE108", "removed":null, "secretValue":null, "state":"active", "transitioning":"no", "transitioningMessage":null, "uuid":"28ac40f8-f59d-4c66-85c0-3971fef6a94c"}' \
'https://dev.mayacloud.io/v3/apikeys/1ak46'
```

#### DELETE &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; DELETE: /v3/apikeys/1ak46

```
curl -u "${API_ACCESS_KEY}:${API_SECRET_KEY}" \
-X DELETE \
-H 'Accept: application/json' \
'https://dev.mayacloud.io/v3/apikeys/1ak46'
```



## Actions

#### DEACTIVATE &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;POST: v3/apikeys/1ak46/?action=deactivate

```
curl -u "${API_ACCESS_KEY}:${API_SECRET_KEY}" \
-X POST \
-H 'Accept: application/json' \
-H 'Content-Type: application/json' \
-d '{}' \
'https://dev.mayacloud.io/v3/apikeys/1ak46/?action=deactivate'
```