from django.db import models
from django.utils.html import format_html
class Teams(models.Model):
    team_name = models.CharField(max_length=20, verbose_name="Nombre del Equipo")
    flag = models.ImageField(upload_to="photos/teams/flags", verbose_name="Bandera del Equipo")
    shield = models.ImageField(upload_to="photos/teams/shields", verbose_name="Escudo del Equipo")
    
    def __str__(self):
           return self.team_name
       
    def bandera(self):
        return format_html('<img src={} width="100" /> ', self.flag.url)
       
    class Meta:
        verbose_name = "Equipo"
        verbose_name_plural = "Equipos"
        db_table = "teams"
        ordering = ['id']
        
class PlayPosition(models.Model):
    position_name = models.CharField(max_length=30, verbose_name="Posición de juego")
    position_description = models.TextField(max_length=512, verbose_name="Descripción de la posición de juego")
    position_image = models.ImageField(upload_to="photos/positions")
    
    def __str__(self):
           return self.position_name
    
    def Foto(self):
        return format_html('<img src={} width="100" /> ', self.position_image.url)
       
    class Meta:
        verbose_name = "Posición de juego"
        verbose_name_plural = "Posiciones de juego"
        db_table = "positions"
        ordering = ['id']

class Players(models.Model):
    p_first_name = models.CharField(max_length=25, verbose_name="Primer nombre del jugador")
    p_second_name = models.CharField(max_length=25, verbose_name="Segundo nombre del jugador", null=True, blank=True)
    p_first_last_name = models.CharField(max_length=25, verbose_name="Primer apellido del jugador")
    p_second_last_name = models.CharField(max_length=25, verbose_name="Segundo apellido del jugador", null=True, blank=True)
    p_photo = models.ImageField(upload_to="photos/players", verbose_name="Foto del jugador", null=True)
    p_birth = models.DateField(verbose_name="Fecha de nacimiento del jugador", null=True, blank=True)
    p_position = models.ForeignKey(PlayPosition, on_delete=models.CASCADE, verbose_name="Posición de juego del jugador")
    p_number = models.PositiveIntegerField(verbose_name="Número de la camiseta del jugador")
    p_is_titular = models.BooleanField(verbose_name="Es jugador titular")
    p_team = models.ForeignKey(Teams, on_delete=models.CASCADE, verbose_name="Equipo del jugador")
    
    def __str__(self):
           return f"{self.p_first_name} {self.p_second_last_name}"
       
    def Foto(self):
        return format_html('<img src={} width="100" /> ', self.p_photo.url)
       
    class Meta:
        verbose_name = "Jugador"
        verbose_name_plural = "Jugadores"
        db_table = "players"
        ordering = ['p_team', 'p_position', 'p_is_titular']
        
class TechnicalTeamRoles(models.Model):
    role_name = models.CharField(max_length=30, verbose_name="Nombre del rol")
    role_description = models.TextField(max_length=255, verbose_name="Descripción del rol")
    
    def __str__(self):
           return self.role_name
       
    class Meta:
        verbose_name = "Rol del ET"
        verbose_name_plural = "Roles del ET"
        db_table = "technicalteamroles"
        ordering = ['id']
    
class TechnicalTeam(models.Model):
    t_first_name = models.CharField(max_length=25, verbose_name="Primer nombre del integrante del ET")
    t_second_name = models.CharField(max_length=25, verbose_name="Segundo nombre del integrante del ET", null=True, blank=True)
    t_first_last_name = models.CharField(max_length=25, verbose_name="Primer apellido del integrante del ET")
    t_second_last_name = models.CharField(max_length=25, verbose_name="Segundo apellido del integrante del ET", null=True, blank=True)
    t_nationality = models.CharField(max_length=30, verbose_name="Nacionalidad")
    t_role = models.ForeignKey(TechnicalTeamRoles, on_delete=models.CASCADE, verbose_name="Rol del integrante del ET")
    t_team = models.ForeignKey(Teams, on_delete=models.CASCADE, verbose_name="Equipo al cual pertenece el ET")
    
    def __str__(self):
           return f"{self.t_first_name} {self.t_second_name}"
       
    class Meta:
        verbose_name = "ET"
        verbose_name_plural = "ET"
        db_table = "technicalteam"
        ordering = ['t_team']
    
