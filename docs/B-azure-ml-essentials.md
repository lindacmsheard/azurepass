# Azure Machine Learning essentials

On this page, we will ensure you are set up to 
- [Work interactively](#a-interactive-access-via-portal) on an Azure Machine Learning VM (for example with notebooks)
- Explore [job submission](#b-job-submission-to-an-azure-ml-compute-target) to an Azure ML remote compute target, to learn about concepts such as pipelines and components

## Pre-requisites
Once per team:
- Work through the [Azure Pass Orientation](A-azure-pass-orientation.md) to set up the tenant and subscription for your team. 
- Follow the instructions linked there in the next steps section to provision an Azure Machine Learning workspace


## A. Interactive access via portal

#### 1. Navigate to https://ml.azure.com and verify that you can see your team's workspace.


#### 2. Subject to available quota, create a compute instance 
This is for interactive use of a single team member or pair programming team. 

> :warning: the default quota for CPU VM cores is 6 per region, allowing for three 2-core machines or one 4-core machine

[MSLearn: Create a compute instance](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-create-compute-instance?view=azureml-api-2&tabs=azure-studio)

> :bulb: if your team needs more machines during the hack, you could create another workspace in a different region, or speak to proctors about raising a quota increase request - these can usually be serviced within the same day.

#### 3.  Review the sample notebooks
[MSLearn: Learn from sample notebooks](https://learn.microsoft.com/en-us/azure/machine-learning/quickstart-create-resources?view=azureml-api-2#learn-from-sample-notebooks)


### Useful links for interactive work:
- [What is an Azure Machine Learning Compute instance](https://learn.microsoft.com/en-us/azure/machine-learning/concept-compute-instance?view=azureml-api-2) *- includes guidance on managing tools, packages and kernels (conda environments)*


## B. Job submission to an Azure ML Compute target
While there is also a [python SDK](https://learn.microsoft.com/en-us/azure/machine-learning/concept-v2?view=azureml-api-2#azure-machine-learning-python-sdk-v2), we will illustrate the concept of job submission using the Azure CLI.


[TODO] - link to azure cli setup - decide on whether to use CI or cloud shell

### Useful links for working with remote compute targets
- [What are compute targets in Azure Machine Learning](https://learn.microsoft.com/en-us/azure/machine-learning/concept-compute-target?view=azureml-api-2)



# Further Reading
- [About Azure ML compute targets](https://learn.microsoft.com/en-gb/azure/machine-learning/concept-compute-target?view=azureml-api-2)