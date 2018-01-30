---
id: api7
title: Organizations
sidebar_label: Organizations
---

MayaOnline Administrator creates an organization while creating a user. As a user, you can only edit the organization fields.

# Resource Fields

## Writeable Fields

| FIELD       | TYPE              | UPDATE |
| ----------- | ----------------- | ------ |
| description | string (optional) | Yes    |
| name        | string (optional) | Yes    |

## Read only Fields

| FIELD                | TYPE    |
| -------------------- | ------- |
| created              | date    |
| id                   | integer |
| kind                 | string  |
| removed              | date    |
| state                | enum    |
| uuid                 | string  |
| transitioning        | enum    |
| transitioningMessage | string  |
| mayaUrl              | string  |
| prometheusUrl        | string  |
| grafanaUrl           | string  |
| alertManagerUrl      | string  |
| apiKey               | string  |
| userCredential       | string  |

# Operations

##### UPDATE&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;PUT: /v3/organizations/1o11

```
curl -u "${API_ACCESS_KEY}:${API_SECRET_KEY}" \
-X PUT \
-H 'Accept: application/json' \
-H 'Content-Type: application/json' \
-d '{"created":"2018-01-29T06:21:27Z", "id":0, "kind":"organization", "name":"Whimsical-Candytuft", "removed":null, "state":"active", "uuid":"79a61a5e-17e6-4137-a98c-02bf9060ac93", "transitioning":"no", "transitioningMessage":null, "mayaUrl":"https://dev.mayacloud.io", "prometheusUrl":"https://dev.mayacloud.io/pr-79a61a5e17e64137a98c02bf9060ac93/", "grafanaUrl":"https://312BD6C58B6773DFE108:fTzva6kajYcrhpArh4nbXje3YG5qd91nnDWudVfZ@dev.mayacloud.io/maya-grafana/dashboard/db/openebs-volume-stats?orgId=312BD6C58B6773DFE108", "alertManagerUrl":"https://dev.mayacloud.io/am-79a61a5e17e64137a98c02bf9060ac93/", "apiKey":"MzEyQkQ2QzU4QjY3NzNERkUxMDg6ZlR6dmE2a2FqWWNyaHBBcmg0bmJYamUzWUc1cWQ5MW5uRFd1ZFZmWg==", "userCredential":"MzEyQkQ2QzU4QjY3NzNERkUxMDg6ZlR6dmE2a2FqWWNyaHBBcmg0bmJYamUzWUc1cWQ5MW5uRFd1ZFZmWg=="}' \
'https://dev.mayacloud.io/v3/organizations/1o11'
```