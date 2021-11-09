# Challenge 1 - Deploy Azure API for FHIR
Welcome to Challenge 1 - deploying Azure API for FHIR.  For this challenge we will walk through the following 
- Login to Azure CLI (via the Portal or directly at shell.azure.com)
- Clone the FHIR-Starter repo 
- Execute the deployment scripts 
- Setup Postman 
- Test Authentication 

Supporting material can be found on the IO Page for this hack - https://microsoft.github.io/openhack-mc4h/ 

---

# FHIR-Starter Deploying Azure API for FHIR via CLI
This script will gather information necessary to the proper deployment and configuration of Azure API for FHIR (PaaS) and the following: an Azue AD Application Service Client, Key Vault and Resource Group.
  
 Prerequisites:  
 - User must have rights to deploy resources at the Subscription scope
 - User must be able to provision an Azure AD Application Service client  

__Note__
A Keyvault is necessary for securing Service Client Credentials used with the FHIR Service and FHIR-Proxy.  Only 1 Keyvault should be used as this script scans the keyvault for FHIR Service and FHIR-Proxy values. If multiple Keyvaults have been used, please use the [backup and restore](https://docs.microsoft.com/en-us/azure/key-vault/general/backup?tabs=azure-cli) option to copy values to 1 keyvault.

__Note__ 
The FHIR-Starter scripts are designed for and tested from the Azure Cloud Shell - Bash Shell environment.

## Step 1. Setup 
Please note you should deploy these components into a tenant that you have appropriate permissions to create and manage Application Registrations, Enterprise Applications, Permissions and Role Definitions Assignments

1. [Get or Obtain a valid Azure Subscription](https://azure.microsoft.com/en-us/free/)

2. [Open Azure Cloud Shell](https://shell.azure.com) you can also access this from [azure portal](https://portal.azure.com)

3. Select Bash Shell 

4. Clone this repo 
```azurecli
git clone https://github.com/microsoft/fhir-starter
```
5. Change to the new directory to keep files organized within the fhir-starter directory
```azurecli
cd ./fhir-starter
```
6. Make the bash scripts executable
```azurecli
chmod +x ./scripts/*.bash
``` 

## Step 2.  deployFhirStarter.bash
This is the main component deployment script for the Azure Components.    

Run the deployment script and follow the prompts
```azurecli
./scripts/deployFhirStarter.bash 
```

Optionally the deployment script can be used with command line options 
```azurecli
./scripts/deployFhirStarter.bash -i <subscriptionId> -g <resourceGroupName> -l <resourceGroupLocation> -k <keyVaultName> -n <fhirServiceName> -p <yes -or - no>
```

Azure Components installed 
 - Resource Group (if needed)
 - Healthcare API for FHIR 
 - Key Vault 
 - Azure AD Application Service Client 

Information needed by this script 
 - FHIR Service Name
 - KeyVault Name 
 - Resource Group Location 
 - Resource Group Name 

__FHIR-Starter__ Key Vault values saved by this script 

Name              | Value                                | Use             
------------------|--------------------------------------|---------------------------------
FS-TENANT-NAME    | Azure AD Tenant GUID                 | Tenant where Client applications can obtain a Token 
FS-CLIENT-ID      | Service Client Application ID        | Client Application ID used for Token Access  
FS-CLIENT-SECRET  | Service Client Application Secret    | Client Application Secret used for Token Access                    
FS-SECRET         | Service Client Application Secret    | Saved for backwards compatibility  
FS-RESOURCE       | Application Endpoint for Auth Access | Endpoint for Authority (AD) Token grant  
FS-URL            | Application Endpoint for Clients     | Endpoint for FHIR Service interaction 


---

# FHIR-Proxy Deploying FHIR-Proxy via CLI




--- 

# Postman Setup and Testing 







