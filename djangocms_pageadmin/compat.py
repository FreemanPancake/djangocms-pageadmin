import django

from cms import __version__ as CMS_VERSION

from packaging.version import Version


DJANGO_4_2 = Version(django.get_version()) >= Version('4.2')

CMS_41 = Version("4.1") <= Version(CMS_VERSION)

if CMS_41:
    from cms.api import create_page_content  # noqa: F401
else:
    from cms.api import create_title as create_page_content  # noqa: F401
