import '../App.css';
import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
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
                                    <Link to={'/offers/' + item.identifier} style={{ textDecoration: 'none' }}>
                                        <Card className="d-flex h-100">
                                            <Card.Img variant="top"
                                                src='https://media.istockphoto.com/id/1147544807/de/vektor/miniaturbild-vektorgrafik.jpg?s=612x612&w=0&k=20&c=IIK_u_RTeRFyL6kB1EMzBufT4H7MYT3g04sz903fXAk='
                                                alt={item.title}
                                                style={{ height: '250px', objectFit: 'cover' }} />
                                            <Card.Body>
                                                <Card.Title><strong>{item.title}</strong></Card.Title>
                                                <Card.Text>{item.description.length > 80 ? item.description.slice(0, 80) + '...' : item.description}</Card.Text>
                                                <Card.Text>Price: {item.price} €</Card.Text>
                                            </Card.Body>
                                            <Card.Footer style={{ fontSize: '15px', padding: '8px' }}>
                                                📅 {new Date(item.start_date).toLocaleDateString('de-DE', {
                                                    weekday: 'long', // Day of the week
                                                    year: 'numeric', // Year
                                                    month: 'long', // Full month name
                                                    day: 'numeric', // Day of the month
                                                })}</Card.Footer>
                                        </Card>
                                    </Link>
                                </Col>
                            ))
                        ) : (
                            <div className="center-text">
                                <p>There are no offers yet. Feel free to place one yourself 😄!</p>
                            </div>
                        )}
                    </Row>
                </Container>

            </header>
        </div >
    );
}

export default Offers;
