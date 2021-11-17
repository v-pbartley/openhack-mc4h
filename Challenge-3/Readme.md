# Challenge 3 - Ingest to FHIR

## Introduction

Welcome to Challenge 3!

In this challenge you will learn how to use the [FHIR Bulk Loader](https://github.com/microsoft/fhir-loader) tool to bulk-ingest data into Azure API for FHIR.

## Background

FHIR is an evolving standard, and one area where the FHIR specification is still in its early stages of development is its coverage of bulk data ingestion. Until HL7 publishes specifications for a FHIR $import operator, implementors will have to rely on alternative methods of getting bulk FHIR data into a FHIR server. In this challenge, we will be working with the current best-practice solution for bulk FHIR import into Azure API for FHIR: the FHIR Bulk Loader utility offered by Microsoft as part of the suite of open-source FHIR tools.

## Learning Objectives

+ Understand data constraints with FHIR bulk data loading
+ Understand how to track and compare bulk FHIR imports

## Prerequisites

+ Successful completion of Challenge 1
+ Postman
+ Text Editor

---

## Step 1 - FHIR Bulk Loader Installation

1. Follow [documentation](https://github.com/microsoft/fhir-loader/blob/main/docs/deployment.md) to install the FHIR Bulk Loader

## Step 2 - Download Sample Data

1. Download the following files to your desktop
    + [good_bundles.zip](/docs/assets/zip/good_bundles.zip)
    + [bad_bundles.zip](/docs/assets/zip/bad_bundles.zip)

## Step 3 - Upload Sample Data

1. In the Azure Portal, navigate to the FHIR Bulk Loader Blob Storage resource that was created in `Step 1`

2. Click on `Storage browser (preview)` and then click on `Blob container`
![Blob Containers](/Challenge-3/media/loader_containers.jpg)

3. Using the `good_bundles.zip` file downloaded in Step 1:
    + Determine which container this file should be uploaded too

4. Using  the `bad_bundles.zip` file downloaded in Step 1:
    + Determine which container this file should be uploaded too

> Refer to the FHIR Bulk Loader [testing](https://github.com/microsoft/fhir-loader/blob/main/docs/testing.md) documentation for more information

## Challenge Success

+ Successfully upload and import data from the file `good_bundles.zip`
+ Successfully upload and import data from the file `bad_bundles.zip`
