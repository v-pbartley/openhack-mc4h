# Challenge 1 - Deloy Azure API for FHIR and FHIR-Proxy (OSS)

## Introduction

Welcome to Challenge 1!

In this challenge you will deploy both Azure API for FHIR (PaaS) and FHIR-Proxy (Open Source Software).

## Background
FHIR is at the center of our healthcare products at Microsoft. FHIR data support in MC4H solutions rests on two fundamental components: Azure API for FHIR and FHIR-Proxy. In MC4H architectures, Azure API for FHIR is at the nexus of FHIR data activity, and FHIR-Proxy acts as a checkpoint, filtering data and enforcing Role-Based Access Control (RBAC) at the FHIR resource level.

## Learning Objectives 
+ Understand the prerequisites for deploying Azure API for FHIR and FHIR-Proxy
+ Become familiar with the Azure API for FHIR and FHIR-Proxy deployment process

## Prerequisites 
HealthArchitecture scripts will gather (and export) information necessary for the proper deployment and configuration of Azure API for FHIR, in addition to multiple HealthArchitecture Open Source Software (OSS) components.  
+ Azure Prerequisite: User must have rights to deploy resources at the Subscription scope (ie Contributor role or Owner role).
+ Azure Active Directory (AAD) Prerequisite: User must have Application Administrator (built-in RBAC role) rights for the AAD tenant they are deploying into.
  

## Step 1 - Set up Azure Environment 
Welcome to Challenge 1 - deploying Azure API for FHIR.  For this challenge we will walk through the following steps: 
- Login to Azure CLI (via the Portal or directly at shell.azure.com)
- Clone the FHIR-Starter repo 
- Execute the deployment scripts 
- Set up Postman 
- Test Authentication 

[![Launch Azure Shell](./media/launchcloudshell.png "Launch Cloud Shell")](https://shell.azure.com/bash?target="_blank")




Select Bash Shell as the operating environment 

## Step 2 - FHIR Service deployment 
HealthArchitecture repos follow a common naming standard (github.com/microsoft/fhir-NAME).  
- Navigate to the FHIR-Starter repo https://github.com/microsoft/fhir-starter, review the main Readme.md, and the [Readme.md](https://github.com/microsoft/fhir-starter/blob/main/scripts/Readme.md) in the ./scripts folder.
- Clone the Repo
- Run the deployFhirStarter.bash script either from the command line or using the prompts
- Be certain to GENERATE the POSTMAN Env

__Note__  During a live session, Resource Groups names will be assigned. If you are performing this hack on your own, you can use any Resource Group name. 

## Step 3 - Setup Postman
Using the Upload / Download button on the Azure CLI, download the _$fhirServiceName.postman_environment.json_ file to your computer. 

Import the Postman Search Collection if you have not already done so. See https://microsoft.github.io/openhack-mc4h/Challenge-1.html for the collection download.

Test access to your FHIR Service 

_[Need help with Postman - try this](https://github.com/daemel/fhir-postman)_ 


## Step 4 - Proxy Setup 
HealthArchitecture repos follow a common naming standard (github.com/microsoft/fhir-NAME).  
- Navigate to the FHIR-Proxy repo https://github.com/microsoft/fhir-proxy, review the main Readme.md, and the [Readme.md](https://github.com/microsoft/fhir-proxy/blob/main/scripts/Readme.md) in the ./scripts folder.
- Clone the Repo
- Run the deployfhirproxy.bash script either from the command line or using the prompts
- Be certain to GENERATE the POSTMAN Env

__Note__  During a live session, Resource Groups names will be assigned.  If you are performing this hack on your own, you can use any Resource Group name. 

## Step 5 - Setup Postman with Proxy 
Using the Upload / Download button on the Azure CLI download the _$fhirServiceName.postman_environment.json_ file to your computer. 



## Challenge Success
+ Azure API for FHIR (PaaS) installed and available 
+ FHIR-Proxy (Open Source Software) installed and able to communicate with Azure API for FHIR
