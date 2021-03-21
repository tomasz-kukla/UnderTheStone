import React from 'react';
import ReactDOM from 'react-dom';

import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link,
  Redirect,
} from "react-router-dom";


import { HomePage } from './components/Pages/Home/HomePage';
import { BookingPage } from './components/Pages/Booking/BookingPage';
import { AboutPage } from './components/Pages/About/AboutPage';
import { MenuPage } from './components/Pages/Menu/MenuPage';


const rootElement = document.getElementById('root');

ReactDOM.render(
  <Router>
    <Switch>
      <Route exact path='/' component={HomePage} />
      <Route exact path='/booking' component={BookingPage} />
      <Route exact path='/menu' component={MenuPage} />
      <Route exact path='/about' component={AboutPage} />
    </Switch>
  </Router>,

  rootElement);

