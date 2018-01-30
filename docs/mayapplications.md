---
id: apimayaproj
title: Maya Projects
sidebar_label: Maya Projects
---

You can go to https://dev.mayacloud.io/v3/project for viewing projects. The following are the namespace types. When a cluster is inactive only two i.e. system and default namespaces are available. When active, you will see the kubesystem namespace added.

- system name
- default - applications, volumes, and hosts (mayaapplications and hosts)
- kubesystem

## Maya Applications

You can use the following API to view the applications.

https://dev.mayacloud.io/v3/projects/1a88/mayaapplications

```
{
	"type": "collection",
	"resourceType": "mayaApplication",
	"links": {
		"self": "…/v3/projects/1a15/mayaapplications"
	},
	"createTypes": { },
	"actions": { },
	"data": [
	{
		"id": "1ma1",
		"type": "mayaApplication",
		"links": {
			"self": "…/v3/projects/1a15/mayaapplications/1ma1",
			"account": "…/v3/projects/1a15/mayaapplications/1ma1/account",
			"cluster": "…/v3/projects/1a15/mayaapplications/1ma1/cluster",
			"remove": "…/v3/projects/1a15/mayaapplications/1ma1",
			"update": "…/v3/projects/1a15/mayaapplications/1ma1"
		},
		"actions": { },
		"baseType": "mayaApplication",
		"name": "jenkins",
		"state": "active",
		"accountId": "1a15",
		"clusterId": "1c3",
		"created": "2018-01-20T08:46:17Z",
		"createdTS": 1516437977000,
		"data": {
			"kind": "Deployment",
			"name": "jenkins",
			"uid": "66c6a23c-fdba-11e7-8f9d-08002728f873",
			"pods": [
			{
				"name": "jenkins-584f44f786-nvhxq",
				"state": "Pending",
				"volumes": [ 2 items
				{
					"name": "pvc-66bf07fa-fdba-11e7-8f9d-08002728f873",
					"capacity": "5G",
					"replicaCount": 1,
					"uid": "979505b6-fdba-11e7-8f9d-08002728f873",
					"state": "Active",
					"controller": {
						"name": "pvc-66bf07fa-fdba-11e7-8f9d-08002728f873-ctrl-7d8448d94d-d8mrj",
						"state": "Running",
						"uid": "9735e49c-fdba-11e7-8f9d-08002728f873"
					},
					"replica": [
					{
						"name": "pvc-66bf07fa-fdba-11e7-8f9d-08002728f873-rep-95468d46c-ctr8n",
						"state": "Running",
						"uid": "974a1665-fdba-11e7-8f9d-08002728f873"
					}
					]
				},
				{
					"name": "pvc-66c2b24d-fdba-11e7-8f9d-08002728f873",
					"capacity": "5G",
					"replicaCount": 1,
					"uid": "979ee439-fdba-11e7-8f9d-08002728f873",
					"state": "Active",
					"controller": {
						"name": "pvc-66c2b24d-fdba-11e7-8f9d-08002728f873-ctrl-76586f46b6-qfhwg",
						"state": "Running",
						"uid": "97114df7-fdba-11e7-8f9d-08002728f873"
					},
					"replica": [
					{
						"name": "pvc-66c2b24d-fdba-11e7-8f9d-08002728f873-rep-7876686d4b-xnx24",
						"state": "Running",
						"uid": "97464476-fdba-11e7-8f9d-08002728f873"
					}
					]
				}
				],
				"uid": "66ccd3aa-fdba-11e7-8f9d-08002728f873"
			}
			]
		},	
		"kind": "Deployment",
		"removed": null,
		"transitioning": "no",
		"transitioningMessage": null,
		"uuid": "a56f25aa-1e1e-4bde-bf7c-67363bdcc0c6"
	}
	],
	"sortLinks": {
		"accountId": "…/v3/projects/1a15/mayaapplications?sort=accountId",
		"clusterId": "…/v3/projects/1a15/mayaapplications?sort=clusterId",
		"created": "…/v3/projects/1a15/mayaapplications?sort=created",
		"creatorId": "…/v3/projects/1a15/mayaapplications?sort=creatorId",
		"externalId": "…/v3/projects/1a15/mayaapplications?sort=externalId",
		"id": "…/v3/projects/1a15/mayaapplications?sort=id",
		"kind": "…/v3/projects/1a15/mayaapplications?sort=kind",
		"name": "…/v3/projects/1a15/mayaapplications?sort=name",
		"removeTime": "…/v3/projects/1a15/mayaapplications?sort=removeTime",
		"removed": "…/v3/projects/1a15/mayaapplications?sort=removed",
		"state": "…/v3/projects/1a15/mayaapplications?sort=state",
		"uuid": "…/v3/projects/1a15/mayaapplications?sort=uuid"
	},
	"pagination": {
		"first": null,
		"previous": null,
		"next": null,
		"limit": 100,
		"total": null,
		"partial": false
	},
	"sort": null,
	"filters": {
		"accountId": null,
		"clusterId": null,
		"created": null,
		"creatorId": null,
		"externalId": null,
		"id": null,
		"kind": null,
		"name": null,
		"removeTime": null,
		"removed": null,
		"state": null,
		"uuid": null
	},
	"createDefaults": { }
}
```

### Applications which are using OpenEBS Volumes

```
{
	"type": "collection",
	"resourceType": "mayaApplication",
	"links": {
		"self": "…/v3/projects/1a79/mayaapplications"
	},
	"createTypes": { },
	"actions": { },
	"data": [
	{
		"id": "1ma4",
		"type": "mayaApplication",
		"links": {
			"self": "…/v3/projects/1a79/mayaapplications/1ma4",
			"account": "…/v3/projects/1a79/mayaapplications/1ma4/account",
			"cluster": "…/v3/projects/1a79/mayaapplications/1ma4/cluster",
			"remove": "…/v3/projects/1a79/mayaapplications/1ma4",
			"update": "…/v3/projects/1a79/mayaapplications/1ma4"
		},
		"actions": { },
		"baseType": "mayaApplication",
		"name": "jenkins",
		"state": "active",
		"accountId": "1a79",
		"clusterId": "1c21",
		"created": "2018-01-23T06:09:05Z",
		"createdTS": 1516687745000,
		"data": {
			"kind": "Deployment",
			"name": "jenkins",
			"uid": "db6692ee-0003-11e8-8f5b-080027b5e23b",
			"pods": [
			{
				"name": "jenkins-584f44f786-wsr98",
				"state": "Pending",
				"volumes": [ 2 items
				{
					"name": "pvc-db2c4c89-0003-11e8-8f5b-080027b5e23b",
					"capacity": "5G",
					"replicaCount": 1,
					"uid": "4714b402-0004-11e8-8f5b-080027b5e23b",
					"state": "Active",
					"controller": {
						"name": "pvc-db2c4c89-0003-11e8-8f5b-080027b5e23b-ctrl-5d9bb58d79-vdzvn",
						"state": "Running",
						"uid": "45e29dcb-0004-11e8-8f5b-080027b5e23b"
					},
					"replica": [
					{
						"name": "pvc-db2c4c89-0003-11e8-8f5b-080027b5e23b-rep-69ddb9c697-skhrf",
						"state": "Running",
						"uid": "4612ee18-0004-11e8-8f5b-080027b5e23b"
					}
					]
				},
				{
					"name": "pvc-db2d9ff6-0003-11e8-8f5b-080027b5e23b",
					"capacity": "5G",
					"replicaCount": 1,
					"uid": "47e889f0-0004-11e8-8f5b-080027b5e23b",
					"state": "Active",
					"controller": {
						"name": "pvc-db2d9ff6-0003-11e8-8f5b-080027b5e23b-ctrl-6b68bd58cd-vtcjl",
						"state": "Running",
						"uid": "4648bf08-0004-11e8-8f5b-080027b5e23b"
					},
					"replica": [
					{
						"name": "pvc-db2d9ff6-0003-11e8-8f5b-080027b5e23b-rep-7c8f445644-5gwln",
						"state": "Running",
						"uid": "465a97be-0004-11e8-8f5b-080027b5e23b"
					}
					]
				},
				"uid": "dc0c1d4b-0003-11e8-8f5b-080027b5e23b"
			}
			]
		},
		"kind": "Deployment",
		"removed": null,
		"transitioning": "no",
		"transitioningMessage": null,
		"uuid": "7dfc14a4-a263-4b24-b90f-eb749ff414b6"
	}
	],
	"sortLinks": {
		"accountId": "…/v3/projects/1a79/mayaapplications?sort=accountId",
		"clusterId": "…/v3/projects/1a79/mayaapplications?sort=clusterId",
		"created": "…/v3/projects/1a79/mayaapplications?sort=created",
		"creatorId": "…/v3/projects/1a79/mayaapplications?sort=creatorId",
		"externalId": "…/v3/projects/1a79/mayaapplications?sort=externalId",
		"id": "…/v3/projects/1a79/mayaapplications?sort=id",
		"kind": "…/v3/projects/1a79/mayaapplications?sort=kind",
		"name": "…/v3/projects/1a79/mayaapplications?sort=name",
		"removeTime": "…/v3/projects/1a79/mayaapplications?sort=removeTime",
		"removed": "…/v3/projects/1a79/mayaapplications?sort=removed",
		"state": "…/v3/projects/1a79/mayaapplications?sort=state",
		"uuid": "…/v3/projects/1a79/mayaapplications?sort=uuid"
	},
	"pagination": {
		"first": null,
		"previous": null,
		"next": null,
		"limit": 100,
		"total": null,
		"partial": false
	},
	"sort": null,
	"filters": {
		"accountId": null,
		"clusterId": null,
		"created": null,
		"creatorId": null,
		"externalId": null,
		"id": null,
		"kind": null,
		"name": null,
		"removeTime": null,
		"removed": null,
		"state": null,
		"uuid": null
	},
	"createDefaults": { }
}
```



## Maya Volumes??

You can use the following API to view the volumes.



## Maya Hosts

You can use the following API to view the hosts.

```
{
	"type": "collection",
	"resourceType": "host",
	"links": {
		"self": "…/v3/projects/1a79/hosts"
	},
	"createTypes": { },
	"actions": { },
	"data": [
	{
		"id": "1h11",
		"type": "host",
		"links": {
			"self": "…/v3/projects/1a79/hosts/1h11",
			"cluster": 		"…/v3/projects/1a79/hosts/1h11/cluster",
			"deploymentUnits": "…/v3/projects/1a79/hosts/1h11/deploymentunits",
			"instances": "…/v3/projects/1a79/hosts/1h11/instances",
			"serviceEvents": "…/v3/projects/1a79/hosts/1h11/serviceevents",
			"volumes": "…/v3/projects/1a79/hosts/1h11/volumes",
			"update": "…/v3/projects/1a79/hosts/1h11",
			"storagePools": "…/v3/projects/1a79/hosts/1h11/storagepools",
			"hostStats": "…/v3/projects/1a79/hosts/1h11/hoststats",
			"containerStats": "…/v3/projects/1a79/hosts/1h11/containerstats"
		},
		"actions": {
			"evacuate": "…/v3/projects/1a79/hosts/1h11/?action=evacuate",
			"dockersocket": "…/v3/projects/1a79/hosts/1h11/?action=dockersocket",
			"deactivate": "…/v3/projects/1a79/hosts/1h11/?action=deactivate"
		},
		"baseType": "host",
		"name": null,
		"state": "active",
		"agentIpAddress": "106.51.73.198",
		"agentState": "active",
		"amazonec2Config": null,
		"authCertificateAuthority": null,
		"authKey": null,
		"azureConfig": null,
		"clusterId": "1c21",
		"created": "2018-01-23T06:08:50Z",
		"createdTS": 1516687730000,
		"description": null,
		"digitaloceanConfig": null,
		"dockerVersion": null,
		"driver": null,
		"engineEnv": null,
		"engineInsecureRegistry": null,
		"engineInstallUrl": null,
		"engineLabel": null,
		"engineOpt": null,
		"engineRegistryMirror": null,
		"engineStorageDriver": null,
		"externalId": "a02d9561-586f-49b6-b832-852af87e22ea-h",
		"hostTemplateId": null,
		"hostname": "minikube",
		"imported": true,
		"info": {
			"cloudProvider": null,
			"cpuInfo": {
				"count": 2,
				"cpuCoresPercentages": [ 2 items
					85.56701030927431,
					90.80459770113943
				],
				"loadAvg": [ 3 items
					"3.13",
					"1.35",
					"0.85"
				],
				"mhz": 1995.328,
				"modelName": "Intel(R) Core(TM) i3-5005U CPU @ 2.00GHz"
			},
			"diskInfo": {
				"dockerStorageDriver": "overlay2",
				"dockerStorageDriverStatus": { },
				"fileSystems": { },
				"mountPoints": { }
			},
			"hostKey": {
				"data": "-----BEGIN RSA PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAsIRdnl5zloIbM7b18s0O\nos/z7Lg3MJ+gNZrtR6CjQ4RMWi3bSgF3/436NCe10CtWx+7Pw/X/3VRbPeQMFb87\nNvPulPDnnzq0zgbLUq4FhzMZdqE8tYHnD8SvkJQyQjfWV4bfGItY8l76W5Ut8LjE\nDjHSzO3mWKIKdbj/2orbbTQBFNq2kchpW3SG+uL78ap6If6p5HTAVjJwZYK+zDsO\nXzyx30RQYWYoCeaROahVu/1cb47ZtZKcFCzDFtJKZG6LXLf6bjv2fsi8kM0SyDms\ni/bVH3wrGcWq0URae5kbEDDj8FexAHxwkATQ1xLQTqh+mnf6kL8GfboWfSN8URQh\nIwIDAQAB\n-----END RSA PUBLIC KEY-----\n"
			},
			"iopsInfo": { },
			"memoryInfo": {
				"active": 545,
				"buffers": 22,
				"cached": 1328,
				"inactive": 904,
				"memAvailable": 1092,
				"memFree": 37,
				"memTotal": 2000,
				"swapCached": 0,
				"swapfree": 999,
				"swaptotal": 999
			},
			"osInfo": {
				"dockerVersion": "Docker version 17.06.0-ce, build 02c1d87",
				"kernelVersion": "4.9.13",
				"operatingSystem": "Buildroot 2017.02"
			}
		},
		"instanceIds": [ 34 items
			"1i6221",
			"1i6222",
			"1i6223",
			"1i6224",
			"1i6225",
			"1i6226",
			"1i6227",
			"1i6228",
			"1i6229",
			"1i6230",
			"1i6231",
			"1i6232",
			"1i6233",
			"1i6234",
			"1i6235",
			"1i6236",
			"1i6237",
			"1i6238",
			"1i6239",
			"1i6240",
			"1i6253",
			"1i6261",
			"1i6266",
			"1i6274",
			"1i6275",
			"1i6276",
			"1i6277",
			"1i6283",
			"1i6290",
			"1i6293",
			"1i6297",
			"1i6312",
			"1i6313",
			"1i6314"
		],
		"kind": "docker",
		"labels": {
			"io.rancher.host.agent_image": "",
			"io.rancher.host.docker_version": "17.06",
			"io.rancher.host.linux_kernel_version": "4.9"
		},
		"localStorageMb": 15244414,
		"memory": 2097152000,
		"milliCpu": 2000,
		"packetConfig": null,
		"publicEndpoints": null,
		"removed": null,
		"stackId": null,
		"transitioning": "no",
		"transitioningMessage": null,
		"uuid": "6b2b7b28-d0d0-449d-90ea-b33b5b4e4914"
	}
	],
	"sortLinks": {
		"agentState": "…/v3/projects/1a79/hosts?sort=agentState",
		"clusterId": "…/v3/projects/1a79/hosts?sort=clusterId",
		"created": "…/v3/projects/1a79/hosts?sort=created",
		"creatorId": "…/v3/projects/1a79/hosts?sort=creatorId",
		"description": "…/v3/projects/1a79/hosts?sort=description",
		"externalId": "…/v3/projects/1a79/hosts?sort=externalId",
		"hostTemplateId": "…/v3/projects/1a79/hosts?sort=hostTemplateId",
		"id": "…/v3/projects/1a79/hosts?sort=id",
		"kind": "…/v3/projects/1a79/hosts?sort=kind",
		"localStorageMb": "…/v3/projects/1a79/hosts?sort=localStorageMb",
		"memory": "…/v3/projects/1a79/hosts?sort=memory",
		"milliCpu": "…/v3/projects/1a79/hosts?sort=milliCpu",
		"name": "…/v3/projects/1a79/hosts?sort=name",
		"removeAfter": "…/v3/projects/1a79/hosts?sort=removeAfter",
		"removeTime": "…/v3/projects/1a79/hosts?sort=removeTime",
		"removed": "…/v3/projects/1a79/hosts?sort=removed",
		"revision": "…/v3/projects/1a79/hosts?sort=revision",
		"stackId": "…/v3/projects/1a79/hosts?sort=stackId",
		"state": "…/v3/projects/1a79/hosts?sort=state",
		"uri": "…/v3/projects/1a79/hosts?sort=uri",
		"uuid": "…/v3/projects/1a79/hosts?sort=uuid"
	},
	"pagination": {
		"first": null,
		"previous": null,
		"next": null,
		"limit": 100,
		"total": null,
		"partial": false
	},
	"sort": null,
	"filters": {
		"agentState": null,
		"clusterId": null,
		"created": null,
		"creatorId": null,
		"description": null,
		"externalId": null,
		"hostTemplateId": null,
		"id": null,
		"kind": null,
		"localStorageMb": null,
		"memory": null,
		"milliCpu": null,
		"name": null,
		"removeAfter": null,
		"removeTime": null,
		"removed": null,
		"revision": null,
		"stackId": null,
		"state": null,
		"uri": null,
		"uuid": null
	},
	"createDefaults": { }
}
```







