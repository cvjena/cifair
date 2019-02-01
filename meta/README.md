CIFAR Duplicates
================

The files in this directory contain lists of duplicate image pairs found in the [CIFAR-10 and CIFAR-100 datasets][1].

[`duplicates_cifar10.csv`](duplicates_cifar10.csv) and [`duplicates_cifar100.csv`](duplicates_cifar100.csv) list images from the test sets that have near-duplicates in the training set.
The columns of these CSV files have the following meaning:

- `TestID`: Index of the test image in the original CIFAR dataset (counting from 0).
- `TrainID`: Index of the training image in the original CIFAR dataset (counting from 0).
- `Distance`: The Euclidean distance between these two images in the L2-normalized CNN feature space.
- `Judgment`: Indicates the type of duplicate (assigned by manual annotation):
    - `0` = **exact duplicate**: Almost all pixels in the two images are approximately identical.
    - `1` = **near-duplicate**: The content of the images is exactly the same, i.e., both originated from the same camera shot. However, different post-processing might have been applied to this original scene, e.g., color shifts, translations, scaling etc.
    - `2` = **very similar**: The contents of the two images are different, but highly similar, so that the difference can only be spotted at the second glance.

On the other hand, [`duplicates_cifar10_test.csv`](duplicates_cifar10_test.csv) and [`duplicates_cifar100_test.csv`](duplicates_cifar100_test.csv) list duplicate image pairs within the test set.
The structure is identical to that of the other two files, but the column `TrainID` now also refers to images in the test set.


[1]: https://www.cs.toronto.edu/~kriz/cifar.html