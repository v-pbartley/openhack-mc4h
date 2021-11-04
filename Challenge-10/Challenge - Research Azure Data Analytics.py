# Databricks notebook source
# DBTITLE 1,Challenge - Research Azure Data Analytics
# MAGIC %md 
# MAGIC This challange will walk you through using exported and anonymized data for research analytics.  You will explore the effect of gender and age on patients'recieving the Flu shot or not. The result of your analysis will help shape Sunrise Health's strategy for increasing Flu vaccination rates.
# MAGIC In this lesson we will complete the following tasks
# MAGIC * Read in anonymized FHIR json files
# MAGIC * Flatten the data structure to tabular format
# MAGIC * Produce descriptive statistics on the dataset
# MAGIC * Visualize data elements within the dataset
# MAGIC * Perform an ANOVA test on two data elements

# COMMAND ----------

# DBTITLE 1,Prerequisites
# MAGIC %md
# MAGIC If you have not already completed Challenge - Export and Anonymize Data, work through the data export steps and record the Container Name, Sas Token, Index, and Sas Key for the output container.

# COMMAND ----------

# DBTITLE 1,Package Imports
import pandas as pd
from pyspark.sql.types import ArrayType, StructType
from pyspark.sql.functions import explode_outer, col, arrays_zip
import os
from pyspark.sql.functions import pandas_udf, explode
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as stats

# COMMAND ----------

# DBTITLE 1,Step 1: Configure FHIR data import into Databricks to read in anonymized FHIR json files
#Options for mounting the blob storage account to Azure DataBricks
dbutils.widgets.combobox("Premium", "Y", ["Y", "N"])
dbutils.widgets.combobox("OutputStorageAccount", "<Blob Storage Account>", ["<Blob Storage Account>"])
dbutils.widgets.combobox("InputContainerName", "<Container>", ["<Container>"])
dbutils.widgets.combobox("OutputContainerName", "<Container>", ["<Container>"])
dbutils.widgets.combobox("InputMountPoint", "<MountPoint>", ["<MountPoint>"])
dbutils.widgets.combobox("SasToken", "N/A", ["N/A", "<SAS token>"])
dbutils.widgets.combobox("Index", "N/A", ["N/A","<Index>"])
dbutils.widgets.combobox("SasKey", "N/A", ["N/A","<SasKey>"])
dbutils.widgets.combobox("OutputMountPoint",  "<MountPoint>", [ "<MountPoint>"])
dbutils.widgets.combobox("InputStorageAccount",  "<Blob Storage Account>", [ "<Blob Storage Account>"])

def mount_storage(container, storage, mountpoint):
  '''Take a container name and mount point input and mounts the mountpoint to the storageaccount container'''
  configs = {
    "fs.azure.account.auth.type": "CustomAccessToken",
    "fs.azure.account.custom.token.provider.class":   spark.conf.get("spark.databricks.passthrough.adls.gen2.tokenProviderClassName")
  }
 
  #Only mount storage if it not already mounted
  if not any(mount.mountPoint == mountpoint for mount in dbutils.fs.mounts()):
 
    if dbutils.widgets.get("Premium") == 'Y':
    #Mounting storage when account is Premium  
      dbutils.fs.mount(
        source = "abfss://"+ container + "@" + storage + ".dfs.core.windows.net/",
        mount_point = mountpoint,
        extra_configs = configs)
 
    else:
    #Mounting storage when account is not Premium
      dbutils.fs.mount(
        source = "wasbs://%s@%s.blob.core.windows.net/" % (container, storage),
        mount_point = mountpoint,
        extra_configs = {"fs.azure.sas.%s.%s.blob.core.windows.net" % (container, storage) : "%s" % dbutils.widgets.get("SasKey")})
      
 #Mounting the output blob storage account to Azure DataBricks
mount_storage(dbutils.widgets.get("InputContainerName"), dbutils.widgets.get("InputStorageAccount"), dbutils.widgets.get("InputMountPoint"))
mount_storage(dbutils.widgets.get("OutputContainerName"), dbutils.widgets.get("OutputStorageAccount"), dbutils.widgets.get("OutputMountPoint"))



# COMMAND ----------

# DBTITLE 1,Define tabular dataset conversion
def explode_arrays(dfflat):
  '''Takes a spark dataframe input and explodes the array columns to multiple rows, returns a dataframe'''
  flat_cols = [field.name for field in dfflat.schema.fields if type(field.dataType) != ArrayType]
  cols = [field.name for field in dfflat.schema.fields if type(field.dataType) == ArrayType]
  exploded_df = dfflat.withColumn('vals', explode_outer(arrays_zip(*cols))) \
           .select(*flat_cols,'vals.*') \
           .fillna('', subset=cols)
  return exploded_df

def flatten_structs(nested_df):
  '''Takes a spark dataframe input and flattens the struct columns into multiple columns prefaced with the parent name, returns a dataframe'''
  stack = [((), nested_df)]
  columns = []
  while len(stack) > 0:
      parents, df = stack.pop()
      flat_cols = [col(".".join(parents + (c[0],))).alias("_".join(parents + (c[0],))) for c in df.dtypes if c[1][:6] != "struct"]
      nested_cols = [c[0] for c in df.dtypes if c[1][:6] == "struct" ]
      columns.extend(flat_cols)
      for nested_col in nested_cols:
          projected_df = df.select(nested_col + ".*")
          stack.append((parents + (nested_col,), projected_df))
  return nested_df.select(columns)

# Flatten the struct columns and explode the array columns to fully flatten the dataframe
def flatten_df(dfflat):
  '''Takes a spark data frame input and flattens struct columns into multiple columns and explodes array columns into multiple rows, returns a dataframe'''
  while len([field.name for field in dfflat.schema.fields if type(field.dataType) == StructType or type(field.dataType) == ArrayType ]) !=0 :
    dfflat = flatten_structs(dfflat)
    dfflat = explode_arrays(dfflat)
  
  return dfflat

# COMMAND ----------

# DBTITLE 1,Step 2: Flatten the data structure to tabular format
#Loop through the FHIR source and generate parquet, ddl, or both outputs based on output parameter
#Assumes files are in folders by FHIR resource type. Ex. CareTeam
try:
  dir = dbutils.fs.ls(dbutils.widgets.get("InputMountPoint"))
  dirdf = pd.DataFrame(dir,columns=['path','name','size'])
  
  for x in dirdf.path:
    df = spark.read.json(x)
    dfflat = flatten_df(df)
    tblname = x[len(dbutils.widgets.get("InputMountPoint"))+6:(len(x)-1)]
    dfoutpath = dbutils.widgets.get("OutputMountPoint") + '/' + tblname + '.parquet'
    print(dfoutpath)
    dfflat.write.mode('append').parquet(dfoutpath)   
except:  
  # Unmount if fails
  dbutils.fs.unmount(dbutils.widgets.get("InputMountPoint"))
  dbutils.fs.unmount(dbutils.widgets.get("OutputMountPoint"))
  raise

# COMMAND ----------

# DBTITLE 1,Step 3: Produce descriptive statistics on the dataset
#It's important to understand what data is in your dataset before performing a specific analysis task
#Basic descriptive statistics
analysis_df_1 = spark.read.parquet(<<filepath>>)
analysis_df_1.select('<<column name>>').describe().show()

#To explore the effect of patient demographics like gender and race on immunization rates, you will need to join datasets. Pay attention to any data transformation necessary to join Patient and Immunization data
#Joining datasets
analysis_df_2 = spark.read.parquet(<<filepath>>)
analysis_df_joined = analysis_df_1.join(analysis_df_2, <<id column = id column>>, "left")

#A group by can give a quick picture of a categorical variables effect on a responsive metric. The sample code below will help with a group by but first you will have to create a column to represent Flu vaccination or not
#Group by aggregations
analysis_df_joined.groupBy("<<column name").sum("<<column name>>").show(truncate=False)

# COMMAND ----------

# DBTITLE 1,Step 4: Visualize data elements within the dataset
#Visually exploring a dataset can generate additional hypothesises. There are a couple of sample code visualizations below.
#Histogram
analysis_df_joined.select('<<column name>>').histogram(5)

#Boxplot
plt.boxplot(df2)
plt.show()

#Correlation Matrix
analysis_df_joined.select(<<list of columns>>).corr().style.background_gradient(cmap='coolwarm').set_precision(2)

# COMMAND ----------

# DBTITLE 1,Step 5 : Perform an ANOVA test on two data elements
#A group by can give us a gut check on how a categorical variable effects a response variable. An ANOVA gives us a statistical answer. Sample code below will get you started exploring the effect of gender and age on Flu vaccination rates
stats.f_oneway(analysis_df_joined.select(<<column name>>),analysis_df_joined.select(<<column name>>))

# COMMAND ----------

# DBTITLE 1,Final: Clean Up
  # Unmount storage account
  dbutils.fs.unmount(dbutils.widgets.get("InputMountPoint"))
  dbutils.fs.unmount(dbutils.widgets.get("OutputMountPoint"))
