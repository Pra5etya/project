from transformers import BertTokenizer, BertForSequenceClassification
import torch

# Muat model dan tokenizer BERT
model_name = "bert-base-uncased"
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertForSequenceClassification.from_pretrained(model_name)

# Siapkan teks yang ingin diklasifikasikan
texts = ["This is a great movie!", "I didn't like this film at all."]

# Tokenisasi teks
inputs = tokenizer(texts, return_tensors="pt", padding=True, truncation=True, max_length=512)

# Lakukan inferensi
with torch.no_grad():
    outputs = model(**inputs)

# Dapatkan prediksi
logits = outputs.logits
predictions = torch.argmax(logits, dim=-1)

# Cetak hasil prediksi
for text, prediction in zip(texts, predictions):
    label = "positive" if prediction == 1 else "negative"
    print(f"Text: {text} - Sentiment: {label}")
