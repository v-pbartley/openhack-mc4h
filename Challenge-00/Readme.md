# Challenge-00 - Welcome!

## Introduction 
In this preliminary challenge, you will be checking your Azure subscription and other parts of your environment to make sure that you can deploy the Microsoft Health and Life Sciences (HLS) components used in this OpenHack. Please make certain that everything is in place before proceeding to Challenge-01.

## Background 
The MC4H OpenHack presents a series of challenges to help learners build skills in deploying and configuring [Azure API for FHIR](https://docs.microsoft.com/en-us/azure/healthcare-apis/azure-api-for-fhir/overview), [FHIR-Proxy](https://github.com/microsoft/fhir-proxy), [Dynamics/Dataverse MC4H solutions](https://docs.microsoft.com/en-us/industry/healthcare/overview), and supporting tools. After completing the MC4H OpenHack, learners will be able to set up the system architectures featured on __[Microsoft Health Architectures](https://microsoft.github.io/health-architectures/)__.
 
## Learning Objectives for Challenge-00
+ Understand the learner goals of the MC4H OpenHack
+ Understand the prerequisites for the MC4H OpenHack

## What are the general learner goals of the MC4H OpenHack?
In general, we want learners to walk away from this hack with a sense of confidence in deploying, configuring, and implementing Microsoft health data solutions.

+ In deploying complex health data systems, problems will inevitably arise and need to be debugged. To help learners develop autonomy in resolving issues, the tasks in this hack require learners to locate information in technical documentation and resolve issues independently.

+ Going through all of the challenges will leave learners with a strong concept of how the various system components fit together. With this knowledge, learners will be ready to take the next step and apply the components in real-world health data use cases.  

## Prerequisite Knowledge for the MC4H OpenHack

+ Participants in the MC4H OpenHack are expected to have a solid foundation in Azure fundamentals. If you are new to Microsoft Azure, please visit [here](https://docs.microsoft.com/en-us/learn/paths/az-900-describe-cloud-concepts/) to learn more about the platform.

+ Since this OpenHack is intended for healthcare IT professionals, we assume learners have a basic familiarity with general topics related to health data interoperability. In particular, learners are expected to have a working knowledge of the FHIR R4 data standard. Please visit [here](https://hl7.org/fhir/R4/) for more information about the FHIR R4 specification.

+ In Challenges 05-08, we cover MC4H architectures based on Microsoft Dynamics/Dataverse healthcare industry solutions. Because most participants do not have access to a Dynamics/Dataverse environment, Challenges 05-08 are presented as instructor-lead training modules. A basic knowledge of the Dynamics/Dataverse landscape will be helpful to get the most out of this portion of the training. Please visit [here](https://powerplatform.microsoft.com/en-us/dataverse/) to learn more about the Dynamics/Dataverse platform.

+ For testing Azure API for FHIR, we will be using the [Postman](https://www.postman.com/api-platform/api-testing/) API testing application. We assume learners have some experience making REST API calls in Postman or in a similar type of utility.

## Environment Prerequisites
Please be sure to have the following ready in your environment before proceeding to Challenge-01.

+ Azure Subscription with [Contributor/Co-Owner rights](https://docs.microsoft.com/en-us/azure/role-based-access-control/built-in-roles)
+ [Application Administrator](https://docs.microsoft.com/en-us/azure/active-directory/roles/permissions-reference#all-roles) role in your [Azure Active Directory (AAD) tenant](https://docs.microsoft.com/en-us/azure/active-directory/fundamentals/active-directory-whatis#:~:text=Azure%20tenant,tenant%20represents%20a%20single%20organization.)
+ GitHub account [link](https://github.com/)
+ Postman (cloud or desktop) installed [link](https://www.postman.com/)

_Note_ Free Postman cloud accounts require a login via email or a Google account. Additionally, Postman recommends that if you choose to use the web client, you should also download the desktop application. You can [read more](https://www.postman.com/downloads/?utm_source=postman-home) and download the web desktop client [here](https://www.postman.com/downloads/?utm_source=postman-home).

## Optional Components (for Challenges 5-8)
+ Dynamics/Dataverse Environment + MC4H temporary license and solution set

Information about obtaining a Dynamics/Dataverse trial license can be found [here](https://docs.microsoft.com/en-us/power-platform/admin/trial-environments).


