# Copyright (C) 2018-2023 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

from utils.graph import Node
from utils.ir_reader.extender import Extender


class Einsum_extender(Extender):
    op = 'Einsum'

    @staticmethod
    def extend(op: Node):
        einsum_name = op.soft_get('name', op.id)
        if isinstance(op['equation'], list):
            op['equation'] = ','.join(op['equation'])
        elif not isinstance(op['equation'], str):
            assert False, "Equation of Einsum node {} has incorrect format.".format(einsum_name)
