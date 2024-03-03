from render import render_latex
from PIL import Image

expression=r"\frac{1}{2} \int_{0}^{\infty} x^2 e^{-x} \, dx"
expression=f'${expression}$'
img=render_latex(expression)
img.show()