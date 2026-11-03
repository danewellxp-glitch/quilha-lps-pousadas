import os
BASE = os.path.dirname(os.path.abspath(__file__))
_maps = {}


def ig(user, idx):
    key = user.replace('.', '_')
    if key not in _maps:
        _maps[key] = open(os.path.join(BASE, 'data', f'_{key}_files.txt')).read().split('\n')
    return os.path.join(os.path.join(os.environ.get('QD_LEGACY', '/home/claude'), 'ig'), _maps[key][idx])


def gm(name):
    return os.path.join('/mnt/user-data/uploads/Quilha Digital/lps-pousadas/_fotos-google/gm', name)


def review_sources(sources):
    """sources: list of (key, name, score_str, head)"""
    return [dict(key=k, name=n, score=s, head=h) for k, n, s, h in sources]


def ig2(user, idx):
    key = user.replace('.', '_')
    if key not in _maps:
        _maps[key] = open(os.path.join(BASE, 'data', f'_{key}_files.txt')).read().split('\n')
    return os.path.join(os.path.join(os.environ.get('QD_LEGACY', '/home/claude'), 'ig2'), _maps[key][idx])
