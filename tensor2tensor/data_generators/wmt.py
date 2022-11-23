#coding=utf-8

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

"""Data generators for WMT data-sets."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import tarfile

import codecs
# Dependency imports

from tensor2tensor.data_generators import wsj_parsing

import tensorflow as tf

from tensor2tensor.data_generators import generator_utils
from tensor2tensor.data_generators import text_encoder

#reload(sys) 
#sys.setdefaultencoding("utf-8")


tf.flags.DEFINE_string("ende_bpe_path", "", "Path to BPE files in tmp_dir."
                       "Download from https://drive.google.com/open?"
                       "id=0B_bZck-ksdkpM25jRUN2X2UxMm8")


FLAGS = tf.flags.FLAGS


# End-of-sentence marker (should correspond to the position of EOS in the
# RESERVED_TOKENS list in text_encoder.py)
EOS = 1


def character_generator(source_path, target_path, character_vocab, eos=None):
  """Generator for sequence-to-sequence tasks that just uses characters.

  This generator assumes the files at source_path and target_path have
  the same number of lines and yields dictionaries of "inputs" and "targets"
  where inputs are characters from the source lines converted to integers,
  and targets are characters from the target lines, also converted to integers.

  Args:
    source_path: path to the file with source sentences.
    target_path: path to the file with target sentences.
    character_vocab: a TextEncoder to encode the characters.
    eos: integer to append at the end of each sequence (default: None).

  Yields:
    A dictionary {"inputs": source-line, "targets": target-line} where
    the lines are integer lists converted from characters in the file lines.
  """
  eos_list = [] if eos is None else [eos]
  with tf.gfile.GFile(source_path, mode="r") as source_file:
    with tf.gfile.GFile(target_path, mode="r") as target_file:
      source, target = source_file.readline(), target_file.readline()
      while source and target:
        source_ints = character_vocab.encode(source.strip()) + eos_list
        target_ints = character_vocab.encode(target.strip()) + eos_list
        yield {"inputs": source_ints, "targets": target_ints}
        source, target = source_file.readline(), target_file.readline()


def token_generator(source_path, target_path, token_vocab, eos=None):
  """Generator for sequence-to-sequence tasks that uses tokens.

  This generator assumes the files at source_path and target_path have
  the same number of lines and yields dictionaries of "inputs" and "targets"
  where inputs are token ids from the " "-split source (and target, resp.) lines
  converted to integers using the token_map.

  Args:
    source_path: path to the file with source sentences.
    target_path: path to the file with target sentences.
    token_vocab: text_encoder.TextEncoder object.
    eos: integer to append at the end of each sequence (default: None).

  Yields:
    A dictionary {"inputs": source-line, "targets": target-line} where
    the lines are integer lists converted from tokens in the file lines.
  """
  eos_list = [] if eos is None else [eos]
  with tf.gfile.GFile(source_path, mode="r") as source_file:
    with tf.gfile.GFile(target_path, mode="r") as target_file:
      source, target = source_file.readline(), target_file.readline()
      while source and target:
        source_ints = token_vocab.encode(source.strip()) + eos_list
        target_ints = token_vocab.encode(target.strip()) + eos_list
        yield {"inputs": source_ints, "targets": target_ints}
        source, target = source_file.readline(), target_file.readline()

def token_generator_2(source_path, target_path, token_vocab_src, token_vocab_tgt, eos=None):
  """Generator for sequence-to-sequence tasks that uses tokens.
  """
  eos_list = [] if eos is None else [eos]
  with tf.gfile.GFile(source_path, mode="r") as source_file:
    with tf.gfile.GFile(target_path, mode="r") as target_file:

  #source_file = codecs.open(source_path,"r","utf-8")
  #target_file = open(target_path,"r")
  #while True:
      source, target = source_file.readline(), target_file.readline()
      ##source = unicode(source,"utf8")
      ##tf.logging.info(source)
      #if not source or not target:
      #    break
      while source and target:
        source_ints = token_vocab_src.encode(source.strip()) + eos_list
        target_ints = token_vocab_tgt.encode(target.strip()) + eos_list
        yield {"inputs": source_ints, "targets": target_ints}
        source, target = source_file.readline(), target_file.readline()

def token_generator_3(sc_path,source_path, target_path, token_vocab_src, token_vocab_tgt, eos=None):
  """Generator for sequence-to-sequence tasks that uses tokens.
  """
  eos_list = [] if eos is None else [eos]
  with tf.gfile.GFile(source_path, mode="r") as source_file:
    with tf.gfile.GFile(target_path, mode="r") as target_file:
      with tf.gfile.GFile(sc_path, mode="r") as sc_file:
  #source_file = codecs.open(source_path,"r","utf-8")
  #target_file = open(target_path,"r")
  #while True:
        sc, source, target = sc_file.readline(), source_file.readline(), target_file.readline()
        ##source = unicode(source,"utf8")
        ##tf.logging.info(source)
        #if not source or not target:
        #    break
        while source and target:
          sc_ints = token_vocab_src.encode(sc.strip()) + eos_list
          source_ints = token_vocab_src.encode(source.strip()) + eos_list
          target_ints = token_vocab_tgt.encode(target.strip()) + eos_list
          yield {"sc_inputs": sc_ints,"inputs": source_ints, "targets": target_ints}
          sc, source, target = sc_file.readline(), source_file.readline(), target_file.readline()
def token_generator_4(sc_path,source_path, target_path, token_vocab_src, token_vocab_tgt, eos=None):
  """Generator for sequence-to-sequence tasks that uses tokens.
  """
  eos_list = [] if eos is None else [eos]
  with tf.gfile.GFile(source_path, mode="r") as source_file:
    with tf.gfile.GFile(target_path, mode="r") as target_file:
      with tf.gfile.GFile(sc_path, mode="r") as sc_file:
  #source_file = codecs.open(source_path,"r","utf-8")
  #target_file = open(target_path,"r")
  #while True:
        sc, source, target = sc_file.readline(), source_file.readline(), target_file.readline()
        ##source = unicode(source,"utf8")
        ##tf.logging.info(source)
        #if not source or not target:
        #    break
        while source and target:
          sc_ints = []
          for ssc in sc.strip().split(','):
            sc_int = token_vocab_src.encode(ssc)
            while len(sc_int) <4:
              sc_int.append(-1)
            sc_ints.extend(sc_int)
          while len(sc_ints) < 4:
              sc_ints.append(-1)
          source_ints = token_vocab_src.encode(source.strip()) + eos_list
          target_ints = token_vocab_tgt.encode(target.strip()) + eos_list
          yield {"sc_inputs": sc_ints,"inputs": source_ints, "targets": target_ints}
          sc, source, target = sc_file.readline(), source_file.readline(), target_file.readline()

def _get_wmt_ende_dataset(directory, filename):
  """Extract the WMT en-de corpus `filename` to directory unless it's there."""
  train_path = os.path.join(directory, filename)
  if not (tf.gfile.Exists(train_path + ".tg") and
          tf.gfile.Exists(train_path + ".sc")):
    # We expect that this file has been downloaded from:
    # https://drive.google.com/open?id=0B_bZck-ksdkpM25jRUN2X2UxMm8 and placed
    # in `directory`.
    corpus_file = os.path.join(directory, FLAGS.ende_bpe_path)
    with tarfile.open(corpus_file, "r:gz") as corpus_tar:
      def is_within_directory(directory, target):
          
          abs_directory = os.path.abspath(directory)
          abs_target = os.path.abspath(target)
      
          prefix = os.path.commonprefix([abs_directory, abs_target])
          
          return prefix == abs_directory
      
      def safe_extract(tar, path=".", members=None, *, numeric_owner=False):
      
          for member in tar.getmembers():
              member_path = os.path.join(path, member.name)
              if not is_within_directory(path, member_path):
                  raise Exception("Attempted Path Traversal in Tar File")
      
          tar.extractall(path, members, numeric_owner=numeric_owner) 
          
      
      safe_extract(corpus_tar, directory)
  return train_path


def ende_bpe_token_generator(tmp_dir, train):
  """Instance of token generator for the WMT en->de task, training set."""
  dataset_path = ("train.unk"
                  if train else "dev.unk")
  train_path = _get_wmt_ende_dataset(tmp_dir, dataset_path)
  #sc_path = os.path.join(tmp_dir, 'sc.unk.sc')
  token_path_src = os.path.join(tmp_dir, "zh.unk.vocab")
  token_path_tgt = os.path.join(tmp_dir, "en.unk.vocab")
  token_vocab_src = text_encoder.TokenTextEncoder(vocab_filename=token_path_src)
  token_vocab_tgt = text_encoder.TokenTextEncoder(vocab_filename=token_path_tgt)
  #return token_generator_3(sc_path,train_path + ".sc", train_path + ".tg", token_vocab_src, token_vocab_tgt, 1)
  return token_generator_2(train_path+'.sc',train_path+'.tg',token_vocab_src,token_vocab_tgt,1)

def _get_paraphrase_dataset(directory, filename):
  """Extract the WMT en-de corpus `filename` to directory unless it's there."""
  train_path = os.path.join(directory, filename)
  if not (tf.gfile.Exists(train_path + ".A") and
          tf.gfile.Exists(train_path + ".B")):
    # We expect that this file has been downloaded from:
    # https://drive.google.com/open?id=0B_bZck-ksdkpM25jRUN2X2UxMm8 and placed
    # in `directory`.
    print(train_path+'.A not found!')
    return None
  return train_path

def token_generator_para(source_path, target_path, token_vocab_src, eos=None):
  """Generator for sequence-to-sequence tasks that uses tokens.
  """
  eos_list = [] if eos is None else [eos]
  with tf.gfile.GFile(source_path, mode="r") as source_file:
    with tf.gfile.GFile(target_path, mode="r") as target_file:

  #source_file = codecs.open(source_path,"r","utf-8")
  #target_file = open(target_path,"r")
  #while True:
      source, target = source_file.readline(), target_file.readline()
      ##source = unicode(source,"utf8")
      ##tf.logging.info(source)
      #if not source or not target:
      #    break
      while source and target:
        source_ints = token_vocab_src.encode(source.strip()) + eos_list
        target_ints = token_vocab_src.encode(target.strip()) + eos_list
        yield {"inputs": source_ints, "targets": target_ints}
        source, target = source_file.readline(), target_file.readline()

def paraphrase_generator(tmp_dir, train):
  """Instance of token generator for the WMT en->de task, training set."""
  dataset_path = ("train.unk"
                  if train else "dev.unk")
  train_path = _get_paraphrase_dataset(tmp_dir, dataset_path)
  #sc_path = os.path.join(tmp_dir, 'sc.unk.sc')
  token_path_src = os.path.join(tmp_dir, "vocab.txt")
  token_vocab_src = text_encoder.TokenTextEncoder(vocab_filename=token_path_src)
  #return token_generator_3(sc_path,train_path + ".sc", train_path + ".tg", token_vocab_src, token_vocab_tgt, 1)
  return token_generator_para(train_path+'.A',train_path+'.B',token_vocab_src,1)

def paraphrase_generator_rl(tmp_dir, train):
  """Instance of token generator for the WMT en->de task, training set."""
  dataset_path = ("train.unk"
                  if train else "dev.unk")
  train_path = _get_paraphrase_dataset(tmp_dir, dataset_path)
  sc_path = os.path.join(tmp_dir, 'entity.txt')
  token_path_src = os.path.join(tmp_dir, "vocab.txt")
  token_vocab_src = text_encoder.TokenTextEncoder(vocab_filename=token_path_src)
  return token_generator_4(sc_path, train_path + ".A", train_path + ".B", token_vocab_src, token_vocab_src, 1)
  #return token_generator_para(train_path+'.A',train_path+'.B',token_vocab_src,1)


_ENDE_TRAIN_DATASETS = [
    [
        "http://data.statmt.org/wmt16/translation-task/training-parallel-nc-v11.tgz",  # pylint: disable=line-too-long
        ("training-parallel-nc-v11/news-commentary-v11.de-en.en",
         "training-parallel-nc-v11/news-commentary-v11.de-en.de")
    ],
    [
        "http://www.statmt.org/wmt13/training-parallel-commoncrawl.tgz",
        ("commoncrawl.de-en.en", "commoncrawl.de-en.de")
    ],
    [
        "http://www.statmt.org/wmt13/training-parallel-europarl-v7.tgz",
        ("training/europarl-v7.de-en.en", "training/europarl-v7.de-en.de")
    ],
]
_ENDE_TEST_DATASETS = [
    [
        "http://data.statmt.org/wmt16/translation-task/dev.tgz",
        ("dev/newstest2013.en", "dev/newstest2013.de")
    ],
]

_ENFR_TRAIN_DATASETS = [
    [
        "http://www.statmt.org/wmt13/training-parallel-commoncrawl.tgz",
        ("commoncrawl.fr-en.en", "commoncrawl.fr-en.fr")
    ],
    [
        "http://www.statmt.org/wmt13/training-parallel-europarl-v7.tgz",
        ("training/europarl-v7.fr-en.en", "training/europarl-v7.fr-en.fr")
    ],
    [
        "http://www.statmt.org/wmt14/training-parallel-nc-v9.tgz",
        ("training/news-commentary-v9.fr-en.en",
         "training/news-commentary-v9.fr-en.fr")
    ],
    [
        "http://www.statmt.org/wmt10/training-giga-fren.tar",
        ("giga-fren.release2.fixed.en.gz", "giga-fren.release2.fixed.fr.gz")
    ],
    [
        "http://www.statmt.org/wmt13/training-parallel-un.tgz",
        ("un/undoc.2000.fr-en.en", "un/undoc.2000.fr-en.fr")
    ],
]
_ENFR_TEST_DATASETS = [
    [
        "http://data.statmt.org/wmt16/translation-task/dev.tgz",
        ("dev/newstest2013.en", "dev/newstest2013.fr")
    ],
]


def _compile_data(tmp_dir, datasets, filename):
  """Concatenate all `datasets` and save to `filename`."""
  filename = os.path.join(tmp_dir, filename)
  lang1_lines, lang2_lines = [], []
  for dataset in datasets:
    url = dataset[0]
    compressed_filename = os.path.basename(url)
    compressed_filepath = os.path.join(tmp_dir, compressed_filename)

    lang1_filename, lang2_filename = dataset[1]
    lang1_filepath = os.path.join(tmp_dir, lang1_filename)
    lang2_filepath = os.path.join(tmp_dir, lang2_filename)

    if not os.path.exists(compressed_filepath):
      generator_utils.maybe_download(tmp_dir, compressed_filename, url)
    if not os.path.exists(lang1_filepath) or not os.path.exists(lang2_filepath):
      mode = "r:gz" if "gz" in compressed_filepath else "r"
      with tarfile.open(compressed_filepath, mode) as corpus_tar:
        corpus_tar.extractall(tmp_dir)
    if ".gz" in lang1_filepath:
      new_filepath = lang1_filepath.strip(".gz")
      generator_utils.gunzip_file(lang1_filepath, new_filepath)
      lang1_filepath = new_filepath
    if ".gz" in lang2_filepath:
      new_filepath = lang2_filepath.strip(".gz")
      generator_utils.gunzip_file(lang2_filepath, new_filepath)
      lang2_filepath = new_filepath
    with tf.gfile.GFile(lang1_filepath, mode="r") as lang1_file:
      with tf.gfile.GFile(lang2_filepath, mode="r") as lang2_file:
        lang1_file_lines = lang1_file.readlines()
        lang2_file_lines = lang2_file.readlines()
        assert len(lang1_file_lines) == len(lang2_file_lines), lang1_filepath
        lang1_lines.extend(lang1_file_lines)
        lang2_lines.extend(lang2_file_lines)

  write_chunk_size = 10000
  assert len(lang1_lines) == len(lang2_lines)
  with tf.gfile.GFile(filename + ".lang1", mode="w") as lang1_file:
    i = 0
    while i <= len(lang1_lines):
      for line in lang1_lines[i * write_chunk_size:(i + 1) * write_chunk_size]:
        lang1_file.write(line)
      i += 1
    for line in lang1_lines[i * write_chunk_size:]:
      lang1_file.write(line)
  with tf.gfile.GFile(filename + ".lang2", mode="w") as lang2_file:
    i = 0
    while i <= len(lang2_lines):
      for line in lang2_lines[i * write_chunk_size:(i + 1) * write_chunk_size]:
        lang2_file.write(line)
      i += 1
    for line in lang2_lines[i * write_chunk_size:]:
      lang2_file.write(line)
  return filename


def ende_wordpiece_token_generator(tmp_dir, train, vocab_size):
  symbolizer_vocab = generator_utils.get_or_generate_vocab(
      tmp_dir, "tokens.vocab.%d" % vocab_size, vocab_size)
  #datasets = _ENDE_TRAIN_DATASETS if train else _ENDE_TEST_DATASETS
  tag = "train" if train else "dev"
  #data_path = _compile_data(tmp_dir, datasets, "wmt_ende_tok_%s" % tag)

  data_path = os.path.join(tmp_dir, "wmt_ende_tok_%s" % tag)

  return token_generator(data_path + ".lang1", data_path + ".lang2",
                         symbolizer_vocab, EOS)


def ende_character_generator(tmp_dir, train):
  character_vocab = text_encoder.ByteTextEncoder()
  datasets = _ENDE_TRAIN_DATASETS if train else _ENDE_TEST_DATASETS
  tag = "train" if train else "dev"
  data_path = _compile_data(tmp_dir, datasets, "wmt_ende_chr_%s" % tag)
  return character_generator(data_path + ".lang1", data_path + ".lang2",
                             character_vocab, EOS)


def enfr_wordpiece_token_generator(tmp_dir, train, vocab_size):
  """Instance of token generator for the WMT en->fr task."""
  symbolizer_vocab = generator_utils.get_or_generate_vocab(
      tmp_dir, "tokens.vocab.%d" % vocab_size, vocab_size)
  datasets = _ENFR_TRAIN_DATASETS if train else _ENFR_TEST_DATASETS
  tag = "train" if train else "dev"
  data_path = _compile_data(tmp_dir, datasets, "wmt_enfr_tok_%s" % tag)
  return token_generator(data_path + ".lang1", data_path + ".lang2",
                         symbolizer_vocab, EOS)


def enfr_character_generator(tmp_dir, train):
  """Instance of character generator for the WMT en->fr task."""
  character_vocab = text_encoder.ByteTextEncoder()
  datasets = _ENFR_TRAIN_DATASETS if train else _ENFR_TEST_DATASETS
  tag = "train" if train else "dev"
  data_path = _compile_data(tmp_dir, datasets, "wmt_enfr_chr_%s" % tag)
  return character_generator(data_path + ".lang1", data_path + ".lang2",
                             character_vocab, EOS)


def parsing_token_generator(tmp_dir, train, vocab_size):
  symbolizer_vocab = generator_utils.get_or_generate_vocab(
      tmp_dir, "tokens.vocab.%d" % vocab_size, vocab_size)
  filename = "%s_%s.trees" % (FLAGS.parsing_path, "train" if train else "dev")
  tree_filepath = os.path.join(tmp_dir, filename)
  return wsj_parsing.token_generator(tree_filepath,
                                     symbolizer_vocab, symbolizer_vocab, EOS)
