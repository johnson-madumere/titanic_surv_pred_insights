from pathlib import Path

import pandas as pd
from loguru import logger
from tqdm import tqdm
import typer

from titanic_surv.config import PROCESSED_DATA_DIR, RAW_DATA_DIR

app = typer.Typer()

def load_data(filename=None):
    # logger.info("Starting dataset processing")

    if not filename:
        filename = "titanic.csv"

    input_path = RAW_DATA_DIR / filename
    # logger.info(f"Loading data from {input_path}")

    return pd.read_csv(input_path)


def save_processed_data(df, filename=None):
    # logger.info("Saving processed Titanic dataset")

    if not filename:
        filename = "titanic_processed.csv"

    output_path = PROCESSED_DATA_DIR / filename
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)

    logger.success(f"Processed data saved to {output_path}")
    return output_path

def load_processed_data(filename):
    # logger.info("Starting dataset processing")

    if not filename:
        return "File name must be provided to load processed data."

    input_path = PROCESSED_DATA_DIR / filename

    return pd.read_csv(input_path)
