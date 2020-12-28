from dataclasses import dataclass


@dataclass
class GetDbTableNamesKeys:
    TABLE_NAMES: str = "TableNames"
