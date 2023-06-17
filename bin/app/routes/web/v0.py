from fastapi import APIRouter, Depends, Request, Response, Form, status

from sqlalchemy.orm import Session

from starlette.templating import Jinja2Templates
from starlette.responses import RedirectResponse

from bin.app.databases.index import connect
from bin.app.models.list import List


templates = Jinja2Templates(directory='bin/src')

router = APIRouter()


@router.get('/')
def index_web(request: Request, db: Session = Depends(connect)):
    lists = db.query(List).all()
    payload = {
        'request': request,
        'doc_title': 'WEBv0 CORE (0.1.0)',
        'data': lists
    }
    return templates.TemplateResponse('views/home.html', payload)


@router.post('/add')
def add(request: Request, title: str = Form(...), db: Session = Depends(connect)):
    new_list = List(title=title)
    db.add(new_list)
    db.commit()

    url = router.url_path_for('index_web')
    return RedirectResponse(url=url, status_code=status.HTTP_303_SEE_OTHER)


@router.get('/update/{list_id}')
def update(request: Request, list_id: int, db: Session = Depends(connect)):
    list = db.query(List).filter(List.id == list_id).first()
    list.complete = not list.complete
    db.commit()

    url = router.url_path_for('index_web')
    return RedirectResponse(url=url, status_code=status.HTTP_302_FOUND)


@router.get('/delete/{list_id}')
def delete(request: Request, list_id: int, db: Session = Depends(connect)):
    list = db.query(List).filter(List.id == list_id).first()
    db.delete(list)
    db.commit()

    url = router.url_path_for('index_web')
    return RedirectResponse(url=url, status_code=status.HTTP_302_FOUND)


@router.get('/robots.txt')
def robots():
    data = '''
    # https://www.robotstxt.org/robotstxt.html
    User-agent: *
    Disallow: /
    '''
    return Response(content=data, media_type='text/plain')
