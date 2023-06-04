# besson_ethan_info_1a

## Tables

### t_categorie

| Nom                    | Type         | Description          | Valeur de base |
|------------------------|--------------|----------------------|----------------|
| id_categorie           | int          | Primary key          | AUTO_INCREMENT |
| nom_cat                | varchar(24)  | Category name        | NULL           |
| description_cat        | varchar(255) | Category description | NULL           |
| derniere_actualisation | timestamp    | Last update          |                |

### t_categorie_avoir_materiel

| Column                      | Type      | Description                |
|-----------------------------|-----------|----------------------------|
| id_categorie_avoir_materiel | int       | Primary key                |
| fk_categorie                | int       | Foreign key to t_categorie |
| fk_materiel                 | int       | Foreign key to t_materiel  |
| derniere_actualisation      | timestamp | Last update                |

### t_departement

| Column                 | Type         | Description            |
|------------------------|--------------|------------------------|
| id_departement         | int          | Primary key            |
| nom_dep                | varchar(12)  | Department name        |
| description_dep        | varchar(255) | Department description |
| derniere_actualisation | timestamp    | Last update            |

### t_departement_avoir_materiel

| Column                        | Type      | Description                  |
|-------------------------------|-----------|------------------------------|
| id_departement_avoir_materiel | int       | Primary key                  |
| fk_materiel                   | int       | Foreign key to t_materiel    |
| fk_departement                | int       | Foreign key to t_departement |
| derniere_actualisation        | timestamp | Last update                  |

### t_fournisseur

| Column                 | Type         | Description   |
|------------------------|--------------|---------------|
| id_fournisseur         | int          | Primary key   |
| nom_four               | varchar(255) | Supplier name |
| adresse                | varchar(255) | Address       |
| num_tel                | varchar(16)  | Phone number  |
| derniere_actualisation | timestamp    | Last update   |

### t_fournisseur_avoir_materiel

| Column                        | Type      | Description                  |
|-------------------------------|-----------|------------------------------|
| id_fournisseur_avoir_materiel | int       | Primary key                  |
| fk_fournisseur                | int       | Foreign key to t_fournisseur |
| fk_materiel                   | int       | Foreign key to t_materiel    |
| derniere_actualisation        | timestamp | Last update                  |

### t_marque

| Column                 | Type         | Description       |
|------------------------|--------------|-------------------|
| id_marque              | int          | Primary key       |
| nom_marque             | varchar(255) | Brand name        |
| description_marque     | varchar(255) | Brand description |
| derniere_actualisation | timestamp    | Last update       |

### t_marque_avoir_materiel

| Column                   | Type      | Description               |
|--------------------------|-----------|---------------------------|
| id_marque_avoir_materiel | int       | Primary key               |
| fk_marque                | int       | Foreign key to t_marque   |
| fk_materiel              | int       | Foreign key to t_materiel |
| derniere_actualisation   | timestamp | Last update               |

### t_materiel

| Column                 | Type         | Description     |
|------------------------|--------------|-----------------|
| id_materiel            | int          | Primary key     |
| nom_mat                | varchar(255) | Material name   |
| model_mat              | varchar(255) | Material model  |
| serial_num             | varchar(255) | Serial number   |
| date_achat             | datetime     | Purchase date   |
| date_expi              | datetime     | Expiration date |
| prix_mat               | varchar(12)  | Material price  |
| derniere_actualisation | timestamp    | Last update     |

### t_personnes

| Column                 | Type         | Description       |
|------------------------|--------------|-------------------|
| id_personnes           | int          | Primary key       |
| prenom_pers            | varchar(255) | First name        |
| nom_pers               | varchar(255) | Last name         |
| dep_pers               | varchar(14)  | Department person |
| derniere_actualisation | timestamp    | Last update       |

### t_personnes_ajout_materiel

| Column                      | Type      | Description                |
|-----------------------------|-----------|----------------------------|
| id_personnes_ajout_materiel | int       | Primary key                |
| fk_personnes                | int       | Foreign key to t_personnes |
| fk_materiel                 | int       | Foreign key to t_materiel  |
| date_ajout                  | datetime  | Date added                 |
| derniere_actualisation      | timestamp | Last update                |

### t_personnes_avoir_materiel

| Column                      | Type      | Description                |
|-----------------------------|-----------|----------------------------|
| id_personnes_avoir_materiel | int       | Primary key                |
| fk_personnes                | int       | Foreign key to t_personnes |
| fk_materiel                 | int       | Foreign key to t_materiel  |
| derniere_actualisation      | timestamp | Last update                |

### t_personnes_retrait_materiel

| Column                        | Type      | Description                |
|-------------------------------|-----------|----------------------------|
| id_personnes_retrait_materiel | int       | Primary key                |
| fk_personnes                  | int       | Foreign key to t_personnes |
| fk_materiel                   | int       | Foreign key to t_materiel  |
| date_retrait                  | datetime  | Date removed               |
| derniere_actualisation        | timestamp | Last update                |
