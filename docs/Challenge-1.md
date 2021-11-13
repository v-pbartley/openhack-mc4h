---
title: 1) Deploy FHIR
parent: FHIR Basics
has_children: false
nav_order: 1
---

## Azure API for FHIR
The FHIR service in the Azure API for FHIR (hereby called the FHIR service) enables rapid exchange of data through Fast Healthcare Interoperability Resources (FHIR®) APIs, backed by a managed Platform-as-a Service (PaaS) offering in the cloud. It makes it easier for anyone working with health data to ingest, manage, and persist Protected Health Information PHI in the cloud


## FHIR-Proxy (OSS)
FHIR-Proxy is an Open Source Software project designed to be a secure FHIR Gateway and Proxy.  FHIR-Proxy is an Azure Function based solution that:
- Acts as an intelligent and secure gateway to FHIR Servers
- Allows multi-tenant access and purpose driven security policies specialized access to a common FHIR Server
- Provides a consolidated approach to PRE and POST processing of FHIR Server Calls 
- Is integrated with Azure Active Directory for authentication and to provide Role based access control
- Acts as a FHIR specific reverse-proxy rewriting responses and brokering requests to FHIR Servers


## Challenge 
+ Deploy both Azure API for FHIR and FHIR-Proxy to your Azure environment 
+ Test Authentication and Authorization with Postman


Access the __Deploy FHIR Challenge__ **[here](https://github.com/microsoft/openhack-mc4h/tree/main/Challenge-1)**.


## Materials 

**[Postman Collections for Testing](./assets/zip/MC4H_Testing.postman_collection.zip)**

## Videos 

### Deploying via Azure Portal 
Quick video on deploying Azure API for FHIR  
<a href="./assets/video/Deploy-FHIR-Service.mp4" title="Deploying Azure API for FHIR"><img src="./assets/images/FHIR-icon.png" alt="FHIR" /></a>

Quick video on deploying the new Healthcare API for FHIR  
<a href="./assets/video/Deploy-FHIR-Service.mp4" title="Deploying Healthcare API's with Workspaces"><img src="./assets/images/FHIR-icon.png" alt="FHIR" /></a>


## Reference Links 
- [Microsoft Docs](https://docs.microsoft.com/en-us/azure/healthcare-apis/)
 
