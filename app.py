import streamlit as st
import google.generativeai as genai
import os

st.set_page_config(page_title="TikTok Script Generator", page_icon="🎬", layout="wide")

st.markdown("""
<style>
    .script-box {
        background-color: #1E1E1E;
        padding: 20px;
        border-radius: 10px;
        border-left: 4px solid #FF0050;
        margin: 10px 0;
    }
    .prompt-box {
        background-color: #2D2D2D;
        padding: 15px;
        border-radius: 10px;
        border-left: 4px solid #00D9FF;
        margin: 10px 0;
    }
    .description-box {
        background-color: #1E1E1E;
        padding: 15px;
        border-radius: 10px;
        border-left: 4px solid #00FF88;
        margin: 10px 0;
    }
</style>
""", unsafe_allow_html=True)

st.title("🎬 TikTok Script Generator")
st.markdown("**Gere roteiros virais em inglês + Image Prompts + Descrição + Hashtags**")

with st.sidebar:
    st.header("⚙️ Configuração")
    api_key = st.text_input("Google Gemini API Key", type="password", help="Cole sua API key aqui")
    st.markdown("[📖 Como pegar API Key](https://aistudio.google.com/apikey)")
    st.markdown("---")
    st.markdown("### 📏 Especificações")
    st.info("✅ Script: 1300-1500 caracteres\n\n✅ Estilo: Viral\n\n✅ Público: Americano\n\n✅ Duração: ~60 segundos")

col1, col2 = st.columns([1, 1])

with col1:
    tema = st.text_area("📝 Tema (em português)", placeholder="Ex: A história sombria por trás do McDonald's", height=100)

with col2:
    roteiro_exemplo = st.text_area("📄 Roteiro Pronto (opcional)", placeholder="Se já tem um roteiro em português, cole aqui. Caso contrário, deixe vazio.", height=100)

if st.button("🚀 Gerar Conteúdo Completo", type="primary", use_container_width=True):
    
    if not api_key:
        st.error("⚠️ Por favor, insira sua API Key na barra lateral!")
        st.stop()
    
    if not tema and not roteiro_exemplo:
        st.error("⚠️ Insira um tema OU um roteiro pronto!")
        st.stop()
    
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-2.0-flash-exp')
        
        if roteiro_exemplo:
            prompt = f"""Você é um especialista em criar conteúdo viral para TikTok voltado para o público AMERICANO.

ROTEIRO ORIGINAL (português):
{roteiro_exemplo}

REGRAS: O SCRIPT deve ter EXATAMENTE entre 1300-1500 caracteres (OBRIGATÓRIO). Se ficar curto, adicione mais detalhes.

FORMATE EXATAMENTE ASSIM:

🎙️ SCRIPT (ElevenLabs Ready)
━━━━━━━━━━━━━━━━━━━━━━━━━━
[Script em inglês com marcações [PAUSE], [EMPHASIS], [BREATH]. Gancho viral nos primeiros 3 segundos. 1300-1500 CARACTERES]

🎨 IMAGE PROMPTS
━━━━━━━━━━━━━━━━━━━━━━━━━━
0-5s: Cinematic [descrição ULTRA detalhada: composição (rule of thirds/centered), lighting (golden hour/neon/rim lighting/shadows), camera angle (low angle/bird's eye/dutch tilt), mood (tense/mysterious), cores (warm amber/cold blue), texturas (grainy/smooth), movimento (zoom in/dolly)]. Hyper-realistic, 4K.
5-10s: Cinematic [descrição ultra detalhada completa]. Hyper-realistic, 4K.
10-15s: Cinematic [descrição ultra detalhada completa]. Hyper-realistic, 4K.
15-20s: Cinematic [descrição ultra detalhada completa]. Hyper-realistic, 4K.
20-25s: Cinematic [descrição ultra detalhada completa]. Hyper-realistic, 4K.
25-30s: Cinematic [descrição ultra detalhada completa]. Hyper-realistic, 4K.
30-35s: Cinematic [descrição ultra detalhada completa]. Hyper-realistic, 4K.
35-40s: Cinematic [descrição ultra detalhada completa]. Hyper-realistic, 4K.
40-45s: Cinematic [descrição ultra detalhada completa]. Hyper-realistic, 4K.
45-50s: Cinematic [descrição ultra detalhada completa]. Hyper-realistic, 4K.
50-55s: Cinematic [descrição ultra detalhada completa]. Hyper-realistic, 4K.
55-60s: Cinematic [descrição ultra detalhada completa]. Hyper-realistic, 4K.

📝 DESCRIPTION + HASHTAGS
━━━━━━━━━━━━━━━━━━━━━━━━━━
[Descrição 150-200 caracteres, call-to-action americano]

[8-10 hashtags trending EUA incluindo #fyp #viral]"""
        else:
            prompt = f"""Você é um especialista em criar conteúdo VIRAL para TikTok voltado para o público AMERICANO.

TEMA (português): {tema}

REGRAS: O SCRIPT deve ter EXATAMENTE entre 1300-1500 caracteres (OBRIGATÓRIO). Crie conteúdo COMPLETO e DETALHADO.

FORMATE EXATAMENTE ASSIM:

🎙️ SCRIPT (ElevenLabs Ready)
━━━━━━━━━━━━━━━━━━━━━━━━━━
[Script viral em inglês com marcações [PAUSE], [EMPHASIS], [BREATH]. Gancho forte nos primeiros 3 segundos. Linguagem simples. 1300-1500 CARACTERES]

🎨 IMAGE PROMPTS
━━━━━━━━━━━━━━━━━━━━━━━━━━
0-5s: Cinematic [descrição ULTRA detalhada: composição (rule of thirds/centered), lighting (golden hour/neon/rim lighting/shadows), camera angle (low angle/bird's eye/dutch tilt), mood (tense/mysterious), cores (warm amber/cold blue), texturas (grainy/smooth), movimento (zoom in/dolly)]. Hyper-realistic, 4K.
5-10s: Cinematic [descrição ultra detalhada completa]. Hyper-realistic, 4K.
10-15s: Cinematic [descrição ultra detalhada completa]. Hyper-realistic, 4K.
15-20s: Cinematic [descrição ultra detalhada completa]. Hyper-realistic, 4K.
20-25s: Cinematic [descrição ultra detalhada completa]. Hyper-realistic, 4K.
25-30s: Cinematic [descrição ultra detalhada completa]. Hyper-realistic, 4K.
30-35s: Cinematic [descrição ultra detalhada completa]. Hyper-realistic, 4K.
35-40s: Cinematic [descrição ultra detalhada completa]. Hyper-realistic, 4K.
40-45s: Cinematic [descrição ultra detalhada completa]. Hyper-realistic, 4K.
45-50s: Cinematic [descrição ultra detalhada completa]. Hyper-realistic, 4K.
50-55s: Cinematic [descrição ultra detalhada completa]. Hyper-realistic, 4K.
55-60s: Cinematic [descrição ultra detalhada completa]. Hyper-realistic, 4K.

📝 DESCRIPTION + HASHTAGS
━━━━━━━━━━━━━━━━━━━━━━━━━━
[Descrição 150-200 caracteres engajante, call-to-action forte]

[8-10 hashtags trending EUA incluindo #fyp #viral e específicos do tema]"""
        
        with st.spinner("🤖 Gerando seu conteúdo viral..."):
            response = model.generate_content(prompt)
            resultado = response.text
        
        try:
            script_text = resultado.split("🎨 IMAGE PROMPTS")[0].split("━━━━━━━━━━━━━━━━━━━━━━━━━━")[1].strip()
            prompts_section = resultado.split("🎨 IMAGE PROMPTS")[1].split("📝 DESCRIPTION + HASHTAGS")[0].split("━━━━━━━━━━━━━━━━━━━━━━━━━━")[1].strip()
            description_section = resultado.split("📝 DESCRIPTION + HASHTAGS")[1].split("━━━━━━━━━━━━━━━━━━━━━━━━━━")[1].strip()
        except:
            st.error("❌ Erro ao processar resposta. Tentando novamente...")
            st.stop()
        
        char_count = len(script_text)
        
        if char_count < 1300:
            st.warning(f"⚠️ Script muito curto ({char_count} caracteres). Gerando novamente...")
            st.rerun()
        elif char_count > 1500:
            script_text = script_text[:1500].rsplit('.', 1)[0] + '.'
            char_count = len(script_text)
        
        st.success("✅ Conteúdo gerado com sucesso!")
        
        col_counter1, col_counter2, col_counter3 = st.columns(3)
        with col_counter1:
            st.metric("📊 Caracteres do Script", f"{char_count}", delta=f"{char_count - 1300} do mínimo" if char_count < 1400 else "Perfeito!")
        with col_counter2:
            st.metric("⏱️ Duração Estimada", "~60s")
        with col_counter3:
            status = "✅ Aprovado" if 1300 <= char_count <= 1500 else "⚠️ Fora do range"
            st.metric("Status", status)
        
        st.markdown("---")
        
        st.markdown("### 🎙️ SCRIPT (ElevenLabs Ready)")
        st.markdown('<div class="script-box">', unsafe_allow_html=True)
        st.markdown(script_text.replace("[PAUSE]", "**[PAUSE]**").replace("[EMPHASIS]", "**[EMPHASIS]**").replace("[BREATH]", "**[BREATH]**"))
        st.markdown('</div>', unsafe_allow_html=True)
        
        with st.expander("📋 Clique para copiar o Script"):
            st.code(script_text, language="text")
        
        st.markdown("---")
        
        st.markdown("### 🎨 IMAGE PROMPTS (Sincronizados por Tempo)")
        
        prompts_lines = [line.strip() for line in prompts_section.split('\n') if line.strip()]
        
        for idx, prompt_line in enumerate(prompts_lines):
            if ':' in prompt_line:
                parts = prompt_line.split(':', 1)
                timestamp = parts[0].strip()
                prompt_content = parts[1].strip()
                
                st.markdown(f"**⏱️ {timestamp}**")
                st.markdown('<div class="prompt-box">', unsafe_allow_html=True)
                st.markdown(prompt_content)
                st.markdown('</div>', unsafe_allow_html=True)
                
                with st.expander(f"📋 Copiar prompt {timestamp}"):
                    st.code(prompt_content, language="text")
                
                st.markdown("")
        
        st.markdown("---")
        
        st.markdown("### 📝 DESCRIPTION + HASHTAGS (Copy & Paste para TikTok)")
        st.markdown('<div class="description-box">', unsafe_allow_html=True)
        st.markdown(description_section)
        st.markdown('</div>', unsafe_allow_html=True)
        
        with st.expander("📋 Copiar Description + Hashtags"):
            st.code(description_section, language="text")
        
        texto_completo = f"""🎬 TIKTOK SCRIPT GENERATOR
{'='*60}

📊 INFORMAÇÕES:
- Caracteres: {char_count}
- Duração: ~60 segundos
- Público: Americano
- Estilo: Viral

{'='*60}

🎙️ SCRIPT (ElevenLabs Ready)
{'-'*60}
{script_text}

{'='*60}

🎨 IMAGE PROMPTS
{'-'*60}
{prompts_section}

{'='*60}

📝 DESCRIPTION + HASHTAGS
{'-'*60}
{description_section}

{'='*60}
Generated by TikTok Script Generator
"""
        
        st.download_button(
            label="📥 Download Conteúdo Completo (.txt)",
            data=texto_completo,
            file_name=f"tiktok_script_{char_count}chars.txt",
            mime="text/plain",
            use_container_width=True
        )
    
    except Exception as e:
        st.error(f"❌ Erro: {str(e)}")
        st.info("💡 Verifique se sua API Key está correta ou tente novamente")

st.markdown("---")
st.markdown("Made with ❤️ for viral TikTok content | Powered by Google Gemini 2.0 Flash")
