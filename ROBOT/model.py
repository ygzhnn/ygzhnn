from gpt4all import GPT4All

def load_model():
    model = GPT4All("C:/Users/yagiz/AppData/Local/nomic.ai/GPT4All/q4_0-orca-mini-3b.gguf", allow_download=False)
    return model
