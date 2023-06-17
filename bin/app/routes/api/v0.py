from fastapi import APIRouter

router = APIRouter()


@router.get('')
def index_api():
    #
    return 'APIv0 PokeCake (0.1.0)'
