---
id: gs1
title: Overview
sidebar_label: Introduction
---

MayaOnline.io is a first solution of its type  and is free for basic usage. It leverages the cross-cloud capabilities of Kubernetes and containers themselves and extends them to the data-plane with the help of the fully containerized OpenEBS. This solution is called a “Cross-cloud data-plane”. DevOps can self manage the storage with the help of MayaOnline and also get visibility into Kubernetes with ChatOps and cross-cloud control.

# MayaOnline Workflow

The following workflow explains the flow from the time you subscribe to MayaOnline, importing clusters,  to integrating it with Slack and other applications.

![MayaOnline Workflow Image](/docs/assets/MayaOnline.png)

# Why MayaOnline

MayaOnline.io is a first solution of its type and is free for basic usage. It leverages the cross-cloud capabilities of Kubernetes and containers themselves and extends them to the data-plane with the help of the fully containerized OpenEBS called as a “Cross-cloud data-plane” solution.

## **Analytics**

MayaOnline shows how workloads are performing and consuming data across clouds; for example, which storage policies result in higher performance for your workloads, irrespective of the underlying cloud vendor or data center.

MayaOnline analytics are based on the CNCF project Prometheus. Prometheus is noted for its scalability and usefulness in distributed environments. For more information about Prometheus, see [https://prometheus.io](https://prometheus.io). MayaOnline runs a Prometheus system for each user and interacts with the Prometheus node exporters of each cluster in your cloud deployments or in your on-premise instances. These time-series data entries are centrally stored and curated on your Prometheus instance on MayaOnline.

The data is monitored and intuitive graphs are delivered using Grafana. For more information, see [Monitoring for OpenEBS Volumes.](/monitoring-for-openebs-volumes.md)

## **Mulebot and other controls**

In addition to the graphical interface enabling analytics and the creation and management of automations, Mulebot is used to communicate with users. MayaOnline can post status to Slack channels and you can initiate actions from these channels that MayaOnline executes. Mulebot also enables developers and administrators to respond to data related alerts and also query the data plane from Slack itself.

## **API driven**

While Mulebot is useful to keep users in the loop, many decisions in large environments are made as part of a pipeline or other automation. You can query MayaOnline for relevant information or can proactively post information using its REST APIs.

## **cMotion**

MayaOnline will be able to balance workloads across clouds proactively. This balancing is implemented in a Kubernetes friendly way - where OpenEBS instances are reconfigured along with the storage policies that are used by Kubernetes to control them. MayaOnline is capable of cross-cloud balancing both stateless and stateful workloads. Workloads from one cloud are automatically replicated to another cloud vendor and made available in that cloud. Enhancement of this feature is planned in future releases.

MayaOnline includes initial cMotion capabilities. These rely upon the power of individual OpenEBS containers which if using the new cStore storage engine has the ability to deliver and copy on write based snapshots. These snapshots and the approach to writing data to the disk itself are inherently safer and more efficient than many other approaches to replication. When used for replication, this approach means that only changes to the underlying data are sent across the network to the far end. The entire experience of moving the OpenEBS data containers across user’s Kubernetes clusters is seamlessly handled by MayaOnline.

