-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: train
-- ------------------------------------------------------
-- Server version	8.4.0
use train;
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
-- Table structure for table `document`
--

DROP TABLE IF EXISTS `document`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `document` (
  `idDocument` int NOT NULL,
  `idTypeDocument` int NOT NULL,
  `number` int NOT NULL,
  PRIMARY KEY (`idDocument`),
  KEY `fk_document_type_document1_idx` (`idTypeDocument`),
  CONSTRAINT `fk_document_type_document1` FOREIGN KEY (`idTypeDocument`) REFERENCES `type_document` (`idTypeDocument`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `document`
--

LOCK TABLES `document` WRITE;
/*!40000 ALTER TABLE `document` DISABLE KEYS */;
INSERT INTO `document` VALUES (1,1,12345678),(2,2,87654321),(3,3,13579246),(4,1,24681357);
/*!40000 ALTER TABLE `document` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `flight`
--

DROP TABLE IF EXISTS `flight`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
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
INSERT INTO `flight` VALUES (1,'Flight 101','2023-11-01'),(2,'Flight 202','2023-11-02'),(3,'Flight 303','2023-11-03');
/*!40000 ALTER TABLE `flight` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `list_status`
--

DROP TABLE IF EXISTS `list_status`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `list_status` (
  `idStatus` int NOT NULL,
  `title` varchar(45) NOT NULL,
  PRIMARY KEY (`idStatus`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `list_status`
--

LOCK TABLES `list_status` WRITE;
/*!40000 ALTER TABLE `list_status` DISABLE KEYS */;
INSERT INTO `list_status` VALUES (1,'Завершен'),(2,'Отменён'),(3,'Подтверждён'),(4,'Проверяется');
/*!40000 ALTER TABLE `list_status` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `passenger`
--

DROP TABLE IF EXISTS `passenger`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
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
INSERT INTO `passenger` VALUES (1,1,'John','Doe',NULL,'M','1990-01-01'),(2,2,'Jane','Smith','Ann','F','1985-05-12'),(3,3,'Alice','Johnson',NULL,'F','1992-07-23'),(4,4,'Bob','Brown',NULL,'M','1980-12-15');
/*!40000 ALTER TABLE `passenger` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `railcar`
--

DROP TABLE IF EXISTS `railcar`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
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
INSERT INTO `railcar` VALUES (1,1,'Economy','Standard',100),(2,2,'Business','Premium',50),(3,3,'First Class','Luxury',20);
/*!40000 ALTER TABLE `railcar` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `station`
--

DROP TABLE IF EXISTS `station`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `station` (
  `idStation` int NOT NULL,
  `title` varchar(45) NOT NULL,
  `city` varchar(45) NOT NULL,
  PRIMARY KEY (`idStation`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `station`
--

LOCK TABLES `station` WRITE;
/*!40000 ALTER TABLE `station` DISABLE KEYS */;
INSERT INTO `station` VALUES (1,'Station A','City One'),(2,'Station B','City Two'),(3,'Station C','City Three');
/*!40000 ALTER TABLE `station` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ticket`
--

DROP TABLE IF EXISTS `ticket`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ticket` (
  `idTicket` int NOT NULL,
  `idUser` int NOT NULL,
  `idRailcar` int NOT NULL,
  `idPassenger` int NOT NULL,
  `idStatus` int NOT NULL,
  `price` int NOT NULL,
  PRIMARY KEY (`idTicket`),
  KEY `fk_ticket_user_idx` (`idUser`),
  KEY `fk_ticket_railcar1_idx` (`idRailcar`),
  KEY `fk_ticket_passenger1_idx` (`idPassenger`),
  KEY `fk_ticket_list_status1_idx` (`idStatus`),
  CONSTRAINT `fk_ticket_list_status1` FOREIGN KEY (`idStatus`) REFERENCES `list_status` (`idStatus`),
  CONSTRAINT `fk_ticket_passenger1` FOREIGN KEY (`idPassenger`) REFERENCES `passenger` (`idPassenger`),
  CONSTRAINT `fk_ticket_railcar1` FOREIGN KEY (`idRailcar`) REFERENCES `railcar` (`idRailcar`),
  CONSTRAINT `fk_ticket_user` FOREIGN KEY (`idUser`) REFERENCES `user` (`idUser`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ticket`
--

LOCK TABLES `ticket` WRITE;
/*!40000 ALTER TABLE `ticket` DISABLE KEYS */;
INSERT INTO `ticket` VALUES (1,4,1,1,1,1500),(2,4,2,2,2,3000),(3,4,3,3,2,2500),(4,4,1,4,4,4000);
/*!40000 ALTER TABLE `ticket` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `timetable`
--

DROP TABLE IF EXISTS `timetable`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `timetable` (
  `idStation` int NOT NULL,
  `idFlight` int NOT NULL,
  `arrival` time NOT NULL,
  `departure` time NOT NULL,
  PRIMARY KEY (`idFlight`,`idStation`),
  KEY `fk_Timetable_flight1_idx` (`idFlight`),
  KEY `fk_timetable_station1_idx` (`idStation`),
  CONSTRAINT `fk_Timetable_flight1` FOREIGN KEY (`idFlight`) REFERENCES `flight` (`idFlight`),
  CONSTRAINT `fk_timetable_station1` FOREIGN KEY (`idStation`) REFERENCES `station` (`idStation`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `timetable`
--

LOCK TABLES `timetable` WRITE;
/*!40000 ALTER TABLE `timetable` DISABLE KEYS */;
INSERT INTO `timetable` VALUES (1,1,'10:00:00','12:00:00'),(2,2,'14:00:00','16:00:00'),(3,3,'18:00:00','20:00:00');
/*!40000 ALTER TABLE `timetable` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `type_document`
--

DROP TABLE IF EXISTS `type_document`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `type_document` (
  `idTypeDocument` int NOT NULL,
  `title` varchar(45) NOT NULL,
  PRIMARY KEY (`idTypeDocument`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `type_document`
--

LOCK TABLES `type_document` WRITE;
/*!40000 ALTER TABLE `type_document` DISABLE KEYS */;
INSERT INTO `type_document` VALUES (1,'Паспорт'),(2,'Военный билет'),(3,'Лицензия документов');
/*!40000 ALTER TABLE `type_document` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
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
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'admin@mail.ru','admin','Steve','Jobs','Yakov','+79197629181','2002-12-10'),(2,'test@mail.ru','testpassword','testname','testsurname','testpatronymic','+79999999999','2000-01-01'),(3,'user_1@gmail.com','random_password',NULL,NULL,NULL,NULL,NULL),(4,'1','1','1','1','1','1','2000-01-01');
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

-- Dump completed on 2024-11-23  0:28:14
