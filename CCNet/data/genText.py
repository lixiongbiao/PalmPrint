import os
import numpy as np

path_train = ['/root/autodl-tmp/TongJi/ROI/session1', '/root/autodl-tmp/MPD_ROI']
path_test = ['/root/autodl-tmp/TongJi/ROI/session2']

root = './'


def genID_Tongji(filename):
    userID = int(filename[:5])
    userID = int((userID - 1) / 10)
    return userID


def genID_MPD(filename):
    userID = int(filename[:3]) - 1
    userID = userID * 2 + 1 if 'l' in filename else userID * 2 + 2
    return userID


with open(os.path.join(root, 'train_Tongji_MPD.txt'), 'w') as ofs:
    id_count = 0
    for path in path_train:
        if 'TongJi' in path:
            files = os.listdir(path)
            files.sort()
            for filename in files:
                imagePath = os.path.join(path, filename)
                userID = genID_Tongji(filename)
                ofs.write('%s %d\n' % (imagePath, id_count + userID))
            id_count += userID
        elif 'MPD' in path:
            files = os.listdir(path)
            files.sort()
            for filename in files:
                userID = genID_MPD(filename)
                imagePath = os.path.join(path, filename)
                ofs.write('%s %d\n' % (imagePath, id_count + userID))
            id_count += userID

with open(os.path.join(root, 'test_Tongji_MPD.txt'), 'w') as ofs:
    id_count = 0
    for path in path_test:
        if 'TongJi' in path:
            files = os.listdir(path)
            files.sort()
            for filename in files:
                imagePath = os.path.join(path, filename)
                userID = genID_Tongji(filename)
                ofs.write('%s %d\n' % (imagePath, id_count + userID))
            id_count += userID
        elif 'MPD' in path:
            files = os.listdir(path)
            files.sort()
            for filename in files:
                userID = genID_MPD(filename)
                imagePath = os.path.join(path, filename)
                ofs.write('%s %d\n' % (imagePath, id_count + userID))
            id_count += userID
