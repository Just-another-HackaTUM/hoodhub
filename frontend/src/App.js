import './App.css';
import ReactDOM from "react-dom/client";
import { BrowserRouter, Routes, Route } from "react-router-dom";

import React, { useState, useEffect } from 'react';



import 'bootstrap/dist/css/bootstrap.min.css';
import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import NavDropdown from 'react-bootstrap/NavDropdown';
import { Link } from 'react-router-dom';


import api from './api.js'

import Home from './pages/Home';
import Offers from './pages/Offers';
import Login from './pages/Login';
import Register from './pages/Register';
import OfferDetail from './pages/OfferDetail'
import OfferCreate from './pages/OfferCreate'



function IsLoggedIn({ currentUser }) {
  if (currentUser) {
    return <Navbar.Collapse className="justify-content-end">
      <Navbar.Text>
        Signed in as <Link to="/ifCurrentUser">Markus</Link> | <Link to="/ifCurrentUserLogOut">Log Out</Link>
      </Navbar.Text>
    </Navbar.Collapse>
  } else {
    return <Navbar.Collapse className="justify-content-end">
      <Navbar.Text>
        Not Signed in | <Link to="/register"> Register</Link> | <Link to="/login">Log In</Link>
      </Navbar.Text>
    </Navbar.Collapse>
  }
}



export default function App() {

  const [currentUser, setCurrentUser] = useState();
  // const [registrationToggle, setRegistrationToggle] = useState(false);
  const [email, setEmail] = useState('');
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');



  useEffect(() => {
    api.get("/user/")
      .then(function (res) {
        setCurrentUser(true);
      })
      .catch(function (error) {
        setCurrentUser(false);
      });
  }, []);





  return (
    <BrowserRouter>


      <Navbar expand="lg" className="bg-body-tertiary">
        <Container>
          <Navbar.Brand as={Link} to="/home">hoodhub</Navbar.Brand>
          <Navbar.Toggle aria-controls="basic-navbar-nav" />
          <Navbar.Collapse id="basic-navbar-nav">
            <Nav className="me-auto">
              <Nav.Link as={Link} to="/home">Home</Nav.Link>
              <Nav.Link as={Link} to="/offers">Offers</Nav.Link>
              <Nav.Link as={Link} to="/offers/create">Create</Nav.Link>
              <NavDropdown title="Dropdown" id="basic-nav-dropdown">
                <NavDropdown.Item href="#action/3.1">Action</NavDropdown.Item>
                <NavDropdown.Item href="#action/3.2">
                  Another action
                </NavDropdown.Item>
                <NavDropdown.Item href="#action/3.3">Something</NavDropdown.Item>
                <NavDropdown.Divider />
                <NavDropdown.Item href="#action/3.4">
                  Separated link
                </NavDropdown.Item>
              </NavDropdown>
            </Nav>
          </Navbar.Collapse>

          <IsLoggedIn currentUser={currentUser} />


        </Container>
      </Navbar>




      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/home" element={<Home />} />

        <Route path="/offers" element={<Offers />} />
        <Route path="/offers/create" element={<OfferCreate />} />
        <Route path="/offers/:identifier" element={<OfferDetail />} />

        <Route path="/login" element={<Login
          currentUser={currentUser}
          setCurrentUser={setCurrentUser}
          email={email}
          setEmail={setEmail}
          username={username}
          setUsername={setUsername}
          password={password}
          setPassword={setPassword} />} />

        <Route path="/register" element={<Register
          currentUser={currentUser}
          setCurrentUser={setCurrentUser}
          email={email}
          setEmail={setEmail}
          username={username}
          setUsername={setUsername}
          password={password}
          setPassword={setPassword} />} />

      </Routes>
    </BrowserRouter>
  );
}


const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<App />);