-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 14, 2023 at 03:37 AM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `bank_ini`
--

-- --------------------------------------------------------

--
-- Table structure for table `list_registrasi`
--

CREATE TABLE `list_registrasi` (
  `id` int(11) NOT NULL,
  `nama` varchar(255) NOT NULL,
  `pin` int(11) NOT NULL,
  `password` varchar(255) NOT NULL,
  `status` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `list_withdraw`
--

CREATE TABLE `list_withdraw` (
  `id` int(11) NOT NULL,
  `saldo` int(11) NOT NULL,
  `amount` int(11) NOT NULL,
  `status` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `list_withdraw`
--

INSERT INTO `list_withdraw` (`id`, `saldo`, `amount`, `status`) VALUES
(14621, 290000, 50000, 0);

-- --------------------------------------------------------

--
-- Table structure for table `tipe_user`
--

CREATE TABLE `tipe_user` (
  `id` int(11) NOT NULL,
  `tipe_user` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tipe_user`
--

INSERT INTO `tipe_user` (`id`, `tipe_user`) VALUES
(11150, 'admin'),
(34521, 'customer'),
(98710, 'teller');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `nama` varchar(255) NOT NULL,
  `pin` int(11) NOT NULL,
  `password` varchar(255) NOT NULL,
  `saldo` int(11) NOT NULL,
  `saving` int(11) NOT NULL,
  `id_tipe` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `nama`, `pin`, `password`, `saldo`, `saving`, `id_tipe`) VALUES
(14621, 'Suliah', 252312, 'Widan anjing', 290000, 0, 34521),
(21126, 'vincent', 918221, 'hallo', 40000, 0, 34521),
(46387, 'Diki', 19284, 'cuk', 0, 0, 98710),
(47883, 'diki', 129083, 'wow', 0, 0, 11150),
(84995, 'widan', 198431, 'asu', 0, 0, 34521),
(98232, 'Jati', 983212, 'hmm', 0, 0, 11150);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `list_registrasi`
--
ALTER TABLE `list_registrasi`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `list_withdraw`
--
ALTER TABLE `list_withdraw`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `tipe_user`
--
ALTER TABLE `tipe_user`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
