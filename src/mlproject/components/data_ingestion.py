# #Database-->data-->Train Test Split
# import os
# import sys
# from mlproject.exception import CustomException
# from mlproject import logging
# import pandas as pd
# from dataclasses import dataclass
# from mlproject.util import read_sql_data
# from sklearn.model_selection import train_test_split

# @dataclass
# class DataIngestionConfig:
#     train_data_path:str=os.path.join('artifact','train.csv')
#     test_data_path:str=os.path.join('artifact','test.csv')
#     raw_data_path:str=os.path.join('artifact','raw.csv')

# class DataIngestion:
#     def __init__(self):
#         self.ingestion_config=DataIngestionConfig()
        
        
#     def initiate_data_ingestion(self):
#         try:
#             #reading the data from sql
#             df=read_sql_data()
#             logging.info("Reading  completed from mysql Database")
            
#             os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
#             df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
#             train_test,test_test=train_test_split(df,test_size=0.2,random_state=42)
#             df.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
#             df.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            
#             logging.info("Data ingestion is completed ")
        
        
        
#         return(
#             self.ingestion_config.train_data_path
#             self.ingestion_config.test_data_path
#         )
            
            
            
            
            
            
            
            
            
            
#             pass
#         except Exception as e:
#             raise CustomException(e,sys)

























import os
import sys
import pandas as pd
from dataclasses import dataclass
from sklearn.model_selection import train_test_split

from mlproject.exception import CustomException
from mlproject.logger import logging
from mlproject.utils import read_sql_data


@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join("artifact", "train.csv")
    test_data_path: str = os.path.join("artifact", "test.csv")
    raw_data_path: str = os.path.join("artifact", "raw.csv")


class DataIngestion:

    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):

        try:
            logging.info("Data ingestion started")

            df = read_sql_data()

            os.makedirs("artifact", exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path, index=False)

            train_df, test_df = train_test_split(
                df,
                test_size=0.2,
                random_state=42
            )

            train_df.to_csv(self.ingestion_config.train_data_path, index=False)
            test_df.to_csv(self.ingestion_config.test_data_path, index=False)

            logging.info("Data ingestion completed")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            raise CustomException(e, sys)
