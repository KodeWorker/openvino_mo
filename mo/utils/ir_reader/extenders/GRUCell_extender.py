# Copyright (C) 2018-2023 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

from front.common.partial_infer.utils import mark_input_bins
from utils.graph import Node
from utils.ir_reader.extender import Extender


class GRUCell_extender(Extender):
    op = 'GRUCell'

    @staticmethod
    def extend(op: Node):
        if not op.has_valid('activations'):
            op['activations'] = None

        mark_input_bins(op, start_port=2)

        op['need_copy_input_blobs'] = True
