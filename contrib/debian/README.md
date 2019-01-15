
Debian
====================
This directory contains files used to package BKSd/BKS-qt
for Debian-based Linux systems. If you compile BKSd/BKS-qt yourself, there are some useful files here.

## BKS: URI support ##


BKS-qt.desktop  (Gnome / Open Desktop)
To install:

	sudo desktop-file-install BKS-qt.desktop
	sudo update-desktop-database

If you build yourself, you will either need to modify the paths in
the .desktop file or copy or symlink your BKS-qt binary to `/usr/bin`
and the `../../share/pixmaps/BKS128.png` to `/usr/share/pixmaps`

BKS-qt.protocol (KDE)

