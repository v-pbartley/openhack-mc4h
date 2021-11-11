#  Challenge 4 - Query and Search FHIR

## Introduction

Welcome to Challenge 4!

In this challenge you will learn how to use the FHIR server's search operations.

## Background
The FHIR specification defines the fundamentals of search for FHIR resources. This hack will guide you through some key aspects to searching resources in FHIR. 

## Learning Objectives 
+ Understand the basic concepts of FHIR Search
+ Perform both Common and Composite Searches 
+ Use Modifiers in Search 
+ Use a Chained & Reverse Chained Search 
+ Defining a Custom Search parameter 


## Search basics 
Each FHIR Resource has specific Search parameters in addition to the [common parameters](https://www.hl7.org/fhir/search.html#all) which also apply. See [Searching](https://www.hl7.org/fhir/search.html) for more information about searching in REST, messaging, and services.  

+ [Patient Resource Search Parameters](https://www.hl7.org/fhir/patient.html#search)


FHIR searches can be against a specific resource type, a specified compartment, or all resources. The simplest way to execute a search in FHIR is to use a GET request. For example, if you want to pull all patients in the database, you could use the following request:

```azurecli
GET {{FHIR_URL}}/Patient
```

You can also search using POST, which is useful if the query string is too long. To search using POST, the search parameters can be submitted as a form body. This allows for longer, more complex series of query parameters that might be difficult to see and understand in a query string.

If the search request is successful, you’ll receive a FHIR bundle response with the type searchset. If the search fails, you’ll find the error details in the OperationOutcome to help you understand why the search failed.

## Common Search Parameters 
The following parameters apply to all resources: ```_content```, ```_id```, ```_lastUpdated```, ```_profile```, ```_query```, ```_security```, ```_source```, ```_tag```.  In addition, the search parameter ```_text``` and ```_filter``, (documented below) also applies to all resources (as do the search result parameters).

The search parameter _id refers to the logical id of the resource, and can be used when the search context specifies a resource type:

```azurecli
 GET {{FHIR_URL}}/Patient?_id=23
```

This search finds the patient resource with the given id (there can only be one resource for a given id). 

## Challenge - Understand the basic concepts of FHIR Search
Using the Postman file [provided]() 


## Challenge - Perform both Common and Composite Searches 




## Challenge - Use Modifiers in Search 




## Challenge - Use a Chained & Reverse Chained Search 




## Challenge - Defining a Custom Search parameter 

