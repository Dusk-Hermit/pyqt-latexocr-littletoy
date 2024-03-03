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
- 窗口启动慢，甚至比[官方示例](https://github.com/zhiyiYo/PyQt-Fluent-Widgets/tree/PyQt6)启动还慢，但启动页却很快跳过去了，这个原因还没弄懂
- 本来打算做一个整合包版本或者打包版本的来练习一下，但发现整合包版的下载依赖包就快2g了，于是放弃