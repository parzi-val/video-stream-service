// models/User.js
const mongoose = require('mongoose');

const userSchema = new mongoose.Schema({
  username: { type: String, required: true, unique: true },
  password: { type: String, required: true },  // You'd want to hash passwords in production
  email: { type: String, required: true, unique: true },
  friends: [{ type: mongoose.Schema.Types.ObjectId, ref: 'User' }],  // Array of friend IDs
  onlineStatus: { type: Boolean, default: false },  // Online/Offline status
});

const User = mongoose.model('User', userSchema);

module.exports = User;
