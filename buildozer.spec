[app]
# (str) Nombre de la aplicación.
title = FindMe42

# (str) Nombre del paquete, debe ser único en el Play Store.
package.name = findme42

# (str) Dominio de la aplicación (formato: org.nombre).
package.domain = dev.greenlass

# (str) Versión de la aplicación.
version = 0.1

# (str) Versión de la aplicación (puede contener letras y números).
version.code = alpha-prerelease

# (list) Lista de requisitos separados por comas
requirements = python3,kivy

# (str) Nombre del archivo fuente de la aplicación.
source.include_exts = py,png,jpg,kv,atlas

# (str) Icono de la aplicación (debe estar en assets/).
icon.filename = %(source.dir)s/assets/icono.png

# (str) Estilo de la aplicación.
android.api = 31
android.minapi = 21
android.sdk = 31
android.ndk = 23b

# (list) Permisos requeridos por la aplicación.
android.permissions = INTERNET

# (bool) Habilitar o deshabilitar la depuración.
# Si se establece en True, se generarán registros de depuración adicionales.
debug = 1

# (list) Archivos de inclusión, lista de archivos adicionales que deseas incluir.
# Por ejemplo: include_patterns = assets/*, other_files/*
# include_patterns = 

# (bool) Si se establece en 1, se empaquetará la aplicación en modo de depuración.
# Esto significa que puedes usar herramientas de depuración como `adb logcat`.
# 0 significa que se empaquetará en modo de lanzamiento.
release = 0
