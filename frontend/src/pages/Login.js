import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';

import '../App.css';
import api from '../api.js'



function Login({ currentUser, setCurrentUser, email, setEmail, username, setUsername, password, setPassword }) {


    function submitLogin(e) {
        e.preventDefault();
        api.post(
            '/login/',
            {
                email: email,
                password: password
            }
        ).then(function (res) {
            setCurrentUser(true);
        });
    }




    return (
        <header className="App-header">
            <h2>Log in with your Account!</h2>
            <div className="center mt-5">
                <Form onSubmit={e => submitLogin(e)}>
                    <Form.Group className="mb-3" controlId="formBasicEmail">
                        <Form.Label>Email address</Form.Label>
                        <Form.Control type="email" placeholder="Enter email" value={email} onChange={e => setEmail(e.target.value)} />
                        <Form.Text style={{ color: '#E2DFD2' }}>
                            We'll never share your email with anyone else.
                        </Form.Text>
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

export default Login;