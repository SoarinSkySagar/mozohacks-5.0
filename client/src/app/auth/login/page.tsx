"use client"
import React from 'react';
import { motion } from 'framer-motion';
import Link from 'next/link';
import { NavbarDemo } from "../../components/Navbar/Navbar";
const Login = ({ onSignupClick }: { onSignupClick: () => void }) => {

  return (
    
    <motion.div
      initial={{ opacity: 0, x: -50 }}
      animate={{ opacity: 1, x: 0 }}
      exit={{ opacity: 0, x: -50 }}
      transition={{ duration: 0.5 }}
      className="bg-gray-900 min-h-screen flex justify-center items-center"
    >
      <div className="bg-gray-800 p-8 rounded-md shadow-lg text-white w-80">
      <NavbarDemo/>

        <h1 className="text-3xl font-bold mb-4">Login</h1>
        <form>
          <div className="mb-4">
            <label htmlFor="email" className="block text-sm font-semibold mb-1">Email</label>
            <input type="email" id="email" name="email" className="w-full px-3 py-2 border rounded-md bg-gray-700 text-white" />
          </div>
          <div className="mb-4">
            <label htmlFor="password" className="block text-sm font-semibold mb-1">Password</label>
            <input type="password" id="password" name="password" className="w-full px-3 py-2 border rounded-md bg-gray-700 text-white" />
          </div>
          <button type="submit" className="w-full py-2 px-4 bg-blue-500 text-white rounded-md hover:bg-blue-600">Login</button>
        </form>
        <p className="text-sm mt-4">Dont have an account? <Link href="/auth/signup"className="text-blue-400 cursor-pointer" onClick={onSignupClick}>Sign up</Link></p>
      </div>
    </motion.div>
  );
};

export default Login;
