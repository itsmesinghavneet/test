---
id: api5
title: Authorization Endpoint
sidebar_label: Authorization Endpoint
---


Go to the following URL to find the authorization endpoint.

[https://dev.mayacloud.io/v3/token](https://dev.mayacloud.io/v3/token)

### Example

You can use the following example to view redirect URL for authorization without logging in.

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
			"redirectUrl": "`[`https://github.com/login/oauth/authorize?client_id=841b168f866f1f7127e4`](https://github.com/login/oauth/authorize?client_id=841b168f866f1f7127e4)`",
			"security": true,
			"slackOauthUrl": "`[`https://slack.com/oauth/authorize?client_id=259700574529.277662436016&scope=channels:history,im:history,bot,commands,incoming-webhook,chat:write:user,channels:read,channels:write,chat:write:bot,groups:read,groups:history,groups:write,im:read,mpim:history,usergroups:read`](https://slack.com/oauth/authorize?client_id=259700574529.277662436016&scope=channels:history,im:history,bot,commands,incoming-webhook,chat:write:user,channels:read,channels:write,chat:write:bot,groups:read,groups:history,groups:write,im:read,mpim:history,usergroups:read)`",
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
