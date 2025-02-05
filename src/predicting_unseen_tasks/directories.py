from pathlib import Path


def project_root() -> Path:
    return Path(__file__).parent.parent.parent


def get_dir(name: str) -> Path:
    path = project_root() / name
    if not path.exists():
        path.mkdir(parents=True)
    return path


def get_data_dir() -> Path:
    return get_dir("data")


def get_plot_dir() -> Path:
    return get_dir("plots")
