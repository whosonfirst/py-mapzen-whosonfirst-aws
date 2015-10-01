# https://pythonhosted.org/setuptools/setuptools.html#namespace-packages
__import__('pkg_resources').declare_namespace(__name__)

from boto.s3.connection import S3Connection
from boto.s3.key import Key

import ConfigParser
import os.path

import geojson
import logging

import mapzen.whosonfirst.utils as utils

class base:

    def __init__(self, **kwargs):

        self._key_ = None
        self._secret_ = None

        if kwargs.get('credentials', False):

            creds = os.path.abspath(kwargs['credentials'])

            if not os.path.exists(creds):
                raise Exception, "E_NONEXISTENT_CREDENTIALS"

            cfg = ConfigParser.ConfigParser()
            cfg.read(creds)

            self._key_ = cfg.get('default', 'aws_access_key_id')
            self._secret_ = cfg.get('default', 'aws_secret_access_key')

        else:
            self._key_ = kwargs.get('aws_key', None)
            self._secret_ = kwargs.get('aws_secret', None)

class s3(base):

    def __init__(self, **kwargs):

        base.__init__(self, **kwargs)

        if not kwargs.get('bucket', None):
            raise Exception, "E_INVISIBLE_BUCKETNAME"

        self.bucketname = kwargs['bucket']

        conn = S3Connection(self._key_, self._secret_)
        bucket = conn.get_bucket(self.bucketname)
        
        self.conn = conn
        self.bucket = bucket

    def store_file(self, path):

        abs_path = os.path.abspath(path)

        fh = open(abs_path, 'r')
        feature = geojson.load(fh)

        props = feature.get('properties', {})
        id = props.get('wof:id', None)

        if id == None:
            raise Exception, "E_INSUFFICIENT_WHOSONFIRST"

        rel_path = utils.id2relpath(id)

        k = Key(self.bucket)
        k.key = rel_path

        k.set_contents_from_filename(abs_path)
        k.set_acl('public-read')

        # print k.generate_url(expires_in=0, query_auth=False)
        return True
        


