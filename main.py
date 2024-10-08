from TextSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from TextSummarizer.logging import logger
STAGE_NAME="data ingestion stage"

try:
    logger.info(f"Starting {STAGE_NAME}")
    pipeline = DataIngestionTrainingPipeline()
    pipeline.main()
    logger.info(f"{STAGE_NAME} completed successfully")

except Exception as e:
    logger.exception(e)
    raise e