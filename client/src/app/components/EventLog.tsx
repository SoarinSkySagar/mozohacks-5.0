import React, {useState} from "react";
import { Event } from "../../types";
import { EventType } from "../../hooks/useCrewInput";
import responseResult from "../../hooks/useCrewInput";

export const EventLog: React.FC<{}> = ({  }) => {
  return (
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
            </div>
  );  
          }
