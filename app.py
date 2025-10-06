import streamlit as st
import google.generativeai as genai

st.set_page_config(
    page_title="TikTok Script Generator",
    page_icon="🎬",
    layout="wide"
)

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
    tema = st.text_area("📝 Tema (em português)", placeholder="Ex: A história sombria por trás do McDonald's", height=150)

with col2:
    roteiro_exemplo = st.text_area("📄 Roteiro Pronto (opcional)", placeholder="Se já tem um roteiro em português, cole aqui.", height=150)

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
            prompt = f"""
Você é um especialista em criar conteúdo viral para TikTok voltado para o público AMERICANO.

ROTEIRO ORIGINAL (português):
{roteiro_exemplo}

REGRAS:
- O SCRIPT deve ter EXATAMENTE entre 1300-1500 caracteres (OBRIGATÓRIO)

FORMATO:

SCRIPT|||
[Script em inglês, formatado para ElevenLabs com [PAUSE], [EMPHASIS], [BREATH]. Gancho viral nos primeiros 3 segundos. 1300-1500 CARACTERES]

PROMPTS|||
0-5s: Cinematic [descrição ULTRA detalhada: composição (rule of thirds/centered/asymmetric), lighting (golden hour/neon/rim lighting/shadows), camera angle (low angle/bird's eye/dutch tilt/POV), mood (tense/mysterious/nostalgic), cores (warm amber/cold blue/high contrast), texturas (grainy/smooth/rough), movimento (zoom in/dolly/handheld)]. Hyper-realistic, 4K, professional color grading.

5-10s: Cinematic [descrição ultra detalhada com todos elementos]. Hyper-realistic, 4K, professional color grading.

10-15s: Cinematic [descrição ultra detalhada com todos elementos]. Hyper-realistic, 4K, professional color grading.

15-20s: Cinematic [descrição ultra detalhada com todos elementos]. Hyper-realistic, 4K, professional color grading.

20-25s: Cinematic [descrição ultra detalhada com todos elementos]. Hyper-realistic, 4K, professional color grading.

25-30s: Cinematic [descrição ultra detalhada com todos elementos]. Hyper-realistic, 4K, professional color grading.

30-35s: Cinematic [descrição ultra detalhada com todos elementos]. Hyper-realistic, 4K, professional color grading.

35-40s: Cinematic [descrição ultra detalhada com todos elementos]. Hyper-realistic, 4K, professional color grading.

40-45s: Cinematic [descrição ultra detalhada com todos elementos]. Hyper-realistic, 4K, professional color grading.

45-50s: Cinematic [descrição ultra detalhada com todos elementos]. Hyper-realistic, 4K, professional color grading.

50-55s: Cinematic [descrição ultra detalhada com todos elementos]. Hyper-realistic, 4K, professional color grading.

55-60s: Cinematic [descrição ultra detalhada com todos elementos]. Hyper-realistic, 4K, professional color grading.

DESCRIPTION|||
[Descrição 150-200 chars para TikTok, call-to-action americano]

[8-10 hashtags trending EUA separados por espaço, mix virais e específicos]
"""
        else:
            prompt = f"""
Você é um especialista em criar conteúdo VIRAL para TikTok voltado para o público AMERICANO.

TEMA (português): {tema}

REGRAS:
- O SCRIPT deve ter EXATAMENTE entre 1300-1500 caracteres (OBRIGATÓRIO)
- Estilo VIRAL: gancho forte, curiosidade, storytelling

FORMATO:

SCRIPT|||
[Script completo em inglês, formatado para ElevenLabs com [PAUSE], [EMPHASIS], [BREATH]. Gancho viral nos primeiros 3 segundos. Linguagem simples para público americano. 1300-1500 CARACTERES]

PROMPTS|||
0-5s: Cinematic [descrição ULTRA detalhada: composição (rule of thirds/centered/asymmetric), lighting (golden hour/neon/rim lighting/shadows), camera angle (low angle/bird's eye/dutch tilt/POV), mood (tense/mysterious/nostalgic), cores (warm amber/cold blue/high contrast), texturas (grainy/smooth/rough), movimento (zoom in/dolly/handheld)]. Hyper-realistic, 4K, professional color grading.

5-10s: Cinematic [descrição ultra detalhada com todos elementos visuais]. Hyper-realistic, 4K, professional color grading.

10-15s: Cinematic [descrição ultra detalhada com todos elementos visuais]. Hyper-realistic, 4K, professional color grading.

15-20s: Cinematic [descrição ultra detalhada com todos elementos visuais]. Hyper-realistic, 4K, professional color grading.

20-25s: Cinematic [descrição ultra detalhada com todos elementos visuais]. Hyper-realistic, 4K, professional color grading.

25-30s: Cinematic [descrição ultra detalhada com todos elementos visuais]. Hyper-realistic, 4K, professional color grading.

30-35s: Cinematic [descrição ultra detalhada com todos elementos visuais]. Hyper-realistic, 4K, professional color grading.

35-40s: Cinematic [descrição ultra detalhada com todos elementos visuais]. Hyper-realistic, 4K, professional color grading.

40-45s: Cinematic [descrição ultra detalhada com todos elementos visuais]. Hyper-realistic, 4K, professional color grading.

45-50s: Cinematic [descrição ultra detalhada com todos elementos visuais]. Hyper-realistic, 4K, professional color grading.

50-55s: Cinematic [descrição ultra detalhada com todos elementos visuais]. Hyper-realistic, 4K, professional color grading.

55-60s: Cinematic [descrição ultra detalhada com todos elementos visuais]. Hyper-realistic, 4K, professional color grading.

DESCRIPTION|||
[Descrição 150-200 chars engajante para TikTok, call-to-action americano forte]

[8-10 hashtags trending EUA incluindo #fyp #viral e específicos do tema]
"""
        
        with st.spinner("🤖 Gerando seu conteúdo viral..."):
            response = model.generate_content(prompt)
            resultado = response.text
        
        try:
            partes = resultado.split("|||")
            script = partes[1].strip() if len(partes) > 1 else ""
            prompts_raw = partes[2].strip() if len(partes) > 2 else ""
            description_full = partes[3].strip() if len(partes) > 3 else ""
            prompts_list = [p.strip() for p in prompts_raw.split('\n') if p.strip()]
        except:
            st.error("Erro ao processar resposta. Tente novamente.")
            st.stop()
        
        char_count = len(script)
        
        if char_count < 1300:
            st.warning(f"⚠️ Script muito curto ({char_count} chars). Gerando novamente...")
            st.rerun()
        elif char_count > 1500:
            script = script[:1500].rsplit('.', 1)[0] + '.'
            char_count = len(script)
        
        st.success("✅ Conteúdo gerado com sucesso!")
        
        col_counter1, col_counter2, col_counter3 = st.columns(3)
        with col_counter1:
            st.metric("📊 Caracteres", f"{char_count}", delta=f"{char_count - 1300} do mínimo" if char_count < 1400 else "Perfeito!")
        with col_counter2:
            st.metric("⏱️ Duração", "~60s")
        with col_counter3:
            status = "✅ Aprovado" if 1300 <= char_count <= 1500 else "⚠️ Fora do range"
            st.metric("Status", status)
        
        st.markdown("---")
        
        st.markdown("### 🎙️ SCRIPT (ElevenLabs Ready)")
        st.markdown('<div class="script-box">', unsafe_allow_html=True)
        st.markdown(script.replace("[PAUSE]", "**[PAUSE]**").replace("[EMPHASIS]", "**[EMPHASIS]**").replace("[BREATH]", "**[BREATH]**"))
        st.markdown('</div>', unsafe_allow_html=True)
        st.code(script, language="text")
        
        st.markdown("---")
        
        st.markdown("### 🎨 IMAGE PROMPTS")
        for idx, prompt_line in enumerate(prompts_list):
            if ':' in prompt_line:
                timestamp = prompt_line.split(':', 1)[0]
                prompt_content = prompt_line.split(':', 1)[1].strip()
                
                st.markdown(f"**⏱️ {timestamp}**")
                st.markdown('<div class="prompt-box">', unsafe_allow_html=True)
                st.markdown(prompt_content)
                st.markdown('</div>', unsafe_allow_html=True)
                st.code(prompt_content, language="text")
                st.markdown("")
        
        st.markdown("---")
        
        st.markdown("### 📝 DESCRIPTION + HASHTAGS")
        st.markdown('<div class="description-box">', unsafe_allow_html=True)
        st.markdown(description_full)
        st.markdown('</div>', unsafe_allow_html=True)
        st.code(description_full, language="text")
        
        texto_completo = f"""🎬 TIKTOK SCRIPT GENERATOR
{'='*60}

📊 INFORMAÇÕES:
- Caracteres: {char_count}
- Duração: ~60 segundos
- Público: Americano

{'='*60}

🎙️ SCRIPT
{'-'*60}
{script}

{'='*60}

🎨 IMAGE PROMPTS
{'-'*60}
{prompts_raw}

{'='*60}

📝 DESCRIPTION + HASHTAGS
{'-'*60}
{description_full}
"""
        
        st.markdown("---")
        st.download_button(
            label="📥 Download Completo (.txt)",
            data=texto_completo,
            file_name=f"tiktok_script_{char_count}chars.txt",
            mime="text/plain",
            use_container_width=True
        )
    
    except Exception as e:
        st.error(f"❌ Erro: {str(e)}")
        st.info("💡 Verifique sua API Key")

st.markdown("---")
st.markdown("Made with ❤️ for viral TikTok content | Powered by Google Gemini 2.0 Flash")
