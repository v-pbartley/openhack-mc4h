# Deploy and demonstrate authentication capabilities of Azure Healthcare APIs

## Challenge

Your challenge is to deploy the Healthcare API FHIR service and validate that user authentication and role-based access controls are functioning as expected. Additionally, you will deploy and configure the Microsoft OSS FHIR proxy server to demonstrate how that component can enhance the out of the box capabilities that are provided by the Healthcare APIs service.

## Customer requirements

Contoso Healthcare has the following requirements which you should take into consideration:

- Contoso has standardized on Microsoft Azure Active Directory as their primary identity provider.
- Contoso wants a flexible authentication platform that will allow them to engage with patients, providers, payors and researchers.
- Contoso considers social identity providers (Facebook, Twitter) as an experimental solution and wants to explore ways to integrate these IdPs into their solution.
 - Contoso does not want to increase the burden on their solution support team as additional users are on-boarded. Self-service password reset and automated identity management tools are a priority for them.

## Cheat sheet


## Success Criteria

+ Successfully deploy Healthcare APIs and configure role-based access controls. Demonstrate that the authentication and access control methods are functioning correctly.
+ Extend the Healthcare API authentication capabilities using the OSS FHIR proxy software to demonstrate how Contoso might integrate additional identity providers + outside of their primary Azure Active Directory domain.
+ Describe how Azure Active Directory features could be used to reduce efforts associated with common support activities such as password resets.


## References

-[Deploy a FHIR service within Azure Healthcare APIs - using portal](https://docs.microsoft.com/en-us/azure/healthcare-apis/fhir/fhir-portal-quickstart)
- [What is Azure Active Directory authentication?](https://docs.microsoft.com/en-us/azure/active-directory/authentication/overview-authentication)
- [Authentication and authorization in Azure App Service and Azure Functions](https://docs.microsoft.com/en-us/azure/app-service/overview-authentication-authorization)
- [Quickstart: Register an application with the Microsoft identity platform](https://docs.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app)
- [Application and service principal objects in Azure Active Directory](https://docs.microsoft.com/en-us/azure/active-directory/develop/app-objects-and-service-principals)
- [App Registration vs Enterprise Applications](https://docs.microsoft.com/en-us/answers/questions/270680/app-registration-vs-enterprise-applications.html)
- [What is Azure Active Directory B2C?](https://docs.microsoft.com/en-us/azure/active-directory-b2c/overview)
- [What Azure AD features are supported by AAD B2C](https://docs.microsoft.com/en-us/azure/active-directory-b2c/supported-azure-ad-features)
- [Create an Azure Active Directory B2C Tenant](https://docs.microsoft.com/en-us/azure/active-directory-b2c/tutorial-create-tenant)

## Challenge Links

+ [Overview](Readme.md)
+ [Authorization](Challenge-Authorization.md)
+ [Consent](Challenge-Consent.md)