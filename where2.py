# -*- coding: utf-8 -*-

import os
import sys

def has_not_extension(path):
    ''' 拡張子の有無 = `.` の有無、だと思う(たぶん) '''
    return path.find('.')==-1

PATH    = os.environ['PATH'].split(';')
PATHEXT = os.environ['PATHEXT'].split(';')

if len(sys.argv)<=1:
    print('<where2 コマンドのヘルプを出す>')
    exit(0)
filename_you_want_to_open = sys.argv[1]

fullpath_you_want_to_open = None
found_fullpaths = []

# カレントディレクトリからの相対アクセス分.
PATH.insert(0, os.getcwd())

for a_folderpath in PATH:
    fullpath_candidate = os.path.join(a_folderpath, filename_you_want_to_open)

    # 入力ファイル名に拡張子が無い場合は PATHEXT で補っていく.
    if has_not_extension(fullpath_candidate):

        # 拡張子が無いそのパス自体も有効なパスかもしれない.
        # 例: C:\Program Files\Git\usr\bin\notepad
        #     Git for Windows が用意してるメモ帳のラッパー？
        fullpath_candidate_without_ext = fullpath_candidate
        if os.path.exists(fullpath_candidate_without_ext):
            fullpath_you_want_to_open = fullpath_candidate_without_ext
            found_fullpaths.append(fullpath_you_want_to_open)
            continue

        for a_ext in PATHEXT:
            fullpath_candidate_real = '{:}{:}'.format(fullpath_candidate, a_ext)
            if os.path.exists(fullpath_candidate_real):
                fullpath_you_want_to_open = fullpath_candidate_real
                found_fullpaths.append(fullpath_you_want_to_open)
        continue

    if os.path.exists(fullpath_candidate):
        fullpath_you_want_to_open = fullpath_candidate
        found_fullpaths.append(fullpath_you_want_to_open)
        continue

if fullpath_you_want_to_open==None:
    print('情報: 与えられたパターンのファイルが見つかりませんでした。')
    exit(1)

for fullpath in found_fullpaths:
    fullpath_for_display = fullpath.lower()
    print(fullpath_for_display)
