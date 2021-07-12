const Ticket = require('../models/ticket');

module.exports = {
    new: newTicket,
    create
};

function newTicket(req, res) {
    res.render('tickets/new', {
        title: 'Add a new ticket',
        flightId: req.params.id
    });
}

function create(req, res) {
    for (let key in req.body) {
        if (req.body[key] === '') delete req.body[key];
    }
    req.body.flight = req.params.id;
    const ticket = new Ticket(req.body);
    ticket.save(function (err) {
        if (err) {
            console.log(err);
            return newTicket(req, res);
        }
        res.redirect(`/flights/show/${req.body.flight}`);
    })
}