"""Constantes globales: rejilla, escalas, colores y afinado del juego."""

# --- Rejilla ---------------------------------------------------------------
# El campo es una rejilla de subtiles de 8 px (como los medios ladrillos del
# Battle City original). Una "celda" clasica de 16 px son 2x2 subtiles.
TILE = 8
FIELD_TILES = 26                      # 26 x 26 subtiles = 13 x 13 celdas
FIELD_PX = TILE * FIELD_TILES         # 208 px logicos

PANEL_PX = 48                         # panel lateral (marcador)
MARGIN_PX = 8

SCREEN_W = MARGIN_PX * 2 + FIELD_PX + PANEL_PX
SCREEN_H = MARGIN_PX * 2 + FIELD_PX
SCALE = 3                             # cada pixel logico son 3 fisicos
FPS = 60

# --- Tanques y balas -------------------------------------------------------
TANK_PX = 16                          # los tanques ocupan 2x2 subtiles
BULLET_PX = 3

PLAYER_SPEED = 0.85
PLAYER_BULLET_SPEED = 2.6
PLAYER_MAX_BULLETS = 1
PLAYER_FIRE_INTERVAL = 0.55     # cadencia base (la usa el disparo automatico)
# Cada canon extra alarga la recarga un 15%: asi el dano crece sublinealmente.
# Sin esto, 4 canones x cadencia x4 daban 19,7 impactos/s y cualquier oleada
# tardia se limpiaba en menos de dos segundos.
MULTI_BARREL_PENALTY = 0.15
PLAYER_LIVES = 3
PLAYER_SPAWN_SHIELD = 2.5             # segundos de invulnerabilidad al nacer

ENEMY_FIRE_MIN = 0.6                  # cadencia enemiga (segundos)
ENEMY_FIRE_MAX = 2.1
ENEMY_TURN_CHANCE = 0.02              # prob. de cambiar de rumbo por frame
ENEMY_HUNT_CHANCE = 0.65              # sesgo hacia el objetivo al girar
ENEMY_SPAWN_DELAY = 1.6               # segundos entre apariciones
ENEMIES_ON_FIELD = 4                  # maximo simultaneo

# --- La vuelta de tuerca: la chatarra --------------------------------------
# Cada ladrillo destruido deja chatarra en el suelo. La recoges pisandola y la
# gastas construyendo muro donde tu quieras: el escenario es tu arsenal.
SCRAP_PER_BRICK = 1
SCRAP_LIFETIME = 14.0                 # segundos antes de oxidarse y desaparecer
# Los costes salen de una medicion, no del gusto: un mapa de campana ofrece
# ~170 de chatarra y una sala de arena ~73, y un bot que no la busca acaba la
# segunda sala con 46-79 en mano. Con ladrillo a 1 y acero a 6 la economia no
# tenia tension: reponer el anillo del aguila costaba 8 de un presupuesto
# practicamente infinito. Al doble, y con techo en mano, cada muro se paga.
COST_BRICK = 2
COST_STEEL = 10
# Techo de chatarra encima: acumular deja de ser gratis y hay que gastar antes
# de seguir. Lo que pasa del techo se pierde (el HUD lo avisa).
SCRAP_CAP = 20
BUILD_RANGE_TILES = 5                 # alcance del cursor de construccion
BUILD_COOLDOWN = 0.12
SCRAP_START = 4                       # con lo que arrancas cada partida

# --- Modo ARENA ------------------------------------------------------------
ARENA_PLAYER_HP = 4                   # el tanque aguanta varios impactos
ARENA_AUTOFIRE = True                 # disparas solo al estar quieto
ARENA_MANUAL_FIRE = True              # ademas puedes disparar con espacio
# Disparar en marcha desestabiliza el canon: misma bala, recarga mas larga.
# A 1.0 el movimiento deja de tener penalizacion.
ARENA_MOVING_FIRE_PENALTY = 1.6

# El jefe: 32x32 (4x4 subtiles), lento, muy duro, y suelta un monton de
# chatarra al caer.
BOSS_PX = 32
# La vida del jefe tiene que crecer como crece el dano del jugador, que es
# multiplicativo (canones x cadencia). Con 10 + 2 por ciclo, el jefe de la
# sala 5 moria en 1,7 s con dos canones y cadencia x2. Ahora crece un 35% por
# ciclo, que es el orden de lo que gana el jugador entre jefe y jefe.
BOSS_HP_BASE = 18
BOSS_HP_GROWTH = 1.35
BOSS_SCRAP_DROP = 12

# --- Puntuacion ------------------------------------------------------------
SCORE_BY_KIND = {"basic": 100, "fast": 200, "power": 300, "armor": 400,
                 "boss": 2500}
SCORE_STAGE_CLEAR = 500

# --- Direcciones -----------------------------------------------------------
UP, RIGHT, DOWN, LEFT = 0, 1, 2, 3
DIR_VECTORS = {UP: (0, -1), RIGHT: (1, 0), DOWN: (0, 1), LEFT: (-1, 0)}

# --- Paleta (NES-ish) ------------------------------------------------------
BLACK = (0, 0, 0)
GREY_FRAME = (99, 99, 99)
WHITE = (232, 232, 232)
BRICK_A = (168, 80, 40)
BRICK_B = (216, 128, 72)
BRICK_MORTAR = (96, 44, 24)
STEEL_A = (144, 152, 168)
STEEL_B = (208, 216, 224)
WATER_A = (24, 64, 168)
WATER_B = (64, 120, 224)
TREE_A = (24, 104, 40)
TREE_B = (56, 152, 64)
ICE_A = (192, 208, 224)
ICE_B = (224, 236, 248)
SCRAP_A = (200, 160, 64)
SCRAP_B = (248, 216, 120)
BASE_A = (216, 176, 48)
BASE_B = (248, 232, 128)
PLAYER_A = (216, 184, 56)
PLAYER_B = (248, 224, 136)
PLAYER_C = (128, 96, 16)
ENEMY_COLORS = {
    "basic": ((176, 176, 176), (232, 232, 232), (88, 88, 88)),
    "fast":  ((72, 160, 216), (152, 216, 248), (24, 80, 136)),
    "power": ((200, 72, 72), (248, 152, 152), (120, 24, 24)),
    "armor": ((168, 88, 200), (224, 168, 248), (88, 32, 112)),
    # El jefe va en acero oscuro con vivos naranjas: pesa a la vista y no se
    # confunde con el dorado del jugador.
    "boss":  ((88, 88, 104), (248, 152, 56), (40, 40, 56)),
}
HUD_DIM = (136, 136, 136)
GHOST_OK = (120, 224, 120)
GHOST_NO = (224, 88, 88)
