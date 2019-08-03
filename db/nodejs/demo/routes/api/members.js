const express = require('express');
const router = express.Router();
const members = require('../../Members');
const uuid = require('uuid');



// Creating a route. It gets all members 
router.get('/', (req, res) => res.json(members));

// Get single Member
router.get('/:id', (req, res) => {
    const found = members.some(member => member.id === parseInt(req.params.id));

    if (found) {
        res.json(members.filter(member => member.id === parseInt(req.params.id)));
    } else {
       res.status(404).json({ msg: `No member with the id: ${req.params.id}`});
    }
})

// Create member
router.post('/', (req, res) => {
    const newMember = {
      id: uuid.v4(),
      name: req.body.name,
      email: req.body.email, 
      status: 'active'
    }; 
    if (!newMember.name || !newMember.email) {
       return res.status(404).json({msg: 'Please fill out name and email'}); 
    } 
    members.push(newMember);
    res.json(members); 
});

// Update member
router.put('/:id', (req, res) => {
    const found = members.some(member => member.id === parseInt(req.params.id));
    if (found) {
       const updMember = req.body;
       members.forEach(member => {
          if(member.id === parseInt(req.params.id)) {
             member.name = updMember.name ? updMember.name : member.name;
             member.email = updMember.email ? updMember.email : member.email;
          }
       } 
    } else {
        res.status(404).json({msg: 'No member with the id of ${req.params.id}'});
    }
});
A
A
B
A
B
A
B
B
B
A
});

module.exports=router 



