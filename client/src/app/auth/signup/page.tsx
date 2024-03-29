"use client"
import React from 'react';
import { motion } from 'framer-motion';
import Link from 'next/link';
import { useState } from 'react';
import { NavbarDemo } from "../../components/Navbar/Navbar";

const Signup = ({ onLoginClick }: { onLoginClick: any }) => {
    const[formData, setFormData] = useState({
        email: '',
        password: '',
        fullName: ''
      });
    
      const handleChange= (e: { target: { name: any; value: any; }; })=>{
        const{name, value} = e.target;
        setFormData({ ...formData, [name]: value });
      }
  return (
    <motion.div
      initial={{ opacity: 0, x: 50 }}
      animate={{ opacity: 1, x: 0 }}
      exit={{ opacity: 0, x: 50 }}
      transition={{ duration: 0.5 }}
      className="bg-gradient-to-bl from-gray-900 via-purple-900 to-violet-600 min-h-screen flex justify-center items-center"
    >
      <div className="bg-gray-800 p-8 rounded-md shadow-lg text-white w-80">
      <NavbarDemo/>

        <h1 className="text-3xl font-bold mb-4">Sign Up</h1>
        <form>
          <div className="mb-4">
            <label htmlFor="fullName" className="block text-sm font-semibold mb-1">Full Name</label>
            <input type="text" id="fullName" name="fullName" value={formData.fullName} onChange={handleChange} className="w-full px-3 py-2 border rounded-md bg-gray-700 text-white" />
          </div>
          <div className="mb-4">
            <label htmlFor="email" className="block text-sm font-semibold mb-1">Email</label>
            <input type="email" id="email" name="email" value={formData.email} onChange={handleChange} className="w-full px-3 py-2 border rounded-md bg-gray-700 text-white" />
          </div>
          <div className="mb-4">
            <label htmlFor="password" className="block text-sm font-semibold mb-1">Password</label>
            <input type="password" id="password" name="password" value={formData.password} onChange={handleChange} className="w-full px-3 py-2 border rounded-md bg-gray-700 text-white" />
          </div>
          <button type="submit" className="w-full py-2 px-4 bg-blue-500 text-white rounded-md hover:bg-blue-600">Sign Up</button>
        </form>
        <p className="text-sm mt-4">Already have an account? <Link href="/auth/login" className="text-blue-400 cursor-pointer">Login</Link></p>
      </div>
    </motion.div>
  );
};

export default Signup;
