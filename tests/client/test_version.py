# pylint: disable=invalid-name

import re

from tests import BASE_URL, MASTER_KEY
from meilisearch.version import *


def test_get_version():
    assert re.match(r'^(\d+\.)?(\d+\.)?(\*|\d+)$', VERSION)

def test_get_qualified_version():
    assert qualified_version() == f"Meilisearch Python (v{VERSION})"
