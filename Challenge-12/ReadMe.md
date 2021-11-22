# Challenge  12 - DICOM

## Introduction

Welcome to Challenge 12!

Congratulations for almost reaching the end. Challenge 12 is a standalone challenge. This challenge is designed to help you become familiar with Medical Imaging basics. This challenge can be performed in either your personal/ organization subscription or the subscription provided for the hackathon.

## Background

Research is broadening beyond text based research. These research initiatives require more resources than on-prem datacenters can provide. DICOM dataset pushing into the 10s of Petabytes, which is pushing the limits of on-prem storage. These larger datasets need a standardized place to reside. The Microsoft Medical Imaging Service provides a DICOMweb standard method for storing these images. This challenge will allow some hands-on experience to how this services, stores, retrieves, and updates images.

## Learning Objectives

- Setup a DICOM instance within Azure Healthcare APIs
- Submit DICOM files to the service
- Successfully view the files with a DICOM viewer connected to the Azure Healthcare APIs

*Note: Azure Healthcare APIs is still in Public Preview. For customers looking to move to production prior to GA please use the OSS Imaging Service or contact this team.*

## Steps

### 1) Clone these repos

&nbsp;&nbsp;&nbsp;&nbsp; This hackathon repo (If not already complete)

```azurecli
git clone https://github.com/microsoft/iomt-fhir
```

&nbsp;&nbsp;&nbsp;&nbsp; The Medical Imaging Server for Azure

```azurecli
git clone https://github.com/microsoft/dicom-server
```


### 2) Setup an Azure Healthcare APIs Workspace using Azure Portal
 
 [Deploy workspace in the Azure portal - Azure Healthcare APIs | Microsoft Docs](https://docs.microsoft.com/en-us/azure/healthcare-apis/healthcare-apis-quickstart)


### 3) Setup DICOM Service using Azure Portal

[Deploy DICOM service using the Azure portal](https://docs.microsoft.com/en-us/azure/healthcare-apis/dicom/deploy-dicom-services-in-azure)

### 4) Choose a path for the rest of the Challenge

Here you need to choose a path for completing the challenge. Thereare two paths
Basic Path and Advanced Path.

**Basic Path** - GUI based operations for uploading Images to the DICOM Service

**Advanced Path** - Programatic method for uploading images to DICOM Service

### Basic Path

This path will use a tool to upload images to the DICOM Service. You will need to setup the upload tool. Configure with the URL you created Step 3. Then upload the image studies.

#### 1) Install upload tool

The upload tool is part of the OSS Medicial Imaging Service for DICOM. You cloned it in Step 2. Follow the instruction [here](https://github.com/microsoft/dicom-server/tree/main/tools/dicom-web-electron) to install and configure the tool. Where you see localhost, replace with the URL from the DICOM service created in Step 3.

If you have not installed Node.js in prior challenges, go to [nodejs.org](https://nodejs.org/), download and install the latest version.

#### 2) Upload images

Once the tool in the prior step is setup and configured, follow the steps to upload the same images from the [dicom-server repo](https://github.com/microsoft/dicom-server/tree/main/docs/dcms). There should be 3 images.

#### 3) Open Viewer and View images

The DICOM Services has a built in DICOM Viewer. By copying and pasting the main URL for the DICOM service into a web browswer you can see the list of uploaded Studies.

If you see 3 Studies listed and they open then you have successful completed this part of the challenge. Move to Part 2 of the challenge.

### Advanced Path

#### 1) Choose a method for uploading images (C#, cURL, or Python)

C# - https://docs.microsoft.com/en-us/azure/healthcare-apis/dicom/dicomweb-standard-apis-c-sharp

cURL - https://docs.microsoft.com/en-us/azure/healthcare-apis/dicom/dicomweb-standard-apis-curl

Python - https://docs.microsoft.com/en-us/azure/healthcare-apis/dicom/dicomweb-standard-apis-python

#### 2) Perform the sample tasks of uploading the files from the link(s) above

Note: The sample files for the link above were downloaded via the second repo clone in Step 1. 

#### 3) View Images in Browser

The DICOM Services has a built in DICOM Viewer. By copying and pasting the main URL for the DICOM service into a web browswer you can see the list of uploaded Studies.

If you see 3 Studies listed and they open then you have successful completed this part of the challenge.

## Part 2

Depending on the path you took, Basic or Advanced, repeat your path using the image studies provided in the SampleData folder of this Challenge's repo.

Success is seeing actual human images in your stuides in the DICOM Service.

## Part 3 - BONUS Challenge

The bonus part of the challenge is to repeat your path but this time deploy the OSS Medical Imageing Server for DICOM. You have already cloned the repo for the tools.

Tip - The GitHub repo site has an Deploy to Azure button built in.
