import os
import urllib.request as request
import zipfile
import requests
import shutil
from TextSummarizer.logging import logger
from TextSummarizer.utils.common import get_size
from pathlib import Path
from TextSummarizer.entity import DataIngestionConfig


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config


    
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            response = requests.get(self.config.source_URL, stream=True)
            response.raise_for_status()  # Check for HTTP errors

            if 'Content-Disposition' in response.headers:
                filename = response.headers['Content-Disposition'].split('filename=')[-1].strip('"')
                logger.info(f"Downloading file as: {filename}")
            else:
                filename = self.config.local_data_file  # Use the configured filename

            with open(filename, "wb") as f:
             shutil.copyfileobj(response.raw, f)
            filename = self.config.local_data_file
            headers= self.config.source_URL
            # filename, headers = request.urlretrieve(
            #     url = self.config.source_URL,
            #     filename = self.config.local_data_file
            # )
            logger.info(f"{filename} download! with following info: \n{headers}")
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")  

        
    
    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)