# Copyright (C) 2018-2023 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

from utils.graph import Node
from utils.ir_reader.extender import Extender


class Interpolate_extender(Extender):
    op = 'Interpolate'

    @staticmethod
    def extend(op: Node):
        Extender.attr_to_list(op, 'axes')
