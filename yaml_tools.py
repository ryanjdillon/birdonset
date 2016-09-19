
def read_yaml(file_path):
    '''Read YAML file and return as python dictionary'''
    import yaml

    with open(file_path, 'r') as f:
        return yaml.safe_load(f)


def write_yaml(data, out_path):
    '''Write python dict to YAML'''
    import errno
    import os
    import yaml

    # Make directory for calibration file if does not exist
    base_path, file_name = os.path.split(out_path)
    try:
        os.makedirs(base_path)
    except OSError as exc: # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(base_path):
            pass
        else: raise

    # Write dictionary to YAML
    with open(out_path, 'w') as f:
        yaml.dump(data, f, default_flow_style=True)
        return None


