from ninja import Router

router = Router(
    tags=['Categories'],
)


@router.get('/')
def get_categories(request):
    pass