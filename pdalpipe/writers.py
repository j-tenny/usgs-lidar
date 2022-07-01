def bpf(filename=None, compression=None, format=None, bundledfile=None, header_data=None, coord_id=None, output_dims=None, inputs=None, tag=None, **kwargs):
    """.. _writers.bpf:



writers.bpf

===========



BPF is an `NGA specification`_ for point cloud data.  The PDAL **BPF Writer**

only supports writing of version 3 BPF format files.



.. _NGA specification: https://nsgreg.nga.mil/doc/view?i=4202



.. embed::



.. streamable::



Example

-------



.. code-block:: json



  [

      {

          "type":"readers.bpf",

          "filename":"inputfile.las"

      },

      {

          "type":"writers.bpf",

          "filename":"outputfile.bpf"

      }

  ]



Options

-------



filename

    BPF file to write.  The writer will accept a filename containing

    a single placeholder character ('#').  If input to the writer consists

    of multiple PointViews, each will be written to a separate file, where

    the placeholder will be replaced with an incrementing integer.  If no

    placeholder is found, all PointViews provided to the writer are

    aggregated into a single file for output.  Multiple PointViews are usually

    the result of using :ref:`filters.splitter`, :ref:`filters.chipper` or

    :ref:`filters.divider`.

    [Required]



compression

    This option can be set to true to cause the file to be written with Zlib

    compression as described in the BPF specification.  [Default: false]



format

    Specifies the format for storing points in the file. [Default: dim]



    * dim: Dimension-major (non-interleaved).  All data for a single dimension

      are stored contiguously.

    * point: Point-major (interleaved).  All data for a single point

      are stored contiguously.

    * byte: Byte-major (byte-segregated).  All data for a single dimension are

      stored contiguously, but bytes are arranged such that the first bytes for

      all points are stored contiguously, followed by the second bytes of all

      points, etc.  See the BPF specification for further information.



bundledfile

    Path of file to be written as a bundled file (see specification).  The path

    part of the filespec is removed and the filename is stored as part of the

    data.  This option can be specified as many times as desired.



header_data

    Base64-encoded data that will be decoded and written following the

    standard BPF header.



coord_id

    The coordinate ID (UTM zone) of the data.  Southern zones take negative

    values.  A value of 0 indicates cartesian instead of UTM coordinates.  A

    value of 'auto' will attempt to set the UTM zone from a suitable spatial

    reference, or set to 0 if no such SRS is set.  [Default: 0]



scale_x, scale_y, scale_z

    Scale to be divided from the X, Y and Z nominal values, respectively, after

    the offset has been applied.  The special value "auto" can be specified,

    which causes the writer to select a scale to set the stored values of the

    dimensions to range from [0, 2147483647].  [Default: .01]



    Note: written value = (nominal value - offset) / scale.



offset_x, offset_y, offset_z

    Offset to be subtracted from the X, Y and Z nominal values, respectively,

    before the value is scaled.  The special value "auto" can be specified,

    which causes the writer to set the offset to the minimum value of the

    dimension.  [Default: auto]



    Note: written value = (nominal value - offset) / scale.



    .. note::



        Because BPF data is always stored in UTM, the XYZ offsets are set to

        "auto" by default. This is to avoid truncation of the decimal digits

        (which may occur with offsets left at 0).



output_dims

    If specified, limits the dimensions written for each point.  Dimensions

    are listed by name and separated by commas.  X, Y and Z are required and

    must be explicitly listed.



.. include:: writer_opts.rst


    """

    vars = dict()
    vars['type'] = 'writers.bpf'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def copc(filename=None, software_id=None, creation_doy=None, creation_year=None, system_id=None, global_encoding=None, project_id=None, filesource_id=None, pipeline=None, vlrs=None, inputs=None, tag=None, **kwargs):
    """.. _writers.copc:



writers.copc

============



The **COPC Writer** supports writing to `COPC format`_ files.



.. embed::



VLRs

----



VLRs can be created by providing a JSON node called `vlrs` with objects

as shown:



.. code-block:: json



  [

      {

          "type":"readers.las",

          "filename":"inputfile.las"

      },

      {

          "type":"writers.las",

          "vlrs": [{

              "description": "A description under 32 bytes",

              "record_id": 42,

              "user_id": "hobu",

              "data": "dGhpcyBpcyBzb21lIHRleHQ="

              },

              {

              "description": "A description under 32 bytes",

              "record_id": 43,

              "user_id": "hobu",

              "filename": "path-to-my-file.input"

              },

              {

              "description": "A description under 32 bytes",

              "record_id": 44,

              "user_id": "hobu",

              "metadata": "metadata_keyname"

              }],

          "filename":"outputfile.las"

      }

  ]



.. note::



    One of `data`, `filename` or `metadata` must be specified. Data must be

    specified as base64 encoded strings. The content of a file is inserted as

    binary. The metadata key specified must refer to a string or base64 encoded data.



Example

-------



.. code-block:: json



  [

      "inputfile1.las",

      "inputfile2.laz",

      {

          "type":"writers.copc",

          "filename":"outputfile.copc.laz"

      }

  ]





Options

-------



filename

  Output filename.  [Required]



_`forward`

  List of header fields whose values should be preserved from a source

  LAS file.  The option can be specified multiple times, which has the same effect as

  listing values separated by a comma.  The following values are valid:

  ``filesource_id``, ``global_encoding``, ``project_id``, ``system_id``, ``software_id``,

  ``creation_doy``, ``creation_year``, ``scale_x``, ``scale_y``, ``scale_z``,

  ``offset_x``, ``offset_y``, ``offset_z``.  In addition, the special value ``header``

  can be specified, which is equivalent to specifying all the values EXCEPT the scale and

  offset values.  Scale and offset values can be forwarded as a group by

  using the special values ``scale`` and ``offset`` respectively.  The special

  value ``all`` is equivalent to specifying ``header``, ``scale``, ``offset`` and

  ``vlr`` (see below).  If a header option is specified explicitly, it will override

  any forwarded header value.

  If a LAS file is the result of multiple LAS input files, the header values

  to be forwarded must match or they will be ignored and a default will

  be used instead.



  VLRs can be forwarded by using the special value ``vlr``.  VLRs containing

  the following User IDs are NOT forwarded: ``LASF_Projection``,

  ``liblas``, ``laszip encoded``.  VLRs with the User ID ``LASF_Spec`` and

  a record ID other than 0 or 3 are also not forwarded.  These VLRs are known

  to contain information regarding the formatting of the data and will be rebuilt

  properly in the output file as necessary.  Unlike header values, VLRs from multiple

  input files are accumulated and each is written to the output file.  Forwarded

  VLRs may contain duplicate User ID/Record ID pairs.



software_id

  String identifying the software that created this LAS file.

  [Default: PDAL version num (build num)]"



creation_doy

  Number of the day of the year (January 1 == 1) this file is being created.



creation_year

  Year (Gregorian) this file is being created.



system_id

  String identifying the system that created this LAS file. [Default: "PDAL"]



global_encoding

  Various indicators to describe the data.  See the LAS documentation.  Note

  that PDAL will always set bit four when creating LAS version 1.4 output.

  [Default: 0]



project_id

  UID reserved for the user [Default: Nil UID]



scale_x, scale_y, scale_z

  Scale to be divided from the X, Y and Z nominal values, respectively, after

  the offset has been applied.  The special value ``auto`` can be specified,

  which causes the writer to select a scale to set the stored values of the

  dimensions to range from [0, 2147483647].  [Default: .01]



  Note: written value = (nominal value - offset) / scale.



offset_x, offset_y, offset_z

   Offset to be subtracted from the X, Y and Z nominal values, respectively,

   before the value is scaled.  The special value ``auto`` can be specified,

   which causes the writer to set the offset to the minimum value of the

   dimension.  [Default: 0]



   Note: written value = (nominal value - offset) / scale.



filesource_id

  The file source id number to use for this file (a value between

  0 and 65535 - 0 implies "unassigned") [Default: 0]



pipeline

  Write a JSON representation of the running pipeline as a VLR.



vlrs

    Add VLRS specified as json. See `VLRs`_ above for details.



.. include:: writer_opts.rst



.. _COPC format: https://copc.io/


    """

    vars = dict()
    vars['type'] = 'writers.copc'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def draco(filename=None, dimensions=None, quantization=None, inputs=None, tag=None, **kwargs):
    """.. _writers.draco:



writers.draco

=============



`Draco`_ is a library for compressing and decompressing 3D geometric meshes and

point clouds and was designed and built for compression efficiency and speed.

The code supports compressing points, connectivity information, texture coordinates,

color information, normals, and any other generic attributes associated with geometry.



This writer aims to use the encoding feature of the Draco library to compress and

output Draco files.



Example

--------------------------------------------------------------------------------



This example will read in a las file and output a Draco encoded file, with options

to include PDAL dimensions X, Y, and Z as double, and explicitly setting quantization

levels of some of the Draco attributes.



.. code-block:: json



    [

        {

            "type": "readers.las",

            "filename": "color.las"

        },

        {

            "type": "writers.draco",

            "filename": "draco.drc",

            "dimensions": {

                "X": "float",

                "Y": "float",

                "Z": "float"

            },

            "quantization": {

                "NORMAL": 8,

                "TEX_COORD": 7,

                "GENERIC": 6

            }

        }

    ]



Options

-------



filename

    Output file name. [Required]



dimensions

    A json map of PDAL dimensions to desired data types. Data types must be string

    and must be available in `PDAL's Type specification`_. Any dimension that

    combine to make one Draco dimension must all have the same type (eg. POSITION is

    made up of X, Y, and Z. X cannot by float while Y and Z are specified as double)



    This argument will filter the dimensions being written to only the dimensions

    that have been specified. If that dimension is part of a multi-dimensional

    draco attribute (POSITION=[X,Y,Z]), then any dimension not specified will be

    filled in with zeros.



quantization

    A json map of Draco attributes to desired quantization levels. These levels

    must be integers. Default quantization levels are below, and will be

    overridden by any values placed in the options.



.. code-block:: json



    {

        "POSITION": 11,

        "NORMAL": 7,

        "TEX_COORD": 10,

        "COLOR": 8,

        "GENERIC": 8

    }



.. include:: writer_opts.rst



.. _PDAL's Type specification: https://github.com/PDAL/PDAL/blob/master/pdal/DimUtil.hpp

.. _Draco: https://github.com/google/draco
    """

    vars = dict()
    vars['type'] = 'writers.draco'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def e57(doublePrecision=None, inputs=None, tag=None, **kwargs):
    """.. _writers.e57:



writers.e57

===========



The **E57 Writer** supports writing to E57 files.



The writer supports E57 files with Cartesian point clouds.



.. note::



   E57 files can contain multiple point clouds stored in a single

   file.  The writer will only write a single cloud per file.



.. note::



   Spherical format points are not supported.



.. note::



   The E57 `cartesianInvalidState` dimension is mapped to the Omit

   PDAL dimension.  A range filter can be used to filter out the

   invalid points.



.. plugin::



.. streamable::





Example

-------



.. code-block:: json



  [

      {

          "type":"readers.las",

          "filename":"inputfile.las"

      },

      {

          "type":"writers.e57",

          "filename":"outputfile.e57",

            "doublePrecision":false

      }

  ]





Options

-------



_`filename`

  E57 file to write [Required]



doublePrecision

  Use double precision for storage (false by default).



.. include:: writer_opts.rst


    """

    vars = dict()
    vars['type'] = 'writers.e57'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def ept_addon(addons=None, threads=None, inputs=None, tag=None, **kwargs):
    """.. _writers.ept_addon:



writers.ept_addon

=================



The **EPT Addon Writer** supports writing additional dimensions to

`Entwine Point Tile`_ datasets.  The EPT addon writer may only

be used in a pipeline with an :ref:`EPT reader <readers.ept>`, and it

creates additional attributes for an existing dataset rather than

creating a brand new one.



The addon dimensions created by this writer are stored independently from the corresponding EPT dataset, therefore write-access to the EPT resource itself is not required to create and use addon dimensions.



.. embed::



Example

--------------------------------------------------------------------------------



This example downloads the Autzen dataset (10M points) and runs the

:ref:`SMRF filter <filters.smrf>`, which populates the ``Classification``

dimension with ground values, and writes the resulting attribute to an EPT

addon dataset on the local filesystem.



.. code-block:: json



  [

      {

          "type": "readers.ept",

           "filename": "http://na.entwine.io/autzen/ept.json"

      },

      {

          "type": "filters.assign",

          "assignment": "Classification[:]=0"

      },

      {

          "type": "filters.smrf"

      },

      {

          "type": "writers.ept_addon",

          "addons": { "~/entwine/addons/autzen/smrf": "Classification" }

      }

  ]



And here is a follow-up example of reading this dataset with the

:ref:`EPT reader <readers.ept>` with the created addon overwriting the

``Classification`` value.  The output is then written to a single file

with the :ref:`LAS writer <writers.las>`.



.. code-block:: json



  [

      {

          "type": "readers.ept",

          "filename": "http://na.entwine.io/autzen/ept.json",

          "addons": { "Classification": "~/entwine/addons/autzen/smrf" }

      },

      {

          "type": "writers.las",

          "filename": "autzen-ept-smrf.las"

      }

  ]



This is an example of using multiple mappings in the ``addons`` option to

apply a new color scheme with :ref:`filters.colorinterp` mapping the

Red, Green, and Blue dimensions to new values.



.. code-block:: json



  [

      {

          "type": "readers.ept",

          "filename": "http://na.entwine.io/autzen/ept.json"

      },

      {

          "type": "filters.colorinterp"

      },

      {

          "type": "writers.ept_addon",

          "addons": {

              "~/entwine/addons/autzen/interp/Red":   "Red",

              "~/entwine/addons/autzen/interp/Green": "Green",

              "~/entwine/addons/autzen/interp/Blue":  "Blue"

          }

      }

  ]



The following pipeline will read the data with the new colors:



.. code-block:: json



  [

      {

          "type": "readers.ept",

          "filename": "http://na.entwine.io/autzen/ept.json",

          "addons": {

              "Red":   "~/entwine/addons/autzen/interp/Red",

              "Green": "~/entwine/addons/autzen/interp/Green",

              "Blue":  "~/entwine/addons/autzen/interp/Blue"

          }

      },

      {

          "type": "writers.las",

          "filename": "autzen-ept-interp.las"

      }

  ]



Options

--------------------------------------------------------------------------------



addons

   A JSON object whose keys represent output paths for each addon dimension,

   and whose corresponding values represent the attributes to be written to

   these addon dimensions. [Required]



.. note::



   The `addons` option is reversed between the EPT reader and addon-writer: in each case, the right-hand side represents an assignment to the left-hand side.  In the writer, the dimension value is assigned to an addon path.  In the reader, the addon path is assigned to a dimension.



threads

    Number of worker threads used to write EPT addon data.  A minimum of 4 will be used no matter what value is specified.



.. include:: writer_opts.rst



.. _Entwine Point Tile: https://entwine.io/entwine-point-tile.html


    """

    vars = dict()
    vars['type'] = 'writers.ept_addon'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def fbx(filename=None, ascii=None, inputs=None, tag=None, **kwargs):
    """.. _writers.fbx:



writers.fbx

===========



Output to the Autodesk FBX format. You must use a filter that

creates a mesh, such as :ref:`filters.poisson` or `filters.greedyprojection`,

in order to use this writer.



.. plugin::



Compilation

-------------



You must download and install the Autodesk SDK

and then compile the PDAL FBX plugin against it. Visit

https://www.autodesk.com/developer-network/platform-technologies/fbx-sdk-2019-0

to obtain a current copy of the SDK.



Example Windows CMake configuration



::

      -DFBX_ROOT_DIR:FILEPATH="C:\fbx\2019.0" ^

      -DBUILD_PLUGIN_FBX=ON ^





Example

-------



.. code-block:: json



  [

      {

          "type":"readers.las",

          "filename":"inputfile.las"

      },

      {

          "type":"filters.poisson"

      },

      {

          "type":"writers.fbox",

          "filename":"outputfile.fbx"

      }

  ]



..code-block:: shell



    pdal translate autzen.las autzen.fbx -f poisson



Options

-------



filename

    FBX filename to write.  [Required]



ascii

    Write ASCII FBX format.  [Default: false]



.. include:: writer_opts.rst


    """

    vars = dict()
    vars['type'] = 'writers.fbx'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def gdal(filename=None, resolution=None, radius=None, power=None, gdaldriver=None, gdalopts=None, data_type=None, nodata=None, output_type=None, window_size=None, dimension=None, bounds=None, origin_x=None, origin_y=None, width=None, height=None, override_srs=None, default_srs=None, inputs=None, tag=None, **kwargs):
    """.. _writers.gdal:



writers.gdal

================================================================================



The **GDAL writer** creates a raster from a point cloud using an interpolation

algorithm.  Output is produced using `GDAL`_ and can use any `driver

that supports creation of rasters`_.  A data_type_ can be specified for the

raster (double, float, int32, etc.).  If no data type is specified, the

data type with the largest range supported by the driver is used.



.. _`GDAL`: http://gdal.org

.. _`driver that supports creation of rasters`: http://www.gdal.org/formats_list.html



The technique used to create the raster is a simple interpolation where

each point that falls within a given radius_ of a raster cell center

potentially contributes to the raster's value.  If no radius is provided,

it is set to the product of the resolution_ and the square root of two.

If a circle with the provided radius

doesn't encompass the entire cell, it is possible that some points will

not be considered at all, including those that may be within the bounds

of the raster cell.



The GDAL writer creates rasters using the data specified in the dimension_

option (defaults to `Z`). The writer creates up to six rasters based on

different statistics in the output dataset.  The order of the layers in the

dataset is as follows:



min

    Give the cell the minimum value of all points within the given radius.



max

    Give the cell the maximum value of all points within the given radius.



mean

    Give the cell the mean value of all points within the given radius.



idw

    Cells are assigned a value based on `Shepard's inverse distance weighting`_

    algorithm, considering all points within the given radius.



count

    Give the cell the number of points that lie within the given radius.



stdev

    Give the cell the population standard deviation of the points that lie

    within the given radius.



.. _`Shepard's inverse distance weighting`: https://en.wikipedia.org/wiki/Inverse_distance_weighting



If no points fall within the circle about a raster cell, a secondary

algorithm can be used to attempt to provide a value after the standard

interpolation is complete.  If the window_size_ option is non-zero, the

values of a square of rasters surrounding an empty cell is applied

using inverse distance weighting of any non-empty cells.

The value provided for window_size is the

maximum horizontal or vertical distance that a donor cell may be in order to

contribute to the subject cell (A window_size of 1 essentially creates a 3x3

array around the subject cell.  A window_size of 2 creates a 5x5 array, and

so on.)



Cells that have no value after interpolation are given a value specified by

the nodata_ option.



.. embed::



.. streamable::





Basic Example

--------------------------------------------------------------------------------



This  pipeline reads the file autzen_trim.las and creates a Geotiff dataset

called outputfile.tif.  Since output_type isn't specified, it creates six

raster bands ("min", "max", "mean", "idx", "count" and "stdev") in the output

dataset.  The raster cells are 10x10 and the radius used to locate points

whose values contribute to the cell value is 14.14.



.. code-block:: json



  [

      "pdal/test/data/las/autzen_trim.las",

      {

          "resolution": 10,

          "radius": 14.14,

          "filename":"outputfile.tif"

      }

  ]





Options

--------------------------------------------------------------------------------



filename

    Name of output file. The writer will accept a filename containing

    a single placeholder character (`#`).  If input to the writer consists

    of multiple PointViews, each will be written to a separate file, where

    the placeholder will be replaced with an incrementing integer.  If no

    placeholder is found, all PointViews provided to the writer are

    aggregated into a single file for output.  Multiple PointViews are usually

    the result of using :ref:`filters.splitter`, :ref:`filters.chipper` or

    :ref:`filters.divider`.[Required]



.. _resolution:



resolution

    Length of raster cell edges in X/Y units.  [Required]



.. _radius:



radius

    Radius about cell center bounding points to use to calculate a cell value.

    [Default: resolution_ * sqrt(2)]



power

    Exponent of the distance when computing IDW. Close points have higher

    significance than far points. [Default: 1.0]



gdaldriver

    GDAL code of the `GDAL driver`_ to use to write the output.

    [Default: "GTiff"]



.. _`GDAL driver`: http://www.gdal.org/formats_list.html



gdalopts

    A list of key/value options to pass directly to the GDAL driver.  The

    format is name=value,name=value,...  The option may be specified

    any number of times.



    .. note::

        The INTERLEAVE GDAL driver option is not supported.  writers.gdal

        always uses BAND interleaving.



.. _data_type:



data_type

    The :ref:`data type <types>` to use for the output raster.

    Many GDAL drivers only

    support a limited set of output data types.

    [Default: depends on the driver]



.. _nodata:



nodata

    The value to use for a raster cell if no data exists in the input data

    with which to compute an output cell value. [Default: depends on the

    data_type_.  -9999 for double, float, int and short, 9999 for

    unsigned int and unsigned short, 255 for unsigned char and -128 for char]



.. _output_type:



output_type

    A comma separated list of statistics for which to produce raster layers.

    The supported values are "min", "max", "mean", "idw", "count", "stdev"

    and "all".  The option may be specified more than once. [Default: "all"]



.. _window_size:



window_size

    The maximum distance from a donor cell to a target cell when applying

    the fallback interpolation method.  See the stage description for more

    information. [Default: 0]



.. _dimension:



dimension

  A dimension name to use for the interpolation. [Default: "Z"]



bounds

  The bounds of the data to be written.  Points not in bounds are discarded.

  The format is ([minx, maxx],[miny,maxy]). [Optional]



origin_x

  X origin (lower left corner) of the grid. [Default: None]



origin_y

  Y origin (lower left corner) of the grid. [Default: None]



width

  Number of cells in the X direction. [Default: None]



height

  Number of cells in the Y direction. [Default: None]



override_srs

  Write the raster with the provided SRS. [Default: None]



default_srs

  Write the raster with the provided SRS if none exists. [Default: None]



metadata:

  Add or set GDAL metadata to set on the raster, in the form

  ``NAME=VALUE,NAME2=VALUE2,NAME3=VALUE3`` [Default: None]



pdal_metadata:

  Write PDAL's pipeline and metadata as base64 to the GDAL PAM metadata [Default: False]





.. include:: writer_opts.rst



.. note::

    You may use the 'bounds' option, or 'origin_x', 'origin_y', 'width'

    and 'height', but not both.



.. note::

    Unless the raster being written is empty, the spatial reference will automatically

    come from the data and does not need to be set with 'override_srs' or 'default_srs'.
    """

    vars = dict()
    vars['type'] = 'writers.gdal'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def gltf(filename=None, metallic=None, roughness=None, red=None, green=None, blue=None, alpha=None, double_sided=None, colors=None, normals=None, inputs=None, tag=None, **kwargs):
    """.. _writers.gltf:



writers.gltf

============



GLTF is a file format `specification`_ for 3D graphics data.

If a mesh has been generated

for a PDAL point view, the **GLTF Writer** will produce simple output in

the GLTF format.  PDAL does not currently support many of the attributes

that can be found in a GLTF file.  This writer creates a *binary* GLTF (extension '.glb').



.. _specification: https://www.khronos.org/gltf/



.. embed::



Example

-------



.. code-block:: json



  [

      "infile.las",

      {

          "type": "filters.poisson",

          "depth": 12

      },

      {

          "type":"writers.gltf",

          "filename":"output.glb",

          "red": 0.8,

          "metallic": 0.5

      }

  ]



Options

-------



filename

    Name of the GLTF (.glb) file to be written. [Required]



metallic

    The metallic factor of the faces. [Default: 0]

    

roughness

    The roughness factor of the faces. [Default: 0]

    

red

    The base red component of the color applied to the faces. [Default: 0]

    

green

    The base green component of the color applied to the faces. [Default: 0]

    

blue

    The base blue component of the color applied to the faces. [Default: 0]

    

alpha

    The alpha component to be applied to the faces. [Default: 1.0]



double_sided

    Whether the faces are colored on both sides, or just the side

    visible from the initial observation point (positive normal vector).

    [Default: false]



colors

    Write color data for each vertex.  Red, Green and Blue dimensions must exist.

    Note that most renderers will "interpolate the

    color of each vertex across a face, so this may look odd." [Default: false]



normals

    Write vertex normals. NormalX, NormalY and NormalZ dimensions must exist. [Default: false]



.. include:: writer_opts.rst


    """

    vars = dict()
    vars['type'] = 'writers.gltf'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def las(filename=None, minor_version=None, software_id=None, creation_doy=None, creation_year=None, dataformat_id=None, system_id=None, a_srs=None, global_encoding=None, project_id=None, compression=None, filesource_id=None, discard_high_return_numbers=None, extra_dims=None, pdal_metadata=None, vlrs=None, inputs=None, tag=None, **kwargs):
    """.. _writers.las:



writers.las

===========



The **LAS Writer** supports writing to `LAS format`_ files, the standard

interchange file format for LIDAR data.



.. warning::



    Scale/offset are not preserved from an input LAS file.  See below for

    information on the scale/offset options and the `forward`_ option.



.. embed::



.. streamable::



VLRs

----



VLRs can be created by providing a JSON node called `vlrs` with objects

as shown:



.. code-block:: json



  [

      {

          "type":"readers.las",

          "filename":"inputfile.las"

      },

      {

          "type":"writers.las",

          "vlrs": [{

              "description": "A description under 32 bytes",

              "record_id": 42,

              "user_id": "hobu",

              "data": "dGhpcyBpcyBzb21lIHRleHQ="

              },

              {

              "description": "A description under 32 bytes",

              "record_id": 43,

              "user_id": "hobu",

              "filename": "path-to-my-file.input"

              },

              {

              "description": "A description under 32 bytes",

              "record_id": 44,

              "user_id": "hobu",

              "metadata": "metadata_keyname"

              }],

          "filename":"outputfile.las"

      }

  ]



.. note::



    One of `data`, `filename` or `metadata` must be specified. Data must be

    specified as base64 encoded strings. The content of a file is inserted as

    binary. The metadata key specified must refer to a string or base64 encoded data.





Example

-------



.. code-block:: json



  [

      {

          "type":"readers.las",

          "filename":"inputfile.las"

      },

      {

          "type":"writers.las",

          "filename":"outputfile.las"

      }

  ]





Options

-------



filename

  Output filename. The writer will accept a filename containing

  a single placeholder character (`#`).  If input to the writer consists

  of multiple PointViews, each will be written to a separate file, where

  the placeholder will be replaced with an incrementing integer.  If no

  placeholder is found, all PointViews provided to the writer are

  aggregated into a single file for output.  Multiple PointViews are usually

  the result of using :ref:`filters.splitter`, :ref:`filters.chipper` or

  :ref:`filters.divider`.

  [Required]



_`forward`

  List of header fields whose values should be preserved from a source

  LAS file.  The

  option can be specified multiple times, which has the same effect as

  listing values separated by a comma.  The following values are valid:

  ``major_version``, ``minor_version``, ``dataformat_id``, ``filesource_id``,

  ``global_encoding``, ``project_id``, ``system_id``, ``software_id``, ``creation_doy``,

  ``creation_year``, ``scale_x``, ``scale_y``, ``scale_z``, ``offset_x``, ``offset_y``,

  ``offset_z``.  In addition, the special value ``header`` can be specified,

  which is equivalent to specifying all the values EXCEPT the scale and

  offset values.  Scale and offset values can be forwarded as a group by

  using the special values ``scale`` and ``offset`` respectively.  The special

  value ``all`` is equivalent to specifying ``header``, ``scale``, ``offset`` and

  ``vlr`` (see below).

  If a header option is specified explicitly, it will override any forwarded

  header value.

  If a LAS file is the result of multiple LAS input files, the header values

  to be forwarded must match or they will be ignored and a default will

  be used instead.



  VLRs can be forwarded by using the special value ``vlr``.  VLRs containing

  the following User IDs are NOT forwarded: ``LASF_Projection``,

  ``liblas``, ``laszip encoded``.  VLRs with the User ID ``LASF_Spec`` and

  a record ID other than 0 or 3 are also not forwarded.  These VLRs are known

  to contain information

  regarding the formatting of the data and will be rebuilt properly in the

  output file as necessary.  Unlike header values, VLRs from multiple input

  files are accumulated and each is written to the output file.  Forwarded

  VLRs may contain duplicate User ID/Record ID pairs.



minor_version

  All LAS files are version 1, but the minor version (0 - 4) can be specified

  with this option. [Default: 2]



software_id

  String identifying the software that created this LAS file.

  [Default: PDAL version num (build num)]"



creation_doy

  Number of the day of the year (January 1 == 1) this file is being created.



creation_year

  Year (Gregorian) this file is being created.



dataformat_id

  Controls whether information about color and time are stored with the point

  information in the LAS file. [Default: 3]



  * 0 == no color or time stored

  * 1 == time is stored

  * 2 == color is stored

  * 3 == color and time are stored

  * 4 [Not Currently Supported]

  * 5 [Not Currently Supported]

  * 6 == time is stored (version 1.4+ only)

  * 7 == time and color are stored (version 1.4+ only)

  * 8 == time, color and near infrared are stored (version 1.4+ only)

  * 9 [Not Currently Supported]

  * 10 [Not Currently Supported]



system_id

  String identifying the system that created this LAS file. [Default: "PDAL"]



a_srs

  The spatial reference system of the file to be written. Can be an EPSG string

  (e.g. "EPSG:26910") or a WKT string. [Default: Not set]



global_encoding

  Various indicators to describe the data.  See the LAS documentation.  Note

  that PDAL will always set bit four when creating LAS version 1.4 output.

  [Default: 0]



project_id

  UID reserved for the user [Default: Nil UID]



compression

  Set to "lazperf" or "laszip" to apply compression to the output, creating

  a LAZ file instead of an LAS file.  "lazperf" selects the LazPerf compressor

  and "laszip" (or "true") selects the LasZip compressor. PDAL must have

  been built with support for the requested compressor.  [Default: "none"]



scale_x, scale_y, scale_z

  Scale to be divided from the X, Y and Z nominal values, respectively, after

  the offset has been applied.  The special value ``auto`` can be specified,

  which causes the writer to select a scale to set the stored values of the

  dimensions to range from [0, 2147483647].  [Default: .01]



  Note: written value = (nominal value - offset) / scale.



offset_x, offset_y, offset_z

   Offset to be subtracted from the X, Y and Z nominal values, respectively,

   before the value is scaled.  The special value ``auto`` can be specified,

   which causes the writer to set the offset to the minimum value of the

   dimension.  [Default: 0]



   Note: written value = (nominal value - offset) / scale.



filesource_id

  The file source id number to use for this file (a value between

  0 and 65535 - 0 implies "unassigned") [Default: 0]



discard_high_return_numbers

  If true, discard all points with a return number greater than the maximum

  supported by the point format (5 for formats 0-5, 15 for formats 6-10).

  [Default: false]



extra_dims

  Extra dimensions to be written as part of each point beyond those specified

  by the LAS point format.  The format of the option is

  ``<dimension_name>=<type> [, ...]``.  Any valid PDAL :ref:`type <types>`

  can be specified.



  The special value ``all`` can be used in place of a dimension/type list

  to request that all dimensions that can't be stored in the predefined

  LAS point record get added as extra data at the end of each point record.



  PDAL writes an extra bytes VLR (User ID: LASF_Spec, Record ID: 4) when

  extra dims are written.  The VLR describes the extra dimensions specified by

  this option.  Note that reading of this VLR is only specified for LAS

  version 1.4, though some systems will honor it for earlier file formats.

  The :ref:`LAS reader <readers.las>` requires the option

  use_eb_vlr in order to

  read the extra bytes VLR for files written with 1.1 - 1.3 LAS format.



  Setting --verbose=Info will provide output on the names, types and order

  of dimensions being written as part of the LAS extra bytes.



pdal_metadata

  Write two VLRs containing `JSON`_ output with both the :ref:`metadata` and

  :ref:`pipeline` serialization. [Default: false]



vlrs

    Add VLRS specified as json. See `VLRs`_ above for details.



.. include:: writer_opts.rst



.. _`JSON`: http://www.json.org/

.. _LAS format: http://asprs.org/Committee-General/LASer-LAS-File-Format-Exchange-Activities.html


    """

    vars = dict()
    vars['type'] = 'writers.las'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def matlab(filename=None, output_dims=None, struct=None, inputs=None, tag=None, **kwargs):
    """.. _writers.matlab:



writers.matlab

==============



The **Matlab Writer** supports writing Matlab `.mat` files.



The produced files has a single variable, `PDAL`, an array struct.



.. image:: ./writers.matlab.png



.. note::



    The Matlab writer requires the Mat-File API from MathWorks, and

    it must be explicitly enabled at compile time with the

    ``BUILD_PLUGIN_MATLAB=ON`` variable



.. plugin::



Example

-------



.. code-block:: json



  [

      {

          "type":"readers.las",

          "filename":"inputfile.las"

      },

      {

          "type":"writers.matlab",

          "output_dims":"X,Y,Z,Intensity",

          "filename":"outputfile.mat"

      }

  ]



Options

-------



filename

  Output file name [Required]



output_dims

  A comma-separated list of dimensions to include in the output file.

  May also be specified as an array of strings. [Default: all available

  dimensions]



struct

  Array structure name to read [Default: "PDAL"]



.. include:: writer_opts.rst


    """

    vars = dict()
    vars['type'] = 'writers.matlab'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def nitf(filename=None, clevel=None, stype=None, ostaid=None, ftitle=None, fsclas=None, oname=None, ophone=None, fsctlh=None, fsclsy=None, idatim=None, iid2=None, fscltx=None, aimidb=None, acftb=None, inputs=None, tag=None, **kwargs):
    """.. _writers.nitf:



writers.nitf

============



The `NITF`_ format is a US Department of Defense format for the transmission

of imagery.  It supports various formats inside a generic wrapper.



.. note::



    LAS inside of NITF is widely supported by software that uses NITF

    for point cloud storage, and LAZ is supported by some softwares.

    No other content type beyond those two is widely supported as

    of January of 2016.



.. embed::



.. streamable::



Example

-------



**Example One**



.. code-block:: json



  [

      {

          "type":"readers.las",

          "filename":"inputfile.las"

      },

      {

          "type":"writers.nitf",

          "compression":"laszip",

          "idatim":"20160102220000",

          "forward":"all",

          "acftb":"SENSOR_ID:LIDAR,SENSOR_ID_TYPE:LILN",

          "filename":"outputfile.ntf"

      }

  ]





**Example Two**



.. code-block:: json



  [

      {

          "type":"readers.las",

          "filename":"inputfile.las"

      },

      {

          "type":"writers.nitf",

          "compression":"laszip",

          "idatim":"20160102220000",

          "forward":"all",

          "acftb":"SENSOR_ID:LIDAR,SENSOR_ID_TYPE:LILN",

          "aimidb":"ACQUISITION_DATE:20160102235900",

          "filename":"outputfile.ntf"

      }

  ]



Options

-------



filename

  NITF file to write.  The writer will accept a filename containing

  a single placeholder character ('#').  If input to the writer consists

  of multiple PointViews, each will be written to a separate file, where

  the placeholder will be replaced with an incrementing integer.  If no

  placeholder is found, all PointViews provided to the writer are

  aggregated into a single file for output.  Multiple PointViews are usually

  the result of using :ref:`filters.splitter`, :ref:`filters.chipper` or

  :ref:`filters.divider`.



clevel

  File complexity level (2 characters) [Default: **03**]



stype

  Standard type (4 characters) [Default: **BF01**]



ostaid

  Originating station ID (10 characters) [Default: **PDAL**]



ftitle

  File title (80 characters) [Default: <spaces>]



fsclas

  File security classification ('T', 'S', 'C', 'R' or 'U') [Default: **U**]



oname

  Originator name (24 characters) [Default: <spaces>]



ophone

  Originator phone (18 characters) [Default: <spaces>]



fsctlh

  File control and handling (2 characters) [Default: <spaces>]



fsclsy

  File classification system (2 characters) [Default: <spaces>]



idatim

  Image date and time (format: 'CCYYMMDDhhmmss'). Required.

  [Default: AIMIDB.ACQUISITION_DATE if set or <spaces>]



iid2

  Image identifier 2 (80 characters) [Default: <spaces>]



fscltx

  File classification text (43 characters) [Default: <spaces>]



aimidb

  Comma separated list of name/value pairs to complete the AIMIDB

  (Additional Image ID) TRE record (format name:value).

  Required: ACQUISITION_DATE, will default to IDATIM value.

  [Default: NITF defaults]



acftb

  Comma separated list of name/value pairs to complete the ACFTB

  (Aircraft Information) TRE record (format name:value). Required:

  SENSOR_ID, SENSOR_ID_TYPE [Default: NITF defaults]



.. include:: writer_opts.rst



.. _NITF: http://en.wikipedia.org/wiki/National_Imagery_Transmission_Format
    """

    vars = dict()
    vars['type'] = 'writers.nitf'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def null(inputs=None, tag=None, **kwargs):
    """.. _writers.null:



writers.null

============



The **null writer** discards its input.  No point output is produced when using

a null writer.



.. embed::



.. streamable::



Example

-------



.. code-block:: json



  [

      {

          "type":"readers.las",

          "filename":"inputfile.las"

      },

      {

          "type":"filters.hexbin"

      },

      {

          "type":"writers.null"

      }

  ]



When used with an option that forces metadata output, like

--pipeline-serialization, this pipeline will create a hex boundary for

the input file, but no output point data file will be produced.



Options

-------



The null writer discards all passed options.


    """

    vars = dict()
    vars['type'] = 'writers.null'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def ogr(multicount=None, measure_dim=None, ogrdriver=None, inputs=None, tag=None, **kwargs):
    """.. _writers.ogr:



writers.ogr

===========



The **OGR Writer** will create files of various `vector formats`_ as supported

by the OGR library.  PDAL points are generally stored as points in the

output format, though PDAL will create multipoint objects instead of point

objects if the 'multicount' argument is set to a value greater than 1.

Points can be written with a single additional value in addition to location

if 'measure_dim' specifies a valid PDAL dimension and the output format

supports measure point types.



By default, the OGR writer will create ESRI shapefiles.  The particular OGR

driver can be specified with the 'ogrdriver' option.



Example

-------



.. code-block:: json



  [

      "inputfile.las",

      {

          "type": "writers.ogr",

          "filename": "outfile.geojson",

          "measure_dim": "Compression"

      }

  ]



Options

-------



_`filename`

  Output file to write.  The writer will accept a filename containing

  a single placeholder character (`#`).  If input to the writer consists

  of multiple PointViews, each will be written to a separate file, where

  the placeholder will be replaced with an incrementing integer.  If no

  placeholder is found, all PointViews provided to the writer are

  aggregated into a single file for output.  Multiple PointViews are usually

  the result of multiple input files, or using :ref:`filters.splitter`,

  :ref:`filters.chipper` or :ref:`filters.divider`.



  The driver will use the OGR GEOjson driver if the output filename

  extension is 'geojson', and the ESRI shapefile driver if the output

  filename extension is 'shp'.

  If neither extension is recognized, the filename is taken

  to represent a directory in which ESRI shapefiles are written.  The

  driver can be explicitly specified by using the 'ogrdriver' option.



multicount

  If 1, point objects will be written.  If greater than 1, specifies the

  number of points to group into a multipoint object.  Not all OGR

  drivers support multipoint objects. [Default: 1]



measure_dim

  If specified, points will be written with an extra data field, the dimension

  of which is specified by this option. Not all output formats support

  measure data. [Default: None]



  .. note::



    The **measure_dim** option is only supported if PDAL is built with

    GDAL version 2.1 or later.



ogrdriver

  The OGR driver to use for output.  This option overrides any inference made

  about output drivers from filename_.



.. include:: writer_opts.rst



.. _vector formats: http://www.gdal.org/ogr_formats.html


    """

    vars = dict()
    vars['type'] = 'writers.ogr'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def pcd(filename=None, compression=None, keep_unspecified=None, inputs=None, tag=None, **kwargs):
    """.. _writers.pcd:



writers.pcd

===========



The **PCD Writer** supports writing to `Point Cloud Data (PCD)`_ formatted

files, which are used by the `Point Cloud Library (PCL)`_.



By default, compression is not enabled, and the PCD writer will output ASCII

formatted data.



.. embed::



.. streamable::



.. note::



    X, Y, and Z dimensions will be written as single-precision floats by

    default to be compatible with most of the existing PCL point types. These

    dimensions can be forced to double-precision using the `order` option, but

    the PCL code reading this data must be capable of reading double-precision

    fields (i.e., it is not the responsibility of PDAL to ensure this

    compatibility).



.. note::



    When working with large coordinate values it is recommended that users

    first translate the coordinate values using :ref:`filters.transformation`

    to avoid loss of precision when writing single-precision XYZ data.





Example

-------



.. code-block:: json



  [

      {

          "type":"readers.pcd",

          "filename":"inputfile.pcd"

      },

      {

          "type":"writers.pcd",

          "filename":"outputfile.pcd"

      }

  ]



Options

-------



filename

  PCD file to write [Required]



compression

  Level of PCD compression to use (ascii, binary, compressed) [Default:

  "ascii"]



_`precision`

  Decimal Precision for output of values. This can be overridden for individual

  dimensions using the order option. [Default: 2]



_`order`

  Comma-separated list of dimension names in the desired output order. For

  example "X,Y,Z,Red,Green,Blue". Dimension names can optionally be followed

  by a PDAL type (e.g., Unsigned32) and dimension-specific precision (used only

  with "ascii" compression).  Ex: "X=Float:2, Y=Float:2, Z=Float:3,

  Intensity=Unsigned32" If no precision is specified the value provided with

  the precision_ option is used.  The default dimension type is double

  precision float. [Default: none]



keep_unspecified

  If true, writes all dimensions. Dimensions specified with the order_ option

  precede those not specified. [Default: **true**]



.. include:: writer_opts.rst



.. _Point Cloud Data (PCD): https://pcl-tutorials.readthedocs.io/en/latest/pcd_file_format.html

.. _Point Cloud Library (PCL): http://pointclouds.org


    """

    vars = dict()
    vars['type'] = 'writers.pcd'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def pgpointcloud(connection=None, table=None, schema=None, column=None, compression=None, overwrite=None, srid=None, pcid=None, pre_sql=None, post_sql=None, output_dims=None, inputs=None, tag=None, **kwargs):
    """.. _writers.pgpointcloud:



writers.pgpointcloud

====================



The **PostgreSQL Pointcloud Writer** allows you to write to PostgreSQL database

that have the `PostgreSQL Pointcloud`_ extension enabled. The Pointcloud

extension stores point cloud data in tables that contain rows of patches. Each

patch in turn contains a large number of spatially nearby points.



While you can theoretically store the contents of a whole file of points in a

single patch, it is more practical to store a table full of smaller patches,

where the patches are under the PostgreSQL page size (8kb). For most LIDAR

data, this practically means a patch size of between 400 and 600 points.



In order to create patches of the right size, the Pointcloud writer should be

preceded in the pipeline file by :ref:`filters.chipper`.



The pgpointcloud format does not support WKT spatial reference specifications.  A subset of spatial references can be stored by using the 'srid' option, which

allows storage of an `EPSG code`_ that covers many common spatial references.

PDAL makes no attempt to reproject data to your specified srid.  Use

:ref:`filters.reprojection` for this purpose.



.. plugin::



Example

-------





.. code-block:: json



  [

      {

          "type":"readers.las",

          "filename":"inputfile.las",

          "spatialreference":"EPSG:26916"

      },

      {

          "type":"filters.chipper",

          "capacity":400

      },

      {

          "type":"writers.pgpointcloud",

          "connection":"host='localhost' dbname='lidar' user='pramsey'",

          "table":"example",

          "compression":"dimensional",

          "srid":"26916"

      }

  ]



Options

-------



connection

  PostgreSQL connection string. In the form *"host=hostname dbname=database user=username password=pw port=5432"* [Required]



table

  Database table to write to. [Required]



schema

  Database schema to write to. [Default: "public"]



column

  Table column to put patches into. [Default: "pa"]



compression

  Patch compression type to use. [Default: ""dimensional""]



  * **none** applies no compression

  * **dimensional** applies dynamic compression to each dimension separately

  * **lazperf** applies a "laz" compression (using the `laz-perf`_ library in PostgreSQL Pointcloud)



overwrite

  To drop the table before writing set to 'true'. To append to the table

  set to 'false'. [Default: false]



srid

  Spatial reference ID (relative to the `spatial_ref_sys` table in PostGIS)

  to store with the point cloud schema. [Default: 4326]



pcid

  An optional existing PCID to use for the point cloud schema. If specified,

  the schema must be present. If not specified, a match will still be

  looked for, or a new schema will be inserted. [Default: 0]



pre_sql

  SQL to execute *before* running the translation. If the value

  references a file, the file is read and any SQL inside is executed.

  Otherwise the value is executed as SQL itself. [Optional]



post_sql

  SQL to execute *after* running the translation. If the value references

  a file, the file is read and any SQL inside is executed. Otherwise the

  value is executed as SQL itself. [Optional]



scale_x, scale_y, scale_z / offset_x, offset_y, offset_z

  If ANY of these options are specified the X, Y and Z dimensions are adjusted

  by subtracting the offset and then dividing the values by the specified

  scaling factor before being written as 32-bit integers (as opposed to double

  precision values).  If any of these options is specified, unspecified

  scale_<x,y,x> options are given the value of 1.0 and unspecified

  offset_<x,y,z> are given the value of 0.0.



output_dims

  If specified, limits the dimensions written for each point.  Dimensions

  are listed by name and separated by commas.



.. include:: writer_opts.rst



.. _PostgreSQL Pointcloud: http://github.com/pramsey/pointcloud

.. _laz-perf: https://github.com/hobu/laz-perf

.. _EPSG code: http://www.epsg.org
    """

    vars = dict()
    vars['type'] = 'writers.pgpointcloud'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def ply(filename=None, storage_mode=None, dims=None, faces=None, sized_types=None, precision=None, inputs=None, tag=None, **kwargs):
    """.. _writers.ply:



writers.ply

===========



The **ply writer** writes the `polygon file format`_, a common file format

for storing three dimensional models.  The writer emits points as PLY vertices.

The writer can also emit a mesh as a set of faces.

:ref:`filters.greedyprojection` and :ref:`filters.poisson` create a

mesh suitable for output as faces.



.. embed::



Example

-------





.. code-block:: json



  [

      {

          "type":"readers.pcd",

          "filename":"inputfile.pcd"

      },

      {

          "type":"writers.ply",

          "storage_mode":"little endian",

          "filename":"outputfile.ply"

      }

  ]





Options

-------



filename

  ply file to write [Required]



storage_mode

  Type of ply file to write. Valid values are 'ascii', 'little endian',

  'big endian'.  [Default: "ascii"]



dims

  List of dimensions (and :ref:`types`) in the format

  ``<dimension_name>[=<type>] [,...]`` to write as output.

  (e.g., "Y=int32_t, X,Red=char")

  [Default: All dimensions with stored types]



faces

  Write a mesh as faces in addition to writing points as vertices.

  [Default: false]



sized_types

  PLY has variously been written with explicitly sized type strings

  ('int8', 'float32", 'uint32', etc.) and implied sized type strings

  ('char', 'float', 'int', etc.).  If true, explicitly sized type strings

  are used.  If false, implicitly sized type strings are used.

  [Default: true]



precision

  If specified, the number of digits to the right of the decimal place

  using f-style formatting.  Only permitted when 'storage_mode' is 'ascii'.

  See the `printf`_ reference for more information.

  [Default: g-style formatting (variable precision)]



.. include:: writer_opts.rst



.. _polygon file format: http://paulbourke.net/dataformats/ply/

.. _printf: https://en.cppreference.com/w/cpp/io/c/fprintf
    """

    vars = dict()
    vars['type'] = 'writers.ply'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def raster(filename=None, gdaldriver=None, gdalopts=None, rasters=None, data_type=None, nodata=None, inputs=None, tag=None, **kwargs):
    """.. _writers.raster:



writers.raster

================================================================================



The **Raster Writer** writes an existing raster to a file.

Output is produced using `GDAL`_ and can use any `driver

that supports creation of rasters`_.  A data_type_ can be specified for the

raster (double, float, int32, etc.).  If no data type is specified, the

data type with the largest range supported by the driver is used.



.. _`GDAL`: http://gdal.org

.. _`driver that supports creation of rasters`: http://www.gdal.org/formats_list.html



Cells that have no value are given a value specified by the nodata_ option.



.. embed::



.. streamable::





Basic Example

--------------------------------------------------------------------------------



This  pipeline reads the file autzen_trim.las, triangulates the data, creates a raster

based on the `Z` dimension as determined by interpolation of the location and values

of 'Z' of the vertices of a containing triangle, if any exists.  The resulting raster

is written to "outputfile.tif".



.. code-block:: json



  [

      "pdal/test/data/las/autzen_trim.las",

      {

          "type": "filters.delaunay"

      }

      {

          "type": "filters.faceraster",

          "resolution": 1

      }

      {

          "type": "writers.raster"

          "filename":"outputfile.tif"

      }

  ]





Options

--------------------------------------------------------------------------------



filename

    Name of output file. [Required]



.. _resolution:



gdaldriver

    GDAL code of the `GDAL driver`_ to use to write the output.

    [Default: "GTiff"]



.. _`GDAL driver`: http://www.gdal.org/formats_list.html



gdalopts

    A list of key/value options to pass directly to the GDAL driver.  The

    format is name=value,name=value,...  The option may be specified

    any number of times.



    .. note::

        The INTERLEAVE GDAL driver option is not supported.  writers.gdal

        always uses BAND interleaving.



rasters

    A comma-separated list of raster names to be written as bands of the raster.

    All rasters must have the same limits (origin/width/height). Rasters following the first

    that don't have the same limits will be dropped. If no raster names are provided,

    only the first raster found will be placed into a single band for output.



.. _data_type:



data_type

    The :ref:`data type <types>` to use for the output raster.  Many GDAL drivers only

    support a limited set of output data types.  [Default: depends on the driver]



.. _nodata:



nodata

    The value to use for a raster cell if the raster contains no data in a cell.

    Note that the nodata written to the output may be different from that of the

    raster being written.

    [Default: depends on the data_type_.  -9999 for double, float, int and short, 9999 for

    unsigned int and unsigned short, 255 for unsigned char and -128 for char]



.. include:: writer_opts.rst
    """

    vars = dict()
    vars['type'] = 'writers.raster'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def sbet(filename=None, angles_are_degrees=None, inputs=None, tag=None, **kwargs):
    """.. _writers.sbet:



writers.sbet

============



The **SBET writer** writes files in the SBET format, used for exchange data from inertial measurement units (IMUs).



.. embed::



Example

-------



.. code-block:: json



  [

      "input.sbet",

      "output.sbet"

  ]





Options

-------



filename

  File to write. [Required]



angles_are_degrees

  Convert all angular values from degrees to radians before write.

  [Default: true]



.. include:: writer_opts.rst


    """

    vars = dict()
    vars['type'] = 'writers.sbet'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def text(filename=None, format=None, keep_unspecified=None, jscallback=None, quote_header=None, write_header=None, newline=None, delimiter=None, inputs=None, tag=None, **kwargs):
    """.. _writers.text:



writers.text

============



The **text writer** writes out to a text file. This is useful for debugging or

getting smaller files into an easily parseable format.  The text writer

supports both `GeoJSON`_ and `CSV`_ output.





.. embed::



.. streamable::



Example

-------



.. code-block:: json



  [

      {

          "type":"readers.las",

          "filename":"inputfile.las"

      },

      {

          "type":"writers.text",

          "format":"geojson",

          "order":"X,Y,Z",

          "keep_unspecified":"false",

          "filename":"outputfile.txt"

      }

  ]



Options

-------



filename

  File to write to, or "STDOUT" to write to standard out [Required]



format

  Output format to use. One of ``geojson`` or ``csv``. [Default: "csv"]



_`precision`

  Decimal Precision for output of values. This can be overridden for

  individual dimensions using the order option. [Default: 3]



_`order`

  Comma-separated list of dimension names in the desired output order.

  For example "X,Y,Z,Red,Green,Blue". Dimension names

  can optionally be followed with a colon (':') and an integer to indicate the

  precision to use for output. Ex: "X:3, Y:5,Z:0" If no precision is specified

  the value provided with the precision_ option is used. [Default: none]



keep_unspecified

  If true, writes all dimensions.  Dimensions specified with the order_

  option precede those not specified. [Default: **true**]



jscallback

  When producing GeoJSON, the callback allows you to wrap the data in

  a function, so the output can be evaluated in a <script> tag.



quote_header

  When producing CSV, should the column header named by quoted?

  [Default: true]



write_header

  Whether a header should be written. [Default: true]



newline

  When producing CSV, what newline character should be used? (For Windows,

  ``\\r\\n`` is common.) [Default: "\\n"]



delimiter

  When producing CSV, what character to use as a delimiter? [Default: ","]



.. include:: writer_opts.rst



.. _GeoJSON: http://geojson.org

.. _CSV: http://en.wikipedia.org/wiki/Comma-separated_values


    """

    vars = dict()
    vars['type'] = 'writers.text'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def tiledb(array_name=None, config_file=None, data_tile_capacity=None, x_tile_size=None, y_tile_size=None, z_tile_size=None, time_tile_size=None, x_domain_st=None, x_domain_end=None, y_domain_st=None, y_domain_end=None, z_domain_st=None, z_domain_end=None, time_domain_st=None, time_domain_end=None, use_time_dim=None, time_first=None, chunk_size=None, compression=None, compression_level=None, append=None, stats=None, filters=None, timestamp=None, inputs=None, tag=None, **kwargs):
    """.. _writers.tiledb:



writers.tiledb

==============



Implements `TileDB`_ 2.3.0+ reads from an array.



.. plugin::



.. streamable::



Example

-------



.. code-block:: json



  [

      {

          "type":"readers.las",

          "array_name":"input.las"

      },

      {

          "type":"filters.stats"

      },

      {

          "type":"writers.tiledb",

          "array_name":"output_array"

      }

  ]





Options

-------



array_name

  `TileDB`_ array to write to. [Required]



config_file

  `TileDB`_ configuration file [Optional]



data_tile_capacity

  Number of points per tile [Optional]



x_tile_size

  Tile size (x) [Optional]



y_tile_size

  Tile size (y) [Optional]



z_tile_size

  Tile size (z) [Optional]

  

time_tile_size  

  Tile size (time) [Optional]



x_domain_st

  Domain minimum in x [Optional]



x_domain_end

  Domain maximum in x [Optional]



y_domain_st

  Domain minimum in y [Optional]



y_domain_end

  Domain maximum in y [Optional]



z_domain_st

  Domain minimum in z [Optional]



z_domain_end

  Domain maximum in z [Optional]



time_domain_st

  Domain minimum in GpsTime [Optional]



time_domain_end

  Domain maximum in GpsTime [Optional]

  

use_time_dim

  Use GpsTime coordinate data as array dimension [Optional]



time_first

  If writing 4D array with XYZ and Time, choose to put time dim first or last (default) [Optional]

  

chunk_size

  Point cache size for chunked writes [Optional]



compression

  TileDB compression type for attributes, default is None [Optional]



compression_level

  TileDB compression level for chosen compression [Optional]



append

  Append to an existing TileDB array with the same schema [Optional]



stats

  Dump query stats to stdout [Optional]



filters

  JSON array or object of compression filters for either `dims` or `attributes` of the form {dim/attributename : {"compression": name, compression_options: value, ...}} [Optional]



timestamp

  Sets the TileDB timestamp for this write



.. include:: writer_opts.rst



By default TileDB will use the following set of compression filters for coordinates and attributes;



.. code-block:: json



  {

      "X":{"compression": "zstd", "compression_level": 7},

      "Y":{"compression": "zstd", "compression_level": 7},

      "Z":{"compression": "zstd", "compression_level": 7},

      "Intensity":{"compression": "bzip2", "compression_level": 5},

      "ReturnNumber": {"compression": "zstd", "compression_level": 7},

      "NumberOfReturns": {"compression": "zstd", "compression_level": 7},

      "ScanDirectionFlag": {"compression": "bzip2", "compression_level": 5},

      "EdgeOfFlightLine": {"compression": "bzip2", "compression_level": 5},

      "Classification": {"compression": "gzip", "compression_level": 9},

      "ScanAngleRank": {"compression": "bzip2", "compression_level": 5},

      "UserData": {"compression": "gzip", "compression_level": 9},

      "PointSourceId": {"compression": "bzip2"},

      "Red": {"compression": "zstd", "compression_level": 7},

      "Green": {{"compression": "zstd", "compression_level": 7},

      "Blue": {{"compression": "zstd", "compression_level": 7},

      "GpsTime": {"compression": "zstd", "compression_level": 7}

  }



.. _TileDB: https://tiledb.io
    """

    vars = dict()
    vars['type'] = 'writers.tiledb'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars
