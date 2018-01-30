---
id: api3
title: Generating an API Access Key
sidebar_label: Generating an API Access Key
---


You can use the following example to access MayaOnline API in third party applications. The publicValue and secretValue must be added in a header in the following format where encdata contains base64 of public and private key.

```
headers:
{
	'Authorization' : 'Basic ' + encdata,
}
```

### Example

```
HTTP/1.1 201
date: Tue, 23 Jan 2018 06:19:28 GMT
x-api-user-id: 1a77
server: nginx/1.13.6
x-api-client-ip: 106.51.73.198
x-api-roles: user
strict-transport-security: max-age=15724800; includeSubDomains;
content-type: application/json; charset=utf-8
status: 201
x-api-account-id: 1a77
x-api-schemas: [https://dev.mayacloud.io/v3/schemas](https://dev.mayacloud.io/v3/schemas)
content-length: 841
expires: Thu, 01 Jan 1970 00:00:00 GMT

{
	"id": ["1ak52"](https://dev.mayacloud.io/v3/apikeys/1ak52),
	"type": ["apiKey"](https://dev.mayacloud.io/v3/schemas/apikey),
	"links": {
		"self": ["…/v3/apikeys/1ak52"](https://dev.mayacloud.io/v3/apikeys/1ak52),
		"account": ["…/v3/apikeys/1ak52/account"](https://dev.mayacloud.io/v3/apikeys/1ak52/account),
		"instances": ["…/v3/apikeys/1ak52/instances"](https://dev.mayacloud.io/v3/apikeys/1ak52/instances),
		"remove": ["…/v3/apikeys/1ak52"](https://dev.mayacloud.io/v3/apikeys/1ak52),
		"update": ["…/v3/apikeys/1ak52"](https://dev.mayacloud.io/v3/apikeys/1ak52),
		"certificate": ["…/v3/apikeys/1ak52/certificate"](https://dev.mayacloud.io/v3/apikeys/1ak52/certificate)
		},
	"actions": { },
	"baseType":
	"credential",
	"name":"test",
	"state":"creating",
	"accountId": ["1a77"](https://dev.mayacloud.io/v3/accounts/1a77),
	"clusterId": null,
	"created": "2018-01-23T06:19:29Z",
	"createdTS": 1516688369000,
	"description": "test",
	"kind": "apiKey",
	"publicValue": "B1EC74D92D93610A2F6F",
	"removed": null,
	"secretValue": "Gp355fxSDFNwZpUnq8UGxszBYydc4x5RrXKT1rLM",
	"transitioning": "yes",
	"transitioningMessage": "Creating",
	"uuid": "b41e3c75-188a-4cd5-86bd-d9c4809dfcd4"
}
```
