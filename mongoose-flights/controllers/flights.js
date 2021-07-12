const Flight = require('../models/flight');
const Ticket = require('../models/ticket');

module.exports = {
    index: index,
    show: show,
    new: newFlight,
    create: create
};

function index(req, res) {
    Flight.find({}, function (err, flights) {
        res.render('flights/index', {
            title: 'All Flights', flights
        });
    });
}

function show(req, res) {
    Flight.findById(req.params.id, function (err, flight) {
        Ticket.find({ flight: flight._id }, function (err, tickets) {
            res.render('flights/show', {
                title: 'Flight Details',
                flight,
                tickets
            });
        });
    });
}

function newFlight(req, res) {
    res.render('flights/new', {
        title: 'Add a flight'
    });
}

function create(req, res) {
    for (let key in req.body) {
        if (req.body[key] === '') delete req.body[key];
    }
    const flight = new Flight(req.body);
    flight.save(function (err) {
        if (err) {
            console.log(err);
            return newFlight(req, res);
        }
        console.log(flight);
        res.redirect('/flights');
    });
}
