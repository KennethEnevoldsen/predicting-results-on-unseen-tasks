import logging
from pathlib import Path

import mteb
import pandas as pd

logger = logging.getLogger(__name__)
default_data_path = Path(__file__).parent.parent.parent / "data"


def fetch_mteb_data(
    path: Path = default_data_path, redownload: bool = False
) -> pd.DataFrame:
    """Fetch the data required for the MTEB project."""
    path = default_data_path
    path.mkdir(exist_ok=True)

    save_path = path / "mteb_data.parquet"

    if not redownload and save_path.exists():
        logger.info("Data already downloaded, skipping.")
        # return pd.read_csv(save_path)
        return pd.read_parquet(save_path)

    logger.info("Fetching MTEB data, this might take a while...")

    results = mteb.load_results()

    results = results.join_revisions()  # only keep one revision of each model
    results = results.filter_models()  # remove models without annotated metadata

    logger.info("Converting mteb results to a pandas DataFrame")
    rows = []
    for model_res in results.model_results:
        for task_res in model_res.task_results:
            task = mteb.get_task(task_res.task_name)
            for split in task_res.scores:
                for hf_subset in task_res.scores[split]:
                    # model, revision, task, task type, subset, split, languages, domains, performance (main metric), metric_name
                    row = {
                        "model_name": model_res.model_name,
                        "revision": model_res.model_revision,
                        "task": task_res.task_name,
                        "subset": hf_subset[
                            "hf_subset"
                        ],  # This corresponds to dataets.load_dataset(dataset_name, subset, split="test"), e.g. load_dataset("glue", "mrpc", split="test")
                        "split": split,
                        "task_type": task_res.task_type,
                        "languages": hf_subset["languages"],
                        "domains": task.metadata.domains,  # in some cases this is not annotated
                        "performance": hf_subset["main_score"],
                        "main_score_name": task.metadata.main_score,
                    }

                    rows.append(row)

    df = pd.DataFrame(rows)

    logger.info(f"Saving data to {save_path}")
    df.to_parquet(save_path)

    return df
