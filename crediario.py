import streamlit as st

# Título do Site
st.title("📱  Crediário para celular ")
st.write("---")

# 1. Valor do Celular
preco_avista = st.number_input("Qual o valor à vista do celular? (R$)", min_value=0.0, step=100.0)

if preco_avista > 0:
    # 2. Recomendação de Entrada
    entradainicial = preco_avista * 0.33
    st.info(f"💡 Recomendamos uma entrada inicial de: **R$ {entradainicial:.2f}**")
    
    # 3. Campo para a Entrada
    entrada = st.number_input("Qual o valor da entrada que consegue dar?", min_value=0.0)
    
    if entrada >= entradainicial:
        st.success("✅ Valor de entrada ótimo! Vamos prosseguir.")
    else:
        st.warning("⚠️ Valor abaixo do recomendado. Vamos negociar.")

    # 4. Escolha do Pagamento
    pagamento = st.selectbox("Forma de pagamento:", ["Semanal / Quinzenal", "Mensal"])

    if "Semanal" in pagamento:
        taxa = 0.15
    else:
        taxa = 0.20

    # Cálculos
    valordojuros = preco_avista * taxa
    valorfinal = valordojuros + preco_avista
    
    st.write("---")
    st.subheader(f"Resumo do Juros: R$ {valordojuros:.2f}")
    st.header(f"Total Final: R$ {valorfinal:.2f}")

    # 5. Parcelamento
    # --- DAQUI PARA BAIXO É O QUE DEVES SUBSTITUIR ---
    st.write("---")
    st.subheader("📊 Opções de Parcelamento")

    valor_restante = valorfinal - entrada
    
    # Usamos o 'for' para criar cada linha de 1 a 5
    for i in range(1, 6):
        valor_da_parcela = valor_restante / i
        # Mostra o texto formatado: "1x de R$ 100.00", "2x de R$ 50.00", etc.
        st.write(f"**{i}x** de **R$ {valor_da_parcela:.2f}**")

    st.caption("⚠️ O parcelamento máximo permitido é de 5 vezes.")
