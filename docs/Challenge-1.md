---
title: 1) Deploy FHIR
parent: FHIR Basics
has_children: false
nav_order: 1
---
# Microsoft Cloud for Healthcare OpenHack
## Deploy Azure API for FHIR and FHIR-Proxy (OSS)
[View Repo on GitHub](https://github.com/microsoft/openhack-mc4h/tree/main/Challenge-01){: .btn }

The FHIR service in Azure API for FHIR enables rapid exchange of data through Fast Healthcare Interoperability Resources (FHIR®) APIs, backed by a managed Platform-as-a Service (PaaS) offering in the cloud. It makes it easier for anyone working with health data to ingest, manage, and persist Protected Health Information PHI in the cloud.  Azure Healthcare APIs enables you to:
- Quickly connect disparate health data sources and formats such as structured, imaging, and device data and normalize it to be persisted in the cloud.
- Transform and ingest data into FHIR. For example, you can transform health data from legacy formats, such as HL7v2 or CDA, or from high frequency IoT data in device proprietary formats to FHIR.
- Connect your data stored in Healthcare APIs with services across the Azure ecosystem, like Synapse, and products across Microsoft, like Teams, to derive new insights through analytics and machine learning and to enable new workflows as well as connection to SMART on FHIR applications.
- Manage advanced workloads with enterprise features that offer reliability, scalability, and security to ensure that your data is protected, meets privacy and compliance certifications required for the healthcare industry.

Read more about Microsoft FHIR Services **[here](https://docs.microsoft.com/en-us/azure/healthcare-apis/)** 


## FHIR-Proxy (OSS)
FHIR-Proxy is an Open Source Software project designed to be a secure FHIR Gateway and Proxy. FHIR-Proxy is an Azure Function based solution that:
- Acts as an intelligent and secure gateway to FHIR Servers
- Allows multi-tenant access and purpose driven security policies specialized access to a common FHIR Server
- Provides a consolidated approach to PRE and POST processing of FHIR Server Calls 
- Is integrated with Azure Active Directory for authentication and to provide Role based access control
- Acts as a FHIR specific reverse-proxy rewriting responses and brokering requests to FHIR Servers


## Challenge 
+ Deploy both Azure API for FHIR and FHIR-Proxy to your Azure environment 

Access the __Deploy FHIR Challenge__ **[here](https://github.com/microsoft/openhack-mc4h/tree/main/Challenge-01)**.

## Materials 
**[Postman Collections for Testing](./assets/zip/MC4H_Testing.postman_collection.zip)**


## Reference Links 
Read more about Microsoft FHIR Services **[here](https://docs.microsoft.com/en-us/azure/healthcare-apis/)** 

Read more about FHIR-Proxy Open Source Software Project **[here](https://github.com/microsoft/fhir-proxy)** 
 
Read more about the Microsoft Cloud for Healthcare **[here](https://www.microsoft.com/en-us/industry/health/microsoft-cloud-for-healthcare)**
