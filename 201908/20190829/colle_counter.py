colours = (
    ('Yasoob', 'Yellow'),
    ('Ali', 'Blue'),
    ('Arham', 'Green'),
    ('Ali', 'Black'),
    ('Yasoob', 'Red'),
    ('Ahmed', 'Silver'),
)
# Counter
from collections import Counter
fav = Counter(name for name,color in colours)
print(fav)
# 统计文件行数
with open("__init__.py","rb") as f:
    line_count = Counter(f)
print(line_count)