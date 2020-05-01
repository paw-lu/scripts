"""Function to merge in all CSV files in a directory."""
import os
import pathlib
import warnings
from typing import Union

import pandas as pd


def fetch_features(
    directory: Union[str, pathlib.Path], data: pd.DataFrame, merge_column: str
) -> pd.DataFrame:
    """
    Merge in features stored in CSV in a directory.

    Assumes files all have one common column name to merge on, and that
    each file has no duplicate values in that column.

    Parameters
    ----------
    directory : Union[str, pathlib.Path]
        The directory where the feature CSV files are stored.
    data : pd.DataFrame
        The data which the features will be merged into.
    merge_column : str
        The name of the column to merge on. The DataFrame and each file
        must contain this column.

    Returns
    -------
    data_features : pd.DataFrame
        The original data with all features merged in.
    """
    data = data.copy()
    original_number_of_rows = data.shape[0]
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".csv"):
            print(filename)
            feature = pd.read_csv(os.path.join(directory, filename))
            data = data.merge(feature, on=merge_column, how="left")
            if data.shape[0] != original_number_of_rows:
                raise ValueError(
                    "A CSV file in the listed directory has duplicate values for"
                    " the column listed in merge_column"
                )
            if "Unnamed" in data.columns:
                warnings.warn("A column is unnamed")
    return data
