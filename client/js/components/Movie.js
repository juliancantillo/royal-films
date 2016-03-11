import React from 'react';

export default class Movie extends React.Component {
  static propTypes = {
    movie: React.PropTypes.object,
    groups: React.PropTypes.array,
  };

  constructor(props) {
    super(props);
  }

  render() {

  	let showtimesList = this.props.groups.map((group, index) => {

      let showtimes = group.showtimes.map(function(elem, idx) {
        return(
          <a className="btn btn-sm btn-link" key={idx}>{elem.time}</a>
          );
      })

  		return (
        <div className="list-group-item-text" key={index}>
          {showtimes}
        </div>
			);
  	});

		return (
			<li className="list-group-item">
				<h5 className="list-group-item-heading">{ this.props.movie.title }</h5>
        <div className="list-group-item-text">
          <span className="label label-default">{ this.props.movie.runtime }</span>
          <a className="pull-xs-right" href={ this.props.movie.url }>Details</a>
        </div>
        {showtimesList}
			</li>
		);
  }
}

