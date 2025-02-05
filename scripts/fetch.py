from predicting_unseen_tasks.fetch_data import fetch_mteb_data


if __name__ == "__main__":
    df = fetch_mteb_data()
    print(df.head())
