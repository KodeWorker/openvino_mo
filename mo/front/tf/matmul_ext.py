# Copyright (C) 2018-2023 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

from ops.MatMul import MatMul
from front.extractor import FrontExtractorOp
from graph.graph import Node
from utils.error import Error


class MatMulExtractor(FrontExtractorOp):
    op = 'MatMul'
    enabled = True

    @classmethod
    def extract(cls, node: Node):
        unsupported_attrs = []
        for attr_name in ['adjoint_a', 'adjoint_b', 'a_is_sparse', 'b_is_sparse']:
            if attr_name in node.pb.attr and node.pb.attr[attr_name].b:
                unsupported_attrs.append(attr_name)
        if len(unsupported_attrs) != 0:
            raise Error('MatMul operation {} use unsupported attrs: {}'.format(node.id, unsupported_attrs))

        MatMul.update_node_stat(node,
                                {
                                    'transpose_a': node.pb.attr['transpose_a'].b,
                                    'transpose_b': node.pb.attr['transpose_b'].b,
                                })
        return cls.enabled
