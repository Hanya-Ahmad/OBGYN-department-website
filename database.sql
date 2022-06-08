-- phpMyAdmin SQL Dump
-- version 5.1.2
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Jun 08, 2022 at 10:47 PM
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
-- Database: `database_project`
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
(2, '2022-09-21', '11:00-12:00 AM', 6),
(3, '2022-06-21', '1:00-2:00PM', 2),
(4, '2022-06-19', '10:00-11:00 AM', 6),
(6, '2022-07-01', '15:00-16:00 PM', 17),
(8, '2022-06-24', '09:30-10:30 AM', 18),
(9, '2022-06-12', '11:00-12:00 AM', 19),
(11, '2022-07-20', '14:00-15:00 PM', 20),
(12, '2022-06-22', '16:00-17:00 PM', 21),
(13, '2022-07-24', '15:30-16:30 PM', 22);

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
(6, 24, 13, '2022-03-25', '10:00-11:00 AM', NULL, '500mg of Amoxicillin twice per day for 5 days to treat UTI'),
(7, 18, 19, '2022-02-22', '18:00-19:00 PM', NULL, '200mg of Diphenhydramine for one week'),
(8, 17, 15, '2022-04-19', '13:00-14:00 PM', NULL, '25mg of Ciprofloxacin for two weeks'),
(9, 2, 11, '2022-10-13', '09:00-10:00 AM', 'upcoming', NULL),
(10, 21, 1, '2022-06-23', '9:00-10:00AM', 'upcoming', '50 mg of Clobex for 3 days'),
(11, 2, 21, '2022-04-22', '9:00-10:00AM', NULL, 'History of Ovarian Cancer'),
(12, 17, 11, '2022-07-01', '16:00-17:00 PM', 'upcoming', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `contact`
--

CREATE TABLE `contact` (
  `contact_name` varchar(20) NOT NULL,
  `contact_email` varchar(20) NOT NULL,
  `contact_comment` int(255) NOT NULL,
  `patient_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

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
(6, 'ahmed@gmail.com', 'ahmedahmed', 'ahmed', '12345678910', '16 st', '1995-08-25', 'MBBCh', 'Active'),
(17, 'peterparker@gmail.com', '1234', 'Dr. Peter Parker', '7539518520', '102, Sky View NYC', '1985-10-29', 'MBBS MS', 'Active'),
(18, 'adambrodly@gmail.com', '2345', 'Dr. Adam Broudly', '753852963', '105, Fort, NYC', '1982-08-10', 'MBBS MD', 'Active'),
(19, 'sophia.parker@gmail.com', '3456', 'Dr. Sophia Parker', '7417417410', '50, Best street CA', '1989-04-03', 'MBBS', 'Active'),
(20, 'williampeterson@gmail.com', '4567', 'Dr. William Peterson', '8523698520', '32, Green City, NYC', '1984-06-11', 'MBBS MD', 'Active'),
(21, 'emmalarsdattor@gmail.com', '5678', 'Dr. Emma Larsdattor', '9635852025', '25, Silver Arch', '1988-03-03', 'MBBS MD', 'Active'),
(22, 'manuel.armstrong@gmail.com', '6789', 'Dr. Manuel Armstrong', '8523697410', '2378 Fire Access Road Asheboro, NC 27203', '1989-03-01', 'MBBS MD (Medicine)', 'Active'),
(23, 'osama.ahmed@gmail.com', '7890', 'Dr. Osama Ahmed', '85745635210', 'Green view, 1025,  NYC', '2021-02-26', 'MBBS DO', 'Inactive'),
(24, 'oliviabaker@gmail.com', '8901', 'Dr. Olivia Baker', '7539518520', 'Diamond street, 115, NYC', '2001-04-05', 'MBBS MD', 'Inactive'),
(25, 'amberanderson@gmail.com', '9012', 'Dr. Amber Anderson', '75394511442', '2083 Cameron Road Buffalo, NY 14202', '1995-07-25', 'MBBS DO', 'Active');

-- --------------------------------------------------------

--
-- Table structure for table `inventory`
--

CREATE TABLE `inventory` (
  `device_booking_id` int(11) NOT NULL,
  `device_sn` int(11) NOT NULL,
  `device_name` varchar(100) DEFAULT NULL,
  `date_imported` date DEFAULT NULL,
  `expiry_date` date NOT NULL,
  `booking_date` date DEFAULT NULL,
  `booking_hour` varchar(20) DEFAULT NULL,
  `device_state` enum('available','not available') DEFAULT NULL,
  `doctor_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `inventory`
--

INSERT INTO `inventory` (`device_booking_id`, `device_sn`, `device_name`, `date_imported`, `expiry_date`, `booking_date`, `booking_hour`, `device_state`, `doctor_id`) VALUES
(1, 1234, 'colposcopes', '2020-09-08', '2030-04-07', '2022-06-01', '07:00-08:00AM', 'not available', 2),
(2, 2345, 'Cervical cytology brush', '2019-03-04', '2029-06-05', '2032-06-09', '04:00-05:00AM', 'not available', 2),
(3, 3456, 'Liquid Based Cytology set', '2021-05-08', '2031-02-08', '2031-12-17', '01:30-02:30PM', 'available', 2),
(4, 4567, 'Hysteroscopes', '2015-05-09', '2025-03-02', '2016-06-14', '07:00-08:00PM', 'available', 2),
(5, 5678, 'Uterine manipulator', '2022-06-05', '2039-02-03', '2031-01-23', '12:00-01:00PM', 'available', 2),
(6, 6789, 'Hysterometer', '2021-09-08', '2031-04-07', '2031-06-05', '05:00-06:00AM', 'not available', 2),
(7, 7890, 'Obstetric suction cup', '2022-05-08', '2032-02-08', '2028-11-10', '03:00-04:00AM', 'available', 17),
(8, 8901, 'Fertility monitor', '2016-05-09', '2026-03-02', '2026-06-03', '08:00-09:00PM', 'available', 2),
(9, 9012, 'Rapid pregnancy test', '2020-06-05', '2040-02-03', '2028-11-15', '12:00-01:50AM', 'not available', 18),
(10, 9532, 'ultrasound', '2017-04-25', '2022-06-23', '2031-06-06', '07:00-09:00PM', 'not available', 2);

-- --------------------------------------------------------

--
-- Table structure for table `patient`
--

CREATE TABLE `patient` (
  `patient_id` int(11) NOT NULL,
  `patient_email_address` varchar(200) DEFAULT NULL,
  `patient_first_name` varchar(100) DEFAULT NULL,
  `patient_last_name` varchar(100) DEFAULT NULL,
  `patient_age` int(11) UNSIGNED NOT NULL,
  `patient_phone_no` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `patient`
--

INSERT INTO `patient` (`patient_id`, `patient_email_address`, `patient_first_name`, `patient_last_name`, `patient_age`, `patient_phone_no`) VALUES
(1, 'mahmoud@gmail.com', 'Mahmoud', 'Mohammed', 20, '01045635210'),
(6, 'hanyaahmad13@gmail.com', 'Hanya', 'Ahmad', 21, '01094536271'),
(7, 'emily@mail.com', 'Emily', 'Davidson', 19, '01245678901'),
(11, 'hanyaahmad13@gmail.com', 'Hanya', 'Ahmad', 21, '01258963217'),
(13, 'sarahandy@mail.com', 'Sarah', 'Andy', 27, '01036597846'),
(14, 'rexanne@mail.com', 'Rexanne', 'Danielson', 22, '01356987456'),
(15, 'summermitch@mail.com', 'Summer', 'Mitchell', 34, '01203698745'),
(16, 'angelawinston@mail.com', 'Angela', 'Winston', 40, '01136987456'),
(17, 'thecarlson@mail.com', 'Anne', 'Carlson', 17, '01136548961'),
(18, 'charlottewitherspoon@mail.com', 'Charlotte', 'Witherspoon', 60, '01236958478'),
(19, 'faiththornton@mail.com', 'Faith', 'Thornton', 39, '01203698745'),
(20, 'shirley12vin@mail.com', 'Sherley', 'Vincent', 31, '01036584971'),
(21, 'cassandra@mail.com', 'Cassandra', 'Harris', 44, '01136578920'),
(22, 'marshamat@mail.com', 'Marsha', 'Matthews', 30, '01256945231'),
(23, 'inezhath@mail.com', 'Inez', 'Hathway', 49, '01197538673'),
(24, 'monicarichardson@mail.com', 'Monica', 'Richardson', 50, '01178376492'),
(25, 'joandrareed@gmail.com', 'Joandra', 'Reed', 60, '01073593677'),
(26, 'cynthia12@mail.com', 'Cynthia', 'Hitchcock', 41, '01038764429'),
(27, 'jessicapink@mail.com', 'Jessica', 'Pink', 29, '01298743556'),
(28, 'khadeeja@mail.com', 'Khadeeja', 'Ahmed', 35, '01567954379');

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
(1, 'olivia', 'password', 'patient'),
(2, 'heidi', 'password', 'doctor'),
(3, 'gufran', 'password', 'admin'),
(6, 'ahmed', 'ahmedahmed', 'doctor'),
(7, 'emily', 'password', 'patient'),
(11, 'hanyaahmad', 'passforhanya', 'patient'),
(13, 'sarahandy', 'sarahandypass', 'patient'),
(14, 'rexannedan', 'rexforexanne', 'patient'),
(15, 'summermitch', 'summermitch', 'patient'),
(16, 'angelawinston', 'angelawinstonpass', 'patient'),
(17, 'annecarlson1', 'theannepass', 'patient'),
(18, 'charlottewitherspoon', 'passforcharlotte', 'patient'),
(19, 'faiththornton', 'faithpass123', 'patient'),
(20, 'shirleyvincent', 'pass123987', 'patient'),
(21, 'cassandraharris', 'cassandrapass', 'patient'),
(22, 'marshamat', 'marshathemat', 'patient'),
(23, 'inezhathway', 'passforinez', 'patient'),
(24, 'monicarichardson', 'monicarichardson', 'patient'),
(25, 'joandrareed', 'joandrareedpass', 'patient'),
(26, 'cynthia12', 'passforcynthia', 'patient'),
(27, 'jessicapink', 'jesspassjess', 'patient'),
(28, 'khadkhoda', 'hajdnflsjn', 'patient');

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
  ADD PRIMARY KEY (`device_booking_id`),
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
  MODIFY `available_appointment_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `booked_appointment`
--
ALTER TABLE `booked_appointment`
  MODIFY `booked_appointment_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `doctor`
--
ALTER TABLE `doctor`
  MODIFY `doctor_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- AUTO_INCREMENT for table `inventory`
--
ALTER TABLE `inventory`
  MODIFY `device_booking_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `patient`
--
ALTER TABLE `patient`
  MODIFY `patient_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `userid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;

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
