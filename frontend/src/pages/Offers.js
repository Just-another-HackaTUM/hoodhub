import '../App.css';
import React, { useState, useEffect } from 'react';
import api from '../api.js'



function Offers() {


    const [response, setResponse] = useState('');


    useEffect(() => {
        const fetchData = async () => {
          const data = await fetchResponse();
          setResponse(data); // Update state with the fetched data
        };
        fetchData(); // Call fetchData on mount
      }, []);



    const fetchResponse = async () => {
        try {
            const response = api.get("/offers")

            return response.data
        } catch (e) {
            return "Mocked offers get index"
        }
    }



    return (
      <div className="Offers">
        <header className="App-header">
          <p>
          Offers example page!!!
          </p>


          <h2> {response} </h2>


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