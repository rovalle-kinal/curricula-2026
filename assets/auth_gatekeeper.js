/**
 * Fundación Kinal - Escuela Técnica Superior (ETS)
 * Sistema de Control de Acceso Criptográfico de Cliente
 * Contraseña Institucional: 3T$Kinal2026
 */
(function() {
    'use strict';

    const AUTH_KEY = 'kinal_auth_session';
    const AUTH_TOKEN = 'kinal_authenticated_2026';
    const TARGET_HASH = 'cd8c7161e853a05ea3f88f5f53784d60fb2aa01c4e66207dec9b8747218b96d8';
    const VALID_PASS = '3T$Kinal2026';

    // Si ya está autenticado en la sesión actual, salimos de inmediato
    if (sessionStorage.getItem(AUTH_KEY) === AUTH_TOKEN) {
        return;
    }

    // Ocultar contenido mientras se verifica
    const lockStyle = document.createElement('style');
    lockStyle.id = 'kinal-auth-lock-style';
    lockStyle.innerHTML = `
        body > * { display: none !important; }
        #kinal-auth-overlay { display: flex !important; }
    `;
    document.head.appendChild(lockStyle);

    // Función auxiliar SHA-256 (con fallback si crypto.subtle no está disponible en file://)
    async function verifyPassword(input) {
        // Limpieza de caracteres invisibles o espacios al pegar
        const cleanInput = input.replace(/[\u200B-\u200D\uFEFF]/g, '').trim();
        
        // 1. Verificación directa infalible
        if (cleanInput === VALID_PASS) {
            return true;
        }

        // 2. Verificación criptográfica SHA-256 (si crypto.subtle está soportado)
        try {
            if (window.crypto && window.crypto.subtle) {
                const msgBuffer = new TextEncoder().encode(cleanInput);
                const hashBuffer = await crypto.subtle.digest('SHA-256', msgBuffer);
                const hashArray = Array.from(new Uint8Array(hashBuffer));
                const computed = hashArray.map(b => b.toString(16).padStart(2, '0')).join('');
                if (computed === TARGET_HASH) {
                    return true;
                }
            }
        } catch (err) {
            console.warn('Crypto API no disponible en este contexto, usando fallback:', err);
        }

        return false;
    }

    function initAuthModal() {
        if (sessionStorage.getItem(AUTH_KEY) === AUTH_TOKEN) {
            if (lockStyle.parentNode) lockStyle.parentNode.removeChild(lockStyle);
            return;
        }

        const overlay = document.createElement('div');
        overlay.id = 'kinal-auth-overlay';
        overlay.style.cssText = `
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            z-index: 999999;
            background: linear-gradient(135deg, #0D162C 0%, #152244 50%, #22376D 100%);
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 1.25rem;
            font-family: Arial, Helvetica, sans-serif;
            color: #0F172A;
        `;

        overlay.innerHTML = `
            <div style="
                background: #FFFFFF;
                max-width: 440px;
                width: 100%;
                border-radius: 1.25rem;
                padding: 2.25rem 2rem;
                box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.45);
                border: 2px solid rgba(236, 145, 35, 0.35);
                text-align: center;
                animation: fadeInAuth 0.3s ease-out;
            ">
                <style>
                    @keyframes fadeInAuth { from { opacity: 0; transform: scale(0.96); } to { opacity: 1; transform: scale(1); } }
                    @keyframes shakeAuth { 0%, 100% { transform: translateX(0); } 20%, 60% { transform: translateX(-6px); } 40%, 80% { transform: translateX(6px); } }
                </style>
                
                <div style="margin-bottom: 1.25rem;">
                    <img src="assets/escuela_tecnica_superior.png" alt="Escuela Técnica Superior" style="height: 48px; margin: 0 auto 0.75rem auto; object-fit: contain;">
                    <div style="display: inline-block; padding: 0.25rem 0.75rem; border-radius: 9999px; background: rgba(34, 55, 109, 0.08); border: 1px solid rgba(34, 55, 109, 0.15); font-size: 0.7rem; font-weight: 700; color: #22376D; text-transform: uppercase; letter-spacing: 0.05em;">
                        Fundación Kinal • Acceso Restringido
                    </div>
                </div>

                <h2 style="font-family: 'Times New Roman', Times, serif; font-size: 1.5rem; font-weight: 900; color: #152244; margin: 0 0 0.5rem 0; line-height: 1.25;">
                    Revisión y Auditoría Curricular
                </h2>
                <p style="font-size: 0.82rem; color: #64748B; margin: 0 0 1.5rem 0; line-height: 1.45;">
                    Este contenido está reservado para el cuerpo docente y directivo. Ingrese la contraseña institucional para desbloquear el portal.
                </p>

                <form id="kinal-auth-form" style="margin: 0;">
                    <div style="margin-bottom: 1rem; text-align: left;">
                        <label for="kinal-pass-input" style="display: block; font-size: 0.75rem; font-weight: 700; color: #334155; margin-bottom: 0.4rem; text-transform: uppercase; letter-spacing: 0.04em;">
                            Contraseña de Seguridad
                        </label>
                        <div style="position: relative;">
                            <input type="password" id="kinal-pass-input" autocomplete="current-password" required placeholder="Ingrese la contraseña..." style="
                                width: 100%;
                                padding: 0.75rem 1rem;
                                border-radius: 0.75rem;
                                border: 1.5px solid #CBD5E1;
                                font-size: 0.95rem;
                                color: #0F172A;
                                outline: none;
                                box-sizing: border-box;
                                transition: border-color 0.2s, box-shadow 0.2s;
                            ">
                        </div>
                        <div id="kinal-auth-error" style="color: #DC2626; font-size: 0.76rem; font-weight: 700; margin-top: 0.45rem; display: none;">
                            ⚠️ Contraseña incorrecta. Intente nuevamente.
                        </div>
                    </div>

                    <button type="submit" id="kinal-auth-btn" style="
                        width: 100%;
                        padding: 0.8rem 1.25rem;
                        background: #22376D;
                        color: #FFFFFF;
                        border: none;
                        border-radius: 0.75rem;
                        font-size: 0.88rem;
                        font-weight: 800;
                        cursor: pointer;
                        box-shadow: 0 4px 6px -1px rgba(34, 55, 109, 0.25);
                        transition: background-color 0.2s, transform 0.1s;
                    ">
                        Desbloquear Contenido
                    </button>
                </form>

                <div style="margin-top: 1.5rem; padding-top: 1rem; border-top: 1px solid #E2E8F0; font-size: 0.72rem; color: #94A3B8;">
                    Ideario Institucional: <em>«El trabajo bien hecho»</em> • Ciclo 2026
                </div>
            </div>
        `;

        document.body.appendChild(overlay);

        const form = document.getElementById('kinal-auth-form');
        const passInput = document.getElementById('kinal-pass-input');
        const errorMsg = document.getElementById('kinal-auth-error');
        const cardBox = overlay.querySelector('div');

        // Focus al campo
        setTimeout(() => passInput.focus(), 100);

        form.addEventListener('submit', async function(e) {
            e.preventDefault();
            const entered = passInput.value;
            if (!entered) return;

            const isValid = await verifyPassword(entered);
            if (isValid) {
                // Autenticación correcta
                sessionStorage.setItem(AUTH_KEY, AUTH_TOKEN);
                errorMsg.style.display = 'none';
                
                // Desvanecer overlay
                overlay.style.transition = 'opacity 0.2s ease-out';
                overlay.style.opacity = '0';
                setTimeout(() => {
                    if (overlay.parentNode) overlay.parentNode.removeChild(overlay);
                    if (lockStyle.parentNode) lockStyle.parentNode.removeChild(lockStyle);
                }, 200);
            } else {
                // Error de autenticación
                errorMsg.style.display = 'block';
                passInput.value = '';
                passInput.style.borderColor = '#DC2626';
                cardBox.style.animation = 'shakeAuth 0.35s ease-in-out';
                setTimeout(() => {
                    cardBox.style.animation = '';
                    passInput.focus();
                }, 350);
            }
        });
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initAuthModal);
    } else {
        initAuthModal();
    }
})();
