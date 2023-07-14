""" 
Filter out rows where the abstract does not contain the word ("artificial intelligence" or "intelligence" or "machine learning") and the word ("sustainability" or "sustainable") and the word ("energy" or "energies")
"""
import pandas as pd


def filter_dataframe(df, source):
    """
    Filter out rows where the abstract does not contain the word ("artificial intelligence" or "intelligence" or "machine learning") and the word ("sustainability" or "sustainable") and the word ("energy" or "energies")
    and save the filtered dataframe to a csv file
    and print how many rows were filtered out
    Parameters
    ----------
    df : pandas.DataFrame
        dataframe to filter
    source : str
        source of the dataframe

    Returns
    -------
    filtered_df : pandas.DataFrame
        filtered dataframe
    """

    # filtering out rows
    mask1 = df["abstract"].str.contains(
        "artificial intelligence|intelligence|intelligent agent|machine learning",
        na=False,
        case=False,
    )
    mask2 = df["abstract"].str.contains(
        "sustainability|sustainable", na=False, case=False
    )
    mask3 = df["abstract"].str.contains("energy|energies", na=False, case=False)

    filtered_df = df[mask1 & mask2 & mask3]

    # print how many rows were filtered out
    print(f"Filtered out {len(df) - len(filtered_df)} rows from {source} dataframe")
    print(f"{len(filtered_df)} rows left in {source} dataframe")

    filtered_df.to_csv(f"./data/raw_data/filtered_{source}_data.csv", index=False)

    return filtered_df


def main():
    df = pd.read_csv("./data/raw_data/xplore_0.csv")
    filtered_df = filter_dataframe(df, "xplore_0")


if __name__ == "__main__":
    main()
