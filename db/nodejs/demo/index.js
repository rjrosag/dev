const express = require('express');
const path = require('path');
const moment = require('moment');
const logger = require('./middleware/logger');
const exphbs = require('express-handlebars');
const members = require('./Members');

// Init express
const app = express();

// Handlebars Middleware
app.engine('handlebars', exphbs({defaultLayout: 'main'}));
app.set('view engine', 'handlebars');

const PORT= process.env.PORT || 5000;

// Init middleware
app.use(logger);

// Body parser middleware
app.use(express.json());
app.use(express.urlencoded({ extended: false}));

// Homepage route
app.get('/', (req, res) => res.render('index', {
   title: 'Member App', 
   members
}));


// Listen on port
app.listen(PORT, ()=> console.log(`Server started on port ${PORT}`));

// Setting static folder with middleware.
app.use(express.static(path.join(__dirname, 'public')));

// Members api routes
app.use('/api/members', require('./routes/api/members')); 



