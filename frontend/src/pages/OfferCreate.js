import React, { useState, useEffect } from 'react';
import { Container, Row, Col, Form, Button } from 'react-bootstrap';

import '../App.css';
import api from '../api.js'



function OfferCreate({ currentUser, setCurrentUser, email, setEmail, username, setUsername, password, setPassword }) {


    const [title, setTitle] = useState('');
    const [description, setDescription] = useState('');
    const [location, setLocation] = useState('');
    const [price, setPrice] = useState('');
    const [type, setType] = useState('');
    const [startDate, setStartDate] = useState('');


    function submitOffer(e) {
        e.preventDefault();
        api.post(
            '/offers/',
            {
                title: email
            }
        ).then(function (res) {
            setCurrentUser(true);
        });
    }




    return (
        <header className="App-header">
            <h2 className="mt-5">Post your very own Offer!</h2>
            <Container fluid="md" className="mt-4">
                <Row className="justify-content-center">
                    <Col md={8} lg={6} xl={5}>
                        <Form onSubmit={submitOffer}>
                            {/* Title Input */}
                            <Form.Group className="mb-3" controlId="formTitle">
                                <Form.Label>Title</Form.Label>
                                <Form.Control
                                    type="text"
                                    placeholder="Enter offer title"
                                    value={title}
                                    onChange={(e) => setTitle(e.target.value)}
                                />
                            </Form.Group>

                            {/* Description Input */}
                            <Form.Group className="mb-3" controlId="formDescription">
                                <Form.Label>Description</Form.Label>
                                <Form.Control
                                    as="textarea"
                                    rows={4}  // You can change the row count to make the textarea larger
                                    placeholder="Enter offer description"
                                    value={description}
                                    onChange={(e) => setDescription(e.target.value)}
                                />
                            </Form.Group>

                            {/* Location Input */}
                            <Form.Group className="mb-3" controlId="formLocation">
                                <Form.Label>Location</Form.Label>
                                <Form.Control
                                    type="text"
                                    placeholder="Enter location"
                                    value={location}
                                    onChange={(e) => setLocation(e.target.value)}
                                />
                            </Form.Group>

                            {/* Price Input */}
                            <Form.Group className="mb-3" controlId="formPrice">
                                <Form.Label>Price</Form.Label>
                                <Form.Control
                                    type="number"
                                    placeholder="Enter price"
                                    value={price}
                                    onChange={(e) => setPrice(e.target.value)}
                                />
                            </Form.Group>

                            {/* Type Dropdown */}
                            <Form.Group className="mb-3" controlId="formType">
                                <Form.Label>Type</Form.Label>
                                <Form.Control
                                    as="select"
                                    value={type}
                                    onChange={(e) => setType(e.target.value)}
                                    className='custom-select'
                                >
                                    <option value="">Select type</option>
                                    <option value="sale">Sale</option>
                                    <option value="rent">Rent</option>
                                    <option value="wanted">Wanted</option>
                                    <option value="event">Event</option>
                                    <option value="conversation">Conversation</option>
                                </Form.Control>
                            </Form.Group>

                            {/* Start Date Picker */}
                            <Form.Group className="mb-4" controlId="formStartDate">
                                <Form.Label>Start Date</Form.Label>
                                <Form.Control
                                    type="date"
                                    value={startDate}
                                    onChange={(e) => setStartDate(e.target.value)}
                                />
                            </Form.Group>

                            {/* Submit Button */}
                            <Button variant="primary" type="submit" className="mb-5">
                                Submit
                            </Button>
                        </Form>
                    </Col>
                </Row>
            </Container>
        </header >
    );
}

export default OfferCreate;