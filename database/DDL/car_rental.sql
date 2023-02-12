--
-- Database: `car_rental`
--

-- --------------------------------------------------------

--
-- Table structure for table `booking`
--

CREATE TABLE `booking` (
  `id` int(11) NOT NULL,
  `customer_id` int(11) NOT NULL,
  `vehicle_id` int(11) NOT NULL,
  `hire_date` datetime NOT NULL,
  `return_date` datetime NOT NULL,
  `is_paid` tinyint(4) NOT NULL DEFAULT '0',
  `is_confirmed` tinyint(4) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `customer`
--

CREATE TABLE `customer` (
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `national_id` varchar(20) NOT NULL,
  `address` varchar(70) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `vehicle`
--

CREATE TABLE `vehicle` (
  `id` int(11) NOT NULL,
  `vehicle_type` varchar(10) NOT NULL,
  `vehicle_plate` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
--
-- Indexes for table `booking`
--
ALTER TABLE `booking`
  ADD PRIMARY KEY (`id`),
  ADD KEY `FK_vehicle_id` (`vehicle_id`),
  ADD KEY `customer_vehicles` (`customer_id`,`vehicle_id`);

--
-- Indexes for table `customer`
--
ALTER TABLE `customer`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `vehicle`
--
ALTER TABLE `vehicle`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for table `booking`
--
ALTER TABLE `booking`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `customer`
--
ALTER TABLE `customer`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `vehicle`
--
ALTER TABLE `vehicle`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Constraints for table `booking`
--
ALTER TABLE `booking`
  ADD CONSTRAINT `FK_customer_id` FOREIGN KEY (`customer_id`) REFERENCES `customer` (`id`),
  ADD CONSTRAINT `FK_vehicle_id` FOREIGN KEY (`vehicle_id`) REFERENCES `vehicle` (`id`);
COMMIT;
