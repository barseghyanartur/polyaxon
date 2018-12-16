from marshmallow import Schema, fields, post_dump, post_load, validates_schema, ValidationError

from constants import stores
from schemas.base import BaseConfig


def validate_store(store):
    if not store in stores.VALUES:
        raise ValidationError("Store is not valid.")


class StoreSchema(Schema):
    store = fields.Str()
    bucket = fields.Str()
    secret = fields.Str()
    secretKey = fields.Str()

    class Meta:
        ordered = True

    @post_load
    def make(self, data):
        return StoreConfig(**data)

    @post_dump
    def unmake(self, data):
        return StoreConfig.remove_reduced_attrs(data)

    @validates_schema
    def validate_store(self, data):
        if data.get('store'):
            validate_store(data['pvalues'])


class StoreConfig(BaseConfig):
    SCHEMA = StoreSchema
    IDENTIFIER = 'store'

    def __init__(self, store, bucket, secret, secretKey):
        self.store = store
        self.bucket = bucket
        self.secret = secret
        self.secretKey = secretKey