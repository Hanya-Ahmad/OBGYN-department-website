-- phpMyAdmin SQL Dump
-- version 5.1.2
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Jun 06, 2022 at 12:31 AM
-- Server version: 5.7.24
-- PHP Version: 8.0.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `obgyn2`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `admin_id` int(11) NOT NULL,
  `admin_email_address` varchar(200) DEFAULT NULL,
  `admin_password` varchar(100) DEFAULT NULL,
  `admin_name` varchar(200) DEFAULT NULL,
  `hospital_name` varchar(200) DEFAULT NULL,
  `hospital_address` varchar(200) DEFAULT NULL,
  `hospital_contact_no` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`admin_id`, `admin_email_address`, `admin_password`, `admin_name`, `hospital_name`, `hospital_address`, `hospital_contact_no`) VALUES
(3, 'gufranmohammed@gmail.com', 'password', 'Gufran Mohammed', 'Mount Hospital', '115, Last Lane, NYC', '741287410');

-- --------------------------------------------------------

--
-- Table structure for table `available_appointment`
--

CREATE TABLE `available_appointment` (
  `available_appointment_id` int(11) NOT NULL,
  `available_appointment_date` date DEFAULT NULL,
  `available_appointment_time` varchar(20) DEFAULT NULL,
  `doctor_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `available_appointment`
--

INSERT INTO `available_appointment` (`available_appointment_id`, `available_appointment_date`, `available_appointment_time`, `doctor_id`) VALUES
(1, '2021-02-19', '09:00', 2);

-- --------------------------------------------------------

--
-- Table structure for table `booked_appointment`
--

CREATE TABLE `booked_appointment` (
  `booked_appointment_id` int(11) NOT NULL,
  `doctor_id` int(11) DEFAULT NULL,
  `patient_id` int(11) DEFAULT NULL,
  `booked_appointment_date` date DEFAULT NULL,
  `booked_appointment_time` varchar(20) DEFAULT NULL,
  `past_or_upcoming` enum('past','upcoming') DEFAULT NULL,
  `doctor_comment` varchar(1000) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `booked_appointment`
--

INSERT INTO `booked_appointment` (`booked_appointment_id`, `doctor_id`, `patient_id`, `booked_appointment_date`, `booked_appointment_time`, `past_or_upcoming`, `doctor_comment`) VALUES
(1, 2, 6, '2022-06-13', '9:00-10:00AM', 'upcoming', 'comment1'),
(2, 6, 1, '2022-06-23', '10:00-11:00AM', 'upcoming', 'comment2'),
(3, 6, 1, '2022-06-08', '12:00-1:00PM', 'past', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `doctor`
--

CREATE TABLE `doctor` (
  `doctor_id` int(11) NOT NULL,
  `doctor_email_address` varchar(200) DEFAULT NULL,
  `doctor_password` varchar(100) DEFAULT NULL,
  `doctor_name` varchar(100) DEFAULT NULL,
  `doctor_phone_no` varchar(30) DEFAULT NULL,
  `doctor_address` varchar(500) DEFAULT NULL,
  `doctor_date_of_birth` date DEFAULT NULL,
  `doctor_degree` varchar(200) DEFAULT NULL,
  `doctor_status` enum('Active','Inactive') DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `doctor`
--

INSERT INTO `doctor` (`doctor_id`, `doctor_email_address`, `doctor_password`, `doctor_name`, `doctor_phone_no`, `doctor_address`, `doctor_date_of_birth`, `doctor_degree`, `doctor_status`) VALUES
(2, 'hideiparker@gmail.com', 'password', 'Dr. hidei Parker', '7539518520', '102, Sky View NYC', '2001-10-29', 'MBBS MS', 'Active'),
(6, 'ahmed@gmail.com', 'ahmedahmed', 'ahmed', '12345678910', '16 st', '1995-08-25', 'MBBCh', 'Active');

-- --------------------------------------------------------

--
-- Table structure for table `inventory`
--

CREATE TABLE `inventory` (
  `device_sn` int(11) NOT NULL,
  `device_name` varchar(100) DEFAULT NULL,
  `date_imported` date DEFAULT NULL,
  `booking_date` date DEFAULT NULL,
  `booking_hour` varchar(20) DEFAULT NULL,
  `device_state` enum('available','not available') DEFAULT NULL,
  `doctor_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `inventory`
--

INSERT INTO `inventory` (`device_sn`, `device_name`, `date_imported`, `booking_date`, `booking_hour`, `device_state`, `doctor_id`) VALUES
(1, 'colposcopes', NULL, NULL, NULL, 'available', 2);

-- --------------------------------------------------------

--
-- Table structure for table `patient`
--

CREATE TABLE `patient` (
  `patient_id` int(11) NOT NULL,
  `patient_email_address` varchar(200) DEFAULT NULL,
  `patient_password` varchar(100) DEFAULT NULL,
  `patient_first_name` varchar(100) DEFAULT NULL,
  `patient_last_name` varchar(100) DEFAULT NULL,
  `patient_age` int(11) UNSIGNED NOT NULL,
  `patient_address` varchar(200) DEFAULT NULL,
  `patient_phone_no` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `patient`
--

INSERT INTO `patient` (`patient_id`, `patient_email_address`, `patient_password`, `patient_first_name`, `patient_last_name`, `patient_age`, `patient_address`, `patient_phone_no`) VALUES
(1, 'mahmoud@gmail.com', 'password', 'mahmoud', 'Mohammed', 20, 'Green view, 1025,    NYC', '85745635210'),
(6, 'hanyaahmad13@gmail.com', NULL, 'Hanya', 'Ahmad', 21, NULL, '01111940445'),
(7, NULL, 'password', NULL, NULL, 19, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `userid` int(11) NOT NULL,
  `username` varchar(255) DEFAULT NULL,
  `pass` varchar(255) DEFAULT NULL,
  `access` enum('admin','patient','doctor') DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`userid`, `username`, `pass`, `access`) VALUES
(1, 'mahmoud', 'password', 'patient'),
(2, 'hiedi', 'password', 'doctor'),
(3, 'gufran', 'password', 'admin'),
(6, 'ahmed', 'ahmedahmed', 'doctor'),
(7, 'emily', 'password', 'patient');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`admin_id`);

--
-- Indexes for table `available_appointment`
--
ALTER TABLE `available_appointment`
  ADD PRIMARY KEY (`available_appointment_id`),
  ADD KEY `doctor_id` (`doctor_id`);

--
-- Indexes for table `booked_appointment`
--
ALTER TABLE `booked_appointment`
  ADD PRIMARY KEY (`booked_appointment_id`),
  ADD KEY `doctor_id` (`doctor_id`),
  ADD KEY `patient_id` (`patient_id`);

--
-- Indexes for table `doctor`
--
ALTER TABLE `doctor`
  ADD PRIMARY KEY (`doctor_id`);

--
-- Indexes for table `inventory`
--
ALTER TABLE `inventory`
  ADD PRIMARY KEY (`device_sn`),
  ADD KEY `doctor_id` (`doctor_id`);

--
-- Indexes for table `patient`
--
ALTER TABLE `patient`
  ADD PRIMARY KEY (`patient_id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`userid`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `admin_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `available_appointment`
--
ALTER TABLE `available_appointment`
  MODIFY `available_appointment_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `doctor`
--
ALTER TABLE `doctor`
  MODIFY `doctor_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `inventory`
--
ALTER TABLE `inventory`
  MODIFY `device_sn` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `patient`
--
ALTER TABLE `patient`
  MODIFY `patient_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `userid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `admin`
--
ALTER TABLE `admin`
  ADD CONSTRAINT `admin_ibfk_1` FOREIGN KEY (`admin_id`) REFERENCES `user` (`userid`);

--
-- Constraints for table `available_appointment`
--
ALTER TABLE `available_appointment`
  ADD CONSTRAINT `available_appointment_ibfk_1` FOREIGN KEY (`doctor_id`) REFERENCES `doctor` (`doctor_id`);

--
-- Constraints for table `booked_appointment`
--
ALTER TABLE `booked_appointment`
  ADD CONSTRAINT `booked_appointment_ibfk_4` FOREIGN KEY (`doctor_id`) REFERENCES `doctor` (`doctor_id`),
  ADD CONSTRAINT `booked_appointment_ibfk_5` FOREIGN KEY (`patient_id`) REFERENCES `patient` (`patient_id`);

--
-- Constraints for table `doctor`
--
ALTER TABLE `doctor`
  ADD CONSTRAINT `doctor_ibfk_1` FOREIGN KEY (`doctor_id`) REFERENCES `user` (`userid`);

--
-- Constraints for table `inventory`
--
ALTER TABLE `inventory`
  ADD CONSTRAINT `inventory_ibfk_1` FOREIGN KEY (`doctor_id`) REFERENCES `doctor` (`doctor_id`);

--
-- Constraints for table `patient`
--
ALTER TABLE `patient`
  ADD CONSTRAINT `patient_ibfk_1` FOREIGN KEY (`patient_id`) REFERENCES `user` (`userid`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
