from transformers import pipeline

summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

def summarizer_article(new):
    resumen = summarizer(new, max_length=60, min_length=20, do_sample=False)
    return resumen[0]['summary_text']

def classifier_article(new):
    labels = [
        "Política",
        "Tecnología",
        "Deportes",
        "Economía",
        "Salud"
        ]
    print(classifier(new, labels))
