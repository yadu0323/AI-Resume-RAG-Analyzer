from RAG.pipeline import ResumeRAGPipeline

pipeline = ResumeRAGPipeline()

pipeline.load_resume("data/uploads/YaduKR_CV.pdf")

while True:
    question = input("\nAsk (type 'exit' to quit): ")

    if question.lower() == "exit":
        break

    response = pipeline.ask(question)

    print("\nIntent :", response["intent"])

    if response["score"] is not None:
        print("Similarity :", response["score"])

    print("\nAnswer:\n")
    print(response["answer"])