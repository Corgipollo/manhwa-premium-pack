# 📋 INSTRUCCIONES PARA ACTIVAR SISTEMA DE VENTAS

**Tiempo estimado: 10 minutos**

---

## ✅ PASO 1: Subir Pack a Google Drive

### Opción A: Con rclone (Recomendado - MÁS FÁCIL)

1. **Configurar rclone** (solo primera vez):
   ```bash
   rclone config
   ```
   - Presiona `n` para nuevo remote
   - Name: `gdrive`
   - Storage: `drive` (elige el número que corresponda a Google Drive)
   - Sigue el wizard de autenticación (se abrirá tu navegador)
   - Acepta los permisos
   - Presiona `q` para salir del config

2. **Ejecutar script de subida**:
   ```bash
   cd C:\Users\Emmanuel\Desktop\manhwa-premium-pack
   python upload_to_drive.py
   ```

3. **Resultado**: El script subirá el ZIP y te dará el link público. 
   - Se guardará en: `drive_link.txt`
   - Link directo de descarga en: `drive_link_direct.txt`

### Opción B: Manual (Si rclone falla)

1. Ve a [Google Drive](https://drive.google.com)
2. Crea carpeta: `ManhuaPremiumPacks`
3. Sube: `Pack_Premium_Manhua_Narrado_13_Videos.zip`
4. Clic derecho → Compartir → Cualquiera con el enlace
5. Copia el link compartido
6. Convierte a link de descarga:
   - Si el link es: `https://drive.google.com/file/d/XXXXXX/view?usp=sharing`
   - Cámbialo a: `https://drive.google.com/uc?export=download&id=XXXXXX`

---

## ✅ PASO 2: Crear Cuenta Gumroad

1. **Ir a**: https://gumroad.com/signup
2. **Crear cuenta** con tu email
3. **Verificar** tu cuenta (revisa tu email)
4. **Ir a Settings** → **Payouts** y conecta tu cuenta bancaria/PayPal

**Importante**: Gumroad cobra 10% de comisión por venta.

---

## ✅ PASO 3: Crear Producto en Gumroad

1. **Ir a**: https://gumroad.com/products/new
2. **Llenar**:
   - **Product name**: `Pack Premium: El Mejor Ingeniero del Mundo - 13 Capítulos Narrados`
   - **Price**: `9.99` USD
   - **Description**: Copia esto:
     ```
     🎬 Pack Premium: 13 capítulos completos de "El Mejor Ingeniero del Mundo" narrados profesionalmente en español.

     ✅ Incluye:
     - 13 videos HD (1080p)
     - Narración profesional con IA de alta calidad
     - Subtítulos sincronizados
     - Más de 2 horas de contenido
     - Descarga instantánea vía Google Drive

     💎 Pago único - Acceso ilimitado de por vida
     🔒 Garantía de satisfacción 7 días
     ```

3. **Tipo de entrega**:
   - Selecciona: **"I'll email the customer"** (Te enviaremos el link)
   - **Content**: Pega el link de Google Drive (del archivo `drive_link_direct.txt`)

4. **Cover Image** (Opcional pero recomendado):
   - Sube una captura del manhwa o del video
   - Tamaño recomendado: 1600x1200px

5. **Click**: `Publish`

6. **Copiar el link del producto**. Será algo como:
   ```
   https://tuusuario.gumroad.com/l/manhwa-premium-pack
   ```

---

## ✅ PASO 4: Actualizar Página de Ventas

1. **Abrir**: `C:\Users\Emmanuel\Desktop\manhwa-premium-pack\index.html`

2. **Buscar** esta línea (aprox. línea 480):
   ```html
   <button class="cta-button" id="buyButton">
   ```

3. **Reemplazar** TODO el bloque del botón con:
   ```html
   <a href="TU_LINK_DE_GUMROAD_AQUI" class="cta-button gumroad-button" target="_blank">
       🛒 Comprar Ahora - $9.99
   </a>
   ```
   **Ejemplo**:
   ```html
   <a href="https://tuusuario.gumroad.com/l/manhwa-premium-pack" class="cta-button gumroad-button" target="_blank">
       🛒 Comprar Ahora - $9.99
   </a>
   ```

4. **ELIMINAR** el bloque de aviso temporal:
   ```html
   <div class="payment-notice">
       <strong>⏳ Sistema de Pago Activándose</strong>
       ...
   </div>
   ```

5. **Guardar** el archivo

---

## ✅ PASO 5: Subir a GitHub y Activar GitHub Pages

1. **Crear repo en GitHub**:
   - Ve a: https://github.com/new
   - Repository name: `manhwa-premium-pack`
   - Tipo: Public
   - Click: `Create repository`

2. **Subir archivos**:
   ```bash
   cd C:\Users\Emmanuel\Desktop\manhwa-premium-pack
   git init
   git add index.html
   git commit -m "Initial commit: Landing page manhwa premium"
   git branch -M main
   git remote add origin https://github.com/TU_USUARIO/manhwa-premium-pack.git
   git push -u origin main
   ```

3. **Activar GitHub Pages**:
   - En el repo, ve a: **Settings** → **Pages**
   - Source: **Deploy from a branch**
   - Branch: **main** → **/root**
   - Click: **Save**

4. **Esperar 2-3 minutos** y tu página estará en:
   ```
   https://TU_USUARIO.github.io/manhwa-premium-pack/
   ```

---

## ✅ PASO 6: Probar Todo el Flujo

1. **Visita tu página**: `https://TU_USUARIO.github.io/manhwa-premium-pack/`
2. **Click en "Comprar Ahora"** → Debe abrir Gumroad
3. **Haz una compra de prueba** (puedes cancelarla o pedir reembolso después)
4. **Verifica** que recibas el email con el link de Drive
5. **Descarga** el ZIP para confirmar que funciona

---

## 🎯 RESULTADO FINAL

Una vez completados todos los pasos tendrás:

✅ Pack subido a Google Drive con link público  
✅ Producto configurado en Gumroad  
✅ Página de ventas profesional online  
✅ Sistema de pago funcional  
✅ Entrega automática vía email  

**Tu página de ventas**: `https://TU_USUARIO.github.io/manhwa-premium-pack/`

---

## 🚨 TROUBLESHOOTING

### Si rclone no funciona:
- Verifica que esté instalado: `rclone version`
- Si no está: `winget install Rclone.Rclone`
- Reconfigura el remote: `rclone config` → delete old → create new

### Si GitHub Pages no carga:
- Espera 5 minutos (puede tardar)
- Verifica que el archivo se llame exactamente: `index.html`
- Revisa Settings → Pages que esté en "main" branch

### Si Gumroad no envía el link:
- Verifica en Product Settings que esté en "Published"
- Revisa que el link de Drive sea público
- Prueba el link de Drive en ventana incógnita

---

## 📞 SOPORTE

Si algo falla:
1. Lee el error exacto
2. Busca en Google: `rclone/gumroad/github pages [tu error]`
3. Revisa los archivos de log

---

## 📊 PRÓXIMOS PASOS (Opcional)

Una vez que todo funcione:

1. **Marketing**:
   - Comparte la página en redes sociales
   - Crea posts en Reddit (r/manhwa, r/noveltranslations)
   - Promociona en grupos de Facebook de manhwa

2. **Analytics**:
   - Añade Google Analytics a tu página
   - Monitorea conversiones en Gumroad Dashboard

3. **Expansión**:
   - Crea más packs (Cap 14-26, 27-39, etc.)
   - Ofrece bundle deals
   - Programa de afiliados con Gumroad

**¡Éxito con las ventas!** 🚀
