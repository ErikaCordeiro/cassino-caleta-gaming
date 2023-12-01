from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Player, Transaction
from django.http import Http404

@csrf_exempt
def index_view(request):
    return JsonResponse({"message": "Welcome to the wallet app!"})

from django.http import JsonResponse

@csrf_exempt
def balance_view(request):
    if request.method == 'GET':
        player_id = request.GET.get('player')
        try:
            player = Player.objects.get(pk=player_id)
            return JsonResponse({"player": player.player_id, "balance": player.balance})
        except Player.DoesNotExist:
            return JsonResponse({"error": "Player does not exist"}, status=404)


# Endpoint para realizar uma aposta
@csrf_exempt
def bet_view(request):
    if request.method == 'POST':
        data = request.POST
        player_id = data.get('player')
        value = float(data.get('value'))
        try:
            player = Player.objects.get(pk=player_id)
            if player.balance >= value:
                player.balance -= value
                player.save()
                transaction = Transaction.objects.create(player=player, value=value, transaction_type='bet')
                return JsonResponse({"player": player_id, "balance": player.balance, "txn": transaction.id})
            else:
                return JsonResponse({"error": "Insufficient balance"}, status=400)
        except Player.DoesNotExist:
            raise Http404("Player does not exist")

# Endpoint para realizar um ganho
@csrf_exempt
def win_view(request):
    if request.method == 'POST':
        data = request.POST
        player_id = data.get('player')
        value = float(data.get('value'))
        try:
            player = Player.objects.get(pk=player_id)
            player.balance += value
            player.save()
            transaction = Transaction.objects.create(player=player, value=value, transaction_type='win')
            return JsonResponse({"player": player_id, "balance": player.balance, "txn": transaction.id})
        except Player.DoesNotExist:
            raise Http404("Player does not exist")

# Endpoint para cancelar transações de apostas
@csrf_exempt
def rollback_view(request):
    if request.method == 'POST':
        data = request.POST
        player_id = data.get('player')
        txn_id = data.get('txn')
        value = float(data.get('value'))
        try:
            player = Player.objects.get(pk=player_id)
            transaction = Transaction.objects.get(pk=txn_id, player=player, value=value)
            
            if transaction.transaction_type == 'bet':
                player.balance += value  
                player.save()
                transaction.delete()  
                return JsonResponse({"code": "OK", "balance": player.balance})
            elif transaction.transaction_type == 'deposit':
                return JsonResponse({"code": "Invalid"})
            elif transaction.transaction_type == 'rollback':
                return JsonResponse({"code": "AlreadyCancelled"})
            else:
                return JsonResponse({"code": "Invalid"})
        
        except (Player.DoesNotExist, Transaction.DoesNotExist):
            return JsonResponse({"code": "Invalid"})