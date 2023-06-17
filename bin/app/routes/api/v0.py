from fastapi import APIRouter

from bin.config import settings

router = APIRouter()


@router.get('')
def index_api():
    #
    return f"APIv0 PokeCake ({settings.PROJECT_VERSION})"
