'''
语料库格式为多个txt，每个txt一段，该文件用于将多个txt合并为一个txt文件
'''
import os
import io
import Translate


def combine_subdir_text(save_path, parent_folder_paths):
    for parent_folder_path in parent_folder_paths:
        # 遍历父文件夹中的每个子文件夹
        for subdir, dirs, files in os.walk(parent_folder_path):
            # 存储所有txt文件内容的列表
            txt_contents = []
            for file in files:
                # 检查文件扩展名是否为.txt
                if file.endswith('.txt'):
                    # 构建完整的文件路径
                    file_path = os.path.join(subdir, file)
                    # 打开并读取文件内容
                    with io.open(file_path, 'r', encoding='utf-8') as f:
                        txt_contents.append(f.read())
            
            # 如果该子文件夹下有txt文件，则合并它们
            if txt_contents:
                combined_txt_path = os.path.join(save_path, '%s.txt' % subdir.split('/')[-1])
                # 写入合并后的内容到新文件
                with io.open(combined_txt_path, 'w', encoding='utf-8') as f:
                    f.write('\n'.join(txt_contents))
                print(f'Combined file created at: {combined_txt_path}')
    
    pass


def combine_dir_text(dir_path, combined_file_name):
    # 设置合并后的文件名
    combined_file_path = os.path.join(dir_path, combined_file_name)

    # 获取文件夹内所有txt文件
    txt_files = [f for f in os.listdir(dir_path) if f.endswith('.txt') and f != combined_file_name]

    # 合并txt文件
    with open(combined_file_path, 'w', encoding='utf-8') as outfile:
        for fname in txt_files:
            with open(os.path.join(dir_path, fname), 'r', encoding='utf-8') as infile:
                outfile.write(infile.read() + '\n')  # 添加换行符以分隔不同文件的内容

    print(f'All .txt files have been combined into {combined_file_path}')            

    pass


def trainset_translate(trainset_path):
    translatedTexts = []
    for line in open(trainset_path, encoding='utf-8'):
        label, text = line.rstrip('\n').split('\t')
        translatedText = Translate.translate(text, 'bo')
        translatedTexts.append(label + '\t' + translatedText)

    with io.open(trainset_path.rstrip('.txt') + '_bo.txt', 'w', encoding='utf-8') as f:
            f.write('\n'.join(translatedTexts))
    pass

if __name__ == '__main__':
    # # 设置你的父文件夹路径(此处运行时工作路径在项目文件夹，而不在代码所在目录)
    # parentFolderPaths = ['corpus/classical/', 'corpus/modern/']
    # savePath = 'corpus/'
    # combinedFileName = 'corpus.txt'
    # combine_subdir_text(savePath, parentFolderPaths)
    # combine_dir_text(savePath, combinedFileName)

    trainset_translate('corpus/sst2_train_500_zh.txt')