# -*- mode: python ; coding: utf-8 -*-

block_cipher = None
mo_a = Analysis(
    ['mo\\main.py'],
    pathex=['mo'],
    datas=[],
    binaries=[('D:\\Users\Kelvin_Wu\\AppData\Local\\anaconda3\\envs\\openvino\\Lib\\site-packages\\openvino\\libs\\openvino.dll', 'openvino\\libs'),
			  ('D:\\Users\Kelvin_Wu\\AppData\Local\\anaconda3\\envs\\openvino\\Lib\\site-packages\\openvino\\libs\\openvino_ir_frontend.dll', 'openvino\\libs'),
			  ('D:\\Users\Kelvin_Wu\\AppData\Local\\anaconda3\\envs\\openvino\\Lib\\site-packages\\openvino\\libs\\openvino_onnx_frontend.dll', 'openvino\\libs'),
			  ('D:\\Users\Kelvin_Wu\\AppData\Local\\anaconda3\\envs\\openvino\\Lib\\site-packages\\openvino\\libs\\openvino_tensorflow_frontend.dll', 'openvino\\libs'),
			  ('D:\\Users\Kelvin_Wu\\AppData\Local\\anaconda3\\envs\\openvino\\Lib\\site-packages\\openvino\\libs\\tbb12.dll', 'openvino\\libs')],
    hiddenimports=[
	"ops.BN,"
	"ops.BatchNormInference,"
	"ops.BlockLSTM,"
	"ops.Cast,"
	"ops.ClipByValueTF,"
	"ops.Complex,"
	"ops.ConvertLike,"
	"ops.DetectionOutput,"
	"ops.Enter,"
	"ops.Exit,"
	"ops.ExtractImagePatches,"
	"ops.GRU,"
	"ops.GRUBlockCell,"
	"ops.GRUCell,"
	"ops.GatherTree,"
	"ops.If,"
	"ops.LSTM,"
	"ops.LookupTableInsert,"
	"ops.MatMul,"
	"ops.NextIteration,"
	"ops.ONNXResize10,"
	"ops.ONNXResize11,"
	"ops.RNN,"
	"ops.RNNCell,"
	"ops.ReduceOps,"
	"ops.Reverse,"
	"ops.TFFFT,"
	"ops.TFResize,"
	"ops.TensorArray,"
	"ops.TensorArrayGather,"
	"ops.TensorArrayRead,"
	"ops.TensorArrayScatter,"
	"ops.TensorArraySize,"
	"ops.TensorArrayWrite,"
	"ops.TensorIterator_ops,"
	"ops.activation,"
	"ops.activation_ops,"
	"ops.adaptive_avg_pooling,"
	"ops.arange_like,"
	"ops.argmax,"
	"ops.argmin,"
	"ops.assert_op,"
	"ops.assign,"
	"ops.aten,"
	"ops.axpy,"
	"ops.binarization,"
	"ops.box_nms,"
	"ops.broadcast,"
	"ops.bucketize,"
	"ops.clamp,"
	"ops.concat,"
	"ops.const,"
	"ops.constant_fill,"
	"ops.constant_of_shape,"
	"ops.convolution,"
	"ops.copyop,"
	"ops.crop,"
	"ops.ctc_greedy_decoder,"
	"ops.ctc_greedy_decoder_seq_len,"
	"ops.ctc_loss,"
	"ops.cumsum,"
	"ops.deconvolution,"
	"ops.deformable_convolution,"
	"ops.depth_to_space,"
	"ops.dequantize_linear,"
	"ops.detection_output_onnx,"
	"ops.dft,"
	"ops.div_sqrt_dim,"
	"ops.dropoutmask,"
	"ops.einsum,"
	"ops.elementwise,"
	"ops.eltwise,"
	"ops.eltwise_n,"
	"ops.eltwise_ninputs_in_1,"
	"ops.embedding_bag,"
	"ops.expand_dims,"
	"ops.eye,"
	"ops.fake_output,"
	"ops.fakequantize,"
	"ops.fill,"
	"ops.flatten,"
	"ops.gather,"
	"ops.gatherelements,"
	"ops.gathernd,"
	"ops.gelu,"
	"ops.grn,"
	"ops.group_norm,"
	"ops.hard_sigmoid,"
	"ops.identity,"
	"ops.instance_normalization,"
	"ops.interp,"
	"ops.interpolate,"
	"ops.layer_norm,"
	"ops.log_softmax,"
	"ops.loop,"
	"ops.lrn,"
	"ops.lstm_cell,"
	"ops.lstm_sequence,"
	"ops.lstmnonlinearity,"
	"ops.memory,"
	"ops.memoryoffset,"
	"ops.merge,"
	"ops.multinomial,"
	"ops.mvn,"
	"ops.mxfft,"
	"ops.mxrepeat,"
	"ops.mxreshape,"
	"ops.nms_rotated,"
	"ops.non_max_suppression,"
	"ops.non_zero,"
	"ops.normalize,"
	"ops.normalize_l2,"
	"ops.one_hot,"
	"ops.op,"
	"ops.pack,"
	"ops.pad,"
	"ops.parameter,"
	"ops.permute,"
	"ops.pnorm,"
	"ops.pooling,"
	"ops.power,"
	"ops.prelu,"
	"ops.priorbox,"
	"ops.priorbox_clustered,"
	"ops.priorgridgenerator_onnx,"
	"ops.proposal,"
	"ops.proposal_onnx,"
	"ops.proposal_python_example,"
	"ops.psroipooling,"
	"ops.quantize_linear,"
	"ops.random_uniform,"
	"ops.range,"
	"ops.rank,"
	"ops.read_value,"
	"ops.regionyolo,"
	"ops.reorgyolo,"
	"ops.reshape,"
	"ops.resize,"
	"ops.resize_factor_utils,"
	"ops.restrictedattentioncomponent,"
	"ops.result,"
	"ops.reverse_sequence,"
	"ops.roialign,"
	"ops.roifeatureextractor_onnx,"
	"ops.roipooling,"
	"ops.roll,"
	"ops.scale_shift,"
	"ops.scatter,"
	"ops.scatternd,"
	"ops.select,"
	"ops.shape,"
	"ops.shufflechannel,"
	"ops.size,"
	"ops.slice,"
	"ops.slice_like,"
	"ops.softmax,"
	"ops.space_to_batch,"
	"ops.space_to_depth,"
	"ops.sparse_fill_empty_rows,"
	"ops.sparse_reshape,"
	"ops.sparse_segment_mean,"
	"ops.sparse_segment_sqrtn,"
	"ops.sparse_segment_sum,"
	"ops.splice,"
	"ops.split,"
	"ops.squeeze,"
	"ops.stop_gradient,"
	"ops.strided_slice,"
	"ops.swapaxis,"
	"ops.switch,"
	"ops.tdnncomponent,"
	"ops.tensor_iterator,"
	"ops.tile,"
	"ops.timeheightconvolution,"
	"ops.topk,"
	"ops.topkrois_onnx,"
	"ops.transpose,"
	"ops.unique,"
	"ops.unsqueeze,"
	"ops.upsample,"
	"analysis.boolean_input,"
	"analysis.inputs,"
	"analysis.json_print,"
	"analysis.nodes,"
	"analysis.tf_od_api,"
	"analysis.tf_retinanet,"
	"analysis.tf_yolo,"
	"load.tf.loader,"
	"front.ATenToEmbeddingBag,"
	"front.ArgOpsSqueeze,"
	"front.AttributedClampNormalizer,"
	"front.AttributedGatherNormalizer,"
	"front.AttributedPadToPad,"
	"front.AttributedRandomUniformToRandomUniform,"
	"front.AttributedRollToRoll,"
	"front.ExpandDimsToUnsqueeze,"
	"front.FakeQuantWithMinMaxVars,"
	"front.FillToBroadcast,"
	"front.GeLUMerger_Erf,"
	"front.GeLUMerger_Tanh,"
	"front.HSigmoid_fusion,"
	"front.HSwish_fusion,"
	"front.InterpolateNormalizer,"
	"front.InterpolateV1ToInterpolate,"
	"front.LayerNorm,"
	"front.Log1p,"
	"front.MatMul_normalizer,"
	"front.MoveEmbeddedInputsToInputs,"
	"front.OneHotDepthNormalizer,"
	"front.Pack,"
	"front.PowerToEltwises,"
	"front.RollWithEmptyAxesReplacer,"
	"front.SizeReplacer,"
	"front.SqueezeNormalize,"
	"front.ThresholdedReluDecomposition,"
	"front.TopKNormalize,"
	"front.TransposeOrderNormalizer,"
	"front.YOLO,"
	"front.binary_quantize_normalization,"
	"front.broadcast_with_range,"
	"front.caffe,"
	"front.common,"
	"front.create_tensor_nodes,"
	"front.disable_weights_quantize_value_propagation,"
	"front.div,"
	"front.eltwise_n,"
	"front.extractor,"
	"front.flatten_to_reshape,"
	"front.freeze_placeholder_value,"
	"front.global_pooling_to_reduce,"
	"front.image_scaler,"
	"front.input_cut,"
	"front.instance_normalization,"
	"front.interpolate_reshape,"
	"front.kaldi,"
	"front.mxnet,"
	"front.no_op_eraser,"
	"front.non_max_suppression_normalize,"
	"front.onnx,"
	"front.output_cut,"
	"front.override_batch,"
	"front.pass_separator,"
	"front.rank_decomposer,"
	"front.reciprocal,"
	"front.reduce_axis_normalizer,"
	"front.reshape_dim_normalizer,"
	"front.restore_ports,"
	"front.scatter_normalizer,"
	"front.softmax,"
	"front.split_normalizer,"
	"front.sub,"
	"front.subgraph_matcher,"
	"front.tf,"
	"front.transformations_config,"
	"front.user_data_repack,"
	"front.tf.AutomlEfficientDet,"
	"front.tf.BatchMatMul_ext,"
	"front.tf.BatchToSpaceNDToUpsample,"
	"front.tf.BlockLSTM,"
	"front.tf.BlockLSTM_ext,"
	"front.tf.CTCGreedyDecoderReplacement,"
	"front.tf.CTCGreedyDecoder_ext,"
	"front.tf.CTCLossReplacement,"
	"front.tf.CTCLoss_ext,"
	"front.tf.Cast_ext,"
	"front.tf.ClipByValueTFTransformation,"
	"front.tf.ClipByValue_ext,"
	"front.tf.ComplexAbs,"
	"front.tf.ComplexAbsAfterComplex,"
	"front.tf.CorrectPaddingsForPadAfterComplex,"
	"front.tf.CropAndResizeReplacement,"
	"front.tf.FakeQuantWithMinMaxVars_ext,"
	"front.tf.FlattenToReshape,"
	"front.tf.GNMT_DynamicSequenceLengths,"
	"front.tf.GRUBlockCellReplacement,"
	"front.tf.GRUBlockCell_ext,"
	"front.tf.GatherTree_ext,"
	"front.tf.IteratorGetNextCut,"
	"front.tf.IteratorGetNext_ext,"
	"front.tf.LookupTableInsert_ext,"
	"front.tf.LoopCond_ext,"
	"front.tf.MapFNTransformation,"
	"front.tf.NonConstBeginStridedSliceReplacement,"
	"front.tf.ObjectDetectionAPI,"
	"front.tf.QueueDequeue_ext,"
	"front.tf.RFFTRealImagToRFFTSplit,"
	"front.tf.RetinaNetFilteredDetectionsReplacement,"
	"front.tf.RollRealImagPack,"
	"front.tf.SSDToolboxDetectionOutput,"
	"front.tf.SwitchMergeOptimization,"
	"front.tf.TFFFTToDFT,"
	"front.tf.TFResizeToInterpolate,"
	"front.tf.TFScatterNDDecomposition,"
	"front.tf.TFSliceToSlice,"
	"front.tf.TensorArrayExtractors,"
	"front.tf.TensorArrayGatherV3,"
	"front.tf.UnpackPackReverseInputChannels,"
	"front.tf.WhereDecomposition,"
	"front.tf.WhileNormalize,"
	"front.tf.activation_ext,"
	"front.tf.argmax_ext,"
	"front.tf.argmin_ext,"
	"front.tf.assign_elimination,"
	"front.tf.basic_lstm_cell,"
	"front.tf.batch_to_space_ext,"
	"front.tf.broadcast_ext,"
	"front.tf.bucketize,"
	"front.tf.bucketize_ext,"
	"front.tf.common,"
	"front.tf.complex_ext,"
	"front.tf.concat,"
	"front.tf.concat_ext,"
	"front.tf.const_ext,"
	"front.tf.conv_ext,"
	"front.tf.crop_and_resize_ext,"
	"front.tf.cumsum_ext,"
	"front.tf.custom_subgraph_call,"
	"front.tf.deconv_ext,"
	"front.tf.depth_to_space,"
	"front.tf.einsum_ext,"
	"front.tf.elementwise_ext,"
	"front.tf.embedding_segments_mean_decomposition,"
	"front.tf.embedding_segments_operation_fusing,"
	"front.tf.expand_dims_ext,"
	"front.tf.extract_image_patches_ext,"
	"front.tf.extractor,"
	"front.tf.extractors,"
	"front.tf.eye_ext,"
	"front.tf.eye_tf_to_eye,"
	"front.tf.fake_const_ext,"
	"front.tf.fft_ext,"
	"front.tf.fifo_queue_v2_ext,"
	"front.tf.fifo_replacer,"
	"front.tf.fill_ext,"
	"front.tf.floor_div_decomposition,"
	"front.tf.floor_ext,"
	"front.tf.gather_ext,"
	"front.tf.gathernd_ext,"
	"front.tf.graph_utils,"
	"front.tf.identityN_to_identity,"
	"front.tf.identity_ext,"
	"front.tf.if_ext,"
	"front.tf.loader,"
	"front.tf.log_softmax_ext,"
	"front.tf.lrn_ext,"
	"front.tf.matmul_ext,"
	"front.tf.mvn,"
	"front.tf.mvn_unrolled,"
	"front.tf.nearest_neighbor_upsampling,"
	"front.tf.next_iteration_ext,"
	"front.tf.non_max_suppression_ext,"
	"front.tf.non_max_suppression_normalize,"
	"front.tf.noop,"
	"front.tf.one_hot_ext,"
	"front.tf.pad_ext,"
	"front.tf.pad_tf_to_pad,"
	"front.tf.partial_infer,"
	"front.tf.placeholder_ext,"
	"front.tf.placeholder_with_default_ext,"
	"front.tf.pooling_ext,"
	"front.tf.prelu,"
	"front.tf.random_uniform_ext,"
	"front.tf.random_uniform_int_ext,"
	"front.tf.range_ext,"
	"front.tf.reduce_ext,"
	"front.tf.register_custom_ops,"
	"front.tf.replacement,"
	"front.tf.reshape_related_ext,"
	"front.tf.resize_bilinear,"
	"front.tf.resize_nearest_neighbor,"
	"front.tf.reverse_sequence,"
	"front.tf.reverse_v2,"
	"front.tf.roll_ext,"
	"front.tf.scatter_nd_ext,"
	"front.tf.select_ext,"
	"front.tf.sign_ext,"
	"front.tf.slice_ext,"
	"front.tf.softmax_ext,"
	"front.tf.softplus_ext,"
	"front.tf.space_to_batch,"
	"front.tf.space_to_batch_ext,"
	"front.tf.space_to_depth_ext,"
	"front.tf.sparse_fill_empty_rows_ext,"
	"front.tf.sparse_segment_mean_ext,"
	"front.tf.sparse_segment_sqrtn_ext,"
	"front.tf.sparse_segment_sum_ext,"
	"front.tf.sparse_to_dense_replacer,"
	"front.tf.split_ext,"
	"front.tf.swap_deconv_inputs,"
	"front.tf.swish_ext,"
	"front.tf.tensorflow_custom_operations_config_update,"
	"front.tf.tile_ext,"
	"front.tf.topk_ext,"
	"front.tf.transpose_ext,"
	"front.tf.transposed_mvn_unrolled,"
	"front.tf.unique_ext,"
	"front.tf.variable_ext,"
	"front.tf.variables_values_freezing,"
	"front.tf.while_ext,"
	"front.tf.extractors.concat,"
	"front.tf.extractors.fused_bn,"
	"front.tf.extractors.identity,"
	"front.tf.extractors.native_tf,"
	"front.tf.extractors.pack,"
	"front.tf.extractors.strided_slice,"
	"front.tf.extractors.subgraph_utils,"
	"front.tf.extractors.utils,"
	"middle.AddFakeQuantizeFuse,"
	"middle.AddIsCyclicAttribute,"
	"middle.ApplyNHWCtoNCHWpermutation,"
	"middle.ApplyPermutations,"
	"middle.ArgOpsToTopK,"
	"middle.AttributedTileNormalizer,"
	"middle.BiasAddBroadcasting,"
	"middle.BinarizeWeightsM1P1,"
	"middle.BlockLSTMtoLSTMSequence,"
	"middle.CheckForCycle,"
	"middle.ConcatOptimization,"
	"middle.ConstSwitchResolver,"
	"middle.ConvToBinaryConv,"
	"middle.ConvertGroupedStridedSlice,"
	"middle.ConvertLayoutDependentOperations,"
	"middle.ConvertMultiInputConv,"
	"middle.CustomSubgraphCall,"
	"middle.CutInputHavingZeroDimFromConcat,"
	"middle.DecomposeBias,"
	"middle.DecomposeBidirectionalRNNSequence,"
	"middle.Deconvolution3rdInputNormalization,"
	"middle.DeleteControlFlowEdges,"
	"middle.DeleteNotExecutable,"
	"middle.DilatedConvolution,"
	"middle.EltwiseChecker,"
	"middle.EltwiseInputReshape,"
	"middle.FakeSplitOutputs,"
	"middle.FuseReshapesSequence,"
	"middle.FusedBatchNormNonConstant,"
	"middle.FusedBatchNormTraining,"
	"middle.GRURNNSequenceToTensorIterator,"
	"middle.GatherNDDecomposition,"
	"middle.GroupNorm,"
	"middle.InputCut,"
	"middle.InsertLayoutPropagationTransposes,"
	"middle.InsertSelect,"
	"middle.InterpolateSequenceToInterpolate,"
	"middle.L2NormFusing,"
	"middle.LSTMRNNSequenceToTensorIterator,"
	"middle.LayoutChangeForConstantShapePaths,"
	"middle.LayoutChangeForEinsum,"
	"middle.LeakyReluPattern,"
	"middle.MXNetRNNSequenceNormalize,"
	"middle.MXNetSplitMultiLayers,"
	"middle.MXTileReplacer,"
	"middle.MakeKaldiConstReshapable,"
	"middle.MarkSubgraphsWithCorrectLayout,"
	"middle.MergeNodesPermutations,"
	"middle.MoveConstToLoopBody,"
	"middle.MulFakeQuantizeFuse,"
	"middle.ONNXRNNSequenceNormalize,"
	"middle.ONNXResize11ToInterpolate,"
	"middle.PartialInfer,"
	"middle.PoolV2ToAttributedPool,"
	"middle.PreserveRuntimeInfo,"
	"middle.RNNSequenceNormalizeToIE,"
	"middle.ReluQuantizeFuse,"
	"middle.RemoveDuplicationMemory,"
	"middle.RemoveIdentity,"
	"middle.RemoveRedundantReshapeAfterCropAndResize,"
	"middle.RemoveRedundantReshapes,"
	"middle.RemoveUselessConcatSplit,"
	"middle.RemoveUselessCrops,"
	"middle.RemoveUselessPad,"
	"middle.ReplaceMemoryOffsetWithSplice,"
	"middle.ReplacePNorm,"
	"middle.ReplaceSpliceNodePattern,"
	"middle.ReverseTransposeNormalization,"
	"middle.ReverseV2ToReverseSequence,"
	"middle.SSliceComplex,"
	"middle.SharedWeightsDuplication,"
	"middle.SliceConverter,"
	"middle.SliceLikeToStridedSlice,"
	"middle.SplitConcatPairToInterpolate,"
	"middle.StridedSliceNormalizer,"
	"middle.SwapAxesMiddleReplacer,"
	"middle.TF_lstm_cell_to_generic,"
	"middle.TensorIteratorBackEdge,"
	"middle.TensorIteratorCondition,"
	"middle.TensorIteratorConditionChecker,"
	"middle.TensorIteratorInput,"
	"middle.TensorIteratorLSTMToLSTMSequence,"
	"middle.TensorIteratorMerge,"
	"middle.TensorIteratorOutput,"
	"middle.TensorIterator_utils,"
	"middle.UnsqueezeTileReshapeBlockToInterpolate,"
	"middle.UpsampleToResample,"
	"middle.UselessMerge,"
	"middle.UselessSplitEraser,"
	"middle.dequantize_linear_resolver,"
	"middle.fusings,"
	"middle.layer_normalization,"
	"middle.pass_separator,"
	"middle.passes,"
	"middle.pattern_match,"
	"middle.permute_tensor_iterator,"
	"middle.preprocessing,"
	"middle.quantize_dequantize_linear_resolver,"
	"middle.quantize_fuses,"
	"middle.quantize_linear_resolver,"
	"middle.replacement,"
	"middle.reverse_tensor_iterator,"
	"middle.sparse_reshape,"
	"middle.split_tdnn_memoryoffset,"
	"back.AvgPool,"
	"back.CellNormalizer,"
	"back.ChangeOutputTypeAttributes,"
	"back.ChangeRandomUniformOutputType,"
	"back.ClampNormalizer,"
	"back.ConvolutionNormalizer,"
	"back.CorrectName,"
	"back.CropToStridedSlice,"
	"back.CutMemory,"
	"back.EnableConstantStridedSlice,"
	"back.FakeOutputResolver,"
	"back.ForceStrictPrecision,"
	"back.FuseTransposesSequence,"
	"back.GatherNormalizer,"
	"back.InterpolateReshape,"
	"back.LRNToNorm,"
	"back.LayoutChangeForGatherND,"
	"back.LeakyReLUMutation,"
	"back.LinearToLinearONNXReplacer,"
	"back.MarkNodesWithShapeValues,"
	"back.MatMulNormalizer,"
	"back.MaxPool,"
	"back.NormalizeToNormalizeL2,"
	"back.OptimizeTransposeReshapeSequence,"
	"back.PackBinaryWeights,"
	"back.ProposalMutation,"
	"back.RNNSequenceTypeRename,"
	"back.ReduceMerge,"
	"back.ReduceTransposeDimensions,"
	"back.RemoveUselessConvert,"
	"back.ReshapeMutation,"
	"back.ResultNormalizer,"
	"back.ResultRename,"
	"back.ReverseInputChannels,"
	"back.SelectBroadcast,"
	"back.ShapeOfConstFolding,"
	"back.ShuffleChannelPatternOptimization,"
	"back.SpecialNodesFinalization,"
	"back.StridedSliceMasksNormalizer,"
	"back.TopKNormalizer,"
	"back.TransposeDFT,"
	"back.TransposeReduceFusing,"
	"back.UselessConcatRemoval,"
	"back.add_outputs_recursive,"
	"back.blob_normalizer,"
	"back.compress_quantized_weights,"
	"back.ie_ir_ver_2,"
	"back.insert_compatibility_l2normalization,"
	"back.kaldi_remove_memory_output,"
	"back.names_uniqueness_check,"
	"back.offline_transformations,"
	"back.op_versioning,"
	"back.pass_separator,"
	"back.preprocessing,"
	"back.priorbox_mutation,"
	"back.remove_last_softmax_pattern,"
	"back.replacement,"
	"load.onnx.loader,"
	"front.onnx.AttributedSliceToSlice,"
	"front.onnx.CTCGreedyDecoder_ext,"
	"front.onnx.LoopNormalize,"
	"front.onnx.MvnOnnxToMvn,"
	"front.onnx.ONNXResize10ToInterpolate,"
	"front.onnx.activation_ext,"
	"front.onnx.affine_ext,"
	"front.onnx.argmax_ext,"
	"front.onnx.argmin_ext,"
	"front.onnx.aten_ext,"
	"front.onnx.cast_ext,"
	"front.onnx.clip_ext,"
	"front.onnx.concat_ext,"
	"front.onnx.const_ext,"
	"front.onnx.constant_fill_ext,"
	"front.onnx.constant_of_shape_ext,"
	"front.onnx.constant_of_shape_to_broadcast,"
	"front.onnx.conv_ext,"
	"front.onnx.crop_ext,"
	"front.onnx.cumsum_ext,"
	"front.onnx.deformable_conv_ext,"
	"front.onnx.depth_to_space_ext,"
	"front.onnx.dequantize_linear_ext,"
	"front.onnx.detection_output,"
	"front.onnx.detection_output_ext,"
	"front.onnx.detection_output_onnx_ext,"
	"front.onnx.dropout_ext,"
	"front.onnx.einsum_ext,"
	"front.onnx.elementwise_ext,"
	"front.onnx.expand_ext,"
	"front.onnx.extractor,"
	"front.onnx.extractors,"
	"front.onnx.flattenONNX_to_reshape,"
	"front.onnx.flatten_ext,"
	"front.onnx.fused_bn_ext,"
	"front.onnx.gather_ext,"
	"front.onnx.gatherelements_ext,"
	"front.onnx.gathernd_ext,"
	"front.onnx.gemm_ext,"
	"front.onnx.group_norm_ext,"
	"front.onnx.gru_ext,"
	"front.onnx.hard_sigmoid_ext,"
	"front.onnx.identity_ext,"
	"front.onnx.image_scaler_ext,"
	"front.onnx.instance_normalization_ext,"
	"front.onnx.loader,"
	"front.onnx.logsoftmaxONNX_to_logsoftmax,"
	"front.onnx.loop_ext,"
	"front.onnx.lp_normalization_ext,"
	"front.onnx.lrn_ext,"
	"front.onnx.lstm_ext,"
	"front.onnx.mask_rcnn_conversion,"
	"front.onnx.matmul_ext,"
	"front.onnx.mean_variance_normalization_ext,"
	"front.onnx.non_max_suppression_ext,"
	"front.onnx.non_zero_ext,"
	"front.onnx.normalize_ext,"
	"front.onnx.normalize_l2_normalize,"
	"front.onnx.one_hot_ext,"
	"front.onnx.one_hot_normalize,"
	"front.onnx.pad_converter,"
	"front.onnx.pad_ext,"
	"front.onnx.parameter_ext,"
	"front.onnx.person_detection_crossroad_conversion,"
	"front.onnx.pooling_ext,"
	"front.onnx.priorbox_clustered_ext,"
	"front.onnx.priorbox_ext,"
	"front.onnx.priorgridgenerator_ext,"
	"front.onnx.proposal_ext,"
	"front.onnx.quantize_ext,"
	"front.onnx.quantize_linear_ext,"
	"front.onnx.random_uniform_ext,"
	"front.onnx.range_ext,"
	"front.onnx.reduce_ext,"
	"front.onnx.register_custom_ops,"
	"front.onnx.reshape_ext,"
	"front.onnx.resize_ext,"
	"front.onnx.reverse_sequence_ext,"
	"front.onnx.rnn_ext,"
	"front.onnx.roialign_ext,"
	"front.onnx.roifeatureextractor_ext,"
	"front.onnx.scatter_ext,"
	"front.onnx.shape_ext,"
	"front.onnx.size_ext,"
	"front.onnx.slice_ext,"
	"front.onnx.softmaxONNX_to_softmax,"
	"front.onnx.softmax_ext,"
	"front.onnx.softplus_ext,"
	"front.onnx.space_to_depth_ext,"
	"front.onnx.split_ext,"
	"front.onnx.squeeze_ext,"
	"front.onnx.top_k_ext,"
	"front.onnx.topkrois_ext,"
	"front.onnx.transpose_ext,"
	"front.onnx.unsqueeze_ext,"
	"front.onnx.upsample_ext,"
	"front.onnx.where_ext,"
	"front.onnx.extractors.utils,"
	"ops.BN",
	"ops.BatchNormInference",
	"ops.BlockLSTM",
	"ops.Cast",
	"ops.ClipByValueTF",
	"ops.Complex",
	"ops.ConvertLike",
	"ops.DetectionOutput",
	"ops.Enter",
	"ops.Exit",
	"ops.ExtractImagePatches",
	"ops.GRU",
	"ops.GRUBlockCell",
	"ops.GRUCell",
	"ops.GatherTree",
	"ops.If",
	"ops.LSTM",
	"ops.LookupTableInsert",
	"ops.MatMul",
	"ops.NextIteration",
	"ops.ONNXResize10",
	"ops.ONNXResize11",
	"ops.RNN",
	"ops.RNNCell",
	"ops.ReduceOps",
	"ops.Reverse",
	"ops.TFFFT",
	"ops.TFResize",
	"ops.TensorArray",
	"ops.TensorArrayGather",
	"ops.TensorArrayRead",
	"ops.TensorArrayScatter",
	"ops.TensorArraySize",
	"ops.TensorArrayWrite",
	"ops.TensorIterator_ops",
	"ops.activation",
	"ops.activation_ops",
	"ops.adaptive_avg_pooling",
	"ops.arange_like",
	"ops.argmax",
	"ops.argmin",
	"ops.assert_op",
	"ops.assign",
	"ops.aten",
	"ops.axpy",
	"ops.binarization",
	"ops.box_nms",
	"ops.broadcast",
	"ops.bucketize",
	"ops.clamp",
	"ops.concat",
	"ops.const",
	"ops.constant_fill",
	"ops.constant_of_shape",
	"ops.convolution",
	"ops.copyop",
	"ops.crop",
	"ops.ctc_greedy_decoder",
	"ops.ctc_greedy_decoder_seq_len",
	"ops.ctc_loss",
	"ops.cumsum",
	"ops.deconvolution",
	"ops.deformable_convolution",
	"ops.depth_to_space",
	"ops.dequantize_linear",
	"ops.detection_output_onnx",
	"ops.dft",
	"ops.div_sqrt_dim",
	"ops.dropoutmask",
	"ops.einsum",
	"ops.elementwise",
	"ops.eltwise",
	"ops.eltwise_n",
	"ops.eltwise_ninputs_in_1",
	"ops.embedding_bag",
	"ops.expand_dims",
	"ops.eye",
	"ops.fake_output",
	"ops.fakequantize",
	"ops.fill",
	"ops.flatten",
	"ops.gather",
	"ops.gatherelements",
	"ops.gathernd",
	"ops.gelu",
	"ops.grn",
	"ops.group_norm",
	"ops.hard_sigmoid",
	"ops.identity",
	"ops.instance_normalization",
	"ops.interp",
	"ops.interpolate",
	"ops.layer_norm",
	"ops.log_softmax",
	"ops.loop",
	"ops.lrn",
	"ops.lstm_cell",
	"ops.lstm_sequence",
	"ops.lstmnonlinearity",
	"ops.memory",
	"ops.memoryoffset",
	"ops.merge",
	"ops.multinomial",
	"ops.mvn",
	"ops.mxfft",
	"ops.mxrepeat",
	"ops.mxreshape",
	"ops.nms_rotated",
	"ops.non_max_suppression",
	"ops.non_zero",
	"ops.normalize",
	"ops.normalize_l2",
	"ops.one_hot",
	"ops.op",
	"ops.pack",
	"ops.pad",
	"ops.parameter",
	"ops.permute",
	"ops.pnorm",
	"ops.pooling",
	"ops.power",
	"ops.prelu",
	"ops.priorbox",
	"ops.priorbox_clustered",
	"ops.priorgridgenerator_onnx",
	"ops.proposal",
	"ops.proposal_onnx",
	"ops.proposal_python_example",
	"ops.psroipooling",
	"ops.quantize_linear",
	"ops.random_uniform",
	"ops.range",
	"ops.rank",
	"ops.read_value",
	"ops.regionyolo",
	"ops.reorgyolo",
	"ops.reshape",
	"ops.resize",
	"ops.resize_factor_utils",
	"ops.restrictedattentioncomponent",
	"ops.result",
	"ops.reverse_sequence",
	"ops.roialign",
	"ops.roifeatureextractor_onnx",
	"ops.roipooling",
	"ops.roll",
	"ops.scale_shift",
	"ops.scatter",
	"ops.scatternd",
	"ops.select",
	"ops.shape",
	"ops.shufflechannel",
	"ops.size",
	"ops.slice",
	"ops.slice_like",
	"ops.softmax",
	"ops.space_to_batch",
	"ops.space_to_depth",
	"ops.sparse_fill_empty_rows",
	"ops.sparse_reshape",
	"ops.sparse_segment_mean",
	"ops.sparse_segment_sqrtn",
	"ops.sparse_segment_sum",
	"ops.splice",
	"ops.split",
	"ops.squeeze",
	"ops.stop_gradient",
	"ops.strided_slice",
	"ops.swapaxis",
	"ops.switch",
	"ops.tdnncomponent",
	"ops.tensor_iterator",
	"ops.tile",
	"ops.timeheightconvolution",
	"ops.topk",
	"ops.topkrois_onnx",
	"ops.transpose",
	"ops.unique",
	"ops.unsqueeze",
	"ops.upsample",
	"analysis.boolean_input",
	"analysis.inputs",
	"analysis.json_print",
	"analysis.nodes",
	"analysis.tf_od_api",
	"analysis.tf_retinanet",
	"analysis.tf_yolo",
	"load.tf.loader",
	"front.ATenToEmbeddingBag",
	"front.ArgOpsSqueeze",
	"front.AttributedClampNormalizer",
	"front.AttributedGatherNormalizer",
	"front.AttributedPadToPad",
	"front.AttributedRandomUniformToRandomUniform",
	"front.AttributedRollToRoll",
	"front.ExpandDimsToUnsqueeze",
	"front.FakeQuantWithMinMaxVars",
	"front.FillToBroadcast",
	"front.GeLUMerger_Erf",
	"front.GeLUMerger_Tanh",
	"front.HSigmoid_fusion",
	"front.HSwish_fusion",
	"front.InterpolateNormalizer",
	"front.InterpolateV1ToInterpolate",
	"front.LayerNorm",
	"front.Log1p",
	"front.MatMul_normalizer",
	"front.MoveEmbeddedInputsToInputs",
	"front.OneHotDepthNormalizer",
	"front.Pack",
	"front.PowerToEltwises",
	"front.RollWithEmptyAxesReplacer",
	"front.SizeReplacer",
	"front.SqueezeNormalize",
	"front.ThresholdedReluDecomposition",
	"front.TopKNormalize",
	"front.TransposeOrderNormalizer",
	"front.YOLO",
	"front.binary_quantize_normalization",
	"front.broadcast_with_range",
	"front.caffe",
	"front.common",
	"front.create_tensor_nodes",
	"front.disable_weights_quantize_value_propagation",
	"front.div",
	"front.eltwise_n",
	"front.extractor",
	"front.flatten_to_reshape",
	"front.freeze_placeholder_value",
	"front.global_pooling_to_reduce",
	"front.image_scaler",
	"front.input_cut",
	"front.instance_normalization",
	"front.interpolate_reshape",
	"front.kaldi",
	"front.mxnet",
	"front.no_op_eraser",
	"front.non_max_suppression_normalize",
	"front.onnx",
	"front.output_cut",
	"front.override_batch",
	"front.pass_separator",
	"front.rank_decomposer",
	"front.reciprocal",
	"front.reduce_axis_normalizer",
	"front.reshape_dim_normalizer",
	"front.restore_ports",
	"front.scatter_normalizer",
	"front.softmax",
	"front.split_normalizer",
	"front.sub",
	"front.subgraph_matcher",
	"front.tf",
	"front.transformations_config",
	"front.user_data_repack",
	"front.tf.AutomlEfficientDet",
	"front.tf.BatchMatMul_ext",
	"front.tf.BatchToSpaceNDToUpsample",
	"front.tf.BlockLSTM",
	"front.tf.BlockLSTM_ext",
	"front.tf.CTCGreedyDecoderReplacement",
	"front.tf.CTCGreedyDecoder_ext",
	"front.tf.CTCLossReplacement",
	"front.tf.CTCLoss_ext",
	"front.tf.Cast_ext",
	"front.tf.ClipByValueTFTransformation",
	"front.tf.ClipByValue_ext",
	"front.tf.ComplexAbs",
	"front.tf.ComplexAbsAfterComplex",
	"front.tf.CorrectPaddingsForPadAfterComplex",
	"front.tf.CropAndResizeReplacement",
	"front.tf.FakeQuantWithMinMaxVars_ext",
	"front.tf.FlattenToReshape",
	"front.tf.GNMT_DynamicSequenceLengths",
	"front.tf.GRUBlockCellReplacement",
	"front.tf.GRUBlockCell_ext",
	"front.tf.GatherTree_ext",
	"front.tf.IteratorGetNextCut",
	"front.tf.IteratorGetNext_ext",
	"front.tf.LookupTableInsert_ext",
	"front.tf.LoopCond_ext",
	"front.tf.MapFNTransformation",
	"front.tf.NonConstBeginStridedSliceReplacement",
	"front.tf.ObjectDetectionAPI",
	"front.tf.QueueDequeue_ext",
	"front.tf.RFFTRealImagToRFFTSplit",
	"front.tf.RetinaNetFilteredDetectionsReplacement",
	"front.tf.RollRealImagPack",
	"front.tf.SSDToolboxDetectionOutput",
	"front.tf.SwitchMergeOptimization",
	"front.tf.TFFFTToDFT",
	"front.tf.TFResizeToInterpolate",
	"front.tf.TFScatterNDDecomposition",
	"front.tf.TFSliceToSlice",
	"front.tf.TensorArrayExtractors",
	"front.tf.TensorArrayGatherV3",
	"front.tf.UnpackPackReverseInputChannels",
	"front.tf.WhereDecomposition",
	"front.tf.WhileNormalize",
	"front.tf.activation_ext",
	"front.tf.argmax_ext",
	"front.tf.argmin_ext",
	"front.tf.assign_elimination",
	"front.tf.basic_lstm_cell",
	"front.tf.batch_to_space_ext",
	"front.tf.broadcast_ext",
	"front.tf.bucketize",
	"front.tf.bucketize_ext",
	"front.tf.common",
	"front.tf.complex_ext",
	"front.tf.concat",
	"front.tf.concat_ext",
	"front.tf.const_ext",
	"front.tf.conv_ext",
	"front.tf.crop_and_resize_ext",
	"front.tf.cumsum_ext",
	"front.tf.custom_subgraph_call",
	"front.tf.deconv_ext",
	"front.tf.depth_to_space",
	"front.tf.einsum_ext",
	"front.tf.elementwise_ext",
	"front.tf.embedding_segments_mean_decomposition",
	"front.tf.embedding_segments_operation_fusing",
	"front.tf.expand_dims_ext",
	"front.tf.extract_image_patches_ext",
	"front.tf.extractor",
	"front.tf.extractors",
	"front.tf.eye_ext",
	"front.tf.eye_tf_to_eye",
	"front.tf.fake_const_ext",
	"front.tf.fft_ext",
	"front.tf.fifo_queue_v2_ext",
	"front.tf.fifo_replacer",
	"front.tf.fill_ext",
	"front.tf.floor_div_decomposition",
	"front.tf.floor_ext",
	"front.tf.gather_ext",
	"front.tf.gathernd_ext",
	"front.tf.graph_utils",
	"front.tf.identityN_to_identity",
	"front.tf.identity_ext",
	"front.tf.if_ext",
	"front.tf.loader",
	"front.tf.log_softmax_ext",
	"front.tf.lrn_ext",
	"front.tf.matmul_ext",
	"front.tf.mvn",
	"front.tf.mvn_unrolled",
	"front.tf.nearest_neighbor_upsampling",
	"front.tf.next_iteration_ext",
	"front.tf.non_max_suppression_ext",
	"front.tf.non_max_suppression_normalize",
	"front.tf.noop",
	"front.tf.one_hot_ext",
	"front.tf.pad_ext",
	"front.tf.pad_tf_to_pad",
	"front.tf.partial_infer",
	"front.tf.placeholder_ext",
	"front.tf.placeholder_with_default_ext",
	"front.tf.pooling_ext",
	"front.tf.prelu",
	"front.tf.random_uniform_ext",
	"front.tf.random_uniform_int_ext",
	"front.tf.range_ext",
	"front.tf.reduce_ext",
	"front.tf.register_custom_ops",
	"front.tf.replacement",
	"front.tf.reshape_related_ext",
	"front.tf.resize_bilinear",
	"front.tf.resize_nearest_neighbor",
	"front.tf.reverse_sequence",
	"front.tf.reverse_v2",
	"front.tf.roll_ext",
	"front.tf.scatter_nd_ext",
	"front.tf.select_ext",
	"front.tf.sign_ext",
	"front.tf.slice_ext",
	"front.tf.softmax_ext",
	"front.tf.softplus_ext",
	"front.tf.space_to_batch",
	"front.tf.space_to_batch_ext",
	"front.tf.space_to_depth_ext",
	"front.tf.sparse_fill_empty_rows_ext",
	"front.tf.sparse_segment_mean_ext",
	"front.tf.sparse_segment_sqrtn_ext",
	"front.tf.sparse_segment_sum_ext",
	"front.tf.sparse_to_dense_replacer",
	"front.tf.split_ext",
	"front.tf.swap_deconv_inputs",
	"front.tf.swish_ext",
	"front.tf.tensorflow_custom_operations_config_update",
	"front.tf.tile_ext",
	"front.tf.topk_ext",
	"front.tf.transpose_ext",
	"front.tf.transposed_mvn_unrolled",
	"front.tf.unique_ext",
	"front.tf.variable_ext",
	"front.tf.variables_values_freezing",
	"front.tf.while_ext",
	"front.tf.extractors.concat",
	"front.tf.extractors.fused_bn",
	"front.tf.extractors.identity",
	"front.tf.extractors.native_tf",
	"front.tf.extractors.pack",
	"front.tf.extractors.strided_slice",
	"front.tf.extractors.subgraph_utils",
	"front.tf.extractors.utils",
	"middle.AddFakeQuantizeFuse",
	"middle.AddIsCyclicAttribute",
	"middle.ApplyNHWCtoNCHWpermutation",
	"middle.ApplyPermutations",
	"middle.ArgOpsToTopK",
	"middle.AttributedTileNormalizer",
	"middle.BiasAddBroadcasting",
	"middle.BinarizeWeightsM1P1",
	"middle.BlockLSTMtoLSTMSequence",
	"middle.CheckForCycle",
	"middle.ConcatOptimization",
	"middle.ConstSwitchResolver",
	"middle.ConvToBinaryConv",
	"middle.ConvertGroupedStridedSlice",
	"middle.ConvertLayoutDependentOperations",
	"middle.ConvertMultiInputConv",
	"middle.CustomSubgraphCall",
	"middle.CutInputHavingZeroDimFromConcat",
	"middle.DecomposeBias",
	"middle.DecomposeBidirectionalRNNSequence",
	"middle.Deconvolution3rdInputNormalization",
	"middle.DeleteControlFlowEdges",
	"middle.DeleteNotExecutable",
	"middle.DilatedConvolution",
	"middle.EltwiseChecker",
	"middle.EltwiseInputReshape",
	"middle.FakeSplitOutputs",
	"middle.FuseReshapesSequence",
	"middle.FusedBatchNormNonConstant",
	"middle.FusedBatchNormTraining",
	"middle.GRURNNSequenceToTensorIterator",
	"middle.GatherNDDecomposition",
	"middle.GroupNorm",
	"middle.InputCut",
	"middle.InsertLayoutPropagationTransposes",
	"middle.InsertSelect",
	"middle.InterpolateSequenceToInterpolate",
	"middle.L2NormFusing",
	"middle.LSTMRNNSequenceToTensorIterator",
	"middle.LayoutChangeForConstantShapePaths",
	"middle.LayoutChangeForEinsum",
	"middle.LeakyReluPattern",
	"middle.MXNetRNNSequenceNormalize",
	"middle.MXNetSplitMultiLayers",
	"middle.MXTileReplacer",
	"middle.MakeKaldiConstReshapable",
	"middle.MarkSubgraphsWithCorrectLayout",
	"middle.MergeNodesPermutations",
	"middle.MoveConstToLoopBody",
	"middle.MulFakeQuantizeFuse",
	"middle.ONNXRNNSequenceNormalize",
	"middle.ONNXResize11ToInterpolate",
	"middle.PartialInfer",
	"middle.PoolV2ToAttributedPool",
	"middle.PreserveRuntimeInfo",
	"middle.RNNSequenceNormalizeToIE",
	"middle.ReluQuantizeFuse",
	"middle.RemoveDuplicationMemory",
	"middle.RemoveIdentity",
	"middle.RemoveRedundantReshapeAfterCropAndResize",
	"middle.RemoveRedundantReshapes",
	"middle.RemoveUselessConcatSplit",
	"middle.RemoveUselessCrops",
	"middle.RemoveUselessPad",
	"middle.ReplaceMemoryOffsetWithSplice",
	"middle.ReplacePNorm",
	"middle.ReplaceSpliceNodePattern",
	"middle.ReverseTransposeNormalization",
	"middle.ReverseV2ToReverseSequence",
	"middle.SSliceComplex",
	"middle.SharedWeightsDuplication",
	"middle.SliceConverter",
	"middle.SliceLikeToStridedSlice",
	"middle.SplitConcatPairToInterpolate",
	"middle.StridedSliceNormalizer",
	"middle.SwapAxesMiddleReplacer",
	"middle.TF_lstm_cell_to_generic",
	"middle.TensorIteratorBackEdge",
	"middle.TensorIteratorCondition",
	"middle.TensorIteratorConditionChecker",
	"middle.TensorIteratorInput",
	"middle.TensorIteratorLSTMToLSTMSequence",
	"middle.TensorIteratorMerge",
	"middle.TensorIteratorOutput",
	"middle.TensorIterator_utils",
	"middle.UnsqueezeTileReshapeBlockToInterpolate",
	"middle.UpsampleToResample",
	"middle.UselessMerge",
	"middle.UselessSplitEraser",
	"middle.dequantize_linear_resolver",
	"middle.fusings",
	"middle.layer_normalization",
	"middle.pass_separator",
	"middle.passes",
	"middle.pattern_match",
	"middle.permute_tensor_iterator",
	"middle.preprocessing",
	"middle.quantize_dequantize_linear_resolver",
	"middle.quantize_fuses",
	"middle.quantize_linear_resolver",
	"middle.replacement",
	"middle.reverse_tensor_iterator",
	"middle.sparse_reshape",
	"middle.split_tdnn_memoryoffset",
	"back.AvgPool",
	"back.CellNormalizer",
	"back.ChangeOutputTypeAttributes",
	"back.ChangeRandomUniformOutputType",
	"back.ClampNormalizer",
	"back.ConvolutionNormalizer",
	"back.CorrectName",
	"back.CropToStridedSlice",
	"back.CutMemory",
	"back.EnableConstantStridedSlice",
	"back.FakeOutputResolver",
	"back.ForceStrictPrecision",
	"back.FuseTransposesSequence",
	"back.GatherNormalizer",
	"back.InterpolateReshape",
	"back.LRNToNorm",
	"back.LayoutChangeForGatherND",
	"back.LeakyReLUMutation",
	"back.LinearToLinearONNXReplacer",
	"back.MarkNodesWithShapeValues",
	"back.MatMulNormalizer",
	"back.MaxPool",
	"back.NormalizeToNormalizeL2",
	"back.OptimizeTransposeReshapeSequence",
	"back.PackBinaryWeights",
	"back.ProposalMutation",
	"back.RNNSequenceTypeRename",
	"back.ReduceMerge",
	"back.ReduceTransposeDimensions",
	"back.RemoveUselessConvert",
	"back.ReshapeMutation",
	"back.ResultNormalizer",
	"back.ResultRename",
	"back.ReverseInputChannels",
	"back.SelectBroadcast",
	"back.ShapeOfConstFolding",
	"back.ShuffleChannelPatternOptimization",
	"back.SpecialNodesFinalization",
	"back.StridedSliceMasksNormalizer",
	"back.TopKNormalizer",
	"back.TransposeDFT",
	"back.TransposeReduceFusing",
	"back.UselessConcatRemoval",
	"back.add_outputs_recursive",
	"back.blob_normalizer",
	"back.compress_quantized_weights",
	"back.ie_ir_ver_2",
	"back.insert_compatibility_l2normalization",
	"back.kaldi_remove_memory_output",
	"back.names_uniqueness_check",
	"back.offline_transformations",
	"back.op_versioning",
	"back.pass_separator",
	"back.preprocessing",
	"back.priorbox_mutation",
	"back.remove_last_softmax_pattern",
	"back.replacement",
	"load.onnx.loader",
	"front.onnx.AttributedSliceToSlice",
	"front.onnx.CTCGreedyDecoder_ext",
	"front.onnx.LoopNormalize",
	"front.onnx.MvnOnnxToMvn",
	"front.onnx.ONNXResize10ToInterpolate",
	"front.onnx.activation_ext",
	"front.onnx.affine_ext",
	"front.onnx.argmax_ext",
	"front.onnx.argmin_ext",
	"front.onnx.aten_ext",
	"front.onnx.cast_ext",
	"front.onnx.clip_ext",
	"front.onnx.concat_ext",
	"front.onnx.const_ext",
	"front.onnx.constant_fill_ext",
	"front.onnx.constant_of_shape_ext",
	"front.onnx.constant_of_shape_to_broadcast",
	"front.onnx.conv_ext",
	"front.onnx.crop_ext",
	"front.onnx.cumsum_ext",
	"front.onnx.deformable_conv_ext",
	"front.onnx.depth_to_space_ext",
	"front.onnx.dequantize_linear_ext",
	"front.onnx.detection_output",
	"front.onnx.detection_output_ext",
	"front.onnx.detection_output_onnx_ext",
	"front.onnx.dropout_ext",
	"front.onnx.einsum_ext",
	"front.onnx.elementwise_ext",
	"front.onnx.expand_ext",
	"front.onnx.extractor",
	"front.onnx.extractors",
	"front.onnx.flattenONNX_to_reshape",
	"front.onnx.flatten_ext",
	"front.onnx.fused_bn_ext",
	"front.onnx.gather_ext",
	"front.onnx.gatherelements_ext",
	"front.onnx.gathernd_ext",
	"front.onnx.gemm_ext",
	"front.onnx.group_norm_ext",
	"front.onnx.gru_ext",
	"front.onnx.hard_sigmoid_ext",
	"front.onnx.identity_ext",
	"front.onnx.image_scaler_ext",
	"front.onnx.instance_normalization_ext",
	"front.onnx.loader",
	"front.onnx.logsoftmaxONNX_to_logsoftmax",
	"front.onnx.loop_ext",
	"front.onnx.lp_normalization_ext",
	"front.onnx.lrn_ext",
	"front.onnx.lstm_ext",
	"front.onnx.mask_rcnn_conversion",
	"front.onnx.matmul_ext",
	"front.onnx.mean_variance_normalization_ext",
	"front.onnx.non_max_suppression_ext",
	"front.onnx.non_zero_ext",
	"front.onnx.normalize_ext",
	"front.onnx.normalize_l2_normalize",
	"front.onnx.one_hot_ext",
	"front.onnx.one_hot_normalize",
	"front.onnx.pad_converter",
	"front.onnx.pad_ext",
	"front.onnx.parameter_ext",
	"front.onnx.person_detection_crossroad_conversion",
	"front.onnx.pooling_ext",
	"front.onnx.priorbox_clustered_ext",
	"front.onnx.priorbox_ext",
	"front.onnx.priorgridgenerator_ext",
	"front.onnx.proposal_ext",
	"front.onnx.quantize_ext",
	"front.onnx.quantize_linear_ext",
	"front.onnx.random_uniform_ext",
	"front.onnx.range_ext",
	"front.onnx.reduce_ext",
	"front.onnx.register_custom_ops",
	"front.onnx.reshape_ext",
	"front.onnx.resize_ext",
	"front.onnx.reverse_sequence_ext",
	"front.onnx.rnn_ext",
	"front.onnx.roialign_ext",
	"front.onnx.roifeatureextractor_ext",
	"front.onnx.scatter_ext",
	"front.onnx.shape_ext",
	"front.onnx.size_ext",
	"front.onnx.slice_ext",
	"front.onnx.softmaxONNX_to_softmax",
	"front.onnx.softmax_ext",
	"front.onnx.softplus_ext",
	"front.onnx.space_to_depth_ext",
	"front.onnx.split_ext",
	"front.onnx.squeeze_ext",
	"front.onnx.top_k_ext",
	"front.onnx.topkrois_ext",
	"front.onnx.transpose_ext",
	"front.onnx.unsqueeze_ext",
	"front.onnx.upsample_ext",
	"front.onnx.where_ext",
	"front.onnx.extractors.utils",
	],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
mo_pyz = PYZ(mo_a.pure, mo_a.zipped_data, cipher=block_cipher)
mo_exe = EXE(
    mo_pyz,
    mo_a.scripts,
    [],
    exclude_binaries=True,
    name='mo',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
	contents_directory='.'
)
cw_a = Analysis(
    ['convert_weights\\convert_weights.py'],
    pathex=['convert_weights'],
    datas=[],
    binaries=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
cw_pyz = PYZ(cw_a.pure, cw_a.zipped_data, cipher=block_cipher)
cw_exe = EXE(
    cw_pyz,
    cw_a.scripts,
    [],
    exclude_binaries=True,
    name='convert_weights',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
	contents_directory='.'
)

MERGE((mo_a, 'mo', 'mo'), (cw_a, 'cw', 'cw'))

coll = COLLECT(
    mo_exe,
	mo_a.binaries,
    mo_a.zipfiles,
    mo_a.datas,
	
	cw_exe,
    cw_a.binaries,
    cw_a.zipfiles,
    cw_a.datas,
    strip=False,
	
    upx=True,
    upx_exclude=[],
    name='mo',
)