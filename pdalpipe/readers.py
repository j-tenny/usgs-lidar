def bpf(filename=None, fix_dims=None, inputs=None, tag=None, **kwargs):
    """.. _readers.bpf:



******************************************************************************

readers.bpf

******************************************************************************



BPF is an NGA `specification <https://nsgreg.nga.mil/doc/view?i=4220&month=8&day=30&year=2016>`_ for point cloud data.  The BPF reader supports

reading from BPF files that are encoded as version 1, 2 or 3.



This BPF reader only supports Zlib compression.  It does NOT support the

deprecated compression types QuickLZ and FastLZ.  The reader will consume files

containing ULEM frame data and polarimetric data, although these data are not

made accessible to PDAL; they are essentially ignored.



Data that follows the standard header but precedes point data is taken to

be metadata and is UTF-encoded and added to the reader's metadata.



.. embed::



.. streamable::



Example

------------------------------------------------------------------------------



.. code-block:: json



    [

        "inputfile.bpf",

        {

          "type":"writers.text",

          "filename":"outputfile.txt"

        }

    ]





Options

------------------------------------------------------------------------------



filename

    BPF file to read [Required]



fix_dims

    BPF files may contain dimension names that aren't allowed by PDAL. When this

    option is 'true', invalid characters in dimension names are replaced by '_' in

    order to make the names valid.

    [Default: true]



.. include:: reader_opts.rst


    """

    vars = dict()
    vars['type'] = 'readers.bpf'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def buffer(inputs=None, tag=None, **kwargs):
    """.. _readers.buffer:



readers.buffer

==============



The :ref:`readers.buffer` stage is a special stage that allows

you to read data from your own PointView rather than

fetching the data from a specific reader. In the :ref:`writing` example,

it is used to take a simple listing of points and turn them into an

LAS file.



.. embed::



Example

-------



See :ref:`writing` for an example usage scenario for :ref:`readers.buffer`.



Options

-------



.. include:: reader_opts.rst
    """

    vars = dict()
    vars['type'] = 'readers.buffer'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def copc(bounds=None, polygon=None, ogr=None, requests=None, resolution=None, header=None, query=None, las=None, fix_dims=None, inputs=None, tag=None, **kwargs):
    """.. _readers.copc:



readers.copc

============



The **COPC Reader** supports reading from `COPC format`_ files. A COPC file is

a `LASzip`_ (compressed LAS) file that organizes its data spatially, allowing for

incremental loading and spatial filtering.



.. _LASzip: http://laszip.org

.. _COPC format: https://copc.io/



.. note::



  LAS stores X, Y and Z dimensions as scaled integers.  Users converting an

  input LAS file to an output LAS file will frequently want to use the same

  scale factors and offsets in the output file as existed in the input

  file in order to

  maintain the precision of the data.  Use the `forward` option of 

  :ref:`writers.las` to facilitate transfer of header information from

  source COPC files to destination LAS/LAZ files.



.. note::



  COPC files can contain datatypes that are actually arrays rather than

  individual dimensions.  Since PDAL doesn't support these datatypes, it

  must map them into datatypes it supports.  This is done by appending the

  array index to the name of the datatype.  For example, datatypes 11 - 20

  are two dimensional array types and if a field had the name Foo for

  datatype 11, PDAL would create the dimensions Foo0 and Foo1 to hold the

  values associated with LAS field Foo.  Similarly, datatypes 21 - 30 are

  three dimensional arrays and a field of type 21 with the name Bar would

  cause PDAL to create dimensions Bar0, Bar1 and Bar2.  See the information

  on the extra bytes VLR in the `LAS Specification`_ for more information

  on the extra bytes VLR and array datatypes.



.. _LAS Specification: http://www.asprs.org/wp-content/uploads/2019/07/LAS_1_4_r15.pdf



.. warning::



  COPC files that use the extra bytes VLR and datatype 0 will be accepted,

  but the data associated with a dimension of datatype 0 will be ignored

  (no PDAL dimension will be created).



.. embed::



.. streamable::





Example

-------



.. code-block:: json



  [

      {

          "type":"readers.copc",

          "filename":"inputfile.copc.laz"

      },

      {

          "type":"writers.text",

          "filename":"outputfile.txt"

      }

  ]



Options

-------



_`filename`

  COPC file to read. Remote file specifications (http, AWS, Google, Azure, Dropbox) are supported.

  [Required]



.. include:: reader_opts.rst



bounds

  The extent of the data to select in 2 or 3 dimensions, expressed as a string,

  e.g.: ``([xmin, xmax], [ymin, ymax], [zmin, zmax])``.  If omitted, the entire dataset

  will be selected. The bounds specification can be followed by a slash ('/') and a

  spatial reference specification to apply to the bounds specification.



polygon

  A clipping polygon, expressed in a well-known text string,

  e.g.: ``POLYGON((0 0, 5000 10000, 10000 0, 0 0))``.  This option can be

  specified more than once. Multiple polygons will will be treated

  as a single multipolygon. The polygon specification can be followed by a slash ('/') and a

  spatial reference specification to apply to the polygon.



ogr

  A JSON object representing an OGR query to fetch polygons to use for filtering. The polygons

  fetched from the query are treated exactly like those specified in the ``polygon`` option.

  The JSON object is specified as follows:



  .. code-block:: json



    {

        "drivers": "OGR drivers to use",

        "openoptions": "Options to pass to the OGR open function [optional]",

        "layer": "OGR layer from which to fetch polygons [optional]",

        "sql": "SQL query to use to filter the polygons in the layer [optional]",

        "options":

        {

            "geometry", "WKT or GeoJSON geomtry used to filter query [optional]"

        }

    }



requests

  The number of worker threads processing data. The optimal number depends on your system

  and your network connection, but more is not necessarily better.  A reasonably fast

  network connection can often fetch data faster than it can be processed, leading to

  memory consumption and slower performance. [Default: 15]



resolution

  Limit the pyramid levels of data to fetch based on the expected resolution of the data.

  Units match that of the data. [Default: no resolution limit]



header

  HTTP headers to forward for remote endpoints. Specify as a JSON

  object of key/value string pairs.



query

  HTTP query parameters to forward for remote endpoints. Specify as a JSON

  object of key/value string pairs.



las

  Read LAS VLRs and import as metadata. [Default: false]

   

fix_dims

  Make invalid dimension names valid by converting disallowed characters to '_'. Only

  applies to names specified in an extra-bytes VLR. [Default: true]
    """

    vars = dict()
    vars['type'] = 'readers.copc'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def draco(filename=None, inputs=None, tag=None, **kwargs):
    """.. _readers.draco:



readers.draco

=============



`Draco`_ is a library for compressing and decompressing 3D geometric meshes and

point clouds and was designed and built for compression efficiency and speed.

The code supports compressing points, connectivity information, texture coordinates,

color information, normals, and any other generic attributes associated with geometry.



Example

--------------------------------------------------------------------------------



.. code-block:: json



    [

        {

            "type": "readers.draco",

            "filename": "color.las"

        }

    ]



Options

-------



filename

    Input file name. [Required]



.. include:: reader_opts.rst



.. _Draco: https://github.com/google/draco
    """

    vars = dict()
    vars['type'] = 'readers.draco'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def e57(inputs=None, tag=None, **kwargs):
    """.. _readers.e57:



readers.e57

===========



The **E57 Reader** supports reading from E57 files.



The reader supports E57 files with Cartesian point clouds.



.. note::



   E57 files can contain multiple point clouds stored in a single

   file.  If that is the case, the reader will read all the points

   from all of the internal point clouds as one.



   Only dimensions present in all of the point clouds will be read.



.. note::



   Point clouds stored in spherical format are not supported.



.. note::



   The E57 `cartesianInvalidState` dimension is mapped to the Omit

   PDAL dimension.  A range filter can be used to filter out the

   invalid points.

   

.. plugin::



.. streamable::





Example 1

---------



.. code-block:: json



  [

      {

          "type":"readers.e57",

          "filename":"inputfile.e57"

      },

      {

          "type":"writers.text",

          "filename":"outputfile.txt"

      }

  ]





Example 2

---------

  

.. code-block:: json



  [

      {

          "type":"readers.e57",

          "filename":"inputfile.e57"

      },

      {

          "type":"filters.range",

          "limits":"Omit[0:0]"

      },

      {

          "type":"writers.text",

          "filename":"outputfile.txt"

      }

  ]



  

Options

-------



_`filename`

  E57 file to read [Required]



.. include:: reader_opts.rst
    """

    vars = dict()
    vars['type'] = 'readers.e57'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def ept(filename=None, spatialreference=None, bounds=None, resolution=None, addons=None, origin=None, polygon=None, ogr=None, requests=None, header=None, query=None, inputs=None, tag=None, **kwargs):
    """.. _readers.ept:



readers.ept

===========



`Entwine Point Tile`_ (EPT) is a hierarchical octree-based point cloud format

suitable for real-time rendering and lossless archival.  `Entwine`_ is a

producer of this format.  The EPT Reader supports reading data from the

EPT format, including spatially accelerated queries and file reconstruction

queries.



Sample EPT datasets of hundreds of billions of points in size may be viewed

with `Potree`_.



.. embed::



.. streamable::



Example

--------------------------------------------------------------------------------



This example downloads a small area around the the Statue of Liberty from the New York City data set (4.7 billion points) which can be viewed in its entirety in `Potree`_.



.. code-block:: json



   [

      {

         "type": "readers.ept",

         "filename": "http://na.entwine.io/nyc/ept.json",

         "bounds": "([-8242669, -8242529], [4966549, 4966674])"

      },

      "statue-of-liberty.las"

   ]



Additional attributes created by the

:ref:`EPT addon writer <writers.ept_addon>` can be referenced with the ``addon`` option.  Here is an example that overrides the ``Classification`` dimension with an addon dimension derived from the original dataset:



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



For more details about addon dimensions and how to produce them, see :ref:`writers.ept_addon`.



Options

--------------------------------------------------------------------------------



filename

    Path to the EPT resource from which to read, ending with ``ept.json``.

    For example, ``/Users/connor/entwine/autzen/ept.json`` or

    ``http://na.entwine.io/autzen/ept.json``. [Required]



spatialreference

    Spatial reference to apply to the data.  Overrides any SRS in the input

    itself.  Can be specified as a WKT, proj.4 or EPSG string. [Default: none]



bounds

    The extents of the resource to select in 2 or 3 dimensions, expressed as a string,

    e.g.: ``([xmin, xmax], [ymin, ymax], [zmin, zmax])``.  If omitted, the entire dataset

    will be selected. The bounds can be followed by a slash ('/') and a spatial reference

    specification to apply to the bounds.



resolution

    A point resolution limit to select, expressed as a grid cell edge length.  Units

    correspond to resource coordinate system units.  For example, for a coordinate system

    expressed in meters, a ``resolution`` value of ``0.1`` will select points up to a

    ground resolution of 100 points per square meter.



    The resulting resolution may not be exactly this value: the minimum possible resolution

    that is at *least* as precise as the requested resolution will be selected.  Therefore

    the result may be a bit more precise than requested.



addons

    A mapping of assignments of the form ``DimensionName: AddonPath``, which

    assigns dimensions from the specified paths to the named dimensions.

    These addon dimensions are created by the

    :ref:`EPT addon writer <writers.ept_addon>`.  If the dimension names

    already exist in the EPT `Schema`_ for the given resource, then their

    values will be overwritten with those from the appropriate addon.



    Addons may used to override well-known :ref:`dimension <dimensions>`.  For example,

    an addon assignment of ``"Classification": "~/addons/autzen/MyGroundDimension/"``

    will override an existing EPT ``Classification`` dimension with the custom dimension.



origin

    EPT datasets are lossless aggregations of potentially multiple source

    files.  The *origin* option can be used to select all points from a

    single source file.  This option may be specified as a string or an

    integral ID.



    The string form of this option selects a source file by its original

    file path.  This may be a substring instead of the entire path, but

    the string must uniquely select only one source file (via substring

    search).  For example, for an EPT dataset created from source files

    *one.las*, *two.las*, and *two.bpf*, "one" is a sufficient selector,

    but "two" is not.



    The integral form of this option selects a source file by its ``OriginId``

    dimension, which can be determined from  the file's position in EPT

    metadata file ``entwine-files.json``.



.. note::



    When using ``pdal info --summary``, using the ``origin`` option will cause the

    resulting bounds to be clipped to those of the selected origin, and the resulting

    number of points to be an upper bound for this selection.



polygon

  The clipping polygon, expressed in a well-known text string,

  e.g.: ``POLYGON((0 0, 5000 10000, 10000 0, 0 0))``.  This option can be

  specified more than once by placing values in an array, in which case all of

  them will be unioned together, acting as a single multipolygon. The polygon definition

  can be followed by a slash ('/') and a spatial reference specification to apply to

  the polygon.



.. note::



    When using ``pdal info --summary``, using the ``polygon`` option will cause the

    resulting bounds to be clipped to the maximal extents of all provided polygons,

    and the resulting number of points to be an upper bound for this polygon selection.



.. note::



    When both the ``bounds`` and ``polygon`` options are specified, only

    the points that fall within *both* the bounds and the polygon(s) will be

    returned.



ogr

  A JSON object representing an OGR query to fetch polygons to use for filtering. The polygons

  fetched from the query are treated exactly like those specified in the ``polygon`` option.

  The JSON object is specified as follows:



  .. code-block:: json



    {

        "drivers": "OGR drivers to use",

        "openoptions": "Options to pass to the OGR open function [optional]",

        "layer": "OGR layer from which to fetch polygons [optional]",

        "sql": "SQL query to use to filter the polygons in the layer [optional]",

        "options":

        {

            "geometry", "WKT or GeoJSON geomtry used to filter query [optional]"

        }

    }



requests

    Maximum number of simultaneous requests for EPT data. [Minimum: 4] [Default: 15]



.. _Entwine Point Tile: https://entwine.io/entwine-point-tile.html

.. _Entwine: https://entwine.io/

.. _Potree: http://potree.entwine.io/data/nyc.html

.. _Schema: https://entwine.io/entwine-point-tile.html#schema



header

    HTTP headers to forward for remote EPT endpoints, specified as a JSON

    object of key/value string pairs.



query

    HTTP query parameters to forward for remote EPT endpoints, specified as a

    JSON object of key/value string pairs.
    """

    vars = dict()
    vars['type'] = 'readers.ept'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def faux(bounds=None, count=None, override_srs=None, mode=None, inputs=None, tag=None, **kwargs):
    """.. _readers.faux:



readers.faux

============



The faux reader is used for testing pipelines. It does not read from a

file or database, but generates synthetic data to feed into the pipeline.



The faux reader requires a mode argument to define the method in which points

should be generated.  Valid modes are as follows:



constant

    The values provided as the minimums to the bounds argument are

    used for the X, Y and Z value, respectively, for every point.

random

    Random values are chosen within the provided bounds.

ramp

    Value increase uniformly from the minimum values to the maximum values.

uniform

    Random values of each dimension are uniformly distributed in the

    provided ranges.

normal

    Random values of each dimension are normally distributed in the

    provided ranges.

grid

    Creates points with integer-valued coordinates in the range provided

    (excluding the upper bound).



.. embed::



.. streamable::



Example

-------



.. code-block:: json



  [

      {

          "type":"readers.faux",

          "bounds":"([0,1000000],[0,1000000],[0,100])",

          "count":"10000",

          "mode":"random"

      },

      {

          "type":"writers.text",

          "filename":"outputfile.txt"

      }

  ]





Options

-------



bounds

  The spatial extent within which points should be generated.

  Specified as a string in the form "([xmin,xmax],[ymin,ymax],[zmin,zmax])".

  [Default: unit cube]



count

  The number of points to generate. [Required, except when mode is 'grid']



override_srs

  Spatial reference to apply to data. [Optional]



mean_x|y|z

  Mean value in the x, y, or z dimension respectively. (Normal mode only)

  [Default: 0]



stdev_x|y|z

  Standard deviation in the x, y, or z dimension respectively. (Normal mode

  only) [Default: 1]



mode

  "constant", "random", "ramp", "uniform", "normal" or "grid" [Required]


    """

    vars = dict()
    vars['type'] = 'readers.faux'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def gdal(filename=None, header=None, inputs=None, tag=None, **kwargs):
    """.. _readers.gdal:



readers.gdal

================================================================================



The `GDAL`_ reader reads `GDAL readable raster`_ data sources as point clouds.



.. _`GDAL`: http://gdal.org

.. _`GDAL readable raster`: http://www.gdal.org/formats_list.html



Each pixel is given an X and Y coordinate (and corresponding PDAL dimensions)

that are center pixel, and each band is represented by "band-1", "band-2", or

"band-n".  Using the 'header' option allows naming the band data to standard

PDAL dimensions.



.. embed::



Basic Example

--------------------------------------------------------------------------------



Simply writing every pixel of a JPEG to a text file is not very useful.



.. code-block:: json



  [

      {

          "type":"readers.gdal",

          "filename":"./pdal/test/data/autzen/autzen.jpg"

      },

      {

          "type":"writers.text",

          "filename":"outputfile.txt"

      }

  ]





LAS Example

--------------------------------------------------------------------------------



The following example assigns the bands from a JPG to the

RGB values of an `ASPRS LAS`_ file using :ref:`writers.las`.



.. _`ASPRS LAS`: http://www.asprs.org/Committee-General/LASer-LAS-File-Format-Exchange-Activities.html



.. code-block:: json



  [

      {

          "type":"readers.gdal",

          "filename":"./pdal/test/data/autzen/autzen.jpg",

          "header": "Red, Green, Blue"

      },

      {

          "type":"writers.las",

          "filename":"outputfile.las"

      }

  ]





Options

--------------------------------------------------------------------------------



filename

  `GDALOpen`_ 'able raster file to read [Required]



.. _`GDALOpen`: https://gdal.org/api/raster_c_api.html#gdal_8h_1aca05455472359964151f9c891d678d5e



.. include:: reader_opts.rst



header

    A comma-separated list of :ref:`dimension <dimensions>` IDs to map

    bands to. The length of the list must match the number

    of bands in the raster.
    """

    vars = dict()
    vars['type'] = 'readers.gdal'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def hdf(dimensions=None, inputs=None, tag=None, **kwargs):
    """.. _readers.hdf:



readers.hdf

===============



The **HDF reader** reads data from files in the

`HDF5 format. <https://www.hdfgroup.org/solutions/hdf5/>`_

You must explicitly specify a mapping of HDF datasets to PDAL

dimensions using the dimensions parameter. ALL dimensions must

be scalars and be of the same length. Compound types are not

supported at this time.





.. plugin::



.. streamable::



Example

-------

This example reads from the Autzen HDF example with all dimension

properly mapped and then outputs a LAS file.



.. code-block:: json



    [

        {

            "type": "readers.hdf",

            "filename": "test/data/hdf/autzen.h5",

            "dimensions":

            {

                "X" : "autzen/X",

                "Y" : "autzen/Y",

                "Z" : "autzen/Z",

                "Red" : "autzen/Red",

                "Blue" : "autzen/Blue",

                "Green" : "autzen/Green",

                "Classification" : "autzen/Classification",

                "EdgeOfFlightLine" : "autzen/EdgeOfFlightLine",

                "GpsTime" : "autzen/GpsTime",

                "Intensity" : "autzen/Intensity",

                "NumberOfReturns" : "autzen/NumberOfReturns",

                "PointSourceId" : "autzen/PointSourceId",

                "ReturnNumber" : "autzen/ReturnNumber",

                "ScanAngleRank" : "autzen/ScanAngleRank",

                "ScanDirectionFlag" : "autzen/ScanDirectionFlag",

                "UserData" : "autzen/UserData"

            }

        },

        {

            "type" : "writers.las",

            "filename": "output.las",

            "scale_x": 1.0e-5,

            "scale_y": 1.0e-5,

            "scale_z": 1.0e-5,

            "offset_x": "auto",

            "offset_y": "auto",

            "offset_z": "auto"

        }

    ]





.. note::

    All dimensions must be simple numeric HDF datasets with

    equal lengths. Compound types, enum types, string types,

    etc. are not supported.





.. warning::

    The HDF reader does not set an SRS.





Common Use Cases

----------------



A possible use case for this driver is reading NASA's `ICESat-2 <https://icesat-2.gsfc.nasa.gov/>`__ data.

This example reads the X, Y, and Z coordinates from the ICESat-2

`ATL03 <https://icesat-2.gsfc.nasa.gov/sites/default/files/page_files/ICESat2_ATL03_ATBD_r002.pdf>`__ format and converts them into a LAS file.



.. note::

    ICESat-2 data use `EPSG:7912 <https://epsg.io/7912>`__. ICESat-2 Data products documentation can be found `here <https://icesat-2.gsfc.nasa.gov/science/data-products>`_





.. code-block:: json



    [

        { 

            "type": "readers.hdf", 

            "filename": "ATL03_20190906201911_10800413_002_01.h5",  

            "dimensions":

            { 

                "X" : "gt1l/heights/lon_ph", 

                "Y" : "gt1l/heights/lat_ph", 

                "Z" : "gt1l/heights/h_ph"

            } 

        }, 

        { 

            "type" : "writers.las", 

            "filename": "output.las" 

        } 

    ] 









Options

-------



.. include:: reader_opts.rst



dimensions

  A JSON map with PDAL dimension names as the keys and HDF dataset paths as the values.


    """

    vars = dict()
    vars['type'] = 'readers.hdf'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def i3s(filename=None, threads=None, obb=None, dimensions=None, inputs=None, tag=None, **kwargs):
    """.. _readers.i3s:



readers.i3s

===========



`Indexed 3d Scene Layer (I3S)`_ is a specification created by Esri as a format for their

3D Scene Layer and scene services. The I3S reader handles RESTful webservices in an I3S

file structure/format.



Example

--------------------------------------------------------------------------------

This example will download the Autzen dataset from the ArcGIS scene server and output it to a las file. This is done through PDAL's command line interface or through the pipeline.



.. code-block:: json



  [

      {

          "type": "readers.i3s",

          "filename": "https://tiles.arcgis.com/tiles/8cv2FuXuWSfF0nbL/arcgis/rest/services/AUTZEN_LiDAR/SceneServer",

          "obb": {

              "center": [

                  636590,

                  849216,

                  460

              ],

              "halfSize": [

                  590,

                  281,

                  60

              ],

              "quaternion":

              [

                  0,

                  0,

                  0,

                  1

              ]

          }

      }

  ]



.. code::



    pdal translate i3s://https://tiles.arcgis.com/tiles/8cv2FuXuWSfF0nbL/arcgis/rest/services/AUTZEN_LiDAR/SceneServer \

        autzen.las \

        --readers.i3s.threads=64



Options

--------------------------------------------------------------------------------



.. include:: reader_opts.rst



filename

    I3S file stored remotely. These must be prefaced with an "i3s://".



    Example remote file: ``pdal translate i3s://https://tiles.arcgis.com/tiles/arcgis/rest/services/AUTZEN_LiDAR/SceneServer autzen.las``



threads

    This specifies the number of threads that you would like to use while

    reading. The default number of threads to be used is 8. This affects

    the speed at which files are fetched and added to the PDAL view.



    Example: ``--readers.i3s.threads=64``



obb

    An oriented bounding box used to filter the data being retrieved.  The obb

    is specified as JSON exactly as described by the `I3S specification`_.



dimensions

    Comma-separated list of dimensions that should be read.  Specify the

    Esri name, rather than the PDAL dimension name.



        =============   ===============

        Esri            PDAL

        =============   ===============

        INTENSITY       Intensity

        CLASS_CODE      ClassFlags

        FLAGS           Flag

        RETURNS         NumberOfReturns

        USER_DATA       UserData

        POINT_SRC_ID    PointSourceId

        GPS_TIME        GpsTime

        SCAN_ANGLE      ScanAngleRank

        RGB             Red

        =============   ===============



    Example: ``--readers.i3s.dimensions="returns, rgb"``



min_density and max_density

    This is the range of density of the points in the nodes that will be selected during the read. The density of a node is calculated by the vertex count divided by the effective area of the node. Nodes do not have a uniform density across depths in the tree, so some sections may be more or less dense than others. The default values for these parameters will pull all the leaf nodes (the highest resolution).



    Example: ``--readers.i3s.min_density=2 --readers.i3s.max_density=2.5``



.. _Indexed 3d Scene Layer (I3S): https://github.com/Esri/i3s-spec/blob/master/format/Indexed%203d%20Scene%20Layer%20Format%20Specification.md

.. _I3S specification: https://github.com/Esri/i3s-spec/blob/master/docs/2.0/obb.cmn.md
    """

    vars = dict()
    vars['type'] = 'readers.i3s'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def ilvis2(filename=None, mapping=None, metadata=None, inputs=None, tag=None, **kwargs):
    """.. _readers.ilvis2:



readers.ilvis2

===============



The **ILVIS2 reader** read from files in the ILVIS2 format. See the

`product spec <https://nsidc.org/data/ilvis2>`_ for more information.



.. figure:: readers.ilvis2.metadata.png



    Dimensions provided by the ILVIS2 reader



.. embed::



.. streamable::



Example

-------



.. code-block:: json



  [

      {

          "type":"readers.ilvis2",

          "filename":"ILVIS2_GL2009_0414_R1401_042504.TXT",

          "metadata":"ILVIS2_GL2009_0414_R1401_042504.xml"

      },

      {

          "type":"writers.las",

          "filename":"outputfile.las"

      }

  ]



Options

-------



filename

  File to read from [Required]



.. include:: reader_opts.rst



mapping

  Which ILVIS2 field type to map to X, Y, Z dimensions

  'LOW', 'CENTROID', or 'HIGH' [Default: 'CENTROID']



metadata

  XML metadata file to coincidentally read [Optional]


    """

    vars = dict()
    vars['type'] = 'readers.ilvis2'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def las(compression=None, ignore_vlr=None, fix_dims=None, nosrs=None, inputs=None, tag=None, **kwargs):
    """.. _readers.las:



readers.las

===========



The **LAS Reader** supports reading from `LAS format`_ files, the standard

interchange format for LIDAR data.  The reader does NOT support point formats

containing waveform data (4, 5, 9 and 10).



The reader also supports compressed LAS files, known as LAZ files or

`LASzip`_ files.

In order to use compressed LAS (LAZ), your version of PDAL must be built

with one of the two supported decompressors, `LASzip`_ or `LAZperf`_.

See the :ref:`compression <las_compression>` option below for more information.



.. _LASzip: http://laszip.org

.. _LAZperf: https://github.com/verma/laz-perf



.. note::



  LAS stores X, Y and Z dimensions as scaled integers.  Users converting an

  input LAS file to an output LAS file will frequently want to use the same

  scale factors and offsets in the output file as existed in the input

  file in order to

  maintain the precision of the data.  Use the `forward` option on the

  :ref:`writers.las` to facilitate transfer of header information from

  source to destination LAS/LAZ files.



.. note::



  LAS 1.4 files can contain datatypes that are actually arrays rather than

  individual dimensions.  Since PDAL doesn't support these datatypes, it

  must map them into datatypes it supports.  This is done by appending the

  array index to the name of the datatype.  For example, datatypes 11 - 20

  are two dimensional array types and if a field had the name Foo for

  datatype 11, PDAL would create the dimensions Foo0 and Foo1 to hold the

  values associated with LAS field Foo.  Similarly, datatypes 21 - 30 are

  three dimensional arrays and a field of type 21 with the name Bar would

  cause PDAL to create dimensions Bar0, Bar1 and Bar2.  See the information

  on the extra bytes VLR in the `LAS Specification`_ for more information

  on the extra bytes VLR and array datatypes.



.. warning::



  LAS 1.4 files that use the extra bytes VLR and datatype 0 will be accepted,

  but the data associated with a dimension of datatype 0 will be ignored

  (no PDAL dimension will be created).



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

          "filename":"outputfile.txt"

      }

  ]



Options

-------



_`filename`

  LAS file to read [Required]



.. include:: reader_opts.rst



_`extra_dims`

  Extra dimensions to be read as part of each point beyond those specified by

  the LAS point format.  The format of the option is

  ``<dimension_name>=<type>[, ...]``.  Any valid PDAL :ref:`type <types>` can be

  specified.



  .. note::



      The presence of an extra bytes VLR when reading a version

      1.4 file or a version 1.0 - 1.3 file with **use_eb_vlr** set

      causes this option to be ignored.



.. _LAS format: http://asprs.org/Committee-General/LASer-LAS-File-Format-Exchange-Activities.html

.. _LAS Specification: http://www.asprs.org/a/society/committees/standards/LAS_1_4_r13.pdf



_`use_eb_vlr`

  If an extra bytes VLR is found in a version 1.0 - 1.3 file, use it as if it

  were in a 1.4 file. This option has no effect when reading a version 1.4 file.

  [Default: false]



.. _las_compression:



compression

  May be set to "lazperf" or "laszip" to choose either the LazPerf decompressor

  or the LASzip decompressor for LAZ files.  PDAL must have been built with

  support for the decompressor being requested.  The LazPerf decompressor

  doesn't support version 1 LAZ files or version 1.4 of LAS. [Default: 'none']



ignore_vlr

  A comma-separated list of "userid/record_id" pairs specifying VLR records that should

  not be loaded.



fix_dims

  Make invalid dimension names valid by converting disallowed characters to '_'. Only

  applies to names specified in an extra-bytes VLR. [Default: true]



nosrs

  Don't read the SRS VLRs. The data will not be assigned an SRS. This option is

  for use only in special cases where processing the SRS could cause performance

  issues. [Default: false]
    """

    vars = dict()
    vars['type'] = 'readers.las'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def matlab(filename=None, struct=None, inputs=None, tag=None, **kwargs):
    """.. _readers.matlab:



readers.matlab

==============



The **Matlab Reader** supports readers Matlab ``.mat`` files. Data

must be in a `Matlab struct`_, with field names that correspond to

:ref:`dimension <dimensions>` names. No ability to provide a name map is yet

provided.



Additionally, each array in the struct should ideally have the

same number of points. The reader takes its number of points

from the first array in the struct. If the array has fewer

elements than the first array in the struct, the point's field

beyond that number is set to zero.



.. _`Matlab struct`: https://www.mathworks.com/help/matlab/ref/struct.html



.. note::



    The Matlab reader requires the Mat-File API from MathWorks, and it must be

    explicitly enabled at compile time with the ``BUILD_PLUGIN_MATLAB=ON``

    variable





.. plugin::



.. streamable::



Example

-------



.. code-block:: json



  [

      {

          "type":"readers.matlab",

          "struct":"PDAL",

          "filename":"autzen.mat"

      },

      {

          "type":"writers.las",

          "filename":"output.las"

      }

  ]



Options

-------



filename

  Input file name. [Required]



.. include:: reader_opts.rst



struct

  Array structure name to read. [Default: 'PDAL']
    """

    vars = dict()
    vars['type'] = 'readers.matlab'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def mbio(filename=None, format=None, datatype=None, timegap=None, speedmin=None, inputs=None, tag=None, **kwargs):
    """.. _readers.mbio:



readers.mbio

============



The mbio reader allows sonar bathymetry data to be read into PDAL and

treated as data collected using LIDAR sources.  PDAL uses the `MB-System`_

library to read the data and therefore supports `all formats`_ supported by

that library.  Some common sonar systems are NOT supported by MB-System,

notably Kongsberg, Reson and Norbit.  The mbio reader reads each "beam"

of data after averaging and processing by the MB-System software and stores

the values for the dimensions 'X', 'Y', 'Z' and 'Amplitude'.  X and Y use

longitude and latitude for units and the Z values are in meters (negative,

being below the surface).  Units for 'Amplitude' is not specified and may

vary.



.. plugin::



.. streamable::





Example

-------



This reads beams from a sonar data file and writes points to a LAS file.



.. code-block:: json



  [

      {

          "type" : "readers.mbio",

          "filename" : "shipdata.m57",

          "format" : "MBF_EM3000RAW"

      },

      {

          "type":"writers.las",

          "filename":"outputfile.las"

      }

  ]





Options

-------



filename

  Filename to read from [Required]



.. include:: reader_opts.rst



format

  Name of number of format of file being read.  See MB-System documentation

  for a list of `all formats`_. [Required]



datatype

  Type of data to read.  Either 'multibeam' or 'sidescan'.

  [Default: 'multibeam']



timegap

  The maximum number of seconds that can elapse between pings before the

  end of the data stream is assumed. [Default: 1.0]



speedmin

  The minimum speed that the ship can be moving to before the end of the

  data stream is assumed. [Default: 0]



.. _MB-System: https://www.mbari.org/products/research-software/mb-system/

.. _all formats: http://www3.mbari.org/products/mbsystem/html/mbsystem_formats.html


    """

    vars = dict()
    vars['type'] = 'readers.mbio'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def memoryview(inputs=None, tag=None, **kwargs):
    """.. _readers.memoryview:



readers.memoryview

==================



The memoryview reader is a special stage that allows

the reading of point data arranged in rows directly from memory --

each point needs to have dimension data arranged at a fixed offset

from a base address of the point.

Before each point is read, the memoryview reader calls a function that

should return the point's base address, or a null pointer if there are no

points to be read.



Note that the memoryview reader does not currently work with columnar

data (data where individual dimensions are packed into arrays).



Usage

=====



The memoryview reader cannot be used from the command-line.  It is for use

by software using the PDAL API.



After creating an instance of the memoryview reader, the user should

call pushField() for every dimension that should be read from memory.

pushField() takes a single argument, a MemoryViewReader::Field, that consists

of a dimension name, a type and an offset from the point base address:



.. code-block:: c++



    struct Field

    {

        std::string m_name;

        Dimension::Type m_type;

        size_t m_offset;

    };



    void pushField(const Field&);



The user should also call setIncrementer(), a function that takes a

single argument, a std::function that receives the ID of the point to

be added and should return the base address of the point data, or a

null pointer if there are no more points to be read.



.. code-block:: c++



    using PointIncrementer = std::function<char *(PointId)>;



    void setIncrementer(PointIncrementer inc);





Options

-------



None.
    """

    vars = dict()
    vars['type'] = 'readers.memoryview'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def mrsid(filename=None, inputs=None, tag=None, **kwargs):
    """  .. _readers.mrsid:



readers.mrsid

=============



.. note::



    The MrSID reader is deprecated and will be removed in a future release.



Implements MrSID 4.0 LiDAR Compressor. It requires the `Lidar_DSDK`_ to be able to

decompress and read data.



.. plugin::



Example

-------



.. code-block:: json



  [

      {

          "type":"readers.mrsid",

          "filename":"myfile.sid"

      },

      {

          "type":"writers.las",

          "filename":"outputfile.las"

      }

  ]





Options

-------



filename

  Filename to read from. [Required]



.. include:: reader_opts.rst



.. _Lidar_DSDK: https://www.extensis.com/support/developers


    """

    vars = dict()
    vars['type'] = 'readers.mrsid'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def nitf(filename=None, extra_dims=None, use_eb_vlr=None, compression=None, inputs=None, tag=None, **kwargs):
    """.. _readers.nitf:



readers.nitf

============



The `NITF`_ format is used primarily by the US Department of Defense and

supports many kinds of data inside a generic wrapper. The `NITF 2.1`_ version

added support for LIDAR point cloud data, and the **NITF file reader** supports

reading that data, if the NITF file supports it.



* The file must be NITF 2.1

* There must be at least one Image segment ("IM").

* There must be at least one `DES segment`_ ("DE") named "LIDARA".

* Only LAS or LAZ data may be stored in the LIDARA segment



The dimensions produced by the reader match exactly to the LAS dimension names

and types for convenience in file format transformation.



.. note::



    Only LAS or LAZ data may be stored in the LIDARA segment. PDAL uses

    the :ref:`readers.las` and :ref:`writers.las`

    to actually read and write the data.



.. note::



    PDAL uses a fork of the `NITF Nitro`_ library available at

    https://github.com/hobu/nitro for NITF read and write support.



.. _`NITF Nitro`: http://nitro-nitf.sourceforge.net/wikka.php?wakka=HomePage



.. embed::



.. streamable::





Example

-------



.. code-block:: json



  [

      {

          "type":"readers.nitf",

          "filename":"mynitf.nitf"

      },

      {

          "type":"writers.las",

          "filename":"outputfile.las"

      }

  ]





Options

-------



filename

  Filename to read from [Required]



.. include:: reader_opts.rst



extra_dims

  Extra dimensions to be read as part of each point beyond those specified by

  the LAS point format.  The format of the option is

  ``<dimension_name>=<type>[, ...]``.  Any PDAL :ref:`type <types>` can

  be specified.



  .. note::



      The presence of an extra bytes VLR when reading a version

      1.4 file or a version 1.0 - 1.3 file with **use_eb_vlr** set

      causes this option to be ignored.



use_eb_vlr

  If an extra bytes VLR is found in a version 1.0 - 1.3 file, use it as if it

  were in a 1.4 file. This option has no effect when reading a version 1.4 file.

  [Default: false]



compression

  May be set to "lazperf" or "laszip" to choose either the LazPerf decompressor

  or the LASzip decompressor for LAZ files.  PDAL must have been built with

  support for the decompressor being requested.  The LazPerf decompressor

  doesn't support version 1 LAZ files or version 1.4 of LAS.

  [Default: "none"]



.. _NITF: http://en.wikipedia.org/wiki/National_Imagery_Transmission_Format



.. _NITF 2.1: http://www.gwg.nga.mil/ntb/baseline/docs/2500c/index.html



.. _DES segment: http://jitc.fhu.disa.mil/cgi/nitf/registers/desreg.aspx
    """

    vars = dict()
    vars['type'] = 'readers.nitf'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def numpy(Pipeline=None, Options=None, filename=None, dimension=None, order=None, module=None, function=None, fargs=None, inputs=None, tag=None, **kwargs):
    """.. _readers.numpy:



readers.numpy

=============



PDAL has support for processing data using :ref:`filters.python`, but it is also

convenient to read data from `Numpy`_ for processing in PDAL.



`Numpy`_ supports saving files with the ``save`` method, usually with the

extension ``.npy``. As of PDAL 1.7.0, ``.npz`` files were not yet supported.



.. warning::



    It is untested whether problems may occur if the versions of Python used

    in writing the file and for reading the file don't match.



Array Types

-----------



readers.numpy supports reading data in two forms:



* As a `structured array`_ with specified field names (from `laspy`_ for

  example)

* As a standard array that contains data of a single type.







Structured Arrays

.................



Numpy arrays can be created as structured data, where each entry is a set

of fields.  Each field has a name.  As an example, `laspy`_ provides its

``.points`` as an array of named fields:



::



    import laspy

    f = laspy.file.File('test/data/autzen/autzen.las')

    print (f.points[0:1])



::



    array([ ((63608330, 84939865, 40735, 65, 73, 1, -11, 126, 7326,  245385.60820904),)],

    dtype=[('point', [('X', '<i4'), ('Y', '<i4'), ('Z', '<i4'), ('intensity', '<u2'), ('flag_byte', 'u1'), ('raw_classification', 'u1'), ('scan_angle_rank', 'i1'), ('user_data', 'u1'), ('pt_src_id', '<u2'), ('gps_time', '<f8')])])



The numpy reader supports reading these Numpy arrays and mapping

field names to standard PDAL :ref:`dimension <dimensions>` names.

If that fails, the reader retries by removing ``_``, ``-``, or ``space``

in turn.  If that also fails, the array field names are used to create

custom PDAL dimensions.





Standard (non-structured) Arrays

................................



Arrays without field information contain a single datatype.  This datatype is

mapped to a dimension specified by the ``dimension`` option.



::



    f = open('./perlin.npy', 'rb')

    data = np.load(f,)



    data.shape

    (100, 100)



    data.dtype

    dtype('float64')



::



    pdal info perlin.npy --readers.numpy.dimension=Intensity --readers.numpy.assign_z=4



::



    {

      "filename": "..\/test\/data\/plang\/perlin.npy",

      "pdal_version": "1.7.1 (git-version: 399e19)",

      "stats":

      {

        "statistic":

        [

          {

            "average": 49.5,

            "count": 10000,

            "maximum": 99,

            "minimum": 0,

            "name": "X",

            "position": 0,

            "stddev": 28.86967866,

            "variance": 833.4583458

          },

          {

            "average": 49.5,

            "count": 10000,

            "maximum": 99,

            "minimum": 0,

            "name": "Y",

            "position": 1,

            "stddev": 28.87633116,

            "variance": 833.8425015

          },

          {

            "average": 0.01112664759,

            "count": 10000,

            "maximum": 0.5189296418,

            "minimum": -0.5189296418,

            "name": "Intensity",

            "position": 2,

            "stddev": 0.2024120437,

            "variance": 0.04097063545

          }

        ]

      }

    }





X, Y and Z Mapping

................................................................................

Unless the X, Y or Z dimension is specified as a field in a structured array,

the reader will create dimensions X, Y and Z as necessary and populate them

based on the position of each item of the array.  Although Numpy arrays always

contain contiguous, linear data, that data can be seen to be arranged in more

than one dimension.  A two-dimensional array will cause dimensions X and Y

to be populated.  A three dimensional array will cause X, Y and Z to be

populated.  An array of more than three dimensions will reuse the X, Y and Z

indices for each dimension over three.



When reading data, X Y and Z can be assigned using row-major (C) order or

column-major (Fortran) order by using the ``order`` option.





.. _`Numpy`: http://www.numpy.org/

.. _`laspy`: https://github.com/laspy/laspy

.. _`structured array`: https://docs.scipy.org/doc/numpy/user/basics.rec.html



.. plugin::



.. streamable::



Loading Options

--------------------------------------------------------------------------------



:ref:`readers.numpy` supports two modes of operation - the first is to pass a

reference to a ``.npy`` file to the ``filename`` argument. It will simply load

it and read.



The second is to provide a reference to a ``.py`` script to the ``filename`` argument.

It will then invoke the Python function specified in ``module`` and ``function`` with

the ``fargs`` that you provide.





Loading from a Python script

................................................................................



A reference to a Python function that returns a Numpy array can also be used

to tell :ref:`readers.numpy` what to load. The following example itself loads

a Numpy array from a Python script



Python Script

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. code-block:: python



    import numpy as np



    def load(filename):

        array = np.load(filename)

        return array



Command Line Invocation

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



Using the above Python file with its ``load`` function, the following

:ref:`pdal info<info_command>` invocation passes in the reference to the filename to load.



::



    pdal info threedim.py  \

        --readers.numpy.function=load \

        --readers.numpy.fargs=threedim.npy \

        --driver readers.numpy



Pipeline

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



An example :ref:`pipeline` definition would follow:



.. code-block::



    [

        {

            "function": "load",

            "filename": "threedim.py",

            "fargs": "threedim.npy",

            "type": "readers.numpy"

        },

        ...

    ]



Options

-------



filename

  npy file to read or optionally, a .py file that defines

  a function that returns a Numpy array using the

  ``module``, ``function``, and ``fargs`` options. [Required]



.. include:: reader_opts.rst



dimension

  :ref:`Dimension <dimensions>` name to map raster values



order

  Either 'row' or 'column' to specify assigning the X,Y and Z values

  in a row-major or column-major order. [Default: matches the natural

  order of the array.]









module

  The Python module name that is holding the function to run.



function

  The function name in the module to call.



fargs

  The function args to pass to the function



.. note::

    The functionality of the 'assign_z' option in previous versions is

    provided with :ref:`filters.assign`



    The functionality of the 'x', 'y', and 'z' options in previous versions

    are generally handled with the current 'order' option.



.. _formatted: http://en.cppreference.com/w/cpp/string/basic_string/stof
    """

    vars = dict()
    vars['type'] = 'readers.numpy'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def obj(filename=None, inputs=None, tag=None, **kwargs):
    """.. _readers.obj:



readers.obj

===============



The **OBJ reader** reads data from files in the OBJ format.

This reader constructs a mesh from the faces specified in the OBJ file, ignoring

vertices that are not associated with any face. Faces, vertices, vertex normals and vertex

textures are read, while all other obj elements (such as lines and curves) are ignored.



.. plugin::



Example

-------

This pipeline reads from an example OBJ file outputs

the vertices as a point to a LAS file.



.. code-block:: json



    [

        {

            "type": "readers.obj",

            "filename": "test/data/obj/1.2-with-color.obj"

        },

        {

            "type" : "writers.las",

            "filename": "output.las",

            "scale_x": 1.0e-5,

            "scale_y": 1.0e-5,

            "scale_z": 1.0e-5,

            "offset_x": "auto",

            "offset_y": "auto",

            "offset_z": "auto"

        }

    ]





Options

-------



.. include:: reader_opts.rst



filename

  File to read. [Required]    """

    vars = dict()
    vars['type'] = 'readers.obj'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def optech(filename=None, inputs=None, tag=None, **kwargs):
    """.. _readers.optech:



readers.optech

==============



The **Optech reader** reads Corrected Sensor Data (.csd) files.  These files

contain scan angles, ranges, IMU and GNSS information, and boresight

calibration values, all of which are combined in the reader into XYZ points

using the WGS84 reference frame.





.. embed::



Example

-------



.. code-block:: json



  [

      {

          "type":"readers.optech",

          "filename":"input.csd"

      },

      {

          "type":"writers.text",

          "filename":"outputfile.txt"

      }

  ]





Options

-------



filename

  csd file to read [Required]



.. include:: reader_opts.rst
    """

    vars = dict()
    vars['type'] = 'readers.optech'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def pcd(filename=None, inputs=None, tag=None, **kwargs):
    """.. _readers.pcd:



readers.pcd

===========



The **PCD Reader** supports reading from `Point Cloud Data (PCD)`_ formatted

files, which are used by the `Point Cloud Library (PCL)`_.



.. embed::



.. streamable::





Example

-------



.. code-block:: json



  [

      {

          "type":"readers.pcd",

          "filename":"inputfile.pcd"

      },

      {

          "type":"writers.text",

          "filename":"outputfile.txt"

      }

  ]



Options

-------



filename

  PCD file to read [Required]



.. include:: reader_opts.rst



.. _Point Cloud Data (PCD): https://pcl-tutorials.readthedocs.io/en/latest/pcd_file_format.html

.. _Point Cloud Library (PCL): http://pointclouds.org


    """

    vars = dict()
    vars['type'] = 'readers.pcd'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def pgpointcloud(connection=None, table=None, schema=None, column=None, inputs=None, tag=None, **kwargs):
    """.. _readers.pgpointcloud:



readers.pgpointcloud

====================



The **PostgreSQL Pointcloud Reader** allows you to read points from a PostgreSQL

database with `PostgreSQL Pointcloud`_ extension enabled. The Pointcloud

extension stores point cloud data in tables that contain rows of patches. Each

patch in turn contains a large number of spatially nearby points.



The reader pulls patches from a table, potentially sub-setting the query

with a "where" clause.



.. plugin::



Example

-------



.. code-block:: json



  [

      {

          "type":"readers.pgpointcloud",

          "connection":"dbname='lidar' user='user'",

          "table":"lidar",

          "column":"pa",

          "spatialreference":"EPSG:26910",

          "where":"PC_Intersects(pa, ST_MakeEnvelope(560037.36, 5114846.45, 562667.31, 5118943.24, 26910))"

      },

      {

          "type":"writers.text",

          "filename":"output.txt"

      }

  ]





Options

-------



.. include:: reader_opts.rst



connection

  PostgreSQL connection string. In the form *"host=hostname dbname=database user=username password=pw port=5432"* [Required]



table

  Database table to read from. [Required]



schema

  Database schema to read from. [Default: **public**]



column

  Table column to read patches from. [Default: **pa**]



.. _PostgreSQL Pointcloud: https://github.com/pramsey/pointcloud
    """

    vars = dict()
    vars['type'] = 'readers.pgpointcloud'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def ply(filename=None, inputs=None, tag=None, **kwargs):
    """.. _readers.ply:



readers.ply

===========



The **ply reader** reads points and vertices from the `polygon file format`_, a

common file format for storing three dimensional models.  The ply reader

can read ASCII and binary ply files.



.. embed::



.. streamable::



Example

-------



.. code-block:: json



  [

      {

          "type":"readers.ply",

          "filename":"inputfile.ply"

      },

      {

          "type":"writers.text",

          "filename":"outputfile.txt"

      }

  ]





Options

-------



filename

  ply file to read [Required]



.. include:: reader_opts.rst



.. _polygon file format: http://paulbourke.net/dataformats/ply/
    """

    vars = dict()
    vars['type'] = 'readers.ply'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def pts(filename=None, inputs=None, tag=None, **kwargs):
    """.. _readers.pts:



readers.pts

============



The **PTS reader** reads data from Leica Cyclone PTS files.  It infers

dimensions from points stored in a text file.



.. embed::





Example Pipeline

----------------



.. code-block:: json



  [

      {

          "type":"readers.pts",

          "filename":"test.pts"

      },

      {

          "type":"writers.text",

          "filename":"outputfile.txt"

      }

  ]



Options

-------



filename

  File to read. [Required]



.. include:: reader_opts.rst


    """

    vars = dict()
    vars['type'] = 'readers.pts'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def qfit(filename=None, flip_coordinates=None, scale_z=None, little_endian=None, inputs=None, tag=None, **kwargs):
    """.. _readers.qfit:



******************************************************************************

readers.qfit

******************************************************************************



The **QFIT reader** read from files in the `QFIT format`_ originated for the

Airborne Topographic Mapper (ATM) project at NASA Goddard Space Flight Center.



.. embed::





Example

-------



.. code-block:: json



  [

      {

          "type":"readers.qfit",

          "filename":"inputfile.qi",

          "flip_coordinates":"false",

          "scale_z":"1.0"

      },

      {

          "type":"writers.las",

          "filename":"outputfile.las"

      }

  ]



Options

-------



filename

  File to read from [Required]



.. include:: reader_opts.rst



flip_coordinates

  Flip coordinates from 0-360 to -180-180 [Default: **true**]



scale_z

  Z scale. Use 0.001 to go from mm to m. [Default: **1**]



little_endian

  Are data in little endian format? This should be automatically detected

  by the driver. [Optional]



.. _QFIT format: http://nsidc.org/data/docs/daac/icebridge/ilatm1b/docs/ReadMe.qfit.txt




    """

    vars = dict()
    vars['type'] = 'readers.qfit'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def rdb(filename=None, filter=None, extras=None, Dimensions=None, Metadata=None, inputs=None, tag=None, **kwargs):
    """.. _readers.rdb:



readers.rdb

===========



The **RDB reader** reads from files in the RDB format, the in-house format

used by `RIEGL Laser Measurement Systems GmbH`_.



.. plugin::



.. streamable::



Installation

------------



To build PDAL with rdb support, ``set rdb_DIR`` to the path of your local

rdblib installation. rdblib can be obtained from the `RIEGL download pages`_

with a properly enabled user account. The rdblib files do not need to be

in a system-level directory, though they could be (e.g. they could be in

``/usr/local``, or just in your home directory somewhere). For help building

PDAL with optional libraries, see `the optional library documentation`_.



.. note::

   - Minimum rdblib version required to build the driver and run

     the tests: 2.1.6

   - This driver was developed and tested on Ubuntu 17.10 using GCC 7.2.0.





Example

-------



This example pipeline reads points from a RDB file and stores them in LAS

format. Only points classified as "ground points" are read since option

``filter`` is set to "riegl.class == 2" (see line 5).



.. code-block:: json

  :emphasize-lines: 5

  :linenos:



  [

      {

          "type": "readers.rdb",

          "filename": "autzen-thin-srs.rdbx",

          "filter": "riegl.class == 2"

      },

      {

          "type": "writers.las",

          "filename": "autzen-thin-srs.rdbx"

      }

  ]





Options

-------



filename

  Name of file to read

  [Required]



.. include:: reader_opts.rst



filter

  Point filter expression string (see RDB SDK documentation for details)

  [Optional]

  [Default: empty string (= no filter)]



extras

  Read all available dimensions (`true`) or known PDAL dimensions only (`false`)

  [Optional]

  [Default: false]





Dimensions

----------



The reader maps following default RDB point attributes to PDAL dimensions

(if they exist in the RDB file):



+----------------------------+-------------------------+

| RDB attribute              | PDAL dimension(s)       |

+============================+=========================+

| riegl.id                   | Id::PointId             |

+----------------------------+-------------------------+

| riegl.source_cloud_id      | Id::OriginId            |

+----------------------------+-------------------------+

| riegl.timestamp            | Id::InternalTime        |

+----------------------------+-------------------------+

|                            | Id::X,                  |

| riegl.xyz                  | Id::Y,                  |

|                            | Id::Z                   |

+----------------------------+-------------------------+

| riegl.intensity            | Id::Intensity           |

+----------------------------+-------------------------+

| riegl.amplitude            | Id::Amplitude           |

+----------------------------+-------------------------+

| riegl.reflectance          | Id::Reflectance         |

+----------------------------+-------------------------+

| riegl.deviation            | Id::Deviation           |

+----------------------------+-------------------------+

| riegl.pulse_width          | Id::PulseWidth          |

+----------------------------+-------------------------+

| riegl.background_radiation | Id::BackgroundRadiation |

+----------------------------+-------------------------+

| riegl.target_index         | Id::ReturnNumber        |

+----------------------------+-------------------------+

| riegl.target_count         | Id::NumberOfReturns     |

+----------------------------+-------------------------+

| riegl.scan_direction       | Id::ScanDirectionFlag   |

+----------------------------+-------------------------+

| riegl.scan_angle           | Id::ScanAngleRank       |

+----------------------------+-------------------------+

| riegl.class                | Id::Classification      |

+----------------------------+-------------------------+

|                            | Id::Red,                |

| riegl.rgba                 | Id::Green,              |

|                            | Id::Blue                |

+----------------------------+-------------------------+

|                            | Id::NormalX,            |

| riegl.surface_normal       | Id::NormalY,            |

|                            | Id::NormalZ             |

+----------------------------+-------------------------+



All other point attributes that may exist in the RDB file are ignored unless

the option ``extras`` is set to `true`. If so, a custom dimension is defined

for each additional point attribute, whereas the dimension name is equal to

the point attribute name.



.. note::



   Point attributes are read "as-is", no scaling or unit conversion is done

   by the reader. The only exceptions are point coordinates (``riegl.xyz``)

   and surface normals (``riegl.surface_normal``) which are transformed to

   the RDB file's SRS by applying the matrix defined in the (optional) RDB

   file metadata object ``riegl.geo_tag``.





Metadata

--------



The reader adds following objects to the stage's metadata node:





Object "database"

~~~~~~~~~~~~~~~~~



Contains basic information about the RDB file such as the bounding box,

number of points and the file ID.



.. code-block:: json

   :caption: Example:

   :linenos:



    {

      "bounds": {

        "maximum": {

          "X": -2504493.762,

          "Y": -3846841.252,

          "Z":  4413210.394

        },

        "minimum": {

          "X": -2505882.459,

          "Y": -3848231.393,

          "Z":  4412172.548

        }

      },

      "points": 10653,

      "uuid": "637de54d-7e6b-4004-b6ab-b6bc588ec9ea"

    }





List "dimensions"

~~~~~~~~~~~~~~~~~



List of point attribute description objects.



.. code-block:: json

   :caption: Example:

   :linenos:



    [{

      "compression_options": "shuffle",

      "default_value": 0,

      "description": "Cartesian point coordinates wrt. application coordinate system (0: X, 1: Y, 2: Z)",

      "invalid_value": "",

      "length": 3,

      "maximum_value": 535000,

      "minimum_value": -535000,

      "name": "riegl.xyz",

      "resolution": 0.00025,

      "scale_factor": 1,

      "storage_class": "variable",

      "title": "XYZ",

      "unit_symbol": "m"

    },

    {

      "compression_options": "shuffle",

      "default_value": 0,

      "description": "Target surface reflectance",

      "invalid_value": "",

      "length": 1,

      "maximum_value": 327.67,

      "minimum_value": -327.68,

      "name": "riegl.reflectance",

      "resolution": 0.01,

      "scale_factor": 1,

      "storage_class": "variable",

      "title": "Reflectance",

      "unit_symbol": "dB"

    }]



Details about the point attribute properties see RDB SDK documentation.





Object "metadata"

~~~~~~~~~~~~~~~~~



Contains one sub-object for each metadata object stored in the RDB file.



.. code-block:: json

   :caption: Example:

   :linenos:



    {

      "riegl.scan_pattern": {

        "rectangular": {

          "phi_start": 45.0,

          "phi_stop": 270.0,

          "phi_increment": 0.040,

          "theta_start": 30.0,

          "theta_stop": 130.0,

          "theta_increment": 0.040,

          "program": {

            "name": "High Speed"

          }

        }

      },

      "riegl.geo_tag": {

        "crs": {

          "epsg": 4956,

          "wkt": "GEOCCS[\"NAD83(HARN) \/ Geocentric\",DATUM[\"NAD83(HARN)\",SPHEROID[\"GRS 1980\",6378137.000,298.257222101,AUTHORITY[\"EPSG\",\"7019\"]],AUTHORITY[\"EPSG\",\"6152\"]],PRIMEM[\"Greenwich\",0.0000000000000000,AUTHORITY[\"EPSG\",\"8901\"]],UNIT[\"Meter\",1.00000000000000000000,AUTHORITY[\"EPSG\",\"9001\"]],AXIS[\"X\",OTHER],AXIS[\"Y\",EAST],AXIS[\"Z\",NORTH],AUTHORITY[\"EPSG\",\"4956\"]]"

        },

        "pose": [

           0.837957447, 0.379440385, -0.392240121, -2505819.156,

          -0.545735575, 0.582617132, -0.602270669, -3847595.645,

           0.000000000, 0.718736580,  0.695282481,  4412064.882,

           0.000000000, 0.000000000,  0.000000000,        1.000

        ]

      }

    }



The ``riegl.geo_tag`` object defines the Spatial Reference System (SRS) of the

file. The point coordinates are actually stored in a local coordinate system

(usually horizontally leveled) which is based on the SRS. The transformation

from the local system to the SRS is defined by the 4x4 matrix ``pose`` which

is stored in row-wise order. Point coordinates (``riegl.xyz``) and surface

normals (``riegl.surface_normal``) are automatically transformed to the SRS

by the reader.



Details about the metadata objects see RDB SDK documentation.





List "transactions"

~~~~~~~~~~~~~~~~~~~



List of transaction objects describing the history of the file.



.. code-block:: json

   :caption: Example:

   :linenos:



    [{

      "agent": "RDB Library 2.1.6-1677 (x86_64-windows, Apr  5 2018, 10:58:39)",

      "comments": "",

      "id": 1,

      "rdb": "RDB Library 2.1.6-1677 (x86_64-windows, Apr  5 2018, 10:58:39)",

      "settings": {

        "cache_size": 524288000,

        "chunk_size": 65536,

        "chunk_size_lod": 20,

        "compression_level": 10,

        "primary_attribute": {

          "compression_options": "shuffle",

          "default_value": 0,

          "description": "Cartesian point coordinates wrt. application coordinate system (0: X, 1: Y, 2: Z)",

          "invalid_value": "",

          "length": 3,

          "maximum_value": 535000,

          "minimum_value": -535000,

          "name": "riegl.xyz",

          "resolution": 0.00025,

          "scale_factor": 1,

          "storage_class": "variable",

          "title": "XYZ",

          "unit_symbol": "m"

        }

      },

      "start": "2018-04-06 10:10:39.336",

      "stop": "2018-04-06 10:10:39.336",

      "title": "Database creation"

    },

    {

      "agent": "rdbconvert",

      "comments": "",

      "id": 2,

      "rdb": "RDB Library 2.1.6-1677 (x86_64-windows, Apr  5 2018, 10:58:39)",

      "settings": "",

      "start": "2018-04-06 10:10:39.339",

      "stop": "2018-04-06 10:10:39.380",

      "title": "Import"

    },

    {

      "agent": "RiSCAN PRO 64 bit v2.6.3",

      "comments": "",

      "id": 3,

      "rdb": "RDB Library 2.1.6-1677 (x86_64-windows, Apr  5 2018, 10:58:39)",

      "settings": "",

      "start": "2018-04-06 10:10:41.666",

      "stop": "2018-04-06 10:10:41.666",

      "title": "Meta data saved"

    }]



Details about the transaction objects see RDB SDK documentation.





.. _RIEGL Laser Measurement Systems GmbH: http://www.riegl.com

.. _RIEGL download pages: http://www.riegl.com/members-area/software-downloads/libraries/

.. _the optional library documentation: http://pdal.io/compilation/unix.html#configure-your-optional-libraries
    """

    vars = dict()
    vars['type'] = 'readers.rdb'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def rxp(filename=None, rdtp=None, sync_to_pps=None, reflectance_as_intensity=None, min_reflectance=None, max_reflectance=None, inputs=None, tag=None, **kwargs):
    """.. _readers.rxp:



readers.rxp

===========



The **RXP reader** read from files in the RXP format, the in-house streaming format used by `RIEGL Laser Measurement Systems GmbH`_.



.. warning::

   This software has not been developed by RIEGL, and RIEGL will not provide

   any support for this driver.  Please do not contact RIEGL with any

   questions or issues regarding this driver.  RIEGL is not responsible

   for damages or other issues that arise from use of this driver.

   This driver has been tested against RiVLib version 1.39 on a Ubuntu

   14.04 using gcc43.



.. plugin::



.. streamable::



Installation

------------



To build PDAL with rxp support, set RiVLib_DIR to the path of your local

RiVLib installation.  RiVLib can be obtained from the `RIEGL download pages`_

with a properly enabled user account.  The RiVLib files do not need to be

in a system-level directory, though they could be (e.g. they could be

in ``/usr/local``, or just in your home directory somewhere).





Example

-------



This example rescales the points, given in the scanner's own coordinate

system, to values that can be written to a las file.  Only points with a

valid gps time, as determined by a pps pulse, are read from the rxp, since

the ``sync_to_pps`` option is "true".  Reflectance values are mapped to

intensity values using sensible defaults.



.. code-block:: json



  [

      {

          "type": "readers.rxp",

          "filename": "120304_204030.rxp",

          "sync_to_pps": "true",

          "reflectance_as_intensity": "true"

      },

      {

          "type": "writers.las",

          "filename": "outputfile.las",

          "discard_high_return_numbers": "true"

      }

  ]





We set the ``discard_high_return_numbers`` option to ``true`` on the

:ref:`writers.las`.  RXP files can contain more returns per shot than is

supported by las, and so we need to explicitly tell the las writer to ignore

those high return number points.  You could also use :ref:`filters.python`

to filter those points earlier in the pipeline.





Options

-------



filename

  File to read from, or rdtp URI for network-accessible scanner. [Required]



.. include:: reader_opts.rst



rdtp

  Boolean to switch from file-based reading to RDTP-based. [Default: false]



sync_to_pps

  If "true", ensure all incoming points have a valid pps timestamp, usually

  provided by some sort of GPS clock.  If "false", use the scanner's internal

  time.  [Default: true]



reflectance_as_intensity

  If "true", in addition to storing reflectance values directly, also

  stores the values as Intensity by mapping the reflectance values in the

  range from `min_reflectance` to `max_reflectance` to the range 0-65535.

  Values less than `min_reflectance` are assigned the value 0.

  Values greater `max_reflectance` are assigned the value 65535.

  [Default: true]



min_reflectance

  The low end of the reflectance-to-intensity map.  [Default: -25.0]



max_reflectance

  The high end of the reflectance-to-intensity map.  [Default: 5.0]



.. _RIEGL Laser Measurement Systems GmbH: http://www.riegl.com

.. _RIEGL download pages: http://www.riegl.com/members-area/software-downloads/libraries/


    """

    vars = dict()
    vars['type'] = 'readers.rxp'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def sbet(filename=None, angles_as_degrees=None, inputs=None, tag=None, **kwargs):
    """.. _readers.sbet:



readers.sbet

============



The **SBET reader** read from files in the SBET format, used for exchange data from inertial measurement units (IMUs).

SBET files store angles as radians, but by default this reader converts all angle-based measurements to degrees.

Set ``angles_as_degrees`` to ``false`` to disable this conversion.



.. embed::



.. streamable::



Example

-------





.. code-block:: json



  [

      "sbetfile.sbet",

      "output.las"

  ]





Options

-------



filename

  File to read from [Required]



.. include:: reader_opts.rst



angles_as_degrees

  Convert all angles to degrees. If false, angles are read as radians. [Default: true]




    """

    vars = dict()
    vars['type'] = 'readers.sbet'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def slpk(filename=None, obb=None, dimensions=None, inputs=None, tag=None, **kwargs):
    """.. _readers.slpk:



readers.slpk

============



`Scene Layer Packages (SLPK)`_ is a specification created by Esri as a format

for their 3D Scene Layer and scene services. SLPK is a format that allows you

to package all the necessary :ref:`I3S <readers.i3s>` files together and store them locally rather

than find information through REST.



Example

--------------------------------------------------------------------------------

This example will unarchive the slpk file, store it in a temp directory,

and traverse it. The data will be output to a las file. This is done

through PDAL's command line interface or through the pipeline.



.. code-block:: json



  [

      {

          "type": "readers.slpk",

          "filename": "PDAL/test/data/i3s/SMALL_AUTZEN_LAS_All.slpk",

          "obb": {

              "center": [

                  636590,

                  849216,

                  460

              ],

              "halfSize": [

                  590,

                  281,

                  60

              ],

              "quaternion":

              [

                  0,

                  0,

                  0,

                  1

              ]

          }

      }

  ]



::



    pdal traslate  PDAL/test/data/i3s/SMALL_AUTZEN_LAS_All.slpk autzen.las



Options

--------------------------------------------------------------------------------

filename

    SLPK file must have a file extension of .slpk.

    Example: ``pdal translate /PDAL/test/data/i3s/SMALL_AUTZEN_LAS_ALL.slpk output.las``



.. include:: reader_opts.rst



obb

    An oriented bounding box used to filter the data being retrieved.  The obb

    is specified as JSON exactly as described by the `I3S specification`_.



dimensions

    Comma-separated list of dimensions that should be read.  Specify the

    Esri name, rather than the PDAL dimension name.



        =============== ===============

        Esri            PDAL

        =============== ===============

        INTENSITY       Intensity

        CLASS_CODE      ClassFlags

        FLAGS           Flag

        RETURNS         NumberOfReturns

        USER_DATA       UserData

        POINT_SRC_ID    PointSourceId

        GPS_TIME        GpsTime

        SCAN_ANGLE      ScanAngleRank

        RGB             Red

        =============== ===============



    Example: ``--readers.slpk.dimensions="rgb, intensity"``



min_density and max_density

    This is the range of density of the points in the nodes that will

    be selected during the read. The density of a node is calculated by

    the vertex count divided by the effective area of the node. Nodes do

    not have a uniform density across depths in the tree, so some sections

    may be more or less dense than others. Default values for these

    parameters will select all leaf nodes (the highest resolution).



    Example: ``--readers.slpk.min_density=2 --readers.slpk.max_density=2.5``



.. _Scene Layer Packages (SLPK): https://github.com/Esri/i3s-spec/blob/master/format/Indexed%203d%20Scene%20Layer%20Format%20Specification.md#_8_1

.. _I3S specification: https://github.com/Esri/i3s-spec/blob/master/docs/2.0/obb.cmn.md
    """

    vars = dict()
    vars['type'] = 'readers.slpk'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def smrmsg(filename=None, inputs=None, tag=None, **kwargs):
    """.. _readers.smrmsg:



readers.smrmsg

================



The **SMRMSG reader** read from POSPac MMS post-processed accuracy files, used to describes the accuracy of the post-processed solution (SBET file) and 

contains the position, orientation and velocity RMS after smoothing. See :ref:`writers.sbet`.



.. embed::



.. streamable::



Example

-------





.. code-block:: json



  [

      "smrmsg_xxx.out",

      "output.txt"

  ]





Options

-------



filename

  File to read from [Required]



.. include:: reader_opts.rst


    """

    vars = dict()
    vars['type'] = 'readers.smrmsg'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def terrasolid(filename=None, inputs=None, tag=None, **kwargs):
    """.. _readers.terrasolid:



readers.terrasolid

==================



The **Terrasolid Reader** loads points from `Terrasolid`_ files (.bin).

It supports both Terrasolid format 1 and format 2.



Example

-------



.. code-block:: json



  [

      {

          "type":"readers.terrasolid",

          "filename":"autzen.bin"

      },

      {

          "type":"writers.las",

          "filename":"output.las"

      }

  ]



Options

-------



filename

  Input file name [Required]



.. include:: reader_opts.rst



.. _Terrasolid: https://www.terrasolid.com/home.php
    """

    vars = dict()
    vars['type'] = 'readers.terrasolid'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def text(**kwargs):
    """    """

    vars = dict()
    vars['type'] = 'readers.text'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def tiledb(array_name=None, config_file=None, chunk_size=None, stats=None, bbox3d=None, timestamp=None, end_timestamp=None, start_timestamp=None, strict=None, inputs=None, tag=None, **kwargs):
    """.. _readers.tiledb:



readers.tiledb

==============



Implements `TileDB`_ 2.3.0+ storage.



.. plugin::



.. streamable::



Example

-------



.. code-block:: json



  [

      {

        "type":"readers.tiledb",

        "array_name":"my_array"

      },

      {

        "type":"writers.las",

        "filename":"outputfile.las"

      }

  ]





Options

-------



array_name

  `TileDB`_ array to read from. [Required]



config_file

  `TileDB`_ configuration file [Optional]



chunk_size

  Size of chunks to read from TileDB array [Optional]



stats

  Dump query stats to stdout [Optional]



bbox3d

  TileDB subarray to read in format ([minx, maxx], [miny, maxy], [minz, maxz]) [Optional]



timestamp

  Opens the array at a particular TileDB timestamp [Optional]



end_timestamp

  Opens the array at a particular TileDB timestamp [Optional]



start_timestamp

  Opens the array between a timestamp range of start_timestamp and end_timestamp [Optional]



strict

  Raise an error if the array contains a TileDB attribute not supported by PDAL, the default is set to true to raise an error for unsupported attribute types [Optional]



.. include:: reader_opts.rst



.. _TileDB: https://tiledb.io
    """

    vars = dict()
    vars['type'] = 'readers.tiledb'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars

def tindex(filename=None, srs_column=None, tindex_name=None, sql=None, t_srs=None, filter_srs=None, where=None, dialect=None, inputs=None, tag=None, **kwargs):
    """.. _readers.tindex:



readers.tindex

================================================================================





A `GDAL tile index`_ is an `OGR`_-readable data source of boundary information.

PDAL provides a similar concept for PDAL-readable point cloud data. You can use

the :ref:`tindex_command` application to generate tile index files in any

format that `OGR`_ supports writing. Once you have the tile index, you can then

use the tindex reader to automatically merge and query the data described by

the tiles.



.. _`GDAL`: http://gdal.org

.. _`OGR`: http://gdal.org/ogr/

.. _`GDAL tile index`: http://www.gdal.org/gdaltindex.html





.. embed::





Basic Example

--------------------------------------------------------------------------------



Given a tile index that was generated with the following scenario:



::



    pdal tindex index.sqlite \

        "/Users/hobu/dev/git/pdal/test/data/las/interesting.las" \

        -f "SQLite" \

        --lyr_name "pdal" \

        --t_srs "EPSG:4326"



Use the following :ref:`pipeline <pipeline>` example to read and automatically

merge the data.





.. code-block:: json



  [

      {

          "type":"readers.tindex",

          "filter_srs":"+proj=lcc +lat_1=43 +lat_2=45.5 +lat_0=41.75 +lon_0=-120.5 +x_0=399999.9999999999 +y_0=0 +ellps=GRS80 +units=ft +no_defs",

          "filename":"index.sqlite",

          "where":"location LIKE \'%nteresting.las%\'",

          "wkt":"POLYGON ((635629.85000000 848999.70000000, 635629.85000000 853535.43000000, 638982.55000000 853535.43000000, 638982.55000000 848999.70000000, 635629.85000000 848999.70000000))"

      },

      {

          "type":"writers.las",

          "filename":"outputfile.las"

      }

  ]





Options

--------------------------------------------------------------------------------



filename

  OGROpen'able raster file to read [Required]



.. include:: reader_opts.rst



_`lyr_name`

  The OGR layer name for the data source to use to

  fetch the tile index information.



srs_column

  The column in the layer that provides the SRS

  information for the file. Use this if you wish to

  override or set coordinate system information for

  files.



tindex_name

  The column name that defines the file location for

  the tile index file.

  [Default: **location**]



sql

  `OGR SQL`_ to use to define the tile index layer.



_`bounds`

  A 2D box to pre-filter the tile index. If it is set,

  it will override any `wkt`_ option.



_`wkt`

  A geometry to pre-filter the tile index using

  OGR.



t_srs

  Reproject the layer SRS, otherwise default to the

  tile index layer's SRS. [Default: "EPSG:4326"]



filter_srs

  Transforms any `wkt`_ or `bounds`_ option to this

  coordinate system before filtering or reading data.

  [Default: "EPSG:4326"]



where

  `OGR SQL`_ filter clause to use on the layer. It only

  works in combination with tile index layers that are

  defined with `lyr_name`_



dialect

  `OGR SQL`_ dialect to use when querying tile index layer

  [Default: OGRSQL]



.. _`OGR SQL`: http://www.gdal.org/ogr_sql.html


    """

    vars = dict()
    vars['type'] = 'readers.tindex'
    vars.update(locals().copy())
    del(vars['kwargs'])
    del(vars['vars'])
    for key in list(vars.keys()):
        if vars[key] is None:
            del(vars[key])
    vars.update(kwargs)
    return vars
