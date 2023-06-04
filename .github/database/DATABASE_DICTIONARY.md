# besson_ethan_info_1a

## Dictionnaire de données

### t_categorie

| Nom                    | Type         | Description                 | Valeur de base    |
|------------------------|--------------|-----------------------------|-------------------|
| id_categorie           | int          | Clef primaire               | AUTO_INCREMENT    |
| nom_cat                | varchar(24)  | Nom de la catégorie         | NULL              |
| description_cat        | varchar(255) | Description de la catégorie | NULL              |
| derniere_actualisation | timestamp    | Dernière mise à jour        | CURRENT_TIMESTAMP |

### t_categorie_avoir_materiel

| Nom                         | Type      | Description                | Valeur de base    |
|-----------------------------|-----------|----------------------------|-------------------|
| id_categorie_avoir_materiel | int       | Clef primaire              | AUTO_INCREMENT    |
| fk_categorie                | int       | Clef étrangère t_categorie | NULL              |
| fk_materiel                 | int       | Clef étrangère t_materiel  | NULL              |
| derniere_actualisation      | timestamp | Dernière mise à jour       | CURRENT_TIMESTAMP |

### t_departement

| Nom                    | Type         | Description            | Valeur de base    |
|------------------------|--------------|------------------------|-------------------|
| id_departement         | int          | Clef primaire          | AUTO_INCREMENT    |
| nom_dep                | varchar(12)  | Department name        | NULL              |
| description_dep        | varchar(255) | Department description | NULL              |
| derniere_actualisation | timestamp    | Dernière mise à jour   | CURRENT_TIMESTAMP |

### t_departement_avoir_materiel

| Nom                           | Type      | Description                  | Valeur de base    |
|-------------------------------|-----------|------------------------------|-------------------|
| id_departement_avoir_materiel | int       | Clef primaire                | AUTO_INCREMENT    |
| fk_materiel                   | int       | Clef étrangère t_materiel    | NULL              |
| fk_departement                | int       | Clef étrangère t_departement | NULL              |
| derniere_actualisation        | timestamp | Dernière mise à jour         | CURRENT_TIMESTAMP |

### t_fournisseur

| Nom                    | Type         | Description          | Valeur de base    |
|------------------------|--------------|----------------------|-------------------|
| id_fournisseur         | int          | Clef primaire        | AUTO_INCREMENT    |
| nom_four               | varchar(255) | Nom du fournisseur   | NULL              |
| adresse                | varchar(255) | Adresse              | NULL              |
| num_tel                | varchar(16)  | N° de téléphone      | NULL              |
| derniere_actualisation | timestamp    | Dernière mise à jour | CURRENT_TIMESTAMP |

### t_fournisseur_avoir_materiel

| Nom                           | Type      | Description                  | Valeur de base    |
|-------------------------------|-----------|------------------------------|-------------------|
| id_fournisseur_avoir_materiel | int       | Clef primaire                | AUTO_INCREMENT    |
| fk_fournisseur                | int       | Clef étrangère t_fournisseur | NULL              |
| fk_materiel                   | int       | Clef étrangère t_materiel    | NULL              |
| derniere_actualisation        | timestamp | Dernière mise à jour         | CURRENT_TIMESTAMP |

### t_marque

| Nom                    | Type         | Description              | Valeur de base    |
|------------------------|--------------|--------------------------|-------------------|
| id_marque              | int          | Clef primaire            | AUTO_INCREMENT    |
| nom_marque             | varchar(255) | Nom de la marque         | NULL              |
| description_marque     | varchar(255) | Description de la marque | NULL              |
| derniere_actualisation | timestamp    | Dernière mise à jour     | CURRENT_TIMESTAMP |

### t_marque_avoir_materiel

| Nom                      | Type      | Description               | Valeur de base    |
|--------------------------|-----------|---------------------------|-------------------|
| id_marque_avoir_materiel | int       | Clef primaire             | AUTO_INCREMENT    |
| fk_marque                | int       | Clef étrangère t_marque   | NULL              |
| fk_materiel              | int       | Clef étrangère t_materiel | NULL              |
| derniere_actualisation   | timestamp | Dernière mise à jour      | CURRENT_TIMESTAMP |

### t_materiel

| Nom                    | Type         | Description                      | Valeur de base    |
|------------------------|--------------|----------------------------------|-------------------|
| id_materiel            | int          | Clef primaire                    | AUTO_INCREMENT    |
| nom_mat                | varchar(255) | Nom du matériel                  | NULL              |
| model_mat              | varchar(255) | Modèle du matériel               | NULL              |
| serial_num             | varchar(255) | Numéro de série                  | NULL              |
| date_achat             | datetime     | Date d'achat                     | NULL              |
| date_expi              | datetime     | Date d'expiration de la garantie | NULL              |
| prix_mat               | varchar(12)  | Prix du matériel                 | NULL              |
| derniere_actualisation | timestamp    | Dernière mise à jour             | CURRENT_TIMESTAMP |

### t_personnes

| Nom                    | Type         | Description                | Valeur de base    |
|------------------------|--------------|----------------------------|-------------------|
| id_personnes           | int          | Clef primaire              | AUTO_INCREMENT    |
| prenom_pers            | varchar(255) | Prénom de la personne      | NULL              |
| nom_pers               | varchar(255) | Nom de la personne         | NULL              |
| dep_pers               | varchar(14)  | Département de la personne | NULL              |
| derniere_actualisation | timestamp    | Dernière mise à jour       | CURRENT_TIMESTAMP |

### t_personnes_ajout_materiel

| Nom                         | Type      | Description                | Valeur de base    |
|-----------------------------|-----------|----------------------------|-------------------|
| id_personnes_ajout_materiel | int       | Clef primaire              | AUTO_INCREMENT    |
| fk_personnes                | int       | Clef étrangère t_personnes | NULL              |
| fk_materiel                 | int       | Clef étrangère t_materiel  | NULL              |
| date_ajout                  | datetime  | Date d'ajout du materiel   | NULL              |
| derniere_actualisation      | timestamp | Dernière mise à jour       | CURRENT_TIMESTAMP |

### t_personnes_avoir_materiel

| Nom                         | Type      | Description                | Valeur de base    |
|-----------------------------|-----------|----------------------------|-------------------|
| id_personnes_avoir_materiel | int       | Clef primaire              | AUTO_INCREMENT    |
| fk_personnes                | int       | Clef étrangère t_personnes | NULL              |
| fk_materiel                 | int       | Clef étrangère t_materiel  | NULL              |
| derniere_actualisation      | timestamp | Dernière mise à jour       | CURRENT_TIMESTAMP |

### t_personnes_retrait_materiel

| Nom                           | Type      | Description                 | Valeur de base    |
|-------------------------------|-----------|-----------------------------|-------------------|
| id_personnes_retrait_materiel | int       | Clef primaire               | AUTO_INCREMENT    |
| fk_personnes                  | int       | Clef étrangère t_personnes  | NULL              |
| fk_materiel                   | int       | Clef étrangère t_materiel   | NULL              |
| date_retrait                  | datetime  | Date de retrait du materiel | NULL              |
| derniere_actualisation        | timestamp | Dernière mise à jour        | CURRENT_TIMESTAMP |