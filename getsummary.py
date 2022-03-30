import pandas as pd
surveys_df = pd.read_csv("surveys.cvs")
weight_summary = surveys_df["weight"].describe()
print(weight_summary)