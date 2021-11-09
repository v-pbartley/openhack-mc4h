# Challenge 0 - Pre-Req Overview
Welcome! Here we'll introduce the basic toolkit used for this OpenHack, and we'll review some of the key topics and concepts that you'll encounter.

## Prerequisites
(please be sure to have the following set up in your environment)

+ Azure Subscription with Contributor/Co-Owner rights 
+ Dynamics Environment + MC4H temporary license and solution set 
+ GitHub account 
+ Postman (cloud or desktop) 

## FHIR - Overview

**Fast Healthcare Interoperability Resources** (FHIR) is the Health and Life Sciences (HLS) industry standard format for storing and exchanging healthcare data. FHIR is specified both as a data model for structuring real-world healthcare information, and as a RESTful API for exchange of healthcare data between Electronic Health Record (EHR) systems. By providing an industry-wide standard for the structure and exchange of health data, FHIR enables health data interoperability, allowing patients' Personal Health Information (PHI) to travel where it is needed. More information is available at [https://www.hl7.org/fhir/overview.html](https://www.hl7.org/fhir/overview.html).

## Microsoft Cloud for Healthcare - Overview
**Microsoft Cloud for Healthcare** is the aggregrate of Microsoft's Health and Life Sciences (HLS) industry solutions, encompassing Azure API for FHIR and its full complement of supporting tools - enabling health data interoperability and integration with Microsoft Dynamics MC4H workstreams.

Azure API for FHIR together with FHIR Proxy (OSS) and the supporting suite of tools enable EHR interoperability, legacy health data format conversion, eventing workflows, IoMT connectivity, bulk FHIR data pipelines for research and ML, SMART on FHIR applications, and more.

Applications built on the Dynamics platform (which include Dynamics model-driven apps) make use of Dataverse and can operate without need of making REST API calls directly to Azure API for FHIR. In addition to running Microsoft Cloud for Healthcare solutions, developers can also take advantage of the Dynamics low-code/no-code environment to construct patient or provider-facing solutions/applications that can tap into healthcare data persisted in Azure API for FHIR.

## Analytics 

Data analytics are fundamental to a wide range of disciplines in the Health and Life Sciences (HLS) industry, including clinical trials, medical research, population health, clinical ML model development, 'omics (genomics, metagenomics, etc.), healthcare quality improvement studies, and more. Many of the challenges in this OpenHack will touch on topics related to data analytics, including FHIR data bulk export and anonymization (i.e., de-identification of PHI).


