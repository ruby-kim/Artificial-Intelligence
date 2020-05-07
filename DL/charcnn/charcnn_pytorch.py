# -*- coding: utf-8 -*-

import torch
import torch.nn as nn
from torch.autograd import Variable
import torch.nn.functional as F
import sys


class CharCNN(nn.Module):
    def __init__(self, char_vocab_size, char_vec_size, char_kernel_widths, char_feature_maps):
        super(CharCNN, self).__init__()
        self.conv_layers = []
        self.char_vec_size = char_vec_size