from setuptools import find_packages, setup
import os
from glob import glob


package_name = 'mypkg'

setup(
    name=package_name,                                  #パッケージ名
    version='0.0.0',                                    #バージョン
    packages=find_packages(exclude=['test']),           #
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*.launch.py'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='hata',
    maintainer_email='s19c1092el@s.chibakoudai.jp',
    description='a package for practice',
    license='BSD-3-Clause',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker = mypkg.talker:main',               #talker.pyのmain関数という意味
            'talker2 = mypkg.talker2:main',               #talker.pyのmain関数という意味
            'listener = mypkg.listener:main',
        ],
    },
)
