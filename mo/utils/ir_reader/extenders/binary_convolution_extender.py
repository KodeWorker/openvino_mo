# Copyright (C) 2018-2023 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

from utils.graph import Node
from utils.ir_reader.extender import Extender
from utils.ir_reader.extenders.conv_extender import Conv_extender


class BinaryConv_extender(Extender):
    op = 'BinaryConvolution'

    @staticmethod
    def extend(op: Node):
        Conv_extender.extend(op)
        op['type_to_create'] = 'Convolution'
