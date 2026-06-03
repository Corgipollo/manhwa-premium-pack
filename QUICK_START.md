# ⚡ QUICK START - Activa Ventas en 10 Minutos

**Solo copia y pega estos comandos en orden**

---

## ✅ PASO 1: Verificar que todo esté listo (30 segundos)

```bash
cd C:\Users\Emmanuel\Desktop\manhwa-premium-pack
python verify_setup.py
```

**Resultado esperado**: 
- ✅ rclone instalado
- ✅ Pack ZIP existe
- ✅ GitHub Pages online

---

## 🔧 PASO 2: Configurar rclone con Google Drive (2 min)

```bash
rclone config
```

**Cuando te pregunte, responde**:
1. `n` (new remote)
2. Name: `gdrive`
3. Storage: Busca el número de "drive" (Google Drive) y ponlo
4. Presiona Enter en las siguientes preguntas (usa defaults)
5. Cuando pida autorizar, se abrirá tu navegador → **Acepta**
6. `q` para salir

---

## 📤 PASO 3: Subir Pack a Google Drive (3 min)

```bash
python upload_to_drive.py
```

**Resultado esperado**:
- ✓ Archivo subido exitosamente
- ✓ Link guardado en `drive_link.txt` y `drive_link_direct.txt`

**Copia el link de descarga**:
```bash
cat drive_link_direct.txt
```

**Guárdalo para el siguiente paso** ⬇️

---

## 💳 PASO 4: Crear cuenta y producto en Gumroad (4 min)

### 4.1. Crear cuenta
1. Ir a: https://gumroad.com/signup
2. Registrarte con tu email
3. Verificar email
4. Ir a Settings → Payouts → Conectar tu banco/PayPal

### 4.2. Crear producto
1. Ir a: https://app.gumroad.com/products/new
2. Llenar:
   - **Product name**: `Pack Premium: El Mejor Ingeniero del Mundo - 13 Capítulos Narrados`
   - **Price**: `9.99` USD
   - **Description**: 
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
   - **Content**: Pega el link de `drive_link_direct.txt` (el que copiaste arriba)
   
3. Click en **Publish**

4. **Copiar el link de tu producto** (será algo como):
   ```
   https://TUUSUARIO.gumroad.com/l/manhwa-premium-pack
   ```

---

## 🔗 PASO 5: Activar botón de compra (1 min)

### 5.1. Editar HTML

Abre: `C:\Users\Emmanuel\Desktop\manhwa-premium-pack\index.html`

**Busca** (Ctrl+F) esta línea (aprox. línea 480):
```html
<button class="cta-button" id="buyButton">
```

**Reemplázala** con (pegando TU link de Gumroad):
```html
<a href="https://TUUSUARIO.gumroad.com/l/manhwa-premium-pack" class="cta-button" target="_blank">
    🛒 Comprar Ahora - $9.99
</a>
```

**IMPORTANTE**: Reemplaza `https://TUUSUARIO.gumroad.com/l/manhwa-premium-pack` con TU link real de Gumroad.

### 5.2. Eliminar mensaje temporal

**Busca y ELIMINA** este bloque completo (aprox. líneas 485-491):
```html
<div class="payment-notice">
    <strong>⏳ Sistema de Pago Activándose</strong>
    El botón de compra estará funcional en las próximas 24 horas. ¡Regresa pronto para aprovechar el precio de lanzamiento!
</div>
```

### 5.3. Guardar y subir

```bash
cd C:\Users\Emmanuel\Desktop\manhwa-premium-pack
git add index.html
git commit -m "Activar sistema de pagos Gumroad"
git push
```

---

## ✅ PASO 6: Verificar que todo funcione (2 min)

### 6.1. Espera 2 minutos
GitHub Pages tarda un poco en actualizar.

### 6.2. Abre tu página
```
https://corgipollo.github.io/manhwa-premium-pack/
```

### 6.3. Verifica:
- [ ] La página carga sin errores
- [ ] El botón "Comprar Ahora" está visible
- [ ] Al hacer clic, redirige a Gumroad
- [ ] En Gumroad se ve tu producto con precio $9.99

### 6.4. Prueba de compra (opcional pero recomendado)
1. Compra tu propio producto desde Gumroad
2. Verifica que recibes el email con el link
3. Descarga el ZIP desde el link
4. Confirma que se descarga correctamente

**Nota**: Puedes pedir reembolso después si no quieres quedarte con la compra.

---

## 🎉 ¡LISTO! Sistema Activo

Ahora tienes:
✅ Página de ventas profesional online  
✅ Pack subido a Google Drive  
✅ Sistema de pagos funcional  
✅ Entrega automática vía email  
✅ Monetización 100% pasiva  

---

## 🚀 Promocionar tu pack

Ahora que todo funciona, comparte el link:

### Reddit
- r/manhwa
- r/noveltranslations
- r/LightNovels

### Facebook
- Busca grupos de "manhwa español", "manhua español", "novelas ligeras"

### TikTok/Instagram
- Crea un clip de 30seg del video
- Pon link en bio: https://corgipollo.github.io/manhwa-premium-pack/

### WhatsApp/Telegram
- Comparte directamente con amigos que lean manhwa

---

## 📊 Monitorear ventas

**Dashboard de Gumroad**: https://app.gumroad.com/

Ahí verás:
- Número de ventas
- Ingresos totales
- Emails de compradores
- Analytics

---

## 🆘 Si algo falla

1. Revisa: `INSTRUCCIONES_EMMANUEL.md` (sección Troubleshooting)
2. Ejecuta: `python verify_setup.py` (te dirá qué falta)
3. Busca en Google el error específico

---

## 💰 Próximo nivel

Una vez que vendas las primeras copias:

1. **Crea más packs** (Cap 14-26, 27-39, etc.)
2. **Bundle deals** (3 packs por $24.99)
3. **Programa de afiliados** (actívalo en Gumroad)
4. **Email marketing** (exporta emails de compradores, mándales nuevos packs)

---

**¡Mucho éxito con las ventas!** 🚀💰
