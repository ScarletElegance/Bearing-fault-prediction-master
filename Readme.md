# 四种分类模型对轴承故障分类效果的比较研究
实验部署运行说明。

## Contents
- [CWRU Data Experiment](#cwru-data-experiment)
  - [Contents](#contents)
  - [Overview](#overview)
  - [Structure](#structure)
  - [Changelog](#changelog)
  - [Setup](#setup)
    - [Install Python](#install-python)
    - [Setup a Conda environment](#setup-a-conda-environment)
    - [Install required packages](#install-required-packages)
  - [Getting start](#getting-start)
    - [Download](#download)
    - [Operation](#operation)
  - [Extension](#extension)
    - [Setup](#setup-1)
    - [Run](#run)
  - [Contact](#contact)


## Overview
BUPT机器学习2020春季学期期末考试大作业代码。

## Structure
代码总体参照以下的目录结构:

```
10
.
├── code
│   ├── data
│   │   ├── train
│   │       └── ...
│   ├── main.ipynb
│   ├── other.ipynb
│   └── requirements.txt
├── othercode
│   └── ...
└── Readme.md
```

## Changelog
- June. 9, 2020: v0.2.0: 测试了多个分类器。
- June. 7, 2020: v0.1.5: 进行时间窗优解测试。
- June. 6, 2020: v0.1.2: 特征提取、分类模型粗略完成。
- June. 4, 2020: v0.0.5: 数据预处理测试。
- June. 3, 2020: v0.0.1: 环境创建调试。

## Setup
如果您已经配置好了python有关环境，可以直接跳到本节的[Install required packages](#install-required-packages)

### Install Python
已针对Python 3.6及更高版本进行了测试，但建议使用Python 3.7。对于Ubuntu：如果您的系统上尚未安装正确的Python版本，请运行以下命令进行安装：

```
sudo apt install python-pip
sudo apt-get update
sudo apt-get install python3.7
```

### Setup a Conda environment
使用 Anaconda 开源的Python包管理器。有关 Conda 环境使用，可以参照[官方网站](https://www.anaconda.com/)。

创建一个名为`CWRU`的新Conda环境

```
conda create --name cwru python=3.7
```

如果您位于虚拟环境中，则shell提示符应类似于：`(cwru) user@computer:~$` 如果不是，则可以使用以下命令启用虚拟环境：

```
source activate cwru 
```

要停用虚拟环境，请使用：

```
source deactivate
```

### Install required packages
要安装所有的包，请在您喜欢的虚拟环境中运行以下命令：

```
pip install -r requirements.txt
```

或者手动安装下列您可能缺少的包：

```
pandas=1.0.1
scikit-learn=0.22.1
scipy=1.3.1
numpy=1.17.3
matplotlib=3.1.2
seaborn=0.10.0
pywavelets=1.1.1
```

如果您需要使用 `Jupyter Notebook`，还可能需要安装：

```
ipykernel=5.1.3
ipython=7.9.0
jupyter=1.0.0
```

## Getting start
### Download
建议使用Git下载代码：
```
git clone https://github.com/yjw1268/CWRU-data-experiment.git
```

### Operation
运行`code/main.ipynb`，内含部分代码的讲解。如需加载模型`cwru.model`验证，可以直接跳到最后一部分。

*运行过程中可能会生成一些临时文件。需要注意的是，由于本研究采用了 K折交叉验证 `KFold`，给出的运行参考的结果可能会与您实际运行的略有不同。*

## Extension
在 `main.ipynb` 中，尝试了4种分类器：

```
DecisionTreeClassifier
SGDClassifier
```

### Setup
在`code/main.ipynb`中，如果您想复现所有的分类器，可能还需要安装：

```
tensorflow=2.0.0
mkl=2019.5
```

*如果您只需要查看最终结果，可以无需安装这些。只需查看main.ipynb文件即可*

### Run
运行 `code/main.ipynb` 中**开始分析数据**部分中的代码即可。

*需要注意的是，由于采用了 K折交叉验证 `KFold`，给出的运行参考的结果可能会与您实际运行的略有不同。*

## Contact
如果您有问题或者建议，欢迎访问开发者 [邮箱](mailto:yhwangbupt@163.com)联系。
