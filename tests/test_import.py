import os , sys
sys.path.append(os.getcwd())
import pytest
from repo_name import *

@pytest.mark.asyncio
async def test_import():
    ...