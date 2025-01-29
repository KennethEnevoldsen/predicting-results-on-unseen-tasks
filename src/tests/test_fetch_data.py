import pandas as pd

from predicting_unseen_tasks.fetch_data import fetch_mteb_data


def test_fetch_mteb_data():
    df = fetch_mteb_data()  # we could probably skip this test if it is too big
    assert isinstance(df, pd.DataFrame)
