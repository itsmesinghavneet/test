---
id: gs4
title: Integrations
sidebar_label: Integrations
---

From the MayaOnline main page, go to **Organizations** and select **Integrations** on the left pane. The screen displays a list of applications that you have integrated under _Monitoring Integrations_ and an option to add to slack under _ChatOps Integrations_.

## Monitoring Integration

**&lt;&lt;TBD&gt;&gt;**

## ChatOps \(Mulebot?\) Integration

Integrating ChatOps enables interaction between clusters present in the organization on [MayaOnline](https://mayaonline.io/) and you through Slack. You will be able to receive alerts and query applications present in MayaOnline.

### What is Mulebot?

Mulebot application covers the storage operational support of Kubernetes clusters. DevOps developers and administrators receive alerts, analytics of their OpenEBS volumes deployed across multi-cloud Kubernetes clusters into their [Slack](https://slack.com/) channels, and also provides a way to query any configuration and status from Slack. The Muletbot functionality also includes interacting with DevOps developers and administrators to manage the yaml configurations files in their CI/CD system. The Mulebot enhances your experience with MayaOnline by allowing you to query the MayaOnline clusters' configuration and MayaOnline applications using the following slash commands.

**&lt;&lt;to add all commands or only maya help??&gt;&gt;**

* **/maya get clusters**
  * Lists all the clusters imported in MayaOnline whether active or inactive.
* **/maya get cluster cluster-name/cluster-Id**
  * Fetches all details of that particular cluster whose cluster-name or cluster-Id is provided.
* **/maya help**
  * Displays a list of all the available slash commands and their functionality that can be used to query the Mulebot..

Mulebot also keeps you informed about the current status of clusters that you have imported in MayaOnline by sending alerts as required. Once you integrate Slack, you will receive alerts related to the clusters imported in MayaOnline to the specified Slack channel. Following are the various types of alerts that you will receive.

* Cluster Up 
* Cluster Down
* Volume Up
* Volume Down
* Volume Write Latency  ??
* Volume Read Latency  ??
* High CPU Usage
* High Disk Usage and so on.

### Adding Slack Configuration

**Prerequisite:**

You must have a Slack workspace.

**To add to Slack, use the following procedure.**

1. Go to **Organizations** &gt; **Integrations** from the MayaOnline page.
2. Click **Add to Slack**.
3. Select the workspace from the drop-down list.
4. Select a channel from the **Post to** drop-down list.
5. Click **Authorize**.
6. Select a cluster you have imported from the **Select cluster** drop-down list.
   **Note:** You can also select multiple clusters.
   You will see the clusters you have added in the **Active connections** box.

**Note:** Repeat the above procedure to add multiple slack channels.

**To edit a cluster, use the following procedure.**

1. Click **Edit **in the **Active connections** box.
2. Click the **Select cluster** drop-down list.
3. Select or deselect the clusters.
4. Click **Done**.
   You will see the changes you have made in the **Active connections** box.

**To delete a cluster, use the following procedure.**

1. Click **Delete **in the **Active connections** box.
   You will see that the clusters are now not visible in the **Active connections** box.

## Integrating with Grafana

details by moteesh

Integrating with Weave Cortex??





