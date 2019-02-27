import sys
import wave
import math
from itertools import *
from typing import List, Tuple
from tree import TreeNode

root = TreeNode()

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


def encode(source: str="file.txt", output: str = "file"):
    with open(source,"r") as source_file:
        for sign in source_file.read():
            code = root.search(sign)

def decode():