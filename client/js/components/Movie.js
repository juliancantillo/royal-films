import React from 'react';

export default class Movie extends React.Component {
  static propTypes = {
    name: React.PropTypes.string,
    showtimes: React.PropTypes.array,
  };

  constructor(props) {
    super(props);
  }

  render() {

  	let showtimesList = this.props.showtimes.map((showtime, idx) => {
  		return (
  			<a className="btn btn-sm btn-link" key={idx}>{showtime.time}</a>
			);
  	});

		return (
			<li className="list-group-item">
				<h5 className="list-group-item-heading">{ this.props.name }</h5>
	    	<div className="list-group-item-text">
	    		{showtimesList}
	    	</div>
			</li>
		);
  }
}

