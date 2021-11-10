# Deploy and demonstrate the consent capabilities of Azure Healthcare APIs

## Challenge

+ Deploy Secure FHIR Proxy and populate the Healthcare APIs instance with patient data and sample consent resources.
+ Define and demonstrate the methods that Contoso will use to obtain user consent and how to expose scopes that will be used to control access to data stored in a Healthcare API FHIR service instance.
+ Demonstrate that Secure FHIR proxy successfully implements the defined consent opt-out feature.
+ Describe techniques and methods that may be used to extend and enhance the default opt-out capability provided by the Secure FHIR proxy.

## Customer requirements

+ There are multiple levels of consent the Contoso is interested in. The first area is in the context of applications that are used to access healthcare data. Are applications trusted and are users aware of the data that applications will access and store or otherwise process.
+ The second level of consent relates to how protected health information is accessed and subsequently used. Secure FHIR proxy provides some capabilities to enable enforcement of user data in the context of FHIR consent resources.
+ Provide support for internally and externally develop SMART on FHIR applications.

## Cheat sheet


## Success Criteria

+ Successfully deploy Healthcare APIs and configure Secure FHIR proxy to implement consent filtering.
+ Define and describe methods or techniques that Contoso could implement to extend the consent capabilities of the Secure FHIR Proxy
+ Successfully configure a SMART on FHIR application in Azure Active Directory

## References

- [Secure FHIR Proxy](https://github.com/microsoft/fhir-proxy)
- [Configuring Secure Proxy Consent](https://github.com/microsoft/fhir-proxy/blob/main/docs/configuration.md)
- [Permissions and consent in the Microsoft identity platform](https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-permissions-and-consent)
+ [FHIR Consent Resource](https://www.hl7.org/fhir/consent.html#:~:text=The%20Consent%20resource%20on%20FHIR%20provides%20support%20for,structures%20with%20optional%20attached%2C%20or%20referenced%20unstructured%20representations.%29)

## Challenge Links

+ [Overview](Readme.md)
+ [Authentication](Challenge-Authentication.md)
+ [Authorization](Challenge-Authorization.md)
