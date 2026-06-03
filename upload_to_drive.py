#!/usr/bin/env python3
"""
Script para subir Pack Premium a Google Drive y obtener link público
Usa rclone (más simple que OAuth2 manual)
"""

import subprocess
import sys
import os
from pathlib import Path

# Configuración
ZIP_FILE = Path("../Pack_Premium_Manhua_Narrado_13_Videos.zip")
REMOTE_NAME = "gdrive"  # Nombre del remote de rclone
REMOTE_PATH = "ManhuaPremiumPacks"  # Carpeta en Drive

def check_rclone():
    """Verifica que rclone esté instalado"""
    try:
        result = subprocess.run(['rclone', 'version'],
                              capture_output=True, text=True, check=True)
        print("✓ rclone encontrado")
        return True
    except FileNotFoundError:
        print("✗ rclone no instalado. Instalar con: winget install Rclone.Rclone")
        return False

def check_remote_configured():
    """Verifica que el remote de Google Drive esté configurado"""
    result = subprocess.run(['rclone', 'listremotes'],
                          capture_output=True, text=True)
    remotes = result.stdout.strip().split('\n')

    if f"{REMOTE_NAME}:" in remotes:
        print(f"✓ Remote '{REMOTE_NAME}' configurado")
        return True
    else:
        print(f"✗ Remote '{REMOTE_NAME}' no configurado")
        print("\nConfigúralo con:")
        print(f"  rclone config")
        print("  - Elige: n (new remote)")
        print(f"  - Name: {REMOTE_NAME}")
        print("  - Storage: drive (Google Drive)")
        print("  - Sigue el wizard de autenticación")
        return False

def upload_file():
    """Sube el archivo a Google Drive"""
    if not ZIP_FILE.exists():
        print(f"✗ Archivo no encontrado: {ZIP_FILE}")
        return False

    print(f"\n📤 Subiendo {ZIP_FILE.name} a Google Drive...")
    print(f"   Tamaño: {ZIP_FILE.stat().st_size / (1024*1024):.1f} MB")

    # Subir archivo
    cmd = [
        'rclone', 'copy',
        str(ZIP_FILE),
        f"{REMOTE_NAME}:{REMOTE_PATH}",
        '--progress',
        '--transfers', '1'
    ]

    result = subprocess.run(cmd)

    if result.returncode == 0:
        print("✓ Archivo subido exitosamente")
        return True
    else:
        print("✗ Error al subir archivo")
        return False

def make_public_and_get_link():
    """Hace el archivo público y obtiene el link"""
    remote_file = f"{REMOTE_NAME}:{REMOTE_PATH}/{ZIP_FILE.name}"

    print("\n🔗 Obteniendo link público...")

    # Obtener link (rclone link crea un link compartible)
    result = subprocess.run(
        ['rclone', 'link', remote_file],
        capture_output=True, text=True
    )

    if result.returncode == 0:
        link = result.stdout.strip()
        print(f"\n✓ LINK PÚBLICO GENERADO:")
        print(f"  {link}")

        # Guardar link en archivo
        with open('drive_link.txt', 'w') as f:
            f.write(link)
        print(f"\n✓ Link guardado en: drive_link.txt")

        # Convertir a link de descarga directa
        if 'drive.google.com' in link and '/file/d/' in link:
            file_id = link.split('/file/d/')[1].split('/')[0]
            direct_link = f"https://drive.google.com/uc?export=download&id={file_id}"
            print(f"\n✓ LINK DE DESCARGA DIRECTA:")
            print(f"  {direct_link}")

            with open('drive_link_direct.txt', 'w') as f:
                f.write(direct_link)

        return link
    else:
        print("✗ Error al obtener link")
        print(f"   {result.stderr}")
        return None

def main():
    print("=" * 60)
    print("  UPLOADER A GOOGLE DRIVE - PACK PREMIUM MANHWA")
    print("=" * 60)

    # Verificaciones
    if not check_rclone():
        sys.exit(1)

    if not check_remote_configured():
        sys.exit(1)

    # Upload
    if not upload_file():
        sys.exit(1)

    # Get public link
    link = make_public_and_get_link()

    if link:
        print("\n" + "=" * 60)
        print("  ✓ PROCESO COMPLETADO")
        print("=" * 60)
        print("\nSiguientes pasos:")
        print("1. Copia el link de drive_link.txt")
        print("2. Úsalo para probar la descarga")
        print("3. Actualiza la página de ventas con el link")
    else:
        print("\n✗ No se pudo completar el proceso")
        sys.exit(1)

if __name__ == "__main__":
    main()
