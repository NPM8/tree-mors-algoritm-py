import sys
import wave
import math
from itertools import *
from typing import List, Tuple
from tree import TreeNode

root = TreeNode(
    TreeNode(
        TreeNode(
            TreeNode(None, None, 'O'),
            TreeNode(
                TreeNode(None, None, "Q"),
                TreeNode(TreeNode(TreeNode(None, None, ",")), None, "Z"),
                "G"
            ),
            "M"
        ),
        TreeNode(
            TreeNode(
                TreeNode(None, None, "Y"),
                TreeNode(
                    TreeNode(
                        TreeNode(None, None, "!")
                    ),
                    None,
                    "C"
                ),
                "K"
            ),
            TreeNode(
                TreeNode(None, None, "X"),
                TreeNode(None, None, "B"),
                "D"
            ),
            "N"
        ),
        "T"
    ),
    TreeNode(
        TreeNode(
            TreeNode(
                TreeNode(None, None, "J"),
                TreeNode(None, None, "P"),
                "W"
            ),
            TreeNode(
                TreeNode(None, TreeNode(TreeNode(None, None, "."))),
                TreeNode(None, None, "L"),
                "R"
            ),
            "A"
        ),
        TreeNode(
            TreeNode(
                TreeNode(
                    None,
                    TreeNode(None, TreeNode(None, None, "?"))
                ),
                TreeNode(None, None, "F"),
                "U"
            ),
            TreeNode(
                TreeNode(None, None, "V"),
                TreeNode(None, None, "H"),
                "S"
            ),
            "I"
        ),
        "E"
    )
)

def sin_wave(frec: float = 440.0, fremrate: int = 44100, aplitude: float = 0.5) -> List[float]:
    period = int(fremrate/frec)
    if aplitude > 1.0:
        aplitude = 1.0
    if aplitude < 0.0:
        aplitude = 0.0
    lookup_table: List[float] = [float(aplitude) * math.sin(2.0*math.pi*float(frec)*(float(i % period)/float(fremrate)))
                                 for i in range(period)]
    return [lookup_table[i % period] for i in count(0)]


def dumped_wave(frec: float = 440.0, fremrate: int = 44100, aplitude: float = 0.5, lenght: int = 44100):
    if aplitude > 1.0:
        aplitude = 1.0
    if aplitude < 0.0:
        aplitude = 0.0
    return (math.exp(-(float(i % lenght)/float(fremrate))) * s
            for i, s in enumerate(sin_wave(frec, fremrate, aplitude)))


def encode(source: str = "file.txt", output: str = "file"):
    with open(output, "w+") as output_file:
        output_file.write("")
    with open(source, "r") as source_file:
        for sign in source_file.read().upper():
            code = root.search_code(sign) if not sign == " " else "._.._"
            with open(output, 'a+') as output_file:
                output_file.write(code+'/')


def decode(source: str = "file", output: str = "decoded.txt"):
    with open(output, "w+") as output_file:
        output_file.write("")
    with open(source, "r") as source_file:
        for i in source_file.read().split("\n")[0].split("/"):
            if i == "":
                continue
            tmp = root
            if i == "._.._":
                tmp = " "
            else:
                for sign in i:
                    if sign == '.':
                        tmp = tmp.left
                    if sign == "_":
                        tmp = tmp.right
            with open(output, "a+") as output_file:
                print(tmp)
                output_file.write(tmp.data if isinstance(tmp, TreeNode) else tmp)


encode()
decode()
