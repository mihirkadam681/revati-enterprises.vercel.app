package com.housekeeping;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

/**
 * Main Spring Boot Application Entry Point
 * Commercial Housekeeping and Maintenance System
 * College: SHETH L.U.J. & SIR M.V. COLLEGE OF SCIENCE
 * Author: Mihir R. Kadam (T082)
 */
@SpringBootApplication
public class HousekeepingApplication {

    public static void main(String[] args) {
        SpringApplication.run(HousekeepingApplication.class, args);
        System.out.println("==========================================================");
        System.out.println("  Spring Boot Commercial Housekeeping Server Running!     ");
        System.out.println("==========================================================");
    }
}
