# Guía de Configuración de Facebook para n8n (Parte Final: Credencial Genérica)

Has seleccionado "Generic Credential Type" > "OAuth2 API". ¡Perfecto! Rellena los campos con estos valores exactos:

| Campo | Valor |
| :--- | :--- |
| **Authorization URL** | `https://www.facebook.com/v19.0/dialog/oauth` |
| **Access Token URL** | `https://graph.facebook.com/v19.0/oauth/access_token` |
| **Client ID** | `905494189119414` |
| **Client Secret** | `9bc22338c0e7b992b794ffa3a86fe44d` |
| **Scope** | `pages_manage_posts,pages_read_engagement,publish_video` |
| **Auth URI Query Parameters** | `response_type=code` |
| **Authentication** | `Header` |

## Pasos siguientes:

1.  Copia la **"OAuth Redirect URL"** que aparece arriba en esa misma ventana (empieza por `http...`).
2.  Ve a Facebook Developers > Inicio de sesión con Facebook > Configuración.
3.  Pega esa URL en "URI de redireccionamiento de OAuth válidos" y guarda.
4.  Vuelve a n8n y dale al botón rojo **"Connect my account"** (o el círculo de conexión).
5.  Se abrirá Facebook para que aceptes los permisos. ¡Acepta todo!
