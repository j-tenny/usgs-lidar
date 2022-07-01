def approximatecoplanar(knn=None, thresh1=None, thresh2=None, inputs=None, tag=None, **kwargs):
    """.. _filters.approximatecoplanar:



filters.approximatecoplanar

===============================================================================



The **approximate coplanar filter** implements a portion of the algorithm

presented

in [Limberger2015]_. Prior to clustering points, the authors first apply an

approximate coplanarity test, where points that meet the following criteria are

labeled as approximately coplanar.



.. math::



  \lambda_2 > (s_{\alpha}\lambda_1) \&\& (s_{\beta}\lambda_2) > \lambda_3



:math:`\lambda_1`, :math:`\lambda_2`, :math:`\lambda_3` are the eigenvalues of

a neighborhood of points (defined by ``knn`` nearest neighbors) in ascending

order. The threshold values :math:`s_{\alpha}` and :math:`s_{\beta}` are

user-defined and default to 25 and 6 respectively.



The filter returns a point cloud with a new dimension ``Coplanar`` that

indicates those points that are part of a neighborhood that is approximately

coplanar (1) or not (0).



.. embed::



Example

-------



The sample pipeline presented below estimates the planarity of a point based on

its eight nearest neighbors using the approximate coplanar filter. A

:ref:`filters.range` stage then filters out any points that were not

deemed to be coplanar before writing the result in compressed LAZ.



.. code-block:: json



  [

      "input.las",

      {

          "type":"filters.approximatecoplanar",

          "knn":8,

          "thresh1":25,

          "thresh2":6

      },

      {

          "type":"filters.range",

          "limits":"Coplanar[1:1]"

      },

      "output.laz"

  ]



Options

-------------------------------------------------------------------------------



knn

  The number of k-nearest neighbors. [Default: 8]



thresh1

  The threshold to be applied to the smallest eigenvalue. [Default: 25]



thresh2

  The threshold to be applied to the second smallest eigenvalue. [Default: 6]



.. include:: filter_opts.rst


    """

    vars = dict()
    vars['type'] = 'filters.approximatecoplanar'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def assign(assignment=None, condition=None, value=None, inputs=None, tag=None, **kwargs):
    """.. _filters.assign:



filters.assign

===================



The assign filter allows you set the value of a dimension for all points

to a provided value that pass a range filter.



.. embed::



.. streamable::



.. note::

    The `assignment` and `condition` options are deprecated and may be removed in a

    future release.



Options

-------



assignment

  A :ref:`range <ranges>` followed by an assignment of a value (see example).

  Can be specified multiple times.  The assignments are applied sequentially

  to the dimension value as set when the filter began processing. [Required]



condition

  A single :ref:`ranges <ranges>` that a point's values must pass in order

  for the assignment to be performed. [Default: none] [Deprecated - use 'value']



value

  A list of :ref:`assignment expressions <Assignment Expressions>` to be applied to points.

  The list of values is evaluated in order. [Default: none]



.. include:: filter_opts.rst



.. _assignment expressions:



Assignment Expressions

======================



The assignment expression syntax is an expansion on the :ref:`PDAL expression` syntax

that provides for assignment of values to points. The generic expression is:



.. code-block::



    "value" : "Dimension = ValueExpression [WHERE ConditionalExpression)]"



``Dimension`` is the name of a PDAL dimension.



A ``ValueExpression`` consists of constants, dimension names and mathematical operators

that evaluates to a numeric value.  The supported mathematical operations are addition(`+`),

subtraction(`-`), multiplication(`*`) and division(`\\`).



A :ref:`ConditionalExpression <PDAL expression>` is an optional boolean value that must

evaluate to `true` for the ``ValueExpression`` to be applied.



Example 1

=========



.. code-block::



    "value" : "Red = Red / 256"



This scales the ``Red`` value by 1/256. If the input values are in the range 0 - 65535, the output

value will be in the range 0 - 255.





Example 2

=========



.. code-block::



    "value" :

    [

        "Classification = 2 WHERE HeightAboveGround < 5",

        "Classification = 1 WHERE HeightAboveGround >= 5"

    ]



This sets the classification of points to either ``Ground`` or ``Unassigned`` depending on the

value of the ``HeightAboveGround`` dimension.



Example 3

=========



.. code-block::



    "value" :

    [

        "X = 1",

        "X = 2 WHERE X > 10"

    ]



This sets the value of ``X`` for all points to 1. The second statement is essentially ignored

since the first statement sets the ``X`` value of all points to 1 and therefore no points

the ``ConditionalExpression`` of the second statement.
    """

    vars = dict()
    vars['type'] = 'filters.assign'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def chipper(inputs=None, tag=None, **kwargs):
    """.. _filters.chipper:



filters.chipper

===============



The **Chipper Filter** takes a single large point cloud and converts it

into a set

of smaller clouds, or chips. The chips are all spatially contiguous and

non-overlapping, so the result is a an irregular tiling of the input data.



.. note::



    Each chip will have approximately, but not exactly, the capacity_ point

    count specified.



.. seealso::



    The :ref:`PDAL split command <split_command>` utilizes the

    :ref:`filters.chipper` to split data by capacity.



.. figure:: filters.chipper.img1.png

    :scale: 100 %

    :alt: Points before chipping



    Before chipping, the points are all in one collection.





.. figure:: filters.chipper.img2.png

    :scale: 100 %

    :alt: Points after chipping



    After chipping, the points are tiled into smaller contiguous chips.



Chipping is usually applied to data read from files (which produce one large

stream of points) before the points are written to a database (which prefer

data segmented into smaller blocks).



.. embed::



Example

-------



.. code-block:: json



  [

      "example.las",

      {

          "type":"filters.chipper",

          "capacity":"400"

      },

      {

          "type":"writers.pgpointcloud",

          "connection":"dbname='lidar' user='user'"

      }

  ]



Options

-------



_`capacity`

  How many points to fit into each chip. The number of points in each chip will

  not exceed this value, and will sometimes be less than it. [Default: 5000]



.. include:: filter_opts.rst


    """

    vars = dict()
    vars['type'] = 'filters.chipper'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def cluster(min_points=None, max_points=None, tolerance=None, is3d=None, inputs=None, tag=None, **kwargs):
    """.. _filters.cluster:



===============================================================================

filters.cluster

===============================================================================



The Cluster filter first performs Euclidean Cluster Extraction on the input

``PointView`` and then labels each point with its associated cluster ID.

It creates a new dimension ``ClusterID`` that contains the cluster ID value.

Cluster IDs start with the value 1.  Points that don't belong to any

cluster will are given a cluster ID of 0.



.. embed::



Example

-------



.. code-block:: json



  [

      "input.las",

      {

          "type":"filters.cluster"

      },

      {

          "type":"writers.bpf",

          "filename":"output.bpf",

          "output_dims":"X,Y,Z,ClusterID"

      }

  ]



Options

-------



min_points

  Minimum number of points to be considered a cluster. [Default: 1]



max_points

  Maximum number of points to be considered a cluster. [Default: 2^64 - 1]



tolerance

  Cluster tolerance - maximum Euclidean distance for a point to be added to the

  cluster. [Default: 1.0]



is3d

  By default, clusters are formed by considering neighbors in a 3D sphere, but

  if ``is3d`` is set to false, it will instead consider neighbors in a 2D

  cylinder (XY plane only). [Default: true]



.. include:: filter_opts.rst
    """

    vars = dict()
    vars['type'] = 'filters.cluster'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def colorinterp(inputs=None, tag=None, **kwargs):
    """.. _filters.colorinterp:



filters.colorinterp

====================



The color interpolation filter assigns scaled RGB values from an image based on

a given dimension.  It provides three possible approaches:



1. You provide a minimum_ and maximum_, and the data are scaled for the

   given dimension_ accordingly.



2. You provide a k_ and a mad_ setting, and the scaling is set based on

   Median Absolute Deviation.



3. You provide a k_ setting and the scaling is set based on the

   k_-number of standard deviations from the median.



You can provide your own `GDAL`_-readable image for the scale color factors,

but a number of pre-defined ramps are embedded in PDAL.  The default ramps

provided by PDAL are 256x1 RGB images, and might be a good starting point for

creating your own scale factors. See `Default Ramps`_ for more information.



.. note::



    :ref:`filters.colorinterp` will use the entire band to scale the colors.



.. embed::



Example

--------------------------------------------------------------------------------



.. code-block:: json



  [

      "uncolored.las",

      {

        "type":"filters.colorinterp",

        "ramp":"pestel_shades",

        "mad":true,

        "k":1.8,

        "dimension":"Z"

      },

      "colorized.las"

  ]



.. figure:: ../images/pestel_scaled_helheim.png

    :scale: 80%



    Image data with interpolated colors based on ``Z`` dimension and ``pestel_shades``

    ramp.



Default Ramps

--------------------------------------------------------------------------------



PDAL provides a number of default color ramps you can use in addition to

providing your own. Give the ramp name as the ramp_ option to the filter

and it will be used. Otherwise, provide a `GDAL`_-readable raster filename.



``awesome_green``

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. image:: ../images/awesome-green.png

    :scale: 400%

    :alt: awesome-green color ramp



``black_orange``

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. image:: ../images/black-orange.png

    :scale: 400%

    :alt: black-orange color ramp



``blue_orange``

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. image:: ../images/blue-orange.png

    :scale: 400%

    :alt: blue-orange color ramp



``blue_hue``

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. image:: ../images/blue-hue.png

    :scale: 400%

    :alt: blue-hue color ramp



``blue_orange``

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. image:: ../images/blue-orange.png

    :scale: 400%

    :alt: blue-orange color ramp



``blue_red``

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. image:: ../images/blue-red.png

    :scale: 400%

    :alt: blue-red color ramp



``heat_map``

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. image:: ../images/heat-map.png

    :scale: 400%

    :alt: heat-map color ramp



``pestel_shades``

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. image:: ../images/pestel-shades.png

    :scale: 400%

    :alt: pestel-shades color ramp



Options

-------



_`ramp`

  The raster file to use for the color ramp. Any format supported by `GDAL`_

  may be read.  Alternatively, one of the default color ramp names can be

  used. [Default: "pestel_shades"]



_`dimension`

  A dimension name to use for the values to interpolate colors. [Default: "Z"]



_`minimum`

  The minimum value to use to scale the data. If none is specified, one is

  computed from the data. If one is specified but a k_ value is also

  provided, the k_ value will be used.



_`maximum`

  The maximum value to use to scale the data. If none is specified, one is

  computed from the data. If one is specified but a k_ value is also

  provided, the k_ value will be used.



_`invert`

  Invert the direction of the ramp? [Default: false]



_`k`

  Color based on the given number of standard deviations from the median. If

  set, minimum_ and maximum_ will be computed from the median and setting

  them will have no effect.



_`mad`

  If true, minimum_ and maximum_ will be computed by the median absolute

  deviation. See :ref:`filters.mad` for discussion. [Default: false]



_`mad_multiplier`

  MAD threshold multiplier. Used in conjunction with k_ to threshold the

  differencing. [Default: 1.4862]



.. include:: filter_opts.rst



.. _`GDAL`: http://www.gdal.org
    """

    vars = dict()
    vars['type'] = 'filters.colorinterp'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def colorization(raster=None, dimensions=None, inputs=None, tag=None, **kwargs):
    """.. _filters.colorization:



filters.colorization

====================



The colorization filter populates dimensions in the point buffer using input

values read from a raster file. Commonly this is used to add Red/Green/Blue

values to points from an aerial photograph of an area. However, any band can be

read from the raster and applied to any dimension name desired.



.. figure:: filters.colorization.img1.jpg

    :scale: 50 %

    :alt: Points after colorization



    After colorization, points take on the colors provided by the input image



.. note::



    `GDAL`_ is used to read the color information and any GDAL-readable

    supported `format`_ can be read.



.. _GDAL: http://www.gdal.org



The bands of the raster to apply to each are selected using the "band" option,

and the values of the band may be scaled before being written to the dimension.

If the band range is 0-1, for example, it might make sense to scale by 256 to

fit into a traditional 1-byte color value range.



.. embed::



.. streamable::



Example

--------------------------------------------------------------------------------



.. code-block:: json



  [

      "uncolored.las",

      {

        "type":"filters.colorization",

        "dimensions":"Red:1:1.0, Blue, Green::256.0",

        "raster":"aerial.tif"

      },

      "colorized.las"

  ]



Considerations

--------------------------------------------------------------------------------



Certain data configurations can cause degenerate filter behavior.

One significant knob to adjust is the ``GDAL_CACHEMAX`` environment

variable. One driver which can have issues is when a `TIFF`_ file is

striped vs. tiled. GDAL's data access in that situation is likely to

cause lots of re-reading if the cache isn't large enough.



Consider a striped TIFF file of 286mb:



::



    -rw-r-----@  1 hobu  staff   286M Oct 29 16:58 orth-striped.tif



.. code-block:: json



  [

      "colourless.laz",

      {

        "type":"filters.colorization",

        "raster":"orth-striped.tif"

      },

      "coloured-striped.las"

  ]



Simple application of the :ref:`filters.colorization` using the striped `TIFF`_

with a 268mb :ref:`readers.las` file will take nearly 1:54.



.. _`TIFF`: http://www.gdal.org/frmt_gtiff.html



::



    [hobu@pyro knudsen (master)]$ time ~/dev/git/pdal/bin/pdal pipeline -i striped.json



    real    1m53.477s

    user    1m20.018s

    sys 0m33.397s





Setting the ``GDAL_CACHEMAX`` variable to a size larger than the TIFF file

dramatically speeds up the color fetching:



::



    [hobu@pyro knudsen (master)]$ export GDAL_CACHEMAX=500

    [hobu@pyro knudsen (master)]$ time ~/dev/git/pdal/bin/pdal pipeline striped.json



    real    0m19.034s

    user    0m15.557s

    sys 0m1.102s



Options

-------



raster

  The raster file to read the band from. Any `format`_ supported by

  `GDAL`_ may be read.



dimensions

  A comma separated list of dimensions to populate with values from the raster

  file. Dimensions will be created if they don't already exist.  The format

  of each dimension is <name>:<band_number>:<scale_factor>.

  Either or both of band number and scale factor may be omitted as may ':'

  separators if the data is not ambiguous.  If not supplied, band numbers

  begin at 1 and increment from the band number of the previous dimension.

  If not supplied, the scaling factor is 1.0.

  [Default: "Red:1:1.0, Green:2:1.0, Blue:3:1.0"]



.. include:: filter_opts.rst



.. _format: https://www.gdal.org/formats_list.html
    """

    vars = dict()
    vars['type'] = 'filters.colorization'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def covariancefeatures(knn=None, threads=None, feature_set=None, stride=None, min_k=None, radius=None, mode=None, optimized=None, inputs=None, tag=None, **kwargs):
    """.. _filters.covariancefeatures:



===============================================================================

filters.covariancefeatures

===============================================================================



This filter implements various local feature descriptors that are based on the

covariance matrix of a point's neighborhood.



The user can pick a set of feature descriptors by setting the ``feature_set``

option. The dimensionality_ set of feature descriptors introduced below is the

default. The user can also provide a comma-separated list of features to

explicitly itemize those covariance features they wish to be computed. This can

be combined with any suppported presets like "Dimensionality".  Specifying "all"

will compute all available features.



Supported features include:



* Anisotropy

* DemantkeVerticality

* Density

* Eigenentropy

* Linearity

* Omnivariance

* Planarity

* Scattering

* EigenvalueSum

* SurfaceVariation

* Verticality



.. note::



    Density requires both ``OptimalKNN`` and ``OptimalRadius`` which can be

    computed by running :ref:`filters.optimalneighborhood` prior to

    ``filters.covariancefeatures``.



Example #1

-------------------------------------------------------------------------------



.. code-block:: json



  [

      "input.las",

      {

          "type":"filters.covariancefeatures",

          "knn":8,

          "threads": 2,

          "feature_set": "Dimensionality"

      },

      {

          "type":"writers.bpf",

          "filename":"output.bpf",

          "output_dims":"X,Y,Z,Linearity,Planarity,Scattering,Verticality"

      }

  ]



Example #2

-------------------------------------------------------------------------------



.. code-block:: json



  [

      "input.las",

      {

          "type":"filters.optimalneighborhood"

      },

      {

          "type":"filters.covariancefeatures",

          "knn":8,

          "threads": 2,

          "optimized":true,

          "feature_set": "Linearity,Omnivariance,Density"

      },

      {

          "type":"writers.las",

          "minor_version":4,

          "extra_dims":"all",

          "forward":"all",

          "filename":"output.las"

      }

  ]



Options

-------------------------------------------------------------------------------



knn

  The number of k nearest neighbors used for calculating the covariance matrix.

  [Default: 10]



threads

  The number of threads used for computing the feature descriptors. [Default: 1]



feature_set

  A comma-separated list of individual features or feature presets (e.g.,

  "Dimensionality") to be computed. To compute all available features, specify

  "all". [Default: "Dimensionality"]



stride

  When finding k nearest neighbors, stride determines the sampling rate. A

  stride of 1 retains each neighbor in order. A stride of two selects every

  other neighbor and so on. [Default: 1]



min_k

  Minimum number of neighbors in radius (radius search only). [Default: 3]



radius

  If radius is specified, neighbors will be obtained by radius search rather

  than k nearest neighbors, subject to meeting the minimum number of neighbors

  (``min_k``).



mode

  By default, features are computed using the standard deviation along each

  eigenvector, i.e., using the square root of the computed eigenvalues

  (``mode="SQRT"``). ``mode`` also accepts "Normalized" which normalizes

  eigenvalue such that they sum to one, or "Raw" such that the eigenvalues are

  used directly. [Default: "SQRT"]



optimized

  ``optimized`` can be set to ``true`` to enable computation of features using

  precomputed optimal neighborhoods (found in the ``OptimalKNN`` dimension).

  Requires :ref:`filters.optimalneighborhood` be run prior to this stage.

  [Default: false]



.. include:: filter_opts.rst



.. _dimensionality:



Dimensionality feature set

................................................................................



The features introduced in [Demantke2011]_ describe the shape of the

neighborhood, indicating whether the local geometry is more linear (1D), planar

(2D) or volumetric (3D) while the one introduced in [Guinard2017]_ adds the

idea of a structure being vertical.



The dimensionality filter introduces the following four descriptors that are

computed from the covariance matrix of a point's neighbors (as defined by

``knn`` or ``radius``):



* linearity - higher for long thin strips

* planarity - higher for planar surfaces

* scattering - higher for complex 3d neighbourhoods

* verticality - higher for vertical structures, highest for thin vertical strips



It introduces four new dimensions that hold each one of these values:

``Linearity``, ``Planarity``, ``Scattering`` and ``Verticality``.


    """

    vars = dict()
    vars['type'] = 'filters.covariancefeatures'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def cpd(inputs=None, tag=None, **kwargs):
    """.. _filters.cpd:



filters.cpd

==============



The **Coherent Point Drift (CPD) filter** uses the algorithm of

:cite:`Myronenko` algorithm to

compute a rigid, nonrigid, or affine transformation between datasets.  The

rigid and affine are what you'd expect; the nonrigid transformation uses Motion

Coherence Theory :cite:`Yuille1998` to "bend" the points to find a best

alignment.



.. note::



    CPD is computationally intensive and can be slow when working with many

    points (i.e. > 10,000).  Nonrigid is significantly slower

    than rigid and affine.



The first input to the change filter are considered the "fixed" points, and all

subsequent inputs are "moving" points.  The output from the change filter are

the "moving" points after the calculated transformation has been applied, one

point view per input.  Any additional information about the cpd registration,

e.g. the rigid transformation matrix, will be placed in the stage's metadata.



When to use CPD vs ICP

----------------------



Summarized from the `Non-rigid point set registration: Coherent Point Drift

<http://graphics.stanford.edu/courses/cs468-07-winter/Papers/nips2006_0613.pdf>`_ paper.



- CPD outperforms the ICP in the presence of noise and outliers by the use of

  a probabilistic assignment of correspondences between pointsets, which is

  innately more robust than the binary assignment used in ICP.



- CPD does not work well for large in-plane rotation, such transformation can

  be first compensated by other well known global registration techniques before

  CPD algorithm is carried out



- CPD is most effective when estimating smooth non-rigid transformations.





.. plugin::



Examples

--------



.. code-block:: json



  [

      "fixed.las",

      "moving.las",

      {

          "type": "filters.cpd",

          "method": "rigid"

      },

      "output.las"

  ]



If method_ is not provided, the cpd filter will default to using the

rigid registration method.  To get the transform matrix, you'll need to

use the "metadata" option of the pipeline command:



::



    $ pdal pipeline cpd-pipeline.json --metadata cpd-metadata.json



The metadata output might start something like:



.. code-block:: json



    {

        "stages":

        {

            "filters.cpd":

            {

                "iterations": 10,

                "method": "rigid",

                "runtime": 0.003839,

                "sigma2": 5.684342128e-16,

                "transform": "           1 -6.21722e-17  1.30104e-18  5.29303e-11-8.99346e-17            1  2.60209e-18 -3.49247e-10 -2.1684e-19  1.73472e-18            1 -1.53477e-12           0            0            0            1"

            },

        },



.. seealso::



    :ref:`filters.transformation` to apply a transform to other points.

    :ref:`filters.icp` for deterministic binary point pair assignments.



Options

--------



_`method`

    Change detection method to use.

    Valid values are "rigid", "affine", and "nonrigid".

    [Default: "rigid""]



.. include:: filter_opts.rst



.. _Coherent Point Drift (CPD): https://github.com/gadomski/cpd



.. bibliography:: references.bib
    """

    vars = dict()
    vars['type'] = 'filters.cpd'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def crop(bounds=None, polygon=None, outside=None, Notes=None, inputs=None, tag=None, **kwargs):
    """.. _filters.crop:



filters.crop

============



The **crop filter** removes points that fall outside or inside a

cropping bounding

box (2D or 3D), polygon, or point+distance.  If more than one bounding region is

specified, the filter will pass all input points through each bounding region,

creating an output point set for each input crop region.



.. embed::



.. streamable::



The provided bounding regions are assumed to have the same spatial reference

as the points unless the option a_srs_ provides an explicit spatial reference

for bounding regions.

If the point input consists of multiple point views with differing

spatial references, one is chosen at random and assumed to be the

spatial reference of the input bounding region.  In this case a warning will

be logged.





Example 1

----------

This example crops an input point cloud using a square polygon.



.. code-block:: json



  [

      "file-input.las",

      {

          "type":"filters.crop",

          "bounds":"([0,1000000],[0,1000000])"

      },

      {

          "type":"writers.las",

          "filename":"file-cropped.las"

      }

  ]



Example 2

----------

This example crops all points more than 500 units in any direction from a point. 



.. code-block:: json



  [

      "file-input.las",

      {

          "type":"filters.crop",

          "point":"POINT(0 0 0)",

          "distance": 500

      },

      {

          "type":"writers.las",

          "filename":"file-cropped.las"

      }

  ]



Options

-------



bounds

  The extent of the clipping rectangle in the format

  ``"([xmin, xmax], [ymin, ymax])"``.  This option can be specified more than

  once by placing values in an array.





  .. note::



    3D bounds can be given in the form ``([xmin, xmax], [ymin, ymax], [zmin, zmax])``.



  .. warning::



    If a 3D bounds is given to the filter, a 3D crop will be attempted, even

    if the Z values are invalid or inconsistent with the data.



polygon

  The clipping polygon, expressed in a well-known text string,

  eg: ``"POLYGON((0 0, 5000 10000, 10000 0, 0 0))"``.  This option can be

  specified more than once by placing values in an array.



outside

  Invert the cropping logic and only take points outside the cropping

  bounds or polygon. [Default: false]



_`point`

  An array of WKT or GeoJSON 2D or 3D points (eg: ``"POINT(0 0 0)"``). Requires distance_.



_`distance`

  Distance (radius) in units of common X, Y, and Z :ref:`dimensions` in combination with point_. Passing a 2D point will crop using a circle. Passing a 3D point will crop using a sphere.



_`a_srs`

  Indicates the spatial reference of the bounding regions.  If not provided,

  it is assumed that the spatial reference of the bounding region matches

  that of the points.



.. include:: filter_opts.rst



Notes

--------------------------------------------------------------------------------



1. See :ref:`workshop-clipping`: and :ref:`clipping` for example usage scenarios for :ref:`filters.crop`.
    """

    vars = dict()
    vars['type'] = 'filters.crop'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def csf(resolution=None, ignore=None, returns=None, threshold=None, smooth=None, step=None, rigidness=None, iterations=None, inputs=None, tag=None, **kwargs):
    """.. _filters.csf:



filters.csf

===============================================================================



The **Cloth Simulation Filter (CSF)** classifies ground points based on the

approach outlined in [Zhang2016]_.



.. embed::



Example

-------



The sample pipeline below uses CSF to segment ground and non-ground returns,

using default options, and writing only the ground returns to the output file.



.. code-block:: json



  [

      "input.las",

      {

          "type":"filters.csf"

      },

      {

          "type":"filters.range",

          "limits":"Classification[2:2]"

      },

      "output.laz"

  ]



Options

-------------------------------------------------------------------------------



resolution

  Cloth resolution. [Default: **1.0**]



ignore

  A :ref:`range <ranges>` of values of a dimension to ignore.



returns

  Return types to include in output.  Valid values are "first", "last",

  "intermediate" and "only". [Default: **"last, only"**]



threshold

  Classification threshold. [Default: **0.5**]



smooth

  Perform slope post-processing? [Default: **true**]



step

  Time step. [Default: **0.65**]



rigidness

  Rigidness. [Default: **3**]



iterations

  Maximum number of iterations. [Default: **500**]



.. include:: filter_opts.rst


    """

    vars = dict()
    vars['type'] = 'filters.csf'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def dbscan(min_points=None, eps=None, dimensions=None, inputs=None, tag=None, **kwargs):
    """.. _filters.dbscan:



===============================================================================

filters.dbscan

===============================================================================



The DBSCAN filter performs Density-Based Spatial Clustering of Applications

with Noise (DBSCAN) [Ester1996]_ and labels each point with its associated

cluster ID. Points that do not belong to a cluster are given a Cluster ID of

-1. The remaining clusters are labeled as integers starting from 0.



.. embed::



.. versionadded:: 2.1



Example

-------



.. code-block:: json



  [

      "input.las",

      {

          "type":"filters.dbscan",

          "min_points":10,

          "eps":2.0,

          "dimensions":"X,Y,Z"

      },

      {

          "type":"writers.bpf",

          "filename":"output.bpf",

          "output_dims":"X,Y,Z,ClusterID"

      }

  ]



Options

-------



min_points

  The minimum cluster size ``min_points`` should be greater than or equal to

  the number of dimensions (e.g., X, Y, and Z) plus one. As a rule of thumb,

  two times the number of dimensions is often used. [Default: 6]



eps

  The epsilon parameter can be estimated from a k-distance graph (for k =

  ``min_points`` minus one). ``eps`` defines the Euclidean distance that will

  be used when searching for neighbors. [Default: 1.0]



dimensions

  Comma-separated string indicating dimensions to use for clustering. [Default: X,Y,Z]



.. include:: filter_opts.rst


    """

    vars = dict()
    vars['type'] = 'filters.dbscan'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def decimation(step=None, offset=None, limit=None, inputs=None, tag=None, **kwargs):
    """.. _filters.decimation:



filters.decimation

==================



The **decimation filter** retains every Nth point from an input point view.



.. embed::



.. streamable::



Example

-------



.. code-block:: json



  [

      {

          "type": "readers.las",

          "filename": "larger.las"

      },

      {

          "type":"filters.decimation",

          "step": 10

      },

      {

          "type":"writers.las",

          "filename":"smaller.las"

      }

  ]



Options

-------



step

  Number of points to skip between each sample point.  A step of 1 will skip

  no points.  A step of 2 will skip every other point.  A step of 100 will

  reduce the input by ~99%. [Default: 1]



offset

  Point index to start sampling.  Point indexes start at 0.  [Default: 0]



limit

  Point index at which sampling should stop (exclusive).  [Default: No limit]



.. include:: filter_opts.rst


    """

    vars = dict()
    vars['type'] = 'filters.decimation'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def delaunay(inputs=None, tag=None, **kwargs):
    """.. _filters.delaunay:



filters.delaunay

================



The **Delaunay Filter** creates a triangulated mesh fulfilling the Delaunay

condition from a collection of points.



The filter is implemented using the `delaunator-cpp`_ library, a C++ port of

the JavaScript `Delaunator`_ library.



The filter currently only supports 2D Delaunay triangulation, using the ``X``

and ``Y`` dimensions of the point cloud.



.. _`delaunator-cpp`: https://github.com/delfrrr/delaunator-cpp

.. _`Delaunator`: https://github.com/mapbox/delaunator



.. embed::



Example

-------



.. code-block:: json



  [

      "input.las",

      {

          "type": "filters.delaunay"

      },

      {

          "type": "writers.ply",

          "filename": "output.ply",

          "faces": true

      }

  ]



Options

-------



.. include:: filter_opts.rst
    """

    vars = dict()
    vars['type'] = 'filters.delaunay'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def dem(limits=None, raster=None, band=None, inputs=None, tag=None, **kwargs):
    """.. _filters.dem:



filters.dem

===============================================================================



The **DEM filter** uses a source raster to keep point cloud data within

a each cell within a computed range.

For example, atmospheric or MTA noise in a scene can be quickly

removed by keeping all data within 100m above and 20m below a preexisting

elevation model.



.. embed::



Example

-------



.. code-block:: json



  [

      {

          "type":"filters.dem",

          "raster":"dem.tif",

          "limits":"Z[20:100]"

      }

  ]



Options

-------------------------------------------------------------------------------



limits

  A :ref:`range <ranges>` that defines the dimension and the magnitude above

  and below the value of the given dimension to filter.



  For example "Z[20:100]" would keep all ``Z`` point cloud values that are

  within 100 units above and 20 units below the elevation model value at the

  given ``X`` and ``Y`` value.



raster

  `GDAL readable raster`_ data to use for filtering.



band

  GDAL Band number to read (count from 1) [Default: 1]



.. include:: filter_opts.rst



.. _`GDAL`: http://gdal.org

.. _`GDAL readable raster`: http://www.gdal.org/formats_list.html
    """

    vars = dict()
    vars['type'] = 'filters.dem'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def divider(inputs=None, tag=None, **kwargs):
    """.. _filters.divider:



filters.divider

===============================================================================



The **Divider Filter** breaks a point view into a set of smaller point views

based on simple criteria.  The number of subsets can be specified explicitly,

or one can specify a maximum point count for each subset.  Additionally,

points can be placed into each subset sequentially (as they appear in the

input) or in round-robin fashion.



Normally points are divided into subsets to facilitate output by writers

that support creating multiple output files with a template (LAS and BPF

are notable examples).



.. embed::



Example

-------



This pipeline will create 10 output files from the input file readers.las.



.. code-block:: json



  [

      "example.las",

      {

          "type":"filters.divider",

          "count":"10"

      },

      {

          "type":"writers.las",

          "filename":"out_#.las"

      }

  ]



Options

-------



_`mode`

  A mode of "partition" will write sequential points to an output view until

  the view meets its predetermined size. "round_robin" mode will iterate

  through the output views as it writes sequential points.

  [Default: "partition"]



_`count`

  Number of output views.  [Default: none]



_`capacity`

  Maximum number of points in each output view.  Views will contain

  approximately equal numbers of points.  [Default: none]



.. include:: filter_opts.rst



.. warning::



    You must specify exactly one of either count_ or capacity_.


    """

    vars = dict()
    vars['type'] = 'filters.divider'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def eigenvalues(knn=None, normalize=None, inputs=None, tag=None, **kwargs):
    """.. _filters.eigenvalues:



filters.eigenvalues

===============================================================================



The **eignvalue filter** returns the eigenvalues for a given point,

based on its k-nearest neighbors.



The filter produces three new dimensions (``Eigenvalue0``, ``Eigenvalue1``, and

``Eigenvalue2``), which can be analyzed directly, or consumed by downstream

stages for more advanced filtering. The eigenvalues are sorted in ascending

order.



The eigenvalue decomposition is performed using Eigen's

SelfAdjointEigenSolver_.



.. _SelfAdjointEigenSolver: https://eigen.tuxfamily.org/dox/classEigen_1_1SelfAdjointEigenSolver.html



.. embed::





Example

-------



This pipeline demonstrates the calculation of the eigenvalues. The newly created

dimensions are written out to BPF for further inspection.



.. code-block:: json



  [

      "input.las",

      {

          "type":"filters.eigenvalues",

          "knn":8

      },

      {

          "type":"writers.bpf",

          "filename":"output.bpf",

          "output_dims":"X,Y,Z,Eigenvalue0,Eigenvalue1,Eigenvalue2"

      }

  ]



Options

-------------------------------------------------------------------------------



knn

  The number of k-nearest neighbors. [Default: 8]



normalize

  Normalize eigenvalues such that the sum is 1. [Default: false]



.. include:: filter_opts.rst


    """

    vars = dict()
    vars['type'] = 'filters.eigenvalues'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def elm(inputs=None, tag=None, **kwargs):
    """.. _filters.elm:



filters.elm

===============================================================================



The Extended Local Minimum (ELM) filter marks low points as noise. This filter

is an implementation of the method described in [Chen2012]_.



ELM begins by rasterizing the input point cloud data at the given cell_ size.

Within each cell, the lowest point is considered noise if the next lowest point

is a given threshold above the current point. If it is marked as noise, the

difference between the next two points is also considered, marking points as

noise if needed, and continuing until another neighbor is found to be within the

threshold. At this point, iteration for the current cell stops, and the next

cell is considered.



.. embed::



Example #1

----------



The following PDAL pipeline applies the ELM filter, using a cell_ size of 20

and

applying the :ref:`classification <class>` code of 18 to those points

determined to be noise.



.. code-block:: json



    {

      "pipeline":[

        "input.las",

        {

          "type":"filters.elm",

          "cell":20.0,

          "class":18

        },

        "output.las"

      ]

    }



Example #2

----------



This variation of the pipeline begins by assigning a value of 0 to all

classifications, thus resetting any existing classifications. It then proceeds

to compute ELM with a threshold_ value of 2.0, and finishes by extracting all

returns that are not marked as noise.



.. code-block:: json



  [

      "input.las",

      {

          "type":"filters.assign",

          "assignment":"Classification[:]=0"

      },

      {

          "type":"filters.elm",

          "threshold":2.0

      },

      {

          "type":"filters.range",

          "limits":"Classification![7:7]"

      },

      "output.las"

  ]



Options

-------------------------------------------------------------------------------



_`cell`

  Cell size. [Default: 10.0]



_`class`

  Classification value to apply to noise points. [Default: 7]



_`threshold`

  Threshold value to identify low noise points. [Default: 1.0]



.. include:: filter_opts.rst


    """

    vars = dict()
    vars['type'] = 'filters.elm'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def estimaterank(inputs=None, tag=None, **kwargs):
    """.. _filters.estimaterank:



filters.estimaterank

===============================================================================



The **rank estimation filter** uses singular value decomposition (SVD) to

estimate the rank of a set of points. Point sets with rank 1 correspond

to linear features, while sets with rank 2 correspond to planar features.

Rank 3 corresponds to a full 3D feature. In practice this can be used alone, or

possibly in conjunction with other filters to extract features (e.g.,

buildings, vegetation).



Two parameters are required to estimate rank (though the default values will be

suitable in many cases). First, the knn_ parameter defines the number of

points to consider when computing the SVD and estimated rank. Second, the

thresh_ parameter is used to determine when a singular value shall be

considered non-zero (when the absolute value of the singular value is greater

than the threshold).



The rank estimation is performed on a pointwise basis, meaning for each point

in the input point cloud, we find its knn_ neighbors, compute the SVD, and

estimate rank. The filter creates a new dimension called ``Rank``

that can be used downstream of this filter stage in the pipeline. The type of

writer used will determine whether or not the ``Rank`` dimension itself can be

saved to disk.



.. embed::



Example

-------



This sample pipeline estimates the rank of each point using this filter

and then filters out those points where the rank is three using

:ref:`filters.range`.



.. code-block:: json



  [

      "input.las",

      {

          "type":"filters.estimaterank",

          "knn":8,

          "thresh":0.01

      },

      {

          "type":"filters.range",

          "limits":"Rank![3:3]"

      },

      "output.laz"

  ]



Options

-------------------------------------------------------------------------------



_`knn`

  The number of k-nearest neighbors. [Default: 8]



_`thresh`

  The threshold used to identify nonzero singular values. [Default: 0.01]



.. include:: filter_opts.rst


    """

    vars = dict()
    vars['type'] = 'filters.estimaterank'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def faceraster(resolution=None, mesh=None, inputs=None, tag=None, **kwargs):
    """.. _filters.faceraster:



filters.faceraster

================================================================================



The **FaceRaster filter** creates a raster from a point cloud using an

algorithm based on an existing triangulation.  Each raster cell

is given a value that is an interpolation of the known values of the containing

triangle.  If the raster cell center is outside of the triangulation, it is

assigned the nodata_ value.  Use `writers.raster` to write the output.



The extent of the raster can be defined by using the origin_x_, origin_y_, width_ and

height_ options. If these options aren't provided the raster is sized to contain the

input data.



.. embed::





Basic Example

--------------------------------------------------------------------------------



This  pipeline reads the file autzen_trim.las and creates a raster based on a

Delaunay trianguation of the points. It then creates a raster, interpolating values

based on the vertices of the triangle that contains each raster cell center.



.. code-block:: json



  [

      "pdal/test/data/las/autzen_trim.las",

      {

          "type": "filters.delaunay"

      },

      {

          "type": "filters.faceraster",

          "resolution": 2,

          "width": 500,

          "height": 500,

          "origin_x": 636000,

          "origin_y": 849000

      }

  ]





Options

--------------------------------------------------------------------------------



.. _resolution:



resolution

    Length of raster cell edges in X/Y units.  [Required]



_`nodata`

    The value to use for a raster cell if no data exists in the input data

    with which to compute an output cell value. Note that this value may be

    different from the value used for nodata when the raster is written.

    [Default: NaN]



mesh

  Name of the triangulation to use for interpolation.  If not provided, the first

  triangulation associated with the input points will be used. [Default: None]

 

_`origin_x`

  X origin (lower left corner) of the grid. [Default: None]



_`origin_y`

  Y origin (lower left corner) of the grid. [Default: None]



_`width`

  Number of cells in the X direction. [Default: None]



_`height`

  Number of cells in the Y direction. [Default: None]



.. include:: filter_opts.rst


    """

    vars = dict()
    vars['type'] = 'filters.faceraster'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def ferry(dimensions=None, inputs=None, tag=None, **kwargs):
    """.. _filters.ferry:



filters.ferry

================================================================================



The ferry filter copies data from one dimension to another, creates new

dimensions or both.



The filter is guided by a list of 'from' and 'to' dimensions in the format

<from>=><to>.  Data from the 'from' dimension is copied to the 'to' dimension.

The 'from' dimension must exist.  The 'to' dimension can be pre-existing or

will be created by the ferry filter.



Alternatively, the format =><to> can be used to create a new dimension without

copying data from any source.  The values of the 'to' dimension are default

initialized (set to 0).



.. embed::



.. streamable::



Example 1

---------



In this scenario, we are making copies of the ``X`` and ``Y`` dimensions

into the

dimensions ``StatePlaneX`` and ``StatePlaneY``.  Since the reprojection

filter will

modify the dimensions ``X`` and ``Y``, this allows us to maintain both the

pre-reprojection values and the post-reprojection values.





.. code-block:: json



  [

      "uncompressed.las",

      {

          "type":"readers.las",

          "spatialreference":"EPSG:2993",

          "filename":"../las/1.2-with-color.las"

      },

      {

          "type":"filters.ferry",

          "dimensions":"X => StatePlaneX, Y=>StatePlaneY"

      },

      {

          "type":"filters.reprojection",

          "out_srs":"EPSG:4326+4326"

      },

      {

          "type":"writers.las",

          "scale_x":"0.0000001",

          "scale_y":"0.0000001",

          "filename":"colorized.las"

      }

  ]



Example 2

---------



The ferry filter is being used to add a dimension ``Classification`` to points

so that the value can be set to '2' and written as a LAS file.



.. code-block:: json



  [

      {

            "type": "readers.gdal",

            "filename": "somefile.tif"

      },

      {

            "type": "filters.ferry",

            "dimensions": "=>Classification"

      },

      {

            "type": "filters.assign",

            "assignment": "Classification[:]=2"

      },

      "out.las"

  ]



Options

-------



dimensions

  A list of dimensions whose values should be copied.

  The format of the option is <from>=><to>, <from>=><to>,...

  Spaces are ignored.

  'from' can be left empty, in which case the 'to' dimension is created and

  default-initialized.  'to' dimensions will be created if necessary.



  Note: the old syntax that used '=' instead of '=>' between dimension names

  is still supported.



.. include:: filter_opts.rst


    """

    vars = dict()
    vars['type'] = 'filters.ferry'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def fps(count=None, inputs=None, tag=None, **kwargs):
    """.. _filters.fps:



filters.fps

===============================================================================



The **Farthest Point Sampling Filter** adds points from the input to the output

``PointView`` one at a time by selecting the point from the input cloud that is

farthest from any point currently in the output.







.. seealso::



    :ref:`filters.sample` produces a similar result, but while

    ``filters.sample`` allows us to target a desired separation of points via

    the ``radius`` parameter at the expense of knowing the number of points in

    the output, ``filters.fps`` allows us to specify exactly the number of

    output points at the expense of knowing beforehand the spacing between

    points.



.. embed::



Options

-------------------------------------------------------------------------------



count

  Desired number of output samples. [Default: 1000]



.. include:: filter_opts.rst


    """

    vars = dict()
    vars['type'] = 'filters.fps'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def gpstimeconvert(conversion=None, inputs=None, tag=None, **kwargs):
    """.. _filters.gpstimeconvert:



filters.gpstimeconvert

======================



The **gpstimeconvert** filter converts between three GPS time standards found in

lidar data:



1. GPS time (gt)

2. GPS standard time (gst), also known as GPS adjusted time

3. GPS week seconds (gws)



Since GPS week seconds are ambiguous (they reset to 0 at the start of each new

GPS week), care must be taken when they are the source or destination of a

conversion:



* When converting from GPS week seconds, the GPS week number must be known. This

  is accomplished by specifying the start_date_ (in the GMT time zone) on which

  the data collection started. The filter will resolve the ambiguity using the

  supplied start date.

* When converting from GPS week seconds and the times span a new GPS week, the

  presence or absence of week second wrapping must be specified with the

  wrapped_ option. Wrapped week seconds reset to 0 at the start of a new week;

  unwrapped week seconds are allowed to exceed 604800 (60x60x24x7) seconds.

* When converting to GPS week seconds, the week second wrapping preference

  should be specified with the wrap_ option.



.. note::



  The filter assumes points are ordered by ascending time, which can be

  accomplished by running :ref:`filters.sort` prior to

  ``filters.gpstimeconvert``. Note that GPS week second times that span a new

  GPS week should not be sorted unless they are unwrapped.



Example #1

----------

Convert from GPS time to GPS standard time.



.. code-block:: json



  [

      "input.las",

      {

          "type":"filters.gpstimeconvert",

          "conversion":"gt2gst"

      },

      "output.las"

  ]



Example #2

----------

Convert from GPS standard time to unwrapped GPS week seconds.



.. code-block:: json



  [

      "input.las",

      {

          "type":"filters.sort",

          "dimension":"GpsTime",

          "order":"ASC"

      },

      {

          "type":"filters.gpstimeconvert",

          "conversion":"gst2gws",

          "wrap":false

      }

  ]



Example #3

----------

Convert from wrapped GPS week seconds to GPS time.



.. code-block:: json



  [

      "input.las",

      {

          "type":"filters.gpstimeconvert",

          "conversion":"gws2gt",

          "start_date":"2020-12-12",

          "wrapped":true

      },

      "output.las"

  ]



Options

-------



conversion

  The time conversion. Must be one of the following: "gst2gt", "gst2gws",

  "gt2gst", "gt2gws", "gws2gst", or "gws2gt". [Required]



_`start_date`

  When the input times are in GPS week seconds, the date on which the data

  collection started must be supplied in the GMT time zone. Must be in

  "YYYY-MM-DD" format. [Required for the "gws2gt" and "gws2gst" conversions]



_`wrap`

  Whether to output wrapped (true) or unwrapped (false) GPS week seconds.

  [Default: false]



_`wrapped`

  Specifies whether input GPS week seconds are wrapped (true) or unwrapped

  (false). [Default: false]
    """

    vars = dict()
    vars['type'] = 'filters.gpstimeconvert'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def greedyprojection(multiplier=None, radius=None, num_neighbors=None, min_angle=None, max_angle=None, eps_angle=None, inputs=None, tag=None, **kwargs):
    """.. _filters.greedyprojection:



filters.greedyprojection

===============================================================================



The **Greedy Projection Filter** creates a mesh (triangulation) in

an attempt to reconstruct the surface of an area from a collection of points.



GreedyProjectionTriangulation is an implementation of a greedy triangulation

algorithm for 3D points based on local 2D projections. It assumes locally

smooth

surfaces and relatively smooth transitions between areas with different point

densities.  The algorithm itself is identical to that used in the `PCL`_

library.



.. _PCL: http://www.pointclouds.org/documentation/tutorials/greedy_projection.php



.. embed::



Example

-------



.. code-block:: json



  [

      "input.las",

      {

          "type": "filters.greedyprojection",

          "multiplier": 2,

          "radius": 10

      },

      {

          "type":"writers.ply",

          "faces":true,

          "filename":"output.ply"

      }

  ]



Options

-------



multiplier

  Nearest neighbor distance multiplier. [Required]



radius

  Search radius for neighbors. [Required]



num_neighbors

  Number of nearest neighbors to consider. [Required]



min_angle

  Minimum angle for created triangles. [Default: 10 degrees]



max_angle

  Maximum angle for created triangles. [Default: 120 degrees]



eps_angle

  Maximum normal difference angle for triangulation consideration. [Default: 45 degrees]



.. include:: filter_opts.rst


    """

    vars = dict()
    vars['type'] = 'filters.greedyprojection'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def groupby(inputs=None, tag=None, **kwargs):
    """.. _filters.groupby:



filters.groupby

===============================================================================



The **Groupby Filter** takes a single ``PointView`` as its input and

creates a ``PointView`` for each category in the named dimension_ as

its output.



.. embed::



Example

-------



The following pipeline will create a set of LAS files, where each file contains

only points of a single ``Classification``.



.. code-block:: json



  [

      "input.las",

      {

          "type":"filters.groupby",

          "dimension":"Classification"

      },

      "output_#.las"

  ]



Options

-------



_`dimension`

  The dimension containing data to be grouped.



.. include:: filter_opts.rst


    """

    vars = dict()
    vars['type'] = 'filters.groupby'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def hag_delaunay(allow_extrapolation=None, inputs=None, tag=None, **kwargs):
    """.. _filters.hag_delaunay:



filters.hag_delaunay

===============================================================================



The **Height Above Ground Delaunay filter** takes as input a point cloud with

``Classification`` set to 2 for ground points.  It creates a new dimension,

``HeightAboveGround``, that contains the normalized height values.



.. note::



   We expect ground returns to have the classification value of 2 in keeping

   with the `ASPRS Standard LIDAR Point Classes

   <http://www.asprs.org/a/society/committees/standards/LAS_1_4_r13.pdf>`_.



Ground points may be generated by :ref:`filters.pmf` or :ref:`filters.smrf`,

but you can use any method you choose, as long as the ground returns are

marked.



Normalized heights are a commonly used attribute of point cloud data. This can

also be referred to as *height above ground* (HAG) or *above ground level*

(AGL) heights. In the end, it is simply a measure of a point's relative height

as opposed to its raw elevation value.



The filter creates a delaunay triangulation of the `count`_ ground points

closest to the non-ground point in question.  If the non-ground point is within

the triangulated area, the assigned ``HeightAboveGround`` is the difference

between its ``Z`` value and a ground height interpolated from the three

vertices of the containing triangle.  If the non-ground point is outside of the

triangulated area, its ``HeightAboveGround`` is calculated as the difference

between its ``Z`` value and the ``Z`` value of the nearest ground point.



Choosing a value for `count`_ is difficult, as placing the non-ground point in

the triangulated area depends on the layout of the nearby points.  If, for

example, all the ground points near a non-ground point lay on one side of that

non-ground point, finding a containing triangle will fail.



.. embed::



Example #1

----------



Using the autzen dataset (here shown colored by elevation), which already has

points classified as ground



.. image:: ./images/autzen-elevation.png

   :height: 400px



we execute the following pipeline



.. code-block:: json



  [

      "autzen.laz",

      {

          "type":"filters.hag_delaunay"

      },

      {

          "type":"writers.laz",

          "filename":"autzen_hag_delaunay.laz",

          "extra_dims":"HeightAboveGround=float32"

      }

  ]



which is equivalent to the ``pdal translate`` command



::



    $ pdal translate autzen.laz autzen_hag_delaunay.laz hag_delaunay \

        --writers.las.extra_dims="HeightAboveGround=float32"



In either case, the result, when colored by the normalized height instead of

elevation is



.. image:: ./images/autzen-hag-delaunay.png

   :height: 400px



Options

-------------------------------------------------------------------------------



_`count`

    The number of ground neighbors to consider when determining the height

    above ground for a non-ground point.  [Default: 10]



allow_extrapolation

    If false and a non-ground point lies outside of the bounding box of

    all ground points, its ``HeightAboveGround`` is set to 0.  If true

    and ``delaunay`` is set, the ``HeightAboveGround`` is set to the

    difference between the heights of the non-ground point and nearest

    ground point.  [Default: false]



.. include:: filter_opts.rst


    """

    vars = dict()
    vars['type'] = 'filters.hag_delaunay'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def hag_dem(band=None, zero_ground=None, inputs=None, tag=None, **kwargs):
    """.. _filters.hag_dem:



filters.hag_dem

===============================================================================



The **Height Above Ground (HAG) Digital Elevation Model (DEM) filter** loads

a GDAL-readable raster image specifying the DEM. The ``Z`` value of each point

in the input is compared against the value at the corresponding X,Y location

in the DEM raster. It creates a new dimension, ``HeightAboveGround``, that

contains the normalized height values.



Normalized heights are a commonly used attribute of point cloud data. This can

also be referred to as *height above ground* (HAG) or *above ground level* (AGL)

heights. In the end, it is simply a measure of a point's relative height as

opposed to its raw elevation value.



.. embed::



.. streamable::



Example #1

----------



Using the autzen dataset (here shown colored by elevation)



.. image:: ./images/autzen-elevation.png

   :height: 400px



we generate a DEM based on the points already classified as ground



::

  

    $ pdal translate autzen.laz autzen_dem.tif range \

        --filters.range.limits="Classification[2:2]" \

        --writers.gdal.output_type="idw" \

        --writers.gdal.resolution=6 \

        --writers.gdal.window_size=24



and execute the following pipeline



.. code-block:: json



  [

      "autzen.laz",

      {

          "type":"filters.hag_dem",

          "raster": "autzen_dem.tif"

      },

      {

          "type":"writers.las",

          "filename":"autzen_hag_dem.laz",

          "extra_dims":"HeightAboveGround=float32"

      }

  ]



which is equivalent to the ``pdal translate`` command



::



    $ pdal translate autzen.laz autzen_hag_dem.laz hag_dem \

        --filters.hag_dem.raster=autzen_dem.tif \

        --writers.las.extra_dims="HeightAboveGround=float32"



In either case, the result, when colored by the normalized height instead of

elevation is



.. image:: ./images/autzen-hag-dem.png

   :height: 400px



Options

-------------------------------------------------------------------------------



_`raster`

    GDAL-readable raster to use for DEM.



band

    GDAL Band number to read (count from 1).

    [Default: 1]



zero_ground

    If true, set HAG of ground-classified points to 0 rather than comparing

    ``Z`` value to raster DEM.

    [Default: true]



.. include:: filter_opts.rst


    """

    vars = dict()
    vars['type'] = 'filters.hag_dem'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def hag_nn(max_distance=None, allow_extrapolation=None, inputs=None, tag=None, **kwargs):
    """.. _filters.hag_nn:



filters.hag_nn

===============================================================================



The **Height Above Ground Nearest Neighbor filter** takes as input a point

cloud with ``Classification`` set to 2 for ground points.  It creates a new

dimension, ``HeightAboveGround``, that contains the normalized height values.



.. note::



   We expect ground returns to have the classification value of 2 in keeping

   with the `ASPRS Standard LIDAR Point Classes

   <http://www.asprs.org/a/society/committees/standards/LAS_1_4_r13.pdf>`_.



Ground points may be generated by :ref:`filters.pmf` or :ref:`filters.smrf`,

but you can use any method you choose, as long as the ground returns are

marked.



Normalized heights are a commonly used attribute of point cloud data. This can

also be referred to as *height above ground* (HAG) or *above ground level*

(AGL) heights. In the end, it is simply a measure of a point's relative height

as opposed to its raw elevation value.



The filter finds the `count`_ ground points nearest the non-ground point under

consideration.  It calculates an average ground height weighted by the distance

of each ground point from the non-ground point.  The ``HeightAboveGround`` is

the difference between the ``Z`` value of the non-ground point and the

interpolated ground height.



.. embed::



Example #1

----------



Using the autzen dataset (here shown colored by elevation), which already has

points classified as ground



.. image:: ./images/autzen-elevation.png

   :height: 400px



we execute the following pipeline



.. code-block:: json



  [

      "autzen.laz",

      {

          "type":"filters.hag_nn"

      },

      {

          "type":"writers.laz",

          "filename":"autzen_hag_nn.laz",

          "extra_dims":"HeightAboveGround=float32"

      }

  ]



which is equivalent to the ``pdal translate`` command



::



    $ pdal translate autzen.laz autzen_hag_nn.laz hag_nn \

        --writers.las.extra_dims="HeightAboveGround=float32"



In either case, the result, when colored by the normalized height instead of

elevation is



.. image:: ./images/autzen-hag-nn.png

   :height: 400px



Example #2

-------------------------------------------------------------------------------



In the previous example, we chose to write ``HeightAboveGround`` using the

``extra_dims`` option of :ref:`writers.las`. If you'd instead like to overwrite

your Z values, then follow the height filter with :ref:`filters.ferry` as shown



.. code-block:: json



  [

      "autzen.laz",

      {

          "type":"filters.hag_nn"

      },

      {

          "type":"filters.ferry",

          "dimensions":"HeightAboveGround=>Z"

      },

      "autzen-height-as-Z.laz"

  ]





Example #3

-------------------------------------------------------------------------------



If you don't yet have points classified as ground, start with :ref:`filters.pmf`

or :ref:`filters.smrf` to label ground returns, as shown



.. code-block:: json



  [

      "autzen.laz",

      {

          "type":"filters.smrf"

      },

      {

          "type":"filters.hag_nn"

      },

      {

          "type":"filters.ferry",

          "dimensions":"HeightAboveGround=>Z"

      },

      "autzen-height-as-Z-smrf.laz"

  ]



Options

-------------------------------------------------------------------------------



_`count`

    The number of ground neighbors to consider when determining the height

    above ground for a non-ground point.  [Default: 1]



max_distance

    Use only ground points within `max_distance` of non-ground point when

    performing neighbor interpolation.  [Default: None]



allow_extrapolation

    If false and a non-ground point lies outside of the bounding box of all

    ground points, its ``HeightAboveGround`` is set to 0.  If true,

    extrapolation is used to assign the ``HeightAboveGround`` value.  [Default:

    false]



.. include:: filter_opts.rst


    """

    vars = dict()
    vars['type'] = 'filters.hag_nn'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def head(count=None, inputs=None, tag=None, **kwargs):
    """.. _filters.head:



filters.head

===============================================================================



The **Head filter** returns a specified number of points from the beginning

of a ``PointView``.



.. note::



    If the requested number of points exceeds the size of the point cloud, all

    points are passed with a warning.



.. embed::





Example #1

----------



Thin a point cloud by first shuffling the point order with

:ref:`filters.randomize` and then picking the first 10000 using the HeadFilter.





.. code-block:: json



  [

      {

          "type":"filters.randomize"

      },

      {

          "type":"filters.head",

          "count":10000

      }

  ]





Example #2

----------



Compute height above ground and extract the ten highest points.





.. code-block:: json



  [

      {

          "type":"filters.smrf"

      },

      {

          "type":"filters.hag_nn"

      },

      {

          "type":"filters.sort",

          "dimension":"HeightAboveGround",

          "order":"DESC"

      },

      {

          "type":"filters.head",

          "count":10

      }

  ]



.. seealso::



    :ref:`filters.tail` is the dual to :ref:`filters.head`.





Options

-------------------------------------------------------------------------------



count

  Number of points to return. [Default: 10]



.. include:: filter_opts.rst


    """

    vars = dict()
    vars['type'] = 'filters.head'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def hexbin(sample_size=None, threshold=None, precision=None, preserve_topology=None, smooth=None, inputs=None, tag=None, **kwargs):
    """.. _filters.hexbin:



filters.hexbin

==============



A common questions for users of point clouds is what the spatial extent of a

point cloud collection is. Files generally provide only rectangular bounds, but

often the points inside the files only fill up a small percentage of the area

within the bounds.



.. figure:: filters.hexbin.img1.jpg

    :scale: 50 %

    :alt: Hexbin derived from input point buffer



    Hexbin output shows boundary of actual points in point buffer, not

    just rectangular extents.



The hexbin filter reads a point stream and writes out a metadata record that

contains a boundary, expressed as a well-known text polygon. The filter counts

the points in each hexagonal area to determine if that area should be included

as part of the boundary.  In

order to write out the metadata record, the *pdal* pipeline command must be

invoked using the "--pipeline-serialization" option:



.. streamable::



Example 1

---------



The following pipeline file and command produces an JSON output file

containing the pipeline's metadata, which includes the result of running

the hexbin filter:



::



  [

      "/Users/me/pdal/test/data/las/autzen_trim.las",

      {

          "type" : "filters.hexbin"

      }

  ]



::



  $ pdal pipeline hexbin-pipeline.json --metadata hexbin-out.json





.. code-block:: none



    {

      "stages":

      {

        "filters.hexbin":

        {

          "area": 746772.7543,

          "avg_pt_per_sq_unit": 22.43269935,

          "avg_pt_spacing": 2.605540869,

          "boundary": "MULTIPOLYGON (((636274.38924399 848834.99817891, 637242.52219686 848834.99817891, 637274.79329529 849226.26445367, 637145.70890157 849338.05481789, 637242.52219686 849505.74036422, 636016.22045656 849505.74036422, 635983.94935813 849114.47408945, 636113.03375184 848890.89336102, 636274.38924399 848834.99817891)))",

          "boundary_json": { "type": "MultiPolygon", "coordinates": [ [ [ [ 636274.38924399, 848834.99817891 ], [ 637242.52219686, 848834.99817891 ], [ 637274.79329529, 849226.26445367 ], [ 637145.70890157, 849338.05481789 ], [ 637242.52219686, 849505.74036422 ], [ 636016.22045656, 849505.74036422 ], [ 635983.94935813, 849114.47408945 ], [ 636113.03375184, 848890.89336102 ], [ 636274.38924399, 848834.99817891 ] ] ] ] },

          "density": 0.1473004999,

          "edge_length": 0,

          "estimated_edge": 111.7903642,

          "hex_offsets": "MULTIPOINT (0 0, -32.2711 55.8952, 0 111.79, 64.5422 111.79, 96.8133 55.8952, 64.5422 0)",

          "sample_size": 5000,

          "threshold": 15

        }

    },

    ...





Example 2

---------



As a convenience, the ``pdal info`` command will produce similar output:



::



    $ pdal info --boundary /Users/me/test/data/las/autzen_trim.las



.. code-block:: json



    {

      "boundary":

      {

        "area": 746772.7543,

        "avg_pt_per_sq_unit": 22.43269935,

        "avg_pt_spacing": 2.605540869,

        "boundary": "MULTIPOLYGON (((636274.38924399 848834.99817891, 637242.52219686 848834.99817891, 637274.79329529 849226.26445367, 637145.70890157 849338.05481789, 637242.52219686 849505.74036422, 636016.22045656 849505.74036422, 635983.94935813 849114.47408945, 636113.03375184 848890.89336102, 636274.38924399 848834.99817891)))",

        "boundary_json": { "type": "MultiPolygon", "coordinates": [ [ [ [ 636274.38924399, 848834.99817891 ], [ 637242.52219686, 848834.99817891 ], [ 637274.79329529, 849226.26445367 ], [ 637145.70890157, 849338.05481789 ], [ 637242.52219686, 849505.74036422 ], [ 636016.22045656, 849505.74036422 ], [ 635983.94935813, 849114.47408945 ], [ 636113.03375184, 848890.89336102 ], [ 636274.38924399, 848834.99817891 ] ] ] ] },

        "density": 0.1473004999,

        "edge_length": 0,

        "estimated_edge": 111.7903642,

        "hex_offsets": "MULTIPOINT (0 0, -32.2711 55.8952, 0 111.79, 64.5422 111.79, 96.8133 55.8952, 64.5422 0)",

        "sample_size": 5000,

        "threshold": 15

      },

      "filename": "\/Users\/acbell\/pdal\/test\/data\/las\/autzen_trim.las",

      "pdal_version": "1.6.0 (git-version: 675afe)"

    }



Options

-------



_`edge_size`

  If not set, the hexbin filter will estimate a hex size based on a sample of

  the data. If set, hexbin will use the provided size in constructing the

  hexbins to test.



sample_size

  How many points to sample when automatically calculating the edge

  size? Only applies if edge_size_ is not explicitly set. [Default: 5000]



threshold

  Number of points that have to fall within a hexagon boundary before it

  is considered "in" the data set. [Default: 15]



precision

  Minimum number of significant digits to use in writing out the

  well-known text of the boundary polygon. [Default: 8]



preserve_topology

  Use GEOS SimplifyPreserveTopology instead of Simplify for polygon simplification with  `smooth` option. [Default: true]



smooth

  Use GEOS simplify operations to smooth boundary to a tolerance [Default: true]



.. include:: filter_opts.rst


    """

    vars = dict()
    vars['type'] = 'filters.hexbin'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def icp(max_iter=None, max_similar=None, mse_abs=None, rt=None, tt=None, inputs=None, tag=None, **kwargs):
    """.. _filters.icp:



filters.icp

==============



The **ICP filter** uses the Iterative Closest Point (ICP) algorithm to

calculate a **rigid** (rotation and translation) transformation that best

aligns two datasets.  The first input to the ICP filter is considered the

"fixed" points, and all subsequent points are "moving" points.  The output from

the filter are the "moving" points after the calculated transformation has been

applied, one point view per input.  The transformation matrix is inserted into

the stage's metadata.



.. note::



    ICP requires the initial pose of the two point sets to be adequately close,

    which is not always possible, especially when the transformation is

    non-rigid.  ICP can handle limited non-rigid transformations but be aware

    ICP may be unable to escape a local minimum. Consider using CPD instead.



    From :cite:`Xuechen2019`:



    ICP starts with an initial guess of the transformation between the two

    point sets and then iterates between finding the correspondence under the

    current transformation and updating the transformation with the newly found

    correspondence. ICP is widely used because it is rather straightforward and

    easy to implement in practice; however, its biggest problem is that it does

    not guarantee finding the globally optimal transformation. In fact, ICP

    converges within a very small basin in the parameter space, and it easily

    becomes trapped in local minima. Therefore, the results of ICP are very

    sensitive to the initialization, especially when high levels of noise and

    large proportions of outliers exist.





Examples

--------



.. code-block:: json



  [

      "fixed.las",

      "moving.las",

      {

          "type": "filters.icp"

      },

      "output.las"

  ]



To get the ``transform`` matrix, you'll need to use the ``--metadata`` option

from the pipeline command:



::



    $ pdal pipeline icp-pipeline.json --metadata icp-metadata.json



The metadata output might start something like:



.. code-block:: json



    {

        "stages":

        {

            "filters.icp":

            {

                "centroid": "    583394  5.2831e+06   498.152",

                "composed": "           1  2.60209e-18 -1.97906e-09       -0.374999  8.9407e-08            1  5.58794e-09      -0.614662 6.98492e-10 -5.58794e-09            1   0.033234           0            0            0            1",

                "converged": true,

                "fitness": 0.01953125097,

                "transform": "           1  2.60209e-18 -1.97906e-09       -0.375  8.9407e-08            1  5.58794e-09      -0.5625 6.98492e-10 -5.58794e-09            1   0.00411987           0            0            0            1"

            }





To apply this transformation to other points, the ``centroid`` and ``transform``

metadata items can by used with ``filters.transformation`` in another pipeline.  First,

move the centroid of the points to (0,0,0), then apply the transform, then move

the points back to the original location.  For the above metadata, the pipeline

would be similar to:



.. code-block:: json



    [

        {

            "type": "readers.las",

            "filename": "in.las"

        },

        {

            "type": "filters.transformation",

            "matrix": "1 0 0 -583394   0 1 0 -5.2831e+06   0 0 1 -498.152   0 0 0 1"

        },

        {

            "type": "filters.transformation",

            "matrix": "1  2.60209e-18 -1.97906e-09       -0.375  8.9407e-08            1  5.58794e-09      -0.5625 6.98492e-10 -5.58794e-09            1   0.00411987           0            0            0            1"

        },

        {

            "type": "filters.transformation",

            "matrix": "1 0 0 583394   0 1 0 5.2831e+06  0 0 1 498.152  0 0 0 1"

        },

        {

            "type": "writers.las",

            "filename": "out.las"

        }

    ]



.. note::



    The ``composed`` metadata matrix is a composition of the three transformation steps outlined above, and can be used in a single call to ``filters.transformation`` as opposed to the three separate calls.



.. seealso::



    :ref:`filters.transformation` to apply a transform to other points.

    :ref:`filters.cpd` for the use of a probabilistic assignment of correspondences between pointsets.





Options

--------



max_iter

  Maximum number of iterations. [Default: **100**]



max_similar

  Max number of similar transforms to consider converged. [Default: **0**]



mse_abs

  Absolute threshold for MSE. [Default: **1e-12**]



rt

  Rotation threshold. [Default: **0.99999**]



tt

  Translation threshold. [Default: **9e-8**]



.. include:: filter_opts.rst


    """

    vars = dict()
    vars['type'] = 'filters.icp'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def info(inputs=None, tag=None, **kwargs):
    """.. _filters.info:



filters.info

======================



The **Info filter** provides simple information on a point set as metadata.

It is usually invoked by the info command, rather than by user code.

The data provided includes bounds, a count of points, dimension names,

spatial reference, and points meeting a query criteria.



.. embed::



.. streamable::



.. code-block:: json



  [

      "input.las",

      {

          "type":"filters.info",

          "point":"1-5"

      }

  ]



Options

-------



_`point`

  A comma-separated list of single point IDs or ranges of points.  For

  example "2-6, 10, 25" selects eight points from the input set.  The first

  point has an ID of 0.  The point_ option can't be used with the query_ option.

  [Default: no points are selected.]



_`query`

  A specification to retrieve points near a location.  Syntax of the the

  query is X,Y[,Z][/count] where 'X', 'Y' and 'Z' are coordinate

  locations mapping to the X, Y and Z point dimension and 'count' is the

  number of points to return.  If 'count' isn't specified, the 10 points

  nearest to the location are returned.  The query_ option can't be used

  with the point_ option. [Default: no points are selected.]



.. include:: filter_opts.rst


    """

    vars = dict()
    vars['type'] = 'filters.info'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def iqr(k=None, dimension=None, inputs=None, tag=None, **kwargs):
    """.. _filters.iqr:



filters.iqr

===============================================================================



The **Interquartile Range Filter** automatically crops the input point

cloud based on the distribution of points in the specified dimension.

The Interquartile Range (IQR) is defined as the range between

the first and third quartile (25th and 75th percentile). Upper and lower bounds

are determined by adding 1.5 times the IQR to the third quartile or subtracting

1.5 times the IQR from the first quartile. The multiplier, which defaults to

1.5, can be adjusted by the user.



.. note::



  This method can remove real data, especially ridges and valleys in rugged

  terrain, or tall features such as towers and rooftops in flat terrain. While

  the number of deviations can be adjusted to account for such content-specific

  considerations, it must be used with care.



.. embed::



Example

-------



The sample pipeline below uses the filter to automatically crop the Z

dimension and remove possible outliers. The multiplier to determine high/low

thresholds has been adjusted to be less aggressive and to only crop those

outliers that are greater than the third quartile plus 3 times the IQR or are

less than the first quartile minus 3 times the IQR.



.. code-block:: json



  [

      "input.las",

      {

          "type":"filters.iqr",

          "dimension":"Z",

          "k":3.0

      },

      "output.laz"

  ]



Options

-------------------------------------------------------------------------------



k

  The IQR multiplier used to determine upper/lower bounds. [Default: 1.5]



dimension

  The name of the dimension to filter.



.. include:: filter_opts.rst


    """

    vars = dict()
    vars['type'] = 'filters.iqr'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def julia(script=None, source=None, module=None, function=None, inputs=None, tag=None, **kwargs):
    """.. _filters.julia:



filters.julia

==============



The **Julia Filter** allows `Julia`_ software to be embedded in a

:ref:`pipeline` that allows modification of PDAL points through a `TypedTables`_

datatype.



The supplied julia function must take a `TypedTables`_ FlexTable as an argument

and return the same object (with modifications).



.. warning::



    The returned Table contains all the :ref:`dimensions` of the incoming ``ins`` Table



.. plugin::



.. code-block:: julia



  module MyModule

    using TypedTables



    function multiply_z(ins)

      for n in 1:length(ins)

        ins[n] = merge(ins[n], (; :Z => row.Z * 10.0)

      end

      return ins

    end

  end





 If you want write a dimension that might not be available, you can specify

 it with the add_dimension_ option:



   ::



       "add_dimension": "NewDimensionOne"



 To create more than one dimension, this option also accepts an array:



   ::



       "add_dimension": [ "NewDimensionOne", "NewDimensionTwo", "NewDimensionThree" ]





 You can also specify the :ref:`type <types>` of the dimension using an ``=``.

   ::



       "add_dimension": "NewDimensionOne=uint8"





Filter Example

--------------------------------------------------------------------------------



.. code-block:: json



  [

      "file-input.las",

      {

          "type":"filters.smrf"

      },

      {

          "type":"filters.julia",

          "script":"filter_z.jl",

          "function":"filter_z",

          "module":"MyModule"

      },

      {

          "type":"writers.las",

          "filename":"file-filtered.las"

      }

  ]



The JSON pipeline file referenced the external `filter_z.jl` `Julia`_ script,

which removes points with the ``Z`` coordinate by less than 420.



.. code-block:: julia



  module MyModule

    using TypedTables



    function filter_z(ins)

      return filter(p -> p.Z > 420, ins)

    end

  end



Modification Example

--------------------------------------------------------------------------------



.. code-block:: json



  [

      "file-input.las",

      {

          "type":"filters.smrf"

      },

      {

          "type":"filters.julia",

          "script":"multiply_z.jl",

          "function":"multiply_z",

          "module":"MyModule"

      },

      {

          "type":"writers.las",

          "filename":"file-modified.las"

      }

  ]



The JSON pipeline file referenced the external `multiply_z.jl` `Julia`_ script,

which scales the ``Z`` coordinate by a factor of 10.



.. code-block:: julia



  module MyModule

    using TypedTables



    function multiply_z(ins)

      for n in 1:length(ins)

        ins[n] = merge(ins[n], (; :Z => row.Z * 10.0)

      end

      return ins

    end

  end



Options

--------------------------------------------------------------------------------



script

  When reading a function from a separate `Julia`_ file, the file name to read

  from.



source

  The literal `Julia`_ code to execute, when the script option is

  not being used.



module

  The Julia module that is holding the function to run. [Required]



function

  The function to call. [Required]



_`add_dimension`

  A dimension name or an array of dimension names to add to the pipeline that do not already exist.



.. include:: filter_opts.rst



.. _Julia: https://julialang.org/

.. _TypedTables: https://github.com/JuliaData/TypedTables.jl
    """

    vars = dict()
    vars['type'] = 'filters.julia'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def litree(min_points=None, min_height=None, radius=None, inputs=None, tag=None, **kwargs):
    """.. _filters.litree:



===============================================================================

filters.litree

===============================================================================



The purpose of the Li tree filter is to segment individual trees from an input

``PointView``. In the output ``PointView`` points that are deemed to be part of

a tree are labeled with a ``ClusterID``. Tree IDs start at 1, with non-tree points

given a ``ClusterID`` of 0.



.. note::



  The filter differs only slightly from the paper in the addition of a few

  conditions on size of tree, minimum height above ground for tree seeding, and

  flexible radius for non-tree seed insertion.



.. note::



  In earlier PDAL releases (up to v2.2.0), ``ClusterID`` was stored in the

  ``TreeID`` Dimemsion.



.. embed::



Example

-------



The Li tree algorithm expects to visit points in descending order of

``HeightAboveGround``, which is also used in determining the minimum tree

height to consider. As such, the following pipeline precomputes

``HeightAboveGround`` using :ref:`filters.hag_delaunay` and subsequently sorts

the ``PointView`` using this dimension.



.. code-block:: json



  [

      "input.las",

      {

          "type":"filters.hag_delaunay"

      },

      {

          "type":"filters.sort",

          "dimension":"HeightAboveGround",

          "order":"DESC"

      },

      {

          "type":"filters.litree",

          "min_points":50,

          "min_height":10.0,

          "radius":200.0

      },

      {

          "type":"writers.las",

          "filename":"output.laz",

          "minor_version":1.4,

          "extra_dims":"all"

      }

  ]



Options

-------



min_points

  Minimum number of points in a tree cluster. [Default: 10]



min_height

  Minimum height above ground to start a tree cluster. [Default: 3.0]



radius

  The seed point for the non-tree cluster is the farthest point in a 2D

  Euclidean sense from the seed point for the current tree. [Default: 100.0]



.. include:: filter_opts.rst


    """

    vars = dict()
    vars['type'] = 'filters.litree'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def lloydkmeans(k=None, maxiters=None, dimensions=None, inputs=None, tag=None, **kwargs):
    """.. _filters.lloydkmeans:



===============================================================================

filters.lloydkmeans

===============================================================================



K-means clustering using Lloyd's algorithm labels each point with its

associated cluster ID (starting at 0).



.. embed::



.. versionadded:: 2.1



Example

-------



.. code-block:: json



  [

      "input.las",

      {

          "type":"filters.lloydkmeans",

          "k":10,

          "maxiters":20,

          "dimensions":"X,Y,Z"

      },

      {

          "type":"writers.las",

          "filename":"output.laz",

          "minor_version":4,

          "extra_dims":"all"

      }

  ]



Options

-------



k

  The desired number of clusters. [Default: 10]



maxiters

  The maximum number of iterations. [Default: 10]



dimensions

  Comma-separated string indicating dimensions to use for clustering.

  [Default: X,Y,Z]



.. include:: filter_opts.rst


    """

    vars = dict()
    vars['type'] = 'filters.lloydkmeans'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def locate(minmax=None, inputs=None, tag=None, **kwargs):
    """.. _filters.locate:



filters.locate

===============================================================================



The Locate filter searches the specified dimension_ for the minimum or

maximum value and returns a single point at this location. If multiple points

share the min/max value, the first will be returned. All dimensions of the

input ``PointView`` will be output, subject to any overriding writer options.



.. embed::



Example

-------



This example returns the point at the highest elevation.



.. code-block:: json



  [

      "input.las",

      {

          "type":"filters.locate",

          "dimension":"Z",

          "minmax":"max"

      },

      "output.las"

  ]



Options

-------



_`dimension`

  Name of the dimension in which to search for min/max value.



minmax

  Whether to return the minimum or maximum value in the dimension.



.. include:: filter_opts.rst


    """

    vars = dict()
    vars['type'] = 'filters.locate'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def lof(inputs=None, tag=None, **kwargs):
    """.. _filters.lof:



filters.lof

===============================================================================



The **Local Outlier Factor (LOF) filter** was introduced as a method

of determining the degree to which an object is an outlier. This filter

is an implementation of the method

described in [Breunig2000]_.



The filter creates three new dimensions, ``NNDistance``,

``LocalReachabilityDistance`` and ``LocalOutlierFactor``, all of which are

double-precision floating values. The ``NNDistance`` dimension records the

Euclidean distance between a point and it's k-th nearest neighbor (the number

of k neighbors is set with the minpts_ option). The

``LocalReachabilityDistance`` is the inverse of the mean

of all reachability distances for a neighborhood of points. This reachability

distance is defined as the max of the Euclidean distance to a neighboring point

and that neighbor's own previously computed ``NNDistance``. Finally, each point

has a ``LocalOutlierFactor`` which is the mean of all

``LocalReachabilityDistance`` values for the neighborhood. In each case, the

neighborhood is the set of k nearest neighbors.



In practice, setting the minpts_ parameter appropriately and subsequently

filtering outliers based on the computed ``LocalOutlierFactor`` can be

difficult. The authors present some work on establishing upper and lower bounds

on LOF values, and provide some guidelines on selecting minpts_ values, which

users of this filter should find instructive.



.. note::



  To inspect the newly created, non-standard dimensions, be sure to write to an

  output format that can support arbitrary dimensions, such as BPF.



.. note::



  In earlier PDAL releases (up to v2.2.0), ``NNDistance`` was stored in the

  ``KDistance`` Dimemsion.



.. embed::



Example

-------



The sample pipeline below computes the LOF with a neighborhood of 20 neighbors,

followed by a range filter to crop out points whose ``LocalOutlierFactor``

exceeds 1.2 before writing the output.



.. code-block:: json



  [

      "input.las",

      {

          "type":"filters.lof",

          "minpts":20

      },

      {

          "type":"filters.range",

          "limits":"LocalOutlierFactor[:1.2]"

      },

      "output.laz"

  ]



Options

-------------------------------------------------------------------------------



_`minpts`

  The number of k nearest neighbors. [Default: 10]



.. include:: filter_opts.rst


    """

    vars = dict()
    vars['type'] = 'filters.lof'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def mad(k=None, inputs=None, tag=None, **kwargs):
    """.. _filters.mad:



filters.mad

===============================================================================



The **MAD filter** filter crops the input point cloud based on

the distribution of points in the specified dimension_. Specifically, we choose

the method of median absolute deviation from the median (commonly referred to

as

MAD), which is robust to outliers (as opposed to mean and standard deviation).



.. note::



  This method can remove real data, especially ridges and valleys in rugged

  terrain, or tall features such as towers and rooftops in flat terrain. While

  the number of deviations can be adjusted to account for such content-specific

  considerations, it must be used with care.



.. embed::



Example

-------



The sample pipeline below uses filters.mad to automatically crop the ``Z``

dimension and remove possible outliers. The number of deviations from the

median has been adjusted to be less aggressive and to only crop those outliers

that are greater than four deviations from the median.



.. code-block:: json



  [

      "input.las",

      {

          "type":"filters.mad",

          "dimension":"Z",

          "k":4.0

      },

      "output.laz"

  ]



Options

-------------------------------------------------------------------------------



k

  The number of deviations from the median. [Default: 2.0]



_`dimension`

  The name of the dimension to filter.



.. include:: filter_opts.rst


    """

    vars = dict()
    vars['type'] = 'filters.mad'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def matlab(script=None, source=None, add_dimension=None, struct=None, inputs=None, tag=None, **kwargs):
    """.. _filters.matlab:



filters.matlab

====================



The **Matlab Filter** allows `Matlab`_ software to be embedded in a

:ref:`pipeline` that interacts with a struct array of the data and allows

you to modify those points. Additionally, some global :ref:`metadata` is also

available that Matlab functions can interact with.



The Matlab interpreter must exit and always set "ans==true" upon success. If

"ans==false", an error would be thrown and the :ref:`pipeline` exited.



.. seealso::

    :ref:`writers.matlab` can be used to write ``.mat`` files.





.. note::

    :ref:`filters.matlab` embeds the entire Matlab interpreter, and it

    will require a fully licensed version of Matlab to execute your script.



.. plugin::



Example

-------



.. code-block:: json



  [

      {

          "filename": "test\/data\/las\/1.2-with-color.las",

          "type": "readers.las"



      },

      {

          "type": "filters.matlab",

          "script": "matlab.m"



      },

      {

          "filename": "out.las",

          "type": "writers.las"

      }

  ]



Options

-------



script

  When reading a function from a separate `Matlab`_ file, the file name to read

  from. [Example: "functions.m"]



source

  The literal `Matlab`_ code to execute, when the script option is not

  being used.



add_dimension

  The name of a dimension to add to the pipeline that does not already exist.



struct

  Array structure name to read [Default: "PDAL"]



.. include:: filter_opts.rst



.. _Matlab: https://www.mathworks.com/products/matlab.html
    """

    vars = dict()
    vars['type'] = 'filters.matlab'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def merge(inputs=None, tag=None, **kwargs):
    """.. _filters.merge:



filters.merge

===============================================================================



The **Merge Filter** combines input from multiple sources into a single output.

In most cases, this happens automatically on output and use of the merge

filter is unnecessary.  However, there may be special cases where

merging points prior to a particular filter or writer is necessary

or desirable.



The merge filter will log a warning if its input point sets are based on

different spatial references.  No checks are made to ensure that points

from various sources being merged have similar dimensions or are generally

compatible.



.. embed::



Example 1

---------



This pipeline will create an output file "output.las" that contcatenates

the points from "file1", "file2" and "file3".  Note that the explicit

use of the merge filter is unnecessary in this case (removing the merge

filter will yield the same result).



.. code-block:: json



  [

      "file1",

      "file2",

      "file3",

      {

          "type": "filters.merge"

      },

      "output.las"

  ]



Example 2

---------



Here are a pair of unlikely pipelines that show one way in which a merge filter

might be used.  The first pipeline simply reads the input files "utm1.las",

"utm2.las" and "utm3.las".  Since the points from each input set are

carried separately through the pipeline, three files are created as output,

"out1.las", "out2.las" and "out3.las".  "out1.las" contains the points

in "utm1.las".  "out2.las" contains the points in "utm2.las" and "out3.las"

contains the points in "utm3.las".



.. code-block:: json



  [

      "utm1.las",

      "utm2.las",

      "utm3.las",

      "out#.las"

  ]



Here is the same pipeline with a merge filter added.  The merge filter will

combine the points in its input: "utm1.las" and "utm2.las".  Then the result

of the merge filter is passed to the writer along with "utm3.las".  This

results in two output files: "out1.las" contains the points from "utm1.las"

and "utm2.las", while "out2.las" contains the points from "utm3.las".



.. code-block:: json



  [

      "utm1.las",

      "utm2.las",

      {

          "type" : "filters.merge"

      },

      "utm3.las",

      "out#.las"

  ]



Options

-------



.. include:: filter_opts.rst


    """

    vars = dict()
    vars['type'] = 'filters.merge'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def miniball(knn=None, inputs=None, tag=None, **kwargs):
    """.. _filters.miniball:



filters.miniball

===============================================================================



The **Miniball Criterion** was introduced in [Weyrich2004]_ and is based on the

assumption that points that are distant to the cluster built by their

k-neighborhood are likely to be outliers. First, the smallest enclosing ball is

computed for the k-neighborhood, giving a center point and radius

[Fischer2010]_. The miniball criterion is then computed by comparing the

distance (from the current point to the miniball center) to the radius of the

miniball.



The author suggests that the Miniball Criterion is more robust than the

:ref:`Plane Fit Criterion <filters.planefit>` around high-frequency details,

but demonstrates poor outlier detection for points close to a smooth surface.



The filter creates a single new dimension, ``Miniball``, that records the

Miniball criterion for the current point.



.. note::



  To inspect the newly created, non-standard dimensions, be sure to write to an

  output format that can support arbitrary dimensions, such as BPF.



.. embed::



Example

-------



The sample pipeline below computes the Miniball criterion with a neighborhood

of 8 neighbors. We do not apply a fixed threshold to single out outliers based

on the Miniball criterion as the range of values can vary from one dataset to

another. In general, higher values indicate the likelihood of a point being an

outlier.



.. code-block:: json



  [

      "input.las",

      {

          "type":"filters.miniball",

          "knn":8

      },

      "output.laz"

  ]



Options

-------------------------------------------------------------------------------



knn

  The number of k nearest neighbors. [Default: 8]



.. include:: filter_opts.rst


    """

    vars = dict()
    vars['type'] = 'filters.miniball'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def mongo(expression=None, Expression=None, inputs=None, tag=None, **kwargs):
    """.. _filters.mongo:



filters.mongo

========================



The **Mongo Filter** applies query logic to the input

point cloud based on a MongoDB-style query expression using the

point cloud attributes.



.. embed::



.. streamable::



Example

-------



This example passes through only the points whose Classification is non-zero.



.. code-block:: json



    [

        "input.las",

        {

            "type": "filters.mongo",

            "expression": {

                "Classification": { "$ne": 0 }

            }

        },

        "filtered.las"

    ]



This example passes through only the points whose ``ReturnNumber``

is equal to the ``NumberOfReturns`` and the ``NumberOfReturns``

is greater than 1.



.. code-block:: json



    [

        "input.las",

        {

            "type": "filters.mongo",

            "expression": { "$and": [

                { "ReturnNumber": "NumberOfReturns" },

                { "NumberOfReturns": { "$gt": 1 } }

            ] }

        },

        "filtered.las"

    ]



Options

-------



expression

    A JSON query :ref:`expression <Mongo expression>` containing a combination of query comparisons

    and logical operators.



.. include:: filter_opts.rst



.. _Mongo expression:



Expression

--------------------------------------------------------------------------------



A query expression is a combination of comparison and logical operators that

define a query which can be used to select matching points by their attribute

values.



Comparison operators

................................................................................



There are 8 valid query comparison operators:



    - ``$eq``: Matches values equal to a specified value.

    - ``$gt``: Matches values greater than a specified value.

    - ``$gte``: Matches values greater than or equal to a specified value.

    - ``$lt``: Matches values less than a specified value.

    - ``$lte``: Matches values less than or equal to a specified value.

    - ``$ne``: Matches values not equal to a specified value.

    - ``$in``: Matches any of the values specified in the array.

    - ``$nin``: Matches none of the values specified in the array.



Comparison operators compare a point cloud attribute with an operand or an

array of operands.  An *operand* is either a numeric constant or a string

representing a dimension name.  For all comparison operators except for ``$in``

and ``$nin``, the comparison value must be a single operand.  For ``$in`` and

``$nin``, the value must be an array of operands.



Comparison operator specifications must be contained within an object whose key

is the dimension name to be compared.



.. code-block:: json



    { "Classification": { "$eq": 2 } }



.. code-block:: json



    { "Intensity": { "$gt": 0 } }



.. code-block:: json



    { "Classification": { "$in": [2, 6, 9] } }



The ``$eq`` comparison operator may be implicitly invoked by setting an

attribute name directly to a value.



.. code-block:: json



    { "Classification": 2 }



Logical operators

................................................................................



There are 4 valid logical operators:



    - ``$and``: Applies a logical **and** on the expressions of the array and

      returns a match only if all expressions match.

    - ``$not``: Inverts the value of the single sub-expression.

    - ``$nor``: Applies a logical **nor** on the expressions of the array and

      returns a match only if all expressions fail to match.

    - ``$nor``: Applies a logical **or** on the expressions of the array and

      returns a match if any of the expressions match.



Logical operators are used to logically combine sub-expressions.  All logical

operators except for ``$not`` are applied to arrays of expressions.

``$not`` is applied to a single expression and negates its result.



Logical operators may be applied directly to comparison expressions or may

contain further nested logical operators.  For example:



.. code-block:: json



    { "$or": [

        { "Classification": 2 },

        { "Intensity": { "$gt": 0 } }

    ] }



.. code-block:: json



    { "$or": [

        { "Classification": 2 },

        { "$and": [

            { "ReturnNumber": "NumberOfReturns" },

            { "NumberOfReturns": { "$gt": 1 } }

        ] }

    ] }



.. code-block:: json



    { "$not": {

        "$or": [

            { "Classification": 2 },

            { "$and": [

                { "ReturnNumber": { "$gt": 0 } },

                { "Z": { "$lte": 42 } }

            ] }

        ] }

    }



For any individual dimension, the logical **and** may be implicitly invoked

via multiple comparisons within the comparison object.  For example:



.. code-block:: json



    { "X": { "$gt": 0, "$lt": 42 } }


    """

    vars = dict()
    vars['type'] = 'filters.mongo'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def mortonorder(inputs=None, tag=None, **kwargs):
    """.. _filters.mortonorder:



filters.mortonorder

================================================================================



Sorts the XY data using `Morton ordering`_.



It's also possible to compute a reverse Morton code by reading the binary

representation from the end to the beginning. This way, points are sorted

with a good dispersement. For example, by successively selecting N

representative points within tiles:



.. figure:: filters.mortonorder.img1.png

    :scale: 100 %

    :alt: Reverse Morton indexing



.. _`Morton ordering`: http://en.wikipedia.org/wiki/Z-order_curve



.. seealso::



    See `LOPoCS`_ and `pgmorton`_ for some use case examples of the

    Reverse Morton algorithm.



.. _`pgmorton`: https://github.com/Oslandia/pgmorton

.. _`LOPoCS`: https://github.com/Oslandia/lopocs



.. embed::



Example

-------



.. code-block:: json



  [

      "uncompressed.las",

      {

          "type":"filters.mortonorder",

          "reverse":"false"

      },

      {

          "type":"writers.las",

          "filename":"compressed.laz",

          "compression":"true"

      }

  ]





Options

--------



.. include:: filter_opts.rst


    """

    vars = dict()
    vars['type'] = 'filters.mortonorder'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def neighborclassifier(processed=None, inputs=None, tag=None, **kwargs):
    """.. _filters.neighborclassifier:



filters.neighborclassifier

==========================



The **neighborclassifier filter** allows you update the value of

the classification

for specific points to a value determined by a K-nearest neighbors vote.

For each point, the k_ nearest neighbors are queried and if more than half of

them have the same value, the filter updates the selected point accordingly



For example, if an automated classification procedure put/left erroneous

vegetation points near the edges of buildings which were largely classified

correctly, you could try using this filter to fix that problem.



Similiarly, some automated classification processes result in prediction for

only a subset of the original point cloud.  This filter could be used to

extrapolate those predictions to the original.



.. embed::



Example 1

---------



This pipeline updates the Classification of all points with classification

1 (unclassified) based on the consensus (majority) of its nearest 10 neighbors.



.. code-block:: json



  [

      "autzen_class.las",

      {

          "type" : "filters.neighborclassifier",

          "domain" : "Classification[1:1]",

          "k" : 10

      },

      "autzen_class_refined.las"

  ]



Example 2

---------



This pipeline moves all the classifications from "pred.txt"

to src.las.  Any points in src.las that are not in pred.txt will be

assigned based on the closest point in pred.txt.



.. code-block:: json



  [

      "src.las",

      {

          "type" : "filters.neighborclassifier",

          "k" : 1,

          "candidate" : "pred.txt"

      },

      "dest.las"

  ]



Options

-------



_`candidate`

  A filename which points to the point cloud containing the points which

  will do the voting.  If not specified, defaults to the input of the filter.



_`domain`

  A :ref:`range <ranges>` which selects points to be processed by the filter.

  Can be specified multiple times.  Points satisfying any range will be

  processed



_`k`

  An integer which specifies the number of neighbors which vote on each

  selected point.



.. include:: filter_opts.rst


    """

    vars = dict()
    vars['type'] = 'filters.neighborclassifier'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def nndistance(inputs=None, tag=None, **kwargs):
    """.. _filters.nndistance:



===============================================================================

filters.nndistance

===============================================================================



The NNDistance filter runs a 3-D nearest neighbor algorithm on the input

cloud and creates a new dimension, ``NNDistance``, that contains a distance

metric described by the mode_ of the filter.



.. embed::



Example

-------------------------------------------------------------------------------



.. code-block:: json



  [

      "input.las",

      {

          "type":"filters.nndistance",

          "k":8

      },

      {

          "type":"writers.bpf",

          "filename":"output.las",

          "output_dims":"X,Y,Z,NNDistance"

      }

  ]





Options

-------------------------------------------------------------------------------



_`mode`

  The mode of operation.  Either "kth", in which the distance is the euclidian

  distance of the subject point from the kth remote point or "avg" in which

  the distance is the average euclidian distance from the k_ nearest points.

  [Default: 'kth']



_`k`

  The number of k nearest neighbors to consider. [Default: **10**]



.. include:: filter_opts.rst


    """

    vars = dict()
    vars['type'] = 'filters.nndistance'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def normal(inputs=None, tag=None, **kwargs):
    """.. _filters.normal:



filters.normal

==============



The **normal filter** returns the estimated normal and curvature for

a collection

of points. The algorithm first computes the eigenvalues and eigenvectors of the

collection of points, which is comprised of the k-nearest neighbors. The normal

is taken as the eigenvector corresponding to the smallest eigenvalue. The

curvature is computed as



.. math::



  curvature = \frac{\lambda_0}{\lambda_0 + \lambda_1 + \lambda_2}



where :math:`\lambda_i` are the eigenvalues sorted in ascending order.



The filter produces four new dimensions (``NormalX``, ``NormalY``, ``NormalZ``,

and ``Curvature``), which can be analyzed directly, or consumed by downstream

stages for more advanced filtering.



The eigenvalue decomposition is performed using Eigen's

`SelfAdjointEigenSolver <https://eigen.tuxfamily.org/dox/classEigen_1_1SelfAdjointEigenSolver.html>`_.



Normals will be automatically flipped towards positive Z, unless the always_up_

flag is set to `false`. Users can optionally set any of the XYZ coordinates to

specify a custom viewpoint_ or set them all to zero to effectively disable the

normal flipping.



.. note::



  By default, the Normal filter will invert normals such that they are always

  pointed "up" (positive Z). If the user provides a viewpoint_, normals will

  instead be inverted such that they are oriented towards the viewpoint,

  regardless of the always_up_ flag. To disable all normal flipping, do not

  provide a viewpoint_ and set `always_up`_ to false.



In addition to always_up_ and viewpoint_, users can run a refinement step (off

by default) that propagates normals using a minimum spanning tree. The

propagated normals can lead to much more consistent results across the dataset.



.. note::



  To enable normal propagation, users can set refine_ to `true`.



.. embed::



Example

-------



This pipeline demonstrates the calculation of the normal values (along with

curvature). The newly created dimensions are written out to BPF for further

inspection.



.. code-block:: json



  [

      "input.las",

      {

          "type":"filters.normal",

          "knn":8

      },

      {

          "type":"writers.bpf",

          "filename":"output.bpf",

          "output_dims":"X,Y,Z,NormalX,NormalY,NormalZ,Curvature"

      }

  ]



Options

-------------------------------------------------------------------------------



_`knn`

  The number of k-nearest neighbors. [Default: 8]



_`viewpoint`

  A single WKT or GeoJSON 3D point. Normals will be inverted such that they are

  all oriented towards the viewpoint.



_`always_up`

  A flag indicating whether or not normals should be inverted only when the Z

  component is negative. [Default: true]



_`refine`

  A flag indicating whether or not to reorient normals using minimum spanning

  tree propagation. [Default: false]



.. include:: filter_opts.rst


    """

    vars = dict()
    vars['type'] = 'filters.normal'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def optimalneighborhood(min_k=None, max_k=None, inputs=None, tag=None, **kwargs):
    """.. _filters.optimalneighborhood:



===============================================================================

filters.optimalneighborhood

===============================================================================



The **Optimal Neighborhood filter** computes the eigenentropy (defined as the

Shannon entropy of the normalized eigenvalues) for a neighborhood of points in

the range ``min_k`` to ``max_k``. The neighborhood size that minimizes the

eigenentropy is saved to a new dimension ``OptimalKNN``. The corresponding

radius of the neighborhood is saved to ``OptimalRadius``. These dimensions can

be written to an output file or utilized directly by

:ref:`filters.covariancefeatures`.



.. embed::



Example

-------------------------------------------------------------------------------



.. code-block:: json



  [

      "input.las",

      {

          "type":"filters.optimalneighborhood",

          "min_k":8,

          "max_k": 50

      },

      {

          "type":"writers.las",

          "minor_version":4,

          "extra_dims":"all",

          "forward":"all",

          "filename":"output.las"

      }

  ]



Options

-------------------------------------------------------------------------------



min_k

  The minimum number of k nearest neighbors to consider for optimal

  neighborhood selection. [Default: 10]



max_k

  The maximum number of k nearest neighbors to consider for optimal

  neighborhood selection. [Default: 14]
    """

    vars = dict()
    vars['type'] = 'filters.optimalneighborhood'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def outlier(method=None, inputs=None, tag=None, **kwargs):
    """.. _filters.outlier:



===============================================================================

filters.outlier

===============================================================================



The **outlier filter** provides two outlier filtering methods: radius and

statistical. These two approaches are discussed in further detail below.



It is worth noting that both filtering methods simply apply a classification

value of 7 to the noise points (per the `LAS specification`_).

To remove the noise

points altogether, users can add a :ref:`range filter<filters.range>` to their

pipeline, downstream from the outlier filter.



.. _LAS specification: http://www.asprs.org/a/society/committees/standards/LAS_1_4_r13.pdf



.. embed::



.. code-block:: json



    {

      "type":"filters.range",

      "limits":"Classification![7:7]"

    }



Statistical Method

-------------------------------------------------------------------------------



The default method for identifying outlier points is the statistical outlier method. This method requires two passes through the input ``PointView``, first to compute a threshold value based on global statistics, and second to identify outliers using the computed threshold.



In the first pass, for each point :math:`p_i` in the input ``PointView``, compute the mean distance :math:`\mu_i` to each of the :math:`k` nearest neighbors (where :math:`k` is configurable and specified by mean_k_). Then,



.. math::



  \overline{\mu} = \frac{1}{N} \sum_{i=1}^N \mu_i



.. math::



  \sigma = \sqrt{\frac{1}{N-1} \sum_{i=1}^N (\mu_i - \overline{\mu})^2}



A global mean :math:`\overline{\mu}` of these mean distances is then computed along with the standard deviation :math:`\sigma`. From this, the threshold is computed as



.. math::



  t = \mu + m\sigma



where :math:`m` is a user-defined multiplier specified by multiplier_.



We now iterate over the pre-computed mean distances :math:`\mu_i` and compare to computed threshold value. If :math:`\mu_i` is greater than the threshold, it is marked as an outlier.



.. math::



  outlier_i = \begin{cases}

      \text{true,} \phantom{false,} \text{if } \mu_i >= t \\

      \text{false,} \phantom{true,} \text{otherwise} \\

  \end{cases}



.. figure:: filters.statisticaloutlier.img1.png

    :scale: 70 %

    :alt: Points before outlier removal



Before outlier removal, noise points can be found both above and below the

scene.





.. figure:: filters.statisticaloutlier.img2.png

    :scale: 60 %

    :alt: Points after outlier removal



After outlier removal, the noise points are removed.



See [Rusu2008]_ for more information.





Example

................................................................................



In this example, points are marked as outliers if the average distance to each

of the 12 nearest neighbors is below the computed threshold.



.. code-block:: json



  [

      "input.las",

      {

          "type":"filters.outlier",

          "method":"statistical",

          "mean_k":12,

          "multiplier":2.2

      },

      "output.las"

  ]



Radius Method

-------------------------------------------------------------------------------



For each point :math:`p_i` in the input ``PointView``, this method counts the

number of neighboring points :math:`k_i` within radius :math:`r` (specified by

radius_). If :math:`k_i<k_{min}`, where :math:`k_{min}` is the minimum number

of neighbors specified by min_k_, it is marked as an outlier.



.. math::



  outlier_i = \begin{cases}

      \text{true,} \phantom{false,} \text{if } k_i < k_{min} \\

      \text{false,} \phantom{true,} \text{otherwise} \\

  \end{cases}



Example

...............................................................................



The following example will mark points as outliers when there are fewer than

four neighbors within a radius of 1.0.



.. code-block:: json



  [

      "input.las",

      {

          "type":"filters.outlier",

          "method":"radius",

          "radius":1.0,

          "min_k":4

      },

      "output.las"

  ]



Options

-------------------------------------------------------------------------------



class

  The classification value to apply to outliers. [Default: 7]



method

  The outlier removal method (either "statistical" or "radius").

  [Default: "statistical"]



_`min_k`

  Minimum number of neighbors in radius (radius method only). [Default: 2]



_`radius`

  Radius (radius method only). [Default: 1.0]



_`mean_k`

  Mean number of neighbors (statistical method only). [Default: 8]



_`multiplier`

  Standard deviation threshold (statistical method only). [Default: 2.0]



.. include:: filter_opts.rst


    """

    vars = dict()
    vars['type'] = 'filters.outlier'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def overlay(dimension=None, column=None, layer=None, inputs=None, tag=None, **kwargs):
    """.. _filters.overlay:



filters.overlay

===================



The **overlay filter** allows you to set the values of a selected dimension

based on an OGR-readable polygon or multi-polygon.



.. embed::



OGR SQL support

----------------



You can limit your queries based on OGR's SQL support. If the

filter has both a datasource_ and a query_ option, those will

be used instead of the entire OGR data source. At this time it is

not possible to further filter the OGR query based on a geometry

but that may be added in the future.



.. note::



    The OGR SQL support follows the rules specified in `ExecuteSQL`_

    documentation, and it will pass SQL down to the underlying

    datasource if it can do so.



.. _`ExecuteSQL`: http://www.gdal.org/ogr__api_8h.html#a9892ecb0bf61add295bd9decdb13797a



Example 1

---------



In this scenario, we are altering the attributes of the dimension

``Classification``.  Points from autzen-dd.las that lie within a feature will

have their classification to match the ``CLS`` field associated with that

feature.



.. code-block:: json



  [

      "autzen-dd.las",

      {

          "type":"filters.overlay",

          "dimension":"Classification",

          "datasource":"attributes.shp",

          "layer":"attributes",

          "column":"CLS"

      },

      {

          "filename":"attributed.las",

          "scale_x":0.0000001,

          "scale_y":0.0000001

      }

  ]





Example 2

--------------------------------------------------------------------------------



This example sets the Intensity attribute to ``CLS`` values read from the

`OGR SQL`_ query.



.. _`OGR SQL`: http://www.gdal.org/ogr_sql_sqlite.html



.. code-block:: json



  [

      "autzen-dd.las",

      {

          "type":"filters.overlay",

          "dimension":"Intensity",

          "datasource":"attributes.shp",

          "query":"SELECT CLS FROM attributes where cls!=6",

          "column":"CLS"

      },

      "attributed.las"

  ]



Options

-------



dimension

  Name of the dimension whose value should be altered.  [Required]



_`datasource`

  OGR-readable datasource for Polygon or MultiPolygon data.  [Required]



column

  The OGR datasource column from which to read the attribute.

  [Default: first column]



_`query`

  OGR SQL query to execute on the datasource to fetch geometry and attributes.

  The entire layer is fetched if no query is provided.  [Default: none]



layer

  The data source's layer to use. [Default: first layer]



.. include:: filter_opts.rst


    """

    vars = dict()
    vars['type'] = 'filters.overlay'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def planefit(knn=None, threads=None, inputs=None, tag=None, **kwargs):
    """.. _filters.planefit:



filters.planefit

===============================================================================



The **Plane Fit Criterion** was introduced in [Weyrich2004]_ and computes the

deviation of a point from a manifold approximating its neighbors.  First, a

plane is fit to each point's k-neighborhood by performing an eigenvalue

decomposition. Next, the mean point to plane distance is computed by

considering all points within the neighborhood. This is compared to the point

to plane distance of the current point giving rise to the k-neighborhood. As

the mean distance of the k-neighborhood approaches 0, the Plane Fit criterion

will tend toward 1. As point to plane distance of the current point approaches

0, the Plane Fit criterion will tend toward 0.



The author suggests that the Plane Fit Criterion is well suited to outlier

detection when considering noisy reconstructions of smooth surfaces, but

produces poor results around small features and creases.



The filter creates a single new dimension, ``PlaneFit``, that records the

Plane Fit criterion for the current point.



.. note::



  To inspect the newly created, non-standard dimensions, be sure to write to an

  output format that can support arbitrary dimensions, such as BPF.



.. embed::



Example

-------



The sample pipeline below computes the Plane Fit criterion with a neighborhood

of 8 neighbors. We do not apply a fixed threshold to single out outliers based

on the Plane Fit criterion as the range of values can vary from one dataset to

another. In general, higher values indicate the likelihood of a point being an

outlier.



.. code-block:: json



  [

      "input.las",

      {

          "type":"filters.planefit",

          "knn":8

      },

      "output.laz"

  ]



Options

-------------------------------------------------------------------------------



knn

  The number of k nearest neighbors. [Default: 8]



threads

  The number of threads used for computing the plane fit criterion. [Default: 1]



.. include:: filter_opts.rst


    """

    vars = dict()
    vars['type'] = 'filters.planefit'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def pmf(**kwargs):
    """    """

    vars = dict()
    vars['type'] = 'filters.pmf'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def poisson(density=None, depth=None, inputs=None, tag=None, **kwargs):
    """.. _filters.poisson:



===============================================================================

filters.poisson

===============================================================================



The **Poisson Filter** passes data Mischa Kazhdan's poisson surface

reconstruction

algorithm. [Kazhdan2006]_  It creates a watertight surface from the original

point set by creating an entirely new point set representing the imputed

isosurface.  The algorithm requires normal vectors to each point in order

to run.  If the x, y and z normal dimensions are present in the input point

set, they will be used by the algorithm.  If they don't exist, the poisson

filter will invoke the PDAL normal filter to create them before running.



The poisson algorithm will usually create a larger output point set

than the input point set.  Because the algorithm constructs new points, data

associated with the original points set will be lost, as the algorithm has

limited ability to impute associated data.  However, if color dimensions

(red, green and blue) are present in the input, colors will be reconstructed

in the output point set. This filter will also run the

:ref:`normal filter <filters.normal>` on the output point set.



This integration of the algorithm with PDAL only supports a limited set of

the options available to the implementation.  If you need support for further

options, please let us know.



.. embed::



Example

-------------------------------------------------------------------------------



.. code-block:: json



  [

      "dense.las",

      {

          "type":"filters.poisson"

      },

      {

          "type":"writers.ply",

          "filename":"isosurface.ply"

      }

  ]



.. note::

    The algorithm is slow.  On a reasonable desktop machine, the surface

    reconstruction shown below took about 15 minutes.



.. figure:: ../images/poisson_points.png



  Point cloud (800,000 points)



.. figure:: ../images/poisson_edges.png



  Reconstruction (1.8 million vertices, 3.7 million faces)





Options

-------------------------------------------------------------------------------



density

  Write an estimate of neighborhood density for each point in the output

  set.



depth

  Maximum depth of the tree used for reconstruction. The output is sensitive

  to this parameter.  Increase if the results appear unsatisfactory.

  [Default: 8]



.. include:: filter_opts.rst


    """

    vars = dict()
    vars['type'] = 'filters.poisson'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def projpipeline(**kwargs):
    """    """

    vars = dict()
    vars['type'] = 'filters.projpipeline'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def python(script=None, source=None, module=None, function=None, inputs=None, tag=None, **kwargs):
    """.. _filters.python:



filters.python

==============



The **Python Filter** allows `Python`_ software to be embedded in a

:ref:`pipeline` that allows modification of PDAL points through a `NumPy`_

array.  Additionally, some global :ref:`metadata` is also

available that Python functions can interact with.



The function must have two `NumPy`_ arrays as arguments, ``ins`` and ``outs``.

The ``ins`` array represents the points before the ``filters.python``

filter and the ``outs`` array represents the points after filtering.



.. warning::



    Make sure `NumPy`_ is installed in your `Python`_ environment.



    .. code-block:: shell



        $ python3 -c "import numpy; print(numpy.__version__)"

        1.18.1



.. warning::



    Each array contains all the :ref:`dimensions` of the incoming ``ins``

    point schema.  Each array in the ``outs`` list matches the `NumPy`_

    array of the same type as provided as ``ins`` for shape and type.



.. plugin::



.. code-block:: python



  import numpy as np



  def multiply_z(ins,outs):

      Z = ins['Z']

      Z = Z * 10.0

      outs['Z'] = Z

      return True





1) The function must always return `True` upon success. If the function

   returned `False`, an error would be thrown and the :ref:`pipeline` exited.







2) If you want write a dimension that might not be available, you can specify

   it with the add_dimension_ option:



   ::



       "add_dimension": "NewDimensionOne"



   To create more than one dimension, this option also accepts an array:



   ::



       "add_dimension": [ "NewDimensionOne", "NewDimensionTwo", "NewDimensionThree" ]





   You can also specify the :ref:`type <types>` of the dimension using an ``=``.

   ::



       "add_dimension": "NewDimensionOne=uint8"





Modification Example

--------------------------------------------------------------------------------



.. code-block:: json



  [

      "file-input.las",

      {

          "type":"filters.smrf"

      },

      {

          "type":"filters.python",

          "script":"multiply_z.py",

          "function":"multiply_z",

          "module":"anything"

      },

      {

          "type":"writers.las",

          "filename":"file-filtered.las"

      }

  ]



The JSON pipeline file referenced the external `multiply_z.py` `Python`_ script,

which scales the ``Z`` coordinate by a factor of 10.



.. code-block:: python



  import numpy as np



  def multiply_z(ins,outs):

      Z = ins['Z']

      Z = Z * 10.0

      outs['Z'] = Z

      return True



Predicates

--------------------------------------------------------------------------------



Points can be retained/removed from the stream by setting true/false values

into a special "Mask" dimension in the output point array.



The example above sets the "mask" to true for points that are in

classifications 1 or 2 and to false otherwise, causing points that are not

classified 1 or 2 to be dropped from the point stream.



.. code-block:: python



  import numpy as np



  def filter(ins,outs):

     cls = ins['Classification']



     keep_classes = [1, 2]



     # Use the first test for our base array.

     keep = np.equal(cls, keep_classes[0])



     # For 1:n, test each predicate and join back

     # to our existing predicate array

     for k in range(1, len(keep_classes)):

         t = np.equal(cls, keep_classes[k])

         keep = keep + t



     outs['Mask'] = keep

     return True



.. note::



    :ref:`filters.range` is a specialized filter that implements the exact

    functionality described in this Python operation. It is likely to be much

    faster than Python, but not as flexible. :ref:`filters.python` is the tool

    you can use for prototyping point stream processing operations.



.. seealso::



    If you want to read a :ref:`pipeline` of operations into a numpy

    array, the `PDAL Python extension <https://pypi.python.org/pypi/PDAL>`_

    is available.



Example pipeline

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. code-block:: json



  [

      "file-input.las",

      {

          "type":"filters.smrf"

      },

      {

          "type":"filters.python",

          "script":"filter_pdal.py",

          "function":"filter",

          "module":"anything"

      },

      {

          "type":"writers.las",

          "filename":"file-filtered.las"

      }

  ]



Module Globals

--------------------------------------------------------------------------------



Three global variables are added to the Python module as it is run to allow

you to get :ref:`dimensions`, :ref:`metadata`, and coordinate system

information.

Additionally, the ``metadata`` object can be set by the function

to modify metadata

for the in-scope :ref:`filters.python` :cpp:class:`pdal::Stage`.



.. code-block:: python



   def myfunc(ins,outs):

       print('schema: ', schema)

       print('srs: ', spatialreference)

       print('metadata: ', metadata)

       outs = ins

       return True



Setting stage metadata

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. note::

    The name of the output metadata variable has changed from ``metadata`` to ``out_metadata``.



Stage metadata can be created by using the ``out_metadata`` dictionary **global** variable.

The ``name`` key must be set. The type of the ``value`` can usually be inferred, but

can be set to one of ``integer``, ``nonNegativeInteger``, ``double``, ``bounds``,

``boolean``, ``spatialreference``, ``uuid`` or ``string``.



Children may be set using the ``children`` key whose value is a list of dictionaries.



.. code-block:: python



   def myfunc(ins,outs):

     global out_metadata

     out_metadata = {'name': 'root', 'value': 'a string', 'type': 'string', 'description': 'a description', 'children': [{'name': 'somekey', 'value': 52, 'type': 'integer', 'description': 'a filter description', 'children': []}, {'name': 'readers.faux', 'value': 'another string', 'type': 'string', 'description': 'a reader description', 'children': []}]}

     return True



Passing Python objects

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



An JSON-formatted option can be passed to the filter representing a

Python dictionary containing objects you want to use in your function.

This feature is useful in situations where you

wish to call :ref:`pipeline_command` with substitutions.



If we needed to be able to provide the Z scaling factor of `Example Pipeline`_

with a

Python argument, we can place that in a dictionary and pass that to the filter

as a separate argument. This feature allows us to be able easily reuse the same

basic Python function while substituting values as necessary.



.. code-block:: json



  [

      "input.las",

      {

          "type":"filters.python",

          "module":"anything",

          "function":"filter",

          "script":"arguments.py",

          "pdalargs":"{\"factor\":0.3048,\"an_argument\":42, \"another\": \"a string\"}"

      },

      "output.las"

  ]



With that option set, you can now fetch the pdalargs_ dictionary in your

Python script and use it:



.. code-block:: python



  import numpy as np



  def multiply_z(ins,outs):

      Z = ins['Z']

      Z = Z * float(pdalargs['factor'])

      outs['Z'] = Z

      return True





Standard output and error

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



A ``redirector`` module is available for scripts to output to PDAL's log stream

explicitly. The module handles redirecting ``sys.stderr`` and

``sys.stdout`` for you

transparently, but it can be used directly by scripts. See the PDAL source

code for more details.





Options

--------------------------------------------------------------------------------



script

  When reading a function from a separate `Python`_ file, the file name to read

  from.



source

  The literal `Python`_ code to execute, when the script option is

  not being used.



module

  The Python module that is holding the function to run. [Required]



function

  The function to call. [Required]





_`add_dimension`

  A dimension name or an array of dimension names to add to the pipeline that do not already exist.



_`pdalargs`

  A JSON dictionary of items you wish to pass into the modules globals as the

  ``pdalargs`` object.



.. include:: filter_opts.rst



.. _Python: http://python.org/

.. _NumPy: http://www.numpy.org/
    """

    vars = dict()
    vars['type'] = 'filters.python'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def radialdensity(inputs=None, tag=None, **kwargs):
    """.. _filters.radialdensity:



===============================================================================

filters.radialdensity

===============================================================================



The **Radial Density filter** creates a new attribute ``RadialDensity`` that

contains the density of points in a sphere of given radius.



The density at each point is computed by counting the number of points falling

within a sphere of given radius_ (default is 1.0) and centered at the current

point. The number of neighbors (including the query point) is then normalized

by the volume of the sphere, defined as



.. math::



  V = \frac{4}{3} \pi r^3



The radius :math:`r` can be adjusted by changing the radius_ option.



.. embed::



Example

-------------------------------------------------------------------------------



.. code-block:: json



  [

      "input.las",

      {

          "type":"filters.radialdensity",

          "radius":2.0

      },

      {

          "type":"writers.bpf",

          "filename":"output.bpf",

          "output_dims":"X,Y,Z,RadialDensity"

      }

  ]





Options

-------------------------------------------------------------------------------



_`radius`

  Radius. [Default: 1.0]



.. include:: filter_opts.rst


    """

    vars = dict()
    vars['type'] = 'filters.radialdensity'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def randomize(inputs=None, tag=None, **kwargs):
    """.. _filters.randomize:



filters.randomize

=================



The randomize filter reorders the points in a point view randomly.



.. embed::



Example

-------



.. code-block:: json



  [

      "input.las",

      {

          "type":"filters.randomize"

      },

      {

          "type":"writers.las",

          "filename":"output.las"

      }

  ]



Options

-------



.. include:: filter_opts.rst


    """

    vars = dict()
    vars['type'] = 'filters.randomize'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def range(limits=None, Ranges=None, inputs=None, tag=None, **kwargs):
    """.. _filters.range:



filters.range

======================



The **Range Filter** applies rudimentary filtering to the input point cloud

based on a set of criteria on the given dimensions.



.. embed::



.. streamable::



Example

-------



This example passes through all points whose ``Z`` value is in the

range [0,100]

and whose ``Classification`` equals 2 (corresponding to ground in LAS).





.. code-block:: json



  [

      "input.las",

      {

          "type":"filters.range",

          "limits":"Z[0:100],Classification[2:2]"

      },

      {

          "type":"writers.las",

          "filename":"filtered.las"

      }

  ]





The equivalent pipeline invoked via the PDAL ``translate`` command would be



.. code-block:: bash



  $ pdal translate -i input.las -o filtered.las -f range --filters.range.limits="Z[0:100],Classification[2:2]"



Options

-------



limits

  A comma-separated list of :ref:`ranges`.  If more than one range is

  specified for a dimension, the criteria are treated as being logically

  ORed together.  Ranges for different dimensions are treated as being

  logically ANDed.



  Example:



  ::



    Classification[1:2], Red[1:50], Blue[25:75], Red[75:255], Classification[6:7]



  This specification will select points that have the classification of

  1, 2, 6 or 7 and have a blue value or 25-75 and have a red value of

  1-50 or 75-255.  In this case, all values are inclusive.



.. include:: filter_opts.rst



.. _ranges:



Ranges

--------------------------------------------------------------------------------



A range specification is a dimension name, followed by an optional negation

character ('!'), and a starting and ending value separated by a colon,

surrounded by parentheses or square brackets.  Either the starting or ending

values can be omitted.  Parentheses indicate an open endpoint that doesn't

include the adjacent value.  Square brackets indicate a closed endpoint

that includes the adjacent value.



Example 1:

................................................................................



::



  Z[10:]



Selects all points with a Z value greater than or equal to 10.



Example 2:

................................................................................



::



  Classification[2:2]



Selects all points with a classification of 2.



Example 3:

................................................................................



::



  Red!(20:40]



Selects all points with red values less than or equal to 20 and those with

values greater than 40



Example 4:

................................................................................



::



  Blue[:255)



Selects all points with a blue value less than 255.



Example 5:

................................................................................



::



  Intensity![25:25]



Selects all points with an intensity not equal to 25.
    """

    vars = dict()
    vars['type'] = 'filters.range'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def reciprocity(knn=None, inputs=None, tag=None, **kwargs):
    """.. _filters.reciprocity:



filters.reciprocity

===============================================================================



The **Nearest-Neighbor Reciprocity Criterion** was introduced in [Weyrich2004]_

and is based on a simple assumption, that valid points may be in the

k-neighborhood of an outlier, but the outlier will most likely not be part of

the valid point's k-neighborhood.



The author suggests that the Nearest-Neighbor Reciprocity Criterion is more

robust than both the :ref:`Plane Fit <filters.planefit>` and :ref:`Miniball

<filters.miniball>` Criterion, being equally sensitive around smooth and

detailed regions. The criterion does however produce invalid results near

manifold borders.



The filter creates a single new dimension, ``Reciprocity``, that records the

percentage of points(in the range 0 to 100) that are considered uni-directional

neighbors of the current point.



.. note::



  To inspect the newly created, non-standard dimensions, be sure to write to an

  output format that can support arbitrary dimensions, such as BPF.



.. embed::



Example

-------



The sample pipeline below computes reciprocity with a neighborhood of 8

neighbors, followed by a range filter to crop out points whose ``Reciprocity``

percentage is less than 98% before writing the output.



.. code-block:: json



  [

      "input.las",

      {

          "type":"filters.reciprocity",

          "knn":8

      },

      {

          "type":"filters.range",

          "limits":"Reciprocity[:98.0]"

      },

      "output.laz"

  ]



Options

-------------------------------------------------------------------------------



knn

  The number of k nearest neighbors. [Default: 8]



.. include:: filter_opts.rst


    """

    vars = dict()
    vars['type'] = 'filters.reciprocity'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def relaxationdartthrowing(decay=None, radius=None, count=None, shuffle=None, seed=None, inputs=None, tag=None, **kwargs):
    """.. _filters.relaxationdartthrowing:



filters.relaxationdartthrowing

===============================================================================



The **Relaxation Dart Throwing Filter** is a variation on Poisson sampling. The

approach was first introduced by [McCool1992]_. The filter operates nearly

identically to :ref:`filters.sample`, except it will continue to shrink the

radius with each pass through the point cloud until the desired number of

output points is reached.



.. seealso::



    :ref:`filters.decimation`, :ref:`filters.fps` and :ref:`filters.sample` all

    perform some form of thinning or resampling.



.. note::



    The ``shuffle`` option does not reorder points in the PointView, but

    shuffles the order in which the points are visited while processing, which

    can improve the quality of the result.



.. embed::



Options

-------------------------------------------------------------------------------



decay

  Decay rate for the radius shrinkage. [Default: 0.9]



radius

  Starting minimum distance between samples. [Default: 1.0]



count

  Desired number of points in the output. [Default: 1000]



shuffle

  Choose whether or not to shuffle order in which points are visited. [Default:

  true]



seed

  Seed for random number generator, used only with shuffle.



.. include:: filter_opts.rst


    """

    vars = dict()
    vars['type'] = 'filters.relaxationdartthrowing'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def reprojection(in_srs=None, out_srs=None, in_axis_ordering=None, out_axis_ordering=None, error_on_failure=None, inputs=None, tag=None, **kwargs):
    """.. _filters.reprojection:



filters.reprojection

===========================



The **reprojection filter** converts the X, Y and/or Z dimensions to a

new spatial

reference system. The old coordinates are replaced by the new ones.

If you want to preserve the old coordinates for future processing, use a

:ref:`filters.ferry` to create copies of the original dimensions before

reprojecting.



.. note::



    When coordinates are reprojected, it may significantly change the precision

    necessary to represent the values in some output formats.  Make sure

    that you're familiar with any scaling necessary for your output format

    based on the projection you've used.



.. embed::



.. streamable::



Example 1

--------------------------------------------------------------------------------



This pipeline reprojects terrain points with Z-values between 0 and 100 by first

applying a range filter and then specifying both the input and output spatial

reference as EPSG-codes. The X and Y dimensions are scaled to allow enough

precision in the output coordinates.



.. code-block:: json



  [

      {

          "filename":"input.las",

          "type":"readers.las",

          "spatialreference":"EPSG:26916"

      },

      {

          "type":"filters.range",

          "limits":"Z[0:100],Classification[2:2]"

      },

      {

          "type":"filters.reprojection",

          "in_srs":"EPSG:26916",

          "out_srs":"EPSG:4326"

      },

      {

          "type":"writers.las",

          "scale_x":"0.0000001",

          "scale_y":"0.0000001",

          "scale_z":"0.01",

          "offset_x":"auto",

          "offset_y":"auto",

          "offset_z":"auto",

          "filename":"example-geog.las"

      }

  ]



Example 2

--------------------------------------------------------------------------------



In some cases it is not possible to use a EPSG-code as a spatial reference.

Instead `Proj.4 <http:/proj4.org>`_ parameters can be used to define a spatial

reference.  In this example the vertical component of points in a laz file is

converted from geometric (ellipsoidal) heights to orthometric heights by using

the ``geoidgrids`` parameter from Proj.4.  Here we change the vertical datum

from the GRS80 ellipsoid to DVR90, the vertical datum in Denmark. In the

writing stage of the pipeline the spatial reference of the file is set to

EPSG:7416. The last step is needed since PDAL will otherwise reference the

vertical datum as "Unnamed Vertical Datum" in the spatial reference VLR.





.. code-block:: json



  [

      "./1km_6135_632.laz",

      {

          "type":"filters.reprojection",

          "in_srs":"EPSG:25832",

          "out_srs":"+init=epsg:25832 +geoidgrids=C:/data/geoids/dvr90.gtx"

      },

      {

          "type":"writers.las",

          "a_srs":"EPSG:7416",

          "filename":"1km_6135_632_DVR90.laz"

      }

  ]



Options

-------



in_srs

  Spatial reference system of the input data. Express as an EPSG string (eg

  "EPSG:4326" for WGS84 geographic), Proj.4 string or a well-known text

  string. [Required if not part of the input data set]



out_srs

  Spatial reference system of the output data. Express as an EPSG string (eg

  "EPSG:4326" for WGS84 geographic), Proj.4 string or a well-known text

  string. [Required]



in_axis_ordering

  An array of numbers that override the axis order for the in_srs (or if

  not specified, the inferred SRS from the previous Stage). "2, 1" for

  example would swap X and Y, which may be commonly needed for

  something like "EPSG:4326".



out_axis_ordering

  An array of numbers that override the axis order for the out_srs.

  "2, 1" for example would swap X and Y, which may be commonly needed for

  something like "EPSG:4326".



error_on_failure

  If true and reprojection of any point fails, throw an exception that terminates

  PDAL . [Default: false]
    """

    vars = dict()
    vars['type'] = 'filters.reprojection'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def returns(inputs=None, tag=None, **kwargs):
    """.. _filters.returns:



filters.returns

===============================================================================



The **Returns Filter** takes a single PointView as its input and creates a

``PointView`` for each of the user-specified groups_ defined below.



"first" is defined as those points whose ``ReturnNumber`` is 1 when the ``NumberOfReturns`` is greater than 1.



"intermediate" is defined as those points whose ``ReturnNumber`` is greater than 1 and less than ``NumberOfReturns`` when ``NumberOfReturns`` is greater than 2.



"last" is defined as those points whose ``ReturnNumber`` is equal to ``NumberOfReturns`` when ``NumberOfReturns`` is greater than 1.



"only" is defined as those points whose ``NumberOfReturns`` is 1.



.. embed::



Example

-------



This example creates two separate output files for the "last" and "only"

returns.



.. code-block:: json



  [

      "input.las",

      {

          "type":"filters.returns",

          "groups":"last,only"

      },

      "output_#.las"

  ]



Options

-------



_`groups`

  Comma-separated list of return number groupings. Valid options are "first",

  "last", "intermediate" or "only". [Default: "last"]



.. include:: filter_opts.rst


    """

    vars = dict()
    vars['type'] = 'filters.returns'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def sample(cell=None, radius=None, inputs=None, tag=None, **kwargs):
    """.. _filters.sample:



filters.sample

===============================================================================



The **Sample Filter** performs Poisson sampling of the input ``PointView``. The 

practice of performing Poisson sampling via "Dart Throwing" was introduced

in the mid-1980's by [Cook1986]_ and [Dippe1985]_, and has been applied to

point clouds in other software [Mesh2009]_.



Our implementation of Poisson sampling is made streamable by voxelizing the

space and only adding points to the output ``PointView`` if they do not violate

the minimum distance criterion (as specified by ``radius``). The voxelization

allows several optimizations, first by checking for existing points within the

same voxel as the point under consideration, which are mostly likely to

violate the minimum distance criterion. Furthermore, we can easily visit

neighboring voxels (limiting the search to those that are populated) without

the need to create a KD-tree from the entire input ``PointView`` first and

performing costly spatial searches.



.. seealso::



    :ref:`filters.decimation`, :ref:`filters.fps`,

    :ref:`filters.relaxationdartthrowing`,

    :ref:`filters.voxelcenternearestneighbor`,

    :ref:`filters.voxelcentroidnearestneighbor`, and :ref:`filters.voxeldownsize` also

    perform decimation.



.. note::



    Starting with PDAL v2.3, the ``filters.sample`` now supports streaming

    mode. As a result, there is no longer an option to ``shuffle`` points (or

    to provide a ``seed`` for the shuffle).



.. note::



    Starting with PDAL v2.3, a ``cell`` option has been added that works with

    the existing ``radius``. The user must provide one or the other, but not

    both. The provided option will be used to automatically compute the other.

    The relationship between ``cell`` and ``radius`` is such that the

    ``radius`` defines the radius of a sphere that circumscribes a voxel with

    edge length defined by ``cell``.



.. note::



    Care must be taken with selection of the ``cell``/``radius`` option.

    Although the filter can now operate in streaming mode, if the extents of

    the point cloud are large (or conversely, if the cell size is small) the

    voxel occupancy map which grows as a function of these variables can still

    require a large memory footprint.



.. note::



    To operate in streaming mode, the filter will typically retain the first

    point to occupy a voxel (subject to the minimum distance criterion set

    forth earlier). This means that point ordering matters, and in fact, it is

    quite possible that points in the incoming stream can be ordered in such a

    way as to introduce undesirable artifacts (e.g., related to previous tiling

    of the data). In our experience, processing data that is still in scan

    order (ordered by GpsTime, if available) does produce reliable results,

    although to require this sort either internally or by inserting

    :ref:`filters.sort` prior to sampling would break our ability to stream the

    data.



.. embed::



.. streamable::



Options

-------------------------------------------------------------------------------



cell

  Voxel cell size. If ``radius`` is set, ``cell`` is automatically computed

  such that the cell is circumscribed by the sphere defined by ``radius``.



radius

  Minimum distance between samples. If ``cell`` is set, ``radius`` is

  automatically computed to defined a sphere that circumscribes the voxel cell.

  Whether specified or derived, ``radius`` defines the minimum allowable

  distance between points.



.. include:: filter_opts.rst


    """

    vars = dict()
    vars['type'] = 'filters.sample'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def separatescanline(inputs=None, tag=None, **kwargs):
    """.. _filters.separatescanline:



filters.separatescanline

===============================================================================



The **Separate scan line Filter** takes a single ``PointView`` as its input and

creates a ``PointView`` for each scan line as its output. ``PointView`` must contain

the ``EdgeOfFlightLine`` dimension.



.. embed::



Example

-------



The following pipeline will create a set of text files, where each file contains

only 10 scan lines.



.. code-block:: json



  [

      "input.text",

      {

          "type":"filters.separatescanline",

          "groupby":10

      },

      "output_#.text"

  ]



Options

-------



_`groupby`

  The number of lines to be grouped by. [Default : 1]



.. include:: filter_opts.rst


    """

    vars = dict()
    vars['type'] = 'filters.separatescanline'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def shell(command=None, inputs=None, tag=None, **kwargs):
    """:orphan:



.. _filters.shell:



filters.shell

===================



The shell filter allows you to run shell operations in-line

with PDAL pipeline tasks. This can be especially useful for

follow-on items or orchestration of complex workflows.



.. embed::



.. warning::



    To use :ref:`filters.shell`, you must set ``PDAL_ALLOW_SHELL=1``

    PDAL's execution environment. Without the environment variable

    set, every attempt at execution will result in the following

    error:



        PDAL_ALLOW_SHELL environment variable not set, shell access is not allowed



Example

---------



GDAL processing operations applied to raster output from :ref:`writers.gdal`

are a common task. Applying these within the PDAL execution environment

can provide some convenience and allow downstream consumers to have deterministic

completion status of the task. The following task writes multiple elevation

models to disk and then uses the `gdaladdo <https://gdal.org/gdaladdo.html>`__

command to construct overview bands for the data using average interpolation.



.. code-block:: json



    {

      "pipeline":[

        "autzen.las",

        {

          "type":"writers.gdal",

          "filename" : "output-1m.tif",

          "resolution" : "1.0"

        },

        {

          "type":"writers.gdal",

          "filename" : "output-2m.tif",

          "resolution" : "2.0"

        },

        {

          "type":"writers.gdal",

          "filename" : "output-5m.tif",

          "resolution" : "5.0"

        },

        {

          "type":"filters.shell",

          "command" : "gdaladdo -r average output-1m.tif 2 4 8 16"

        },

        {

          "type":"filters.shell",

          "command" : "gdaladdo -r average output-2m.tif 2 4 8 16"

        },

        {

          "type":"filters.shell",

          "command" : "gdaladdo -r average output-5m.tif 2 4 8 16"

        }

        ]

    }





Options

-------



command

  The shell command to run. It is run in relation to the current

  working directory of the pipeline executing it.



.. include:: filter_opts.rst


    """

    vars = dict()
    vars['type'] = 'filters.shell'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def skewnessbalancing(inputs=None, tag=None, **kwargs):
    """.. _filters.skewnessbalancing:



filters.skewnessbalancing

===============================================================================



**Skewness Balancing** classifies ground points based on the approach outlined

in [Bartels2010]_.



.. embed::



.. note::



    For Skewness Balancing to work well, the scene being processed needs to be

    quite flat, otherwise many above ground features will begin to be included

    in the ground surface.



Example

-------



The sample pipeline below uses the Skewness Balancing filter to segment ground

and non-ground returns, using default options, and writing only the ground

returns to the output file.



.. code-block:: json



  [

      "input.las",

      {

          "type":"filters.skewnessbalancing"

      },

      {

          "type":"filters.range",

          "limits":"Classification[2:2]"

      },

      "output.laz"

  ]



Options

-------------------------------------------------------------------------------



.. include:: filter_opts.rst



.. note::



    The Skewness Balancing method is touted as being threshold-free. We may

    still in the future add convenience parameters that are common to other

    ground segmentation filters, such as ``returns`` or ``ignore`` to limit the

    points under consideration for filtering.
    """

    vars = dict()
    vars['type'] = 'filters.skewnessbalancing'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def smrf(cell=None, classbits=None, cut=None, dir=None, ignore=None, returns=None, scalar=None, slope=None, threshold=None, window=None, inputs=None, tag=None, **kwargs):
    """.. _filters.smrf:



filters.smrf

===============================================================================



The **Simple Morphological Filter (SMRF)** classifies ground points based

on the approach outlined in [Pingel2013]_.



.. embed::



Example #1

----------



The sample pipeline below uses the SMRF filter to segment ground and non-ground

returns, using default options, and writing only the ground returns to the

output file.



.. code-block:: json



  [

      "input.las",

      {

          "type":"filters.smrf"

      },

      {

          "type":"filters.range",

          "limits":"Classification[2:2]"

      },

      "output.laz"

  ]



Example #2

----------



A more complete example, specifying some options. These match the

optimized parameters for Sample 1 given in Table 3 of [Pingel2013]_.



.. code-block:: json



  [

      "input.las",

      {

          "type":"filters.smrf",

          "scalar":1.2,

          "slope":0.2,

          "threshold":0.45,

          "window":16.0

      },

      {

          "type":"filters.range",

          "limits":"Classification[2:2]"

      },

      "output.laz"

  ]



Options

-------------------------------------------------------------------------------



cell

  Cell size. [Default: 1.0]



classbits

  Selectively ignore points marked as "synthetic", "keypoint", or "withheld".

  [Default: empty string, use all points]



cut

  Cut net size (``cut=0`` skips the net cutting step). [Default: 0.0]



dir

  Optional output directory for debugging intermediate rasters.



ignore

  A :ref:`range <ranges>` of values of a dimension to ignore.



returns

  Return types to include in output.  Valid values are "first", "last",

  "intermediate" and "only". [Default: "last, only"]



scalar

  Elevation scalar. [Default: **1.25**]



slope

  Slope (rise over run). [Default: **0.15**]



threshold

  Elevation threshold. [Default: **0.5**]



window

  Max window size. [Default: **18.0**]



.. include:: filter_opts.rst


    """

    vars = dict()
    vars['type'] = 'filters.smrf'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def sort(inputs=None, tag=None, **kwargs):
    """.. _filters.sort:



filters.sort

============



The sort filter orders a point view based on the values of a dimension_. The

sorting can be done in increasing (ascending) or decreasing (descending) order_.



.. embed::



Example

-------





.. code-block:: json



  [

      "unsorted.las",

      {

          "type":"filters.sort",

          "dimension":"X",

          "order":"ASC"

      },

      "sorted.las"

  ]





Options

-------



_`dimension`

  The dimension on which to sort the points. [Required]



_`order`

  The order in which to sort, ASC or DESC [Default: "ASC"]



.. include:: filter_opts.rst


    """

    vars = dict()
    vars['type'] = 'filters.sort'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def splitter(length=None, buffer=None, inputs=None, tag=None, **kwargs):
    """.. _filters.splitter:



filters.splitter

===============================================================================



The **Splitter Filter** breaks a point cloud into square tiles of a

specified size.  The origin of the tiles is chosen arbitrarily unless specified

with the origin_x_ and origin_y_ option.



The splitter takes a single ``PointView`` as its input and creates a

``PointView`` for each tile as its output.



Splitting is usually applied to data read from files (which produce one large

stream of points) before the points are written to a database (which prefer

data segmented into smaller blocks).



.. embed::



Example

-------



.. code-block:: json



  [

      "input.las",

      {

          "type":"filters.splitter",

          "length":"100",

          "origin_x":"638900.0",

          "origin_y":"835500.0"

      },

      {

          "type":"writers.pgpointcloud",

          "connection":"dbname='lidar' user='user'"

      }

  ]



Options

-------



length

  Length of the sides of the tiles that are created to hold points.

  [Default: 1000]



_`origin_x`

  X Origin of the tiles.  [Default: none (chosen arbitrarily)]



_`origin_y`

  Y Origin of the tiles.  [Default: none (chosen arbitrarily)]



buffer

  Amount of overlap to include in each tile. This buffer is added onto

  length in both the x and the y direction.  [Default: 0]



.. include:: filter_opts.rst


    """

    vars = dict()
    vars['type'] = 'filters.splitter'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def stats(dimensions=None, count=None, advanced=None, inputs=None, tag=None, **kwargs):
    """.. _filters.stats:



filters.stats

===============================================================================



The **Stats Filter** calculates the minimum, maximum and average (mean) values

of dimensions.  On request it will also provide an enumeration of values of

a dimension and skewness and kurtosis.



The output of the stats filter is metadata that can be stored by writers or

used through the PDAL API.  Output from the stats filter can also be

quickly obtained in JSON format by using the command "pdal info --stats".



.. note::



    The filter can compute both sample and population statistics.  For kurtosis,

    the filter can also compute standard and excess kurtosis.  However, only

    a single value is reported for each statistic type in metadata, and that is

    the sample statistic, rather than the population statistic.  For kurtosis

    the sample excess kurtosis is reported.  This seems to match the behavior

    of many other software packages.



Example

................................................................................



.. code-block:: json



  [

      "input.las",

      {

          "type":"filters.stats",

          "dimensions":"X,Y,Z,Classification",

          "enumerate":"Classification"

      },

      {

          "type":"writers.las",

          "filename":"output.las"

      }

  ]



Options

-------



.. _stats-dimensions:



dimensions

  A comma-separated list of dimensions whose statistics should be

  processed.  If not provided, statistics for all dimensions are calculated.



_`enumerate`

  A comma-separated list of dimensions whose values should be enumerated.

  Note that this list does not add to the list of dimensions that may be

  provided in the :ref:`dimensions <stats-dimensions>` option.



count

  Identical to the enumerate_ option, but provides a count of the number

  of points in each enumerated category.



global

  A comma-separated list of dimensions for which global statistics (median,

  mad, mode) should be calculated.



advanced

  Calculate advanced statistics (skewness, kurtosis). [Default: false]



.. include:: filter_opts.rst


    """

    vars = dict()
    vars['type'] = 'filters.stats'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def streamcallback(inputs=None, tag=None, **kwargs):
    """.. _filters.streamcallback:



filters.streamcallback

======================



The **Stream Callback Filter** provides a simple hook for a

user-specified action

to occur for each point.  The stream callback filter is for use by C++

programmers extending PDAL functionality and isn't useful to end users.



.. embed::



.. streamable::



Options

-------



.. include:: filter_opts.rst


    """

    vars = dict()
    vars['type'] = 'filters.streamcallback'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def tail(count=None, inputs=None, tag=None, **kwargs):
    """.. _filters.tail:



filters.tail

===============================================================================



The **Tail Filter** returns a specified number of points from the end of the

``PointView``.



.. note::



    If the requested number of points exceeds the size of the point cloud, all

    points are passed with a warning.



.. embed::



Example

-------



Sort and extract the 100 lowest intensity points.





.. code-block:: json



  [

      {

          "type":"filters.sort",

          "dimension":"Intensity",

          "order":"DESC"

      },

      {

          "type":"filters.tail",

          "count":100

      }

  ]





.. seealso::



    :ref:`filters.head` is the dual to :ref:`filters.tail`.





Options

-------------------------------------------------------------------------------



count

  Number of points to return. [Default: 10]



.. include:: filter_opts.rst


    """

    vars = dict()
    vars['type'] = 'filters.tail'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def teaser(nr=None, fr=None, fpfh=None, inputs=None, tag=None, **kwargs):
    """.. _filters.teaser:



filters.teaser

==============



The **TEASER filter** uses the Truncated least squares Estimation And

SEmidefinite Relaxation (TEASER) algorithm [Yang2020]_ to calculate a **rigid**

transformation that best aligns two datasets. The first input to the ICP filter

is considered the "fixed" points, and all subsequent points are "moving"

points. The output from the filter are the "moving" points after the calculated

transformation has been applied, one point view per input. The transformation

matrix is inserted into the stage's metadata.



.. seealso::



    The plugin wraps the TEASER++ library, which can be found at

    https://github.com/MIT-SPARK/TEASER-plusplus.



.. plugin::



Examples

--------



.. code-block:: json



  [

      "fixed.las",

      "moving.las",

      {

          "type": "filters.teaser"

      },

      "output.las"

  ]



To get the ``transform`` matrix, you'll need to use the ``--metadata`` option

from the pipeline command:



::



    $ pdal pipeline teaser-pipeline.json --metadata teaser-metadata.json



The metadata output might start something like:



.. code-block:: json



    {

        "stages":

        {

            "filters.teaser":

            {

                "centroid": "    583394  5.2831e+06   498.152",

                "composed": "           1  2.60209e-18 -1.97906e-09       -0.374999  8.9407e-08            1  5.58794e-09      -0.614662 6.98492e -10 -5.58794e-09            1   0.033234           0            0            0            1",

                "converged": true,

                "fitness": 0.01953125097,

                "transform": "           1  2.60209e-18 -1.97906e-09       -0.375  8.9407e-08            1  5.58794e-09      -0.5625 6.98492e -10 -5.58794e-09            1   0.00411987           0            0            0            1"

            }





To apply this transformation to other points, the ``centroid`` and

``transform`` metadata items can by used with ``filters.transformation`` in

another pipeline. First, move the centroid of the points to (0,0,0), then apply

the transform, then move the points back to the original location.  For the

above metadata, the pipeline would be similar to:



.. code-block:: json



    [

        {

            "type": "readers.las",

            "filename": "in.las"

        },

        {

            "type": "filters.transformation",

            "matrix": "1 0 0 -583394   0 1 0 -5.2831e+06   0 0 1 -498.152   0 0 0 1"

        },

        {

            "type": "filters.transformation",

            "matrix": "1  2.60209e-18 -1.97906e-09       -0.375  8.9407e-08            1  5.58794e-09      -0.5625 6.98492e -10 -5.58794e-09            1   0.00411987           0            0            0            1"

        },

        {

            "type": "filters.transformation",

            "matrix": "1 0 0 583394   0 1 0 5.2831e+06  0 0 1 498.152  0 0 0 1"

        },

        {

            "type": "writers.las",

            "filename": "out.las"

        }

    ]



.. note::



    The ``composed`` metadata matrix is a composition of the three transformation steps outlined above, and can be used in a single call to ``filters.transformation`` as opposed to the three separate calls.



.. seealso::



    :ref:`filters.transformation` to apply a transform to other points.





Options

--------



nr

  Radius to use for normal estimation. [Default: **0.02**]



fr

  Radius to use when computing features. [Default: **0.04**]



fpfh

  Use FPFH to find correspondences? [Default: **true**]



.. include:: filter_opts.rst


    """

    vars = dict()
    vars['type'] = 'filters.teaser'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def trajectory(dtr=None, dst=None, minsep=None, tblock=None, tout=None, inputs=None, tag=None, **kwargs):
    """.. _filters.trajectory:



filters.trajectory

==================



The **trajectory filter** computes an estimate the the sensor location based

on the position of multiple returns and the sensor scan angle. It is primarily

useful for LAS input as it requires scan angle and return counts in order to

work.



The method is described in detail `here`_. It extends the method of :cite:`Gatziolis2019`.



.. note::



  This filter creates a new dataset describing the trajectory of the sensor,

  replacing the input dataset.



Examples

--------



.. code-block:: json



  [

      "input.las",

      {

          "type": "filters.trajectory"

      },

      "trajectory.las"

  ]





Options

--------



dtr

  Multi-return sampling interval in seconds. [Default: .001]



dst

  Single-return sampling interval in seconds. [Default: .001]



minsep

   Minimum separation of returns considered in meters. [Default: .01]



tblock

  Block size for cublic spline in seconds. [Default: 1.0]



tout

  Output data interval in seconds. [Default: .01]



.. include:: filter_opts.rst



.. _`here`: ../papers/lidar-traj.pdf
    """

    vars = dict()
    vars['type'] = 'filters.trajectory'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def transformation(invert=None, Translation=None, Scaling=None, Rotation=None, inputs=None, tag=None, **kwargs):
    """.. _filters.transformation:



filters.transformation

======================



The transformation filter applies an arbitrary homography

transformation, represented as a 4x4 matrix_, to each xyz triplet.



.. note::



    The transformation filter does not apply or consider any spatial

    reference information.



.. embed::



.. streamable::



Example

-------



This example rotates the points around the z-axis while translating them.



.. code-block:: json



  [

      "untransformed.las",

      {

          "type":"filters.transformation",

          "matrix":"0 -1  0  1  1  0  0  2  0  0  1  3  0  0  0  1"

      },

      {

          "type":"writers.las",

          "filename":"transformed.las"

      }

  ]





Options

-------



invert

  If set to true, applies the inverse of the provided transformation matrix.

  [Default: false]



_`matrix`

  A whitespace-delimited transformation matrix.

  The matrix is assumed to be presented in row-major order.

  Only matrices with sixteen elements are allowed.



.. include:: filter_opts.rst



Further details

---------------



A full tutorial about transformation matrices is beyond the scope of this

documentation. Instead, we will provide a few pointers to introduce core

concepts, especially as pertains to PDAL's handling of the ``matrix`` argument.



Transformations in a 3-dimensional coordinate system can be represented

as a homography transformation using homogeneous coordinates. This 4x4

matrix can represent affine transformations describing operations like

translation, rotation, and scaling of coordinates.  In addition it can

represent perspective transformations modeling a pinhole camera.



The transformation filter's ``matrix`` argument is a space delimited, 16

element string. This string is simply a row-major representation of the 4x4

matrix (i.e., first four elements correspond to the top row of the

transformation matrix and so on).



In the event that readers are accustomed to an alternate representation of the

transformation matrix, we provide some simple examples in the form of pure

translations, rotations, and scaling, and show the corresponding ``matrix``

string.



Translation

...........



A pure translation by :math:`t_x`, :math:`t_y`, and :math:`t_z` in the X, Y,

and Z dimensions is represented by the following matrix.



.. math::



    \begin{matrix}

        1 & 0 & 0 & t_x \\

        0 & 1 & 0 & t_y \\

        0 & 0 & 1 & t_z \\

        0 & 0 & 0 & 1

    \end{matrix}



The JSON syntax required for such a translation is written as follows for :math:`t_x=7`, :math:`t_y=8`, and :math:`t_z=9`.



.. code-block:: json



  [

      {

          "type":"filters.transformation",

          "matrix":"1  0  0  7  0  1  0  8  0  0  1  9  0  0  0  1"

      }

  ]



Scaling

.......



Scaling of coordinates is also possible using a transformation matrix. The

matrix shown below will scale the X coordinates by :math:`s_x`, the Y

coordinates by :math:`s_y`, and Z by :math:`s_z`.



.. math::



    \begin{matrix}

        s_x &   0 &   0 & 0 \\

          0 & s_y &   0 & 0 \\

          0 &   0 & s_z & 0 \\

          0 &   0 &   0 & 1

    \end{matrix}



We again provide an example JSON snippet to demonstrate the scaling

transformation. In the example, X and Y are not scaled at all (i.e.,

:math:`s_x=s_y=1`) and Z is magnified by a factor of 2 (:math:`s_z=2`).



.. code-block:: json



  [

      {

          "type":"filters.transformation",

          "matrix":"1  0  0  0  0  1  0  0  0  0  2  0  0  0  0  1"

      }

  ]



Rotation

........



A rotation of coordinates by :math:`\theta` radians counter-clockwise about

the z-axis is accomplished with the following matrix.



.. math::



    \begin{matrix}

        \cos{\theta} & -\sin{\theta} & 0 & 0 \\

        \sin{\theta} &  \cos{\theta} & 0 & 0 \\

                   0 &             0 & 1 & 0 \\

                   0 &             0 & 0 & 1

    \end{matrix}



In JSON, a rotation of 90 degrees (:math:`\theta=1.57` radians) takes the form

shown below.



.. code-block:: json



  [

      {

          "type":"filters.transformation",

          "matrix":"0  0  -1  0  1  0  0  0  0  0  1  0  0  0  0  1"

      }

  ]



Similarly, a rotation about the x-axis by :math:`\theta` radians is represented

as



.. math::



    \begin{matrix}

        1 &            0 &             0 & 0 \\

        0 & \cos{\theta} & -\sin{\theta} & 0 \\

        0 & \sin{\theta} &  \cos{\theta} & 0 \\

        0 &            0 &             0 & 1

    \end{matrix}



which takes the following form in JSON for a rotation of 45 degrees (:math:`\theta=0.785` radians)



.. code-block:: json



  [

      {

          "type":"filters.transformation",

          "matrix":"1  0  0  0  0  0.707  -0.707  0  0  0.707  0.707  0  0  0  0  1"

      }

  ]



Finally, a rotation by :math:`\theta` radians about the y-axis is accomplished

with the matrix



.. math::



    \begin{matrix}

         \cos{\theta} & 0 & \sin{\theta} & 0 \\

                    0 & 1 &            0 & 0 \\

        -\sin{\theta} & 0 & \cos{\theta} & 0 \\

                    0 & 0 &            0 & 1

    \end{matrix}



and the JSON string for a rotation of 10 degrees (:math:`\theta=0.175` radians) becomes



.. code-block:: json



  [

      {

          "type":"filters.transformation",

          "matrix":"0.985  0  0.174  0  0  1  0  0  -0.174  0  0.985  0  0  0  0  1"

      }

  ]
    """

    vars = dict()
    vars['type'] = 'filters.transformation'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def voxelcenternearestneighbor(cell=None, inputs=None, tag=None, **kwargs):
    """.. _filters.voxelcenternearestneighbor:



filters.voxelcenternearestneighbor

===============================================================================



The **VoxelCenterNearestNeighbor filter** is a voxel-based sampling filter.

The input point

cloud is divided into 3D voxels at the given cell size. For each populated

voxel, the coordinates of the voxel center are used as the query point in a 3D

nearest neighbor search. The nearest neighbor is then added to the output point

cloud, along with any existing dimensions.



.. embed::





Example

-------



.. code-block:: json



  [

      "input.las",

      {

          "type":"filters.voxelcenternearestneighbor",

          "cell":10.0

      },

      "output.las"

  ]



.. seealso::



    :ref:`filters.voxelcentroidnearestneighbor` offers a similar solution,

    using as the query point the centroid of all points falling within the voxel as

    opposed to the voxel center coordinates.  The drawback with this approach is that

    all dimensional data is lost, leaving the the sampled cloud consisting of only

    XYZ coordinates.



Options

-------------------------------------------------------------------------------



cell

  Cell size in the ``X``, ``Y``, and ``Z`` dimension. [Default: 1.0]



.. include:: filter_opts.rst


    """

    vars = dict()
    vars['type'] = 'filters.voxelcenternearestneighbor'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def voxelcentroidnearestneighbor(cell=None, inputs=None, tag=None, **kwargs):
    """.. _filters.voxelcentroidnearestneighbor:



filters.voxelcentroidnearestneighbor

===============================================================================



The **VoxelCentroidNearestNeighbor Filter** is a voxel-based sampling filter.

The input point cloud is divided into 3D voxels at the given cell size. For

each populated voxel, we apply the following ruleset. For voxels with only one

point, the point is passed through to the output. For voxels with exactly two

points, the point closest the voxel center is returned. Finally, for voxels

with more than two points, the centroid of the points within that voxel is

computed. This centroid is used as the query point in a 3D nearest neighbor

search (considering only those points lying within the voxel). The nearest

neighbor is then added to the output point cloud, along with any existing

dimensions.



.. embed::



Example

-------





.. code-block:: json



  [

      "input.las",

      {

          "type":"filters.voxelcentroidnearestneighbor",

          "cell":10.0

      },

      "output.las"

  ]



.. seealso::



    :ref:`filters.voxelcenternearestneighbor` offers a similar solution, using

    the voxel center as opposed to the voxel centroid for the query point.



Options

-------------------------------------------------------------------------------



cell

  Cell size in the ``X``, ``Y``, and ``Z`` dimension. [Default: 1.0]



.. include:: filter_opts.rst


    """

    vars = dict()
    vars['type'] = 'filters.voxelcentroidnearestneighbor'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def voxeldownsize(cell=None, mode=None, inputs=None, tag=None, **kwargs):
    """.. _filters.voxeldownsize:



filters.voxeldownsize

===============================================================================



The **voxeldownsize filter** is a voxel-based sampling filter.

The input point cloud is divided into 3D voxels at the given cell size.

For each populated voxel, either first point entering in the voxel or

center of a voxel (depending on mode argument) is accepted and voxel is

marked as populated.  All other points entering in the same voxel are

filtered out.



Example

-------



.. code-block:: json



  [

      "input.las",

      {

          "type":"filters.voxeldownsize",

          "cell":1.0,

          "mode":"center"

      },

      "output.las"

  ]



.. seealso::



    :ref:`filters.voxelcenternearestneighbor` offers a similar solution,

    using the coordinates of the voxel center as the query point in a 3D

    nearest neighbor search.  The nearest neighbor is then added to the

    output point cloud, along with any existing dimensions.



Options

-------------------------------------------------------------------------------



cell

  Cell size in the ``X``, ``Y``, and ``Z`` dimension. [Default: 0.001]



mode

  Mode for voxel based filtering. [Default: center]

  **center**: Coordinates of the first point found in each voxel will

  be modified to be the center of the voxel.

  **first**: Only the first point found in each voxel is retained.



.. include:: filter_opts.rst



.. warning::

    If you choose **center** mode, you are overwriting the X, Y and Z

    values of retained points.  This may invalidate other dimensions of

    the point if they depend on this location or the location of other points

    in the input.

  
    """

    vars = dict()
    vars['type'] = 'filters.voxeldownsize'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def zsmooth(radius=None, medianpercent=None, dim=None, inputs=None, tag=None, **kwargs):
    """.. _filters.zsmooth:



filters.zsmooth

===============================================================================



The **Zsmooth Filter** computes a new Z value as another dimension that is based

on the Z values of neighboring points.



All points within some distance in the X-Y plane from a reference point are ordered by Z value.

The reference point's new smoothed Z value is chosen to be that of the Nth median value of

the neighboring points, where N is specified as the _`medianpercent` option.



Use :ref:`filters.assign` to assign the smoothed Z value to the actual Z dimension if

desired.



Example

-------



Compute the smoothed Z value as the median Z value of the neighbors within 2 units and

assign the value back to the Z dimension.



.. code_block::json



    [

        "input.las",

        {

            "type": "filters.zsmooth",

            "radius": 2,

            "dim": "Zadj"

        },

        {

            "type": "filters.assign",

            "value": "Z = Zadj"

        },

        "output.las"

    ]



Options

-------------------------------------------------------------------------------



radius

  All points within `radius` units from the reference point in the X-Y plane are considered

  to determine the smoothed Z value. [Default: 1]



medianpercent

  A value between 0 and 100 that specifies the relative position of ordered Z values of neighbors

  to use as the new smoothed Z value. 0 specifies the minimum value. 100 specifies the

  maximum value. 50 specifies the mathematical median of the values. [Default: 50]



dim

  The name of a dimension to use for the adjusted Z value. Cannot be 'Z'. [Required]



.. include:: filter_opts.rst


    """

    vars = dict()
    vars['type'] = 'filters.zsmooth'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars
