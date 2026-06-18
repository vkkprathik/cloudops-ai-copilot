from rag.vector_store import search_knowledge

query = "Disk usage is 100%"

result = search_knowledge(query)

print(result)