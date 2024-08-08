const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');

const app = express();

// Body parser middleware
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

// Connect to MongoDB
mongoose.connect('mongodb://localhost:27017/gym_database', { useNewUrlParser: true, useUnifiedTopology: true })
  .then(() => console.log('MongoDB Connected'))
  .catch(err => console.log(err));

// Create schema
const memberSchema = new mongoose.Schema({
  name: String,
  email: String,
  gender: String,
  dob: Date,
  phone: String
});

// Create model
const Member = mongoose.model('Member', memberSchema);

// POST endpoint to handle form submission
app.post('/join_gym', (req, res) => {
  const newMember = new Member({
    name: req.body.name,
    email: req.body.email,
    gender: req.body.gender,
    dob: req.body.dob,
    phone: req.body.phone
  });

  newMember.save()
    .then(member => res.json({ message: 'Member added successfully', member }))
    .catch(err => res.status(500).json({ message: 'Failed to add member', error: err }));
});

const PORT = process.env.PORT || 3000;

app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
