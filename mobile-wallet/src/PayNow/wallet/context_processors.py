from .models import Wallet


def wallet(request):
    if request.user.is_authenticated:
        wallet = Wallet.objects.filter(wallet=request.user).first()
        return {'wallet': wallet}
    return {}