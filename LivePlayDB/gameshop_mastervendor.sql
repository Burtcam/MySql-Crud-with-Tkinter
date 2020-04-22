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
-- Table structure for table `mastervendor`
--

DROP TABLE IF EXISTS `mastervendor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mastervendor` (
  `vendorId` char(48) NOT NULL,
  `contactName` char(50) DEFAULT NULL,
  `vendorName` char(48) NOT NULL,
  `country` varchar(48) DEFAULT NULL,
  `state` varchar(48) DEFAULT NULL,
  `zip` int DEFAULT NULL,
  `address` varchar(50) DEFAULT NULL,
  `termsID` char(12) DEFAULT NULL,
  PRIMARY KEY (`vendorId`),
  KEY `FK_terms` (`termsID`),
  CONSTRAINT `FK_terms` FOREIGN KEY (`termsID`) REFERENCES `termscodes` (`termsID`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mastervendor`
--

LOCK TABLES `mastervendor` WRITE;
/*!40000 ALTER TABLE `mastervendor` DISABLE KEYS */;
INSERT INTO `mastervendor` VALUES ('ABCWIDGET','BOB','ABC Widget Company',NULL,NULL,NULL,NULL,'net30'),('Corona','Dr Fauci','White House','CHN','RI',2852,'6548 Blah blah blah street','Net120'),('HTEi','Bill','SCHWABB','USA','DC',54659,'243 Every place drive','net30'),('KYUNG','bob smith','Kyung Unlimited','CHI','Wuhan',55555,'110 someplace drive','net30'),('owei','Dokd','dlkjfskljf','USA','AR',54545,'Hello street 34','net30'),('testvendor1','gary','vendor name','USA','RI',2852,'555 whyyouasking blvd','net30');
/*!40000 ALTER TABLE `mastervendor` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-04-22 13:41:54
