# Instalar o eliminar un paquete

## Antes

```bash
cd ~/GitHub/trabajo/code-temple
git status
pacman -Qqe > /tmp/paquetes-explicitos-antes.txt
```

Registrar el motivo y comprobar si el paquete puede crear servicios o modificar
la red.

## Ejecución

```bash
sudo pacman -S nombre-del-paquete
```

Para eliminarlo:

```bash
sudo pacman -Rns nombre-del-paquete
```

## Después

```bash
pacman -Qqe > docs/infra/madre/paquetes-explicitos.txt
systemctl list-unit-files --type=service --state=enabled --no-pager
systemctl list-units --type=service --state=running --no-pager
```

Actualizar `software.md`, `servicios.md` y `cambios.md` según corresponda.

## Rollback

```bash
sudo pacman -Rns nombre-del-paquete
```

Antes de eliminarlo comprobar que ningún servicio o paquete importante depende
de él.
