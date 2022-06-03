-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 03, 2022 at 03:08 AM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `obgyn`
--

-- --------------------------------------------------------

--
-- Table structure for table `appointment`
--

CREATE TABLE `appointment` (
  `appointment_id` int(11) NOT NULL,
  `SRFid` int(20) NOT NULL,
  `patient_name` varchar(50) NOT NULL,
  `patient_phone` varchar(20) NOT NULL,
  `Did` int(11) NOT NULL,
  `schedule_id` int(11) NOT NULL,
  `appointment_time` time NOT NULL,
  `appointment_number` int(11) NOT NULL,
  `appointment_status` varchar(30) NOT NULL,
  `doctor_comment` mediumtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `appointment`
--

INSERT INTO `appointment` (`appointment_id`, `SRFid`, `patient_name`, `patient_phone`, `Did`, `schedule_id`, `appointment_time`, `appointment_number`, `appointment_status`, `doctor_comment`) VALUES
(3, 3, 'mohamed ahmed', '011223344', 1, 2, '09:00:00', 1000, 'booked', ''),
(4, 2, 'osama', '01212121', 1, 6, '02:26:26', 1001, 'completed', 'everything is good');

-- --------------------------------------------------------

--
-- Table structure for table `doctor`
--

CREATE TABLE `doctor` (
  `Did` int(11) NOT NULL,
  `Dname` varchar(100) NOT NULL,
  `Demail` varchar(100) NOT NULL,
  `Daddress` varchar(100) NOT NULL,
  `Dphone` varchar(30) NOT NULL,
  `Ddatebirth` date NOT NULL,
  `Ddegree` varchar(200) NOT NULL,
  `Dstatus` enum('Active','Inactive') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `doctor`
--

INSERT INTO `doctor` (`Did`, `Dname`, `Demail`, `Daddress`, `Dphone`, `Ddatebirth`, `Ddegree`, `Dstatus`) VALUES
(1, 'Dr. Peter Parker', 'peterparker@gmail.com', '102, Sky View, NYC', '7539518520', '1985-10-29', 'MBBS MS', 'Active'),
(2, 'Dr. Adam Broudly', 'adambrodly@gmail.com', '105, Fort, NYC', '753852963', '1988-07-04', 'MBBS MD', 'Inactive');

-- --------------------------------------------------------

--
-- Table structure for table `doctor_schedule`
--

CREATE TABLE `doctor_schedule` (
  `schedule_id` int(11) NOT NULL,
  `Did` int(11) NOT NULL,
  `schedule_date` date NOT NULL,
  `schedule_day` enum('Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday') NOT NULL,
  `start-time` varchar(20) NOT NULL,
  `end-time` varchar(20) NOT NULL,
  `schedule_status` enum('availabe','not availabe') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `doctor_schedule`
--

INSERT INTO `doctor_schedule` (`schedule_id`, `Did`, `schedule_date`, `schedule_day`, `start-time`, `end-time`, `schedule_status`) VALUES
(2, 1, '2022-06-19', 'Sunday', '09:00', '14:00', 'availabe'),
(3, 2, '2022-06-22', 'Wednesday', '09:00', '14:00', 'not availabe');

-- --------------------------------------------------------

--
-- Table structure for table `inventory`
--

CREATE TABLE `inventory` (
  `device_id` int(11) NOT NULL,
  `device_name` varchar(50) NOT NULL,
  `Did` int(11) NOT NULL,
  `device_count` int(11) NOT NULL,
  `device_status` enum('available','not available') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `inventory`
--

INSERT INTO `inventory` (`device_id`, `device_name`, `Did`, `device_count`, `device_status`) VALUES
(1, 'colposcopes', 1, 5, 'available'),
(2, 'ultrasound system', 2, 2, 'not available');

-- --------------------------------------------------------

--
-- Table structure for table `stafflogin`
--

CREATE TABLE `stafflogin` (
  `staffID` int(11) NOT NULL,
  `Did` varchar(20) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(1000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `stafflogin`
--

INSERT INTO `stafflogin` (`staffID`, `Did`, `email`, `password`) VALUES
(9, '1', 'me@gmail.com', '123me'),
(10, '2', 'me12@gmail.com', 'me123');

-- --------------------------------------------------------

--
-- Table structure for table `test`
--

CREATE TABLE `test` (
  `id` int(11) NOT NULL,
  `name` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `test`
--

INSERT INTO `test` (`id`, `name`) VALUES
(1, 'gufran'),
(2, 'mohammed');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `Uid` int(11) NOT NULL,
  `SRFid` varchar(20) NOT NULL,
  `email` varchar(20) NOT NULL,
  `birthdate` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`Uid`, `SRFid`, `email`, `birthdate`) VALUES
(8, 'abc12', 'abc@gmail.com', '2001-10-10'),
(9, 'def123', 'def@gmail.com', '2002-5-6');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `appointment`
--
ALTER TABLE `appointment`
  ADD PRIMARY KEY (`appointment_id`),
  ADD UNIQUE KEY `SRFid` (`SRFid`);

--
-- Indexes for table `doctor`
--
ALTER TABLE `doctor`
  ADD PRIMARY KEY (`Did`);

--
-- Indexes for table `doctor_schedule`
--
ALTER TABLE `doctor_schedule`
  ADD PRIMARY KEY (`schedule_id`);

--
-- Indexes for table `inventory`
--
ALTER TABLE `inventory`
  ADD PRIMARY KEY (`device_id`);

--
-- Indexes for table `stafflogin`
--
ALTER TABLE `stafflogin`
  ADD PRIMARY KEY (`staffID`);

--
-- Indexes for table `test`
--
ALTER TABLE `test`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`Uid`),
  ADD UNIQUE KEY `SRFid` (`SRFid`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `appointment`
--
ALTER TABLE `appointment`
  MODIFY `appointment_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `doctor`
--
ALTER TABLE `doctor`
  MODIFY `Did` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `doctor_schedule`
--
ALTER TABLE `doctor_schedule`
  MODIFY `schedule_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `inventory`
--
ALTER TABLE `inventory`
  MODIFY `device_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `stafflogin`
--
ALTER TABLE `stafflogin`
  MODIFY `staffID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `test`
--
ALTER TABLE `test`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `Uid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
