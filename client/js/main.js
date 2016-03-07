import React from 'react';
import ReactDOM from 'react-dom';
import ShowtimesForm from './components/ShowtimesForm'
import MovieShowtimes from './components/MovieShowtimes'

window.app = {
	init(opts = {el: null, movie: null }) {
		let mountPoint = document.querySelector(opts.el);
		ReactDOM.render(<ShowtimesForm movie={opts.movie}/>, mountPoint);
	},
	movieDetail(opts = {el: null, movie: null }) {
		let mountPoint = document.querySelector(opts.el);
		ReactDOM.render(<MovieShowtimes movie={opts.movie}/>, mountPoint);
	}
}

