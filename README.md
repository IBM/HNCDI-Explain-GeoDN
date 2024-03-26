<!--
 Copyright (c) 2024 International Business Machines
 
 This software is released under the MIT License.
 https://opensource.org/licenses/MIT
-->

# Geospatial Data and Modeling - HNCDI Explain Course

These Jupyter Notebooks are part of the [Hartree National Centre for Digital Innovation (HNCDI) Explain](https://www.hartree.stfc.ac.uk/digital-innovation/hartree-national-centre-for-digital-innovation/explain/) course on Geospatial Data and Modeling.

In this repository, a series of notebooks have been developed to guide users through the GeoDN modeling and data discovery capabilities. A video series accompanies this course material.

This repository is a place to explore the capabilities of GeoDN, to suggest new features and raise bugs or issues. See the [contributing](./CONTRIBUTING.md) section for more details. 

To sign up to the Geospatial Data and Modeling Explain course, please visit the [Hartree Centre Training Portal](https://hartreetraining.stfc.ac.uk/moodle/local/hartree/index.php).

## Course Overview

The course is split in to two sections, *A Practical Guide to Geospatial Data* and *Fundamentals of Geospatial Data and Modeling*. Fundamentals of Geospatial Data and Modeling includes two parts, *Part 1 - Geospatial Data Discovery for Climate Risk
requirements* and *Part 2 - Geospatial Foundation Models and Workflows*.

The course will be launched in January 2024 and will be hosted on STFC's Learning Management service. As part of the course, users will be given access to the GeoDN platform via Open Data Hub where these notebooks will be available to run. 

### Practical Guide to Geospatial Data
<u>**Course description:**</u>

In this course you will be shown how to use mass geospatial data for model for predicting trends in business operations or planning. Starting with the challenges experienced with today’s solutions, we will explore the consequences of these existing technical limitations with a focus on flood events in the UK. Floods are the costliest natural hazard in the UK, with the winter storm season of 2022 causing £500 million in insurance damages. A new solution is needed to effectively manage the risk of flood impact and other climate related challenges. 

You will get the opportunity to explore geospatial data using a case-study example to walk through the Geospatial Discovery Network (GeoDN). Next you will browse the geospatial data catalogue and query some of the data available on the platform. You will also be introduced to the lab environment, during which you will have the chance to experience the programming interface of GeoDN using the SDK. You will set up your environment, include your credentials and then connect to GeoDN. Once connected you will practice exploring and querying datasets. To conclude this section of the course, you will be shown an example of running a modelling workflow, ready to implement yourself in the following course. 

<u>**Learning objectives:**</u>

- Understand the challenges with today’s geospatial analytics tools and technologies 
- Explore the consequences of these current limitations 
- An overview and introduction of an example toolkit 
- Explore geospatial data with GeoDN 
- Browse the GeoDN data catalogue 
- Set up and be introduced to the Lab environment 
- Configure credentials and connect to GeoDN using the SDK 
= Browse and query the data catalogue using the Lab 

<u>**Course content:**</u>
1. [Data exploration using GeoDN](./Practical_Guide/1.%20Data%20exploration%20using%20GeoDN.ipynb)
2. [Running a workflow with GeoDN](./Practical_Guide/2.%20Running%20a%20Workflow.ipynb)

<u>**Requirements:**</u>
- Prior knowledge of python. 
- Basic understanding of jupyter notebook, perhaps undertake an introduction to jupyter notebooks course. 
- Optional to complete Beginner's Guide to Geospatial Data course.

<u>**Target audience:**</u>

Data analysts and data scientists, business analysts and risk analysts who want to build models to leverage geospatial data (e.g. weather, climate, satellite data), and potentially combine with their own datasets (for example about location of property or infrastructure). Target domains include supply chain, asset management, insurance, or climate risk.



### Fundamentals of Geospatial Data and Modeling 
<u>**Course description:**</u>

In this course you will first be given an introduction to climate datasets and climate risk assessment, before being led through a series of examples, all related to post-event analysis of an extreme weather event (in this case flooding).  

Following an introduction to climate data science and risk assessment, you will begin the first interactive session, where you will query and explore the datasets used in subsequent parts using the example toolkit, GeoDN. You will use Jupyter notebooks to carry out in-depth analysis of flood risk. You will learn how to calculate anomalies to find unusually high rainfall events using python, and also how to intersect raster and vector datasets to identify properties at risk programmatically. 

In the second part, you will learn about impact functions, which connect the severity of a climate hazard (in this case, flood depth), to the proportion of a building expected to be damaged. You will create and deploy a GeoDN workflow to combine flood risk with impact functions and building locations and categories and complete a full climate risk calculation.  

 In the final part of the course, you will be shown how to train, then develop and onboard an AI model. This will give you the building blocks to be able to use AI modelling at scale. 

<u>**Learning objectives:**</u>

- Learn which weather, climate and related datasets are needed for climate risk assessment, and the challenges of working with these datasets 
- Learn how hazard, exposure and vulnerability are combined in a climate risk calculation 
- Discover and explore datasets relevant to flood risk via interactive querying and visualization 
- Learn how to upload local data and combine with large raster datasets 
- Learn how geospatial discovery operations can be used to efficiently find interesting events in a dataset 
- Combine raster and vector data to locate buildings at risk 
- Create an impact function describing the relationship between flood severity and damage 
- Create and run a hazard to impact workflow 
- Use the workflow to calculate the damage exposure of a set of buildings. 

<u>**Course content:**</u>

Part 1: Geospatial Data Discovery for Climate Risk
1. [Query Analyse Rainfall](./Fundamentals/Part_1/1.%20Query%20Analyse%20Rainfall.ipynb)
2. [Flood model and real flood extent with buildings](./Fundamentals/Part_1/2.%20Intersect%20Building%20Flood.ipynb)
3. [Impact Functions with OpenStreetMaps and Flood Outlines](./Fundamentals/Part_1/3.%20Impact%20Function.ipynb)

Part 2: Geospatial Foundation Models and Workflows
1. [Burn scar fine-tuning](./Fundamentals/Part_2/1.%20Fine%20Tuning.ipynb)
2. [Workflow development/testing and sharing](./Fundamentals/Part_2/2.%20Model%20Onboarding.ipynb)
3. [Running a workflow from the catalogue](./Fundamentals/Part_2/3.%20Running%20Models%20from%20Catalogue.ipynb)

<u>**Requirements:**</u>
- Practical Guide to Geospatial Data. 
- Experience with Python. 
- Previous geospatial data science experience is not necessary.

<u>**Target Audience:**</u>

Data analysts and data scientists, business analysts and risk analysts who want to build models to leverage geospatial data (e.g. weather, climate, satellite data), and potentially combine with their own datasets (for example about location of property or infrastructure). Target domains include supply chain, asset management, insurance, or climate risk.





## Contributors

Blair Edwards, Anne Jones, Katerina Reusch, Paolo Fraccaro, Rosie Lickorish, Junaid Butt & Geoffrey Dawson.
