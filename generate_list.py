import os
import google.generativeai as genai
import json

# --- CONFIGURATION ---
# Remplacez par votre vraie clé API ou définissez la variable d'environnement GOOGLE_API_KEY
# Vous pouvez trouver votre clé ici : https://aistudio.google.com/app/apikey
API_KEY = os.getenv("GOOGLE_API_KEY") or "AIzaSyB-LaI8y7D2ll1eq0TPX-zUuxCJFs1Bx6Y"

# --- DONNÉES (MENUS) ---
# Mettez à jour cette section avec vos vrais menus !
MEALS = [
    {
        "title": "Vendredi Soir (Arrivée)",
        "starter": "Soupe de potiron",
        "main": "Quiche lorraine et salade",
        "dessert": "Tarte aux pommes"
    },
    {
        "title": "Samedi Midi",
        "starter": "Avocat crevettes",
        "main": "Poulet rôti et pommes de terre",
        "dessert": "Mousse au chocolat"
    },
    {
        "title": "Samedi Soir (Réveillon)",
        "starter": "Foie gras et toasts",
        "main": "Dinde aux marrons",
        "dessert": "Bûche de Noël"
    },
    {
        "title": "Dimanche Midi (Départ)",
        "starter": "Reste de foie gras",
        "main": "Reste de dinde",
        "dessert": "Clémentines"
    }
]

PARTICIPANTS_COUNT = "6 adultes et 3 enfants"

def generate_grocery_list():
    if API_KEY == "YOUR_API_KEY_HERE":
        print("❌ Erreur: Veuillez configurer votre clé API dans le script (variable API_KEY).")
        return

    print(f"⚙️ Configuration Gemini avec la clé : {API_KEY[:5]}...")
    genai.configure(api_key=API_KEY)
    
    # Préparation du prompt
    meals_summary = "\n".join([f"{m['title']}: {m.get('starter', '-')}, {m.get('main', '-')}, {m.get('dessert', '-')}" for m in MEALS])
    
    prompt = f"""
    Tu es un assistant culinaire expert pour Noël.
    Contexte : Week-end de Noël pour {PARTICIPANTS_COUNT}.
    
    Voici les menus prévus :
    {meals_summary}
    
    Tâche : Génère une liste de courses COMPLÈTE et DÉTAILLÉE pour réaliser ces repas.
    - Adapte les quantités pour {PARTICIPANTS_COUNT}.
    - Ajoute les indispensables du petit-déjeuner et du goûter si non précisés.
    - Le format de sortie doit être un tableau JSON d'objets, chaque objet ayant les propriétés "name" (string) et "category" (string, parmi "Frais", "Épicerie", "Boissons", "Autre").
    - Ne retourne QUE le JSON, sans texte explicatif avant ou après.
    """
    
    print("🔮 Génération de la liste de courses en cours avec Gemini...")
    
    try:
        model = genai.GenerativeModel('gemini-2.0-flash-lite')
        response = model.generate_content(prompt)
        
        text = response.text
        # Nettoyage des blocs de code markdown si présents
        if "```json" in text:
            text = text.replace("```json", "").replace("```", "")
        elif "```" in text:
            text = text.replace("```", "")
            
        data = json.loads(text.strip())
        
        print(f"✅ Liste générée avec succès ({len(data)} articles) !")
        
        # Sauvegarde dans un fichier
        filename = "grocery_list.json"
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
            
        print(f"📁 Sauvegardé dans '{filename}'")
        
        # Aperçu
        print("\n--- Aperçu des 5 premiers articles ---")
        for item in data[:5]:
            print(f"- {item['name']} ({item['category']})")
        print("...")

    except Exception as e:
        print(f"❌ Erreur lors de la génération : {e}")
        if 'response' in locals() and hasattr(response, 'text'):
             print(f"Réponse brute reçue : {response.text}")

if __name__ == "__main__":
    generate_grocery_list()
