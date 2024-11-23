import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';

import api from '../api.js'



const OfferDetail = () => {
    const { id } = useParams();  // Get the UUID from the URL
    const [offer, setOffer] = useState(null);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        api
            .get('/offers/' + id)
            .then(response => {
                setOffer(response.data);
                setLoading(false);
            })
            .catch(error => {
                console.error("There was an error fetching the offer!", error);
            });
    }, [id]);

    if (loading) {
        return <div>Loading...</div>;
    }

    if (!offer) {
        return <div>Offer not found</div>;
    }

    return (
        <header className="App-header">
            <div className="container mt-5">
                <h1>{offer.title}</h1>
                <p>{offer.description}</p>
                <p><strong>Price:</strong> ${offer.price}</p>
                {offer.image && <img src={offer.image} alt={offer.title} />}
            </div>
        </header>
    );
};

export default OfferDetail;
