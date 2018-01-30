---
id: api9
title: Clusters
sidebar_label: Clusters
---

The examples in this category consist of various cluster tasks that you can perform in MayaOnline such as Creating, Modifying, and Deleting clusters.

## Resource Fields

### Writeable Fields

| Field                  | Type                                     | Create    | Update | Default | Notes |
| :--------------------- | :--------------------------------------- | :-------- | :----- | :------ | :---- |
| description            | string                                   | optional  | Yes    |         |       |
| name                   | string                                   | mandatory | Yes    |         |       |
| hostRemoveDelaySeconds | integer                                  | optional  | Yes    |         |       |
| k8sServerConfig        | [k8sServerConfig](https://dev.mayacloud.io/v3/schemas/k8sserverconfig) | optional  |        |         |       |
| provider               | string                                   | optional  | Yes    |         |       |

### Read only Fields

| Field                | Type                                     | Notes |
| :------------------- | :--------------------------------------- | :---- |
| created              | date                                     |       |
| embedded             | boolean                                  |       |
| id                   | integer                                  |       |
| kind                 | string                                   |       |
| organizationid       | reference[[organization](https://dev.mayacloud.io/v3/organizations)] |       |
| removed              | date                                     |       |
| state                | enum                                     |       |
| uuid                 | string                                   |       |
| transitioning        | enum                                     |       |
| transitioningMessage | string                                   |       |
| orchestration        | enum                                     |       |
| k8sClientConfig      | [k8sClientConfig](https://dev.mayacloud.io/v3/schemas/k8sclientconfig) |       |
| registrationToken    | [registrationToken](https://dev.mayacloud.io/v3/schemas/registrationtoken) |       |
| systemStacks         | array[[stackConfiguration](https://dev.mayacloud.io/v3/schemas/stackconfiguration)] |       |

## Operations

#### CREATE &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; POST: /v3/clusters

```
curl -u "${CATTLE_ACCESS_KEY}:${CATTLE_SECRET_KEY}" \
-X POST \
-H 'Accept: application/json' \
-H 'Content-Type: application/json' \
-d '{"name":"test", "organizationId":"1o11", "k8sServerConfig":null, "provider":"default", "systemStacks":[]}' \
'https://dev.mayacloud.io/v3/clusters'
```



#### UPDATE &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; PUT: /v3/clusters/1c36

```
curl -u "${CATTLE_ACCESS_KEY}:${CATTLE_SECRET_KEY}" \
-X PUT \
-H 'Accept: application/json' \
-H 'Content-Type: application/json' \
-d '{"created":"2018-01-29T08:14:57Z", "id":0, "kind":"cluster", "name":"test", "organizationId":"1o11", "removed":null, "state":"inactive", "uuid":"fa470dad-b62b-4257-a915-be8e75c2dd1a", "transitioning":"no", "transitioningMessage":null, "orchestration":null, "k8sServerConfig":null, "k8sClientConfig":null, "provider":"default", "registrationToken":{"hostCommand":"sudo docker run --rm --privileged -v /var/run/docker.sock:/var/run/docker.sock -v /var/lib/rancher:/var/lib/rancher mayadata/maya-io-agent:latest https://dev.mayacloud.io/v3/scripts/614E79EE98C8C09F02C3:1514678400000:ktgbQNuCtYxAsY4uadOWLSOcI", "clusterCommand":"kubectl apply -f https://dev.mayacloud.io/v3/scripts/614E79EE98C8C09F02C3:1514678400000:ktgbQNuCtYxAsY4uadOWLSOcI.yaml", "clusterOpenebsCommand":"kubectl apply -f https://dev.mayacloud.io/v3/scripts/614E79EE98C8C09F02C3:1514678400000:ktgbQNuCtYxAsY4uadOWLSOcI.maya.yaml", "windowsCommand":"New-Item -Path 'C:\\Program Files\\Rancher' -Type Directory\nInvoke-WebRequest -UseBasicParsing 'https://github.com/rancher/agent/releases/download/v0.6.0/agent.exe' -OutFile 'C:\\Program Files\\Rancher\\agent.exe'\n& 'C:\\Program Files\\Rancher\\agent.exe' -register-service https://dev.mayacloud.io/v3/scripts/614E79EE98C8C09F02C3:1514678400000:ktgbQNuCtYxAsY4uadOWLSOcI", "image":"mayadata/maya-io-agent:latest", "token":"614E79EE98C8C09F02C3:1514678400000:ktgbQNuCtYxAsY4uadOWLSOcI", "registrationUrl":"https://dev.mayacloud.io/v3/scripts/614E79EE98C8C09F02C3:1514678400000:ktgbQNuCtYxAsY4uadOWLSOcI"}, "systemStacks":[]}' \
'https://dev.mayacloud.io/v3/clusters/1c36'
```



#### DELETE &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; DELETE: /v3/clusters/1c36

```
curl -u "${CATTLE_ACCESS_KEY}:${CATTLE_SECRET_KEY}" \
-X DELETE \
-H 'Accept: application/json' \
'https://dev.mayacloud.io/v3/clusters/1c36'
```


