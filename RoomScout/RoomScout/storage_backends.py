from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class PublicMediaStorage(S3Boto3Storage):
	bucket_name = 'roomscout-public'
	location = settings.AWS_PUBLIC_MEDIA_LOCATION
	file_overwrite = False


class PrivateMediaStorage(S3Boto3Storage):
	location = settings.AWS_PRIVATE_MEDIA_LOCATION
	bucket_name = 'roomscout-private'
	default_acl = 'private'
	file_overwrite = False
	custom_domain = False
