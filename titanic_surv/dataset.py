from pathlib import Path

import pandas as pd
from loguru import logger
from tqdm import tqdm
import typer

from titanic_surv.config import PROCESSED_DATA_DIR, RAW_DATA_DIR

app = typer.Typer()

# def load_data(input_path: Path = RAW_DATA_DIR / "titanic.csv") -> pd.DataFrame:
#     # Load raw Titanic dataset.
#     logger.info(f"Loading data from {input_path}")
#     return pd.read_csv(input_path)
def load_data():
    input_path = RAW_DATA_DIR / "titanic.csv"
    return pd.read_csv(input_path)


@app.command()
def main(
    input_path: Path = RAW_DATA_DIR / "titanic.csv",
    output_path: Path = PROCESSED_DATA_DIR / "titanic_processed.csv",
):
    # Load, inspect, and save the Titanic dataset.
    logger.info("Starting dataset processing")

    # Load data
    df = load_data(input_path)

    logger.info(f"Dataset shape: {df.shape}")
    logger.info(f"Columns: {list(df.columns)}")

    # (Optional placeholder for future processing)
    for _ in tqdm(range(1), desc="Processing"):
        pass

    # Save processed dataset
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)

    logger.success(f"Processed dataset saved to {output_path}")

if __name__ == "__main__":
    app()
