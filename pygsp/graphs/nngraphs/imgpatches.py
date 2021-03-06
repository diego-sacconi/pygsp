# -*- coding: utf-8 -*-

from . import NNGraph
from ...features import patch_features


class ImgPatches(NNGraph):
    r"""
    Create a nearest neighbors graph from patches of an image.

    Parameters
    ----------
    img : array
        Input image.
    patch_shape : tuple, optional
        Dimensions of the patch window. Syntax: (height, width), or (height,),
        in which case width = height.
    n_nbrs : int, optional
        Number of neighbors to consider
    dist_type : string, optional
        Type of distance between patches to compute. See
        :func:`pyflann.index.set_distance_type` for possible options.

    Examples
    --------
    >>> from pygsp.graphs import nngraphs
    >>> from skimage import data, img_as_float
    >>> img = img_as_float(data.camera()[::2, ::2])
    >>> G = nngraphs.ImgPatches(img)

    """

    def __init__(self, img, patch_shape=(3, 3), n_nbrs=8, use_flann=True,
                 dist_type='euclidean', symmetrize_type='full', **kwargs):

        X = patch_features(img, patch_shape=patch_shape)

        super(ImgPatches, self).__init__(X,
                                         use_flann=use_flann,
                                         symmetrize_type=symmetrize_type,
                                         dist_type=dist_type,
                                         gtype='patch-graph',
                                         perform_all_checks=False,
                                         **kwargs)
        self.img = img
