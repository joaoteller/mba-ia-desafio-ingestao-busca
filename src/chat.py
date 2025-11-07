from search import search_prompt


def main():
    chain = search_prompt()

    if not chain:
        print("Não foi possível iniciar o chat. Verifique os erros de inicialização.")
        return

    print("\n" + "=" * 50)
    print("Chat RAG com PDF (PostgreSQL + LangChain)")
    print(
        "Faça sua pergunta sobre o conteúdo do PDF carregado. Digite 'sair' para encerrar."
    )
    print("=" * 50 + "\n")

    while True:
        try:
            user_question = input("Faça sua pergunta: ")

            if user_question.lower().strip() == "sair":
                print("Encerrando o chat. Até mais!")
                break

            if not user_question.strip():
                print("Por favor, insira uma pergunta válida.")
                continue

            # invocando a chain
            answer = chain.invoke(user_question)

            print(f"\nResposta: {answer}\n")
            print("-" * 50 + "\n")
        except Exception as e:
            print(f"Erro ao processar a pergunta: {str(e)}")


if __name__ == "__main__":
    main()
