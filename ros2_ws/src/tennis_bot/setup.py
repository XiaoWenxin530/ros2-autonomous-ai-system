import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'tennis_bot'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name] if os.path.exists('resource/' + package_name) else []),
        ('share/' + package_name, ['package.xml']),
        # 包含 launch 文件夹
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
        # 包含 config 文件夹
        (os.path.join('share', package_name, 'config'), glob('config/*')),
        # 包含 maps 文件夹
        (os.path.join('share', package_name, 'maps'), glob('maps/*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Group17',
    maintainer_email='your_email@example.com',
    description='Tennis-Bot core node',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'tennis_pick_node = tennis_bot.tennis_pick_node:main'
        ],
    },
)