from datasets import load_dataset

dataset = load_dataset("code_search_net", "python")
df = dataset['train'].to_pandas()

df_slice = df[:2000]
df_slice['func_documentation_string'] = df['func_documentation_string'].apply(lambda x: ' '.join(x.replace('\n', ' ').split()))

with open('resources/data.txt', 'w') as f:
    f.write(df_slice['func_documentation_string'].str.cat(sep='\n'))
