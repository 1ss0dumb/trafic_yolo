from distutils.core import setup

setup(
    name="智能交通监控系统",
    version="1.0",
    description="智能交通监控系统",
    author="Louis Young",
    # 包路径与python模块（.py扩展名文件）
    packages=[
        "trafficapp",
        "trafficapp.aicv",
        "trafficapp.biz",
        "trafficapp.uis",
        "trafficapp.dao", 
    ],
    # 脚本文件（bat）
    scripts=[ 
        "run_app.bat"
    ],
    # 数据文件
    package_data={
    },
)


# python setup.py --help
# python setup.py --help-commands
# python setup.py build
# python setup.py install