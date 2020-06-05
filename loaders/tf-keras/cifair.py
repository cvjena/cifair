""" ciFAIR data loader for tf.keras. Requires tensorflow >= 1.9.

Version: 1.0

https://cvjena.github.io/cifair/
"""

from tensorflow.python.keras import backend as K
from tensorflow.python.keras.utils.data_utils import get_file
from six.moves import cPickle
import numpy as np
import os
import sys


def load_cifair10():
    """Loads [ciFAIR-10 dataset](https://cvjena.github.io/cifair/).

    This is a variant of the [CIFAR-10](https://www.cs.toronto.edu/~kriz/cifar.html)
    dataset with a duplicate-free test set.
    See the [ciFAIR homepage](https://cvjena.github.io/cifair/) for more information.

    Returns:
        Tuple of Numpy arrays: `(x_train, y_train), (x_test, y_test)`.

        **x_train, x_test**: uint8 arrays of RGB image data with shape
            `(num_samples, 3, 32, 32)` if `tf.keras.backend.image_data_format()` is
            `'channels_first'`, or `(num_samples, 32, 32, 3)` if the data format
            is `'channels_last'`.

        **y_train, y_test**: uint8 arrays of category labels
            (integers in range 0-9) each with shape (num_samples, 1).
    """
    dirname = 'ciFAIR-10'
    archive_name = 'ciFAIR-10.zip'
    origin = 'https://github.com/cvjena/cifair/releases/download/v1.0/ciFAIR-10.zip'
    md5_hash = 'ca08fd390f0839693d3fc45c4e49585f'

    path = get_file(archive_name, origin=origin, file_hash=md5_hash, hash_algorithm='md5', extract=True, archive_format='zip')
    path = os.path.join(os.path.dirname(path), dirname)

    num_train_samples = 50000

    x_train = np.empty((num_train_samples, 3, 32, 32), dtype='uint8')
    y_train = np.empty((num_train_samples,), dtype='uint8')

    for i in range(1, 6):
        fpath = os.path.join(path, 'data_batch_' + str(i))
        (x_train[(i - 1) * 10000:i * 10000, :, :, :],
        y_train[(i - 1) * 10000:i * 10000]) = _load_batch(fpath)

    fpath = os.path.join(path, 'test_batch')
    x_test, y_test = _load_batch(fpath)

    y_train = np.reshape(y_train, (len(y_train), 1))
    y_test = np.reshape(y_test, (len(y_test), 1))

    if K.image_data_format() == 'channels_last':
        x_train = x_train.transpose(0, 2, 3, 1)
        x_test = x_test.transpose(0, 2, 3, 1)

    x_test = x_test.astype(x_train.dtype)
    y_test = y_test.astype(y_train.dtype)

    return (x_train, y_train), (x_test, y_test)


def load_cifair100(label_mode='fine'):
    """Loads [ciFAIR-100 dataset](https://cvjena.github.io/cifair/).

    This is a variant of the [CIFAR-100](https://www.cs.toronto.edu/~kriz/cifar.html)
    dataset with a duplicate-free test set.
    See the [ciFAIR homepage](https://cvjena.github.io/cifair/) for more information.

    Arguments:
        label_mode: one of "fine", "coarse". If it is "fine" the category labels
        are the fine-grained labels, if it is "coarse" the output labels are the
        coarse-grained superclasses.
    
    Returns:
        Tuple of Numpy arrays: `(x_train, y_train), (x_test, y_test)`.

        **x_train, x_test**: uint8 arrays of RGB image data with shape
            `(num_samples, 3, 32, 32)` if `tf.keras.backend.image_data_format()` is
            `'channels_first'`, or `(num_samples, 32, 32, 3)` if the data format
            is `'channels_last'`.

        **y_train, y_test**: uint8 arrays of category labels with shape
            (num_samples, 1).

    Raises:
        ValueError: in case of invalid `label_mode`.
    """
    if label_mode not in ['fine', 'coarse']:
        raise ValueError('`label_mode` must be one of `"fine"`, `"coarse"`.')

    dirname = 'ciFAIR-100'
    archive_name = 'ciFAIR-100.zip'
    origin = 'https://github.com/cvjena/cifair/releases/download/v1.0/ciFAIR-100.zip'
    md5_hash = 'ddc236ab4b12eeb8b20b952614861a33'

    path = get_file(archive_name, origin=origin, file_hash=md5_hash, hash_algorithm='md5', extract=True, archive_format='zip')
    path = os.path.join(os.path.dirname(path), dirname)

    fpath = os.path.join(path, 'train')
    x_train, y_train = _load_batch(fpath, label_key=label_mode + '_labels')

    fpath = os.path.join(path, 'test')
    x_test, y_test = _load_batch(fpath, label_key=label_mode + '_labels')

    y_train = np.reshape(y_train, (len(y_train), 1))
    y_test = np.reshape(y_test, (len(y_test), 1))

    if K.image_data_format() == 'channels_last':
        x_train = x_train.transpose(0, 2, 3, 1)
        x_test = x_test.transpose(0, 2, 3, 1)

    return (x_train, y_train), (x_test, y_test)


def _load_batch(fpath, label_key='labels'):
    """Internal utility for parsing ciFAIR data.
    # Arguments
        fpath: path the file to parse.
        label_key: key for label data in the retrieve
            dictionary.
    # Returns
        A tuple `(data, labels)`.
    """
    with open(fpath, 'rb') as f:
        if sys.version_info < (3,):
            d = cPickle.load(f)
            # encode utf8 to ascii
            d_decoded = {}
            for k, v in d.items():
                d_decoded[k.encode('utf-8') if isinstance(k, unicode) else k] = v
            d = d_decoded
        else:
            d = cPickle.load(f, encoding='bytes')
            # decode bytes to utf8
            d_decoded = {}
            for k, v in d.items():
                d_decoded[k.decode('utf-8') if isinstance(k, bytes) else k] = v
            d = d_decoded
    data = d['data']
    labels = d[label_key]

    data = data.reshape(data.shape[0], 3, 32, 32)
    return data, labels
