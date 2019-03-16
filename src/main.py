import os
import sys
import re
import glob


def main():
    # 全ての画像をロード
    files = glob.glob('/data/*')
    images = []
    for f in files:
        if re.search('.+.(jpg|png)', f):
            images += [f]
    print(images)

    # 画像を結合

    # 保存

if __name__ == '__main__':
    main()