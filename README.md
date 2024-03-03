*一个PyQt6做的Latex识别桌面应用*

## 前置条件

首先安装TexLive，并且配置好环境变量

其次，创建python环境：

```cmd
conda create -n latexocr python=3.10
conda activate latexocr
pip install -r requirements.txt
```

然后运行入口文件
```cmd
python demo.py
```

或者双击`run.bat`以运行

上面方法均需要安装好anaconda，不适用anaconda则可以自己配好python环境，安装依赖包并启动

## 笔记

- 增加资源文件，可以使用vscode PYQT Intergration插件，右键`.qrc`文件直接编译出`.py`
- 