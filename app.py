import streamlit as st
import google.generativeai as genai
import os

# Configuração da página
st.set_page_config(
    page_title="TikTok Script Generator",
    page_icon="🎬",
    layout="wide"
)

# CSS customizado para melhor visualização
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
    .hashtag-box {
        background-color: #2D2D2D;
        padding: 15px;
        border-radius: 10px;
        border-left: 4px solid #FFB800;
        margin: 10px 0;
    }
    .char-counter {
        font-size: 18px;
        font-weight: bold;
        color: #00FF88;
    }
</style>
""", unsafe_allow_html=True)

# Título
st.title("🎬 TikTok Script Generator")
st.markdown("**Gere roteiros virais em inglês + Image Prompts + Descrição + Hashtags**")

# Sidebar para API Key
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
        height=100
    )

with col2:
    roteiro_exemplo = st.text_area(
        "📄 Roteiro Pronto (opcional)",
        placeholder="Se já tem um roteiro em português, cole aqui. Caso contrário, deixe vazio.",
        height=100
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

ENTREGUE:

1. **SCRIPT EM INGLÊS** (1300-1500 caracteres):
   - Tradução adaptada para público americano
   - Linguagem simples e conversacional
   - Formatado para ElevenLabs com marcações de pausa [PAUSE], ênfase [EMPHASIS], [BREATH], etc
   - Gancho viral nos primeiros 3 segundos

2. **IMAGE PROMPTS** (para cada trecho de 5 segundos):
   - Prompts ULTRA DETALHADOS para geração de imagens/vídeo
   - Incluir: composição específica (rule of thirds, centered, asymmetric), lighting detalhado (golden hour, neon glow, rim lighting, dramatic shadows), camera angle preciso (low angle shot, bird's eye view, dutch tilt, over-the-shoulder), mood/atmosfera (tense, mysterious, nostalgic), paleta de cores específica (warm amber tones, cold blue hues, high contrast), texturas (grainy film, smooth digital, rough concrete), movimento de câmera (slow zoom in, dolly push, handheld shake)
   - Formato: "0-5s: [prompt detalhado]", "5-10s: [prompt detalhado]"
   - Cinematográfico e chamativo, hyper-realistic, 4K quality

3. **DESCRIPTION + HASHTAGS** (juntos, para copiar e colar direto no TikTok):
   - Descrição: 150-200 caracteres, call-to-action americano, engajante
   - Hashtags: 8-10 hashtags trending nos EUA (incluir #fyp #viral e específicos do tema)

FORMATE A RESPOSTA EXATAMENTE ASSIM:

🎙️ SCRIPT (ElevenLabs Ready)
━━━━━━━━━━━━━━━━━━━━━━━━━━
[script aqui com marcações]

🎨 IMAGE PROMPTS
━━━━━━━━━━━━━━━━━━━━━━━━━━
0-5s: [prompt ultra detalhado com composição, lighting, angle, mood, cores, textura, movimento]
5-10s: [prompt ultra detalhado]
10-15s: [prompt ultra detalhado]
15-20s: [prompt ultra detalhado]
20-25s: [prompt ultra detalhado]
25-30s: [prompt ultra detalhado]
30-35s: [prompt ultra detalhado]
35-40s: [prompt ultra detalhado]
40-45s: [prompt ultra detalhado]
45-50s: [prompt ultra detalhado]
50-55s: [prompt ultra detalhado]
55-60s: [prompt ultra detalhado]

📝 DESCRIPTION + HASHTAGS
━━━━━━━━━━━━━━━━━━━━━━━━━━
[descrição aqui]

[hashtags aqui separados por espaço]
"""
        else:
            prompt = f"""
Você é um especialista em criar conteúdo VIRAL para TikTok voltado para o público AMERICANO.

TEMA (em português): {tema}

CRIE UM ROTEIRO COMPLETO:

REGRAS IMPORTANTES:
- O SCRIPT deve ter EXATAMENTE entre 1300-1500 caracteres (OBRIGATÓRIO)
- Crie conteúdo COMPLETO e DETALHADO para atingir o mínimo de 1300 caracteres
- Estilo VIRAL: gancho forte, curiosidade, storytelling impactante

1. **SCRIPT EM INGLÊS** (1300-1500 caracteres):
   - Estilo VIRAL (gancho forte, curiosidade, storytelling)
   - Linguagem simples para público americano
   - Formatado para ElevenLabs com marcações [PAUSE], [EMPHASIS], [BREATH], etc
   - Gancho viral nos primeiros 3 segundos
   - Duração: ~60 segundos

2. **IMAGE PROMPTS** (para cada trecho de 5 segundos):
   - Prompts ULTRA DETALHADOS para geração de imagens/vídeo
   - Incluir: composição específica (rule of thirds, centered, asymmetric), lighting detalhado (golden hour, neon glow, rim lighting, dramatic shadows), camera angle preciso (low angle shot, bird's eye view, dutch tilt, over-the-shoulder), mood/atmosfera (tense, mysterious, nostalgic), paleta de cores específica (warm amber tones, cold blue hues, high contrast), texturas (grainy film, smooth digital, rough concrete), movimento de câmera (slow zoom in, dolly push, handheld shake)
   - Formato: "0-5s: [prompt]", "5-10s: [prompt]"
   - Cinematográfico e impactante, hyper-realistic, 4K quality

3. **DESCRIPTION + HASHTAGS** (juntos):
   - Descrição: 150-200 caracteres, call-to-action americano, engajante e clicável
   - Hashtags: 8-10 hashtags trending nos EUA (incluir #fyp #viral e específicos do tema)

FORMATE A RESPOSTA EXATAMENTE ASSIM:

🎙️ SCRIPT (ElevenLabs Ready)
━━━━━━━━━━━━━━━━━━━━━━━━━━
[script aqui com marcações]

🎨 IMAGE PROMPTS
━━━━━━━━━━━━━━━━━━━━━━━━━━
0-5s: Cinematic [prompt ultra detalhado com composição, lighting, angle, mood, cores, textura, movimento]. Hyper-realistic, 4K quality.
5-10s: Cinematic [prompt ultra detalhado]. Hyper-realistic, 4K quality.
10-15s: Cinematic [prompt ultra detalhado]. Hyper-realistic, 4K quality.
15-20s: Cinematic [prompt ultra detalhado]. Hyper-realistic, 4K quality.
20-25s: Cinematic [prompt ultra detalhado]. Hyper-realistic, 4K quality.
25-30s: Cinematic [prompt ultra detalhado]. Hyper-realistic, 4K quality.
30-35s: Cinematic [prompt ultra detalhado]. Hyper-realistic, 4K quality.
35-40s: Cinematic [prompt ultra detalhado]. Hyper-realistic, 4K quality.
40-45s: Cinematic [prompt ultra detalhado]. Hyper-realistic, 4K quality.
45-50s: Cinematic [prompt ultra detalhado]. Hyper-realistic, 4K quality.
50-55s: Cinematic [prompt ultra detalhado]. Hyper-realistic, 4K quality.
55-60s: Cinematic [prompt ultra detalhado]. Hyper-realistic, 4K quality.

📝 DESCRIPTION + HASHTAGS
━━━━━━━━━━━━━━━━━━━━━━━━━━
[descrição aqui]

[hashtags aqui separados por espaço]
"""
        
        # Gerar com loading
        with st.spinner("🤖 Gerando seu conteúdo viral..."):
            response = model.generate_content(prompt)
            resultado = response.text
        
        # Parse do resultado
        try:
            script_text = resultado.split("🎨 IMAGE PROMPTS")[0].split("━━━━━━━━━━━━━━━━━━━━━━━━━━")[1].strip()
            prompts_section = resultado.split("🎨 IMAGE PROMPTS")[1].split("📝 DESCRIPTION + HASHTAGS")[0].split("━━━━━━━━━━━━━━━━━━━━━━━━━━")[1].strip()
            description_section = resultado.split("📝 DESCRIPTION + HASHTAGS")[1].split("━━━━━━━━━━━━━━━━━━━━━━━━━━")[1].strip()
        except:
            st.error("❌ Erro ao processar resposta. Tentando novamente...")
            st.stop()
        
        # Contador de caracteres do script
        char_count = len(script_text)
        
        # Validação do tamanho
        if char_count < 1300:
            st.warning(f"⚠️ Script muito curto ({char_count} caracteres). Gerando novamente...")
            st.rerun()
        elif char_count > 1500:
            st.warning(f"⚠️ Script muito longo ({char_count} caracteres). Ajustando...")
            script_text = script_text[:1500].rsplit('.', 1)[0] + '.'
            char_count = len(script_text)
        
        # Exibir resultado
        st.success("✅ Conteúdo gerado com sucesso!")
        
        # Contador de caracteres destacado
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
        
        # SCRIPT COM BOTÃO COPIAR
        st.markdown("### 🎙️ SCRIPT (ElevenLabs Ready)")
        st.markdown('<div class="script-box">', unsafe_allow_html=True)
        st.markdown(script_text.replace("[PAUSE]", "**[PAUSE]**").replace("[EMPHASIS]", "**[EMPHASIS]**").replace("[BREATH]", "**[BREATH]**"))
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Caixa de código para copiar script
        with st.expander("📋 Clique para copiar o Script"):
            st.code(script_text, language="text")
        
        st.markdown("---")
        
        # IMAGE PROMPTS COM BOTÕES
        st.markdown("### 🎨 IMAGE PROMPTS (Sincronizados por Tempo)")
        
        # Separar prompts por linha
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
                
                # Botão copiar cada prompt
                with st.expander(f"📋 Copiar prompt {timestamp}"):
                    st.code(prompt_content, language="text")
