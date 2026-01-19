# Menetou 🎅 - Tableau de Bord de Noël

Ce projet est un tableau de bord interactif pour organiser un week-end de Noël en famille à Menetou. Il permet de gérer les menus, de générer des listes de courses via l'IA (Gemini) et de suivre le budget et les tâches.

L'objectif était de créer une interface accessible pour tous les membres de la famille, simple d'utilisation, en mélangeant l'idée d'un menu interactif et d'un "Tricount" pour les dépenses.

## Fonctionnalités

- **Compte à rebours** : Avant l'arrivée du grand jour.
- **Gestion des Menus** : Planifiez les entrées, plats et desserts.
- **Génération par IA** : Utilisez Google Gemini pour transformer vos menus en une liste de courses détaillée.
- **Synchronisation Cloud** : Sauvegarde et partage des données via Google Sheets (Apps Script).
- **Suivi Budget & Tâches** : Organisez-vous efficacement.

## Installation

1. Clonez le dépôt.
2. Installez les dépendances Python (pour les scripts de génération en local) :
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

### Dashboard HTML
Ouvrez `christmas_dashboard.html` dans votre navigateur. Cliquez sur l'icône ⚙️ pour configurer :
- **Clé API Gemini** : Pour la génération de listes.
- **URL Apps Script** : Pour la synchronisation entre appareils.

### Scripts Python
Pour utiliser `generate_list.py`, définissez votre clé API dans les variables d'environnement :
```powershell
$env:GOOGLE_API_KEY="VOTRE_CLE_API"
python generate_list.py
```

## Structure du Projet

- `christmas_dashboard.html` : L'application principale (SPA).
- `generate_list.py` : Script Python pour générer la liste de courses en CLI.
- `list_models.py` : Utilitaire pour lister les modèles Gemini disponibles.
- `deploy_to_nas.bat` : Script de déploiement (nécessite configuration).
