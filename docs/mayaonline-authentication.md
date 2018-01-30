---
id: api2
title: MayaOnline Authentication
sidebar_label: MayaOnline Authentication
---


You can access MayaOnline without logging in by going to [https://dev.mayacloud.io/v3/token](https://dev.mayacloud.io/v3/token) and using the following example.

```
{
	"type": "collection",
	"resourceType": "token",
	"links": {
		"self": "…/v3/token"
	},
	"createTypes": { },
	"actions": { },
	"data": [
	    {
			"id": null,
			"type": "token",
			"links": {
			"remove": null
		},
		"actions": { },
		"baseType": "token",
		"accountId": null,
		"authProvider": "githubconfig",
		"code": null,
		"enabled": true,
		"inviteCode": null,
		"jwt": "d1tRMgFzWffE9QsfA8neVr6iE7LE8QKEi2SkPJeo",
		"redirectUrl": "https://github.com/login/oauth/authorize?client_id=841b168f866f1f7127e4",
		"security": true,
		"slackOauthUrl": "https://slack.com/oauth/authorize?client_id=259700574529.277662436016&scope=channels:history,im:history,bot,commands,incoming-webhook,chat:write:user,channels:read,channels:write,chat:write:bot,groups:read,groups:history,groups:write,im:read,mpim:history,usergroups:read",`
		"user": null,
		"userType": "user"
		}
	],
	"sortLinks": { },
	"pagination": null,
	"sort": null,
	"filters": { },
	"createDefaults": { }
}
```


