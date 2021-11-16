## Sample script execution 

dale@Azure:~/fhir-proxy/scripts$ ./deployfhirproxy.bash <br>
Executing ./deployfhirproxy.bash... <br>
Checking Azure Authentication... <br>
Enter your subscription ID [de91991f-4607-4d0e-80fc-66a33f4e1681]: <br>
 <br>
This script will look for an existing resource group, otherwise a new one will be created <br>
You can create new resource groups with the CLI using: az group create <br>
Enter a resource group name
api-fhir-7700 <br>
If creating a *new* resource group, you need to set a location <br>
You can lookup locations with the CLI using: az account list-locations <br>
Enter resource group location:
westus2 <br>
Enter your deployment prefix - proxy components begin with this prefix [apifhir7700]:
proxy7700 <br>
Enter a keyvault name to store/retreive FHIR Server configuration [proxy7700kv7354]:
fhir7700kv <br>
Checking for keyvault fhir7700kv... <br>
Loading FHIR Server Credential/Connection Information from fhir7700kv... <br>
Enter the proxy function app name[sfp19081]:
sfp7700 <br>
Setting default subscription and checking for resource group... <br>
Using existing resource group... <br>
Starting deployment of... ./deployfhirproxy.bash -i de91991f-4607-4d0e-80fc-66a33f4e1681 -g api-fhir-7700 -l westus2 -p apifhir7700 <br>
Press Enter to continue, or Ctrl+C to exit <br>
Starting Secure FHIR Proxy deployment... <br>
Creating Storage Account [proxy7700store12080]... <br>
Retrieving Storage Account Connection String... <br>
Creating Redis Cache [proxy7700cache9400]... <br>
Creating Redis Connection String... <br>
Creating Secure FHIR Proxy Function App Serviceplan[proxy7700asp]... <br>
Creating Secure FHIR Proxy Function App [sfp7700]... <br>
WARNING: --runtime-version is not supported for --runtime dotnet. Dotnet version is determined by --functions-version. Dotnet version will be 3.1 for this function app. <br>
WARNING: Application Insights "sfp7700" was created for this Function App. You can visit https://portal.azure.com/#resource/subscriptions/de91991f-4607-4d0e-80fc-66a33f4e1681/resourceGroups/api-fhir-7700/providers/microsoft.insights/components/sfp7700/overview to view your Application Insights component <br>
Creating MSI for Function App... <br>
Setting KeyVault Policy to allow secret access... <br>
Configuring Secure FHIR Proxy App [sfp7700]... <br>
Deploying Secure FHIR Proxy Function App from source repo to [sfp7700.azurewebsites.net]... <br>
Creating Service Principal for AAD Auth <br>
WARNING: The output includes credentials that you must protect. Be sure that you do not include these credentials in your code or check the credentials into your source control. <br> For more information, see https://aka.ms/azadsp-cli <br>
WARNING: 'name' property in the output is deprecated and will be removed in the future. Use 'appId' instead. <br>
Storing FHIR Proxy Client Information in Vault... <br>
Adding Sign-in User Read Permission on Graph API... <br>
WARNING: Invoking "az ad app permission grant --id ef4999b2-8376-4f1e-8869-bc1add28cb16 --api 00000002-0000-0000-c000-000000000000" is needed to make the change effective <br>
Configuring reply urls for app... <br>
Adding FHIR Custom Roles to Manifest... <br>
Enabling AAD Authorization and Securing the FHIR Proxy <br>
Starting fhir proxy function app... <br>
 <br>
************************************************************************************************************
Secure FHIR Proxy Platform has successfully been deployed to group api-fhir-7700 on Mon 15 Nov 2021 05:07:44 PM UTC <br>
Please note the following reference information for future use: <br>
Your secure fhir proxy host is: https://sfp7700.azurewebsites.net <br>
Your app configuration settings are stored securely in KeyVault: fhir7700kv <br>
************************************************************************************************************
 <br>
dale@Azure:~/fhir-proxy/scripts$
