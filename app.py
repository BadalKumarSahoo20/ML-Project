# # from mlproject.logger import logging




# # if __name__=="_main_":
# #     logging.info("The execution has started")




# from mlproject.logger import logging
# from mlproject.exception import CustomException
# from mlproject.components.data_ingestion import DataIngestion
# from mlproject.components.data_ingestion import DataIngestionConfog
# import sys





# if __name__ == "__main__":
#     logging.info("The execution has started")
#     print("App ran successfully")
    
#     try:
#         data_ingestion=data_ingestion()
#         data_ingestion.initiate_data_ingestion()
#     except Exception as e:
#         raise CustomException(e,sys)



import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "src"))













from mlproject.logger import logging
from mlproject.exception import CustomException
from mlproject.components.data_ingestion import DataIngestion
import sys


if __name__ == "__main__":

    logging.info("Application started")

    try:
        obj = DataIngestion()
        train_path, test_path = obj.initiate_data_ingestion()

        print("Train file:", train_path)
        print("Test file:", test_path)

    except Exception as e:
        raise CustomException(e, sys)
