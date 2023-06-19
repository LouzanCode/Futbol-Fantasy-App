from .models import Player, PlayerPosition, Team

def players(request):
    return {
        'players': Player.objects.all()
    }
    
def positions(request):
    return {
        'postions': PlayerPosition.objects.all()
    }
    
def teams(request):
    return {
        'teams': Team.objects.all()
    }