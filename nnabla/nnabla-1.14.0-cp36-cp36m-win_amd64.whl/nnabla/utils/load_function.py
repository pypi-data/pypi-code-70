# Copyright (c) 2017 Sony Corporation. All Rights Reserved.
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# *WARNING*
# THIS FILE IS AUTO-GENERATED BY CODE GENERATOR.
# PLEASE DO NOT EDIT THIS FILE BY HAND!
# If you want to modify this file, edit following files.
# - build-tools/code_generator/generator/generate_python_src_nnabla_utils_load_function_py.py
# - build-tools/code_generator/templates/python_src_nnabla_utils_load_function_py_template.py
'''
.. note::
    This module is auto-generated from

    - :file:`utils/load_function.py.tmpl`
    - :file:`build-tools/code_generator/generate.py`
'''


import nnabla.function as F


def _create_function_instance(ctx, f):
    function = None
    if f.type == 'Affine':
        function = F.Affine(
            ctx,
            base_axis=f.affine_param.base_axis,
            )
    elif f.type == 'RNN':
        function = F.RNN(
            ctx,
            num_layers=f.rnn_param.num_layers,
            nonlinearity=f.rnn_param.nonlinearity,
            dropout=f.rnn_param.dropout,
            bidirectional=f.rnn_param.bidirectional,
            training=f.rnn_param.training,
            )
    elif f.type == 'LSTM':
        function = F.LSTM(
            ctx,
            num_layers=f.lstm_param.num_layers,
            dropout=f.lstm_param.dropout,
            bidirectional=f.lstm_param.bidirectional,
            training=f.lstm_param.training,
            )
    elif f.type == 'GRU':
        function = F.GRU(
            ctx,
            num_layers=f.gru_param.num_layers,
            dropout=f.gru_param.dropout,
            bidirectional=f.gru_param.bidirectional,
            training=f.gru_param.training,
            )
    elif f.type == 'Convolution':
        function = F.Convolution(
            ctx,
            base_axis=f.convolution_param.base_axis,
            pad=f.convolution_param.pad.dim,
            stride=f.convolution_param.stride.dim,
            dilation=f.convolution_param.dilation.dim,
            group=f.convolution_param.group,
            channel_last=f.convolution_param.channel_last,
            )
    elif f.type == 'FusedConvolution':
        function = F.FusedConvolution(
            ctx,
            base_axis=f.fused_convolution_param.base_axis,
            pad=f.fused_convolution_param.pad.dim,
            stride=f.fused_convolution_param.stride.dim,
            dilation=f.fused_convolution_param.dilation.dim,
            group=f.fused_convolution_param.group,
            channel_last=f.fused_convolution_param.channel_last,
            decay_rate=f.fused_convolution_param.decay_rate,
            eps=f.fused_convolution_param.eps,
            batch_stat=f.fused_convolution_param.batch_stat,
            nonlinearity=f.fused_convolution_param.nonlinearity,
            nonlinearity_args=f.fused_convolution_param.nonlinearity_args,
            )
    elif f.type == 'DepthwiseConvolution':
        function = F.DepthwiseConvolution(
            ctx,
            base_axis=f.depthwise_convolution_param.base_axis,
            pad=f.depthwise_convolution_param.pad.dim,
            stride=f.depthwise_convolution_param.stride.dim,
            dilation=f.depthwise_convolution_param.dilation.dim,
            multiplier=f.depthwise_convolution_param.multiplier,
            )
    elif f.type == 'Deconvolution':
        function = F.Deconvolution(
            ctx,
            base_axis=f.deconvolution_param.base_axis,
            pad=f.deconvolution_param.pad.dim,
            stride=f.deconvolution_param.stride.dim,
            dilation=f.deconvolution_param.dilation.dim,
            group=f.deconvolution_param.group,
            channel_last=f.deconvolution_param.channel_last,
            output_padding=f.deconvolution_param.output_padding.dim,
            )
    elif f.type == 'DepthwiseDeconvolution':
        function = F.DepthwiseDeconvolution(
            ctx,
            base_axis=f.depthwise_deconvolution_param.base_axis,
            pad=f.depthwise_deconvolution_param.pad.dim,
            stride=f.depthwise_deconvolution_param.stride.dim,
            dilation=f.depthwise_deconvolution_param.dilation.dim,
            divisor=f.depthwise_deconvolution_param.divisor,
            )
    elif f.type == 'AdaptiveSeparableConvolution':
        function = F.AdaptiveSeparableConvolution(
            ctx,
            )
    elif f.type == 'MaxPooling':
        function = F.MaxPooling(
            ctx,
            kernel=f.max_pooling_param.kernel.dim,
            stride=f.max_pooling_param.stride.dim,
            ignore_border=f.max_pooling_param.ignore_border,
            pad=f.max_pooling_param.pad.dim,
            channel_last=f.max_pooling_param.channel_last,
            )
    elif f.type == 'AveragePooling':
        function = F.AveragePooling(
            ctx,
            kernel=f.average_pooling_param.kernel.dim,
            stride=f.average_pooling_param.stride.dim,
            ignore_border=f.average_pooling_param.ignore_border,
            pad=f.average_pooling_param.pad.dim,
            channel_last=f.average_pooling_param.channel_last,
            including_pad=f.average_pooling_param.including_pad,
            )
    elif f.type == 'GlobalAveragePooling':
        function = F.GlobalAveragePooling(
            ctx,
            )
    elif f.type == 'SumPooling':
        function = F.SumPooling(
            ctx,
            kernel=f.sum_pooling_param.kernel.dim,
            stride=f.sum_pooling_param.stride.dim,
            ignore_border=f.sum_pooling_param.ignore_border,
            pad=f.sum_pooling_param.pad.dim,
            channel_last=f.sum_pooling_param.channel_last,
            )
    elif f.type == 'Unpooling':
        function = F.Unpooling(
            ctx,
            kernel=f.unpooling_param.kernel.dim,
            channel_last=f.unpooling_param.channel_last,
            )
    elif f.type == 'Embed':
        function = F.Embed(
            ctx,
            )
    elif f.type == 'Sigmoid':
        function = F.Sigmoid(
            ctx,
            )
    elif f.type == 'Swish':
        function = F.Swish(
            ctx,
            )
    elif f.type == 'Tanh':
        function = F.Tanh(
            ctx,
            )
    elif f.type == 'ReLU':
        function = F.ReLU(
            ctx,
            inplace=f.relu_param.inplace,
            )
    elif f.type == 'LeakyReLU':
        function = F.LeakyReLU(
            ctx,
            alpha=f.leaky_relu_param.alpha,
            inplace=f.leaky_relu_param.inplace,
            )
    elif f.type == 'Softmax':
        function = F.Softmax(
            ctx,
            axis=f.softmax_param.axis,
            )
    elif f.type == 'LogSoftmax':
        function = F.LogSoftmax(
            ctx,
            axis=f.log_softmax_param.axis,
            )
    elif f.type == 'ELU':
        function = F.ELU(
            ctx,
            alpha=f.elu_param.alpha,
            )
    elif f.type == 'SELU':
        function = F.SELU(
            ctx,
            scale=f.selu_param.scale,
            alpha=f.selu_param.alpha,
            )
    elif f.type == 'CReLU':
        function = F.CReLU(
            ctx,
            axis=f.crelu_param.axis,
            )
    elif f.type == 'CELU':
        function = F.CELU(
            ctx,
            alpha=f.celu_param.alpha,
            axis=f.celu_param.axis,
            )
    elif f.type == 'PReLU':
        function = F.PReLU(
            ctx,
            base_axis=f.prelu_param.base_axis,
            )
    elif f.type == 'GELU':
        function = F.GELU(
            ctx,
            )
    elif f.type == 'Mish':
        function = F.Mish(
            ctx,
            )
    elif f.type == 'ReLU6':
        function = F.ReLU6(
            ctx,
            )
    elif f.type == 'HardSigmoid':
        function = F.HardSigmoid(
            ctx,
            )
    elif f.type == 'HardTanh':
        function = F.HardTanh(
            ctx,
            )
    elif f.type == 'LogSigmoid':
        function = F.LogSigmoid(
            ctx,
            )
    elif f.type == 'SoftPlus':
        function = F.SoftPlus(
            ctx,
            )
    elif f.type == 'SoftSign':
        function = F.SoftSign(
            ctx,
            )
    elif f.type == 'TanhShrink':
        function = F.TanhShrink(
            ctx,
            )
    elif f.type == 'Sinc':
        function = F.Sinc(
            ctx,
            )
    elif f.type == 'FusedBatchNormalization':
        function = F.FusedBatchNormalization(
            ctx,
            axes=f.fused_batch_normalization_param.axes,
            decay_rate=f.fused_batch_normalization_param.decay_rate,
            eps=f.fused_batch_normalization_param.eps,
            batch_stat=f.fused_batch_normalization_param.batch_stat,
            nonlinearity=f.fused_batch_normalization_param.nonlinearity,
            )
    elif f.type == 'BatchNormalization':
        function = F.BatchNormalization(
            ctx,
            axes=f.batch_normalization_param.axes,
            decay_rate=f.batch_normalization_param.decay_rate,
            eps=f.batch_normalization_param.eps,
            batch_stat=f.batch_normalization_param.batch_stat,
            )
    elif f.type == 'NormNormalization':
        function = F.NormNormalization(
            ctx,
            p=f.norm_normalization_param.p,
            axes=f.norm_normalization_param.axes,
            eps=f.norm_normalization_param.eps,
            )
    elif f.type == 'SyncBatchNormalization':
        function = F.SyncBatchNormalization(
            ctx,
            comm=f.sync_batch_normalization_param.comm,
            group=f.sync_batch_normalization_param.group,
            axes=f.sync_batch_normalization_param.axes,
            decay_rate=f.sync_batch_normalization_param.decay_rate,
            eps=f.sync_batch_normalization_param.eps,
            batch_stat=f.sync_batch_normalization_param.batch_stat,
            )
    elif f.type == 'WeightNormalization':
        function = F.WeightNormalization(
            ctx,
            dim=f.weight_normalization_param.dim,
            eps=f.weight_normalization_param.eps,
            )
    elif f.type == 'MeanSubtraction':
        function = F.MeanSubtraction(
            ctx,
            base_axis=f.mean_subtraction_param.base_axis,
            update_running_mean=f.mean_subtraction_param.update_running_mean,
            )
    elif f.type == 'ClipGradByValue':
        function = F.ClipGradByValue(
            ctx,
            )
    elif f.type == 'ClipGradByNorm':
        function = F.ClipGradByNorm(
            ctx,
            clip_norm=f.clip_grad_by_norm_param.clip_norm,
            axes=f.clip_grad_by_norm_param.axes,
            )
    elif f.type == 'Sum':
        function = F.Sum(
            ctx,
            axes=f.sum_param.axes,
            keep_dims=f.sum_param.keep_dims,
            )
    elif f.type == 'Mean':
        function = F.Mean(
            ctx,
            axes=f.mean_param.axes,
            keep_dims=f.mean_param.keep_dims,
            )
    elif f.type == 'Max':
        function = F.Max(
            ctx,
            axes=f.max_param.axes,
            keep_dims=f.max_param.keep_dims,
            with_index=f.max_param.with_index,
            only_index=f.max_param.only_index,
            )
    elif f.type == 'Min':
        function = F.Min(
            ctx,
            axes=f.min_param.axes,
            keep_dims=f.min_param.keep_dims,
            with_index=f.min_param.with_index,
            only_index=f.min_param.only_index,
            )
    elif f.type == 'Norm':
        function = F.Norm(
            ctx,
            p=f.norm_param.p,
            axes=f.norm_param.axes,
            keep_dims=f.norm_param.keep_dims,
            )
    elif f.type == 'Prod':
        function = F.Prod(
            ctx,
            axes=f.prod_param.axes,
            keep_dims=f.prod_param.keep_dims,
            )
    elif f.type == 'ReduceSum':
        function = F.ReduceSum(
            ctx,
            )
    elif f.type == 'ReduceMean':
        function = F.ReduceMean(
            ctx,
            )
    elif f.type == 'Add2':
        function = F.Add2(
            ctx,
            inplace=f.add2_param.inplace,
            )
    elif f.type == 'AddN':
        function = F.AddN(
            ctx,
            )
    elif f.type == 'BcAdd2':
        function = F.BcAdd2(
            ctx,
            inplace=f.bc_add2_param.inplace,
            )
    elif f.type == 'Sub2':
        function = F.Sub2(
            ctx,
            inplace=f.sub2_param.inplace,
            )
    elif f.type == 'Mul2':
        function = F.Mul2(
            ctx,
            inplace=f.mul2_param.inplace,
            )
    elif f.type == 'MulN':
        function = F.MulN(
            ctx,
            )
    elif f.type == 'Div2':
        function = F.Div2(
            ctx,
            inplace=f.div2_param.inplace,
            )
    elif f.type == 'Pow2':
        function = F.Pow2(
            ctx,
            inplace=f.pow2_param.inplace,
            )
    elif f.type == 'AddScalar':
        function = F.AddScalar(
            ctx,
            val=f.add_scalar_param.val,
            inplace=f.add_scalar_param.inplace,
            )
    elif f.type == 'MulScalar':
        function = F.MulScalar(
            ctx,
            val=f.mul_scalar_param.val,
            inplace=f.mul_scalar_param.inplace,
            )
    elif f.type == 'PowScalar':
        function = F.PowScalar(
            ctx,
            val=f.pow_scalar_param.val,
            inplace=f.pow_scalar_param.inplace,
            )
    elif f.type == 'RSubScalar':
        function = F.RSubScalar(
            ctx,
            val=f.r_sub_scalar_param.val,
            )
    elif f.type == 'RDivScalar':
        function = F.RDivScalar(
            ctx,
            val=f.r_div_scalar_param.val,
            )
    elif f.type == 'RPowScalar':
        function = F.RPowScalar(
            ctx,
            val=f.r_pow_scalar_param.val,
            )
    elif f.type == 'Sign':
        function = F.Sign(
            ctx,
            alpha=f.sign_param.alpha,
            )
    elif f.type == 'Minimum2':
        function = F.Minimum2(
            ctx,
            )
    elif f.type == 'Maximum2':
        function = F.Maximum2(
            ctx,
            )
    elif f.type == 'MinimumScalar':
        function = F.MinimumScalar(
            ctx,
            val=f.minimum_scalar_param.val,
            )
    elif f.type == 'MaximumScalar':
        function = F.MaximumScalar(
            ctx,
            val=f.maximum_scalar_param.val,
            )
    elif f.type == 'LogicalAnd':
        function = F.LogicalAnd(
            ctx,
            )
    elif f.type == 'LogicalOr':
        function = F.LogicalOr(
            ctx,
            )
    elif f.type == 'LogicalXor':
        function = F.LogicalXor(
            ctx,
            )
    elif f.type == 'Equal':
        function = F.Equal(
            ctx,
            )
    elif f.type == 'NotEqual':
        function = F.NotEqual(
            ctx,
            )
    elif f.type == 'GreaterEqual':
        function = F.GreaterEqual(
            ctx,
            )
    elif f.type == 'Greater':
        function = F.Greater(
            ctx,
            )
    elif f.type == 'LessEqual':
        function = F.LessEqual(
            ctx,
            )
    elif f.type == 'Less':
        function = F.Less(
            ctx,
            )
    elif f.type == 'LogicalAndScalar':
        function = F.LogicalAndScalar(
            ctx,
            val=f.logical_and_scalar_param.val,
            )
    elif f.type == 'LogicalOrScalar':
        function = F.LogicalOrScalar(
            ctx,
            val=f.logical_or_scalar_param.val,
            )
    elif f.type == 'LogicalXorScalar':
        function = F.LogicalXorScalar(
            ctx,
            val=f.logical_xor_scalar_param.val,
            )
    elif f.type == 'EqualScalar':
        function = F.EqualScalar(
            ctx,
            val=f.equal_scalar_param.val,
            )
    elif f.type == 'NotEqualScalar':
        function = F.NotEqualScalar(
            ctx,
            val=f.not_equal_scalar_param.val,
            )
    elif f.type == 'GreaterEqualScalar':
        function = F.GreaterEqualScalar(
            ctx,
            val=f.greater_equal_scalar_param.val,
            )
    elif f.type == 'GreaterScalar':
        function = F.GreaterScalar(
            ctx,
            val=f.greater_scalar_param.val,
            )
    elif f.type == 'LessEqualScalar':
        function = F.LessEqualScalar(
            ctx,
            val=f.less_equal_scalar_param.val,
            )
    elif f.type == 'LessScalar':
        function = F.LessScalar(
            ctx,
            val=f.less_scalar_param.val,
            )
    elif f.type == 'LogicalNot':
        function = F.LogicalNot(
            ctx,
            )
    elif f.type == 'IsNaN':
        function = F.IsNaN(
            ctx,
            )
    elif f.type == 'IsInf':
        function = F.IsInf(
            ctx,
            )
    elif f.type == 'ResetNaN':
        function = F.ResetNaN(
            ctx,
            val=f.reset_nan_param.val,
            )
    elif f.type == 'ResetInf':
        function = F.ResetInf(
            ctx,
            val=f.reset_inf_param.val,
            )
    elif f.type == 'Where':
        function = F.Where(
            ctx,
            )
    elif f.type == 'Constant':
        function = F.Constant(
            ctx,
            val=f.constant_param.val,
            shape=f.constant_param.shape.dim,
            )
    elif f.type == 'Arange':
        function = F.Arange(
            ctx,
            start=f.arange_param.start,
            stop=f.arange_param.stop,
            step=f.arange_param.step,
            )
    elif f.type == 'Abs':
        function = F.Abs(
            ctx,
            )
    elif f.type == 'Exp':
        function = F.Exp(
            ctx,
            )
    elif f.type == 'Log':
        function = F.Log(
            ctx,
            )
    elif f.type == 'Identity':
        function = F.Identity(
            ctx,
            )
    elif f.type == 'BatchMatmul':
        function = F.BatchMatmul(
            ctx,
            transpose_a=f.batch_matmul_param.transpose_a,
            transpose_b=f.batch_matmul_param.transpose_b,
            )
    elif f.type == 'Round':
        function = F.Round(
            ctx,
            )
    elif f.type == 'Ceil':
        function = F.Ceil(
            ctx,
            )
    elif f.type == 'Floor':
        function = F.Floor(
            ctx,
            )
    elif f.type == 'Sin':
        function = F.Sin(
            ctx,
            )
    elif f.type == 'Cos':
        function = F.Cos(
            ctx,
            )
    elif f.type == 'Tan':
        function = F.Tan(
            ctx,
            )
    elif f.type == 'Sinh':
        function = F.Sinh(
            ctx,
            )
    elif f.type == 'Cosh':
        function = F.Cosh(
            ctx,
            )
    elif f.type == 'ASin':
        function = F.ASin(
            ctx,
            )
    elif f.type == 'ACos':
        function = F.ACos(
            ctx,
            )
    elif f.type == 'ATan':
        function = F.ATan(
            ctx,
            )
    elif f.type == 'ATan2':
        function = F.ATan2(
            ctx,
            )
    elif f.type == 'ASinh':
        function = F.ASinh(
            ctx,
            )
    elif f.type == 'ACosh':
        function = F.ACosh(
            ctx,
            )
    elif f.type == 'ATanh':
        function = F.ATanh(
            ctx,
            )
    elif f.type == 'Concatenate':
        function = F.Concatenate(
            ctx,
            axis=f.concatenate_param.axis,
            )
    elif f.type == 'Split':
        function = F.Split(
            ctx,
            axis=f.split_param.axis,
            )
    elif f.type == 'Stack':
        function = F.Stack(
            ctx,
            axis=f.stack_param.axis,
            )
    elif f.type == 'Slice':
        function = F.Slice(
            ctx,
            start=f.slice_param.start,
            stop=f.slice_param.stop,
            step=f.slice_param.step,
            )
    elif f.type == 'Pad':
        function = F.Pad(
            ctx,
            pad_width=f.pad_param.pad_width,
            mode=f.pad_param.mode,
            constant_value=f.pad_param.constant_value,
            )
    elif f.type == 'Transpose':
        function = F.Transpose(
            ctx,
            axes=f.transpose_param.axes,
            )
    elif f.type == 'Broadcast':
        function = F.Broadcast(
            ctx,
            shape=f.broadcast_param.shape.dim,
            )
    elif f.type == 'BroadcastTo':
        function = F.BroadcastTo(
            ctx,
            axis=f.broadcast_to_param.axis,
            )
    elif f.type == 'Tile':
        function = F.Tile(
            ctx,
            reps=f.tile_param.reps,
            )
    elif f.type == 'OneHot':
        function = F.OneHot(
            ctx,
            shape=f.one_hot_param.shape.dim,
            )
    elif f.type == 'Flip':
        function = F.Flip(
            ctx,
            axes=f.flip_param.axes,
            )
    elif f.type == 'Shift':
        function = F.Shift(
            ctx,
            shifts=f.shift_param.shifts,
            border_mode=f.shift_param.border_mode,
            )
    elif f.type == 'Sort':
        function = F.Sort(
            ctx,
            axis=f.sort_param.axis,
            reverse=f.sort_param.reverse,
            with_index=f.sort_param.with_index,
            only_index=f.sort_param.only_index,
            )
    elif f.type == 'Reshape':
        function = F.Reshape(
            ctx,
            shape=f.reshape_param.shape.dim,
            inplace=f.reshape_param.inplace,
            )
    elif f.type == 'MatrixDiag':
        function = F.MatrixDiag(
            ctx,
            )
    elif f.type == 'MatrixDiagPart':
        function = F.MatrixDiagPart(
            ctx,
            )
    elif f.type == 'BatchInv':
        function = F.BatchInv(
            ctx,
            )
    elif f.type == 'BatchDet':
        function = F.BatchDet(
            ctx,
            )
    elif f.type == 'Assign':
        function = F.Assign(
            ctx,
            )
    elif f.type == 'Gather':
        function = F.Gather(
            ctx,
            axis=f.gather_param.axis,
            batch_dims=f.gather_param.batch_dims,
            )
    elif f.type == 'GatherNd':
        function = F.GatherNd(
            ctx,
            )
    elif f.type == 'ScatterNd':
        function = F.ScatterNd(
            ctx,
            shape=f.scatter_nd_param.shape,
            )
    elif f.type == 'ScatterAdd':
        function = F.ScatterAdd(
            ctx,
            axis=f.scatter_add_param.axis,
            )
    elif f.type == 'PackPaddedSequence':
        function = F.PackPaddedSequence(
            ctx,
            batch_first=f.pack_padded_sequence_param.batch_first,
            )
    elif f.type == 'PadPackedSequence':
        function = F.PadPackedSequence(
            ctx,
            batch_first=f.pad_packed_sequence_param.batch_first,
            padding_value=f.pad_packed_sequence_param.padding_value,
            total_length=f.pad_packed_sequence_param.total_length,
            )
    elif f.type == 'Interpolate':
        function = F.Interpolate(
            ctx,
            output_size=f.interpolate_param.output_size,
            mode=f.interpolate_param.mode,
            align_corners=f.interpolate_param.align_corners,
            half_pixel=f.interpolate_param.half_pixel,
            half_pixel_for_nn=f.interpolate_param.half_pixel_for_nn,
            channel_last=f.interpolate_param.channel_last,
            )
    elif f.type == 'FFT':
        function = F.FFT(
            ctx,
            signal_ndim=f.fft_param.signal_ndim,
            normalized=f.fft_param.normalized,
            )
    elif f.type == 'IFFT':
        function = F.IFFT(
            ctx,
            signal_ndim=f.ifft_param.signal_ndim,
            normalized=f.ifft_param.normalized,
            )
    elif f.type == 'Dropout':
        function = F.Dropout(
            ctx,
            p=f.dropout_param.p,
            seed=f.dropout_param.seed,
            )
    elif f.type == 'TopKData':
        function = F.TopKData(
            ctx,
            k=f.top_k_data_param.k,
            abs=f.top_k_data_param.abs,
            reduce=f.top_k_data_param.reduce,
            base_axis=f.top_k_data_param.base_axis,
            )
    elif f.type == 'TopKGrad':
        function = F.TopKGrad(
            ctx,
            k=f.top_k_grad_param.k,
            abs=f.top_k_grad_param.abs,
            base_axis=f.top_k_grad_param.base_axis,
            )
    elif f.type == 'Rand':
        function = F.Rand(
            ctx,
            low=f.rand_param.low,
            high=f.rand_param.high,
            shape=f.rand_param.shape.dim,
            seed=f.rand_param.seed,
            )
    elif f.type == 'Randint':
        function = F.Randint(
            ctx,
            low=f.randint_param.low,
            high=f.randint_param.high,
            shape=f.randint_param.shape.dim,
            seed=f.randint_param.seed,
            )
    elif f.type == 'Randn':
        function = F.Randn(
            ctx,
            mu=f.randn_param.mu,
            sigma=f.randn_param.sigma,
            shape=f.randn_param.shape.dim,
            seed=f.randn_param.seed,
            )
    elif f.type == 'RandBinomial':
        function = F.RandBinomial(
            ctx,
            n=f.rand_binomial_param.n,
            p=f.rand_binomial_param.p,
            shape=f.rand_binomial_param.shape.dim,
            seed=f.rand_binomial_param.seed,
            )
    elif f.type == 'RandBeta':
        function = F.RandBeta(
            ctx,
            alpha=f.rand_beta_param.alpha,
            beta=f.rand_beta_param.beta,
            shape=f.rand_beta_param.shape.dim,
            seed=f.rand_beta_param.seed,
            )
    elif f.type == 'RandGamma':
        function = F.RandGamma(
            ctx,
            k=f.rand_gamma_param.k,
            theta=f.rand_gamma_param.theta,
            shape=f.rand_gamma_param.shape.dim,
            seed=f.rand_gamma_param.seed,
            )
    elif f.type == 'RandomChoice':
        function = F.RandomChoice(
            ctx,
            shape=f.random_choice_param.shape.dim,
            replace=f.random_choice_param.replace,
            seed=f.random_choice_param.seed,
            )
    elif f.type == 'RandomCrop':
        function = F.RandomCrop(
            ctx,
            shape=f.random_crop_param.shape.dim,
            base_axis=f.random_crop_param.base_axis,
            seed=f.random_crop_param.seed,
            )
    elif f.type == 'RandomFlip':
        function = F.RandomFlip(
            ctx,
            axes=f.random_flip_param.axes,
            base_axis=f.random_flip_param.base_axis,
            seed=f.random_flip_param.seed,
            )
    elif f.type == 'RandomShift':
        function = F.RandomShift(
            ctx,
            shifts=f.random_shift_param.shifts,
            border_mode=f.random_shift_param.border_mode,
            base_axis=f.random_shift_param.base_axis,
            seed=f.random_shift_param.seed,
            )
    elif f.type == 'RandomErase':
        function = F.RandomErase(
            ctx,
            prob=f.random_erase_param.prob,
            area_ratios=f.random_erase_param.area_ratios,
            aspect_ratios=f.random_erase_param.aspect_ratios,
            replacements=f.random_erase_param.replacements,
            n=f.random_erase_param.n,
            share=f.random_erase_param.share,
            inplace=f.random_erase_param.inplace,
            base_axis=f.random_erase_param.base_axis,
            seed=f.random_erase_param.seed,
            channel_last=f.random_erase_param.channel_last,
            ste_fine_grained=f.random_erase_param.ste_fine_grained,
            )
    elif f.type == 'ImageAugmentation':
        function = F.ImageAugmentation(
            ctx,
            shape=f.image_augmentation_param.shape.dim,
            pad=f.image_augmentation_param.pad.dim,
            min_scale=f.image_augmentation_param.min_scale,
            max_scale=f.image_augmentation_param.max_scale,
            angle=f.image_augmentation_param.angle,
            aspect_ratio=f.image_augmentation_param.aspect_ratio,
            distortion=f.image_augmentation_param.distortion,
            flip_lr=f.image_augmentation_param.flip_lr,
            flip_ud=f.image_augmentation_param.flip_ud,
            brightness=f.image_augmentation_param.brightness,
            brightness_each=f.image_augmentation_param.brightness_each,
            contrast=f.image_augmentation_param.contrast,
            contrast_center=f.image_augmentation_param.contrast_center,
            contrast_each=f.image_augmentation_param.contrast_each,
            noise=f.image_augmentation_param.noise,
            seed=f.image_augmentation_param.seed,
            )
    elif f.type == 'SigmoidCrossEntropy':
        function = F.SigmoidCrossEntropy(
            ctx,
            )
    elif f.type == 'BinaryCrossEntropy':
        function = F.BinaryCrossEntropy(
            ctx,
            )
    elif f.type == 'SoftmaxCrossEntropy':
        function = F.SoftmaxCrossEntropy(
            ctx,
            axis=f.softmax_cross_entropy_param.axis,
            )
    elif f.type == 'CategoricalCrossEntropy':
        function = F.CategoricalCrossEntropy(
            ctx,
            axis=f.categorical_cross_entropy_param.axis,
            )
    elif f.type == 'SquaredError':
        function = F.SquaredError(
            ctx,
            )
    elif f.type == 'AbsoluteError':
        function = F.AbsoluteError(
            ctx,
            )
    elif f.type == 'HuberLoss':
        function = F.HuberLoss(
            ctx,
            delta=f.huber_loss_param.delta,
            )
    elif f.type == 'EpsilonInsensitiveLoss':
        function = F.EpsilonInsensitiveLoss(
            ctx,
            epsilon=f.epsilon_insensitive_loss_param.epsilon,
            )
    elif f.type == 'KLMultinomial':
        function = F.KLMultinomial(
            ctx,
            base_axis=f.kl_multinomial_param.base_axis,
            )
    elif f.type == 'AffineGrid':
        function = F.AffineGrid(
            ctx,
            size=f.affine_grid_param.size,
            align_corners=f.affine_grid_param.align_corners,
            )
    elif f.type == 'WarpByGrid':
        function = F.WarpByGrid(
            ctx,
            mode=f.warp_by_grid_param.mode,
            padding_mode=f.warp_by_grid_param.padding_mode,
            align_corners=f.warp_by_grid_param.align_corners,
            channel_last=f.warp_by_grid_param.channel_last,
            )
    elif f.type == 'WarpByFlow':
        function = F.WarpByFlow(
            ctx,
            )
    elif f.type == 'BinarySigmoid':
        function = F.BinarySigmoid(
            ctx,
            )
    elif f.type == 'BinaryTanh':
        function = F.BinaryTanh(
            ctx,
            )
    elif f.type == 'BinaryConnectAffine':
        function = F.BinaryConnectAffine(
            ctx,
            base_axis=f.binary_connect_affine_param.base_axis,
            quantize_zero_to=f.binary_connect_affine_param.quantize_zero_to,
            )
    elif f.type == 'BinaryConnectConvolution':
        function = F.BinaryConnectConvolution(
            ctx,
            base_axis=f.binary_connect_convolution_param.base_axis,
            pad=f.binary_connect_convolution_param.pad.dim,
            stride=f.binary_connect_convolution_param.stride.dim,
            dilation=f.binary_connect_convolution_param.dilation.dim,
            group=f.binary_connect_convolution_param.group,
            quantize_zero_to=f.binary_connect_convolution_param.quantize_zero_to,
            )
    elif f.type == 'BinaryWeightAffine':
        function = F.BinaryWeightAffine(
            ctx,
            base_axis=f.binary_weight_affine_param.base_axis,
            quantize_zero_to=f.binary_weight_affine_param.quantize_zero_to,
            )
    elif f.type == 'BinaryWeightConvolution':
        function = F.BinaryWeightConvolution(
            ctx,
            base_axis=f.binary_weight_convolution_param.base_axis,
            pad=f.binary_weight_convolution_param.pad.dim,
            stride=f.binary_weight_convolution_param.stride.dim,
            dilation=f.binary_weight_convolution_param.dilation.dim,
            group=f.binary_weight_convolution_param.group,
            quantize_zero_to=f.binary_weight_convolution_param.quantize_zero_to,
            )
    elif f.type == 'INQAffine':
        function = F.INQAffine(
            ctx,
            base_axis=f.inq_affine_param.base_axis,
            num_bits=f.inq_affine_param.num_bits,
            inq_iterations=f.inq_affine_param.inq_iterations,
            selection_algorithm=f.inq_affine_param.selection_algorithm,
            seed=f.inq_affine_param.seed,
            )
    elif f.type == 'INQConvolution':
        function = F.INQConvolution(
            ctx,
            base_axis=f.inq_convolution_param.base_axis,
            pad=f.inq_convolution_param.pad.dim,
            stride=f.inq_convolution_param.stride.dim,
            dilation=f.inq_convolution_param.dilation.dim,
            group=f.inq_convolution_param.group,
            num_bits=f.inq_convolution_param.num_bits,
            inq_iterations=f.inq_convolution_param.inq_iterations,
            selection_algorithm=f.inq_convolution_param.selection_algorithm,
            seed=f.inq_convolution_param.seed,
            )
    elif f.type == 'FixedPointQuantize':
        function = F.FixedPointQuantize(
            ctx,
            sign=f.fixed_point_quantize_param.sign,
            n=f.fixed_point_quantize_param.n,
            delta=f.fixed_point_quantize_param.delta,
            ste_fine_grained=f.fixed_point_quantize_param.ste_fine_grained,
            )
    elif f.type == 'MinMaxQuantize':
        function = F.MinMaxQuantize(
            ctx,
            decay=f.min_max_quantize_param.decay,
            x_min_max=f.min_max_quantize_param.x_min_max,
            ema=f.min_max_quantize_param.ema,
            ste_fine_grained=f.min_max_quantize_param.ste_fine_grained,
            eps=f.min_max_quantize_param.eps,
            )
    elif f.type == 'Pow2Quantize':
        function = F.Pow2Quantize(
            ctx,
            sign=f.pow2_quantize_param.sign,
            with_zero=f.pow2_quantize_param.with_zero,
            n=f.pow2_quantize_param.n,
            m=f.pow2_quantize_param.m,
            ste_fine_grained=f.pow2_quantize_param.ste_fine_grained,
            )
    elif f.type == 'Prune':
        function = F.Prune(
            ctx,
            rate=f.prune_param.rate,
            )
    elif f.type == 'QuantizeLinear':
        function = F.QuantizeLinear(
            ctx,
            round_mode=f.quantize_linear_param.round_mode,
            narrow_range=f.quantize_linear_param.narrow_range,
            dtype=f.quantize_linear_param.dtype,
            )
    elif f.type == 'DequantizeLinear':
        function = F.DequantizeLinear(
            ctx,
            )
    elif f.type == 'TopNError':
        function = F.TopNError(
            ctx,
            axis=f.top_n_error_param.axis,
            n=f.top_n_error_param.n,
            )
    elif f.type == 'BinaryError':
        function = F.BinaryError(
            ctx,
            )
    elif f.type == 'ConfusionMatrix':
        function = F.ConfusionMatrix(
            ctx,
            axis=f.confusion_matrix_param.axis,
            )
    elif f.type == 'VATNoise':
        function = F.VATNoise(
            ctx,
            base_axis=f.vat_noise_param.base_axis,
            eps=f.vat_noise_param.eps,
            )
    elif f.type == 'Unlink':
        function = F.Unlink(
            ctx,
            )
    elif f.type == 'Sink':
        function = F.Sink(
            ctx,
            one_input_grad=f.sink_param.one_input_grad,
            )
    elif f.type == 'NmsDetection2d':
        function = F.NmsDetection2d(
            ctx,
            thresh=f.nms_detection2d_param.thresh,
            nms=f.nms_detection2d_param.nms,
            nms_per_class=f.nms_detection2d_param.nms_per_class,
            )
    elif f.type == 'MaxPoolingBackward':
        function = F.MaxPoolingBackward(
            ctx,
            kernel=f.max_pooling_backward_param.kernel.dim,
            stride=f.max_pooling_backward_param.stride.dim,
            ignore_border=f.max_pooling_backward_param.ignore_border,
            pad=f.max_pooling_backward_param.pad.dim,
            channel_last=f.max_pooling_backward_param.channel_last,
            )
    elif f.type == 'PatchCorrelation':
        function = F.PatchCorrelation(
            ctx,
            patch=f.patch_correlation_param.patch.dim,
            shift=f.patch_correlation_param.shift.dim,
            patch_step=f.patch_correlation_param.patch_step.dim,
            shift_step=f.patch_correlation_param.shift_step.dim,
            padding=f.patch_correlation_param.padding.dim,
            )
    else:
        raise ValueError('Function "' + f.type + '" is not supported.')
    return function
