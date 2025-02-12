#!/usr/bin/env python
# Official implementation code for "Lung Nodule Detection and Classification from Thorax CT-Scan Using RetinaNet with Transfer Learning" and "Lung Nodule Texture Detection and Classification Using 3D CNN."
# Adapted from of [medicaldetectiontoolkit](https://github.com/pfjaeger/medicaldetectiontoolkit) and [kinetics_i3d_pytorch](https://github.com/hassony2/kinetics_i3d_pytorch)
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
# ==============================================================================

"""Default Configurations script. Avoids changing configs of all experiments if general settings are to be changed."""

import os

class DefaultConfigs:

    def __init__(self, model, server_env=None, dim=2):

        #########################
        #         I/O           #
        #########################

        self.model = model
        self.dim = dim
        # int [0 < dataset_size]. select n patients from dataset for prototyping.
        self.select_prototype_subset = None

        # some default paths.
        # self.backbone_path = 'models/backbone.py'
        self.backbone_path = 'models/i3dbackbone.py'
        self.source_dir = os.path.dirname(os.path.realpath(__file__)) #current dir.
        self.input_df_name = 'info_df.pickle'
        self.model_path = 'models/{}.py'.format(self.model)

        if server_env:
            self.source_dir = '/home/jaegerp/code/mamma_code/medicaldetectiontoolkit'


        #########################
        #      Data Loader      #
        #########################

        #random seed for fold_generator and batch_generator.
        self.seed = 0

        #number of threads for multithreaded batch generation.
        self.n_workers = 6

        # if True, segmentation losses learn all categories, else only foreground vs. background.
        self.class_specific_seg_flag = False

        #########################
        #      Architecture      #
        #########################

        self.weight_decay = 0.0

        # nonlinearity to be applied after convs with nonlinearity. one of 'relu' or 'leaky_relu'
        self.relu = 'relu'

        # if True initializes weights as specified in model script. else use default Pytorch init.
        self.custom_init = False

        # if True adds high-res decoder levels to feature pyramid: P1 + P0. (e.g. set to true in retina_unet configs)
        self.operate_stride1 = False

        #########################
        #  Schedule             #
        #########################

        # number of folds in cross validation.
        self.n_cv_splits = 5


        # number of probabilistic samples in validation.
        self.n_probabilistic_samples = None

        #########################
        #   Testing / Plotting  #
        #########################

        # perform mirroring at test time. (only XY. Z not done to not blow up predictions times).
        self.test_aug = True

        # if True, test data lies in a separate folder and is not part of the cross validation.
        self.hold_out_test_set = False

        # if hold_out_test_set provided, ensemble predictions over models of all trained cv-folds.
        self.ensemble_folds = False

        # color specifications for all box_types in prediction_plot.
        self.box_color_palette = {'det': 'b', 'gt': 'r', 'neg_class': 'purple',
                                  'prop': 'w', 'pos_class': 'g', 'pos_anchor': 'c', 'neg_anchor': 'c'}

        # scan over confidence score in evaluation to optimize it on the validation set.
        self.scan_det_thresh = False

        # plots roc-curves / prc-curves in evaluation.
        self.plot_stat_curves = True

        # evaluates average precision per image and averages over images. instead computing one ap over data set.
        self.per_patient_ap = True

        # threshold for clustering 2D box predictions to 3D Cubes. Overlap is computed in XY.
        self.merge_3D_iou = 0.1

        # monitor any value from training.
        self.n_monitoring_figures = 1
        # dict to assign specific plot_values to monitor_figures > 0. {1: ['class_loss'], 2: ['kl_loss', 'kl_sigmas']}
        self.assign_values_to_extra_figure = {}

        #########################
        #   MRCNN               #
        #########################

        # if True, mask loss is not applied. used for data sets, where no pixel-wise annotations are provided.
        self.frcnn_mode = False

        # if True, unmolds masks in Mask R-CNN to full-res for plotting/monitoring.
        self.return_masks_in_val = False
        self.return_masks_in_test = False # needed if doing instance segmentation. evaluation not yet implemented.

        # add P6 to Feature Pyramid Network.
        self.sixth_pooling = False

        # for probabilistic detection
        self.n_latent_dims = 0


