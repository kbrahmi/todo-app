### Commandes disponibles 
# Commandes Docker

Construisez les conteneurs Docker en utilisant la commande suivante
```bash
docker-compose build
```

1. Lancez l'application en utilisant la commande :
```bash
docker-compose up 
```

2. Exécutez les migrations pour créer les tables de la base de données :


```bash
docker-compose exec web-todo-tasks python manage.py migrate
```

3. Créez un superutilisateur pour accéder au panneau d'administration et gérer l'application:

```bash
docker-compose exec web-todo-tasks python manage.py createsuperuser
```

Suivez les invites pour configurer votre compte de superutilisateur.

4. Run tests to ensure everything is working as expected:

```bash
docker-compose exec web-todo-tasks pytest
```

## Guide d'utilisation du Makefile

# Commandes du Django
**setup** : Installer toutes les dépendances Python nécessaires et migrer la base de données.
```bash
make setup
```
**test**  : Exécuter des tests unitaires.
```bash
make test
```


**create_superuser** : Créer un super utilisateur avec des identifiants prédéfinis: \
 username= tiki & password: tiki123  \
[Se connecter sur Admin Django](http://localhost:8000/admin/)

```bash
make create_superuser
```

**run** : Démarrer le serveur de développement Django. \
[Voir les APIs sur ce lien](http://localhost:8000/swagger/)

```bash
make run
```


**all** : Faire tout: installation, exécution et démarrage du serveur.

```bash
make all
``` 
---

---


### Test Technique pour Tech Lead Développeur Python

#### Objectif:

Construire une petite API RESTful qui permet de gérer une liste de tâches (to-do list) et des utilisateurs. Vous pouvez utiliser FastAPI, Django ou Flask pour ce test.

#### Exigences:

1. **Modèle de données**: Utilisez SQLAlchemy (pour FastAPI ou Flask) ou le modèle ORM de Django pour créer les modèles suivants avec les relations appropriées:
    - **Utilisateur** (User)
        - ID (unique, généré automatiquement)
        - Nom
        - Email
        - Tâches assignées (relation One-to-Many avec Tâche)
    - **Tâche** (Task)
        - ID (unique, généré automatiquement)
        - Titre
        - Description
        - État (Non commencé, En cours, Terminé)
        - ID de l'utilisateur assigné (relation One-to-Many avec Utilisateur)

2. **Base de données**: Utilisez SQLite comme base de données pour stocker les tâches et les utilisateurs.

3. **API RESTful**: Créez les endpoints suivants:
    - **Endpoints pour les tâches**
        - GET `/tasks/`: Récupérer toutes les tâches
        - GET `/tasks/{id}`: Récupérer une tâche par ID
        - POST `/tasks/`: Créer une nouvelle tâche
        - PUT `/tasks/{id}`: Mettre à jour une tâche
        - DELETE `/tasks/{id}`: Supprimer une tâche
    - **Endpoints pour les utilisateurs**
        - GET `/users/`: Récupérer tous les utilisateurs
        - GET `/users/{id}/tasks`: Récupérer toutes les tâches d'un utilisateur

4. **Tests**: Écrivez des tests unitaires pour chaque endpoint. Utilisez Pytest si vous utilisez FastAPI ou Flask, et Django Test si vous utilisez Django.

#### Bonus:

- Ajoutez une authentification JWT (pour FastAPI ou Flask) ou utilisez le système d'authentification de Django.
- Utilisez des migrations de base de données.
- Ajoutez une documentation API avec Swagger (pour FastAPI) ou DRF (pour Django).
- **Gestion des étiquettes (Tags)**
    - Modèle d'étiquette avec ID et Nom
    - Relation Many-to-Many entre Tâche et Étiquette
    - Endpoints pour ajouter/retirer des étiquettes à une tâche

#### Livrables:

- Code source de l'application
- Instructions pour exécuter les tests et lancer l'application

#### Évaluation:

- Respect des exigences et de la structure du code
- Qualité des tests unitaires
- Utilisation efficace de Git (commits bien structurés, utilisation de branches, etc.)
- Bonus: Qualité de la documentation et des commentaires
