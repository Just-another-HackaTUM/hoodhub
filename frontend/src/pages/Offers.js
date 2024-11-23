import '../App.css';
import React, { useState, useEffect } from 'react';
import { Card, Container, Row, Col } from 'react-bootstrap';
import api from '../api.js';

import { offers } from '../tempdata/data.js';
import { getImageUrl } from '../tempdata/utils.js';



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
        // const response = await api.get("/offers/");
        // console.log(response.data); // Log the response data
        // return response.data; // Return only the data, not the whole response
    };




    return (

        <div className="Offers">
            <header className="App-header">

                <Container className="mt-4">
                    <Row>
                        {offers.length > 0 ? (
                            offers.map(item => (
                                <Col key={item.id} sm={12} md={6} lg={4} className="mb-4">
                                    <Card>
                                        <Card.Img variant="top" src='https://media.istockphoto.com/id/1147544807/de/vektor/miniaturbild-vektorgrafik.jpg?s=612x612&w=0&k=20&c=IIK_u_RTeRFyL6kB1EMzBufT4H7MYT3g04sz903fXAk=' alt={item.title} />
                                        <Card.Body>
                                            <Card.Title>{item.title}</Card.Title>
                                            <Card.Text>{item.description}</Card.Text>
                                            <Card.Text><strong>Price: {item.price} €</strong></Card.Text>
                                        </Card.Body>
                                    </Card>
                                </Col>
                            ))
                        ) : (
                            <p>Loading offers...</p>
                        )}
                    </Row>
                </Container>

            </header>
        </div>
    );
}

export default Offers;
