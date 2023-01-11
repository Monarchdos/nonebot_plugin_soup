'''
Name: Code.
Author: Monarchdos
Date: 2023-01-11
'''
import io
import sys
import setuptools

with open("README.md", "r", encoding="utf-8", errors="ignore") as fh:
    long_description = fh.read()

setuptools.setup(name="nonebot_plugin_soup",
                version="1.0.0",
                author="Monarchdos",
                author_email="admin@ayfre.com",
                keywords=("pip", "nonebot2", "nonebot", "nonebot_plugin"),
                description="""心灵鸡汤""",
                long_description=long_description,
                long_description_content_type="text/markdown",
                url="https://github.com/Monarchdos/nonebot_plugin_soup",
                packages=setuptools.find_packages(),
                include_package_data=True,
                platforms="any",
                install_requires=[
                    'nonebot-adapter-onebot>=2.0.0-beta.1,<3.0.0',
                    'nonebot2>=2.0.0-beta.1,<3.0.0', 'requests'
                ])
