from datasets import load_dataset

dataset = load_dataset("code_search_net", "python")
df = dataset['train'].to_pandas()

df_slice = df[:10000]
df_slice['func_documentation_string'] = df_slice['func_documentation_string'].str.replace(r'\n', ' ', regex=True)
print(df_slice.iloc[0:10])
with open('../resources/data_raw.txt', 'w') as f:
    f.write(df_slice['func_documentation_string'].str.cat(sep='\n'))

text_file = open("resources/data_raw.txt", "r")
lines = text_file.readlines()
for line in lines:
    print(" ".join(line.split()))
