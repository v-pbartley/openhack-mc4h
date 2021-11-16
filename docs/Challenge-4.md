---
title: 4) Query & Search FHIR
parent: FHIR Basics
has_children: false
nav_order: 4
---


## Search 
Searching for resources is fundamental to the mechanics of FHIR. Search operations traverse through an existing set of resources filtering by parameters supplied to the search operation.

Search operations are executed in one of three defined contexts that control which set of resources are being searched:

A specified resource type: 
```azurecli
GET [base]/[type]?parameter(s)
```

A specified compartment, perhaps with a specified resource type in that compartment: 
```azurecli
GET [base]/Patient/[id]/[type]?parameter(s)
```

All resource types:  
```azurecli
GET [base]?parameter(s) (parameters common to all types)
```

_Note_ Search using GET may include sensitive information in the search parameters. Therefore, secure communications and endpoint management are recommended.

## Challenge 

Access the **Search Challenge [here](https://github.com/microsoft/openhack-mc4h/tree/main/Challenge-4)**.


## Materials   
**[Postman Search Collection](./assets/zip/FHIR_Search.postman_collection.zip)**

click to download to your desktop, unzip then import
for help on importing postman files: https://learning.postman.com/docs/getting-started/importing-and-exporting-data/#importing-postman-data
