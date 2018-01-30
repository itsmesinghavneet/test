---
id: gs5
title: Managing Clusters
sidebar_label: Managing Clusters
---

Managing clusters in MayaOnline is simple and easy to use. By default, when you login, the **Clusters** page is displayed. You can add a cluster to import, edit a cluster, and delete a cluster using the following procedures.

When you have not imported any clusters, you will have an option to import your very first cluster.

Click **Import a cluster now** or view a demo by clicking on the **Watch how to import your first cluster** on the right pane.

## Adding and Importing Clusters

You must add a cluster and import them to so that you can monitor

1. Click on the **+** sign to add a cluster.
2. You can either **Import an existing OpenEBS cluster** or **Install OpenEBS on your K8s cluster and import.** Click on either of these options.
3. A kubectl command is displayed. Click **Copy** to copy the command and run it at your command prompt.
4. Close the window.
5. Paste the command at the Terminal \(which has access to the cluster\) and press **Enter** to run the command.
6. You will be automatically be redirected to the **Clusters** page where you can see the cluster details such as the OpenEBS applications, host details, and clicking **Kubernetes Dashboard** displays the Kubernetes dashboard associated with that cluster. 

**&lt;&lt;screenshot required??&gt;&gt;**

**Note:** You can also click on the ![](/assets/dotmenu.png)  icon, and select **Import** on an Inactive cluster and follow the procedure above from step 2.

## Editing a Cluster

1. Click on the ![](/assets/dotmenu.png)  icon and select **Edit**.

2. Edit the **Name** and **Description** of the cluster if required.

3. Select the provider image from the drop-down list on the right.

4. Click **Save**.

## Deleting a Cluster

1. Click on the ![](/assets/dotmenu.png)  icon and select **Delete**.
2. Click **Continue** if you are sure you want to delete.
   The status says **Deleting** and the the cluster is now deleted. 



