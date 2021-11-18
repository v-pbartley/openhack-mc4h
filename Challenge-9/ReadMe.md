# Challenge  - Export and Anonymize Data
## Introduction

Welcome to Challenge 9!

In this challenge you will learn how to export anonymized data from the FHIR server.

## Background

Healthcare organizations and payors frequently partner with outside organizations for research projects. If the use case is acedemic and not for treatment, payment, or healthcare operations, the partner organizations cannot have access to PHI data.

## Learning Objectives
By the end of the section you will be able to
* Configure export on the in the FHIR service
* Use the sample anonymization config file to anonymize a data export
* Export anonymized data to and ADLS gen 2 account
* Share anonymized data with a group not affiliated with your organization

## Prerequisites 
* Deployed and populated Azure API for FHIR. If the data you have loaded does not include Immunization or Patient Resources go ahead and [load this bundle](https://github.com/kamoclav/openhack-mc4h-2/blob/main/Challenge-9/synthea_sample_data_fhir_r4%20OpenHack.zip).
* Deployed Azure Data Lake Storage Gen2

## Step 1: Review sample anonymization configuration and customize if needed
Microsoft provides a sample configuration file to anonymize data according to HIPAA safe harbor specifications. It's important to review the sample configuration and HIPAA safe harbor to determine if the sample configuration will work for your organization or if you need to develop your own anonymization rules.

To configure your FHIR service for export to a storage account follow the instructions [here](https://docs.microsoft.com/en-us/azure/healthcare-apis/data-transformation/configure-export-data)

For more information on the sample anonymization file check out [de-identified-export-operation-on-the-fhir-server](https://github.com/microsoft/Tools-for-Health-Data-Anonymization/blob/master/docs/FHIR-anonymization.md#how-to-perform-de-identified-export-operation-on-the-fhir-server)

For a general overview of the $export anonymization query parameters check out [this documentation](https://docs.microsoft.com/en-us/azure/healthcare-apis/data-transformation/de-identified-export)


## Step 2: Export minimal necessary anonymized data to a storage account
HIPAA rules dictate only the minimal data necessary should be used for research projects even if the data is anonymized. Determine what FHIR objects are necessary to study yearly Flu trends.

Perform a de-identified $export operation on the FHIR server. If you get stuck refer to the documentation in step 1.


## Step 3: Securely transfer the file to the research team
Researchers from partner organizations cannot have access to Healthcare or Payor organizations' Azure tennants. You will need to set up a way to transfer the anonymized datasets to them.

Set up a shared access signature (SAS) token to allow the research team to access the anonymized datasets.

If you get stuck check out [Create SAS Tokens](https://docs.microsoft.com/en-us/azure/cognitive-services/translator/document-translation/create-sas-tokens?tabs=Containers)

## Challenge Success

+ Successfully utilize an anonymization configuration file and $export to export a minimally necessary, anonymized dataset from the FHIR server
+ Successfully set up a SAS token to allow access to the anonymized dataset
