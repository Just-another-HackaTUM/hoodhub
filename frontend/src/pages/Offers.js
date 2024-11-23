import '../App.css';
import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { Form, Card, Container, Row, Col } from 'react-bootstrap';
import api from '../api.js';

import { offers } from '../tempdata/data.js';
import { getImageUrl } from '../tempdata/utils.js';



function Offers() {
    const [response, setResponse] = useState([]);
    const [filter, setFilter] = useState({
        category: '',
        priceRange: '',
        sortBy: '',
    });

    
    const handleFilterChange = (e) => {
        const { name, value } = e.target;
        setFilter((prevFilter) => ({
            ...prevFilter,
            [name]: value,
        }));
    };

    /* 
    const filteredOffers = offers.filter((item) => {
        if (filter.category && item.category !== filter.category) {
            return false;
        }

        if (filter.priceRange && !(item.price >= filter.priceRange.split('-')[0] && item.price <= filter.priceRange.split('-')[1])) {
            return false;
        }

        return true;
    }); */



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
                {/* Floating Filter Bar */}
                <div className="floating-filter-bar">
                    <Form>
                        <Row>
                            <Col sm={12} md={4}>
                                <Form.Group controlId="category">
                                    <Form.Label>Category</Form.Label>
                                    <Form.Control
                                        as="select"
                                        name="category"
                                        value={filter.category}
                                        onChange={handleFilterChange}
                                    >
                                        <option value="">All Categories</option>
                                        <option value="electronics">Electronics</option>
                                        <option value="clothing">Clothing</option>
                                        <option value="home">Home</option>
                                    </Form.Control>
                                </Form.Group>
                            </Col>

                            <Col sm={12} md={4}>
                                <Form.Group controlId="priceRange">
                                    <Form.Label>Price Range</Form.Label>
                                    <Form.Control
                                        as="select"
                                        name="priceRange"
                                        value={filter.priceRange}
                                        onChange={handleFilterChange}
                                    >
                                        <option value="">Any Price</option>
                                        <option value="0-50">0 - 50</option>
                                        <option value="50-100">50 - 100</option>
                                        <option value="100-500">100 - 500</option>
                                    </Form.Control>
                                </Form.Group>
                            </Col>

                            <Col sm={12} md={4}>
                                <Form.Group controlId="sortBy">
                                    <Form.Label>Sort By</Form.Label>
                                    <Form.Control
                                        as="select"
                                        name="sortBy"
                                        value={filter.sortBy}
                                        onChange={handleFilterChange}
                                    >
                                        <option value="">Select</option>
                                        <option value="price-asc">Price: Low to High</option>
                                        <option value="price-desc">Price: High to Low</option>
                                    </Form.Control>
                                </Form.Group>
                            </Col>
                        </Row>
                    </Form>
                </div>




                { /* Display Offers */ }
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
                                            <Card.Footer style={{ fontSize: '15px', padding: '8px', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                                                <span>
                                                    📅 {new Date(item.start_date).toLocaleDateString('en-GB', {
                                                        weekday: 'long', // Day of the week
                                                        year: 'numeric', // Year
                                                        month: 'long', // Full month name
                                                        day: 'numeric', // Day of the month
                                                    })}
                                                </span>
                                                <span>{item.location.length > 20 ? item.location.slice(0, 20) + '...' : item.location}</span>
                                            </Card.Footer>
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
