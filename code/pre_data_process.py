'''
语料库格式为多个txt，每个txt一段，该文件用于将多个txt合并为一个txt文件
'''
import os
import io

# 设置你的父文件夹路径
parent_folder_paths = ['../corpus/classical', '../corpus/modern']
print(parent_folder_paths)

for parent_folder_path in parent_folder_paths:
    # 遍历父文件夹中的每个子文件夹
    for subdir, dirs, files in os.walk(parent_folder_path):
        print(subdir, dirs, files)
        # # 存储所有txt文件内容的列表
        # txt_contents = []
        # for file in files:
        #     # 检查文件扩展名是否为.txt
        #     if file.endswith('.txt'):
        #         # 构建完整的文件路径
        #         file_path = os.path.join(subdir, file)
        #         # 打开并读取文件内容
        #         with io.open(file_path, 'r', encoding='utf-8') as f:
        #             txt_contents.append(f.read())
        
        # # 如果该子文件夹下有txt文件，则合并它们
        # if txt_contents:
        #     combined_txt_path = os.path.join(subdir, 'combined.txt')
        #     # 写入合并后的内容到新文件
        #     with io.open(combined_txt_path, 'w', encoding='utf-8') as f:
        #         f.write('\n'.join(txt_contents))
        #     print(f'Combined file created at: {combined_txt_path}')