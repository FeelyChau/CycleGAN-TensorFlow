# coding:utf-8

from setuptools import setup
# or
# from distutils.core import setup  

setup(
    name='cyclegan',     # 包名字
    version='1.0',   # 包版本
    description='This is a test of the setup',   # 简单描述
    author='feely',  # 作者
    author_email='pipcook@alibaba-inc.com',  # 作者邮箱
    url='https://github.com/alibaba/pipcook',      # 包的主页
    packages=[ 'train', 'model' ],                 # 包
)
