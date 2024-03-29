"use client";

import { motion } from "framer-motion";
import React from "react";
import { AuroraBackground } from "../ui/aurora-background";
import { NavbarDemo } from "../Navbar/Navbar";

export function AuroraBackgroundDemo() {
  return (
    
    <AuroraBackground>
          <NavbarDemo />

      <motion.div
        initial={{ opacity: 0.0, y: 40 }}
        whileInView={{ opacity: 1, y: 0 }}
        transition={{
          delay: 0.3,
          duration: 0.8,
          ease: "easeInOut",
        }}
        className="relative flex flex-col gap-4 items-center justify-center px-4"
      >
        <div className="font-extralight text-base md:text-4xl dark:text-neutral-200 py-4">
          Welcome to IdeateX
        </div>
        <div className="text-3xl md:text-7xl font-bold dark:text-white text-center">
          We help you in a way, other AI platforms dont
        </div>
        <div className="flex gap-4 sm:pt-5">
        <button className="  bg-[radial-gradient(ellipse_at_center,_var(--tw-gradient-stops))] from-gray-700 via-gray-900 to-black dark:bg-white rounded-full w-fit text-white dark:text-black px-4 py-2">
          Get Started
        </button>
                <button className="bg-[radial-gradient(ellipse_at_center,_var(--tw-gradient-stops))] from-gray-700 via-gray-900 to-black dark:bg-white rounded-full w-fit text-white dark:text-black px-4 py-2">
          Get Started
        </button>
        </div>

      </motion.div>
    </AuroraBackground>
  );
}
