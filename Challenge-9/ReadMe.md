# Challenge  - Export and Anonymize Data
The biostatistics program at Sunnyville University regularly partners with Sunrise Healthcare on medical research projects. They are interested in studying yearly Flu trends. Since the use case is academic and not for treatment, payment, or healthcare operations, the biostatisticians cannot have access to PHI. In this challenge you will review the data in your FHIR server, determine the minimal necessary data for the Sunnyville University biostatisticans and export the data anonymized based on the HIPAA Safe Harbor specifications.


## Learning Objectives
By the end of the section you will be able to
* Configure export on the in the FHIR service
* Use the sample anonymization config file to anonymize a data export
* Export anonymized data to and ADLS gen 2 account
* Share anonymized data with a group not affiliated with your organization

## Prerequisites 
* Deployed and populated Azure API for FHIR
* Deployed Azure Data Lake Storage Gen2
* Azure Databricks

### Step 1: Review sample anaonymization configuration and customize if needed
Microsoft provides a sample configuration file to anonymize data according to HIPAA safe harbor specifications. It's important to review the sample configuration and HIPAA safe harbor to determine if the sample configuration will work for your organization or if you need to develop your own anonymization rules.

For more information on the sample anonymization file check out this documentation
https://github.com/microsoft/Tools-for-Health-Data-Anonymization/blob/master/docs/FHIR-anonymization.md#how-to-perform-de-identified-export-operation-on-the-fhir-server


### Step 2: Export minimal necessary anonymized data to a storage account
HIPAA rules dictate only the minimal data necessary should be used for research projects even if the data is anonymized. Determine what FHIR objects are necessary for Sunnyville University students to study yearly Flu trends.

Perform a de-identified $export operation on the FHIR server. If you get stuck refer to the documentation in step 1.


### Step 3: Securely transfer the file to the research team
Since the researchers at Sunnyville University are not a part of Sunrise Healthcare, they cannot be given access in Sunrise Healthcare's Azure.

Set up a shared access signature (SAS) token to allow the research team to access the anonymized datasets.

If you get stuck check out https://docs.microsoft.com/en-us/azure/cognitive-services/translator/document-translation/create-sas-tokens?tabs=Containers

You have successfully supported the Sunnyville University and Sunrise Healthcare research partnership!
