# Customer Orders Analysis & Enrichment Pipeline

Un script Python automatisé permettant de nettoyer, joindre et analyser des données de ventes et de clients à l'aide de la bibliothèque **Pandas**.

---

##  Fonctionnalités

- **Merging de données :** Jointure (`left join`) entre l'historique des commandes (`orders.csv`) et les informations clients (`customers.csv`).
- **Feature Engineering :** 
  - Calcul du prix total par commande (`total_price`).
  - Identification des commandes à forte valeur (> 1000).
  - Extraction et conversion des dates (mois et périodes mensuelles `YYYY-MM`).
- **Nettoyage de données :** Détection et gestion des valeurs manquantes (remplacement par `"Unknown"` pour les profils clients introuvables).
- **Reporting automatique :** Génération d'un fichier texte résumé (`report.txt`) contenant le chiffre d'affaires total, le panier moyen, la répartition par ville et par mois.
- **Exportation :** Sauvegarde du dataset enrichi dans un nouveau fichier CSV.

---

##  Structure du projet

```text
customer-orders/
│
├── data/
│   ├── customers.csv         # Données clients
│   ├── orders.csv            # Historique des commandes
│   └── enriched_orders.csv   # Dataset final généré
│
├── output/
│   └── report.txt            # Rapport d'analyse texte
│
├── main.py                   # Script principal de traitement
└── README.md                 # Documentation du projet