import torch.nn as nn
import torch.nn.functional as F


class Highway(nn.Module):
    def __init__(self, input_size, num_layers, f):
        super(Highway, self).__init__()
        self.num_layers = num_layers

        self.nonlinear = nn.ModuleList()
        self.linear = nn.ModuleList()
        self.gate = nn.ModuleList()

        for i in range(num_layers):
            self.nonlinear.append(nn.Linear(input_size, input_size))
            self.linear.append(nn.Linear(input_size, input_size))
            self.gate.append(nn.Linear(input_size, input_size))

    def forward(self, x):
        """
            :param x: tensor with shape of [batch_size, input_size]
            :return: tensor with shape of [batch_size, input_size]
            applies σ(x) ⨀ (f(G(x))) + (1 - σ(x)) ⨀ (Q(x)) transformation | G and Q is affine transformation,
            f is non-linear transformation, σ(x) is affine transformation with sigmoid non-linearition
            and ⨀ is element-wise multiplication
            """

        for i in range(self.num_layers):
            gate = F.sigmoid(self.gate[i](x))

            nonlinear = self.f(self.nonlinear[i](x))
            linear = self.linear[i](x)

            x = gate * nonlinear + (1 - gate) * linear
        return x
