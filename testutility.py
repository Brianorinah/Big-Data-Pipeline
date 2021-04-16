import logging
import os
import subprocess
import pandas as pd
import datetime
import gc
import re
import yaml

###function to read the yaml file
def read_conf(filepath):
    with open(filepath , "r") as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            logging.error(exc)

###function to validate the column names
def field_validation(df,conf):
    ###convert all column names in the dataframe to lower case    
    df.columns = [x.lower() for x in df.columns]
    ### convert all column names in the config file to lower case
    conf_columns =[x.lower() for x in conf["columns"]]
    
    ### Remove all white spaces and replace them with underscores
    for col in df.columns:
        if " " in col:
            df = df.rename(columns={col:col.replace(" ","_")})
    ### removing all the underscore for comparison purposes
    df.columns = [x.strip("_") for x in df.columns]
    conf_columns = [x.strip("_") for x in conf["columns"]]
    
    ###comparing the two column names
    if list(df.columns) == list(conf_columns):
        return 1
    else:
        missing_columns =list(set(df.columns).difference(conf_columns))
        print("The following columns are not in the yaml file", missing_columns)
        missing_yaml_file =list(set(conf_columns).difference(df.columns))
        print("The following columns are not in the uploaded file", missing_yaml_file)
        return 0
        
        
                      
