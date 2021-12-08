# Challenge  11 - IoT Connector for FHIR

## Introduction

Welcome to Challenge 11!

Challenges 11 and 12 are designed to introduce you to the upcoming PaaS releases of the IoMT and DICOM services. Challenges 11 and 12 can be performed in any subscription and are not dependent the work from prior challenges.

This challenge will help you become familiar with the data flow for IoT to FHIR. Building on the skills learned in prior challenges, Challenge 11 will broaden your knowledge of Remote Patient Monitoring scenarios.

Challenge 11 introduce the IoT Connector in PaaS, with the OSS deployments offered as a bonus challenges.

## Background

With the rise of wearable devices, Remote Patient Monitoring (RPM) has exploded in the marketplace. Many hardware vendors have tried a proprietary approach for providing the hardware and monitoring software. Microsoft has taken an agnostic approach to Remote Patient Monitoring and wearable data ingestion. Microsoft has created a tool kit for converting the output from any wearable into FHIR resources.

## Learning Objectives

- Deploy and configure the IoT Connector via Azure portal.
- Deploy and configure additional Azure services required for the IoT connector
- Connect the IoT Connector to Azure API for FHIR
- Create a map for incoming device data through to FHIR
- Understand the data flow for medical IoT data

## Challenges

### Challenge 11a

Let us begin with a basic walk through, perform the steps in this [IoT Quickstart](https://docs.microsoft.com/en-us/azure/healthcare-apis/azure-api-for-fhir/iot-fhir-portal-quickstart). Success for 12a means you can query the IoT FHIR Observation via Postman.

Link - https://docs.microsoft.com/en-us/azure/healthcare-apis/azure-api-for-fhir/iot-fhir-portal-quickstart

__Note:__ Azure IoT Central is no longer needed. Please delete your Azure IoT Central instance prior to moving forward.

### Challenge 11b - Building Mappings from Sample Data

Now lets go a step forward. This time let's create our own mappings using sample data.

#### 1) Clone these repos

&nbsp;&nbsp;&nbsp;&nbsp; This hackathon repo (If not already complete)

```azurecli
git clone https://github.com/microsoft/openhack-mc4h
```

&nbsp;&nbsp;&nbsp;&nbsp; IoMT FHIR Connector for Azure

```azurecli
git clone https://github.com/microsoft/iomt-fhir
```

### 2) Install Node.js (If not already complete)

### 3) Setup IoT Mapping Tool

Follow the instructions for running the mapper [here](https://github.com/microsoft/iomt-fhir/tree/master/tools/data-mapper#getting-started)

Link - https://github.com/microsoft/iomt-fhir/tree/master/tools/data-mapper#getting-started

Skip the optional steps on this page.

The mapper will be at this address when running: http://localhost:5000

### 4) Continue through making sample maps

Link - https://github.com/microsoft/iomt-fhir/tree/master/tools/data-mapper#how-to-make-mappings

At the end of step 4 you will have a sample set of IoT Maps which can be used with the Azure IoT Connector for FHIR.

For more information on the IoT Mappings visit the docs page - https://github.com/microsoft/iomt-fhir/blob/master/docs/Configuration.md

__Note:__ When creating a new mapping, you must click the 'Confirm' button. Pressing ENTER after typing will not work.

### (Optional) Step 5

Upload your newly created sample mappings to the IoT Connector via the portal.

- Create a new IoT Connector.
- Figure out the steps for uploading a device mapping.
- Repeat for FHIR mapping.

## Challenge 11c

This is the most difficult challenge. However, this could be one of the most crucial to the success of an IoMT/ RPM project.

Use the IoT Mapper from Challenge 11b to create maps for the sample messages in the SampleData folder. There are three sample messages in one file - vitals, BP, and weight. Vitals is an array of data while BP & weight are single entry messages. The SampleData folder has two files. Both files are the same data. Three-Sample-Message-Types-with-labels.json is the message data with data descriptions and/or units of measure.

When you get to the FHIR mapping you can make up values for the 'Code' For example - Code: A1235, System: https://loinc.org, Text: Heart Rate

Answers are in the 'Answer' folder if you get stuck. Final mappings may vary from the answer mapping.

Hint - You may need to create multiple maps and combine the output into a single JSON file.

## [BONUS] Challenge 11d

This challenge is a variation of Challenge 11a. Deploy and configure the OSS IoMT FHIR Connector for Azure. Use Azure IoT Central as the source and the mappings from the Quickstart.

Link to OSS - https://github.com/microsoft/iomt-fhir