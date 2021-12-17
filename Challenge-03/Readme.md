# Challenge 3 - Ingest to FHIR

## Introduction

Welcome to Challenge 3!

In this challenge you will learn how to use the [FHIR Bulk Loader & Export](https://github.com/microsoft/fhir-loader) tool to bulk-ingest data into Azure API for FHIR.

## Background

FHIR is an evolving standard, and one area where the FHIR specification is still in its early stages of development is its coverage of bulk data ingestion. Until HL7 publishes specifications for a FHIR $import operator, implementors will have to rely on alternative methods for getting bulk FHIR data into a FHIR server. In this challenge, we will be using the current best-practice solution for bulk FHIR import into Azure API for FHIR: the FHIR Bulk Loader & Export utility (OSS).

## Learning Objectives

+ Understand data constraints with FHIR bulk data loading
+ Understand how to track and compare bulk FHIR imports

### Azure API for FHIR, FHIR-Proxy and FHIR-Bulk Loader & Export Relationship 
The FHIR-Bulk Loader & Export tool is designed to work directly with Azure API for FHIR and through FHIR-Proxy. Advantages of using FHIR-Proxy include additional scalability, monitoring, and security. __Note:  If you are connecting to MC4H solutions in Dynamics/Dataverse, you must use FHIR-Proxy__. For the remainder of the Challenges, we assume you are using FHIR-Bulk Loader & Export with FHIR-Proxy.

Component view of Azure API for FHIR with FHIR Bulk Loader & Export and FHIR-Proxy.  

![components](./media/components.png)


## Prerequisites
+ Successful completion of Challenge 1
+ Postman
+ Text Editor

## Getting Started
Deploying FHIR-Bulk Loader & Export 
For this challenge, we will walk through these steps: 
- Login to Azure CLI (via the Portal or directly at shell.azure.com)
- Clone the FHIR-Loader repo 
- Execute the deployment scripts 
- Test Data Loading 

To begin the deployment process, CTRL+click (Windows or Linux) or CMD+click (Mac) on the "Launch Azure Shell" button below.  
The Azure Cloud Shell CLI will open in a new tab.

[![Launch Azure Shell](./media/launchcloudshell.png "Launch Cloud Shell")](https://shell.azure.com/bash?target="_blank")

Select Bash as the operating environment.

## Step 1 - FHIR Bulk Loader Installation

- Navigate to the FHIR-Loader repo (CTRL+click or CMD+click for new tab) https://github.com/microsoft/fhir-loader in your browser, review the main [Readme.md](https://github.com/microsoft/fhir-loader#fhir-loader), and the [Readme.md](https://github.com/microsoft/fhir-loader/blob/main/scripts/Readme.md) in the ./scripts folder.  

- Clone the FHIR-Loader repo in your Azure Cloudshell environment.  
    ```azurecli-interactive
    git clone https://github.com/microsoft/fhir-loader.git
    ```

- Change the working directory to the ```./fhir-loader/scripts``` directory in the repo.  
    ```azurecli-interactive
    cd $HOME/fhir-loader/scripts
    ```

- Make the Bash scripts for deployment and setup executable.  
    ```azurecli-interactive
    chmod +x *.bash
    ```

- Execute the ```deployFhirBulk.bash``` script.  
    ```azurecli-interactive
    ./deployFhirBulk.bash
    ```

Deployed Components.  _Larger image [here](./media/install-components.png)_ 

![fhir-bulk](./media/install-components-small.png)



## Step 2 - Download Sample Data

1. Download the following files to your desktop
    + [good_bundles.zip](/docs/assets/zip/good_bundles.zip)
    + [bad_bundles.zip](/docs/assets/zip/bad_bundles.zip)

## Step 3 - Upload Sample Data

1. In the Azure Portal, navigate to the FHIR Bulk Loader Blob Storage resource that was created in `Step 1`

2. Click on `Storage browser (preview)` and then click on `Blob container`
![Blob Containers](./media/portal-browser-container.png)  

3. Using the `good_bundles.zip` file downloaded in Step 1:
    + Determine which container this file should be uploaded to.

4. Using  the `bad_bundles.zip` file downloaded in Step 1:
    + Determine which container this file should be uploaded to.

> Refer to the Troubleshooting section below or FHIR Bulk Loader [testing](https://github.com/microsoft/fhir-loader/blob/main/docs/testing.md) documentation for more information


## Challenge Success

+ Successfully upload and import data from the file `good_bundles.zip`
+ Successfully identify the problem in the `bad_bundles.zip` file.  Use the Troubleshooting tips below to help. 
+ Identify the **most important issue to address in production**

## Troubleshooting 
The most common issue is that files are not loaded.  Use these points to understand where something happened. 

Check Container bundlesprocessed and / or bundleserr for your file name.  

_Note: if you used a zip file the names of the bundles within the zip file are exposed, not the zip file itself_

![bundlesprocessed](./media/bundlesprocessed.png)

Click on a **.result** file, then click on Edit

![bundle-edit](./media/bundle-edit.png)

In the Editor view, look for status codes, here a 201 is successful, and the logs show the FHIR Resource now containing the informatio. 

![bundle-edit-status](./media/bundle-edit-status.png)
