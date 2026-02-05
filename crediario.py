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
    parcela = st.slider("Em quantas parcelas deseja dividir?", 1, 10, 5)

    if parcela <= 5:
        valor_restante = valorfinal - entrada
        valor_da_parcela = valor_restante / parcela
        st.metric("Valor de cada parcela", f"R$ {valor_da_parcela:.2f}")
    else:
        st.error("❌ Não podemos fazer em mais de 5 parcelas.")

