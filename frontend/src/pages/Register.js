import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
import React, { useState, useEffect } from 'react';

import '../App.css';
import api from '../api.js'





function Register({ currentUser, setCurrentUser, email, setEmail, username, setUsername, password, setPassword }) {

    const [confirmpassword, setConfirmpassword] = useState('');
    const [hasInteracted, setHasInteracted] = useState(false);
    const [passwordError, setPasswordError] = useState('');


    function submitRegistration(e) {

        e.preventDefault();

        if (!(password === confirmpassword)) {
            setPasswordError('Passwords do not match!');
            return;
        }

        api.post(
            "/api/register",
            {
                email: email,
                username: username,
                password: password
            }
        ).then(function (res) {
            api.post(
                "/api/login",
                {
                    email: email,
                    password: password
                }
            ).then(function (res) {
                setCurrentUser(true);
            });
        });
    }



    const handleConfirmPasswordChange = (e) => {
        setConfirmpassword(e.target.value);
        setHasInteracted(true);
    };


    return (
        <header className="App-header">
            <h2>Register a new User to the App!</h2>
            <div className="center mt-4">
                <Form onSubmit={e => submitRegistration(e)}>
                    <Form.Group className="mb-1" controlId="formBasicEmail">
                        <Form.Label>Email address</Form.Label>
                        <Form.Control type="email" placeholder="Enter email" value={email} onChange={e => setEmail(e.target.value)} />
                        <Form.Text style={{ color: '#E2DFD2' }}>
                            We'll never share your email with anyone else.
                        </Form.Text>
                    </Form.Group>
                    <Form.Group className="mb-4" controlId="formBasicUsername">
                        <Form.Label>Username</Form.Label>
                        <Form.Control type="text" placeholder="Enter username" value={username} onChange={e => setUsername(e.target.value)} />
                    </Form.Group>
                    <Form.Group className="mb-1" controlId="formBasicPassword">
                        <Form.Label>Password</Form.Label>
                        <Form.Control type="password" placeholder="Enter password" value={password} onChange={e => setPassword(e.target.value)} />
                    </Form.Group>

                    <Form.Group className="mb-3" controlId="formBasicPassword">
                        <Form.Label>Confirm Password</Form.Label>
                        <Form.Control type="password" placeholder="Confirm password" value={confirmpassword} onChange={e => handleConfirmPasswordChange(e)} />
                        {hasInteracted && password !== confirmpassword && (
                            <Form.Text className="text-danger">
                                Passwords do not match.
                            </Form.Text>
                        )}
                    </Form.Group>

                    <Button variant="primary" type="submit">
                        Submit
                    </Button>
                </Form>
            </div>
        </header>
    );
}

export default Register;