import streamlit as st
import google.generativeai as genai
import os

# Configuração da página
st.set_page_config(
    page_title="TikTok Script Generator",
    page_icon="🎬",
    layout="wide"
)

# Título
st.title("🎬 TikTok Script Generator")
st.markdown("**Gere roteiros virais em inglês + Image Prompts + Descrição + Hashtags**")

# Sidebar para API Key
with st.sidebar:
    st.header("⚙️ Configuração")
    api_key = st.text_input("Google Gemini API Key", type="password", help="Cole sua API key aqui")
    st.markdown("[📖 Como pegar API Key](https://aistudio.google.com/apikey)")

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

ENTREGUE:

1. **SCRIPT EM INGLÊS** (1300-1500 caracteres):
   - Tradução adaptada para público americano
   - Linguagem simples e conversacional
   - Formatado para ElevenLabs com marcações de pausa [PAUSE], ênfase [EMPHASIS], etc
   - Gancho viral nos primeiros 3 segundos

2. **IMAGE PROMPTS** (para cada trecho de 5-10 segundos):
   - Prompts detalhados para geração de imagens/vídeo
   - Formato: "0-5s: [prompt]", "5-12s: [prompt]"
   - Cinematográfico e chamativo

3. **DESCRIPTION** (para TikTok):
   - 150-200 caracteres
   - Call-to-action americano
   - Engajante

4. **HASHTAGS**:
   - 8-10 hashtags trending nos EUA
   - Mix de virais e nichos

FORMATE A RESPOSTA EXATAMENTE ASSIM:

🎙️ SCRIPT (ElevenLabs Ready)
━━━━━━━━━━━━━━━━━━━━━━━━━━
[script aqui com marcações]

🎨 IMAGE PROMPTS
━━━━━━━━━━━━━━━━━━━━━━━━━━
0-5s: [prompt]
5-12s: [prompt]
[continue...]

📝 DESCRIPTION
━━━━━━━━━━━━━━━━━━━━━━━━━━
[descrição aqui]

#️⃣ HASHTAGS
━━━━━━━━━━━━━━━━━━━━━━━━━━
[hashtags aqui]
"""
        else:
            prompt = f"""
Você é um especialista em criar conteúdo VIRAL para TikTok voltado para o público AMERICANO.

TEMA (em português): {tema}

CRIE UM ROTEIRO COMPLETO:

1. **SCRIPT EM INGLÊS** (1300-1500 caracteres):
   - Estilo VIRAL (gancho forte, curiosidade, storytelling)
   - Linguagem simples para público americano
   - Formatado para ElevenLabs com marcações [PAUSE], [EMPHASIS], etc
   - Gancho viral nos primeiros 3 segundos
   - Duração: ~60 segundos

2. **IMAGE PROMPTS** (para cada trecho de 5-10 segundos):
   - Prompts detalhados para geração de imagens/vídeo
   - Formato: "0-5s: [prompt]", "5-12s: [prompt]"
   - Cinematográfico e impactante

3. **DESCRIPTION** (para TikTok):
   - 150-200 caracteres
   - Call-to-action americano
   - Engajante e clicável

4. **HASHTAGS**:
   - 8-10 hashtags trending nos EUA
   - Mix de virais (#fyp, #viral) e específicos do tema

FORMATE A RESPOSTA EXATAMENTE ASSIM:

🎙️ SCRIPT (ElevenLabs Ready)
━━━━━━━━━━━━━━━━━━━━━━━━━━
[script aqui com marcações]

🎨 IMAGE PROMPTS
━━━━━━━━━━━━━━━━━━━━━━━━━━
0-5s: [prompt]
5-12s: [prompt]
[continue...]

📝 DESCRIPTION
━━━━━━━━━━━━━━━━━━━━━━━━━━
[descrição aqui]

#️⃣ HASHTAGS
━━━━━━━━━━━━━━━━━━━━━━━━━━
[hashtags aqui]
"""
        
        # Gerar com loading
        with st.spinner("🤖 Gerando seu conteúdo viral..."):
            response = model.generate_content(prompt)
            resultado = response.text
        
        # Exibir resultado
        st.success("✅ Conteúdo gerado com sucesso!")
        st.markdown("---")
        st.markdown(resultado)
        
        # Botão de download
        st.download_button(
            label="📥 Download do Conteúdo",
            data=resultado,
            file_name="tiktok_script.txt",
            mime="text/plain",
            use_container_width=True
        )
        
        # Contador de caracteres do script
        if "SCRIPT" in resultado:
            script_text = resultado.split("🎨 IMAGE PROMPTS")[0]
            char_count = len(script_text.split("━━━━━━━━━━━━━━━━━━━━━━━━━━")[1].strip())
            st.info(f"📊 Script tem **{char_count} caracteres** (ideal: 1300-1500)")
    
    except Exception as e:
        st.error(f"❌ Erro: {str(e)}")
        st.info("💡 Verifique se sua API Key está correta")

# Footer
st.markdown("---")
st.markdown("Made with ❤️ for viral TikTok content | Powered by Google Gemini")
