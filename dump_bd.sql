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

DROP TABLE IF EXISTS `document`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
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
 SET character_set_client = utf8mb4 ;
CREATE TABLE `flight` (
  `idFlight` int NOT NULL,
  `title` varchar(45) NOT NULL,
  PRIMARY KEY (`idFlight`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COMMENT='																													';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `flight`
--

LOCK TABLES `flight` WRITE;
/*!40000 ALTER TABLE `flight` DISABLE KEYS */;
INSERT INTO `flight` VALUES (1,'Flight 101'),(2,'Flight 202'),(3,'Flight 303'),(4,'Flight 434'),(5,'Flight 501'),(6,'Flight 625'),(7,'Flight 705'),(8,'Flight 811'),(9,'Flight 961'),(10,'Flight 109');
/*!40000 ALTER TABLE `flight` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `list_status`
--

DROP TABLE IF EXISTS `list_status`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
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
INSERT INTO `passenger` VALUES (1,1,'John','Doe',NULL,'M','1990-01-01'),(2,2,'Jane','Smith','Ann','F','1985-05-12'),(3,3,'Alice','Johnson',NULL,'F','1992-07-23'),(4,4,'Bob','Brown',NULL,'M','1980-12-15');
/*!40000 ALTER TABLE `passenger` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `railcar`
--

DROP TABLE IF EXISTS `railcar`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `railcar` (
  `idRailcar` int NOT NULL AUTO_INCREMENT,
  `idFlight` int NOT NULL,
  `type` varchar(45) NOT NULL,
  `class_of_service` varchar(45) NOT NULL,
  `count_of_seat` int NOT NULL,
  `price` int NOT NULL,
  PRIMARY KEY (`idRailcar`),
  KEY `fk_railcar_flight1_idx` (`idFlight`),
  CONSTRAINT `fk_railcar_flight1` FOREIGN KEY (`idFlight`) REFERENCES `flight` (`idFlight`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `railcar`
--

LOCK TABLES `railcar` WRITE;
/*!40000 ALTER TABLE `railcar` DISABLE KEYS */;
INSERT INTO `railcar` VALUES (1,1,'Плацкарт','Обычный',100,100),(2,2,'Купе','Премиум',50,5200),(3,3,'Купе','Бизнес',25,1250),(4,1,'Купе','Бизнес',25,5000),(5,3,'Экспресс','Премиум',15,12500),(6,4,'Купе','Бизнес',25,3000),(7,5,'Люкс','Люкс',15,8000),(8,5,'Плацкарт','Обычный',100,1200),(9,6,'Сидячий','Эконом',100,600),(10,7,'Купе','Премиум',50,3500),(11,8,'Люкс','Люкс',15,12000),(12,9,'Плацкарт','Обычный',100,1100),(13,10,'Купе','Бизнес',25,4000);
/*!40000 ALTER TABLE `railcar` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `station`
--

DROP TABLE IF EXISTS `station`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
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
INSERT INTO `station` VALUES (1,'Казанский','Москва'),(2,'Ярославский','Санкт-Петербург'),(3,'Южный','Воронеж'),(4,'Белорусский','Москва'),(5,'Курский','Москва'),(6,'Новосибирский','Новосибирск'),(7,'Калининский','Санкт-Петербург'),(8,'Витебский','Санкт-Петербург'),(9,'Нижегородский','Нижний Новгород'),(10,'Тракторостроителей','Челябинск'),(11,'Ростовский','Ростов-на-Дону'),(12,'Тула','Тула'),(13,'Кострома','Кострома'),(14,'Рязань','Рязань'),(15,'Уфа','Уфа'),(16,'Воронежский','Воронеж'),(17,'Саратовский','Саратов'),(18,'Самарский','Самара'),(19,'Иркутский','Иркутск'),(20,'Хабаровский','Хабаровск'),(21,'Омский','Омск'),(22,'Чебоксарский','Чебоксары'),(23,'Томский','Томск'),(24,'Краснодарский','Краснодар'),(25,'Петрозаводский','Петрозаводск'),(26,'Калининградский','Калининград'),(27,'Смоленский','Смоленск'),(28,'Липецкий','Липецк'),(29,'Астраханский','Астрахань'),(30,'Сургутский','Сургут');
/*!40000 ALTER TABLE `station` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ticket`
--

DROP TABLE IF EXISTS `ticket`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `ticket` (
  `idTicket` int NOT NULL AUTO_INCREMENT,
  `idUser` int NOT NULL,
  `idRailcar` int NOT NULL,
  `idPassenger` int NOT NULL,
  `idStatus` int NOT NULL,
  `idFlight` int NOT NULL,
  PRIMARY KEY (`idTicket`),
  KEY `fk_ticket_user_idx` (`idUser`),
  KEY `fk_ticket_railcar1_idx` (`idRailcar`),
  KEY `fk_ticket_passenger1_idx` (`idPassenger`),
  KEY `fk_ticket_list_status1_idx` (`idStatus`),
  KEY `fk_ticket_flight1_idx` (`idFlight`),
  CONSTRAINT `fk_ticket_flight1` FOREIGN KEY (`idFlight`) REFERENCES `flight` (`idFlight`),
  CONSTRAINT `fk_ticket_list_status1` FOREIGN KEY (`idStatus`) REFERENCES `list_status` (`idStatus`),
  CONSTRAINT `fk_ticket_passenger1` FOREIGN KEY (`idPassenger`) REFERENCES `passenger` (`idPassenger`),
  CONSTRAINT `fk_ticket_railcar1` FOREIGN KEY (`idRailcar`) REFERENCES `railcar` (`idRailcar`),
  CONSTRAINT `fk_ticket_user` FOREIGN KEY (`idUser`) REFERENCES `user` (`idUser`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ticket`
--

LOCK TABLES `ticket` WRITE;
/*!40000 ALTER TABLE `ticket` DISABLE KEYS */;
INSERT INTO `ticket` VALUES (1,4,2,2,3,2),(2,4,1,2,2,1),(4,4,1,1,3,1);
/*!40000 ALTER TABLE `ticket` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `timetable`
--

DROP TABLE IF EXISTS `timetable`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `timetable` (
  `idStation` int NOT NULL,
  `idFlight` int NOT NULL,
  `arrival` datetime NOT NULL,
  `departure` datetime NOT NULL,
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
INSERT INTO `timetable` VALUES (1,1,'2020-10-01 08:00:00','2020-10-01 08:30:00'),(4,1,'2020-10-01 11:00:00','2020-10-01 11:30:00'),(5,1,'2020-10-01 12:45:00','2020-10-01 13:20:00'),(1,2,'2020-10-01 11:00:00','2020-10-01 11:30:00'),(2,2,'2020-10-01 08:00:00','2020-10-01 08:30:00'),(3,2,'2020-10-01 12:45:00','2020-10-01 13:20:00'),(1,3,'2020-10-01 12:45:00','2020-10-01 13:20:00'),(2,3,'2020-10-01 11:00:00','2020-10-01 11:30:00'),(4,3,'2020-10-01 08:00:00','2020-10-01 08:30:00'),(5,3,'2020-10-01 14:55:00','2020-10-01 20:20:00'),(7,3,'2023-10-02 19:00:00','2023-10-02 17:00:00'),(7,4,'2023-10-01 16:00:00','2023-10-01 14:00:00'),(8,5,'2023-10-01 18:00:00','2023-10-01 16:00:00'),(1,6,'2023-10-01 20:00:00','2023-10-01 18:00:00'),(9,6,'2023-10-02 23:30:00','2023-10-02 21:30:00'),(2,7,'2023-10-02 10:00:00','2023-10-02 08:00:00'),(3,8,'2023-10-02 11:30:00','2023-10-02 09:30:00'),(4,9,'2023-10-02 13:45:00','2023-10-02 11:45:00'),(6,10,'2023-10-02 17:30:00','2023-10-02 15:30:00'),(10,10,'2023-10-02 15:00:00','2023-10-02 13:00:00');
/*!40000 ALTER TABLE `timetable` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `type_document`
--

DROP TABLE IF EXISTS `type_document`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
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
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'admin@mail.ru','admin','Steve','Jobs','Yakov','+79197629181','2002-12-10'),(2,'test@mail.ru','testpassword','testname','testsurname','testpatronymic','+79999999999','2000-01-01'),(3,'user_1@gmail.com','random_password',NULL,NULL,NULL,NULL,NULL),(4,'1','1','Сергей','Пронин','Дмитриевич','+71234567890','2002-01-15'),(6,'test@mail.ru','random_password',NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'train'
--
/*!50003 DROP PROCEDURE IF EXISTS `railcar_filter` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `railcar_filter`(IN id_flight INT)
BEGIN
	SELECT  distinct `type`
	FROM railcar AS r
	LEFT JOIN (
		select idRailcar, count(idTicket) as "seat"
		from ticket
		where idStatus = 3
		group by idRailcar) as t ON t.idRailcar = r.idRailcar
	WHERE r.idFlight = id_flight;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `railcar_table` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `railcar_table`(IN id_flight INT)
BEGIN
	SELECT  r.idRailcar, r.count_of_seat - COALESCE(t.seat, 0), r.class_of_service, r.type, r.price
	FROM railcar AS r
	LEFT JOIN (
		select idRailcar, count(idTicket) as "seat"
		from ticket
		where idStatus = 3
		group by idRailcar) as t ON t.idRailcar = r.idRailcar
	WHERE r.idFlight = id_flight;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `tickets_common` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `tickets_common`()
BEGIN
SELECT 
    f.idFlight,
    (SELECT CONCAT(s1.title, " ",s1.city)
     FROM timetable AS tt1 
     JOIN station AS s1 ON tt1.idStation = s1.idStation 
     WHERE tt1.idFlight = f.idFlight 
       AND tt1.departure = MIN(tt.departure)) AS "Откуда",
    (SELECT CONCAT(s2.title, " ", s2.city)
     FROM timetable AS tt2 
     JOIN station AS s2 ON tt2.idStation = s2.idStation 
     WHERE tt2.idFlight = f.idFlight 
       AND tt2.arrival = MAX(tt.arrival)) AS "Куда",
	MIN(tt.departure) AS "Время отправки",
    MAX(tt.arrival) AS "Время прибытия",
        s.seat as "Кол-во мест",
    p.price as "Минимальная цена"
FROM flight AS f
JOIN timetable AS tt ON f.idFlight = tt.idFlight
JOIN (
	SELECT DISTINCT r.idFlight, min(price) as "price"
	FROM railcar as r
	JOIN flight as f ON f.idFlight = r.idFlight
	GROUP BY r.idFlight
) as p ON p.idFlight = f.idFlight
JOIN (
	SELECT f.idFlight, (sum(r.count_of_seat) - count(t.idTicket)) as "seat"
	FROM railcar as r
	JOIN flight as f ON f.idFlight = r.idFlight
	LEFT JOIN (select * from ticket where idStatus = 3) as t ON t.idRailcar = r.idRailcar
    group by f.idFlight
) as s ON s.idFlight = f.idFlight
GROUP BY f.idFlight;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `tickets_extended` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `tickets_extended`(IN first_station VARCHAR(45), IN last_station VARCHAR(45), IN `date` DATE)
BEGIN

SELECT idStation INTO first_station
FROM station
WHERE title = first_station;
    
SELECT idStation INTO last_station
FROM station
WHERE title = last_station;


SELECT t1.idFlight,
       CONCAT(t1.title, ' ',t1.city) as "Откуда",
       CONCAT(t2.title, ' ',t2.city) as "Куда",
       t1.departure AS "Время отправки",
       MAX(t2.arrival) AS "Время прибытия",  -- Здесь используем MAX
       s.seat AS "Кол-во мест",
       p.price AS "Минимальная цена"
FROM (
    SELECT t.idFlight, s.title, s.city, t.departure
    FROM timetable AS t
    JOIN station AS s ON s.idStation = t.idStation
    WHERE t.idStation = first_station 
      AND t.idFlight IN (
          SELECT t1.idFlight
          FROM timetable AS t1
          JOIN timetable AS t2 ON t1.idFlight = t2.idFlight
          WHERE t1.idStation = first_station
            AND t2.idStation = last_station
            AND t1.departure < t2.departure)
) AS t1
JOIN (
    SELECT t.idFlight, s.title, s.city, t.arrival
    FROM timetable AS t
    JOIN station AS s ON s.idStation = t.idStation
    WHERE t.idStation = last_station 
      AND t.idFlight IN (
          SELECT t1.idFlight
          FROM timetable AS t1
          JOIN timetable AS t2 ON t1.idFlight = t2.idFlight
          WHERE t1.idStation = first_station
            AND t2.idStation = last_station
            AND t1.departure < t2.departure)
) AS t2 ON t2.idFlight = t1.idFlight
JOIN (
    SELECT DISTINCT r.idFlight, MIN(price) AS "price"
    FROM railcar AS r
    JOIN flight AS f ON f.idFlight = r.idFlight
    GROUP BY r.idFlight
) AS p ON t1.idFlight = p.idFlight
JOIN (
    SELECT f.idFlight, (sum(r.count_of_seat) - count(t.idTicket)) as "seat"
	FROM railcar as r
	JOIN flight as f ON f.idFlight = r.idFlight
	LEFT JOIN (select * from ticket where idStatus = 3) as t ON t.idRailcar = r.idRailcar
    group by f.idFlight
) AS s ON t1.idFlight = s.idFlight
GROUP BY t1.idFlight, t1.title, t1.departure, t2.title, t1.city, t2.city, s.seat, p.price  -- Группируем по этим полям
HAVING DATE(MAX(t2.arrival)) = `date`
LIMIT 0, 1000;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-12-04 18:53:36
