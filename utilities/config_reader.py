import yaml
from pathlib import Path

def read_config():

    base_dir = Path(__file__).resolve().parent.parent
    config_path = base_dir / "configs" / "config.yaml"

    print("\n CONFIG PATH USED:", config_path.resolve())

    with open(config_path, "r") as file:
        data = yaml.safe_load(file)

    print("RAW CONFIG LOADED:", data)

    return data