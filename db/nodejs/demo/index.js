const express = require('express');
const path = require('path');
const members = require('./Members');
const moment = require('moment');
const logger = require('./middleware/logger');

// Init express
const app = express();


const PORT= process.env.PORT || 5000;

// Init middleware
app.use(logger);

// Creating a route. It gets all members 
app.get('/api/members', (req, res) => res.json(members));

// Listen on port
app.listen(PORT, ()=> console.log(`Server started on port ${PORT}`));


// Setting static folder with middleware.
app.use(express.static(path.join(__dirname, 'public')));
 



