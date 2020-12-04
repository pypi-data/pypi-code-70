# Copyright 2020 The TensorFlow Authors. All Rights Reserved.
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
"""Utilities for model specification."""

import tensorflow as tf


def dict_with_default(default_dict, **updates):
  default_dict.update(updates)
  return default_dict


def create_int_feature(values):
  feature = tf.train.Feature(int64_list=tf.train.Int64List(value=list(values)))
  return feature


def get_num_gpus(num_gpus):
  try:
    tot_num_gpus = len(tf.config.experimental.list_physical_devices('GPU'))
  except (tf.errors.NotFoundError, tf.errors.InternalError):
    tot_num_gpus = max(0, num_gpus)
  if num_gpus > tot_num_gpus or num_gpus == -1:
    num_gpus = tot_num_gpus
  return num_gpus
