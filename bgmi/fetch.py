# coding=utf-8
from __future__ import print_function, unicode_literals

from bgmi.config import DATA_SOURCE
from bgmi.utils import print_error
from bgmi.website import bangumi_moe, mikan

DATA_SOURCE_MAP = {
    'mikan_project': mikan.Mikanani,
    'bangumi_moe': bangumi_moe.BangumiMoe
}


def wrap(*args,**kwargs):
    print_error('date source "{}" in config is wrong, please edit it manually'.format(DATA_SOURCE))

    pass


website = DATA_SOURCE_MAP.get(DATA_SOURCE, wrap)()
