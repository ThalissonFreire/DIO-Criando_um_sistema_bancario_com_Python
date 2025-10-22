# 💰 Sistema Bancário em Python  
**Desafio de Projeto – DIO | Python Developer – Suzano**  
**Autor:** Thalisson Freire  

---

## 🧠 Sobre o Projeto
Este projeto foi desenvolvido como parte do **Bootcamp Python Developer (Suzano)** da [Digital Innovation One (DIO)](https://www.dio.me/).  
O desafio propõe a criação de um **sistema bancário simples**, com as operações fundamentais de **depósito**, **saque** e **extrato**, utilizando apenas os recursos básicos da linguagem Python.

O objetivo é consolidar o entendimento sobre **entrada e saída de dados**, **estruturas condicionais** e **laços de repetição**, sem o uso de coleções, funções ou orientação a objetos.

---

## 🎯 Objetivos do Desafio

- Implementar as operações básicas de um sistema bancário:
  - **Depósito:** aceitar apenas valores positivos e armazenar no extrato.  
  - **Saque:** permitir até **3 saques por sessão**, com limite de **R$ 500,00 por operação**, respeitando o saldo disponível.  
  - **Extrato:** listar todos os depósitos e saques realizados, além de exibir o saldo atual formatado em `R$ xxx.xx`.

---

## ⚙️ Funcionalidades Implementadas

| Função | Descrição |
|:--|:--|
| **Depósito** | Permite adicionar valores positivos ao saldo. Registra a operação no extrato. Inclui tratamento de erro para entradas inválidas. |
| **Saque** | Permite até 3 saques por sessão, com valor máximo de R$ 500,00. Verifica saldo e valida entrada numérica. |
| **Extrato** | Mostra todas as movimentações registradas e o saldo atual formatado. |
| **Sair** | Encerra o programa com mensagem de agradecimento. |

---

## 💡 Decisões Técnicas

- O controle de **limite de 3 saques** é feito **por sessão**.  
  > O desafio cita “3 saques diários”, mas como o curso abordou apenas sintaxe básica (sem manipulação de datas), nesta versão o controle é feito durante a execução do programa.  
- Os valores monetários são armazenados como `float` para simplicidade.  
  > Em versões futuras, a classe `Decimal` pode ser utilizada para maior precisão.  
- O **extrato** é armazenado em uma **string**, concatenando todas as operações.  
  > Essa abordagem é compatível com o escopo do módulo (sem listas ou dicionários).

---

## 🧾 Exemplo de Uso

```bash
[1] - Depositar
[2] - Sacar
[3] - Extrato
[4] - Sair
=> 1

Opção selecionada: Depósito
Informe o valor a ser depositado:
=> R$ 100
Depósito de R$ 100.00 realizado com sucesso!
Seu novo saldo é de R$ 100.00
