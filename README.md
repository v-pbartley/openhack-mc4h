# Microsoft Cloud for Healthcare 2021 OpenHack

# Introduction
Hello and welcome to the Microsoft Cloud for Healthcare 2021 OpenHack! This live event will take place in online sessions Wednesday-Friday Nov 10-12, 2021. For information about how to register, please visit ______________. All registered participants will be placed on a team and given instructions for how to log in to the event.


# MC4H 2021 OpenHack Overview
Over the course of three days, you and your teammates will work through a series of guided challenges where you'll test your skills building FHIR data workflows using Microsoft Cloud for Healthcare (MC4H) tools and architectures. You will gain exposure to a complete host of MC4H components and get hands on experience deploying and configuring systems capable of handling production workloads.

The challenges in this OpenHack are designed to give you and your teammates a chance to exercise your health data problem-solving skills in a collaborative environment. To make this a valuable experience for everyone, each team will need to make sure that 

+ All team members can contribute to the team's success
+ Everyone works in areas that provide opportunities to gain new skills (whatever those areas may be for different team members)

In finding solutions to problems together, you and your teammates will help strengthen each other's knowledge. Ideally, you will all get practice in areas that you have less experience in, and in areas where you have more experience, hopefully you will find opportunities to share what you know and bring the team forward.

For each challenge, there will be a Microsoft Health and Life Sciences Cloud and Data engineer present to lead the session and serve as a coach, providing guidance as needed. Your team will be able to ask questions, and the coach in attendance will be available to provide support. Bear in mind, however, that the coach can only point you in the right direction. The rest will be up to you and your teammates. As you progress through the challenges, the tasks will increase in difficulty, and you will need to be self-sufficient with information from publically available documentation.

Overall, the most important thing in this OpenHack is for you and your teammates to have a valuable, productive experience gaining new skills with Microsoft Cloud for Healthcare solutions. We wish you and your team the best of luck in your MC4H 2021 OpenHack journey!


## Microsoft Cloud for Healthcare - Overview
**Microsoft Cloud for Healthcare** is the aggregrate of Microsoft's Health and Life Sciences (HLS) industry solutions, encompassing Azure API for FHIR and its full complement of supporting tools - enabling health data interoperability and integration with Microsoft Dynamics MC4H workstreams.

Azure API for FHIR together with FHIR Proxy (OSS) and the supporting suite of tools enable EHR interoperability, legacy health data format conversion, eventing workflows, IoMT connectivity, bulk FHIR data pipelines for research and ML, SMART on FHIR applications, and more.

Applications built on the Dynamics platform (which include Dynamics model-driven apps) make use of Dataverse and can operate without need of making REST API calls directly to Azure API for FHIR. In addition to running Microsoft Cloud for Healthcare solutions, developers can also take advantage of the Dynamics low-code/no-code environment to construct patient or provider-facing solutions/applications that can tap into healthcare data persisted in Azure API for FHIR.

## Prerequisites

+ Azure Subscription with Contributor/Co-Owner rights 
+ Global Admin in your Azure tenant 
+ Dynamics Environment + MC4H temporary license and solution set 
+ GitHub account 
+ Postman (cloud or desktop) 

## Challenges  
List of challenges at publishing, others will be added over time 
- [Challenge 0](Challenge-0/Readme.md) - Hack Overview

### FHIR Basics 
- [Challenge 1](Challenge-1/Readme.md) - Deploy Azure API for FHIR
- [Challenge 2](Challenge-2/Readme.md) - Convert HL7 to FHIR
- [Challenge 3](Challenge-3/Readme.md) - Ingest to FHIR
- [Challenge 4](Challenge-4/Readme.md) - Query and Search FHIR using Postman 

### Microsoft Cloud for Healthcare 
- FHIR Basics challenges +
- [Challenge 5](Challenge-5/Readme.md) - SyncAgent 
- [Challenge 6](Challenge-6/Readme.md) - Dataverse Entity and Attribute Mapping 
- [Challenge 7](Challenge-7/Readme.md) - Dataverse writing data
- [Challenge 8](Challenge-8/Readme.md) - Debugging, Operations and Maintenance 

### Analytics 
- FHIR Basics challenges +
- [Challenge 9](Challenge-9/Readme.md) - Export and Anonymize Data 
- [Challenge 10](Challenge-10/Readme.md) - Research Azure Data Analytics

### IoMT
- FHIR Basics challenges +
- [Challenge 11](Challenge-11/Readme.md) - IoMT FHIR Connector

### DICOM
- FHIR Basics challenges +
- [Challenge 12](Challenge-12/Readme.md) - DICOM Service   

## Components  
Components used in this OpenHack 

![component deployment](/docs/assets/images/architecture/BigPicture.png)







## Trademarks

This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft 
trademarks or logos is subject to and must follow 
[Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship.
Any use of third-party trademarks or logos are subject to those third-party's policies.
