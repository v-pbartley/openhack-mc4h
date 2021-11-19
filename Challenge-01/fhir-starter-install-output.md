## Sample script execution 

dale@Azure:~/fhir-starter/scripts$ ./deployFhirStarter.bash
Executing ./deployFhirStarter.bash...
Checking Azure Authentication...

FHIR API Application deployment script...
 - Prerequisite:  Must have rights to provision Resources within the Subscription (ie Contributor)
 - Prerequisite:  Azure CLI (bash) access from the Azure Portal

The script gathers information then lets users choose to use a template or script deployment. <br>
Users without CLI Access can use the template deployment from the templates directory in this repo. <br>

Press Enter to continue, or Ctrl+C to exit

Collecting Azure Parameters (unless supplied on the command line)
Enter your subscription ID <press Enter to accept default> [de91991f-4607-4d0e-80fc-66a33f4e1681]:

This script will look for an existing resource group, otherwise a new one will be created <br>
You can create new resource groups with the CLI using: az group create <br>
Enter a resource group name <press Enter to accept default> [api-fhir-7700]:

If creating a *new* resource group, you need to set a location <br>
You can lookup locations with the CLI using: az account list-locations <br>
Azure API is currently availalbe in: East US, East US 2, North Central US, South Central US, West US, West US 2 <br>
Enter resource group location <press Enter to accept default> [eastus]:
westus2
 <br>
  Checking for existing Resource Group named [api-fhir-7700]... <br>
  Resource Group [api-fhir-7700] not found a new Resource group will be created <br>
--- <br>
Collecting Script Parameters (unless supplied on the command line).. <br>
Enter your FHIR Service name <press Enter to accept default> [fhir7700]: <br>
 <br>
  Checking for exiting FHIR Service named [fhir7700] ...Warnings can be safely ignored... <br>
WARNING: Command group 'config' is experimental and under development. Reference and support levels: https://aka.ms/CLI_refstatus <br>
WARNING: Command group 'healthcareapis service' is experimental and under development. Reference and support levels: https://aka.ms/CLI_refstatus <br>
  FHIR Service [fhir7700] not found, a new FHIR Service will be created <br>

Enter a Key Vault name <press Enter to accept default> [fhir7700kv]: <br>

  Checking for existing Key Vault named [fhir7700kv]... <br>
  Script will deploy new Key Vault [fhir7700kv] for FHIR Service [fhir7700] <br>
 <br>
Do you want to generate a Postman Environment for FHIR Service access? [y/n]:
y <br>
<br>
Ready to start deployment of [fhir7700] with the following values: <br>
Subscription ID:....................... de91991f-4607-4d0e-80fc-66a33f4e1681 <br>
Use Existing Resource Group:........... no <br>
Create New Resource Group:............. yes <br>
Resource Group Name:................... api-fhir-7700 <br>
Resource Group Location:............... westus2 <br>
Use Existing Key Vault:................ no <br>
Create New Key Vault:.................. yes <br>
KeyVault Name:......................... fhir7700kv <br>
FHIR Service Client Application Name:.. fhir7700-svc-client <br>
Generate Postman Environment:.......... yes <br>
 <br>
Please validate the settings above before continuing <br>
Press Enter to continue, or Ctrl+C to exit <br>
 <br>
Starting Deployments <br>
 <br>
Creating Resource Group [api-fhir-7700] in location [westus2] <br>
  az group create --name api-fhir-7700 --location westus2 --output none --tags 'HealthArchitectures FHIRStarter' <br>
 <br>
 <br>
Creating Key Vault [fhir7700kv] in location [api-fhir-7700] <br>
  az keyvault create --name fhir7700kv --resource-group api-fhir-7700 --location westus2 --tags 'HealthArchitectures FHIRStarter' --output none <br>
  stepresult= <br>
 <br>
Deploying FHIR Service [fhir7700] <br>
... note that warnings here are expected and can be safely ignored ... <br>
 <br>
Creating FHIR Service [fhir7700] in location [api-fhir-7700] <br>
WARNING: Command group 'healthcareapis service' is experimental and under development. Reference and support levels: https://aka.ms/CLI_refstatus <br>
WARNING: Command group 'healthcareapis service' is experimental and under development. Reference and support levels: https://aka.ms/CLI_refstatus <br>
 <br>
FHIR Service Audience set to [https://fhir7700.azurehealthcareapis.com] <br>
 <br>
WARNING: Command group 'healthcareapis service' is experimental and under development. Reference and support levels: https://aka.ms/CLI_refstatus <br>
 <br>
FHIR Service Resource ID set to [/subscriptions/de91991f-4607-4d0e-80fc-66a33f4e1681/resourceGroups/api-fhir-7700/providers/Microsoft.HealthcareApis/services/fhir7700] <br>
 <br>
Creating FHIR Service Client Application [fhir7700-svc-client] <br>
WARNING: The output includes credentials that you must protect. Be sure that you do not include these credentials in your code or check the credentials into your source control. <br> For more information, see https://aka.ms/azadsp-cli <br>
WARNING: 'name' property in the output is deprecated and will be removed in the future. Use 'appId' instead. <br>
FHIR Service Client Application ID is [734dfac4-4830-458e-a66c-449ca1971494] <br>
 <br>
Setting FHIR Service Client Object ID <br>
 <br>
Saving FHIR Service Client Information (FS-name) to Key Vault [fhir7700kv] <br>
 <br>
Granting FHIR Service Client Application FHIR Data Contributor Role <br>
 <br>
Generating Postman Environment File <br>
 <br>
The Postman environment [fhir7700.postman_environment.json] has been generated <br>
The environment file along with the FHIR-CALLS-Sample-postman-collection.json can be used to access [fhir7700] <br>
 <br>
Download Files from Cloud Shell <br>
https://docs.microsoft.com/en-us/azure/cloud-shell/using-the-shell-window#upload-and-download-files <br>
 <br>
Importing Postman files <br>
https://learning.postman.com/docs/getting-started/importing-and-exporting-data/#importing-postman-data <br>
************************************************************************************************************
Deployment of FHIR Service [fhir7700] and [fhir7700-svc-client] completed successfully <br>
The FHIR Service Client Application can be used for OAuth2 client_credentials flow authentication to the FHIR Server <br>
Client Credentials have been securely stored as Secrets in the Key Vault [fhir7700kv] <br>
The secret prefix is FS (for FHIR Service) <br>
************************************************************************************************************
dale@Azure:~/fhir-starter/scripts$ <br>

---

## Deployment Architecture 

![diagram](./media/fhir-starter-diagram.png)


