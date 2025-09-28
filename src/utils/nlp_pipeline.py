from transformers import pipeline

def summarizer_article(new):
    summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
    
    resumen = summarizer(new, max_length=60, min_length=20, do_sample=False)
    return resumen[0]['summary_text']

def classifier_article(new):
    classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

    labels = [
        "Política",
        "Tecnología",
        "Deportes",
        "Economía",
        "Salud"
        ]
    print(classifier(new, labels))
