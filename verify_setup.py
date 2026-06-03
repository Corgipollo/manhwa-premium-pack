#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de verificación del sistema de ventas manhwa
Ejecuta checks para confirmar que todo está listo
"""

import subprocess
import urllib.request
import sys
import io
from pathlib import Path

# Fix para Windows encoding
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

def check(name, test_func):
    """Helper para ejecutar checks"""
    try:
        result = test_func()
        status = "✅" if result else "❌"
        print(f"{status} {name}")
        return result
    except Exception as e:
        print(f"❌ {name} - Error: {e}")
        return False

def check_rclone_installed():
    """Verifica que rclone esté instalado"""
    try:
        subprocess.run(['rclone', 'version'],
                      capture_output=True, check=True)
        return True
    except:
        return False

def check_rclone_configured():
    """Verifica que Google Drive esté configurado en rclone"""
    try:
        result = subprocess.run(['rclone', 'listremotes'],
                              capture_output=True, text=True)
        return 'gdrive:' in result.stdout
    except:
        return False

def check_zip_exists():
    """Verifica que el ZIP exista"""
    zip_path = Path("../Pack_Premium_Manhua_Narrado_13_Videos.zip")
    return zip_path.exists()

def check_github_pages():
    """Verifica que GitHub Pages esté online"""
    try:
        response = urllib.request.urlopen(
            'https://corgipollo.github.io/manhwa-premium-pack/',
            timeout=10
        )
        return response.status == 200
    except:
        return False

def check_html_has_content():
    """Verifica que el HTML tenga contenido esperado"""
    html_path = Path("index.html")
    if not html_path.exists():
        return False

    content = html_path.read_text(encoding='utf-8')
    checks = [
        "El Mejor Ingeniero del Mundo" in content,
        "$9.99" in content,
        "13 capítulos" in content.lower() or "13 videos" in content.lower()
    ]
    return all(checks)

def check_drive_link_exists():
    """Verifica si ya se generó el link de Drive"""
    return Path("drive_link.txt").exists()

def main():
    print("=" * 60)
    print("  VERIFICACIÓN DEL SISTEMA DE VENTAS MANHWA")
    print("=" * 60)
    print()

    # Checks pre-requisitos
    print("📋 PRE-REQUISITOS:")
    checks_prereq = [
        ("rclone instalado", check_rclone_installed),
        ("Pack ZIP existe (1.6GB)", check_zip_exists),
        ("HTML contiene información correcta", check_html_has_content),
    ]

    prereq_ok = all(check(name, func) for name, func in checks_prereq)

    print()
    print("🔧 CONFIGURACIÓN:")
    checks_config = [
        ("rclone configurado con Google Drive", check_rclone_configured),
        ("Link de Drive generado", check_drive_link_exists),
    ]

    config_ok = all(check(name, func) for name, func in checks_config)

    print()
    print("🌐 DEPLOYMENT:")
    checks_deploy = [
        ("GitHub Pages online", check_github_pages),
    ]

    deploy_ok = all(check(name, func) for name, func in checks_deploy)

    print()
    print("=" * 60)

    if prereq_ok and deploy_ok:
        print("✅ SISTEMA BASE OPERACIONAL")
        print()
        if not config_ok:
            print("⚠️  PENDIENTE: Configurar rclone y subir pack a Drive")
            print()
            print("Siguiente paso:")
            print("  1. Ejecutar: rclone config")
            print("  2. Ejecutar: python upload_to_drive.py")
        else:
            print("✅ TODO LISTO - PROCEDER A GUMROAD")
            print()
            print("Siguiente paso:")
            print("  1. Crear cuenta Gumroad: https://gumroad.com/signup")
            print("  2. Crear producto con link de drive_link_direct.txt")
            print("  3. Actualizar botón en index.html")
    else:
        print("❌ HAY PROBLEMAS - REVISAR ARRIBA")
        sys.exit(1)

    print("=" * 60)

if __name__ == "__main__":
    main()
