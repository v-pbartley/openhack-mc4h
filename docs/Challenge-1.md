---
title: 1) Deploy FHIR
parent: FHIR Basics
has_children: false
nav_order: 1
---

# Introduction 
The healthcare industry is rapidly transforming health data to the emerging standard of [FHIR®](https://hl7.org/fhir/) (Fast Healthcare Interoperability Resources). FHIR enables a robust, extensible data model with standardized semantics and data exchange that enables all systems using FHIR to work together. 

Transforming your data to FHIR allows you to quickly connect existing data sources such as the electronic health record systems or research databases. FHIR also enables the rapid exchange of data in modern implementations of mobile and web development. Most importantly, FHIR can simplify data ingestion and accelerate development with analytics and machine learning tools.


## API FHIR (PaaS) 
The FHIR service in the Azure Healthcare APIs (hereby called the FHIR service) enables rapid exchange of data through Fast Healthcare Interoperability Resources (FHIR®) APIs, backed by a managed Platform-as-a Service (PaaS) offering in the cloud. It makes it easier for anyone working with health data to ingest, manage, and persist Protected Health Information PHI in the cloud

Deploy Azure API for FHIR  
[Challenge 1](https://github.com/microsoft/openhack-mc4h/blob/main/Challenge-1/#fhir-starter-deploying-azure-api-for-fhir-via-cli)


## FHIR-Proxy (OSS)
FHIR-Proxy is an Open Source Software project designed to be a secure FHIR Gateway and Proxy.  FHIR-Proxy is an Azure Function based solution that:
- Acts as an intelligent and secure gateway to FHIR Servers
- Allows multi-tenant access and purpose driven security policies specialized access to a common FHIR Server
- Provides a consolidated approach to PRE and POST processing of FHIR Server Calls to support various access and result filtering or actions.
- Is integrated with Azure Active Directory for authentication and to provide Role based access control.
- Acts as a FHIR specific reverse proxy rewriting responses and brokering requests to FHIR Servers

Deploy FHIR-Proxy  
[Challenge 1](https://github.com/microsoft/openhack-mc4h/blob/main/Challenge-1/#fhir-proxy-deploying-fhir-proxy-via-cli)


## Testing with Postman 

Setup Postman 
[Challenge 1](https://github.com/microsoft/openhack-mc4h/blob/main/Challenge-1/#postman-setup-and-testing)


## Videos 

### Deploying Healthcare API 
Quick video on deploying Azure API for FHIR  
<a href="./assets/video/Deploy-FHIR-Service.mp4" title="Deploying Healthcare API's with Workspaces"><img src="./assets/images/FHIR-icon.png" alt="FHIR" /></a>

Quick video on deploying the new Healthcare API for FHIR  
<a href="./assets/video/Deploy-FHIR-Service.mp4" title="Deploying Healthcare API's with Workspaces"><img src="./assets/images/FHIR-icon.png" alt="FHIR" /></a>


## Reference Links 
- [Microsoft Docs](https://docs.microsoft.com/en-us/azure/healthcare-apis/)
 
