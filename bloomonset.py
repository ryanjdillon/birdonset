
def read_data():
    import netCDF4
    return lons, lats, vals


def create_circle(x, y, radius):
    import shapely

    return shapely.Point(x,y).buffer(radius)


def get_mean_chla(data, circle):
    # data within circle
    # numpy.nanmean()

    return mean_chla


def project_lonlat(lon, lat):
    import pyproj

    # LatLon with WGS84 datum used by GPS units and Google Earth
    wgs84=pyproj.Proj("+init=EPSG:4326")

    # nplaea
    # http://spatialreference.org/ref/epsg/wgs-84-north-pole-laea-canada/
    nplaea=pyproj.Proj("+init=EPSG:3573")

    return pyproj.transform(wgs84, nplaea, lon, lat)


def get_bloom_onset():
    '''Cacluate bloom onset n kilometers around colonies'''

    radius = 5 # km

    # read chl-a data

    # Define colony coordinates in WGS84 Lat & Lon
    colonies = dict()
    colonies['rost'] = dict()
    colonies['rost']['lonlat'] = (67.456, 10.123)

    # Create circle polygons around colony locations
    for colony in colonies:
        lon, lat = colony['lonlat']
        colony['xy'] = project_lonlat(lon, lat)

        # make polygon from projection centroid
        circle = create_polygon(x, y, radius)
        colony['circle'] = create_circle(x, y, radius)

        # Get chl-a means over time period
        colony['mean'] = get_mean_chla(data, circle)

    return colonies


    # Return bloom onset (threshold % above median)
