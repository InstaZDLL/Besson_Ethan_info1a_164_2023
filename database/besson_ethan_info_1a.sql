-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               8.0.30 - MySQL Community Server - GPL
-- Server OS:                    Win64
-- HeidiSQL Version:             12.1.0.6537
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Dumping database structure for besson_ethan_info_1a
DROP DATABASE IF EXISTS `besson_ethan_info_1a`;
CREATE DATABASE IF NOT EXISTS `besson_ethan_info_1a` /*!40100 DEFAULT CHARACTER SET utf8mb3 COLLATE utf8mb3_bin */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `besson_ethan_info_1a`;

-- Dumping structure for table besson_ethan_info_1a.t_categorie
DROP TABLE IF EXISTS `t_categorie`;
CREATE TABLE IF NOT EXISTS `t_categorie` (
  `id_categorie` int NOT NULL AUTO_INCREMENT,
  `nom_cat` varchar(24) CHARACTER SET utf8mb3 COLLATE utf8mb3_bin DEFAULT NULL,
  `description_cat` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_bin DEFAULT NULL,
  `derniere_actualisation` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id_categorie`)
) ENGINE=InnoDB AUTO_INCREMENT=68 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;

-- Dumping data for table besson_ethan_info_1a.t_categorie: ~6 rows (approximately)
INSERT INTO `t_categorie` (`id_categorie`, `nom_cat`, `description_cat`, `derniere_actualisation`) VALUES
	(1, 'Ordinateurs', NULL, '2023-03-16 14:08:55'),
	(2, 'Claviers et souris', NULL, '2023-03-16 14:38:19'),
	(4, 'Cartouche d\'encre', NULL, '2023-03-16 14:09:43'),
	(5, 'Photoconducteurs', NULL, '2023-03-16 14:09:52'),
	(6, 'Recupereteur de tonner', NULL, '2023-04-18 07:49:03'),
	(7, 'Serveurs', NULL, '2023-04-18 07:55:19'),
	(8, 'Moniteurs', NULL, '2023-04-18 07:56:23'),
	(9, 'Autres', NULL, '2023-04-18 07:56:22');

-- Dumping structure for table besson_ethan_info_1a.t_categorie_avoir_materiel
DROP TABLE IF EXISTS `t_categorie_avoir_materiel`;
CREATE TABLE IF NOT EXISTS `t_categorie_avoir_materiel` (
  `id_categorie_avoir_materiel` int NOT NULL AUTO_INCREMENT,
  `fk_categorie` int NOT NULL,
  `fk_materiel` int NOT NULL,
  `derniere_actualisation` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id_categorie_avoir_materiel`),
  KEY `fk_t_categorie_avoir_materiel_t_categorie` (`fk_categorie`),
  KEY `fk_t_categorie_avoir_materiel_t_materiel` (`fk_materiel`),
  CONSTRAINT `fk_t_categorie_avoir_materiel_t_categorie` FOREIGN KEY (`fk_categorie`) REFERENCES `t_categorie` (`id_categorie`) ON DELETE CASCADE ON UPDATE RESTRICT,
  CONSTRAINT `fk_t_categorie_avoir_materiel_t_materiel` FOREIGN KEY (`fk_materiel`) REFERENCES `t_materiel` (`id_materiel`) ON DELETE CASCADE ON UPDATE RESTRICT
) ENGINE=InnoDB AUTO_INCREMENT=39 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;

-- Dumping data for table besson_ethan_info_1a.t_categorie_avoir_materiel: ~38 rows (approximately)
INSERT INTO `t_categorie_avoir_materiel` (`id_categorie_avoir_materiel`, `fk_categorie`, `fk_materiel`, `derniere_actualisation`) VALUES
	(1, 2, 1, '2023-04-18 07:59:18'),
	(2, 2, 2, '2023-04-18 07:59:18'),
	(3, 2, 3, '2023-04-18 07:59:18'),
	(4, 2, 4, '2023-04-18 07:59:18'),
	(5, 2, 5, '2023-04-18 07:59:18'),
	(6, 2, 6, '2023-04-18 07:59:18'),
	(7, 2, 7, '2023-04-18 07:59:18'),
	(8, 2, 8, '2023-04-18 07:59:18'),
	(9, 2, 9, '2023-04-18 07:59:18'),
	(10, 2, 10, '2023-04-18 07:59:18'),
	(11, 2, 11, '2023-04-18 07:59:18'),
	(12, 1, 12, '2023-04-18 07:59:18'),
	(13, 1, 13, '2023-04-18 07:59:18'),
	(14, 1, 14, '2023-04-18 07:59:18'),
	(15, 1, 15, '2023-04-18 07:59:18'),
	(16, 1, 16, '2023-04-18 07:59:18'),
	(17, 1, 17, '2023-04-18 07:59:18'),
	(18, 1, 18, '2023-04-18 07:59:18'),
	(19, 1, 19, '2023-04-18 07:59:18'),
	(20, 1, 20, '2023-04-18 07:59:18'),
	(21, 1, 21, '2023-04-18 07:59:18'),
	(22, 1, 22, '2023-04-18 07:59:18'),
	(23, 1, 23, '2023-04-18 07:59:18'),
	(24, 1, 24, '2023-04-18 07:59:18'),
	(25, 7, 25, '2023-04-18 07:59:18'),
	(26, 7, 26, '2023-04-18 07:59:18'),
	(27, 7, 27, '2023-04-18 07:59:18'),
	(28, 8, 28, '2023-04-18 07:59:18'),
	(29, 8, 29, '2023-04-18 07:59:18'),
	(30, 8, 30, '2023-04-18 07:59:18'),
	(31, 8, 31, '2023-04-18 07:59:18'),
	(32, 8, 32, '2023-04-18 07:59:18'),
	(33, 8, 33, '2023-04-18 07:59:18'),
	(34, 8, 34, '2023-04-18 07:59:18'),
	(35, 8, 35, '2023-04-18 07:59:18'),
	(36, 8, 36, '2023-04-18 07:59:18'),
	(37, 8, 37, '2023-04-18 07:59:18'),
	(38, 8, 38, '2023-04-18 07:59:18');

-- Dumping structure for table besson_ethan_info_1a.t_departement
DROP TABLE IF EXISTS `t_departement`;
CREATE TABLE IF NOT EXISTS `t_departement` (
  `id_departement` int NOT NULL AUTO_INCREMENT,
  `nom_dep` varchar(12) CHARACTER SET utf8mb3 COLLATE utf8mb3_bin DEFAULT NULL,
  `description_dep` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_bin DEFAULT NULL,
  `derniere_actualisation` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id_departement`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;

-- Dumping data for table besson_ethan_info_1a.t_departement: ~4 rows (approximately)
INSERT INTO `t_departement` (`id_departement`, `nom_dep`, `description_dep`, `derniere_actualisation`) VALUES
	(1, '502', 'Dep informatique', '2023-03-16 14:10:56'),
	(2, '431', 'Dep finances', '2023-03-16 14:10:51'),
	(3, '444', 'Dep RH', '2023-03-16 14:11:13'),
	(4, '432', 'Dep commercial', '2023-03-16 14:11:39');

-- Dumping structure for table besson_ethan_info_1a.t_departement_avoir_materiel
DROP TABLE IF EXISTS `t_departement_avoir_materiel`;
CREATE TABLE IF NOT EXISTS `t_departement_avoir_materiel` (
  `id_departement_avoir_materiel` int NOT NULL AUTO_INCREMENT,
  `fk_materiel` int NOT NULL,
  `fk_departement` int NOT NULL,
  `derniere_actualisation` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id_departement_avoir_materiel`),
  KEY `fk_t_departement_avoir_materiel_t_materiel` (`fk_materiel`),
  KEY `fk_t_departement_avoir_materiel_t_departement` (`fk_departement`),
  CONSTRAINT `fk_t_departement_avoir_materiel_t_departement` FOREIGN KEY (`fk_departement`) REFERENCES `t_departement` (`id_departement`) ON DELETE CASCADE ON UPDATE RESTRICT,
  CONSTRAINT `fk_t_departement_avoir_materiel_t_materiel` FOREIGN KEY (`fk_materiel`) REFERENCES `t_materiel` (`id_materiel`) ON DELETE CASCADE ON UPDATE RESTRICT
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;

-- Dumping data for table besson_ethan_info_1a.t_departement_avoir_materiel: ~10 rows (approximately)
INSERT INTO `t_departement_avoir_materiel` (`id_departement_avoir_materiel`, `fk_materiel`, `fk_departement`, `derniere_actualisation`) VALUES
	(1, 1, 1, '2023-04-18 08:13:19'),
	(2, 13, 1, '2023-04-18 08:13:30'),
	(3, 28, 1, '2023-04-18 08:13:40'),
	(4, 2, 3, '2023-04-18 08:14:12'),
	(5, 14, 3, '2023-04-18 08:14:20'),
	(6, 29, 3, '2023-04-18 08:14:30'),
	(7, 3, 2, '2023-04-18 08:15:21'),
	(8, 30, 2, '2023-04-18 08:15:30'),
	(9, 31, 2, '2023-04-18 08:15:37'),
	(10, 15, 2, '2023-04-18 08:17:24');

-- Dumping structure for table besson_ethan_info_1a.t_fournisseur
DROP TABLE IF EXISTS `t_fournisseur`;
CREATE TABLE IF NOT EXISTS `t_fournisseur` (
  `id_fournisseur` int NOT NULL AUTO_INCREMENT,
  `nom_four` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_bin DEFAULT NULL,
  `adresse` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_bin DEFAULT NULL,
  `num_tel` varchar(16) CHARACTER SET utf8mb3 COLLATE utf8mb3_bin DEFAULT NULL,
  `derniere_actualisation` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id_fournisseur`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;

-- Dumping data for table besson_ethan_info_1a.t_fournisseur: ~5 rows (approximately)
INSERT INTO `t_fournisseur` (`id_fournisseur`, `nom_four`, `adresse`, `num_tel`, `derniere_actualisation`) VALUES
	(1, 'HP', 'Ueberlandstrasse 1, 8600 DÃ¼bendorf, Switzerland', '+41 58 444 ', '2023-04-18 07:52:00'),
	(2, 'Benq', '16 Jihu Road Neihu, Taipei 114 Taiwan', '+886 2 2727', '2023-03-16 14:18:36'),
	(3, 'Hewlett Packard Enterprise', '1701 E Mossy Oaks Rd, Spring, TX 77389, United States', '+1 888 342 ', '2023-03-16 14:16:18'),
	(4, 'Synology', '9F., No.1, Yuandong Rd., Banqiao Dist., New Taipei City 220632, Taiwan', '+886 2 2955 1814', '2023-04-18 07:20:02'),
	(5, 'Samsung', '1, SAMSUNGJEONJA-RO, HWASEONG-SI, GYEONGGI-DO 18448, KOREA', '+82-31-209-7114', '2023-04-18 07:24:38');

-- Dumping structure for table besson_ethan_info_1a.t_fournisseur_avoir_materiel
DROP TABLE IF EXISTS `t_fournisseur_avoir_materiel`;
CREATE TABLE IF NOT EXISTS `t_fournisseur_avoir_materiel` (
  `id_fournisseur_avoir_materiel` int NOT NULL AUTO_INCREMENT,
  `fk_fournisseur` int NOT NULL,
  `fk_materiel` int NOT NULL,
  `derniere_actualisation` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id_fournisseur_avoir_materiel`),
  KEY `fk_t_fournisseur_avoir_materiel_t_fournisseur` (`fk_fournisseur`),
  KEY `fk_t_fournisseur_avoir_materiel_t_materiel` (`fk_materiel`),
  CONSTRAINT `fk_t_fournisseur_avoir_materiel_t_fournisseur` FOREIGN KEY (`fk_fournisseur`) REFERENCES `t_fournisseur` (`id_fournisseur`) ON DELETE CASCADE ON UPDATE RESTRICT,
  CONSTRAINT `fk_t_fournisseur_avoir_materiel_t_materiel` FOREIGN KEY (`fk_materiel`) REFERENCES `t_materiel` (`id_materiel`) ON DELETE CASCADE ON UPDATE RESTRICT
) ENGINE=InnoDB AUTO_INCREMENT=39 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;

-- Dumping data for table besson_ethan_info_1a.t_fournisseur_avoir_materiel: ~38 rows (approximately)
INSERT INTO `t_fournisseur_avoir_materiel` (`id_fournisseur_avoir_materiel`, `fk_fournisseur`, `fk_materiel`, `derniere_actualisation`) VALUES
	(1, 1, 1, '2023-04-18 07:25:54'),
	(2, 1, 2, '2023-04-18 07:25:54'),
	(3, 1, 3, '2023-04-18 07:25:54'),
	(4, 1, 4, '2023-04-18 07:25:54'),
	(5, 1, 5, '2023-04-18 07:25:54'),
	(6, 1, 6, '2023-04-18 07:25:54'),
	(7, 1, 7, '2023-04-18 07:25:54'),
	(8, 1, 8, '2023-04-18 07:25:54'),
	(9, 1, 9, '2023-04-18 07:25:54'),
	(10, 1, 10, '2023-04-18 07:25:54'),
	(11, 1, 11, '2023-04-18 07:25:54'),
	(12, 1, 12, '2023-04-18 07:25:54'),
	(13, 1, 13, '2023-04-18 07:25:54'),
	(14, 1, 14, '2023-04-18 07:25:54'),
	(15, 1, 15, '2023-04-18 07:25:54'),
	(16, 1, 16, '2023-04-18 07:25:54'),
	(17, 1, 17, '2023-04-18 07:25:54'),
	(18, 1, 18, '2023-04-18 07:25:54'),
	(19, 1, 19, '2023-04-18 07:25:54'),
	(20, 1, 20, '2023-04-18 07:25:54'),
	(21, 1, 21, '2023-04-18 07:25:54'),
	(22, 1, 22, '2023-04-18 07:25:54'),
	(23, 1, 23, '2023-04-18 07:25:54'),
	(24, 1, 24, '2023-04-18 07:25:54'),
	(25, 4, 25, '2023-04-18 07:25:54'),
	(26, 4, 26, '2023-04-18 07:25:54'),
	(27, 4, 27, '2023-04-18 07:25:54'),
	(28, 5, 28, '2023-04-18 07:25:54'),
	(29, 5, 29, '2023-04-18 07:25:54'),
	(30, 5, 30, '2023-04-18 07:25:54'),
	(31, 5, 31, '2023-04-18 07:25:54'),
	(32, 5, 32, '2023-04-18 07:25:54'),
	(33, 5, 33, '2023-04-18 07:25:54'),
	(34, 5, 34, '2023-04-18 07:25:54'),
	(35, 5, 35, '2023-04-18 07:25:54'),
	(36, 5, 36, '2023-04-18 07:25:54'),
	(37, 5, 37, '2023-04-18 07:25:54'),
	(38, 5, 38, '2023-04-18 07:25:54');

-- Dumping structure for table besson_ethan_info_1a.t_marque
DROP TABLE IF EXISTS `t_marque`;
CREATE TABLE IF NOT EXISTS `t_marque` (
  `id_marque` int NOT NULL AUTO_INCREMENT,
  `nom_marque` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_bin DEFAULT NULL,
  `description_marque` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_bin DEFAULT NULL,
  `derniere_actualisation` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id_marque`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;

-- Dumping data for table besson_ethan_info_1a.t_marque: ~13 rows (approximately)
INSERT INTO `t_marque` (`id_marque`, `nom_marque`, `description_marque`, `derniere_actualisation`) VALUES
	(1, 'HP', 'Hewlett Packard', '2023-04-23 12:05:54'),
	(2, 'HPE', 'Hewlett Packard Enterprise', '2023-04-23 12:05:51'),
	(3, 'Benq', 'Benq', '2023-04-18 07:26:00'),
	(4, 'Synology', 'Synology', '2023-04-18 07:26:30'),
	(5, 'Samsung', 'Samsung', '2023-04-18 07:26:41'),
	(6, 'Apple', 'Apple', '2023-04-23 12:07:49'),
	(7, 'Asus', 'Asus', '2023-04-23 12:08:02'),
	(8, 'Lenovo', 'Lenovo', '2023-04-23 12:08:29'),
	(9, 'TP-Link', 'TP-Link', '2023-04-23 12:11:16'),
	(10, 'Sony', 'Sony', '2023-04-23 12:11:34'),
	(11, 'Dell', 'Dell', '2023-04-23 12:11:36'),
	(12, 'Brother', 'Brother', '2023-04-23 12:11:47'),
	(13, 'Cisco', 'Cisco', '2023-04-23 12:15:04');

-- Dumping structure for table besson_ethan_info_1a.t_marque_avoir_materiel
DROP TABLE IF EXISTS `t_marque_avoir_materiel`;
CREATE TABLE IF NOT EXISTS `t_marque_avoir_materiel` (
  `id_marque_avoir_materiel` int NOT NULL AUTO_INCREMENT,
  `fk_marque` int NOT NULL,
  `fk_materiel` int NOT NULL,
  `derniere_actualisation` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id_marque_avoir_materiel`),
  KEY `fk_t_marque_avoir_materiel_t_marque` (`fk_marque`),
  KEY `fk_t_marque_avoir_materiel_t_materiel` (`fk_materiel`),
  CONSTRAINT `fk_t_marque_avoir_materiel_t_marque` FOREIGN KEY (`fk_marque`) REFERENCES `t_marque` (`id_marque`) ON DELETE CASCADE ON UPDATE RESTRICT,
  CONSTRAINT `fk_t_marque_avoir_materiel_t_materiel` FOREIGN KEY (`fk_materiel`) REFERENCES `t_materiel` (`id_materiel`) ON DELETE CASCADE ON UPDATE RESTRICT
) ENGINE=InnoDB AUTO_INCREMENT=39 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;

-- Dumping data for table besson_ethan_info_1a.t_marque_avoir_materiel: ~38 rows (approximately)
INSERT INTO `t_marque_avoir_materiel` (`id_marque_avoir_materiel`, `fk_marque`, `fk_materiel`, `derniere_actualisation`) VALUES
	(1, 1, 1, '2023-04-18 07:37:12'),
	(2, 1, 2, '2023-04-18 07:37:12'),
	(3, 1, 3, '2023-04-18 07:37:12'),
	(4, 1, 4, '2023-04-18 07:37:12'),
	(5, 1, 5, '2023-04-18 07:37:12'),
	(6, 1, 6, '2023-04-18 07:37:12'),
	(7, 1, 7, '2023-04-18 07:37:12'),
	(8, 1, 8, '2023-04-18 07:37:12'),
	(9, 1, 9, '2023-04-18 07:37:12'),
	(10, 1, 10, '2023-04-18 07:37:12'),
	(11, 1, 11, '2023-04-18 07:37:12'),
	(12, 1, 12, '2023-04-18 07:37:12'),
	(13, 1, 13, '2023-04-18 07:37:12'),
	(14, 1, 14, '2023-04-18 07:37:12'),
	(15, 1, 15, '2023-04-18 07:37:12'),
	(16, 1, 16, '2023-04-18 07:37:12'),
	(17, 1, 17, '2023-04-18 07:37:12'),
	(18, 1, 18, '2023-04-18 07:37:12'),
	(19, 1, 19, '2023-04-18 07:37:12'),
	(20, 1, 20, '2023-04-18 07:37:12'),
	(21, 1, 21, '2023-04-18 07:37:12'),
	(22, 1, 22, '2023-04-18 07:37:12'),
	(23, 1, 23, '2023-04-18 07:37:12'),
	(24, 1, 24, '2023-04-18 07:37:12'),
	(25, 4, 25, '2023-04-18 07:37:12'),
	(26, 4, 26, '2023-04-18 07:37:12'),
	(27, 4, 27, '2023-04-18 07:37:12'),
	(28, 5, 28, '2023-04-18 07:37:12'),
	(29, 5, 29, '2023-04-18 07:37:12'),
	(30, 5, 30, '2023-04-18 07:37:12'),
	(31, 5, 31, '2023-04-18 07:37:12'),
	(32, 5, 32, '2023-04-18 07:37:12'),
	(33, 5, 33, '2023-04-18 07:37:12'),
	(34, 5, 34, '2023-04-18 07:37:12'),
	(35, 5, 35, '2023-04-18 07:37:12'),
	(36, 5, 36, '2023-04-18 07:37:12'),
	(37, 5, 37, '2023-04-18 07:37:12'),
	(38, 5, 38, '2023-04-18 07:37:12');

-- Dumping structure for table besson_ethan_info_1a.t_materiel
DROP TABLE IF EXISTS `t_materiel`;
CREATE TABLE IF NOT EXISTS `t_materiel` (
  `id_materiel` int NOT NULL AUTO_INCREMENT,
  `nom_mat` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_bin DEFAULT NULL,
  `model_mat` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_bin DEFAULT NULL,
  `serial_num` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_bin DEFAULT NULL,
  `date_achat` datetime DEFAULT NULL,
  `date_expi` datetime DEFAULT NULL,
  `prix_mat` varchar(12) CHARACTER SET utf8mb3 COLLATE utf8mb3_bin DEFAULT NULL,
  `derniere_actualisation` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id_materiel`)
) ENGINE=InnoDB AUTO_INCREMENT=39 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;

-- Dumping data for table besson_ethan_info_1a.t_materiel: ~0 rows (approximately)
INSERT INTO `t_materiel` (`id_materiel`, `nom_mat`, `model_mat`, `serial_num`, `date_achat`, `date_expi`, `prix_mat`, `derniere_actualisation`) VALUES
	(1, 'HP Wireless Keyboard and Mouse', 'HSA-A011M', '7CH31915XH', '2023-03-16 15:20:00', '2027-03-16 15:20:00', '65', '2023-03-16 14:20:00'),
	(2, 'HP Wireless Keyboard and Mouse', 'HSA-A011M', '7CH57683QG', '2023-03-16 15:20:00', '2027-03-16 15:20:00', '65', '2023-03-16 14:20:00'),
	(3, 'HP Wireless Keyboard and Mouse', 'HSA-A011M', '7CH25547ZY', '2023-03-16 15:20:00', '2027-03-16 15:20:00', '65', '2023-03-16 14:20:00'),
	(4, 'HP Wireless Keyboard and Mouse', 'HSA-A011M', '7CH62266TR', '2023-03-16 15:20:00', '2027-03-16 15:20:00', '65', '2023-03-16 14:20:00'),
	(5, 'HP Wireless Keyboard and Mouse', 'HSA-A011M', '7CH94668GA', '2023-03-16 15:20:00', '2027-03-16 15:20:00', '65', '2023-03-16 14:20:00'),
	(6, 'HP Wireless Keyboard and Mouse', 'HSA-A011M', '7CH25749UX', '2023-03-16 15:20:00', '2027-03-16 15:20:00', '65', '2023-03-16 14:20:00'),
	(7, 'HP Wireless Keyboard and Mouse', 'HSA-A011M', '7CH93753ZW', '2023-03-16 15:20:00', '2027-03-16 15:20:00', '65', '2023-03-16 14:20:00'),
	(8, 'HP Wireless Keyboard and Mouse', 'HSA-A011M', '7CH87983VN', '2023-03-16 15:20:00', '2027-03-16 15:20:00', '65', '2023-03-16 14:20:00'),
	(9, 'HP Wireless Keyboard and Mouse', 'HSA-A011M', '7CH35444LQ', '2023-03-16 15:20:00', '2027-03-16 15:20:00', '65', '2023-03-16 14:20:00'),
	(10, 'HP Wireless Keyboard and Mouse', 'HSA-A011M', '7CH79634TN', '2023-03-16 15:20:00', '2027-03-16 15:20:00', '65', '2023-03-16 14:20:00'),
	(11, 'HP Wireless Keyboard and Mouse', 'HSA-A011M', '7CH83329AQ', '2023-03-16 15:20:00', '2027-03-16 15:20:00', '65', '2023-03-16 14:20:00'),
	(12, 'HP Wireless Keyboard and Mouse', 'HSA-A011M', '7CH64438RM', '2023-03-16 15:20:00', '2027-03-16 15:20:00', '65', '2023-03-16 14:20:00'),
	(13, 'HP Pro Mini 400 G9', '4G4N7AV', '7CH27474DV', '2023-04-17 08:50:22', '2027-04-17 08:50:23', '478', '2023-03-16 14:20:00'),
	(14, 'HP Pro Mini 400 G9', '4G4N7AV', '7CH43239QJ', '2023-04-17 08:50:22', '2027-04-17 08:50:23', '478', '2023-03-16 14:20:00'),
	(15, 'HP Pro Mini 400 G9', '4G4N7AV', '7CH25677AM', '2023-04-17 08:50:22', '2027-04-17 08:50:23', '478', '2023-03-16 14:20:00'),
	(16, 'HP Pro Mini 400 G9', '4G4N7AV', '7CH54657Q7', '2023-04-17 08:50:22', '2027-04-17 08:50:23', '478', '2023-03-16 14:20:00'),
	(17, 'HP Pro Mini 400 G9', '4G4N7AV', '7CH98634RD', '2023-04-17 08:50:22', '2027-04-17 08:50:23', '478', '2023-03-16 14:20:00'),
	(18, 'HP Pro Mini 400 G9', '4G4N7AV', '7CH92593JW', '2023-04-17 08:50:22', '2027-04-17 08:50:23', '478', '2023-03-16 14:20:00'),
	(19, 'HP Pro Mini 400 G9', '4G4N7AV', '7CH97862AJ', '2023-04-17 08:50:22', '2027-04-17 08:50:23', '478', '2023-03-16 14:20:00'),
	(20, 'HP Pro Mini 400 G9', '4G4N7AV', '7CH39272NA', '2023-04-17 08:50:22', '2027-04-17 08:50:23', '478', '2023-03-16 14:20:00'),
	(21, 'HP Pro Mini 400 G9', '4G4N7AV', '7CH97845LK', '2023-04-17 08:50:22', '2027-04-17 08:50:23', '478', '2023-03-16 14:20:00'),
	(22, 'HP Pro Mini 400 G9', '4G4N7AV', '7CH86748YM', '2023-04-17 08:50:22', '2027-04-17 08:50:23', '478', '2023-03-16 14:20:00'),
	(23, 'HP Pro Mini 400 G9', '4G4N7AV', '7CH54727HR', '2023-04-17 08:50:22', '2027-04-17 08:50:23', '478', '2023-03-16 14:20:00'),
	(24, 'HP Pro Mini 400 G9', '4G4N7AV', '7CH89995PM', '2023-04-17 08:50:22', '2027-04-17 08:50:23', '478', '2023-03-16 14:20:00'),
	(25, 'Synology', 'DS1821+', 'MSA-X25677QBAA', '2023-04-17 08:50:22', '2027-04-17 08:50:23', '1058', '2023-03-16 14:20:00'),
	(26, 'Synology', 'DS1821+', 'MSA-Z69827DDEA', '2023-04-17 08:50:22', '2027-04-17 08:50:23', '1058', '2023-03-16 14:20:00'),
	(27, 'Synology', 'DS1821+', 'MSA-S68268YWEU', '2023-04-17 08:50:22', '2027-04-17 08:50:23', '1058', '2023-03-16 14:20:00'),
	(28, 'Samsung 24" Business Monitor with IPS Panel', '24S40VA', 'LS24A400VEUXEN', '2023-03-16 15:20:00', '2027-03-16 15:20:00', '249', '2023-03-16 14:20:00'),
	(29, 'Samsung 24" Business Monitor with IPS Panel', '24S40VA', 'LS24A400EAUKLV', '2023-03-16 15:20:00', '2027-03-16 15:20:00', '249', '2023-03-16 14:20:00'),
	(30, 'Samsung 24" Business Monitor with IPS Panel', '24S40VA', 'LS24A400EEAPJZ', '2023-03-16 15:20:00', '2027-03-16 15:20:00', '249', '2023-03-16 14:20:00'),
	(31, 'Samsung 24" Business Monitor with IPS Panel', '24S40VA', 'LS24A400EEAPJ', '2023-03-16 15:20:00', '2027-03-16 15:20:00', '249', '2023-03-16 14:20:00'),
	(32, 'Samsung 24" Business Monitor with IPS Panel', '24S40VA', 'LS24A400UAELM', '2023-03-16 15:20:00', '2027-03-16 15:20:00', '249', '2023-03-16 14:20:00'),
	(33, 'Samsung 24" Business Monitor with IPS Panel', '24S40VA', 'LS24A400UAEHK', '2023-03-16 15:20:00', '2027-03-16 15:20:00', '249', '2023-03-16 14:20:00'),
	(34, 'Samsung 24" Business Monitor with IPS Panel', '24S40VA', 'LS24A400AUAPP', '2023-03-16 15:20:00', '2027-03-16 15:20:00', '249', '2023-03-16 14:20:00'),
	(35, 'Samsung 24" Business Monitor with IPS Panel', '24S40VA', 'LS24A400AUEVL', '2023-03-16 15:20:00', '2027-03-16 15:20:00', '249', '2023-03-16 14:20:00'),
	(36, 'Samsung 24" Business Monitor with IPS Panel', '24S40VA', 'LS24A400EEUTK', '2023-03-16 15:20:00', '2027-03-16 15:20:00', '249', '2023-03-16 14:20:00'),
	(37, 'Samsung 24" Business Monitor with IPS Panel', '24S40VA', 'LS24A400AEARF', '2023-03-16 15:20:00', '2027-03-16 15:20:00', '249', '2023-03-16 14:20:00'),
	(38, 'Samsung 24" Business Monitor with IPS Panel', '24S40VA', 'LS24A400AEUNC', '2023-03-16 15:20:00', '2027-03-16 15:20:00', '249', '2023-03-16 14:20:00');

-- Dumping structure for table besson_ethan_info_1a.t_personnes
DROP TABLE IF EXISTS `t_personnes`;
CREATE TABLE IF NOT EXISTS `t_personnes` (
  `id_personnes` int NOT NULL AUTO_INCREMENT,
  `prenom_pers` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_bin DEFAULT NULL,
  `nom_pers` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_bin DEFAULT NULL,
  `dep_pers` varchar(14) CHARACTER SET utf8mb3 COLLATE utf8mb3_bin DEFAULT NULL,
  `derniere_actualisation` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id_personnes`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;

-- Dumping data for table besson_ethan_info_1a.t_personnes: ~0 rows (approximately)
INSERT INTO `t_personnes` (`id_personnes`, `prenom_pers`, `nom_pers`, `dep_pers`, `derniere_actualisation`) VALUES
	(1, 'Darwin', 'Lamark', '502', '2023-03-15 09:59:44'),
	(2, 'Lara', 'Croft', '444', '2023-04-04 09:48:11'),
	(3, 'Tom', 'Chandler', '431', '2023-04-18 08:02:24'),
	(4, 'Infra', NULL, NULL, '2023-04-18 08:04:06');

-- Dumping structure for table besson_ethan_info_1a.t_personnes_ajout_materiel
DROP TABLE IF EXISTS `t_personnes_ajout_materiel`;
CREATE TABLE IF NOT EXISTS `t_personnes_ajout_materiel` (
  `id_personnes_ajout_materiel` int NOT NULL AUTO_INCREMENT,
  `fk_personnes` int DEFAULT NULL,
  `fk_materiel` int DEFAULT NULL,
  `date_ajout` datetime DEFAULT NULL,
  `derniere_actualisation` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id_personnes_ajout_materiel`),
  KEY `fk_t_personnes_has_t_materiel_t_materiel1` (`fk_materiel`),
  KEY `fk_t_personnes_has_t_materiel_t_personnes1` (`fk_personnes`),
  CONSTRAINT `fk_t_personnes_has_t_materiel_t_materiel1` FOREIGN KEY (`fk_materiel`) REFERENCES `t_materiel` (`id_materiel`) ON DELETE CASCADE ON UPDATE RESTRICT,
  CONSTRAINT `fk_t_personnes_has_t_materiel_t_personnes1` FOREIGN KEY (`fk_personnes`) REFERENCES `t_personnes` (`id_personnes`) ON DELETE CASCADE ON UPDATE RESTRICT
) ENGINE=InnoDB AUTO_INCREMENT=39 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;

-- Dumping data for table besson_ethan_info_1a.t_personnes_ajout_materiel: ~0 rows (approximately)
INSERT INTO `t_personnes_ajout_materiel` (`id_personnes_ajout_materiel`, `fk_personnes`, `fk_materiel`, `date_ajout`, `derniere_actualisation`) VALUES
	(1, 1, 1, '2023-04-18 10:06:23', '2023-04-18 08:09:11'),
	(2, 1, 2, '2023-04-18 10:06:23', '2023-04-18 08:09:11'),
	(3, 1, 3, '2023-04-18 10:06:23', '2023-04-18 08:09:13'),
	(4, 1, 4, '2023-04-18 10:06:23', '2023-04-18 08:09:13'),
	(5, 1, 5, '2023-04-18 10:06:23', '2023-04-18 08:09:14'),
	(6, 1, 6, '2023-04-18 10:06:23', '2023-04-18 08:09:15'),
	(7, 1, 7, '2023-04-18 10:06:23', '2023-04-18 08:09:16'),
	(8, 1, 8, '2023-04-18 10:06:23', '2023-04-18 08:09:17'),
	(9, 1, 9, '2023-04-18 10:06:23', '2023-04-18 08:09:18'),
	(10, 1, 10, '2023-04-18 10:06:23', '2023-04-18 08:09:19'),
	(11, 1, 11, '2023-04-18 10:06:23', '2023-04-18 08:09:20'),
	(12, 1, 12, '2023-04-18 10:06:23', '2023-04-18 08:09:21'),
	(13, 1, 13, '2023-04-18 10:06:23', '2023-04-18 08:09:21'),
	(14, 1, 14, '2023-04-18 10:06:23', '2023-04-18 08:09:22'),
	(15, 1, 15, '2023-04-18 10:06:23', '2023-04-18 08:09:24'),
	(16, 1, 16, '2023-04-18 10:06:23', '2023-04-18 08:09:25'),
	(17, 1, 17, '2023-04-18 10:06:23', '2023-04-18 08:09:25'),
	(18, 1, 18, '2023-04-18 10:06:23', '2023-04-18 08:09:28'),
	(19, 1, 19, '2023-04-18 10:06:23', '2023-04-18 08:09:30'),
	(20, 1, 20, '2023-04-18 10:06:23', '2023-04-18 08:09:31'),
	(21, 1, 21, '2023-04-18 10:06:23', '2023-04-18 08:09:32'),
	(22, 1, 22, '2023-04-18 10:06:23', '2023-04-18 08:09:34'),
	(23, 1, 23, '2023-04-18 10:06:23', '2023-04-18 08:09:38'),
	(24, 1, 24, '2023-04-18 10:06:23', '2023-04-18 08:09:35'),
	(25, 1, 25, '2023-04-18 10:06:23', '2023-04-18 08:09:38'),
	(26, 1, 26, '2023-04-18 10:06:23', '2023-04-18 08:09:39'),
	(27, 1, 27, '2023-04-18 10:06:23', '2023-04-18 08:09:40'),
	(28, 1, 28, '2023-04-18 10:06:23', '2023-04-18 08:09:40'),
	(29, 1, 29, '2023-04-18 10:06:23', '2023-04-18 08:09:40'),
	(30, 1, 30, '2023-04-18 10:06:23', '2023-04-18 08:09:41'),
	(31, 1, 31, '2023-04-18 10:06:23', '2023-04-18 08:09:41'),
	(32, 1, 32, '2023-04-18 10:06:23', '2023-04-18 08:09:41'),
	(33, 1, 33, '2023-04-18 10:06:23', '2023-04-18 08:09:44'),
	(34, 1, 34, '2023-04-18 10:06:23', '2023-04-18 08:09:43'),
	(35, 1, 35, '2023-04-18 10:06:23', '2023-04-18 08:09:43'),
	(36, 1, 36, '2023-04-18 10:06:23', '2023-04-18 08:09:49'),
	(37, 1, 37, '2023-04-18 10:06:23', '2023-04-18 08:09:47'),
	(38, 1, 38, '2023-04-18 10:06:23', '2023-04-18 08:09:47');

-- Dumping structure for table besson_ethan_info_1a.t_personnes_avoir_materiel
DROP TABLE IF EXISTS `t_personnes_avoir_materiel`;
CREATE TABLE IF NOT EXISTS `t_personnes_avoir_materiel` (
  `id_personnes_avoir_materiel` int NOT NULL AUTO_INCREMENT,
  `fk_personnes` int DEFAULT NULL,
  `fk_materiel` int DEFAULT NULL,
  `derniere_actualisation` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id_personnes_avoir_materiel`),
  KEY `fk_t_personnes_has_t_materiel_t_materiel` (`fk_materiel`),
  KEY `fk_t_personnes_has_t_materiel_t_personnes` (`fk_personnes`),
  CONSTRAINT `fk_t_personnes_has_t_materiel_t_materiel` FOREIGN KEY (`fk_materiel`) REFERENCES `t_materiel` (`id_materiel`) ON DELETE CASCADE ON UPDATE RESTRICT,
  CONSTRAINT `fk_t_personnes_has_t_materiel_t_personnes` FOREIGN KEY (`fk_personnes`) REFERENCES `t_personnes` (`id_personnes`) ON DELETE CASCADE ON UPDATE RESTRICT
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;

-- Dumping data for table besson_ethan_info_1a.t_personnes_avoir_materiel: ~0 rows (approximately)
INSERT INTO `t_personnes_avoir_materiel` (`id_personnes_avoir_materiel`, `fk_personnes`, `fk_materiel`, `derniere_actualisation`) VALUES
	(1, 1, 1, '2023-04-18 08:00:45'),
	(2, 1, 13, '2023-04-18 08:01:09'),
	(3, 2, 2, '2023-04-18 08:01:19'),
	(4, 2, 14, '2023-04-18 08:01:29'),
	(5, 3, 3, '2023-04-18 08:02:44'),
	(6, 3, 15, '2023-04-18 08:02:53'),
	(7, 1, 28, '2023-04-18 08:03:02'),
	(8, 2, 29, '2023-04-18 08:03:14'),
	(9, 3, 30, '2023-04-18 08:03:24'),
	(10, 3, 31, '2023-04-18 08:03:33'),
	(11, 4, 25, '2023-04-18 08:04:25'),
	(12, 4, 26, '2023-04-18 08:04:25'),
	(13, 4, 27, '2023-04-18 08:04:25');

-- Dumping structure for table besson_ethan_info_1a.t_personnes_retrait_materiel
DROP TABLE IF EXISTS `t_personnes_retrait_materiel`;
CREATE TABLE IF NOT EXISTS `t_personnes_retrait_materiel` (
  `id_personnes_retrait_materiel` int NOT NULL AUTO_INCREMENT,
  `fk_personnes` int DEFAULT NULL,
  `fk_materiel` int DEFAULT NULL,
  `date_retrait` datetime DEFAULT NULL,
  `derniere_actualisation` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id_personnes_retrait_materiel`),
  KEY `fk_t_personnes_has_t_materiel_t_materiel2` (`fk_materiel`),
  KEY `fk_t_personnes_has_t_materiel_t_personnes2` (`fk_personnes`),
  CONSTRAINT `fk_t_personnes_has_t_materiel_t_materiel2` FOREIGN KEY (`fk_materiel`) REFERENCES `t_materiel` (`id_materiel`) ON DELETE CASCADE ON UPDATE RESTRICT,
  CONSTRAINT `fk_t_personnes_has_t_materiel_t_personnes2` FOREIGN KEY (`fk_personnes`) REFERENCES `t_personnes` (`id_personnes`) ON DELETE CASCADE ON UPDATE RESTRICT
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;

-- Dumping data for table besson_ethan_info_1a.t_personnes_retrait_materiel: ~1 rows (approximately)
INSERT INTO `t_personnes_retrait_materiel` (`id_personnes_retrait_materiel`, `fk_personnes`, `fk_materiel`, `date_retrait`, `derniere_actualisation`) VALUES
	(1, 2, 14, '2023-04-18 10:11:02', '2023-04-18 08:11:03');

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
