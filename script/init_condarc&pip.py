# -*- coding: UTF-8 -*-
r"""
@time : 2022/6/27 14:02
@Author : tz
@File : init_condarc&pip.py
@Description : 配置环境源conda使用mirrors.bfsu.edu.cn源，而pip使用mirrors.aliyun.com源

在windows中,condarc默认位置是在~/.condarc中(C:\Users\用户名\.condarc),pip在~/pip/pip.ini

在Linux系统中，在~/.conda中(/home/username/)，默认是不存在的，使用conda config命令会生成
            ，而pip在~/.pip/pip.conf，默认是不存在的，需要手动创建
"""
import os


def init_pip(mirror_url: str = "mirrors.aliyun.com") -> None:
    """
    初始化pip.ini
    :param mirror_url:镜像源url
    :return:
    """

    # 说明，如果是linux系统中，pip需要设置为~/.pip/pip.conf
    # pip_ini = os.path.expanduser('~/.pip/pip.conf')
    pip_ini = os.path.expanduser('~/pip/pip.ini')

    # 判断pip文件夹是否存在
    if not os.path.exists(pip_ini):
        os.makedirs(os.path.dirname(pip_ini), exist_ok=True)

    # 向pip.ini写入镜像配置
    with open(pip_ini, 'w') as f:
        f.write("[global]\n")
        f.write(f"index-url = https://{mirror_url}/pypi/simple/\n")
        f.write("[install]\n")
        f.write(f"trusted-host = {mirror_url}\n")
        print("pip.ini 初始化完成")


def init_condarc(mirror_url: str = "mirrors.bfsu.edu.cn", set_env_dir: bool = False) -> None:
    """
    初始化condarc
    :param mirror_url:镜像源url
    :param set_env_dir:是否设置环境目录
    :return:
    """
    condarc = os.path.expanduser('~/.condarc')
    # 向condarc写入镜像配置
    with open(condarc, 'w') as f:
        if set_env_dir:
            f.write("envs_dirs:\n")
            f.write(f"  - D:\Program Files\Conda\envs\n")
            f.write("pkgs_dirs:\n")
            f.write(f"  - D:\Program Files\Conda\pkgs\n")
        f.write("channels:\n")
        f.write("  - defaults\n")
        f.write("show_channel_urls: true\n")
        f.write("default_channels:\n")
        f.write(f"  - https://{mirror_url}/anaconda/pkgs/main\n")
        f.write(f"  - https://{mirror_url}/anaconda/pkgs/r\n")
        f.write(f"  - https://{mirror_url}/anaconda/pkgs/msys2\n")
        f.write("custom_channels:\n")
        f.write(f"  conda-forge: https://{mirror_url}/anaconda/cloud\n")
        f.write(f"  msys2: https://{mirror_url}/anaconda/cloud\n")
        f.write(f"  bioconda: https://{mirror_url}/anaconda/cloud\n")
        f.write(f"  menpo: https://{mirror_url}/anaconda/cloud\n")
        f.write(f"  pytorch: https://{mirror_url}/anaconda/cloud\n")
        f.write(f"  pytorch-lts: https://{mirror_url}/anaconda/cloud\n")
        f.write(f"  simpleitk: https://{mirror_url}/anaconda/cloud\n")
        f.write(f"  paddle: https://{mirror_url}/anaconda/cloud\n")
        f.write("ssl_verify: true\n")
        print("condarc 初始化完成")


if __name__ == '__main__':
    init_pip()
    init_condarc()
