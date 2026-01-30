# Sup 🤝💰  
### Seu ajudante inteligente de organização e motivação financeira

O **Sup** é um agente financeiro inteligente focado em **apoio, conscientização e motivação financeira**, criado para ajudar pessoas que se sentem sobrecarregadas, desmotivadas ou sem tempo para cuidar da própria vida financeira.

Diferente de soluções que apenas recomendam produtos ou tomam decisões automáticas, o Sup atua como um **companheiro financeiro consciente**, ajudando o usuário a entender sua realidade financeira, refletir sobre prioridades e reduzir o peso psicológico associado ao planejamento financeiro.

---

## ✨ Visão Geral

- 💬 Interface conversacional simples (chat)
- 🧠 LLM local via **Ollama** (privacidade total dos dados)
- 📊 Uso de dados reais do usuário (perfil, transações, histórico)
- 🛑 Sem decisões automáticas ou execução de operações financeiras
- 🎯 Foco em educação, reflexão e autonomia financeira


---

## ❗ O Problema

Muitas pessoas possuem acesso a dados financeiros — extratos, históricos, produtos — mas:

- Não conseguem transformá-los em clareza
- Sentem ansiedade ao lidar com dinheiro
- Adiam constantemente o planejamento financeiro
- Têm medo de tomar decisões erradas

O problema não é falta de informação.  
É **falta de orientação contextualizada, responsável e humana**.

---

## ✅ A Solução

O **Sup** centraliza e contextualiza informações financeiras do usuário para responder perguntas de forma clara, responsável e personalizada.

Ele:
- Analisa o contexto financeiro completo do usuário
- Estimula reflexão sobre tempo, metas e decisões
- Ajuda a quebrar o mito de que planejamento financeiro é “tempo perdido”
- Atua como apoio motivacional, nunca como decisor

> ⚠️ O Sup **não executa operações financeiras**, **não recomenda investimentos sem contexto** e **não substitui profissionais**.

---

## 🧠 Como Funciona

O agente constrói um **contexto único por usuário**, combinando:

- Perfil do investidor (`perfil_investidor.json`)
- Histórico de transações (`transacoes.csv`)
- Atendimentos anteriores (`historico_atendimento.csv`)
- Produtos financeiros disponíveis (`produtos_financeiros.json`)

Esse contexto é enviado junto ao **System Prompt** para o modelo local no Ollama, garantindo respostas:

- Baseadas apenas nos dados fornecidos
- Sem alucinações
- Alinhadas às limitações do agente

---

## 🧩 Tecnologias Utilizadas

- **Python**
- **Streamlit** – Interface web
- **Ollama** – Execução local de LLM
- **Requests** – Comunicação HTTP
- **Pandas** – Manipulação de dados
- **JSON / CSV** – Persistência de dados

---

## 🔐 Princípios de Segurança e Ética

- 🔒 Execução local do modelo (privacidade)
- ❌ Nenhuma informação sensível é solicitada
- ❌ Nenhuma decisão financeira é tomada pelo agente
- 📚 Respostas baseadas apenas nos dados fornecidos
- 🧠 Incentivo constante à verificação das informações

---

## 🧭 Limitações Declaradas

O Sup:
- Não resolve problemas financeiros de forma definitiva
- Não executa operações bancárias
- Não fornece aconselhamento financeiro personalizado sem contexto
- Não substitui um consultor financeiro

Ele é um **apoio temporário e educativo**, um “empurrãozinho” para quem precisa retomar o controle da própria vida financeira.

---

## ▶️ Executando o Projeto

### Pré-requisitos
- Python 3.10+
- Ollama instalado e rodando localmente
- Modelo configurado no Ollama (ex: `gpt-oss`)

### Instalação
bash
pip install -r requirements.txt

## Execução
streamlit run app.py

##📌 Exemplo de Uso

Usuário:

"Não tenho tempo para organizar minhas finanças."

Sup:

"Entendo essa sensação. Podemos avaliar juntos quanto tempo seria necessário para organizar o básico e refletir se esse tempo é maior do que parece. Você prefere começar por gastos, dívidas ou metas?"

##🚀 Impacto

O Sup busca tornar o planejamento financeiro:

Mais acessível

Menos intimidador

Mais humano

Mais consciente

Acreditamos que educação financeira começa pela clareza, não pela pressão.

## 📄 Licença

Este projeto é open-source e pode ser adaptado para fins educacionais, acadêmicos ou experimentais.

## 🤝 Contribuições

Contribuições são bem-vindas!
Sinta-se à vontade para abrir issues, sugerir melhorias ou enviar pull requests.

