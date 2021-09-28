import pandas as pd

data_frame = pd.read_csv("data/survey_results_public.csv")

# data_frame = pd.read_csv("daftarnilai.csv")

print(data_frame.shape)
data_frame.info()

# data_frame_schema = pd.read_csv("data/survey_results_schema.csv")
# print(data_frame_schema)