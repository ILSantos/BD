-- MySQL dump 10.13  Distrib 5.6.19, for osx10.7 (i386)
--
-- Host: localhost    Database: mas
-- ------------------------------------------------------
-- Server version	5.6.23

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `organization`
--

DROP TABLE IF EXISTS `organization`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `organization` (
  `oid` int(11) NOT NULL,
  `name` varchar(150) DEFAULT NULL,
  `continent` varchar(45) DEFAULT NULL,
  `homepage` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`oid`),
  FULLTEXT KEY `organization_id` (`name`),
  FULLTEXT KEY `homepage` (`homepage`),
  FULLTEXT KEY `continent` (`continent`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `domain`
--

DROP TABLE IF EXISTS `domain`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `domain` (
  `did` int(11) NOT NULL,
  `name` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`did`),
  FULLTEXT KEY `domain_name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `publication`
--

DROP TABLE IF EXISTS `publication`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `publication` (
  `pid` int(11) NOT NULL,
  `title` varchar(200) DEFAULT NULL,
  `abstract` varchar(2000) DEFAULT NULL,
  `year` int(11) DEFAULT NULL,
  `cid` int(11) DEFAULT NULL,
  `jid` int(11) DEFAULT NULL,
  `reference_num` int(11) DEFAULT NULL,
  `citation_num` int(11) DEFAULT NULL,
  `doi` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`pid`),
  KEY `cid` (`cid`),
  KEY `jid` (`jid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `journal`
--

DROP TABLE IF EXISTS `journal`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `journal` (
  `jid` int(11) NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `full_name` varchar(200) DEFAULT NULL,
  `homepage` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`jid`),
  FULLTEXT KEY `name` (`name`),
  FULLTEXT KEY `homepage` (`homepage`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `keyword_variations`
--

DROP TABLE IF EXISTS `keyword_variations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `keyword_variations` (
  `kid` int(11) NOT NULL,
  `variation` varchar(100) NOT NULL,
  PRIMARY KEY (`kid`,`variation`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `keyword`
--

DROP TABLE IF EXISTS `keyword`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `keyword` (
  `kid` int(11) NOT NULL,
  `keyword` varchar(100) DEFAULT NULL,
  `keyword_short` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`kid`),
  FULLTEXT KEY `journal_name` (`keyword`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;


--
-- Table structure for table `conference`
--

DROP TABLE IF EXISTS `conference`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `conference` (
  `cid` int(11) NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `full_name` varchar(200) DEFAULT NULL,
  `homepage` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`cid`),
  FULLTEXT KEY `name` (`name`),
  FULLTEXT KEY `homepage` (`homepage`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `author`
--

DROP TABLE IF EXISTS `author`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `author` (
  `aid` int(11) NOT NULL,
  `name` varchar(150) DEFAULT NULL,
  `oid` int(11) DEFAULT NULL,
  `homepage` varchar(200) DEFAULT NULL,
  `photo` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`aid`),
  FOREIGN KEY (`oid`) REFERENCES organization(`oid`),
  FULLTEXT KEY `author_name` (`name`),
  FULLTEXT KEY `homepage` (`homepage`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `cite`
--

DROP TABLE IF EXISTS `cite`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cite` (
  `citing` int(11) NOT NULL,
  `cited` int(11) NOT NULL,
  PRIMARY KEY (`citing`,`cited`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;



--
-- Table structure for table `domain_author`
--

DROP TABLE IF EXISTS `domain_author`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `domain_author` (
  `aid` int(11) NOT NULL,
  `did` int(11) NOT NULL,
  PRIMARY KEY (`aid`,`did`),
  KEY `aid` (`aid`),
  KEY `did` (`did`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;


--
-- Table structure for table `domain_conference`
--

DROP TABLE IF EXISTS `domain_conference`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `domain_conference` (
  `cid` int(11) NOT NULL,
  `did` int(11) NOT NULL,
  PRIMARY KEY (`cid`,`did`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;


--
-- Table structure for table `domain_journal`
--

DROP TABLE IF EXISTS `domain_journal`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `domain_journal` (
  `jid` int(11) NOT NULL,
  `did` int(11) NOT NULL,
  PRIMARY KEY (`jid`,`did`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;



--
-- Table structure for table `domain_keyword`
--

DROP TABLE IF EXISTS `domain_keyword`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `domain_keyword` (
  `kid` int(11) NOT NULL,
  `did` int(11) NOT NULL,
  `rank` int(11) NOT NULL,
  PRIMARY KEY (`kid`,`did`,`rank`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `domain_publication`
--

DROP TABLE IF EXISTS `domain_publication`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `domain_publication` (
  `pid` int(11) NOT NULL,
  `did` int(11) NOT NULL,
  PRIMARY KEY (`pid`,`did`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;



--
-- Table structure for table `ids`
--

DROP TABLE IF EXISTS `ids`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ids` (
  `relation` varchar(10) NOT NULL,
  `id` int(11) NOT NULL,
  `exist` int(11) DEFAULT '0',
  PRIMARY KEY (`relation`,`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;








--
-- Table structure for table `publication_keyword`
--

DROP TABLE IF EXISTS `publication_keyword`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `publication_keyword` (
  `pid` int(11) NOT NULL,
  `kid` int(11) NOT NULL,
  PRIMARY KEY (`pid`,`kid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `writes`
--

DROP TABLE IF EXISTS `writes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `writes` (
  `aid` int(11) NOT NULL,
  `pid` int(11) NOT NULL,
  PRIMARY KEY (`aid`,`pid`),
  KEY `aid` (`aid`),
  KEY `pid` (`pid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;


--
-- Dumping data for table `author`
--
LOCK TABLES `author` WRITE;
/*!40000 ALTER TABLE `author` DISABLE KEYS */;
