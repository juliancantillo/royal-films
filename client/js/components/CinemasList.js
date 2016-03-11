import React from 'react';
import Cinema from './Cinema'

export default class CinemasList extends React.Component {
  static propTypes = {
    cinemas: React.PropTypes.array,
  };

  constructor(props) {
    super(props);

    this.props = {
      cinemas: []
    }
  }

  render() {

  	let cinemaList = this.props.cinemas.map((showtimes) => {
			return (<Cinema key={showtimes.cinema.uuid} name={showtimes.cinema.name} groups={showtimes.group}/>);
		});

    return (
			<ul className="list-group list-group-flush">
				{cinemaList}
			</ul>
    );
  }
}
