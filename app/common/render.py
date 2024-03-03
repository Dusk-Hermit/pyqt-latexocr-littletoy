import matplotlib.pyplot as plt
from PIL import Image
import io

plt.rcParams.update({
    "text.usetex": True,
    "text.latex.preamble": r'''
    \usepackage{mathrsfs}
    \usepackage{amsmath}
    \usepackage{amssymb}
    \usepackage{amsfonts}
    \usepackage{bm}
    ''',
})
# https://www.sibida.net/detail/4566

def render_latex(latex_expression):
    try:
        # 设置 Matplotlib 使用 LaTeX 渲染
        plt.rc('text', usetex=True)
        plt.rc('font', family='serif')
        
        # 创建图像
        fig, ax = plt.subplots()
        
        # 添加文本框并渲染 LaTeX 公式
        ax.text(0.5, 0.5, latex_expression, fontsize=12, ha='center')
        
        renderer = fig.canvas.get_renderer()
        bbox = ax.texts[0].get_window_extent(renderer=renderer)
        
        # set the image size based on the text bounding box
        img_size = (bbox.width / 100, bbox.height / 100)
        
        # 留出一些白边
        img_size= (img_size[0]+0.5,img_size[1]+0.5)
        fig.set_size_inches(img_size)

        # plt.tight_layout()
        # 隐藏坐标轴
        ax.axis('off')
        
        # 获得图像
        buffer = io.BytesIO()
        plt.savefig(buffer, format='png', bbox_inches='tight', pad_inches=0,dpi=600)
        plt.close(fig)
        buffer.seek(0)
        img=Image.open(buffer)
        
        
        # img.show()
        
        return img
    except Exception as e:
        print("An error occurred while rendering LaTeX:", e)
        return Image.new('RGB',(0,0))
    
    print('here')

if __name__ == "__main__":
    latex_expression = r"\frac{1}{2} \int_{0}^{\infty} x^2 e^{-x} \, dx"
    latex_expression=f'${latex_expression}$'
    render_latex(latex_expression)
