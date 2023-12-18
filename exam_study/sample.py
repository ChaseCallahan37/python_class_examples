import re
import pandas as pd


def main():
    df = pd.DataFrame()

    df["word_count"] = df["comment"].apply(get_word_count)

def get_word_count(comment: str):

    if comment == "": return 0

    return len(re.sub("[ ]{2, }", "", comment).strip().split(" "))


main()