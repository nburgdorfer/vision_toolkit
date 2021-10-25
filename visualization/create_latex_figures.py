import sys
import os
import numpy as np

from typing import List

def create_subfigures(images: List[np.ndarray], captions: List[str], labels: List[str]):
    num_sub_figs = len(images)
    width_scale = 1/num_sub_figs

    figure = "\\begin{figure}\n"

    for n in range(num_sub_figs):
        figure +=   "\t\\centering\n" + \
                    "\t\\begin{{subfigure}}{{{w:.1f}\\textwidth}}\n".format(w=width_scale) + \
                        "\t\t\\centering\n" + \
                        "\t\t\\includegraphics[width=\\textwidth]{{{img}}}\n".format(img=images[n]) + \
                        "\t\t\\caption{{{caption}}}\n".format(caption=captions[n]) + \
                        "\t\t\\label{{fig:{label}}}\n".format(label=labels[n]) + \
                        "\t\\end{subfigure}\n\t\\hfill\n"
    figure +=   "\t\\caption{{{caption}}}\n".format(caption=captions[-1]) + \
                "\t\\label{{fig:{label}}}\n".format(label=labels[-1]) + \
                "\\end{figure}"

    return figure
