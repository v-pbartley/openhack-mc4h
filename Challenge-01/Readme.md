# Challenge-01 - Deploy Azure API for FHIR (PaaS), FHIR-Proxy (OSS), and FHIR-Bulk Loader (OSS)

## Introduction

Welcome to Challenge-01!

In this challenge, you will use an Azure Resource Manager (ARM) template to deploy **Azure API for FHIR** (PaaS), **FHIR-Proxy** (OSS), and **FHIR-Bulk Loader** (OSS). In addition, you will set up a **Postman** environment to make REST API calls to Azure API for FHIR.

## Background
FHIR (Fast Healthcare Interoperability Resources) is the industry standard format underlying Microsoft's cloud data platform for healthcare. Microsoft's support for FHIR rests on [Azure API for FHIR](https://docs.microsoft.com/en-us/azure/healthcare-apis/azure-api-for-fhir/overview) (PaaS) (soon to be succeeded by [Azure Healthcare APIs](https://azure.microsoft.com/en-us/services/healthcare-apis/) - currently in Public Preview).

In Azure FHIR data architectures, Azure API for FHIR receives REST API requests from client apps and manages all FHIR data persistance and retrieval tasks. Meanwhile, the open-source [FHIR-Proxy](https://github.com/microsoft/fhir-proxy) acts as a checkpoint surrounding Azure API for FHIR, filtering the incoming and outgoing FHIR data according to a set of admin-defined rules.

For bulk ingestion of FHIR data into Azure API for FHIR, Microsoft offers the open-source [FHIR-Bulk Loader](https://github.com/microsoft/fhir-loader) utility. With FHIR-Bulk loader, admins can import large amounts of FHIR data into Azure API for FHIR at one time. The FHIR Bulk-Loader can import data from FHIR Bundles (compressed and non-compressed) as well as FHIR NDJSON files. 

## Learning Objectives 
+ Use an ARM template to deploy Azure API for FHIR, FHIR-Proxy, and FHIR-Bulk Loader
+ Understand the Azure API for FHIR - FHIR-Proxy relationship
+ Configure AAD authentication for FHIR-Proxy
+ Configure Postman for testing FHIR API calls

### Azure API for FHIR and FHIR-Proxy Relationship
In the Azure health data platform, FHIR-Proxy acts as a pre- and post- processor, selectively filtering FHIR data on its way into and out of Azure API for FHIR. Admins can set up FHIR-Proxy to listen to the stream of FHIR data and trigger custom workflows based on specific FHIR events. FHIR-Proxy also brings enhanced Role-Based Access Control (RBAC) to Azure API for FHIR, allowing fine-grained Client Credential Authorization for REST API actions at the FHIR Resource level. This also provides a means of Role-Based Consent so that users (i.e., patients) can authorize or deny access to certain FHIR data.

Component View of Azure API for FHIR and FHIR-Proxy.  _Larger image available [here](./media/component-view.png)_ 

![component-view](./media/component-view-small.png)


## Prerequisites 

Before deploying Azure API for FHIR, FHIR-Proxy, and FHIR-Bulk Loader, please make sure that you have the following permissions in your Azure environment:

+ **Azure Subscription:** User must have rights to deploy resources at the Resource Group scope in their Azure Subscription (i.e. [Contributor](https://docs.microsoft.com/en-us/azure/role-based-access-control/built-in-roles) built-in role).

+ **Azure Active Directory (AAD):** User must have [Application Administrator](https://docs.microsoft.com/en-us/azure/active-directory/roles/permissions-reference#application-administrator) rights for the AAD tenant attached to the Azure Subscription.


## Step 1 - Deploy Azure API for FHIR, FHIR-Proxy, and FHIR-Bulk Loader
In the first part of this challenge, you will
- Visit another repo and read the deployment instructions
- Go to the Azure Portal and begin the process for deploying Azure API for FHIR, FHIR-Proxy, and FHIR-Bulk Loader


To begin, **CTRL+click** (Windows or Linux) or **CMD+click** (Mac) on the link below to visit the fhir-starter quickstart repo (https://github.com/ToddM2/fhir-starter/tree/quickstarts/quickstarts) in a new browser tab.

Follow the instructions in the repo and return here when finished.

## What does success look like for Challenge-01?
+ Azure API for FHIR (PaaS) deployed and available
+ FHIR-Proxy (OSS) deployed and able to communicate with Azure API for FHIR
+ FHIR-Bulk Loader (OSS) deployed and available
+ Postman set up and able to make REST API calls to Azure API for FHIR


## Deployed Components 

Azure API for FHIR and FHIR-Proxy

![proxy-deployment](./media/proxy-deployment.png)

FHIR-Bulk Loader

![fhir-bulk](./media/install-components-small.png)


## Next Steps

Click [here](../Challenge-02/Readme.md) to proceed to the next challenge.
