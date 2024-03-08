from fastapi import APIRouter

# item 관련 API 호출
router = APIRouter()


@router.get('/api/v1/items/{item_id}',
            status_code=200,
            tags=['items', 'payment'],
            summary='특정 아이템을 가져오기',
            description='Item모델의 item_id값을 가지고 하나의 아이템 데이터 정보를 가져옴',
            response_description='아이템 세부 정보 반환'
            )
def get_item(item_id: int):
    return {'items': 'item'}

# async & sync (동기 비동기)