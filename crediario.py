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
    st.subheader("📊 Simulação de Parcelamento")

    valor_restante = valorfinal - entrada
    
    # Criamos as colunas para mostrar as 5 opções de uma vez
    col1, col2, col3, col4, col5 = st.columns(5)
    
    # Lista com as colunas para facilitar o laço 'for'
    colunas = [col1, col2, col3, col4, col5]

    for i in range(1, 6):
        valor_da_parcela = valor_restante / i
        with colunas[i-1]:
            st.metric(label=f"{i}x", value=f"R$ {valor_da_parcela:.2f}")

    st.caption("⚠️ Nota: O parcelamento máximo é de 5x conforme a política da loja.")
