"""Pruebas de humo: se ejecutan sin ventana (SDL dummy)."""
import os
import tempfile

os.environ.setdefault("SDL_VIDEODRIVER", "dummy")
os.environ.setdefault("SDL_AUDIODRIVER", "dummy")
# el record no debe tocar el HOME real durante los tests
os.environ["XDG_DATA_HOME"] = tempfile.mkdtemp(prefix="tank-scrap-test-")

import pygame  # noqa: E402

from tank_scrap import field as fld  # noqa: E402
from tank_scrap import levels  # noqa: E402
from tank_scrap.constants import COST_BRICK, COST_STEEL, FPS, TILE  # noqa: E402
from tank_scrap.entities import Bullet, Scrap  # noqa: E402
from tank_scrap.game import PLAY, Game, _KeyProxy  # noqa: E402

pygame.init()
pygame.display.set_mode((64, 64))


def free_tile(g, skip=()):
    """Primer subtile donde se puede construir (evitando los ya usados)."""
    for y in range(25, 0, -1):
        for x in range(26):
            if (x, y) not in skip and g.field.can_build(x, y):
                return x, y
    raise AssertionError("no hay hueco donde construir")


def new_game():
    g = Game(seed=1)
    g.state = PLAY
    return g


def test_record_va_y_vuelve(tmp_path, monkeypatch):
    from tank_scrap import storage
    monkeypatch.setattr(storage, "APP_DIR", str(tmp_path))
    monkeypatch.setattr(storage, "HISCORE_FILE", str(tmp_path / "hiscore.json"))
    assert storage.load_hiscore() == 0
    assert storage.save_hiscore(4200)
    assert storage.load_hiscore() == 4200


def test_fin_de_fase_pasa_por_el_recuento():
    g = new_game()
    g.queue = []
    g.enemies = []
    for _ in range(int(2.0 * FPS)):
        g.update(1.0 / FPS)
        if g.state == "tally":
            break
    assert g.state == "tally"
    g.state_timer = 99.0
    g.update(1.0 / FPS)
    assert g.state == "intro"
    assert g.stage_index == 1


def test_stages_bien_formados():
    for i in range(levels.stage_count()):
        rows = levels.stage(i)
        assert len(rows) == 13
        assert all(len(r) == 13 for r in rows)
        assert sum(r.count("A") for r in rows) == 1


def test_romper_ladrillo_da_chatarra():
    g = new_game()
    tx, ty = next((x, y) for y in range(26) for x in range(26)
                  if g.field.at(x, y) == fld.BRICK)
    blocked, scrap, base = g.field.hit(tx, ty)
    assert blocked and scrap == 1 and not base
    assert g.field.at(tx, ty) == fld.EMPTY


def test_construir_gasta_chatarra_y_recuperar_devuelve():
    g = new_game()
    g.scrap = 10
    g.build_mode = True
    tx, ty = free_tile(g)
    g.build_cursor = [tx, ty]
    g._build(fld.BUILT_BRICK, COST_BRICK)
    assert g.field.at(tx, ty) == fld.BUILT_BRICK
    assert g.scrap == 10 - COST_BRICK
    g.build_cd = 0.0
    g._demolish()
    assert g.field.at(tx, ty) == fld.EMPTY
    assert g.scrap == 10


def test_no_se_construye_sin_chatarra():
    g = new_game()
    g.scrap = 0
    tx, ty = free_tile(g)
    g.build_cursor = [tx, ty]
    g._build(fld.BUILT_BRICK, COST_BRICK)
    assert g.field.at(tx, ty) == fld.EMPTY


def test_acero_propio_aguanta_bala_normal():
    g = new_game()
    g.scrap = COST_STEEL
    tx, ty = free_tile(g)
    g.build_cursor = [tx, ty]
    g._build(fld.BUILT_STEEL, COST_STEEL)
    assert g.field.at(tx, ty) == fld.BUILT_STEEL
    blocked, scrap, _ = g.field.hit(tx, ty, piercing=False)
    assert blocked and scrap == 0
    assert g.field.at(tx, ty) == fld.BUILT_STEEL
    blocked, _, _ = g.field.hit(tx, ty, piercing=True)
    assert blocked and g.field.at(tx, ty) == fld.EMPTY


def test_recoger_chatarra_al_pisarla():
    g = new_game()
    g.scrap = 0
    r = g.player.rect
    g.scraps.append(Scrap(r.centerx // TILE, r.centery // TILE, 3))
    g._update_player(1.0 / FPS, _KeyProxy({}))
    assert g.scrap == 3
    assert all(s.dead for s in g.scraps)


def test_base_destruida_termina_la_partida():
    g = new_game()
    tx, ty = g.field.base_tiles[0]
    g.bullets.append(Bullet(tx * TILE + 4, ty * TILE + 4, 2, 1.0, "enemy"))
    for _ in range(5):
        g.update(1.0 / FPS)
    assert not g.field.base_alive
    assert g.state == "over"


def test_partida_larga_no_revienta():
    g = new_game()
    for t in range(1200):
        keys = _KeyProxy({pygame.K_RIGHT: t % 80 < 40, pygame.K_UP: t % 80 >= 40})
        g.update(1.0 / FPS, keys=keys)
        if t % 30 == 0:
            g._player_fire()
        g.draw()
        if g.state == "over":
            break
    assert g.frame >= 1


# --- Modo ARENA -------------------------------------------------------------

def arena_game():
    g = Game(seed=2)
    g.mode = "arena"
    g._load_stage(0, reset_run=True)
    g.state = PLAY
    return g


def test_salas_bien_formadas_y_sin_aguila():
    from tank_scrap import arena
    rng = __import__("random").Random(7)
    for i in range(12):
        rows = arena.generate_room(i, rng)
        assert len(rows) == 13 and all(len(r) == 13 for r in rows)
        assert all("A" not in r for r in rows)      # en arena no hay aguila
        assert rows[11][6] == "." and rows[12][6] == "."   # sitio donde apareces
        for (cx, cy) in ((0, 0), (6, 0), (12, 0)):
            assert rows[cy][cx] == "."              # bocas de aparicion libres


def test_arena_tiene_vida_y_no_vidas():
    g = arena_game()
    assert g.player.max_hp == 4 and g.player.hp == 4
    assert g.lives == 0


def test_impacto_quita_vida_no_mata():
    g = arena_game()
    g.player.shield = 0.0
    r = g.player.rect
    g.bullets.append(Bullet(r.centerx, r.centery, 0, 0.1, "enemy"))
    g.update(1.0 / FPS)
    assert g.player.hp == 3
    assert g.state == PLAY


def test_disparo_automatico_solo_al_estar_quieto():
    g = arena_game()
    g.player.fire_cd = 0.0
    g._update_player(1.0 / FPS, _KeyProxy({pygame.K_RIGHT: True}))
    assert not [b for b in g.bullets if b.owner == "player"]
    g.player.fire_cd = 0.0
    g._update_player(1.0 / FPS, _KeyProxy({}))
    assert len([b for b in g.bullets if b.owner == "player"]) == 1


def test_el_keydown_de_espacio_no_dispara_en_arena():
    """En arena el disparo se lee cada fotograma, no en el evento de tecla."""
    g = arena_game()
    g._handle_play_key(pygame.K_SPACE)
    assert not g.bullets


def test_espacio_dispara_en_marcha_pero_recarga_mas_lenta():
    from tank_scrap.constants import ARENA_MOVING_FIRE_PENALTY
    g = arena_game()
    g.player.fire_cd = 0.0
    g._update_player(1.0 / FPS, _KeyProxy({pygame.K_RIGHT: True,
                                           pygame.K_SPACE: True}))
    disparos = [b for b in g.bullets if b.owner == "player"]
    assert len(disparos) == 1
    esperado = g.player.fire_interval * ARENA_MOVING_FIRE_PENALTY
    assert abs(g.player.fire_cd - esperado) < 1e-6

    # parado, la misma tecla recarga a cadencia normal
    g2 = arena_game()
    g2.player.fire_cd = 0.0
    g2._update_player(1.0 / FPS, _KeyProxy({pygame.K_SPACE: True}))
    assert abs(g2.player.fire_cd - g2.player.fire_interval) < 1e-6


def test_en_modo_obra_el_espacio_construye_y_no_dispara():
    g = arena_game()
    g.build_mode = True
    g.player.fire_cd = 0.0
    g._update_player(1.0 / FPS, _KeyProxy({pygame.K_SPACE: True}))
    assert not [b for b in g.bullets if b.owner == "player"]


def test_mejora_se_aplica_y_se_apunta():
    from tank_scrap import arena
    g = arena_game()
    g.offer = [arena.BY_ID["canon"]]
    antes = g.player.max_bullets
    g._choose_upgrade(0)
    assert g.player.max_bullets == antes + 1
    assert g.taken["canon"] == 1
    assert g.stage_index == 1          # elegir mejora pasa a la sala siguiente


def test_las_mejoras_sobreviven_a_la_sala_siguiente():
    from tank_scrap import arena
    g = arena_game()
    g.offer = [arena.BY_ID["orugas"]]
    g._choose_upgrade(0)
    veloz = g.player.speed
    g.offer = [arena.BY_ID["orugas"]]
    g._choose_upgrade(0)
    assert g.player.speed > veloz


def test_reroll_cuesta_chatarra_y_no_va_sin_ella():
    from tank_scrap import arena
    g = arena_game()
    g.scrap = arena.REROLL_COST
    g.offer = arena.offer(g.taken, g.rng)
    g._reroll_offer()
    assert g.scrap == 0 and len(g.offer) == 3
    antes = list(g.offer)
    g._reroll_offer()                  # ya no hay chatarra: la oferta no cambia
    assert g.offer == antes


def test_la_chatarra_sobrante_se_funde_en_puntos():
    from tank_scrap import arena
    g = arena_game()
    g.scrap = 7
    g.score = 100
    g.player.hp = 1
    g.player.shield = 0.0
    g._player_died()
    assert g.state == "over"
    assert g.melted == 7 * arena.SCRAP_TO_SCORE
    assert g.score == 100 + g.melted and g.scrap == 0


def test_bala_perforante_atraviesa_el_ladrillo():
    g = arena_game()
    g.player.pierce_brick = True
    tx, ty = next((x, y) for y in range(26) for x in range(26)
                  if g.field.at(x, y) == fld.BRICK)
    b = Bullet(tx * TILE + 4, ty * TILE + 4, 2, 0.1, "player", pierce_brick=True)
    g.bullets.append(b)
    g._bullet_vs_terrain(b)
    assert g.field.at(tx, ty) == fld.EMPTY
    assert not b.dead                  # sigue su camino


def test_bala_con_rebote_cambia_de_sentido():
    b = Bullet(40, 40, 2, 0.1, "player", bounces=1)
    b.bounce()
    assert b.direction == 0 and b.bounces == 0


# --- Jefe y sonido ----------------------------------------------------------

def test_la_sala_de_jefe_trae_un_jefe():
    from tank_scrap import arena
    rng = __import__("random").Random(3)
    roster = arena.room_roster(4, rng)          # sala 5
    assert roster.count("boss") == 1
    assert roster[-1] == "boss"                 # sale primero (se saca del final)
    assert len(roster) > 1                      # y con escolta
    assert not any("boss" in arena.room_roster(i, rng) for i in (0, 1, 2, 3))


def test_el_jefe_es_grande_duro_y_dispara_por_dos_bocas():
    from tank_scrap import arena
    from tank_scrap.constants import BOSS_PX
    from tank_scrap.entities import BossTank
    g = arena_game()
    boss = BossTank(40, 40, arena.boss_hp(4))
    assert boss.size == BOSS_PX == 32
    assert boss.hp >= 10 and boss.hp > g.player.max_hp
    assert len(boss.muzzles()) == 2
    assert arena.boss_hp(9) > arena.boss_hp(4)  # engorda con la run


def test_el_jefe_suelta_chatarra_al_caer():
    from tank_scrap import arena
    from tank_scrap.constants import BOSS_SCRAP_DROP
    from tank_scrap.entities import BossTank
    g = arena_game()
    boss = BossTank(80, 80, 1)
    g.enemies = [boss]
    g.scraps = []
    b = Bullet(boss.rect.centerx, boss.rect.centery, 0, 0.1, "player")
    g.bullets.append(b)
    g._bullet_vs_tanks(b)
    assert boss.dead
    assert len(g.scraps) == BOSS_SCRAP_DROP
    assert g.score >= 2500
    assert arena.BOSS_CLEAR_SCORE > arena.ROOM_CLEAR_SCORE


def test_el_banco_de_sonido_se_genera_entero():
    from tank_scrap import audio
    bank = audio._build_bank()
    assert len(bank) >= 12
    for name, buf in bank.items():
        assert len(buf) > 100, name             # nada de efectos vacios
        assert max(abs(v) for v in buf) > 1000, name   # y con senal de verdad


def test_el_juego_funciona_sin_tarjeta_de_sonido():
    from tank_scrap import audio
    g = arena_game()
    assert isinstance(g.sfx, audio.NullSfx)     # los tests corren mudos
    g.sfx.play("disparo")                       # no revienta
    assert g.sfx.toggle_mute() is True


# --- Balance: reglas que salen de las mediciones -----------------------------

def test_el_techo_de_chatarra_no_se_pasa_y_cuenta_lo_perdido():
    from tank_scrap.constants import SCRAP_CAP
    g = arena_game()
    g.scrap = SCRAP_CAP - 2
    perdido = g._gain_scrap(10)
    assert g.scrap == SCRAP_CAP
    assert perdido == 8
    assert g.run_wasted == 8
    assert g.run_collected == 2
    assert g._gain_scrap(5) == 5          # en el techo, todo se pierde


def test_recuperar_un_muro_devuelve_exactamente_su_coste():
    """Regresion: los reembolsos estaban a mano y no siguieron a los costes."""
    g = arena_game()
    g.scrap = COST_STEEL + 2
    tx, ty = free_tile(g)
    g.build_cursor = [tx, ty]
    g._build(fld.BUILT_BRICK, COST_BRICK)
    g.build_cd = 0.0
    antes = g.scrap
    g._demolish()
    assert g.scrap - antes == COST_BRICK
    tx, ty = free_tile(g, skip={(tx, ty)})
    g.build_cursor = [tx, ty]
    g.build_cd = 0.0
    g._build(fld.BUILT_STEEL, COST_STEEL)
    g.build_cd = 0.0
    antes = g.scrap
    g._demolish()
    assert g.scrap - antes == COST_STEEL


def test_no_derriba_su_muro_si_el_material_no_le_cabe():
    """Con el techo puesto, recuperar sin sitio borraba el muro y no devolvia
    nada. Ahora se niega y el muro sigue en pie."""
    from tank_scrap.constants import SCRAP_CAP
    g = arena_game()
    g.scrap = 4
    tx, ty = free_tile(g)
    g.build_cursor = [tx, ty]
    g._build(fld.BUILT_BRICK, COST_BRICK)
    g.scrap = SCRAP_CAP
    g.build_cd = 0.0
    g._demolish()
    assert g.field.at(tx, ty) == fld.BUILT_BRICK
    assert g.scrap == SCRAP_CAP


def test_cada_canon_extra_alarga_la_recarga():
    g = arena_game()
    p = g.player
    p.max_bullets = 1
    uno = p.reload_time()
    p.max_bullets = 4
    cuatro = p.reload_time()
    assert cuatro > uno
    # el dano crece, pero menos que el numero de canones
    assert 4 / cuatro < 4 * (1 / uno)


def test_la_vida_del_jefe_crece_mas_que_lineal():
    from tank_scrap import arena
    v = [arena.boss_hp(i) for i in (4, 9, 14, 19)]
    assert v == sorted(v)
    saltos = [v[i + 1] - v[i] for i in range(len(v) - 1)]
    assert saltos == sorted(saltos)       # cada salto es mayor que el anterior
    assert v[0] >= 18


def test_la_escolta_engorda_en_salas_tardias():
    from tank_scrap import arena
    assert arena.enemy_hp_bonus(0) == 0
    assert arena.enemy_hp_bonus(9) == 0
    assert arena.enemy_hp_bonus(10) == 1
    assert arena.enemy_hp_bonus(20) == 2


# --- Mapas de campana: reglas que deben cumplir todos --------------------------

CAMPAIGN_SPAWNS = [(8, 24), (0, 0), (12, 0), (24, 0)]   # jugador y tres bocas


def test_todas_las_fases_dejan_libres_las_apariciones():
    """Regresion: la fase 2 tenia acero en una boca de aparicion, asi que los
    enemigos nunca entraban por ahi y el temporizador perdia turnos."""
    from tank_scrap.constants import TANK_PX, TILE
    for i in range(levels.stage_count()):
        f = fld.Field(levels.stage(i))
        for (tx, ty) in CAMPAIGN_SPAWNS:
            hueco = pygame.Rect(tx * TILE, ty * TILE, TANK_PX, TANK_PX)
            assert not f.blocks_tank_rect(hueco), \
                "fase %d: la aparicion en %s esta tapada" % (i + 1, (tx, ty))


def test_en_todas_las_fases_se_puede_llegar_al_aguila():
    """El ladrillo cuenta como paso (se rompe); el acero y el agua, no."""
    import collections
    for i in range(levels.stage_count()):
        f = fld.Field(levels.stage(i))
        meta = set(f.base_tiles)
        start = (8, 24)
        visto = {start}
        cola = collections.deque([start])
        llega = False
        while cola and not llega:
            x, y = cola.popleft()
            if (x, y) in meta:
                llega = True
                break
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                n = (x + dx, y + dy)
                if n in visto or not f.inside(*n):
                    continue
                if f.at(*n) in (fld.STEEL, fld.WATER):
                    continue
                visto.add(n)
                cola.append(n)
        assert llega, "fase %d: no hay camino del jugador al aguila" % (i + 1)


def test_hay_ocho_fases():
    assert levels.stage_count() == 8


# --- Mejoras con coste (maldiciones) -----------------------------------------

def test_hay_maldiciones_y_cobran_las_dos_mitades():
    from tank_scrap import arena
    maldiciones = [u for u in arena.UPGRADES if u.curse]
    assert len(maldiciones) >= 4
    g = arena_game()
    p = g.player
    vida_antes, cadencia_antes = p.max_hp, p.fire_interval
    g.offer = [arena.BY_ID["sobrecarga"]]
    g._choose_upgrade(0)
    assert p.fire_interval < cadencia_antes      # la mitad buena
    assert p.max_hp == vida_antes - 1            # el precio


def test_la_maldicion_de_vida_nunca_te_deja_en_cero():
    from tank_scrap import arena
    g = arena_game()
    g.player.max_hp = 1
    g.player.hp = 1
    g.offer = [arena.BY_ID["sobrecarga"]]
    g._choose_upgrade(0)
    assert g.player.max_hp == 1 and g.player.hp == 1


def test_el_obus_atraviesa_el_acero_tambien_el_propio():
    from tank_scrap import arena
    g = arena_game()
    g.offer = [arena.BY_ID["obus"]]
    g._choose_upgrade(0)
    assert g.player.pierce_steel
    g.scrap = COST_STEEL
    tx, ty = free_tile(g)
    g.build_cursor = [tx, ty]
    g._build(fld.BUILT_STEEL, COST_STEEL)
    g.player.fire_cd = 0.0
    g._player_fire()
    bala = [b for b in g.bullets if b.owner == "player"][0]
    assert bala.piercing                          # se come su propio muro
    g.field.hit(tx, ty, piercing=bala.piercing)
    assert g.field.at(tx, ty) == fld.EMPTY


def test_los_canones_gemelos_alargan_la_recarga():
    from tank_scrap import arena
    g = arena_game()
    balas_antes = g.player.max_bullets
    recarga_antes = g.player.reload_time()
    g.offer = [arena.BY_ID["gemelos"]]
    g._choose_upgrade(0)
    assert g.player.max_bullets == balas_antes + 2
    assert g.player.reload_time() > recarga_antes


# --- Mando -------------------------------------------------------------------

def test_el_stick_se_traduce_a_una_sola_direccion():
    from tank_scrap.constants import DOWN, LEFT, RIGHT, UP
    from tank_scrap.input import Pads
    assert Pads.axes_to_directions(0.0, 0.0) == []        # zona muerta
    assert Pads.axes_to_directions(0.2, -0.1) == []
    assert Pads.axes_to_directions(0.9, 0.0) == [RIGHT]
    assert Pads.axes_to_directions(-0.9, 0.0) == [LEFT]
    assert Pads.axes_to_directions(0.0, 0.9) == [DOWN]
    assert Pads.axes_to_directions(0.0, -0.9) == [UP]
    # en diagonal manda el eje mas inclinado: una sola direccion, es rejilla
    assert Pads.axes_to_directions(0.9, 0.5) == [RIGHT]
    assert Pads.axes_to_directions(0.5, -0.9) == [UP]


def test_los_botones_del_mando_son_las_mismas_acciones_que_el_teclado():
    from tank_scrap.input import Pads
    assert Pads.button_key(0) == pygame.K_SPACE       # disparar
    assert Pads.button_key(2) == pygame.K_b           # modo obra
    assert Pads.button_key(7) == pygame.K_RETURN      # menus
    assert Pads.button_key(99) is None                # boton sin asignar


def test_el_boton_de_disparo_del_mando_dispara_en_campana():
    g = Game(seed=1)
    g.state = PLAY
    ev = pygame.event.Event(pygame.JOYBUTTONDOWN, button=0)
    g.handle_event(ev)
    assert [b for b in g.bullets if b.owner == "player"]


def test_el_mando_y_el_teclado_suman():
    teclado = _KeyProxy({pygame.K_UP: True})
    mezcla = _KeyProxy({pygame.K_SPACE: True}, teclado)
    assert mezcla[pygame.K_SPACE] and mezcla[pygame.K_UP]
    assert not mezcla[pygame.K_LEFT]
