-- MySQL dump 10.13  Distrib 8.0.16, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: train
-- ------------------------------------------------------
-- Server version	8.3.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `document`
--
use train;

DROP TABLE IF EXISTS `document`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `document` (
  `idDocument` int NOT NULL,
  `typeDocument` varchar(45) NOT NULL,
  `number` int NOT NULL,
  PRIMARY KEY (`idDocument`),
  KEY `fk_Document_TypesOfDocument1_idx` (`typeDocument`),
  CONSTRAINT `fk_Document_TypesOfDocument1` FOREIGN KEY (`typeDocument`) REFERENCES `typedocument` (`typeDocument`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `document`
--

LOCK TABLES `document` WRITE;
/*!40000 ALTER TABLE `document` DISABLE KEYS */;
/*!40000 ALTER TABLE `document` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `flight`
--

DROP TABLE IF EXISTS `flight`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `flight` (
  `idFlight` int NOT NULL,
  `title` varchar(45) NOT NULL,
  `date` date NOT NULL,
  PRIMARY KEY (`idFlight`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COMMENT='																													';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `flight`
--

LOCK TABLES `flight` WRITE;
/*!40000 ALTER TABLE `flight` DISABLE KEYS */;
/*!40000 ALTER TABLE `flight` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `passenger`
--

DROP TABLE IF EXISTS `passenger`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `passenger` (
  `idPassenger` int NOT NULL,
  `idDocument` int NOT NULL,
  `name` varchar(45) NOT NULL,
  `surname` varchar(45) NOT NULL,
  `patronymic` varchar(45) DEFAULT NULL,
  `gender` varchar(45) NOT NULL,
  `birthday` varchar(45) NOT NULL,
  PRIMARY KEY (`idPassenger`),
  KEY `fk_Passenger_Document1_idx` (`idDocument`),
  CONSTRAINT `fk_Passenger_Document1` FOREIGN KEY (`idDocument`) REFERENCES `document` (`idDocument`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `passenger`
--

LOCK TABLES `passenger` WRITE;
/*!40000 ALTER TABLE `passenger` DISABLE KEYS */;
/*!40000 ALTER TABLE `passenger` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `railcar`
--

DROP TABLE IF EXISTS `railcar`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `railcar` (
  `idRailcar` int NOT NULL,
  `idFlight` int NOT NULL,
  `type` varchar(45) NOT NULL,
  `class_of_service` varchar(45) NOT NULL,
  `countOfSeat` int NOT NULL,
  PRIMARY KEY (`idRailcar`),
  KEY `fk_railcar_flight1_idx` (`idFlight`),
  CONSTRAINT `fk_railcar_flight1` FOREIGN KEY (`idFlight`) REFERENCES `flight` (`idFlight`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `railcar`
--

LOCK TABLES `railcar` WRITE;
/*!40000 ALTER TABLE `railcar` DISABLE KEYS */;
/*!40000 ALTER TABLE `railcar` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `station`
--

DROP TABLE IF EXISTS `station`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `station` (
  `titleStation` varchar(45) NOT NULL,
  `city` varchar(45) NOT NULL,
  PRIMARY KEY (`titleStation`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `station`
--

LOCK TABLES `station` WRITE;
/*!40000 ALTER TABLE `station` DISABLE KEYS */;
/*!40000 ALTER TABLE `station` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ticket`
--

DROP TABLE IF EXISTS `ticket`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `ticket` (
  `idTicket` int NOT NULL,
  `idRailcar` int NOT NULL,
  `idPassenger` int NOT NULL,
  `idUser` int NOT NULL,
  `price` int NOT NULL,
  `status` varchar(45) NOT NULL,
  PRIMARY KEY (`idTicket`),
  KEY `fk_Ticket_Railcar1_idx` (`idRailcar`),
  KEY `fk_Ticket_Passenger1_idx` (`idPassenger`),
  KEY `fk_ticket_user1_idx` (`idUser`),
  CONSTRAINT `fk_Ticket_Passenger1` FOREIGN KEY (`idPassenger`) REFERENCES `passenger` (`idPassenger`),
  CONSTRAINT `fk_Ticket_Railcar1` FOREIGN KEY (`idRailcar`) REFERENCES `railcar` (`idRailcar`),
  CONSTRAINT `fk_ticket_user1` FOREIGN KEY (`idUser`) REFERENCES `user` (`idUser`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ticket`
--

LOCK TABLES `ticket` WRITE;
/*!40000 ALTER TABLE `ticket` DISABLE KEYS */;
/*!40000 ALTER TABLE `ticket` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `timetable`
--

DROP TABLE IF EXISTS `timetable`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `timetable` (
  `titleStation` varchar(45) NOT NULL,
  `idFlight` int NOT NULL,
  `arrival` time NOT NULL,
  `departure` time NOT NULL,
  PRIMARY KEY (`titleStation`,`idFlight`),
  KEY `fk_Timetable_Station1_idx` (`titleStation`),
  KEY `fk_Timetable_flight1_idx` (`idFlight`),
  CONSTRAINT `fk_Timetable_flight1` FOREIGN KEY (`idFlight`) REFERENCES `flight` (`idFlight`),
  CONSTRAINT `fk_Timetable_Station1` FOREIGN KEY (`titleStation`) REFERENCES `station` (`titleStation`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `timetable`
--

LOCK TABLES `timetable` WRITE;
/*!40000 ALTER TABLE `timetable` DISABLE KEYS */;
/*!40000 ALTER TABLE `timetable` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `typedocument`
--

DROP TABLE IF EXISTS `typedocument`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `typedocument` (
  `typeDocument` varchar(45) NOT NULL,
  PRIMARY KEY (`typeDocument`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `typedocument`
--

LOCK TABLES `typedocument` WRITE;
/*!40000 ALTER TABLE `typedocument` DISABLE KEYS */;
/*!40000 ALTER TABLE `typedocument` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `user` (
  `idUser` int NOT NULL AUTO_INCREMENT,
  `email` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `password` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `name` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `surname` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `patronymic` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `phone` varchar(12) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `birthday` date DEFAULT NULL,
  PRIMARY KEY (`idUser`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'admin@mail.ru','admin','Steve','Jobs','Yakov','+79197629181','2002-12-10'),(2,'test@mail.ru','testpassword','testname','testsurname','testpatronymic','+79999999999','2000-01-01'),(3,'user_1@gmail.com','random_password',NULL,NULL,NULL,NULL,NULL),(4,'1','1','1','1','1','<12sa','2000-01-01');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-11-22 16:00:46
