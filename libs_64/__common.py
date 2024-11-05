# -*- coding: utf-8 -*-
import os
import sys
import ctypes
import platform

# 获取当前系统名称
__system = platform.system()

if __system == "Windows":
    #print("当前系统为Windows")
    def init_env():
        base_dir = os.path.abspath(os.path.dirname(__file__))
        #print('base dir', base_dir)

        # 指定 Windows 动态库查找路径
        syspath = os.path.join(base_dir)
        sys.path.append(syspath)
        #print('sys.path:', sys.path)

        # 指定 Windows Python jkzuc模块查找路径
        env_path = os.path.join(base_dir)
        path_env = os.environ.get('PATH')
        path_env = env_path + ';' + path_env
        os.environ['PATH'] = path_env
        #print('env: {}'.format(os.environ['PATH']))
elif __system == "Linux":
    #print("当前系统为Linux")
    def init_env():
        base_dir = os.path.abspath(os.path.dirname(__file__))

        # 加载 Linux 动态库 libjakaAPI.so
        env_path = os.path.join(base_dir, 'libjakaAPI.so')
        ctypes.CDLL(env_path)

        # 加载 Linux Python jkrc 模块查找路径
        syspath = os.path.join(base_dir)
        sys.path.append(syspath)

        # 设置 LD_LIBRARY_PATH 环境变量
        ld_library_path = os.environ.get('LD_LIBRARY_PATH', '')
        new_ld_library_path = f"{base_dir}:{ld_library_path}"
        os.environ['LD_LIBRARY_PATH'] = new_ld_library_path

        #print('SYS PATH: {}\n {}'.format(sys.path, syspath))
        #print('LD_LIBRARY_PATH: {}'.format(os.environ.get('LD_LIBRARY_PATH')))
else:
    print("未知系统")

if __name__ == '__main__':
    init_env()