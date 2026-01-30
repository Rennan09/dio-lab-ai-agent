import json
import pandas as pd
import requests
import streamlit as st


OLLAMA_URL = "https://localhost:11434/api/generate"
MODELO = "gpt-oss"

perfil = json.load(open("./data/perfil_investidor.json"))
transacoes = json.load(open("./data/transacoes.csv"))
historico = json.load(open("./data/historico_atendimento.csv"))
produtos = json.load(open("./data/produtos_financeiros.json"))

contexto = f"""
CLIENTE: {perfil["nome"]}, {perfil["idade"]}, anos, perfil {perfil["perfil_investidor"]}
OBJETIVO: {perfil["objetivo_principal"]}, 
PATRIMÔNIO: R$ {perfil["patrimonio_total"]} | RESERVA: R$ {perfil["reserva_emergencia_atual"]}

TRANSAÇÕES RECENTES:
{transacoes.to_string(index=False)}

ATENDIMENTOS ANTERIORES:
{historico.to_string(index=False)}

PRODUTOS DISPONÍVEIS:
{json.dumps(produtos, indent=2, ensure_ascii=False)}

"""

SYSTEM_PROMPT = """Você é um agente financeiro inteligente de apoio e motivação financeira, especializado em organização financeira pessoal, planejamento de metas e conscientização financeira.

Seu objetivo é auxiliar usuários que se sentem desmotivados, sobrecarregados ou sem tempo para cuidar da própria vida financeira, ajudando-os a refletir sobre gestão de tempo, organização financeira, planejamento de metas, quitação de dívidas, reserva de emergência e importância do acompanhamento financeiro, removendo o peso psicológico associado a essas tarefas.

Você NÃO resolve problemas financeiros diretamente, NÃO toma decisões pelo usuário e NÃO executa ações financeiras. Você atua apenas como um apoio temporário, oferecendo conscientização, motivação e direcionamento. As decisões finais sempre pertencem ao usuário.
"""

def perguntar(msg):
    prompt = f"""
{SYSTEM_PROMPT}

CONTEXTO DO CLIENTE:
{contexto}

PERGUNTA: {msg}"""
    
    r = requests.post(OLLAMA_URL, json={"model": MODELO, "prompt": prompt, "stream": False })
    return r.json()["response"]

st.title("Sup, seu ajudante de finanças")

if pergunta  := st.chat_input("Sua questão sobre finanças..."):
    st.chat_message("user").write(pergunta)
    with st.spinner("..."):
        st.chat_message("assistant").write(perguntar(pergunta))

