from transformers import pipeline

from transformers import pipeline

summarizer = pipeline(
    "summarization", 
    model="mrm8488/bert2bert_shared-spanish-finetuned-summarization",
    device_map=None,   # fuerza a cargar en CPU/GPU sin meta-tensors
)

classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

def summarizer_article(new):
    if not new or len(new.strip()) == 0:
        return "Resumen no disponible"

    try:
        resumen = summarizer(
            new, 
            max_length=120, 
            min_length=40, 
            do_sample=False,
            forced_bos_token_id=250004  # código de idioma español
        )
        return resumen[0]['summary_text']
    except Exception as e:
        print("Error en summarizer_article:", e)
        return "Error al resumir"

def classifier_article(new):
    labels = [
        "Política",
        "Tecnología",
        "Deportes",
        "Economía",
        "Salud"
        ]
    print(classifier(new, labels))
