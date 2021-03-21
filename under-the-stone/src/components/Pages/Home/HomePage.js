import React, { Component } from 'react';
import { useState } from "react";
import { render } from "react-dom";

export const HomePage = (props) => {

    return (
        <div>
            <div style={{
                backgroundImage: `url(${process.env.PUBLIC_URL + 'main-page.jpg'})`,
                backgroundSize: 'cover',
                backgroundRepeat: 'no-repeat',
                width: '100vw',
                height: '100vh',
                opacity: '86%'
            }}></div>
            <h1>HOME  PAGE</h1>
        </div>

    );

};

