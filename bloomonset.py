
def read_data(file_path):
    '''Read in netCDF chl-a data into numpy masked arrays'''
    import netCDF4

    #TODO
    #nc = netCDF4.D

    return lons, lats, vals


def create_circle(x, y, r_xy):
    '''Create circle polygon around projected coordinates with given radius'''
    import shapely

    return shapely.Point(x,y).buffer(r_xy)


def get_mean_chla(data, circle):
    '''Cacluate mean value of data within circle polygon'''

    #TODO

    # data within circle
    # numpy.nanmean()

    return mean_chla


def dates_over_threshold(data, circle, threshold):
    #TODO
    return dates


def km2proj(lon, lat, in_proj, out_proj, km):
    '''Convert km to projection units at a given latitude'''
    import pyproj

    # TODO use inproj for g creation

    # Use WGS84 for creating new point r_km away on same latitude
    # r_km converted from km to m for calculation
    g = pyproj.Geod(epsg='WGS84')
    x, y, az = g.fwd(lon, lat, 90, km*1000)

    x0, y0 = pyproj.transform(wgs84, lon0, lat0)
    x1, y1 = pyproj.transform(wgs84, lon1, lat1)

    xy = x1 - x0

    return xy


def get_bloom_onset():
    '''Cacluate bloom onset n kilometers around colonies'''
    import yaml_tools

    r_km = 5 # km

    # WGS84 - datum used commonly used for longitude and latitude
    wgs84=pyproj.Proj("+init=EPSG:4326")

    # nplaea - equal area projection best for arctic geo calculations
    # http://spatialreference.org/ref/epsg/wgs-84-north-pole-laea-canada/
    nplaea=pyproj.Proj("+init=EPSG:3573")

    # read chl-a data

    # Define colony coordinates in WGS84 Lat & Lon
    # TODO read from yaml
    # TODO Save data path/version and code version to colony dict field
    #          - if data/code version changed, save new file
    # TODO process for multiple polygon radii
    # colonies = yaml_tools.read_yaml(file_path)

    colonies = dict()
    colonies['rost'] = dict()
    colonies['rost']['lonlat'] = (67.456, 10.123)


    # Create circle polygons around colony locations
    for colony in colonies:
        lon, lat = colony['lonlat']
        colony['xy'] = pyproj.transform(wgs84, nplaea, lon, lat)

        # Convert radius in km to proj units at colony latitude
        r_xy = km2proj(lon, lat, wgs84, nplaea, r_km)

        # Create circle polygon around colony
        colony['circle'] = create_circle(x, y, r_xy)

        # Get chl-a means over time period
        colony['mean'] = get_mean_chla(data, circle)

    # TODO write to yaml
    # yaml_tools.write_yaml(colonies, out_path)

    return colonies


    # Return bloom onset (threshold % above median)
