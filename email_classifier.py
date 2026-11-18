
def classify_email(email):
    text = email.lower()

    if "pilne" in text or "urgent" in text or "asap" in text:
        return "PILNE"
    elif "faktura" in text or "invoice" in text:
        return "FAKTURY"
    elif "praca" in text or "meeting" in text or "spotkanie" in text or "porozmawia" in text:
        return "SOPTKANIA"
    else:
        return "INNE"


emails = [
    "Pilne! Prosze o odpowiedz dzisiaj.",
    "Przesylam faktura za usluge.",
    "Meeting z zespolem jutro.",
    "Zapraszamy na weekendowa promocje.",
  "Urgent! Please send the documents today.",
  "Spotkanie z kientem w poniedzialek.",
  "Czy mozemy jutro porozmawiac o projekcie?"
  "Prosze przeslac dokumenty ASAP"
  
]

for email in emails:
    category = classify_email(email)
    print(f"Email: {email}")
    print(f"Kategoria: {category}")
    print("--------------------")
