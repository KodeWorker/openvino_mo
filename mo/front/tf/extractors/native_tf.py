# Copyright (C) 2018-2023 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

from front.tf.partial_infer.tf import tf_native_tf_node_infer


def native_tf_node_extractor(pb):
    return {
        'infer': tf_native_tf_node_infer,
    }
