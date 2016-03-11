import React from 'react';
import Movie from './Movie'

export default class MoviesList extends React.Component {
  static propTypes = {
    movies: React.PropTypes.array,
  };

  constructor(props) {
    super(props);

    this.props = {
    	movies: []
    }
  }

  render() {

  	let movieList = this.props.movies.map((movie) => {
			return (<Movie key={movie.uuid} movie={movie.movie} groups={movie.group}/>);
		});

    return (
			<ul className="list-group list-group-flush">
				{movieList}
			</ul>
    );
  }
}
