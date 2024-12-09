from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from .models import Teams, TechnicalTeam, Players
from django.contrib.auth.decorators import login_required

@login_required(login_url=reverse_lazy('no_access'))
def teams(request):
    user = request.user
    teams = Teams.objects.all()
    context = {'teams':teams, 'user':user}
    return render(request, 'logged/teams.html', context)

@login_required(login_url=reverse_lazy('no_access'))
def team_detail(request, id):
    team = get_object_or_404(Teams, id=id)
    technicians = TechnicalTeam.objects.filter(t_team_id=team)
    player = Players.objects.filter(p_team_id=team)
    return render(request, 'logged/team_detail.html', {'team': team, 'tech': technicians, 'player': player})

@login_required(login_url=reverse_lazy('no_access'))
def player_detail(request, id):
    player = get_object_or_404(Players, id=id)
    team = player.p_team
    context = {
        'player': player,
        'team_name': team.team_name,
        'team_flag': team.flag.url,
        'team_shield': team.shield.url
    }
    return render(request, 'logged/player_detail.html', context)

@login_required(login_url=reverse_lazy('no_access'))
def techs(request):
    techs = TechnicalTeam.objects.all()
    context = {'techs':techs}
    return render(request, 'logged/techs.html', context)

@login_required(login_url=reverse_lazy('no_access'))
def players(request):
    players = Players.objects.all()
    context = {'players':players}
    return render(request, 'logged/players.html', context)

@login_required(login_url=reverse_lazy('no_access'))
def can(request):
    return render(request, 'logged/cities/cn.html')

@login_required(login_url=reverse_lazy('no_access'))
def us(request):
    return render(request, 'logged/cities/us.html')

@login_required(login_url=reverse_lazy('no_access'))
def mex(request):
    return render(request, 'logged/cities/mx.html')