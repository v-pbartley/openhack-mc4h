# Challenge 1 - Deploy Azure API for FHIR (PaaS), FHIR-Proxy (OSS), and FHIR-Bulk Loader (OSS)

## Introduction

Welcome to Challenge 1!

In this challenge, you will use an Azure Resource Manager (ARM) template to deploy **Azure API for FHIR** (PaaS), **FHIR-Proxy** (OSS), and **FHIR-Bulk Loader** (OSS). In addition, you will set up a **Postman** environment to make REST API calls to Azure API for FHIR.

## Background
FHIR (Fast Healthcare Interoperability Resources) is at the center of our healthcare products at Microsoft. Microsoft's support for FHIR rests on two Azure components: [Azure API for FHIR](https://docs.microsoft.com/en-us/azure/healthcare-apis/azure-api-for-fhir/overview) (PaaS) and [FHIR-Proxy](https://github.com/microsoft/fhir-proxy) (OSS). In Azure FHIR data architectures, Azure API for FHIR receives REST API requests and manages all FHIR data persistance and retrieval tasks. Meanwhile, FHIR-Proxy acts as a checkpoint surrounding Azure API for FHIR, filtering the incoming and outgoing data according to a set of admin-defined rules. In effect, FHIR-Proxy serves to enforce Role-Based Access Control (RBAC) at the FHIR Resource level.

For bulk ingestion of FHIR data, Microsoft offers the open-source FHIR-Bulk Loader utility. With FHIR-Bulk loader, admins can import large amounts of FHIR data into Azure API for FHIR without REST API call rate limitations. The FHIR Bulk-Loader can import data from FHIR Bundles (compressed and non-compressed) as well as FHIR NDJSON files. Please visit [here](https://github.com/microsoft/fhir-loader) to learn more about the FHIR-Bulk Loader.  

## Learning Objectives 
+ Use an ARM template to deploy Azure API for FHIR, FHIR-Proxy, and FHIR-Bulk Loader
+ Understand the Azure API for FHIR - FHIR-Proxy relationship
+ Configure AAD authentication for FHIR-Proxy
+ Configure Postman for testing FHIR API calls

### Azure API for FHIR and FHIR-Proxy Relationship
In the Azure health data platform, FHIR-Proxy acts as a pre- and post- processor selectively filtering FHIR data on its way into and out of the FHIR Server within Azure API for FHIR. FHIR-Proxy's fine-grained RBAC brings enhanced Client Credential Authorization capabilities to Azure API for FHIR, providing a means of Role-Based Consent so that users can authorize access to FHIR data.

Component View of Azure API for FHIR and FHIR-Proxy.  _Larger image available [here](./media/component-view.png)_ 

![component-view](./media/component-view-small.png)


## Prerequisites 

Before deploying Azure API for FHIR, FHIR-Proxy, and FHIR-Bulk Loader, please make sure to have the following permissions in your Azure environment:

+ **Azure Subscription Prerequisite:** User must have rights to deploy resources at the Resource Group scope (i.e. Contributor role or Owner role).

+ **Azure Active Directory (AAD) Prerequisite:** User must have Application Administrator rights for the AAD tenant attached to the Azure Subscription.


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

## Next Steps

Click [here](../Challenge-02/Readme.md) to proceed to the next challenge.
