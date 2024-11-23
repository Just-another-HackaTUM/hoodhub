import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';

import '../App.css';
import api from '../api.js'





function Register({ currentUser, setCurrentUser, email, setEmail, username, setUsername, password, setPassword }) {

    function submitRegistration(e) {
        e.preventDefault();
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



    return (
        <header className="App-header">
            <h2>Register a new User to the App!</h2>
            <div className="center mt-5">
                <Form onSubmit={e => submitRegistration(e)}>
                    <Form.Group className="mb-3" controlId="formBasicEmail">
                        <Form.Label>Email address</Form.Label>
                        <Form.Control type="email" placeholder="Enter email" value={email} onChange={e => setEmail(e.target.value)} />
                        <Form.Text style={{ color: '#E2DFD2' }}>
                            We'll never share your email with anyone else.
                        </Form.Text>
                    </Form.Group>
                    <Form.Group className="mb-3" controlId="formBasicUsername">
                        <Form.Label>Username</Form.Label>
                        <Form.Control type="text" placeholder="Enter username" value={username} onChange={e => setUsername(e.target.value)} />
                    </Form.Group>
                    <Form.Group className="mb-3" controlId="formBasicPassword">
                        <Form.Label>Password</Form.Label>
                        <Form.Control type="password" placeholder="Password" value={password} onChange={e => setPassword(e.target.value)} />
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