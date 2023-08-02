
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from aifs_client.api.annotation_template_api import AnnotationTemplateApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from aifs_client.api.annotation_template_api import AnnotationTemplateApi
from aifs_client.api.annotation_template_type_api import AnnotationTemplateTypeApi
from aifs_client.api.data_view_api import DataViewApi
from aifs_client.api.data_view_upload_api import DataViewUploadApi
