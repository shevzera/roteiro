import streamlit as st
import google.generativeai as genai

# Configuração da página
st.set_page_config(
    page_title="TikTok Script Generator",
    page_icon="🎬",
    layout="wide"
)

# CSS customizado
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

# Título
st.title("🎬 TikTok Script Generator")
st.markdown("**Gere roteiros virais em inglês + Image Prompts + Descrição + Hashtags**")

# Sidebar
with st.sidebar:
    st.header("⚙️ Configuração")
    api_key = st.text_input("Google Gemini API Key", type="password", help="Cole sua API key aqui")
    st.markdown("[📖 Como pegar API Key](https://aistudio.google.com/apikey)")
    
    st.markdown("---")
    st.markdown("### 📏 Especificações")
    st.info("✅ Script: 1300-1500 caracteres\n\n✅ Estilo: Viral\n\n✅ Público: Americano\n\n✅ Duração: ~60 segundos")

# Inputs principais
col1, col2 = st.columns([1, 1])

with col1:
    tema = st.text_area(
        "📝 Tema (em português)",
        placeholder="Ex: A história sombria por trás do McDonald's",
        height=150
    )

with col2:
    roteiro_exemplo = st.text_area(
        "📄 Roteiro Pronto (opcional)",
        placeholder="Se já tem um roteiro em português, cole aqui. Caso contrário, deixe vazio.",
        height=150
    )

# Botão de geração
if st.button("🚀 Gerar Conteúdo Completo", type="primary", use_container_width=True):
    
    if not api_key:
        st.error("⚠️ Por favor, insira sua API Key na barra lateral!")
        st.stop()
    
    if not tema and not roteiro_exemplo:
        st.error("⚠️ Insira um tema OU um roteiro pronto!")
        st.stop()
    
    try:
        # Configurar Gemini
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-2.0-flash-exp')
        
        # Criar prompt
        if roteiro_exemplo:
            prompt = f"""
Você é um especialista em criar conteúdo viral para TikTok voltado para o público AMERICANO.

TAREFA: Pegue este roteiro em português e faça:

ROTEIRO ORIGINAL (português):
{roteiro_exemplo}

REGRAS IMPORTANTES:
- O SCRIPT deve ter EXATAMENTE entre 1300-1500 caracteres (OBRIGATÓRIO)
- Se ficar curto, adicione mais detalhes, exemplos, ou expanda a narrativa
- Se ficar longo, não corte conteúdo importante, apenas seja mais conciso

ENTREGUE EXATAMENTE NESTE FORMATO:

SCRIPT|||
[Script completo aqui em inglês, formatado para ElevenLabs com marcações [PAUSE], [EMPHASIS], [BREATH], etc. Gancho viral nos primeiros 3 segundos. Linguagem simples e conversacional. DEVE TER 1300-1500 CARACTERES]

PROMPTS|||
0-5s: Cinematic [descrição ULTRA detalhada da cena: composição específica, tipo de lighting (ex: golden hour, neon, harsh shadows), camera angle preciso (ex: low angle, dutch tilt, POV), mood/atmosfera, paleta de cores RGB específica, texturas visíveis, movimento de câmera]. Hyper-realistic, 4K quality, dramatic lighting, professional color grading.

5-10s: Cinematic [descrição ULTRA detalhada da cena com todos os detalhes: composição, lighting, angle, mood, cores, textura, movimento]. Hyper-realistic, 4K quality, dramatic lighting, professional color grading.

10-15s: Cinematic [descrição ULTRA detalhada da cena com todos os detalhes: composição, lighting, angle, mood, cores, textura, movimento]. Hyper-realistic, 4K quality, dramatic lighting, professional color grading.

15-20s: Cinematic [descrição ULTRA detalhada da cena com todos os detalhes: composição, lighting, angle, mood, cores, textura, movimento]. Hyper-realistic, 4K quality, dramatic lighting, professional color grading.

20-25s: Cinematic [descrição ULTRA detalhada da cena com todos os detalhes: composição, lighting, angle, mood, cores, textura, movimento]. Hyper-realistic, 4K quality, dramatic lighting, professional color grading.

25-30s: Cinematic [descrição ULTRA detalhada da cena com todos os detalhes: composição, lighting, angle, mood, cores, textura, movimento]. Hyper-realistic, 4K quality, dramatic lighting, professional color grading.

30-35s: Cinematic [descrição ULTRA detalhada da cena com todos os detalhes: composição, lighting, angle, mood, cores, textura, movimento]. Hyper-realistic, 4K quality, dramatic lighting, professional color grading.

35-40s: Cinematic [descrição ULTRA detalhada da cena com todos os detalhes: composição, lighting, angle, mood, cores, textura, movimento]. Hyper-realistic, 4K quality, dramatic lighting, professional color grading.

40-45s: Cinematic [descrição ULTRA detalhada da cena com todos os detalhes: composição, lighting, angle, mood, cores, textura, movimento]. Hyper-realistic, 4K quality, dramatic lighting, professional color grading.

45-50s: Cinematic [descrição ULTRA detalhada da cena com todos os detalhes: composição, lighting, angle, mood, cores, textura, movimento]. Hyper-realistic, 4K quality, dramatic lighting, professional color grading.

50-55s: Cinematic [descrição ULTRA detalhada da cena com todos os detalhes: composição, lighting, angle, mood, cores, textura, movimento]. Hyper-realistic, 4K quality, dramatic lighting, professional color grading.

55-60s: Cinematic [descrição ULTRA detalhada da cena com todos os detalhes: composição, lighting, angle, mood, cores, textura, movimento]. Hyper-realistic, 4K quality, dramatic lighting, professional color grading.

DESCRIPTION|||
[Descrição de 150-200 caracteres para TikTok, engajante, com call-to-action americano]

[8-10 hashtags trending nos EUA separados por espaço, mix de virais e específicos do tema]
"""
        else:
            prompt = f"""
Você é um especialista em criar conteúdo VIRAL para TikTok voltado para o público AMERICANO.

TEMA (em português): {tema}

REGRAS IMPORTANTES:
- O SCRIPT deve ter EXATAMENTE entre 1300-1500 caracteres (OBRIGATÓRIO)
- Crie um roteiro COMPLETO e DETALHADO
- Se precisar, adicione contexto, exemplos, curiosidades para atingir o tamanho mínimo
- Estilo VIRAL: gancho forte, curiosidade, storytelling impactante

ENTREGUE EXATAMENTE NESTE FORMATO:

SCRIPT|||
[Script completo aqui em inglês, formatado para ElevenLabs com marcações [PAUSE], [EMPHASIS], [BREATH], etc. Gancho viral nos primeiros 3 segundos. Linguagem simples e conversacional para público americano. DEVE TER 1300-1500 CARACTERES]

PROMPTS|||
0-5s: Cinematic [descrição ULTRA detalhada da cena: composição específica (ex: rule of thirds, centered, asymmetric), tipo de lighting preciso (ex: golden hour, neon glow, rim lighting, dramatic shadows), camera angle específico (ex: low angle shot, bird's eye view, dutch tilt, over-the-shoulder), mood/atmosfera clara (ex: tense, mysterious, nostalgic), paleta de cores específica (ex: warm amber tones, cold blue hues, high contrast black and white), texturas visíveis (ex: grainy film, smooth digital, rough concrete), movimento de câmera (ex: slow zoom in, dolly push, handheld shake)]. Hyper-realistic, 4K quality, professional color grading, cinematic composition.

5-10s: Cinematic [mesma estrutura ultra detalhada com TODOS os elementos visuais específicos]. Hyper-realistic, 4K quality, professional color grading, cinematic composition.

10-15s: Cinematic [mesma estrutura ultra detalhada com TODOS os elementos visuais específicos]. Hyper-realistic, 4K quality, professional color grading, cinematic composition.

15-20s: Cinematic [mesma estrutura ultra detalhada com TODOS os elementos visuais específicos]. Hyper-realistic, 4K quality, professional color grading, cinematic composition.

20-25s: Cinematic [mesma estrutura ultra detalhada com TODOS os elementos visuais específicos]. Hyper-realistic, 4K quality, professional color grading, cinematic composition.

25-30s: Cinematic [mesma estrutura ultra detalhada com TODOS os elementos visuais específicos]. Hyper-realistic, 4K quality, professional color grading, cinematic composition.

30-35s: Cinematic [mesma estrutura ultra detalhada com TODOS os elementos visuais específicos]. Hyper-realistic, 4K quality, professional color grading, cinematic composition.

35-40s: Cinematic [mesma estrutura ultra detalhada com TODOS os elementos visuais específicos]. Hyper-realistic, 4K quality, professional color grading, cinematic composition.

40-45s: Cinematic [mesma estrutura ultra detalhada com TODOS os elementos visuais específicos]. Hyper-realistic, 4K quality, professional color grading, cinematic composition.

45-50s: Cinematic [mesma estrutura ultra detalhada com TODOS os elementos visuais específicos]. Hyper-realistic, 4K quality, professional color grading, cinematic composition.

50-55s: Cinematic [mesma estrutura ultra detalhada com TODOS os elementos visuais específicos]. Hyper-realistic, 4K quality, professional color grading, cinematic composition.

55-60s: Cinematic [mesma estrutura ultra detalhada com TODOS os elementos visuais específicos]. Hyper-realistic, 4K quality, professional color grading, cinematic composition.

DESCRIPTION|||
[Descrição de 150-200 caracteres para TikTok, engajante e clicável, com call-to-action americano forte]

[8-10 hashtags trending nos EUA separados por espaço, incluindo #fyp #viral e específicos do tema]
"""
        
        # Gerar com loading
        with st.spinner("🤖 Gerando seu conteúdo viral..."):
            response = model.generate_content(prompt)
            resultado = response.text
        
        # Parse do resultado
        try:
            partes = resultado.split("|||")
            
            script = partes[1].strip() if len(partes) > 1 else ""
            prompts_raw = partes[2].strip() if len(partes) > 2 else ""
            description_full = partes[3].strip() if len(partes) > 3 else ""
            
            # Separar prompts por linha
            prompts_list = [p.strip() for p in prompts_raw.split('\n') if p.strip()]
            
        except:
            st.error("Erro ao processar resposta. Tentando novamente...")
            st.stop()
        
        # Contador de caracteres
        char_count = len(script)
        
        # Validação do tamanho
        if char_count < 1300:
            st.warning(f"⚠️ Script muito curto ({char_count} chars). Gerando novamente...")
            st.rerun()
        elif char_count > 1500:
            st.warning(f"⚠️ Script muito longo ({char_count} chars). Ajustando...")
            script = script[:1500].rsplit('.', 1)[0] + '.'
            char_count = len(script)
        
        # Exibir resultado formatado
        st.success("✅ Conteúdo gerado com sucesso!")
        
        # Métricas
        col_counter1, col_counter2, col_counter3 = st.columns(3)
        with col_counter1:
            st.metric("📊 Caracteres do Script", f"{char_count}", 
                     delta=f"{char_count - 1300} do mínimo" if char_count < 1400 else "Perfeito!")
        with col_counter2:
            st.metric("⏱️ Duração Estimada", "~60s")
        with col_counter3:
            status = "✅ Aprovado" if 1300 <= char_count <= 1500 else "⚠️ Fora do range"
            st.metric("Status", status)
        
        st.markdown("---")
        
        # ===== SCRIPT COM BOTÃO DE COPIAR =====
        st.markdown("### 🎙️ SCRIPT (ElevenLabs Ready)")
        st.markdown('<div class="script-box">', unsafe_allow_html=True)
        st.markdown(script.replace("[PAUSE]", "**[PAUSE]**").replace("[EMPHASIS]", "**[EMPHASIS]**").replace("[BREATH]", "**[BREATH]**"))
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Botão copiar script
        st.code(script, language="text")
        
        # ===== IMAGE PROMPTS COM BOTÕES =====
        st.markdown("### 🎨 IMAGE PROMPTS (Sincronizados por Tempo)")
        
        for idx, prompt_line in enumerate(prompts_list):
            st.markdown(f"**{prompt_line.split(':')[0]}:**")
            prompt_content = ':'.join(prompt_line.split(':')[1:]).strip()
            
            # Box com o prompt
            st.markdown('<div class="prompt-box">', unsafe_allow_html=True)
            st.markdown(prompt_content)
            st.markdown('</div>', unsafe_allow_html=True)
            
            # Botão copiar cada prompt
            st.code(prompt_content, language="text")
            st.markdown("---")
        
        # ===== DESCRIPTION + HASHTAGS JUNTOS =====
        st.markdown("### 📝 DESCRIPTION + HASHTAGS (Copy & Paste para TikTok)")
        st.markdown('<div class="description-box">', unsafe_allow_html=True)
        st.markdown(description_full)
        st.markdown('</div>', unsafe
