# Copyright 2017 Google Inc.
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

"""Tests for tensor2tensor.utils.metrics."""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

# Dependency imports

import numpy as np
from utils import metrics

import tensorflow as tf


class CommonLayersTest(tf.test.TestCase):

  def testAccuracyMetric(self):
    predictions = np.random.randint(1, 5, size=(12, 12, 12, 1))
    targets = np.random.randint(1, 5, size=(12, 12, 12, 1))
    expected = np.mean((predictions == targets).astype(float))
    with self.test_session() as session:
      scores, _ = metrics.padded_accuracy(
          tf.one_hot(predictions, depth=5, dtype=tf.float32),
          tf.constant(targets, dtype=tf.int32))
      a = tf.reduce_mean(scores)
      session.run(tf.global_variables_initializer())
      actual = session.run(a)
    self.assertAlmostEqual(actual, expected)

  def testAccuracyTopKMetric(self):
    predictions = np.random.randint(1, 5, size=(12, 12, 12, 1))
    targets = np.random.randint(1, 5, size=(12, 12, 12, 1))
    expected = np.mean((predictions == targets).astype(float))
    with self.test_session() as session:
      predicted = tf.one_hot(predictions, depth=5, dtype=tf.float32)
      scores1, _ = metrics.padded_accuracy_topk(
          predicted, tf.constant(targets, dtype=tf.int32), k=1)
      scores2, _ = metrics.padded_accuracy_topk(
          predicted, tf.constant(targets, dtype=tf.int32), k=7)
      a1 = tf.reduce_mean(scores1)
      a2 = tf.reduce_mean(scores2)
      session.run(tf.global_variables_initializer())
      actual1, actual2 = session.run([a1, a2])
    self.assertAlmostEqual(actual1, expected)
    self.assertAlmostEqual(actual2, 1.0)

  def testSequenceAccuracyMetric(self):
    predictions = np.random.randint(4, size=(12, 12, 12, 1))
    targets = np.random.randint(4, size=(12, 12, 12, 1))
    expected = np.mean(
        np.prod((predictions == targets).astype(float), axis=(1, 2)))
    with self.test_session() as session:
      scores, _ = metrics.padded_sequence_accuracy(
          tf.one_hot(predictions, depth=4, dtype=tf.float32),
          tf.constant(targets, dtype=tf.int32))
      a = tf.reduce_mean(scores)
      session.run(tf.global_variables_initializer())
      actual = session.run(a)
    self.assertEqual(actual, expected)

  def testNegativeLogPerplexity(self):
    predictions = np.random.randint(4, size=(12, 12, 12, 1))
    targets = np.random.randint(4, size=(12, 12, 12, 1))
    with self.test_session() as session:
      scores, _ = metrics.padded_neg_log_perplexity(
          tf.one_hot(predictions, depth=4, dtype=tf.float32),
          tf.constant(targets, dtype=tf.int32))
      a = tf.reduce_mean(scores)
      session.run(tf.global_variables_initializer())
      actual = session.run(a)
    self.assertEqual(actual.shape, ())

if __name__ == '__main__':
  tf.test.main()
