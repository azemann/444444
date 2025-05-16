def init_chat():
    return []

def update_chat(question, history):
    history.append({"role": "user", "content": question})
    reply = f"(Réponse simulée à : '{question[:50]}...')"
    history.append({"role": "assistant", "content": reply})
    return reply
