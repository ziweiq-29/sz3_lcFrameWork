import numpy as np

# 读取 quant_inds.dat 文件（每个元素是 int32）
quant_inds = np.fromfile("quant_inds.dat", dtype=np.int32)

# 打印前 20 个元素
print("First 2000 elements in quant_inds.dat:")
print(quant_inds[:20])

# 也可以看看总长度
print(f"Total elements: {len(quant_inds)}")
