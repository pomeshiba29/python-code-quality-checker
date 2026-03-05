import pandas as pd
import datetime

def make_report():
    #レポート作成
    today = datetime.date.today()
    df = pd.DataFrame({"price": [100, 200], "qty": [2,3]})
    df["total"] = df["price"] * df["qty"]
    total = df["total"].sum()
    print(str(today) + " total=" + str(total))


if __name__ == "__main__":
    make_report()
