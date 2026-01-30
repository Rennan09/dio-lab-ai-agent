import json
import pandas as pd
import requests
import streamlit as st
from datetime import datetime
from pathlib import Path

OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "gpt-oss"
DATA_DIR = Path("./data")
HISTORICO_FILE = DATA_DIR / "historico_chat.json"

SYSTEM_PROMPT = """
Você é um agente financeiro inteligente de apoio e motivação financeira.

REGRAS ABSOLUTAS:
- Responda SOMENTE com base nas informações fornecidas no CONTEXTO
- NÃO invente dados, valores, projeções ou conclusões
- Se algo não estiver claro no contexto, diga explicitamente
- Não tome decisões financeiras pelo usuário
- Não recomende produtos sem contexto suficiente
"""

VALIDATION_PROMPT = """
Analise a resposta abaixo e verifique:

1. Existe alguma informação que NÃO esteja no contexto fornecido?
2. Existe alguma suposição ou conclusão não suportada pelos dados?
3. Existe alguma recomendação financeira direta?

Responda APENAS com:
- "APROVADA"
ou
- "REJEITADA: <motivo>"
"""

def carregar_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def carregar_csv(path):
    return pd.read_csv(path)

def carregar_historico():
    if HISTORICO_FILE.exists():
        return carregar_json(HISTORICO_FILE)
    return []

def salvar_historico(historico):
    with open(HISTORICO_FILE, "w", encoding="utf-8") as f:
        json.dump(historico, f, indent=2, ensure_ascii=False)

perfil = carregar_json(DATA_DIR / "perfil_investidor.json")
transacoes = carregar_csv(DATA_DIR / "transacoes.csv")
produtos = carregar_json(DATA_DIR / "produtos_financeiros.json")
historico_chat = carregar_historico()

def montar_contexto():
    ultimas_interacoes = historico_chat[-5:]

    return f"""
CLIENTE:
Nome: {perfil['nome']}
Idade: {perfil['idade']}
Perfil: {perfil['perfil_investidor']}
Objetivo: {perfil['objetivo_principal']}
Patrimônio: R$ {perfil['patrimonio_total']}
Reserva de Emergência: R$ {perfil['reserva_emergencia_atual']}

TRANSAÇÕES RECENTES:
{transacoes.tail(10).to_string(index=False)}

PRODUTOS DISPONÍVEIS:
{json.dumps(produtos, indent=2, ensure_ascii=False)}

HISTÓRICO DE CONVERSA:
{json.dumps(ultimas_interacoes, indent=2, ensure_ascii=False)}
"""


def chamar_llm(prompt):
    response = requests.post(
        OLLAMA_URL,
        json={"model": MODELO, "prompt": prompt, "stream": False},
        timeout=60
    )
    response.raise_for_status()
    return response.json()["response"].strip()

def perguntar(msg):
    contexto = montar_contexto()

    prompt_principal = f"""
{SYSTEM_PROMPT}

CONTEXTO:
{contexto}

PERGUNTA DO USUÁRIO:
{msg}
"""

    resposta = chamar_llm(prompt_principal)

    validacao_prompt = f"""
CONTEXTO:
{contexto}

RESPOSTA:
{resposta}

{VALIDATION_PROMPT}
"""
    validacao = chamar_llm(validacao_prompt)

    if not validacao.startswith("APROVADA"):
        return (
            "Não tenho informações suficientes no contexto para responder isso com segurança. "
            "Podemos revisar os dados juntos ou você pode me fornecer mais detalhes."
        )

    historico_chat.append({
        "timestamp": datetime.utcnow().isoformat(),
        "usuario": msg,
        "assistente": resposta
    })
    salvar_historico(historico_chat)

    return resposta

st.set_page_config(page_title="Sup • Assistente Financeiro", layout="centered")
st.title("🤝 Sup — Seu ajudante de finanças")

for item in historico_chat[-10:]:
    st.chat_message("user").write(item["usuario"])
    st.chat_message("assistant").write(item["assistente"])

if pergunta := st.chat_input("Digite sua pergunta financeira..."):
    st.chat_message("user").write(pergunta)
    with st.spinner("Pensando..."):
        resposta = perguntar(pergunta)
        st.chat_message("assistant").write(resposta)
