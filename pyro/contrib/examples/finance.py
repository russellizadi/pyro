# Copyright Contributors to the Pyro project.
# SPDX-License-Identifier: Apache-2.0

import os
import urllib

import pandas as pd

from pyro.contrib.examples.util import get_data_directory

DATA = get_data_directory(__file__)

# https://finance.yahoo.com/quote/%5EGSPC/history/
CACHE_URL = "https://fritzo.org/media/snp500.csv.bz2"


def load_snp500():
    """
    Loads pandas dataframe of S&P 500 daily values from 1927-12-30 thru 2020-01-10.
    """
    filename = os.path.join(DATA, "snp500.csv.bz2")
    if not os.path.exists(filename):
        urllib.request.urlretrieve(CACHE_URL, filename)
    df = pd.read_csv(filename)
    return df
