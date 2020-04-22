CREATE DATABASE  IF NOT EXISTS `gameshop` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `gameshop`;
-- MySQL dump 10.13  Distrib 8.0.19, for Win64 (x86_64)
--
-- Host: localhost    Database: gameshop
-- ------------------------------------------------------
-- Server version	8.0.19

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `masteritem`
--

DROP TABLE IF EXISTS `masteritem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `masteritem` (
  `itemID` char(48) NOT NULL,
  `lastPriceChange` date DEFAULT NULL,
  `previousCost` float DEFAULT NULL,
  `vendorId` char(48) NOT NULL,
  `cost` float NOT NULL,
  `intialPurchaseDate` datetime DEFAULT NULL,
  PRIMARY KEY (`itemID`),
  KEY `vendorId` (`vendorId`),
  CONSTRAINT `masteritem_ibfk_1` FOREIGN KEY (`vendorId`) REFERENCES `mastervendor` (`vendorId`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `masteritem`
--

LOCK TABLES `masteritem` WRITE;
/*!40000 ALTER TABLE `masteritem` DISABLE KEYS */;
INSERT INTO `masteritem` VALUES ('3D459',NULL,NULL,'testvendor1',5,'0000-00-00 00:00:00'),('54ewe',NULL,NULL,'owei',64.4,NULL),('c-19',NULL,NULL,'Corona',10,NULL),('Christina',NULL,NULL,'HTEi',65.4,NULL),('dse',NULL,NULL,'Corona',6.4,'2020-04-20 21:02:46'),('Finaltest',NULL,NULL,'KYUNG',65,'2020-04-22 13:38:06'),('I10000','0000-00-00',4.5,'testvendor1',6.5,'0000-00-00 00:00:00'),('I11000','0000-00-00',6.5,'testvendor1',8.5,'0000-00-00 00:00:00'),('Test39',NULL,NULL,'owei',65,NULL),('Test554',NULL,NULL,'ABCWIDGET',54,NULL);
/*!40000 ALTER TABLE `masteritem` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-04-22 13:41:55
