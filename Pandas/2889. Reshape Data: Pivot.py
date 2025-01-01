import pandas as pd


def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    pivoted = pd.pivot_table(
        weather, columns=["city"], values="temperature", index="month"
    )
    return pivoted
