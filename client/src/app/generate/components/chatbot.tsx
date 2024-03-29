"use client"
import React, { useState } from "react";
import { motion } from "framer-motion";
import { NavbarDemo } from "../../components/Navbar/Navbar";
import { useForm } from "react-hook-form";
import useCrewInput, { PositionInfo } from "../../../hooks/useCrewInput";
import responseResult from "../../../hooks/useCrewInput";
import { EventLog } from "../../components/EventLog";

const transition = {
  type: "spring",
  mass: 0.5,
  damping: 11.5,
  stiffness: 100,
  restDelta: 0.001,
  restSpeed: 0.001,
};

const ChatbotPage = () => {
  const [history, setHistory] = useState<string[]>([]);
  const { register, handleSubmit, reset } = useForm();
  const [output1, setOutput1] = useState<string>('');
  const [output2, setOutput2] = useState<string>('');
  const [output3, setOutput3] = useState<string>('');
  const crewInput = useCrewInput();
  const [positionInfoList, setPositionInfoList] = useState<PositionInfo[]>([]);
  // const onSubmit = async (data: any) => {
  //   try {
  //     const response = await fetch("/api/chatbot", {
  //       method: "POST",
  //       headers: {
  //         'Content-Type': 'application/json'
  //       },
  //       body: JSON.stringify({ input1: crewInput.productIdea, input2: crewInput.momma })
  //     });

  //     if (response.ok) {
  //       const responseData = await response.json();
  //       console.log(responseData);
  //       setHistory([...history, `${crewInput.productIdea} ${crewInput.momma} ${data.input3}`]);
  //       reset();
  //     } else {
  //       console.log("Error:", response.status);
  //     }
  //   } catch (error) {
  //     console.error("Error:", error);
  //   }
  // };

  return (
    <div className="bg-black min-h-screen">
      <NavbarDemo />
      <div className="flex h-screen">
        {/* Sidebar */}
        <div className="w-1/4 bg-slate-900 p-4 text-gray-300">
          <h2 className="text-xl font-bold mb-4 text-gray-400">Previous Chats</h2>
          <ul>
            {history.map((item, index) => (
              <li key={index} className="p-2 rounded-md bg-slate-800 mb-2 cursor-pointer hover:bg-slate-700">
                {item}
              </li>
            ))}
          </ul>
        </div>
        {/* Main Content */}
        <div className="flex flex-col flex-grow p-8 text-gray-300">
          {/* Introductory Header */}
          <motion.div
            initial={{ opacity: 0, y: -20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={transition}
            className="mb-8 pt-24"
          >
            <h1 className="text-4xl font-bold text-gray-400">Welcome to ChatBot</h1>
            <p className="text-xl text-gray-500">
              Ask me anything, and I will do my best to provide you with helpful information.
            </p>
          </motion.div>
          <div className="flex-grow overflow-y-auto">
          </div>
          <div className="mt-4">
            <div className="flex">
              <div className="flex-grow mr-4">
                <input
                  {...register("input1")}
                  className="w-full p-2 bg-slate-800 text-gray-300 border border-slate-700 rounded-xl focus:outline-none focus:ring-2 focus:ring-slate-600"
                  placeholder="What do you want to build"
                  value={crewInput.productIdea}
                  onChange={(e) => crewInput.setProductIdea(e.target.value)}
                />
              </div>
              <div className="flex-grow mr-4">
                <input
                  {...register("input2")}
                  className="w-full p-2 bg-slate-800 text-gray-300 border border-slate-700 rounded-xl focus:outline-none focus:ring-2 focus:ring-slate-600"
                  placeholder="Provide me the project idea"
                  value={crewInput.momma}
                  onChange={(e) => crewInput.setMomma(e.target.value)}
                />
              </div>
              
              <button
                type="submit"
                className="px-4 py-2 bg-slate-600 text-gray-300 rounded-xl hover:bg-slate-500"
                onClick={crewInput.startJob}
              >
                Send
              </button>
            </div>
          </div>
          <div className="flex mt-8">
          <div className="w-1/2 p-4 bg-slate-800 rounded-2xl">
          <h2 className="text-2xl font-bold mb-2 text-gray-400">Output</h2>
          {positionInfoList.map((position, index) => (
            <div key={index} className="p-2 rounded-md bg-slate-700 mb-2">
              <p>Name: {position.name}</p>
              <p>Company: {position.company}</p>
              <p>Position: {position.position}</p>
              <h3 className="text-lg font-bold mt-2 text-gray-400">Blog Articles</h3>
              <ul>
                {position.blog_articles_urls.map((url, index) => (
                  <li key={index}>{url}</li>
                ))}
              </ul>
              <h3 className="text-lg font-bold mt-2 text-gray-400">YouTube Interviews</h3>
              <ul>
                {position.youtube_interviews_urls.map((namedUrl, index) => (
                  <li key={index}>
                    <a href={namedUrl.url} target="_blank" rel="noopener noreferrer">
                      {namedUrl.name}
                    </a>
                  </li>
                ))}
              </ul>
            </div>
          ))}
        </div>

        <div className="flex flex-col h-full">
              <h2 className="text-lg font-semibold mb-2">Event Details</h2>
              <div className="flex-grow overflow-auto border-2 border-gray-300 p-2">
                  {/* {events.map((event, index) => (
                    <div key={index} className="p-2 border-b border-gray-200">
                      <p>
                        {event.timestamp}: {event.data}
                      </p>
                    </div>
                  ))} */}
        <div>
          {responseResult && <p>{String(responseResult)}</p>}
        </div>
              </div>
            </div>          </div>
        </div>
      </div>
    </div>
  );
};

export default ChatbotPage;