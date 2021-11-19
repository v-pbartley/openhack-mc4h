## Sample script execution

### Repo Download 
```
dale@Azure:~$ git clone -b main https://github.com/microsoft/fhir-cds-agent
Cloning into 'fhir-cds-agent'...
Username for 'https://github.com': daemel@microsoft.com
Password for 'https://daemel@microsoft.com@github.com':
remote: Enumerating objects: 441, done.
remote: Counting objects: 100% (441/441), done.
remote: Compressing objects: 100% (335/335), done.
remote: Total 441 (delta 216), reused 253 (delta 82), pack-reused 0
Receiving objects: 100% (441/441), 47.57 MiB | 38.14 MiB/s, done.
Resolving deltas: 100% (216/216), done.
dale@Azure:~$
```

### Deployment Script execution (part 1)
```
dale@Azure:~/fhir-cds-agent/scripts$ ./deploysyncagent.bash
Executing ./deploysyncagent.bash...
Checking Azure Authentication...

FHIR-SyncAgent Application installation script...
 - Prerequisite:  Azure API for FHIR must be installed
 - Prerequisite:  HealthArchitectures FHIR-Proxy must be installed with a KeyVault

Note: You must have rights to able to provision Service Bus resources, Function Apps and App Insights at the Subscription level

Press Enter to continue, or Ctrl+C to exit

Collecting Azure Parameters (unless supplied on the command line)
Enter your subscription ID <press Enter to accept default> [de91991f-4607-4d0e-80fc-66a33f4e1681]:

This script will look for an existing resource group, otherwise a new one will be created
You can create new resource groups with the CLI using: az group create

Enter a resource group name []:
api-fhir-7700
If creating a *new* resource group, you need to set a location
You can lookup locations with the CLI using: az account list-locations

Enter resource group location []:
westus2

Collecting Script Parameters...
Enter your application install prefix <press Enter to accept default> [syncagent26952]:
syncagent7700

Enter an existing keyvault name to retrieve FHIR-Proxy configuration []:
fhir7700kv

   Checking for keyvault fhir7700kv...
   ............. fhir7700kv found

   Checking [fhir7700kv] for FHIR-Proxy configuration...
   .......... found FP-HOST: [sfp7700.azurewebsites.net]

   Checking [fhir7700kv] for FHIR Service configuration...
   ......... found FHIR Service [https://fhir7700.azurehealthcareapis.com]
   ......... FHIR Resource ID set to: [fhir7700]

Enter the FHIR-SyncAgent app name <press Enter to accept default> [sfsa9344]:
sfsa7700

Enter the Service Bus SKU to be used, Premium or Standard <press Enter to accept default> [Standard]:

Setting default subscription.....
Using api-fhir-7700 as resource group...
Ready to start deployment of [sfsa7700] with the following values:
Subscription ID:  GUID
Resource Group Name:  api-fhir-7700
Resource Group Location:  westus2
Application Prefix:  syncagent7700
 FHIR-Proxy App Name: sfp7700
 FHIR Service Name: fhir7700
Service Bus SKU:  Standard

Please validate the settings above and...
Press Enter to continue, or Ctrl+C to exit

Updating Secure FHIR-Proxy [sfp7700] Application Configuration to enable FHIR-SyncAgent...

Starting Secure FHIR-SyncAgent Function Application [sfsa7700] deployment...
Creating Secure Function App Storage Account [syncagent7700store]...
Retrieving Storage Account Connection String...
Creating ndjson container in the SyncAgent Storage Account...
...note this is for small scale testing, not production capacity - for production, use the FHIR-Loader
Creating Secure FHIR-SyncAgent Function App Serviceplan [syncagent7700asp]...
Creating Secure FHIR-SyncAgent Function App [sfsa7700]...
WARNING: --runtime-version is not supported for --runtime dotnet. Dotnet version is determined by --functions-version. Dotnet version will be 3.1 for this function app.
WARNING: Application Insights "sfsa7700" was created for this Function App. You can visit https://portal.azure.com/#resource/subscriptions/GUID/resourceGroups/api-fhir-7700/providers/microsoft.insights/components/sfsa7700/overview to view your Application Insights component
FHIR-SyncAgent Function App Host name = sfsa7700.azurewebsites.net
FHIR-SyncAgent [sfsa7700] state...
  "state": "Running",
Creating MSI for FHIR-SyncAgent Function App [sfsa7700]
Setting Application Config MSI Setting
Setting KeyVault Policy to allow KeyVault Secret access for FHIR-SyncAgent App...
Applying FHIR-SyncAgent Application Configuration settings for [sfsa7700]...
Retrieving FHIR-SyncAgent Host Key...  this step will automatically retry if it fails
ERROR: Bad Request({"Code":"BadRequest","Message":"Encountered an error (ServiceUnavailable) from host runtime.","Target":null,"Details":[{"Message":"Encountered an error (ServiceUnavailable) from host runtime."},{"Code":"BadRequest"},{"ErrorEntity":{"Code":"BadRequest","Message":"Encountered an error (ServiceUnavailable) from host runtime."}}],"Innererror":null})
Command failed. Retry Attempt 2/5 in 20 seconds:
Deploying FHIR-SyncAgent App code from local source to [sfsa7700]... this step will automatically retry if it fails
WARNING: Setting SCM_DO_BUILD_DURING_DEPLOYMENT to false
WARNING: Waiting SCM site to be updated with the latest app settings
WARNING: Getting scm site credentials for zip deployment
WARNING: Starting zip deployment. This operation can take a while to complete ...
WARNING: Deployment endpoint responded with status code 202
...NOTE:  After deployment, the FHIR-SyncAgent App [sfsa7700] will restart automatically
FHIR-SyncAgent [sfsa7700] state...
  "state": "Running",
Setting [sfsa7700] MSI RBAC Access to FHIR Service [fhir7700]...

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
 Secure FHIR-SyncAgent Function has successfully been deployed to group [api-fhir-7700] on Mon 15 Nov 2021 09:11:47 PM UTC
 Secure FHIR-SyncAgent Function App URL is: [https://sfsa7700.azurewebsites.net]
 Secure app configuration settings are stored securely in KeyVault: [fhir7700kv]
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


Starting FHIR-SyncAgent Service Bus Namespace and Queue deployment...
Creating Standard Service Bus Namespace [syncagent7700sbns]  This operation can take a while to complete..
Creating [syncagent7700sbns] SyncAgentSharedAccessKey Authorization rule...
Creating [syncagent7700sbns] SyncAgentSharedAccessKey connection string...

Creating [syncagent7700sbns] Queue's...

Creating syncagent7700sbns Queue [cdsupdates]...
Storing cdsupdates connection string in KeyVault fhir7700kv
Storing fhirupdates connection string in [sfsa7700] config

Creating syncagent7700sbns Queue [fhirupdates]...
Storing fhirupdates connection string in KeyVault fhir7700kv
Storing fhirupdates connection string in [sfsa7700] config

Creating syncagent7700sbns Queue [ehrupdatebroker]...
Storing ehrupdatebroker connection string in KeyVault fhir7700kv
Storing fhirupdates connection string in [sfsa7700] config

Creating syncagent7700sbns Queue [fhirbulkloadunordered]...
Storing fhirbulkloadunordered connection string in KeyVault fhir7700kv
Storing fhirbulkloadunordered connection string in [sfsa7700] config

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
 FHIR-SyncAgent Service Bus Namespace and Queue's have been deployed to group [api-fhir-7700] on Mon 15 Nov 2021 09:14:20 PM UTC
 Secure Service Bus Connection settings are stored in KeyVault: [fhir7700kv]
 Service Bus Queue Names are stored in the [sfsa7700] Application Configuration
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

Finishing Deployment and Configuration...
Storing Connection Strings in Secure FHIR-Proxy [sfp7700] Application Configuration...
Setting FHIR-SyncAgent Application Config option to Read Only

************************************************************************************************************
 FHIR-SyncAgent and Service Bus Installation completed without errors
 Run the [SetupSyncAgent.bash] script next to gather and export the new ServiceBus Key needed in Dynamics
************************************************************************************************************

dale@Azure:~/fhir-cds-agent/scripts$
``` 

---

## Deployment Architecture 

![diagram](./media/sync-agent-deployment-diagram.png)
