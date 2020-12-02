# -*- coding: utf-8 -*-
""" 
    @author  : dingyaru
    @version : 
    @time    : 2020/10/10 9:20
    @function: 根据标签文件名删除多余图片,划分数据集
"""
import glob
import os
import random
import shutil

orgin_images_path = r'G:\xiamen-project-train-data-3\image'
orgin_labels_path = r'E:\object365\labels\train'
images_path = r'G:\xiamen-project-train-data-3\images'
labels_path = r'G:\xiamen-project-train-data-3\labels'


for labels_file in os.listdir(orgin_labels_path):  # 列出所有标签文件
    images_name = str(labels_file).split('.')[0] + '.jpg'  # 图片名
    orgin_images_ = os.path.join(orgin_images_path, images_name)  # 原始图片的完整路径
    if os.path.exists(orgin_images_):
        orgin_labels_ = os.path.join(orgin_labels_path, labels_file)
        target_labels = os.path.join(labels_path, labels_file)
        target_images_ = os.path.join(images_path, images_name)  # 目标图片的完整路径
        if not os.path.exists(target_images_):
            shutil.move(orgin_images_, target_images_)  # 复制
        if not os.path.exists(target_labels):
            shutil.copyfile(orgin_labels_, target_labels)

# for labels_file in os.listdir(labels_path):  # 列出所有标签文件
#     images_name = str(labels_file).split('.')[0] + '.jpg'  # 图片名
#     # orgin_images_ = glob.glob(os.path.join(orgin_images_path, r'patch*\{}'.format(images_name)))  # 原始图片的完整路径
#     # target_images_ = os.path.join(images_path, images_name)
#     # if os.path.exists(target_images_):  # 有标签有图片
#         # print(os.path.join(orgin_images_path, r'train_0*/{}.jpg'.format(images_name)))
#     target_images_ = os.path.join(images_path, images_name)  # 目标图片的完整路径
#     if not os.path.exists(target_images_):
#         # print(orgin_images_)
#         # print(target_images_)
#         # print(images_name)
#         # shutil.copyfile(orgin_images_[0], target_images_)  # 复制
#         os.remove(os.path.join(labels_path, labels_file))
# def divide_file():
#     model = ['train', 'val']
#     file_num = len([x for x in os.listdir(labels_path)])
#     val_percent = int(file_num * 0.33)  # 划分验证集为305，按照coco数据集比例划分
#     # print(range(file_num))
#     val_ran = random.sample(range(file_num), val_percent)
#     print(val_ran)
#     img_num = 0
#     for label in os.listdir(labels_path):
#         img_num += 1
#         if img_num in val_ran:  # 测试集
#             strs = str(label).split('.')[0]
#             src2 = os.path.join(images_path, '{}.jpg'.format(strs))
#             if os.path.exists(src2):
#                 dst2 = os.path.join(images_path, model[1], '{}.jpg'.format(strs))
#                 shutil.move(src2, dst2)  # images
#                 src1 = os.path.join(labels_path, label)
#                 dst1 = os.path.join(labels_path, model[1], label)
#                 shutil.move(src1, dst1)  # labels
#         else:  # 训练集
#             strs = str(label).split('.')[0]
#             src2 = os.path.join(images_path, '{}.jpg'.format(strs))
#             if os.path.exists(src2):
#                 dst2 = os.path.join(images_path, model[0], '{}.jpg'.format(strs))
#                 shutil.move(src2, dst2)  # images
#                 src1 = os.path.join(labels_path, label)
#                 dst1 = os.path.join(labels_path, model[0], label)
#                 shutil.move(src1, dst1)  # labels
#
#
# if __name__ == '__main__':
#     divide_file()
