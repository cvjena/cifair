ciFAIR Website
==============

This repository hosts the following website:

[**ciFAIR: a duplicate-free variant of the CIFAR test set.**][1]

---

Adding a new model to the leaderboard
-------------------------------------

If you think an important CNN architecture is missing from the leaderboard on the [ciFAIR page][1] or you have come up with your own architecture outperforming the previous state-of-the-art, we would be happy to accept a pull request from you to update the leaderboard.

Note, however, that we only accept submissions which provide pre-trained models and source code to load and run these models, so that we can verify their performance.

The process for making a pull request to the leaderboard is as follows:

1. Fork this repository.

2. Create a new YAML file (file extension `.yml`) in the directory `_data/models` and fill it with information about your model according to the following example:

   ```YAML
   name: ResNeXt-29 (8x64d)
   paper: http://openaccess.thecvf.com/content_cvpr_2017/papers/Xie_Aggregated_Residual_Transformations_CVPR_2017_paper.pdf
   code: https://github.com/prlz77/ResNeXt.pytorch
   framework: PyTorch
   cifar10_model: 
   cifar100_model: 
   cifar10_error: 3.56
   cifair10_error: 3.95
   cifar100_error: 18.38
   cifair100_error: 20.84
   ```

   Leave the fields for the links to the pre-trained models blank for now; we will add them later.

3. Create a pull request to merge this new file into `cvjena/cifar` and upload your pre-trained models (for both ciFAIR-10 and ciFAIR-100) as attachments to the pull request.

4. Add the links to the two models uploaded in the previous step to your YAML file and push the commit to the branch from which you created the pull request. The PR will automatically be updated with the changes.

5. We will validate the performance of the model and merge the pull request. Once merged, the leaderboard will update itself automatically based on the information in the YAML file.


[1]: https://cvjena.github.io/cifair/
