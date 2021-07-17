# !/usr/bin/env python
# -*- encoding: utf-8 -*-
# @File: vertify_convert_model.py
# @Time: 2021/01/05 16:49:06
# @Author: Max
import argparse

import numpy as np
import onnx
import onnxruntime

parser = argparse.ArgumentParser()
parser.add_argument('--onnx_path', type=str,
                    default='convert_model/general_mobile_v2_det_infer.onnx')
parser.add_argument('--type_model', choices=['rec', 'det', 'cls'], default='det')
args = parser.parse_args()
onnx_path = args.onnx_path

if args.type_model == 'det':
    onnx_model = onnx.load(onnx_path)
    onnx.checker.check_model(onnx_model)
    print(f'The {onnx_path} is checked!')

    onnx_model.graph.input[0].type.tensor_type.shape.dim[2].dim_param = '?'
    onnx_model.graph.input[0].type.tensor_type.shape.dim[3].dim_param = '?'
    onnx.save(onnx_model, onnx_path)

    x = np.random.rand(1, 3, 640, 480)
    session = onnxruntime.InferenceSession(onnx_path)
    onnx_inputs = {session.get_inputs()[0].name: x.astype(np.float32)}
    onnx_outputs = session.run(None, onnx_inputs)
    print('Inference is successful!')

elif args.type_model == 'rec':
    # 文本识别模型
    onnx_model = onnx.load(onnx_path)
    onnx.checker.check_model(onnx_model)
    print(f'The {onnx_path} is checked!')

    onnx_model.graph.input[0].type.tensor_type.shape.dim[2].dim_param = '?'
    onnx_model.graph.input[0].type.tensor_type.shape.dim[3].dim_param = '?'
    onnx.save(onnx_model, onnx_path)

    x = np.random.rand(1, 3, 32, 120)
    session = onnxruntime.InferenceSession(onnx_path)
    onnx_inputs = {session.get_inputs()[0].name: x.astype(np.float32)}
    onnx_outputs = session.run(None, onnx_inputs)
    print('Inference is successful!')

elif args.type_model == 'cls':
    # 方向分类模型
    onnx_model = onnx.load(onnx_path)
    onnx.checker.check_model(onnx_model)
    print(f'The {onnx_path} is checked!')

    onnx_model.graph.input[0].type.tensor_type.shape.dim[2].dim_param = '?'
    onnx_model.graph.input[0].type.tensor_type.shape.dim[3].dim_param = '?'
    onnx.save(onnx_model, onnx_path)

    x = np.random.rand(1, 3, 224, 224)
    session = onnxruntime.InferenceSession(onnx_path)
    onnx_inputs = {session.get_inputs()[0].name: x.astype(np.float32)}
    onnx_outputs = session.run(None, onnx_inputs)
    print('Inference is successful!')

else:
    raise ValueError(f'The {args.type_model} is not supported!')
