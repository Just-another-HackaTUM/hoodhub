import '../App.css';
import React, { useState, useEffect } from 'react';
import api from '../api.js';

function Offers() {
    const [response, setResponse] = useState([]);

    useEffect(() => {
        const fetchData = async () => {
            const data = await fetchResponse();
            setResponse(data); // Set response with the actual data
        };
        fetchData();
    }, []);

    const fetchResponse = async () => {
        const response = await api.get("/offers/test");
        console.log(response.data); // Log the response data
        return response.data; // Return only the data, not the whole response
    };

    return (
        <div className="Offers">
            <header className="App-header">
                <p>
                    Offers example page!!!
                </p>

                <div>
                    {response.length > 0 ? (
                        response.map(item => (
                            <div key={item.id}>
                                <h2>{item.title}</h2>
                                <p>{item.description}</p>
                            </div>
                        ))
                    ) : (
                        <p>Loading offers...</p> // Show loading if response is still empty
                    )}
                </div>

                <a
                    className="App-link"
                    href="https://reactjs.org"
                    target="_blank"
                    rel="noopener noreferrer"
                >
                    Offers example page!!!
                </a>
            </header>
        </div>
    );
}

export default Offers;
