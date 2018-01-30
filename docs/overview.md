---
id: overview
title: MayaOnline Overview
sidebar_label: MayaOnline Introduction
---



MayaOnline is the SaaS platform that enables the DevOps developers and admins to connect their OpenEBS enabled Kubernetes clusters for centralized monitoring, ChatOps and obtaining support from MayaData.  Users can signup to MayaOnline using their GitHub credentials  and it is free for basic usage.



![MayaOnline Overview Image](/docs/assets/mo-overview.jpg)






## Why MayaOnline?
Kubernetes has enabled enterprises to consider true multi-cloud solutions. Users end up having multiple stateful workloads across various Kubernetes clusters deployed sometimes across different cloud providers.  A cross cloud management platform for these Kubernetes clusters will help application developers gain visibility their application data access patterns, performance patterns, correlate such patterns across various applications etc. Managing the operations of the applications need the latest information to be instantly provided to the DevOps using the modern tools such as slack so that the CI/CD system stays efficient.



MayaOnline is designed as a SaaS platform to provide the above capabilities to DevOps. Developers can use MayaOnline as an extension to their CI/CD system. MayaOnline provides detailed API to turn itself as a white box to the DevOps. MayaOnline helps DevOps and developers to manage the data life cycle of the stateful workloads seamlessly and efficiently. 



## Features

### Visibility

MayaOnline combines user's Kubernetes clusters across the multiple cloud providers and on-premise datacenters into one single control plane and displays the applications that uses OpenEBS for easy viewing and management.  Users also get visibility into applications and application data patterns. They can gain access to detailed OpenEBS volume dashboards with granularity that goes all the way to volume read/write latencies.  

### Slack Application

For providing efficient ChatOps support to the end users, MayaOnline has developed a Slack Application called "**MuleBot**". MuleBot is a distributed Slack Application that can be found in the public applications directory of Slack. MayaOnline has made the integration of MuleBot into MayaOnline amazingly simple. After choosing the target Slack workspace and authenticating against slack, users can map the MayaOnline clusters to Slack channels. From a given channel users can query almost everything about their MayaOnline infrastructure. 

### Smart Alerts

Smart Alerts are delivered right into configured Slack channels.Smart alerts help the users to act on the status changes of the stateful workloads. These alerts typically come with a suggestive action to resolve the alert so that the action can be taken by the end user from the slack itself. 



### Cross Cloud workload movement / cMotion

Using cMotion feature, users can move the workloads across Kubernetes clusters. This feature helps the users from being locked into a particular cloud provider environment. The workload movement workflow is nicely integrated into MayaOnline, and can be achieved using MayaOnline APIs. This enables the end users to integrate cMotion capability into their CI/CD environement. 

`This is a tech preview feature and may be enabled to user's on request.` 



### MayaOnline API

MayaOnline exposes a powerful set of REST APIs for the developers to integrate MayaOnline's capabilities into their external applications, typically their CI/CD systems. The API set can be used for easy access of various MayaOnline resources such as cluster configuration, curated monitoring data, meaningful reports etc. 

### Enterprise support for OpenEBS clusters

Connecting your OpenEBS clusters to MayaOnline is the easiest way to get Enterprise support from MayaData Inc. MayaOnline offers various support subscription packages to select from. See <pricing>
Connecting your OpenEBS clusters to MayaOnline is the easiest way to get Enterprise support from MayaData Inc. MayaOnline offers various support subscription packages to select from. See Pricing

