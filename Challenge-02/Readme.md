# Challenge-02 - Convert HL7 and C-CDA to FHIR

## Introduction

Welcome to Challenge-02!

In this challenge you will learn how to use the custom `$convert-data` operation in Azure API for FHIR to convert HL7 and C-CDA files into FHIR.

## Background

In today's health industry, the FHIR R4 format has become the HLS industry standard for storage and exchange of health data. As FHIR interoperability spreads throughout the industry, health IT operations are deploying conversion pipelines for ingesting and transforming legacy data formats into FHIR. Two of the most common legacy formats still in use are HL7v2 and C-CDA. In this challenge, we will explore how to convert these formats into FHIR using the Microsoft health data platform.

## Learning Objectives

+ Make an API call for a FHIR API operation 
+ Specify API request parameters in Postman
+ Prepare/clean data for conversion into FHIR

## Prerequisites

+ Successful completion of Challenge-01
+ Postman installed
+ [VS Code](https://code.visualstudio.com/) or [7Edit](http://7edit.com/home/) (optional)
+ [VS Code HL7 Language Support](https://marketplace.visualstudio.com/items?itemName=pbrooks.hl7) (optional)

---

## Step 1 - Postman Setup

1. Create a `New Request` in the Postman collection imported in Challenge-01.
![New Postman Request Image](./media/add_request.jpg)
2. Rename the new request to `Convert Data - HL7`.
3. Change the HTTP operation type from **GET** to **POST**.
4. Fill in the URL of this request with `{{fhirurl}}/$convert-data`.
5. Change to the **Authorization** tab of the request and change:
    + **Type** to **OAuth 2.0**
    + Add `{{bearerToken}}` as the **Access Token**

    + ![Request Authorization Tab](./media/request-auth.jpg)

## Step 2 - Setup Request Parameters

1. Download the sample HL7 file, [ADT_A01.hl7](./samples/ADT_A01.hl7), from the Challenge 2 samples folder.

2. [Optional] Review the contents of the HL7 file using 7Edit or open the HL7 file in VS Code and view it using the HL7 extension.

3. Refer to the Azure API for FHIR [documentation](https://docs.microsoft.com/en-us/azure/healthcare-apis/azure-api-for-fhir/convert-data) on how to set up request parameters for a ```$convert-data``` call.

## Step 3 - Convert Data

1. Get a new Bearer token from the FHIR server via Postman.
2. Execute the `Convert Data - HL7` request.

## Step 4 - Convert C-CDA Data

1. Create a `New Request` in the Postman collection created in Challenge 1.
![New Postman Request Image](./media/add_request.jpg)
2. Rename the new request to `Convert Data - CCDA`.
3. Change the HTTP operation type from **GET** to **POST**.
4. Fill in the URL of this request with `{{fhirurl}}/$convert-data`.
5. Change to the **Authorization** tab of the request and change:
    + **Type** to **OAuth 2.0**
    + Add `{{bearerToken}}` as the **Access Token**

    + ![Request Authorization Tab](./media/request-auth.jpg)

## Step 5 - Setup Request Parameters

1. Download the sample C-CDA file [CCDA_Ford_Elaine.xml](./samples/CCDA_Ford_Elaine.xml), from the Challenge 2 samples folder.

2. Refer to the FHIR server [documentation](https://github.com/microsoft/fhir-server/blob/main/docs/ConvertDataOperation.md#2-make-api-call) for ```$convert-data``` on how to create a parameter request.

## Step 6 - Convert Data

1. Get a new Bearer token from the FHIR server via Postman.
2. Execute the `Convert Data - CCDA` request.

> Note: You may have to escape certain values in the C-CDA before executing the request.

## What does success look like for Challenge-02?

+ Successfully received a FHIR bundle from calling ```$convert-data``` with HL7 data
+ Successfully received a FHIR bundle from calling ```$convert-data``` with C-CDA data

## Next Steps

Click [here](../Challenge-03/Readme.md) to proceed to the next challenge.
