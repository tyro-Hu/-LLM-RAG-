import pandas as pd

# 创建一个示例 DataFrame
data = {
    'news_id': [1, 2, 3],
    'title': ['新闻标题1', '新闻标题2', '新闻标题3'],
    'category': ['科技', '体育', '娱乐'],
    'abstract': ['这是第一条新闻的摘要', '这是第二条新闻的摘要', '这是第三条新闻的摘要']
}

df_news_batch = pd.DataFrame(data)

print("原始 DataFrame:")
print(df_news_batch)
print("\n" + "="*50 + "\n")

# 使用 to_dict(orient='records') 转换
batch_payloads = df_news_batch.to_dict(orient='records')

print("转换后的字典列表:")
for i, record in enumerate(batch_payloads):
    print(f"记录 {i+1}: {record}")

print("\n" + "="*50 + "\n")

# 展示其他 orient 参数的效果
print("其他 orient 参数的效果:")
print("\n1. orient='dict' (默认):")
print(df_news_batch.to_dict(orient='dict'))

print("\n2. orient='list':")
print(df_news_batch.to_dict(orient='list'))

print("\n3. orient='index':")
print(df_news_batch.to_dict(orient='index'))

print("\n4. orient='records' (我们使用的):")
print(df_news_batch.to_dict(orient='records')) 