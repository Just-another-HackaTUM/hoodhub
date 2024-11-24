import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { offers } from '../tempdata/data.js';

const OfferDetail = () => {
    const { identifier } = useParams(); // `identifier` will be a string
    const offer = offers.find(offer => offer.identifier === parseInt(identifier));

    if (!offer) {
        return <div>Loading...</div>;
    }

    return (
        <header className="App-header">
            <div className="container mt-5">
                <h1>{offer.title}</h1>
                <p>{offer.description}</p>
                <p>Price: {offer.price} €</p>
                <p>Location: {offer.location}</p>
                <p>Start Date: {new Date(offer.start_date).toLocaleDateString()}</p>
                <p>End Date: {new Date(offer.end_date).toLocaleDateString()}</p>
            </div>
        </header>
    );
};

export default OfferDetail;