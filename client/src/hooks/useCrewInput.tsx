import axios from "axios";
import toast from "react-hot-toast";
import { useState, useEffect } from "react";

export type EventType = {
  data: string;
  timestamp: string;
};

export type NamedUrl = {
  name: string;
  url: string;
};

export type PositionInfo = {
  company: string;
  position: string;
  name: string;
  blog_articles_urls: string[];
  youtube_interviews_urls: NamedUrl[];
};


const useCrewInput = () => {
  const [productIdea, setProductIdea] = useState<string>("");
  const [momma, setMomma] = useState<string>("");
  const [running, setRunning] = useState<boolean>(false);
  const [events, setEvents] = useState<EventType[]>([]);
  const [positionInfoList, setPositionInfoList] = useState<PositionInfo[]>([]);
  const [result, setResult] = useState<string | null>(null);
  const [CurrentReqId, setCurrentReqId] = useState<string>("");
  const [responseResult,setResponseResult] = useState<string | null>(null);
  useEffect(() => {
    let intervalId: any;

    const fetchJobStatus = async () => {
      try {
        const response = await axios.get<{
          status: string;
          result: string;
          events: EventType[];
        }>(`http://127.0.0.1:5000/api/crew/${CurrentReqId}`);
        const { status, events: fetchedEvents, result } = response.data;
    
        console.log("API Response:", response.data);
        console.log(response.data.result) // Add this line
        setResponseResult(response.data.result) // Add this line
        setEvents(fetchedEvents);
        setResult(result);

        if (status === "COMPLETE" || status === "ERROR") {
          if (intervalId) {
            clearInterval(intervalId);
          }
          setRunning(false);
          toast.success(`Job ${status.toLowerCase()}.`);
        }
      } catch (error) {
        if (intervalId) {
          clearInterval(intervalId);
        }
        setRunning(false);
        toast.error("Failed to get job status.");
        console.error(error);
      }
    };

    if (CurrentReqId !== "") {
      intervalId = setInterval(fetchJobStatus, 1000);
    }

    return () => {
      if (intervalId) {
        clearInterval(intervalId);
      }
    };
  }, [CurrentReqId]);
  const startJob = async () => {
    setEvents([]);
    setPositionInfoList([]);
    setRunning(true);
    try {
      const response = await axios.post<{ req_id: string }>(
        "http://127.0.0.1:5000/input",
        {
          productIdea,
          momma,
        }
      );
      toast.success("req started");
      console.log("request id", response.data.req_id);
      setCurrentReqId(response.data.req_id);
    } catch (error) {
      toast.error("Failed to start job");
      console.error(error);
      setCurrentReqId("");
    }
  };

  return {
    productIdea,
    setProductIdea,
    momma,
    setMomma,
    startJob,
    events,    
    result,
    positionInfoList,
    responseResult
  };
};

export default useCrewInput;