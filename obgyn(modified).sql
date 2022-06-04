-- phpMyAdmin SQL Dump
-- version 5.1.2
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Jun 04, 2022 at 07:42 PM
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
-- Database: `obgyn`
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
(1, 'gufranmohammed@gmail.com', 'password', 'Gufran Mohammed', 'Mount Hospital', '115, Last Lane, NYC', '741287410');

-- --------------------------------------------------------

--
-- Table structure for table `available_appointment`
--

CREATE TABLE `available_appointment` (
  `available_appointment_id` int(11) NOT NULL,
  `doctor_id` int(11) DEFAULT NULL,
  `available_appointment_date` date DEFAULT NULL,
  `available_appointment_day` enum('Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday') DEFAULT NULL,
  `available_appointment_time` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `available_appointment`
--

INSERT INTO `available_appointment` (`available_appointment_id`, `doctor_id`, `available_appointment_date`, `available_appointment_day`, `available_appointment_time`) VALUES
(2, 1, '2021-02-19', 'Friday', '09:00-10:00AM'),
(3, 2, '2021-02-19', 'Friday', '09:00-10:00AM'),
(4, 5, '2021-02-19', 'Friday', '10:00-11:00AM'),
(5, 3, '2021-02-19', 'Friday', '13:00-14:00PM'),
(6, 4, '2021-02-19', 'Friday', '15:00-16:00PM'),
(7, 5, '2021-02-22', 'Monday', '12:00-13:00PM'),
(8, 2, '2021-02-24', 'Wednesday', '10:00-11:00AM'),
(9, 5, '2021-02-24', 'Wednesday', '11:00AM-12:00PM'),
(10, 1, '2021-02-24', 'Wednesday', '12:00-13:00PM'),
(11, 3, '2021-02-24', 'Wednesday', '14:00-15:00PM'),
(12, 4, '2021-02-24', 'Wednesday', '13:00-14:00PM'),
(13, 6, '2021-02-24', 'Wednesday', '10:00-11:00AM'),
(14, 6, '2021-02-25', 'Thursday', '9:00-10:00AM');

-- --------------------------------------------------------

--
-- Table structure for table `booked_appointment`
--

CREATE TABLE `booked_appointment` (
  `booked_appointment_id` int(11) NOT NULL,
  `doctor_id` int(11) DEFAULT NULL,
  `patient_id` int(11) DEFAULT NULL,
  `booked_appointment_time` varchar(20) DEFAULT NULL,
  `doctor_comment` varchar(1000) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

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
(1, 'peterparker@gmail.com', 'password', 'Dr. Peter Parker', '7539518520', '102, Sky View NYC', '1985-10-29', 'MBBS MS', 'Active'),
(2, 'adambrodly@gmail.com', 'password', 'Dr. Adam Broudly', '753852963', '105, Fort, NYC', '1982-08-10', 'MBBS MD(Cardiac)', 'Active'),
(3, 'sophia.parker@gmail.com', 'password', 'Dr. Sophia Parker', '7417417410', '50, Best street CA', '1989-04-03', 'MBBS', 'Active'),
(4, 'williampeterson@gmail.com', 'password', 'Dr. William Peterson', '8523698520', '32, Green City, NYC', '1984-06-11', 'MBBS MD', 'Active'),
(5, 'emmalarsdattor@gmail.com', 'password', 'Dr. Emma Larsdattor', '9635852025', '25, Silver Arch', '1988-03-03', 'MBBS MD', 'Active'),
(6, 'manuel.armstrong@gmail.com', 'password', 'Dr. Manuel Armstrong', '8523697410', '2378 Fire Access Road Asheboro, NC 27203', '1989-03-01', 'MBBS MD (Medicine)', 'Active');

-- --------------------------------------------------------

--
-- Table structure for table `inventory`
--

CREATE TABLE `inventory` (
  `device_id` int(11) NOT NULL,
  `device_name` varchar(100) DEFAULT NULL,
  `doctor_id` int(11) DEFAULT NULL,
  `device_count` int(11) DEFAULT NULL,
  `device_status` enum('available','not available') DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `inventory`
--

INSERT INTO `inventory` (`device_id`, `device_name`, `doctor_id`, `device_count`, `device_status`) VALUES
(1, 'colposcopes', 1, 5, 'available'),
(2, 'ultrasound system', 2, 2, 'not available'),
(3, 'Liquid Based Cytology set', 3, 4, 'available');

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
  `patient_date_of_birth` date DEFAULT NULL,
  `patient_address` varchar(200) DEFAULT NULL,
  `patient_phone_no` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `patient`
--

INSERT INTO `patient` (`patient_id`, `patient_email_address`, `patient_password`, `patient_first_name`, `patient_last_name`, `patient_date_of_birth`, `patient_address`, `patient_phone_no`) VALUES
(3, 'jacobmartin@gmail.com', 'password', 'Jacob', 'Martin', '2021-02-26', 'Green view, 1025,    NYC', '85745635210'),
(4, 'oliviabaker@gmail.com', 'password', 'Olivia', 'Baker', '2001-04-05', 'Diamond street, 115, NYC', '7539518520'),
(5, 'amberanderson@gmail.com', 'password', 'Amber', 'Anderson', '1995-07-25', '2083 Cameron Road Buffalo, NY 14202', '75394511442');

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
  ADD PRIMARY KEY (`available_appointment_id`);

--
-- Indexes for table `booked_appointment`
--
ALTER TABLE `booked_appointment`
  ADD PRIMARY KEY (`booked_appointment_id`);

--
-- Indexes for table `doctor`
--
ALTER TABLE `doctor`
  ADD PRIMARY KEY (`doctor_id`);

--
-- Indexes for table `inventory`
--
ALTER TABLE `inventory`
  ADD PRIMARY KEY (`device_id`);

--
-- Indexes for table `patient`
--
ALTER TABLE `patient`
  ADD PRIMARY KEY (`patient_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `admin_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `doctor`
--
ALTER TABLE `doctor`
  MODIFY `doctor_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `inventory`
--
ALTER TABLE `inventory`
  MODIFY `device_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `patient`
--
ALTER TABLE `patient`
  MODIFY `patient_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
