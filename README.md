# 🎬 Pack Premium: El Mejor Ingeniero del Mundo

Landing page de ventas para pack premium de 13 capítulos de manhwa narrado.

## 📁 Estructura del Proyecto

```
manhwa-premium-pack/
├── index.html                    # Landing page de ventas
├── upload_to_drive.py           # Script para subir a Google Drive
├── INSTRUCCIONES_EMMANUEL.md    # Guía paso a paso para activar ventas
└── README.md                    # Este archivo
```

## 🚀 Inicio Rápido

### 1. Subir Pack a Google Drive
```bash
# Configurar rclone (primera vez)
rclone config

# Ejecutar upload
python upload_to_drive.py
```

### 2. Configurar Gumroad
- Crear cuenta en https://gumroad.com
- Crear producto con el link de Drive
- Copiar link del producto

### 3. Actualizar HTML
Reemplaza el botón placeholder con tu link de Gumroad en `index.html`

### 4. Deploy a GitHub Pages
```bash
git add .
git commit -m "Update con link de Gumroad"
git push
```

## 📖 Documentación Completa

Ver: [INSTRUCCIONES_EMMANUEL.md](./INSTRUCCIONES_EMMANUEL.md)

## 🛠️ Stack Técnico

- HTML5 + CSS3 (sin frameworks, vanilla)
- Python 3 + rclone (para upload a Drive)
- Gumroad (procesamiento de pagos)
- GitHub Pages (hosting)

## 💰 Monetización

- Precio: $9.99 USD
- Plataforma: Gumroad (10% comisión)
- Entrega: Google Drive link automático
- Garantía: 7 días

## 📊 Características de la Landing

✅ Diseño responsive  
✅ Hero section atractivo  
✅ Lista de 13 capítulos  
✅ Sección de pricing con CTA  
✅ FAQ section  
✅ Optimizada para conversión  

## 🔗 Links

- **Página de ventas**: `https://TU_USUARIO.github.io/manhwa-premium-pack/`
- **Gumroad**: `https://gumroad.com/TU_PRODUCTO`
- **Google Drive**: Ver `drive_link.txt` después del upload

## 📝 Licencia

Todos los derechos reservados © 2026
