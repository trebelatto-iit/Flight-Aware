CREATE DATABASE  IF NOT EXISTS `flight_aware` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `flight_aware`;
-- MySQL dump 10.13  Distrib 8.0.38, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: flight_aware
-- ------------------------------------------------------
-- Server version	8.0.39

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
-- Table structure for table `flight`
--

DROP TABLE IF EXISTS `flight`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `flight` (
  `FlightID` int NOT NULL AUTO_INCREMENT,
  `AirlineID` int DEFAULT NULL,
  `FlightNum` varchar(10) DEFAULT NULL,
  `PlaneID` varchar(10) DEFAULT NULL,
  `DepartingAirportCode` char(5) DEFAULT NULL,
  `ArrivingAirportCode` char(5) DEFAULT NULL,
  `Date` date DEFAULT NULL,
  `Status` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`FlightID`),
  KEY `idx_airline_id` (`AirlineID`),
  KEY `idx_plane_id` (`PlaneID`),
  KEY `idx_flight_route_date` (`DepartingAirportCode`,`ArrivingAirportCode`,`Date`),
  CONSTRAINT `flight_ibfk_1` FOREIGN KEY (`PlaneID`) REFERENCES `plane` (`PlaneID`),
  CONSTRAINT `flight_ibfk_2` FOREIGN KEY (`AirlineID`) REFERENCES `airline` (`AirlineID`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `flight`
--

LOCK TABLES `flight` WRITE;
/*!40000 ALTER TABLE `flight` DISABLE KEYS */;
INSERT INTO `flight` VALUES (1,1,'AA101','N301FR','ATL','LAX','2024-10-01','On Time'),(2,2,'DL202','N302UA','ORD','DFW','2024-10-02','Delayed'),(3,3,'UA303','N303AA','DFW','DEN','2024-10-03','On Time'),(4,4,'WN404','N304SW','DEN','JFK','2024-10-04','Cancelled'),(5,5,'AS505','N305FR','JFK','SFO','2024-10-05','On Time'),(6,6,'B606','N306UA','SFO','SEA','2024-10-06','On Time'),(7,7,'NK707','N307AA','SEA','LAS','2024-10-07','Delayed'),(8,8,'F808','N308SW','LAS','MCO','2024-10-08','On Time'),(9,9,'HA909','N309FR','MCO','MIA','2024-10-09','On Time'),(10,10,'G410','N310UA','MIA','PHX','2024-10-10','Cancelled'),(11,11,'SY111','N311AA','PHX','IAH','2024-10-11','On Time'),(12,12,'3M112','N312SW','IAH','CLT','2024-10-12','Delayed'),(13,13,'MQ113','N313FR','CLT','EWR','2024-10-13','On Time'),(14,14,'OO114','N314UA','EWR','ATL','2024-10-14','On Time'),(15,15,'YX115','N315AA','ATL','LAX','2024-10-15','On Time'),(18,2,'FL1234','N12345','ORD','LAX','2024-10-01','Cancelled');
/*!40000 ALTER TABLE `flight` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-10-24 14:24:24
